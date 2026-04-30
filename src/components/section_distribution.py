"""Component B: mapped section distribution similarity."""

from __future__ import annotations

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


def section_distribution_similarity(section_totals_a: np.ndarray, section_totals_b: np.ndarray) -> float:
    """Cosine on row-normalized mapped-section totals."""
    a = row_proportions(np.asarray(section_totals_a, dtype=float))
    b = row_proportions(np.asarray(section_totals_b, dtype=float))
    return cosine_similarity(a, b)


def section_distribution_similarity_from_matrix(section_count_matrix: pd.DataFrame, study_id_a: str, study_id_b: str) -> float:
    """Notebook-style Component B using mapped-section count matrix."""
    row_a = section_count_matrix.loc[study_id_a].to_numpy(dtype=float)
    row_b = section_count_matrix.loc[study_id_b].to_numpy(dtype=float)
    return section_distribution_similarity(row_a, row_b)
