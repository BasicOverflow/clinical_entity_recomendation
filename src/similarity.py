"""Section alignment and graph-backed similarity for the public corpus."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from src.components.deviation import entity_deviation_level1
from src.components.entity_type import entity_type_similarity
from src.components.metadata import metadata_similarity
from src.config import CORPUS_TAG
from src.embeddings import embed_texts
from src.engine import SimilarityWeights, StudySimilarityEngine, StudySimilarityInput, StudySimilarityResult
from src.graph import connect

METADATA_FIELDS = (
    "study_phase",
    "indication",
    "subject_type",
    "design",
    "blinding",
    "comparative_study",
    "allocation",
    "sex",
)


@dataclass
class SectionNode:
    section_id: str
    name: str
    section_number: str
    is_parent: bool


_DRIVER = None
_DATABASE = None


def _session():
    global _DRIVER, _DATABASE
    if _DRIVER is None:
        _DRIVER, settings = connect()
        _DATABASE = settings.database
    return _DRIVER, _DRIVER.session(database=_DATABASE)


def run_df(query: str, **params) -> pd.DataFrame:
    _, session = _session()
    try:
        rows = session.run(query, **params).data()
    finally:
        session.close()
    return pd.DataFrame(rows)


def graph_summary() -> str:
    driver, session = _session()
    try:
        row = session.run(
            "MATCH (n {corpus: $corpus}) RETURN count(n) AS nodes",
            corpus=CORPUS_TAG,
        ).single()
        rels = session.run(
            "MATCH ()-[r]->() WHERE startNode(r).corpus = $corpus RETURN count(r) AS rels",
            corpus=CORPUS_TAG,
        ).single()
    finally:
        session.close()
    return f"[public-ctg] Total nodes: {row['nodes']}, Total relationships: {rels['rels']}"


def study_preview(limit: int = 5) -> pd.DataFrame:
    return run_df(
        """
        MATCH (n:STUDY {corpus: $corpus})
        RETURN n.study_title AS study_title,
               n.comparative_study AS comparative_study,
               n.subject_type AS subject_type,
               n.study_phase AS study_phase,
               n.study_status AS study_status
        ORDER BY n.name
        LIMIT $limit
        """,
        corpus=CORPUS_TAG,
        limit=limit,
    )


def protocol_studies() -> pd.DataFrame:
    return run_df(
        """
        MATCH (s:STUDY {corpus: $corpus})-[:HAS_DOCUMENT]->(:PROTOCOL)
        RETURN DISTINCT s.name AS study_name, elementId(s) AS study_node_id
        ORDER BY s.name
        """,
        corpus=CORPUS_TAG,
    )


def protocol_csr_studies() -> pd.DataFrame:
    return run_df(
        """
        MATCH (s:STUDY {corpus: $corpus})-[:HAS_DOCUMENT]->(:PROTOCOL)
        MATCH (s)-[:HAS_DOCUMENT]->(:CSR)
        RETURN DISTINCT s.name AS study_name, elementId(s) AS study_node_id
        ORDER BY s.name
        """,
        corpus=CORPUS_TAG,
    )


def build_entity_counts_matrix(study_names: list[str]) -> pd.DataFrame:
    rows = run_df(
        """
        MATCH (s:STUDY {corpus: $corpus})<-[:BELONGS_TO_STUDY]-(std:STANDARDIZED {corpus: $corpus})
              <-[:HAS_STANDARDIZED_VERSION]-(e {corpus: $corpus})-[:EXTRACTED_FROM]->(c:SECTION_CONTENT {corpus: $corpus})
        WHERE s.name IN $studies AND c.document_type = 'PROTOCOL' AND NOT e:STANDARDIZED
        RETURN s.name AS study_id,
               std.entity_type AS entity_type,
               std.name AS entity_name,
               count(e) AS entity_count
        """,
        corpus=CORPUS_TAG,
        studies=study_names,
    )
    if rows.empty:
        return pd.DataFrame()
    rows["entity_col"] = rows["entity_type"].astype(str) + "- " + rows["entity_name"].astype(str)
    return rows.pivot_table(index="study_id", columns="entity_col", values="entity_count", aggfunc="sum", fill_value=0)


def entity_type_overlap(matrix: pd.DataFrame, study_a: str, study_b: str) -> dict:
    score, _ = entity_type_similarity(matrix.loc[study_a].to_dict(), matrix.loc[study_b].to_dict(), list(matrix.columns))
    left = matrix.loc[study_a]
    right = matrix.loc[study_b]
    return {
        "similarity": score,
        "num_shared_types": int(((left > 0) & (right > 0)).sum()),
        "num_unique_a": int(((left > 0) & (right == 0)).sum()),
        "num_unique_b": int(((right > 0) & (left == 0)).sum()),
    }


def protocol_sections(study_name: str) -> list[SectionNode]:
    frame = run_df(
        """
        MATCH (:STUDY {name: $study, corpus: $corpus})-[:HAS_DOCUMENT]->(:PROTOCOL)-[:HAS_CONTENT]->(c:SECTION_CONTENT {corpus: $corpus})
        RETURN c.section_id AS section_id, c.name AS name, c.section_number AS section_number
        ORDER BY c.section_number, c.name
        """,
        study=study_name,
        corpus=CORPUS_TAG,
    )
    nodes = []
    for row in frame.itertuples(index=False):
        name = row.name or ""
        letters = sum(character.isalpha() for character in name)
        if letters < 12:
            continue
        number = str(row.section_number or "")
        nodes.append(SectionNode(row.section_id, name, number, "." not in number))
    return nodes


def map_section_lists(left: list[SectionNode], right: list[SectionNode], threshold: float = 0.42) -> list[tuple[SectionNode, SectionNode, float]]:
    if not left or not right:
        return []
    vectors = embed_texts([node.name for node in left + right])
    left_vec = vectors[: len(left)]
    right_vec = vectors[len(left) :]
    pairs: list[tuple[SectionNode, SectionNode, float]] = []

    def greedy(group_a: list[int], group_b: list[int]) -> None:
        scored = []
        for i in group_a:
            for j in group_b:
                score = float(np.dot(left_vec[i], right_vec[j]))
                if score >= threshold:
                    scored.append((score, i, j))
        scored.sort(reverse=True)
        used_a: set[int] = set()
        used_b: set[int] = set()
        for score, i, j in scored:
            if i in used_a or j in used_b:
                continue
            used_a.add(i)
            used_b.add(j)
            pairs.append((left[i], right[j], score))

    greedy([i for i, node in enumerate(left) if node.is_parent], [i for i, node in enumerate(right) if node.is_parent])
    greedy([i for i, node in enumerate(left) if not node.is_parent], [i for i, node in enumerate(right) if not node.is_parent])
    return pairs


def section_entity_matrix(studies: list[str], mapping: list[tuple[SectionNode, SectionNode, float]]) -> pd.DataFrame:
    columns = [f"{left.name} -> {right.name}" for left, right, _ in mapping]
    frame = pd.DataFrame(0.0, index=studies, columns=columns)
    if not mapping:
        return frame
    ids = [node.section_id for pair in mapping for node in pair[:2]]
    counts = run_df(
        """
        UNWIND $ids AS section_id
        MATCH (c:SECTION_CONTENT {section_id: section_id, corpus: $corpus})<-[:EXTRACTED_FROM]-(e {corpus: $corpus})
        WHERE NOT e:STANDARDIZED
        RETURN c.section_id AS section_id, count(e) AS n
        """,
        ids=ids,
        corpus=CORPUS_TAG,
    )
    lookup = dict(zip(counts["section_id"], counts["n"])) if not counts.empty else {}
    for study in studies:
        owned = set(run_df(
            """
            MATCH (:STUDY {name: $study, corpus: $corpus})-[:HAS_DOCUMENT]->(:PROTOCOL)-[:HAS_CONTENT]->(c)
            RETURN c.section_id AS section_id
            """,
            study=study,
            corpus=CORPUS_TAG,
        )["section_id"])
        for column, (left, right, _) in zip(columns, mapping):
            section_id = left.section_id if left.section_id in owned else right.section_id
            if section_id in owned:
                frame.loc[study, column] = float(lookup.get(section_id, 0))
    return frame


def global_entity_stats(matrix: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "mean": matrix.mean(axis=0),
        "std": matrix.std(axis=0).fillna(0),
        "studies_present": (matrix > 0).sum(axis=0),
    })


def significant_deviations(matrix: pd.DataFrame, study_a: str, study_b: str) -> pd.DataFrame:
    population = [row.astype(int).to_dict() for _, row in matrix.iterrows()]
    _, rows = entity_deviation_level1(
        matrix.loc[study_a].astype(int).to_dict(),
        matrix.loc[study_b].astype(int).to_dict(),
        population,
        list(matrix.columns),
    )
    frame = pd.DataFrame(rows)
    if frame.empty:
        return frame
    return frame.reindex(frame["weight"].sort_values(ascending=False).index)


def nonentity_section_counts(study_names: list[str]) -> pd.DataFrame:
    return run_df(
        """
        MATCH (s:STUDY {corpus: $corpus})-[:HAS_DOCUMENT]->(:PROTOCOL)-[:HAS_CONTENT]->(c:SECTION_CONTENT {corpus: $corpus})
        WHERE s.name IN $studies AND NOT (c)<-[:EXTRACTED_FROM]-({corpus: $corpus})
        RETURN s.name AS study_id, count(c) AS non_entity_sections
        ORDER BY study_id
        """,
        corpus=CORPUS_TAG,
        studies=study_names,
    )


def _mean_pool(chunks: list[np.ndarray]) -> np.ndarray:
    if not chunks:
        return np.array([])
    mean = np.stack([np.asarray(chunk, dtype=float).ravel() for chunk in chunks], axis=0).mean(axis=0)
    norm = np.linalg.norm(mean)
    return mean / norm if norm else mean


def study_protocol_embedding(study_name: str) -> np.ndarray:
    texts = run_df(
        """
        MATCH (:STUDY {name: $study, corpus: $corpus})-[:HAS_DOCUMENT]->(:PROTOCOL)-[:HAS_CONTENT]->(c:SECTION_CONTENT)
        WHERE NOT (c)<-[:EXTRACTED_FROM]-({corpus: $corpus})
        RETURN c.text AS text
        LIMIT 8
        """,
        study=study_name,
        corpus=CORPUS_TAG,
    )
    if texts.empty:
        return np.array([])
    return _mean_pool(embed_texts([text[:1500] for text in texts["text"].tolist()]))


def protocol_embedding_frame(study_names: list[str]) -> pd.DataFrame:
    rows = []
    for name in study_names:
        vector = study_protocol_embedding(name)
        rows.append({"study_id": name, "dimensions": int(vector.size), "norm": float(np.linalg.norm(vector)) if vector.size else 0.0})
    return pd.DataFrame(rows)


def study_metadata_frame(study_names: list[str]) -> pd.DataFrame:
    frame = run_df(
        """
        MATCH (s:STUDY {corpus: $corpus})
        WHERE s.name IN $studies
        RETURN s.name AS study_id, s.study_phase AS study_phase, s.indication AS indication,
               s.subject_type AS subject_type, s.design AS design, s.blinding AS blinding,
               s.comparative_study AS comparative_study, s.allocation AS allocation, s.sex AS sex,
               s.study_title AS study_title, s.study_status AS study_status
        ORDER BY study_id
        """,
        corpus=CORPUS_TAG,
        studies=study_names,
    )
    return frame.set_index("study_id")


def _clean_meta(row: pd.Series) -> dict:
    cleaned = {}
    for field in METADATA_FIELDS:
        value = row[field] if field in row.index else None
        if value is None or pd.isna(value):
            cleaned[field] = None
        else:
            cleaned[field] = value
    return cleaned


def compare_studies(study_a: str, study_b: str, matrix: pd.DataFrame, metadata: pd.DataFrame, weights: SimilarityWeights | None = None, threshold: float = 0.42) -> StudySimilarityResult:
    keys = list(matrix.columns)
    mapping = map_section_lists(protocol_sections(study_a), protocol_sections(study_b), threshold=threshold)
    section_frame = section_entity_matrix([study_a, study_b], mapping)
    totals_a = section_frame.loc[study_a].to_numpy(dtype=float) if len(section_frame.columns) else np.zeros(1)
    totals_b = section_frame.loc[study_b].to_numpy(dtype=float) if len(section_frame.columns) else np.zeros(1)
    by_a, by_b = _entity_section_maps(mapping, keys)
    emb_a = study_protocol_embedding(study_a)
    emb_b = study_protocol_embedding(study_b)
    payload = StudySimilarityInput(
        study_id_a=study_a,
        study_id_b=study_b,
        entity_counts_a={k: int(matrix.loc[study_a, k]) for k in keys},
        entity_counts_b={k: int(matrix.loc[study_b, k]) for k in keys},
        entity_keys=keys,
        section_totals_a=totals_a,
        section_totals_b=totals_b,
        section_mapping=[(left.name, right.name) for left, right, _ in mapping] or [("", "")],
        population_entity_totals=[row.astype(int).to_dict() for _, row in matrix.iterrows()],
        entity_by_section_a=by_a,
        entity_by_section_b=by_b,
        population_section_per_entity=[by_a, by_b],
        chunk_embeddings_a=[emb_a] if emb_a.size else [],
        chunk_embeddings_b=[emb_b] if emb_b.size else [],
        metadata_a=_clean_meta(metadata.loc[study_a]),
        metadata_b=_clean_meta(metadata.loc[study_b]),
        metadata_fields=METADATA_FIELDS,
    )
    result = StudySimilarityEngine(weights).compute(payload)
    result.artifacts["section_score_rows"] = [
        {"section_a": left.name, "section_b": right.name, "cosine": score} for left, right, score in mapping
    ]
    return result


def _entity_section_maps(mapping, keys):
    width = max(len(mapping), 1)
    if not mapping:
        empty = {key: np.zeros(1) for key in keys}
        return empty, empty
    rows = run_df(
        """
        UNWIND $ids AS section_id
        MATCH (c:SECTION_CONTENT {section_id: section_id, corpus: $corpus})<-[:EXTRACTED_FROM]-(e {corpus: $corpus})-[:HAS_STANDARDIZED_VERSION]->(std:STANDARDIZED)
        WHERE NOT e:STANDARDIZED
        RETURN c.section_id AS section_id, std.entity_type + '- ' + std.name AS entity, count(e) AS n
        """,
        ids=[node.section_id for pair in mapping for node in pair[:2]],
        corpus=CORPUS_TAG,
    )
    lookup = {}
    if not rows.empty:
        for record in rows.itertuples(index=False):
            lookup[(record.section_id, record.entity)] = int(record.n)

    def pack(side: int) -> dict[str, np.ndarray]:
        return {
            key: np.array([lookup.get((mapping[index][side].section_id, key), 0) for index in range(width)], dtype=float)
            for key in keys
        }

    return pack(0), pack(1)


class PublicStudySimilarityEngine:
    """Graph-backed engine used by the how-to and recommendation notebooks."""

    def __init__(self, weights: dict | None = None):
        self.weights = SimilarityWeights(**{k: v for k, v in (weights or {}).items() if k in SimilarityWeights.__dataclass_fields__}) if weights else SimilarityWeights()
        if weights:
            known = {k: v for k, v in weights.items() if k in SimilarityWeights.__dataclass_fields__}
            self.weights = SimilarityWeights(**known) if known else self.weights
        self._cache: dict = {}
        self.study_names = protocol_studies()["study_name"].tolist()
        self.matrix = build_entity_counts_matrix(self.study_names)
        self.metadata = study_metadata_frame(self.study_names)

    def compare(self, study_a: str, study_b: str, weights: dict | None = None, use_llm_reviewer: bool = False) -> StudySimilarityResult:
        active = self.weights
        if weights:
            known = {k: v for k, v in weights.items() if k in SimilarityWeights.__dataclass_fields__}
            active = SimilarityWeights(**known)
        key = (study_a, study_b, tuple(sorted((field, getattr(active, field)) for field in SimilarityWeights.__dataclass_fields__)))
        if key not in self._cache:
            self._cache[key] = compare_studies(study_a, study_b, self.matrix, self.metadata, active)
        return self._cache[key]

    def find_top_n_similar(self, target_study: str, n: int = 5, weights: dict | None = None, candidates: list[str] | None = None) -> list[StudySimilarityResult]:
        pool = candidates or [name for name in self.study_names if name != target_study]
        ranked = [self.compare(target_study, other, weights=weights) for other in pool]
        ranked.sort(key=lambda item: item.study_design_similarity, reverse=True)
        return ranked[:n]
