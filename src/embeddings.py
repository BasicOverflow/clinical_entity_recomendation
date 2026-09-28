"""Local sentence-transformer embeddings with an on-disk cache."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "corpus" / "cache" / "embeddings.json"
_model = None


def _hasher(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _load_cache() -> dict:
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def _save_cache(cache: dict) -> None:
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(cache), encoding="utf-8")


def embed_texts(texts: list[str]) -> list[np.ndarray]:
    global _model
    cache = _load_cache()
    missing = []
    for text in texts:
        key = _hasher(text[:4000])
        if key not in cache:
            missing.append(text[:4000])
    if missing:
        if _model is None:
            from sentence_transformers import SentenceTransformer
            _model = SentenceTransformer("all-MiniLM-L6-v2")
        vectors = _model.encode(missing, normalize_embeddings=True, show_progress_bar=False)
        for text, vector in zip(missing, vectors):
            cache[_hasher(text)] = vector.tolist()
        _save_cache(cache)
    return [np.asarray(cache[_hasher(text[:4000])], dtype=float) for text in texts]
