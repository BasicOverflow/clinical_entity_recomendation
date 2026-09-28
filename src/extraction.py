"""LangChain entity extraction from SECTION_CONTENT into canonical entities."""

from __future__ import annotations

import os
import re
from typing import Any

from pydantic import BaseModel, Field

from src.config import CORPUS_TAG
from src.graph import connect

ENTITY_TYPES = (
    "INCLUSION_CRITERION",
    "EXCLUSION_CRITERION",
    "OBJECTIVE",
    "ENDPOINT",
    "INTERVENTION",
    "ASSESSMENT",
)
KEYWORDS = ("eligib", "inclusion", "exclusion", "endpoint", "objective", "intervention", "assessment", "dose", "outcome")


class Mention(BaseModel):
    entity_type: str
    name: str = Field(description="Short canonical name reusable across studies, under 12 words")
    span: str


class MentionBatch(BaseModel):
    mentions: list[Mention]


def build_chat_model():
    """OpenAI-compatible LangChain chat model.

    Set ``LLM_API_KEY``, optional ``LLM_BASE_URL`` (a local or hosted server), and optional ``LLM_MODEL``.
    """
    from dotenv import load_dotenv
    from pathlib import Path

    load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)
    key = os.getenv("LLM_API_KEY")
    if not key:
        raise RuntimeError("Set LLM_API_KEY before calling the chat model. LLM_BASE_URL is optional.")
    from langchain_openai import ChatOpenAI

    kwargs = {"model": os.getenv("LLM_MODEL") or "gpt-4o-mini", "temperature": 0, "api_key": key}
    if os.getenv("LLM_BASE_URL"):
        kwargs["base_url"] = os.getenv("LLM_BASE_URL")
    return ChatOpenAI(**kwargs)


def _prompt():
    from langchain_core.prompts import ChatPromptTemplate

    return ChatPromptTemplate.from_messages([
        ("system",
         "You extract clinical protocol design entities. "
         "Use only these types: INCLUSION_CRITERION, EXCLUSION_CRITERION, OBJECTIVE, ENDPOINT, INTERVENTION, ASSESSMENT. "
         "Return short canonical names that would match the same idea in another study, such as 'Adults 18 years or older' or 'Change in PASI score'. "
         "Skip boilerplate, page numbers, and administrative text. Return at most 8 mentions."),
        ("human", "Section title: {title}\n\n{text}"),
    ])


def extraction_chain(model):
    return _prompt() | model.with_structured_output(MentionBatch)


def normalize_name(name: str) -> str:
    cleaned = re.sub(r"\s+", " ", name or "").strip(" .:-")
    return cleaned[:180]


def sections_to_extract(per_study: int = 10) -> list[dict]:
    driver, settings = connect()
    query = """
    MATCH (s:STUDY {corpus: $corpus})-[:HAS_DOCUMENT]->(:PROTOCOL)-[:HAS_CONTENT]->(c:SECTION_CONTENT)
    WHERE c.text IS NOT NULL AND size(c.text) > 80
    RETURN s.name AS study_id, c.section_id AS section_id, c.name AS title, c.text AS text
    """
    with driver.session(database=settings.database) as session:
        rows = session.run(query, corpus=CORPUS_TAG).data()
    grouped: dict[str, list[dict]] = {}
    for row in rows:
        grouped.setdefault(row["study_id"], []).append(row)
    chosen = []
    for study_rows in grouped.values():
        def rank(item: dict) -> tuple:
            title = (item["title"] or "").lower()
            hit = 0 if any(word in title for word in KEYWORDS) else 1
            return (hit, -min(len(item["text"]), 4000))
        study_rows.sort(key=rank)
        chosen.extend(study_rows[:per_study])
    return chosen


def _canonical_id(entity_type: str, name: str) -> str:
    return f"{entity_type}|{normalize_name(name).lower()}"


def write_mentions(section_id: str, study_id: str, mentions: list[Mention]) -> int:
    driver, settings = connect()
    written = 0
    with driver.session(database=settings.database) as session:
        for index, mention in enumerate(mentions):
            entity_type = mention.entity_type.strip().upper().replace(" ", "_")
            if entity_type not in ENTITY_TYPES:
                continue
            name = normalize_name(mention.name)
            if len(name) < 3:
                continue
            session.run(
                """
                MATCH (c:SECTION_CONTENT {section_id: $section_id, corpus: $corpus})
                MATCH (s:STUDY {name: $study_id, corpus: $corpus})
                MERGE (std:STANDARDIZED {canonical_id: $canonical_id, corpus: $corpus})
                SET std.name = $name, std.entity_type = $entity_type
                MERGE (s)<-[:BELONGS_TO_STUDY]-(std)
                CREATE (e:ENTITY {corpus: $corpus, mention_id: $mention_id})
                SET e.name = $span, e.entity_type = $entity_type
                MERGE (e)-[:EXTRACTED_FROM]->(c)
                MERGE (e)-[:HAS_STANDARDIZED_VERSION]->(std)
                """,
                section_id=section_id,
                corpus=CORPUS_TAG,
                study_id=study_id,
                canonical_id=_canonical_id(entity_type, name),
                name=name,
                entity_type=entity_type,
                span=normalize_name(mention.span or name)[:400],
                mention_id=f"{section_id}:{index}:{_canonical_id(entity_type, name)}",
            )
            written += 1
    return written


