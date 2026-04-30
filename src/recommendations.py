"""Top-K neighbors, missing-entity mining, co-occurrence filtering, rerank hooks."""

from __future__ import annotations

from collections import Counter
from typing import Any, Callable

import networkx as nx
import numpy as np
import pandas as pd


def top_k_neighbors(target_id: str, similarity_with_target: dict[str, float], k: int) -> list[tuple[str, float]]:
    """Return top-K neighbors from {study_id: similarity_score}."""
    items = [(sid, sc) for sid, sc in similarity_with_target.items() if sid != target_id]
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:k]


def entity_frequency_in_neighbors(neighbor_entity_sets: list[set[str]]) -> Counter[str]:
    """Count in how many neighbor studies each entity appears."""
    c: Counter[str] = Counter()
    for s in neighbor_entity_sets:
        for e in s:
            c[e] += 1
    return c


def missing_entity_candidates(neighbor_entity_sets: list[set[str]], target_entities: set[str]) -> list[tuple[str, int]]:
    """Rank entities present in neighbors but absent in the target."""
    freq = entity_frequency_in_neighbors(neighbor_entity_sets)
    out = [(e, n) for e, n in freq.items() if e not in target_entities]
    out.sort(key=lambda x: x[1], reverse=True)
    return out


def cooccurrence_pairs(target_entities: set[str], neighbor_entity_sets: list[set[str]], min_neighbor_studies: int = 1, min_conditional_pct: float = 0.0) -> pd.DataFrame:
    """
    Among similar studies, pairs (entity_in_target -> entity_suggested) where both appear
    in the same neighbor study. Filter by support and P(suggested | target entity in neighbor).
    """
    n_n = len(neighbor_entity_sets)
    if n_n == 0:
        return pd.DataFrame(
            columns=[
                "entity_in_target",
                "entity_suggested",
                "neighbor_studies_with_pair",
                "conditional_pct",
            ]
        )

    # Build directional recommendation edges: target entity -> suggested entity.
    rows = []
    for e_t in target_entities:
        for e_s in set().union(*neighbor_entity_sets):
            if e_s in target_entities:
                continue
            support = sum(1 for s in neighbor_entity_sets if e_t in s and e_s in s)
            if support < min_neighbor_studies:
                continue
            has_t = sum(1 for s in neighbor_entity_sets if e_t in s)
            cond = support / has_t if has_t else 0.0
            if cond < min_conditional_pct:
                continue
            rows.append(
                {
                    "entity_in_target": e_t,
                    "entity_suggested": e_s,
                    "neighbor_studies_with_pair": support,
                    "conditional_pct": round(cond, 4),
                }
            )
    return pd.DataFrame(rows)


def rerank_specialized_deviation(df: pd.DataFrame, global_entity_counts: dict[str, int], score_col: str = "neighbor_studies_with_pair", rarity_power: float = 1.0) -> pd.DataFrame:
    """
    Up-weight pairs where the suggested entity is globally rare but locally frequent.
    Adds column specialized_deviation_score.
    """
    if df.empty:
        return df
    # Rarity proxy: inverse global prevalence of suggested entity.
    total = sum(global_entity_counts.values()) or 1
    rarity = []
    for _, r in df.iterrows():
        g = global_entity_counts.get(r["entity_suggested"], 1)
        rarity.append((total / max(g, 1)) ** rarity_power)
    base = df[score_col].astype(float).values
    spec = base * np.array(rarity)
    out = df.copy()
    out["specialized_deviation_score"] = spec
    return out.sort_values("specialized_deviation_score", ascending=False).reset_index(drop=True)


def _cooccurrence_graph(df: pd.DataFrame) -> nx.Graph:
    """Create weighted undirected graph from co-occurrence table rows."""
    g = nx.Graph()
    for _, r in df.iterrows():
        u, v = r["entity_in_target"], r["entity_suggested"]
        w = float(r.get("neighbor_studies_with_pair", 1))
        if g.has_edge(u, v):
            g[u][v]["weight"] += w
        else:
            g.add_edge(u, v, weight=w)
    return g


def rerank_network_scores(df: pd.DataFrame, target_entities: set[str], alpha: float = 0.5) -> pd.DataFrame:
    """PageRank + betweenness on co-occurrence graph; overlap boost with target entities."""
    if df.empty:
        return df

    # Network structure over recommendation edges.
    g = _cooccurrence_graph(df)
    pr = nx.pagerank(g, weight="weight")
    bet = nx.betweenness_centrality(g, weight="weight")

    # Extra local-fit signal: shared neighbors with target-side entities.
    overlap = []
    for _, r in df.iterrows():
        es = r["entity_suggested"]
        nbrs = set(g.neighbors(es)) if es in g else set()
        overlap.append(len(nbrs & target_entities))

    out = df.copy()
    out["pagerank_suggested"] = [pr.get(r["entity_suggested"], 0.0) for _, r in df.iterrows()]
    out["betweenness_suggested"] = [bet.get(r["entity_suggested"], 0.0) for _, r in df.iterrows()]
    out["target_overlap"] = overlap
    out["network_score"] = (
        out["pagerank_suggested"]
        + 0.25 * out["betweenness_suggested"]
        + alpha * out["target_overlap"]
    )
    return out.sort_values("network_score", ascending=False).reset_index(drop=True)


