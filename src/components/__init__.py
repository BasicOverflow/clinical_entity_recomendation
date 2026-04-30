"""Similarity component helpers package (A-E)."""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as sk_cosine_similarity
from src.components.deviation import (
    entity_deviation_combined,
    entity_deviation_level1,
    entity_deviation_level2,
)
from src.components.entity_type import (
    entity_type_similarity,
    entity_type_similarity_from_matrix,
)
from src.components.metadata import metadata_similarity
from src.components.protocol_embedding import protocol_embedding_similarity
from src.components.section_distribution import (
    section_distribution_similarity,
    section_distribution_similarity_from_matrix,
)


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

__all__ = [
    "cosine_similarity",
    "row_proportions",
    "entity_type_similarity",
    "entity_type_similarity_from_matrix",
    "section_distribution_similarity",
    "section_distribution_similarity_from_matrix",
    "entity_deviation_level1",
    "entity_deviation_level2",
    "entity_deviation_combined",
    "protocol_embedding_similarity",
    "metadata_similarity",
]
