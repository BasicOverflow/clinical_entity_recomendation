"""Component D: non-entity protocol embedding similarity."""

from __future__ import annotations

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as sk_cosine_similarity

def cosine_similarity(u: np.ndarray, v: np.ndarray) -> float:
    """Cosine similarity via sklearn pairwise utility."""
    u = np.asarray(u, dtype=float).reshape(1, -1)
    v = np.asarray(v, dtype=float).reshape(1, -1)
    return float(sk_cosine_similarity(u, v)[0, 0])


def protocol_embedding_similarity(chunk_embeddings_a: list[np.ndarray], chunk_embeddings_b: list[np.ndarray], renorm_mean: bool = True) -> float:
    """Normalize-per-chunk, mean-pool, then cosine between studies."""

    def pool(chunks: list[np.ndarray]) -> np.ndarray:
        if not chunks:
            return np.array([])
        normed = []
        for c in chunks:
            v = np.asarray(c, dtype=float).ravel()
            n = np.linalg.norm(v)
            normed.append(v / n if n > 0 else v)

        m = np.mean(np.stack(normed, axis=0), axis=0)
        if renorm_mean:
            nm = np.linalg.norm(m)
            if nm > 0:
                m = m / nm
        return m

    pa = pool(chunk_embeddings_a)
    pb = pool(chunk_embeddings_b)
    if pa.size == 0 or pb.size == 0:
        return 0.0
    return cosine_similarity(pa, pb)
