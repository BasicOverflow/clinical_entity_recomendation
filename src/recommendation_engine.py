"""Recommendation engine on top of graph similarity."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from src.recommendations import (
    aggregate_missing_entities,
    cooccurrence_from_recommendation_map,
    rerank_network_scores,
    rerank_specialized_deviation,
    rerank_specialized_network,
)
from src.similarity import PublicStudySimilarityEngine


@dataclass
class AggregatedRecommendation:
    recommended_entity: str
    entity_type: str
    frequency: int
    similar_studies: list[str]
    natural_language_recommendation: str


def _align(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return frame
    out = frame.copy()
    out["entity_in_target"] = out["Target Entity"]
    out["entity_suggested"] = out["Recommended Entity"]
    out["neighbor_studies_with_pair"] = out["Co-occurrence Count"]
    return out


def _target_entity_studies(top_k) -> dict[str, set[str]]:
    mapping: dict[str, set[str]] = {}
    for study_id, result in top_k:
        for row in result.artifacts.get("entity_comparison", []):
            if row.get("status") == "shared":
                mapping.setdefault(row["entity"], set()).add(study_id)
    return mapping


def natural_language(row: pd.Series) -> str:
    return (
        f"Studies that used {row['Target Entity']} also used {row['Recommended Entity']} "
        f"in {int(row['Co-occurrence Count'])} similar studies ({row['Co-occurrence %']}%)."
    )


class RecommendationEngine:
    def __init__(self, similarity_weights: dict | None = None, similarity_top_k: int = 5, cooccurrence_min_count: int = 1, cooccurrence_min_pct: float = 20.0, cooccurrence_min_target_studies: int = 1):
        self.similarity = PublicStudySimilarityEngine(similarity_weights)
        self.similarity_top_k = similarity_top_k
        self.cooccurrence_min_count = cooccurrence_min_count
        self.cooccurrence_min_pct = cooccurrence_min_pct
        self.cooccurrence_min_target_studies = cooccurrence_min_target_studies

    def recommend(self, target_study: str, top_k: int | None = None, weights: dict | None = None) -> dict:
        ranked = self.similarity.find_top_n_similar(target_study, n=top_k or self.similarity_top_k, weights=weights)
        pairs = [(result.study_pair[1], result) for result in ranked]
        entity_recs, target_entities, missing = aggregate_missing_entities(pairs)
        cooccurrence = cooccurrence_from_recommendation_map(
            entity_recs,
            _target_entity_studies(pairs),
            min_cooccurrence_count=self.cooccurrence_min_count,
            min_cooccurrence_pct=self.cooccurrence_min_pct,
            min_target_entity_studies=self.cooccurrence_min_target_studies,
        )
        aligned = _align(cooccurrence)
        if not aligned.empty:
            aligned["Natural language"] = aligned.apply(natural_language, axis=1)
        aggregated = _aggregate(aligned)
        return {
            "similar_studies": pairs,
            "missing_entities": missing,
            "target_entities": target_entities,
            "cooccurrence": aligned,
            "aggregated": aggregated,
        }


def _aggregate(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return pd.DataFrame(columns=["Recommended Entity", "Entity type", "Frequency", "Example", "Natural language"])
    rows = []
    for entity, group in frame.groupby("Recommended Entity"):
        top = group.sort_values("Co-occurrence %", ascending=False).iloc[0]
        entity_type = entity.split("- ", 1)[0] if "- " in entity else ""
        rows.append({
            "Recommended Entity": entity,
            "Entity type": entity_type,
            "Frequency": int(group["Recommended Entity Studies"].max()),
            "Example": top["Target Entity"],
            "Natural language": top["Natural language"],
        })
    return pd.DataFrame(rows).sort_values("Frequency", ascending=False).reset_index(drop=True)


def experiment_frames(target_study: str) -> dict[str, pd.DataFrame]:
    base = RecommendationEngine(similarity_top_k=5, cooccurrence_min_pct=0, cooccurrence_min_count=1, cooccurrence_min_target_studies=1)
    baseline = base.recommend(target_study)
    wider = RecommendationEngine(
        similarity_weights={"entity_deviation": 0.45, "entity_type": 0.2, "section_distribution": 0.15, "protocol_embedding": 0.15, "metadata": 0.05},
        similarity_top_k=8,
        cooccurrence_min_pct=0,
        cooccurrence_min_count=1,
    ).recommend(target_study)
    cooccurrence = baseline["cooccurrence"]
    global_counts = base.similarity.matrix.sum(axis=0).astype(int).to_dict()
    specialized = rerank_specialized_deviation(cooccurrence, global_counts) if not cooccurrence.empty else cooccurrence
    network = rerank_network_scores(cooccurrence, baseline["target_entities"]) if not cooccurrence.empty else cooccurrence
    specialized_network = rerank_specialized_network(cooccurrence, baseline["target_entities"]) if not cooccurrence.empty else cooccurrence
    return {
        "similar": pd.DataFrame([
            {"study_id": study_id, "similarity": result.study_design_similarity}
            for study_id, result in baseline["similar_studies"]
        ]),
        "missing": baseline["missing_entities"],
        "baseline": cooccurrence,
        "experiment_1": wider["cooccurrence"],
        "experiment_2": specialized,
        "experiment_3": network,
        "experiment_4": specialized_network,
        "aggregated": baseline["aggregated"] if False else _aggregate(specialized_network if not specialized_network.empty else cooccurrence),
    }
