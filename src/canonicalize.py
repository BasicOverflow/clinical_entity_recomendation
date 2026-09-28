"""Merge near-paraphrase canonical entities within one entity type."""

from __future__ import annotations

from src.config import CORPUS_TAG
from src.embeddings import embed_texts
from src.extraction import refresh_occurs_with
from src.graph import connect


ALIASES = (
    ("informed consent", "Written informed consent"),
    ("childbearing", "Pregnancy and contraception"),
    ("pregnan", "Pregnancy and contraception"),
    ("years of age", "Age requirement"),
    ("years old", "Age requirement"),
    ("aged ", "Age requirement"),
    ("able to comply", "Able to comply with study procedures"),
    ("willing to", "Able to comply with study procedures"),
    ("placebo", "Placebo"),
    ("egfr", "Renal function requirement"),
    ("creatinine", "Renal function requirement"),
    ("bilirubin", "Hepatic laboratory requirement"),
    ("aminotransferase", "Hepatic laboratory requirement"),
    ("malignan", "Active malignancy"),
    ("hiv", "HIV infection"),
)


def alias_common_entities() -> int:
    driver, settings = connect()
    changed = 0
    with driver.session(database=settings.database) as session:
        rows = session.run(
            "MATCH (std:STANDARDIZED {corpus: $corpus}) RETURN std.canonical_id AS canonical_id, std.name AS name, std.entity_type AS entity_type",
            corpus=CORPUS_TAG,
        ).data()
        for row in rows:
            lowered = (row["name"] or "").lower()
            for needle, label in ALIASES:
                if needle in lowered and row["name"] != label:
                    session.run(
                        """
                        MATCH (std:STANDARDIZED {canonical_id: $canonical_id, corpus: $corpus})
                        SET std.name = $label
                        """,
                        canonical_id=row["canonical_id"],
                        corpus=CORPUS_TAG,
                        label=label,
                        entity_type=row["entity_type"],
                    )
                    changed += 1
                    break
    return changed


def merge_identical_names() -> int:
    driver, settings = connect()
    with driver.session(database=settings.database) as session:
        groups = session.run(
            """
            MATCH (std:STANDARDIZED {corpus: $corpus})
            WITH std.entity_type AS entity_type, toLower(std.name) AS key, collect(std) AS nodes
            WHERE size(nodes) > 1
            RETURN entity_type, key, [n IN nodes | n.canonical_id] AS ids
            """,
            corpus=CORPUS_TAG,
        ).data()
    merged = 0
    with driver.session(database=settings.database) as session:
        for group in groups:
            winner_id = group["ids"][0]
            for loser_id in group["ids"][1:]:
                session.run(
                    """
                    MATCH (loser:STANDARDIZED {canonical_id: $loser_id, corpus: $corpus})
                    MATCH (winner:STANDARDIZED {canonical_id: $winner_id, corpus: $corpus})
                    WITH loser, winner
                    OPTIONAL MATCH (e:ENTITY)-[rel:HAS_STANDARDIZED_VERSION]->(loser)
                    FOREACH (_ IN CASE WHEN e IS NULL THEN [] ELSE [1] END |
                        MERGE (e)-[:HAS_STANDARDIZED_VERSION]->(winner)
                        DELETE rel
                    )
                    WITH DISTINCT loser, winner
                    OPTIONAL MATCH (loser)-[:BELONGS_TO_STUDY]->(s:STUDY)
                    FOREACH (_ IN CASE WHEN s IS NULL THEN [] ELSE [1] END |
                        MERGE (winner)-[:BELONGS_TO_STUDY]->(s)
                    )
                    DETACH DELETE loser
                    """,
                    loser_id=loser_id,
                    winner_id=winner_id,
                    corpus=CORPUS_TAG,
                )
                merged += 1
    return merged


def cluster_canonical_entities(threshold: float = 0.78) -> int:
    driver, settings = connect()
    with driver.session(database=settings.database) as session:
        rows = session.run(
            """
            MATCH (std:STANDARDIZED {corpus: $corpus})
            RETURN std.canonical_id AS canonical_id, std.entity_type AS entity_type, std.name AS name
            """,
            corpus=CORPUS_TAG,
        ).data()
    by_type: dict[str, list[dict]] = {}
    for row in rows:
        by_type.setdefault(row["entity_type"], []).append(row)
    rewrites = []
    for group in by_type.values():
        vectors = embed_texts([item["name"] for item in group])
        parent = list(range(len(group)))

        def find(index: int) -> int:
            while parent[index] != index:
                parent[index] = parent[parent[index]]
                index = parent[index]
            return index

        for left in range(len(group)):
            for right in range(left + 1, len(group)):
                if float(vectors[left] @ vectors[right]) >= threshold:
                    parent[find(right)] = find(left)
        clusters: dict[int, list[int]] = {}
        for index in range(len(group)):
            clusters.setdefault(find(index), []).append(index)
        for members in clusters.values():
            if len(members) < 2:
                continue
            winner = min(members, key=lambda index: len(group[index]["name"]))
            for index in members:
                if index == winner:
                    continue
                rewrites.append((group[index]["canonical_id"], group[winner]["canonical_id"], group[winner]["name"]))
    with driver.session(database=settings.database) as session:
        for loser_id, winner_id, winner_name in rewrites:
            session.run(
                """
                MATCH (loser:STANDARDIZED {canonical_id: $loser_id, corpus: $corpus})
                MATCH (winner:STANDARDIZED {canonical_id: $winner_id, corpus: $corpus})
                SET winner.name = $winner_name
                WITH loser, winner
                OPTIONAL MATCH (e:ENTITY)-[rel:HAS_STANDARDIZED_VERSION]->(loser)
                FOREACH (_ IN CASE WHEN e IS NULL THEN [] ELSE [1] END |
                    MERGE (e)-[:HAS_STANDARDIZED_VERSION]->(winner)
                    DELETE rel
                )
                WITH DISTINCT loser, winner
                OPTIONAL MATCH (loser)-[:BELONGS_TO_STUDY]->(s:STUDY)
                FOREACH (_ IN CASE WHEN s IS NULL THEN [] ELSE [1] END |
                    MERGE (winner)-[:BELONGS_TO_STUDY]->(s)
                )
                DETACH DELETE loser
                """,
                loser_id=loser_id,
                winner_id=winner_id,
                winner_name=winner_name,
                corpus=CORPUS_TAG,
            )
    refresh_occurs_with()
    return len(rewrites)