def refresh_occurs_with() -> None:
    driver, settings = connect()
    with driver.session(database=settings.database) as session:
        session.run(
            "MATCH (:STANDARDIZED {corpus: $corpus})-[r:OCCURS_WITH]->(:STANDARDIZED {corpus: $corpus}) DELETE r",
            corpus=CORPUS_TAG,
        )
        session.run(
            """
            MATCH (s:STUDY {corpus: $corpus})<-[:BELONGS_TO_STUDY]-(a:STANDARDIZED {corpus: $corpus})
            MATCH (s)<-[:BELONGS_TO_STUDY]-(b:STANDARDIZED {corpus: $corpus})
            WHERE a.entity_type = b.entity_type AND a.canonical_id < b.canonical_id
            WITH a, b, count(DISTINCT s) AS times
            MERGE (a)-[r:OCCURS_WITH]-(b)
            SET r.times = times
            """,
            corpus=CORPUS_TAG,
        )

def clear_entities() -> None:
    driver, settings = connect()
    with driver.session(database=settings.database) as session:
        session.run("MATCH (e:ENTITY {corpus: $corpus}) DETACH DELETE e", corpus=CORPUS_TAG)
        session.run("MATCH (e:STANDARDIZED {corpus: $corpus}) DETACH DELETE e", corpus=CORPUS_TAG)

def run_extraction(model, per_study: int = 10, replace: bool = False) -> dict[str, Any]:
    chain = extraction_chain(model)
    if replace:
        clear_entities()
    done = set()
    if not replace:
        driver, settings = connect()
        with driver.session(database=settings.database) as session:
            rows = session.run(
                """
                MATCH (c:SECTION_CONTENT {corpus: $corpus})<-[:EXTRACTED_FROM]-(:ENTITY {corpus: $corpus})
                RETURN DISTINCT c.section_id AS section_id
                """,
                corpus=CORPUS_TAG,
            ).data()
        done = {row["section_id"] for row in rows}
    sections = [section for section in sections_to_extract(per_study=per_study) if section["section_id"] not in done]
    written = 0
    failures = 0
    for section in sections:
        try:
            batch = chain.invoke({"title": section["title"], "text": section["text"][:6000]})
            mentions = batch.mentions if isinstance(batch, MentionBatch) else MentionBatch.model_validate(batch).mentions
            written += write_mentions(section["section_id"], section["study_id"], mentions)
        except Exception:
            failures += 1
    refresh_occurs_with()
    from src.canonicalize import alias_common_entities, cluster_canonical_entities, merge_identical_names
    alias_common_entities()
    merged = cluster_canonical_entities()
    merge_identical_names()
    return {"sections": len(sections), "mentions": written, "failures": failures, "merged_canonical": merged}


def preview_extractions(limit: int = 20):
    import pandas as pd

    driver, settings = connect()
    with driver.session(database=settings.database) as session:
        rows = session.run(
            """
            MATCH (s:STUDY {corpus: $corpus})<-[:BELONGS_TO_STUDY]-(std:STANDARDIZED)
                  <-[:HAS_STANDARDIZED_VERSION]-(e:ENTITY)-[:EXTRACTED_FROM]->(c:SECTION_CONTENT)
            RETURN s.name AS study_id, c.name AS section, e.entity_type AS entity_type,
                   e.name AS span, std.name AS canonical_name
            LIMIT $limit
            """,
            corpus=CORPUS_TAG,
            limit=limit,
        ).data()
        shared = session.run(
            """
            MATCH (std:STANDARDIZED {corpus: $corpus})-[:BELONGS_TO_STUDY]->(s:STUDY)
            WITH std, count(DISTINCT s) AS studies
            WHERE studies > 1
            RETURN std.entity_type AS entity_type, std.name AS canonical_name, studies
            ORDER BY studies DESC
            LIMIT $limit
            """,
            corpus=CORPUS_TAG,
            limit=limit,
        ).data()
    return pd.DataFrame(rows), pd.DataFrame(shared)
