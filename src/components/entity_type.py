"""Component A: entity-type similarity and matrix adapter."""

from __future__ import annotations

from typing import Any, Iterable

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity as sk_cosine_similarity


def cosine_similarity(u: np.ndarray, v: np.ndarray) -> float:
    """Cosine similarity via sklearn pairwise utility."""
    u = np.asarray(u, dtype=float).reshape(1, -1)
    v = np.asarray(v, dtype=float).reshape(1, -1)
    return float(sk_cosine_similarity(u, v)[0, 0])


def row_proportions(counts: np.ndarray) -> np.ndarray:
    """Convert counts to proportions; return unchanged if row sum is zero."""
    s = counts.sum()
    if s == 0:
        return counts.astype(float)
    return counts.astype(float) / s


def entity_type_similarity(entity_counts_a: dict[str, int], entity_counts_b: dict[str, int], entity_keys: Iterable[str]) -> tuple[float, list[dict[str, Any]]]:
    """Compare entity composition via cosine on normalized vectors."""
    keys = list(entity_keys)

    va = np.array([entity_counts_a.get(k, 0) for k in keys], dtype=float)
    vb = np.array([entity_counts_b.get(k, 0) for k in keys], dtype=float)
    pa = row_proportions(va)
    pb = row_proportions(vb)
    score = cosine_similarity(pa, pb)

    artifact = []
    for k in keys:
        ca = entity_counts_a.get(k, 0)
        cb = entity_counts_b.get(k, 0)
        if ca > 0 and cb > 0:
            status = "shared"
        elif ca > 0:
            status = "unique_to_a"
        elif cb > 0:
            status = "unique_to_b"
        else:
            status = "absent"
        artifact.append({"entity": k, "count_a": ca, "count_b": cb, "status": status})
    return score, artifact


def entity_type_similarity_from_matrix(entity_count_matrix: pd.DataFrame, study_id_a: str, study_id_b: str) -> tuple[float, list[dict[str, Any]]]:
    """Notebook-style Component A using a study x entity count matrix."""
    row_a = entity_count_matrix.loc[study_id_a]
    row_b = entity_count_matrix.loc[study_id_b]
    entity_counts_a = row_a.to_dict()
    entity_counts_b = row_b.to_dict()
    entity_keys = list(entity_count_matrix.columns)
    return entity_type_similarity(entity_counts_a, entity_counts_b, entity_keys)