def rerank_specialized_network(df: pd.DataFrame, target_entities: set[str], hub_penalty: float = 0.5) -> pd.DataFrame:
    """Down-weight suggested nodes with very high degree (global hubs)."""
    df2 = rerank_network_scores(df, target_entities)
    if df2.empty:
        return df2
    g = _cooccurrence_graph(df)
    deg = dict(g.degree(weight="weight"))
    maxd = max(deg.values()) or 1.0
    # Penalize heavy hubs so locally relevant entities can rise.
    adj = []
    for _, r in df2.iterrows():
        es = r["entity_suggested"]
        d = deg.get(es, 0.0)
        adj.append(1.0 - hub_penalty * (d / maxd))
    out = df2.copy()
    out["hub_adjustment"] = adj
    out["specialized_network_score"] = out["network_score"] * out["hub_adjustment"]
    return out.sort_values("specialized_network_score", ascending=False).reset_index(drop=True)


def apply_rerank_fn(df: pd.DataFrame, fn: Callable[[pd.DataFrame], pd.DataFrame]) -> pd.DataFrame:
    """Utility hook for notebook experiments with custom rerank functions."""
    return fn(df)


def aggregate_missing_entities(top_k_results: list[tuple[str, Any]]) -> tuple[dict[str, dict[str, Any]], set[str], pd.DataFrame]:
    """
    Notebook-style extraction of missing entities from pairwise similarity artifacts.

    Expected shape (from each result object):
    - result.study_design_similarity
    - result.artifacts["entity_comparison"] with rows containing:
      {"entity": ..., "status": "shared|unique_to_a|unique_to_b", ...}
    """
    entity_recs: dict[str, dict[str, Any]] = {}
    target_study_entities: set[str] = set()

    for study_id, result in top_k_results:
        comparison_rows = result.artifacts.get("entity_comparison", [])
        comparison_df = pd.DataFrame(comparison_rows)
        if comparison_df.empty:
            continue

        shared = comparison_df[comparison_df["status"] == "shared"]
        unique_to_b = comparison_df[comparison_df["status"] == "unique_to_b"]

        for _, row in shared.iterrows():
            target_study_entities.add(row["entity"])

        for _, row in unique_to_b.iterrows():
            entity = row["entity"]
            if entity not in entity_recs:
                entity_recs[entity] = {"frequency": 0, "similar_studies": [], "similarities": []}
            entity_recs[entity]["frequency"] += 1
            entity_recs[entity]["similar_studies"].append(study_id)
            entity_recs[entity]["similarities"].append(result.study_design_similarity)

    # Match notebook-oriented display columns.
    rec_rows = []
    for entity, data in entity_recs.items():
        avg_similarity = sum(data["similarities"]) / len(data["similarities"])
        rec_rows.append(
            {
                "Entity": entity,
                "Frequency": data["frequency"],
                "Similar Studies": ", ".join(data["similar_studies"]),
                "Avg Similarity": round(avg_similarity, 3),
            }
        )
    recommendations_df = pd.DataFrame(rec_rows).sort_values("Frequency", ascending=False) if rec_rows else pd.DataFrame(columns=["Entity", "Frequency", "Similar Studies", "Avg Similarity"])
    return entity_recs, target_study_entities, recommendations_df


def cooccurrence_from_recommendation_map(entity_recs: dict[str, dict[str, Any]], target_entity_studies: dict[str, set[str]], min_cooccurrence_count: int = 1, min_cooccurrence_pct: float = 0.0, min_target_entity_studies: int = 1) -> pd.DataFrame:
    """
    Notebook-style co-occurrence table builder with familiar columns and filters.
    """
    pairs = []
    for target_entity, target_studies_set in target_entity_studies.items():
        target_count = len(target_studies_set)
        if target_count < min_target_entity_studies:
            continue

        for rec_entity, rec_data in entity_recs.items():
            rec_studies_set = set(rec_data["similar_studies"])
            cooccurrence_count = len(target_studies_set & rec_studies_set)
            if cooccurrence_count < min_cooccurrence_count:
                continue

            cooccurrence_pct = round((cooccurrence_count / target_count) * 100, 1) if target_count > 0 else 0.0
            if cooccurrence_pct < min_cooccurrence_pct:
                continue

            pairs.append(
                {
                    "Target Entity": target_entity,
                    "Recommended Entity": rec_entity,
                    "Co-occurrence Count": cooccurrence_count,
                    "Target Entity Studies": target_count,
                    "Recommended Entity Studies": len(rec_studies_set),
                    "Co-occurrence %": cooccurrence_pct,
                    "Co-occurring Studies": ", ".join(sorted(target_studies_set & rec_studies_set)),
                }
            )

    if not pairs:
        return pd.DataFrame(
            columns=[
                "Target Entity",
                "Recommended Entity",
                "Co-occurrence Count",
                "Target Entity Studies",
                "Recommended Entity Studies",
                "Co-occurrence %",
                "Co-occurring Studies",
            ]
        )

    return pd.DataFrame(pairs).sort_values(
        ["Co-occurrence %", "Co-occurrence Count", "Recommended Entity Studies"],
        ascending=[False, False, False],
    ).reset_index(drop=True)
