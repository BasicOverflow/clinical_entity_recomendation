"""Weighted study–study similarity and artifacts."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

from src.components.deviation import (
    entity_deviation_combined,
    entity_deviation_level1,
    entity_deviation_level2,
)
from src.components.entity_type import entity_type_similarity
from src.components.metadata import metadata_similarity
from src.components.protocol_embedding import protocol_embedding_similarity
from src.components.section_distribution import section_distribution_similarity


W_ENTITY_TYPE = 0.30
W_SECTION = 0.25
W_DEVIATION = 0.25
W_PROTOCOL = 0.15
W_METADATA = 0.05

W_DEV_L1 = 0.7
W_DEV_L2 = 0.3

DEFAULT_METADATA_FIELDS = (
    "phase",
    "indication",
    "therapeutic_area",
    "design",
    "blinding",
)


@dataclass
class SimilarityWeights:
    """Top-level and deviation-subscore weights used by StudySimilarityEngine."""

    entity_type: float = W_ENTITY_TYPE
    section_distribution: float = W_SECTION
    entity_deviation: float = W_DEVIATION
    protocol_embedding: float = W_PROTOCOL
    metadata: float = W_METADATA
    deviation_level1: float = W_DEV_L1
    deviation_level2: float = W_DEV_L2


@dataclass
class StudySimilarityInput:
    """All precomputed inputs needed to score one study pair."""

    study_id_a: str
    study_id_b: str
    entity_counts_a: dict[str, int]
    entity_counts_b: dict[str, int]
    entity_keys: list[str]
    section_totals_a: np.ndarray
    section_totals_b: np.ndarray
    section_mapping: list[tuple[str, str]]
    population_entity_totals: list[dict[str, int]]
    entity_by_section_a: dict[str, np.ndarray]
    entity_by_section_b: dict[str, np.ndarray]
    population_section_per_entity: list[dict[str, np.ndarray]]
    chunk_embeddings_a: list[np.ndarray]
    chunk_embeddings_b: list[np.ndarray]
    metadata_a: dict[str, Any]
    metadata_b: dict[str, Any]
    metadata_fields: tuple[str, ...] = DEFAULT_METADATA_FIELDS
    deviation_step_threshold: float = 0.5


@dataclass
class StudySimilarityResult:
    """Composite score plus per-component breakdown and debug artifacts."""

    study_design_similarity: float
    study_pair: tuple[str, str]
    raw_scores: dict[str, float]
    weights: dict[str, float]
    component_breakdown: dict[str, Any]
    artifacts: dict[str, Any] = field(default_factory=dict)


class StudySimilarityEngine:
    """Compute weighted multi-signal similarity for a pair of studies."""

    def __init__(self, weights: SimilarityWeights | None = None):
        self.weights = weights or SimilarityWeights()

    def compute(self, inp: StudySimilarityInput) -> StudySimilarityResult:
        """Run components A-E, apply weights, and return score + artifacts."""
        w = self.weights

        # 1) Raw component scores and core artifact tables.
        s_a, art_entity = entity_type_similarity(
            inp.entity_counts_a,
            inp.entity_counts_b,
            inp.entity_keys,
        )
        s_b = section_distribution_similarity(
            inp.section_totals_a,
            inp.section_totals_b,
        )
        s_c1, art_l1 = entity_deviation_level1(
            inp.entity_counts_a,
            inp.entity_counts_b,
            inp.population_entity_totals,
            inp.entity_keys,
        )
        s_c2, art_l2 = entity_deviation_level2(
            inp.entity_counts_a,
            inp.entity_counts_b,
            inp.entity_by_section_a,
            inp.entity_by_section_b,
            inp.population_section_per_entity,
            inp.entity_keys,
            step_threshold=inp.deviation_step_threshold,
        )
        s_c = entity_deviation_combined(
            s_c1, s_c2, w.deviation_level1, w.deviation_level2
        )
        s_d = protocol_embedding_similarity(
            inp.chunk_embeddings_a,
            inp.chunk_embeddings_b,
        )
        s_e, art_meta = metadata_similarity(
            inp.metadata_a,
            inp.metadata_b,
            inp.metadata_fields,
        )

        # 2) Raw values collected for diagnostics and notebook display.
        raw = {
            "entity_type": s_a,
            "section_distribution": s_b,
            "entity_deviation": s_c,
            "entity_deviation_level1": s_c1,
            "entity_deviation_level2": s_c2,
            "protocol_embedding": s_d,
            "metadata": s_e,
        }

        # 3) Weighted contributions and final scalar similarity.
        contrib = {
            "entity_type": w.entity_type * s_a,
            "section_distribution": w.section_distribution * s_b,
            "entity_deviation": w.entity_deviation * s_c,
            "protocol_embedding": w.protocol_embedding * s_d,
            "metadata": w.metadata * s_e,
        }
        total = sum(contrib.values())

        # 4) JSON-friendly breakdown mirroring the methodology writeup.
        breakdown = {
            "entity_type_similarity": {
                "raw_score": s_a,
                "weight_applied": w.entity_type,
                "weighted_contribution": contrib["entity_type"],
            },
            "section_distribution_similarity": {
                "raw_score": s_b,
                "weight_applied": w.section_distribution,
                "weighted_contribution": contrib["section_distribution"],
            },
            "entity_deviation_similarity": {
                "raw_score": s_c,
                "level1_score": s_c1,
                "level2_score": s_c2,
                "weight_applied": w.entity_deviation,
                "weighted_contribution": contrib["entity_deviation"],
            },
            "protocol_embedding_similarity": {
                "raw_score": s_d,
                "weight_applied": w.protocol_embedding,
                "weighted_contribution": contrib["protocol_embedding"],
            },
            "metadata_similarity": {
                "raw_score": s_e,
                "weight_applied": w.metadata,
                "weighted_contribution": contrib["metadata"],
            },
        }

        # 5) Section artifact keeps mapped titles and per-section totals.
        section_artifact = []
        for j, (ta, tb) in enumerate(inp.section_mapping):
            section_artifact.append(
                {
                    "section_a": ta,
                    "section_b": tb,
                    "total_mentions_a": float(inp.section_totals_a[j]),
                    "total_mentions_b": float(inp.section_totals_b[j]),
                }
            )

        # 6) Artifact bundle used for explanation/debugging in notebooks.
        artifacts = {
            "entity_comparison": art_entity,
            "section_mapping_table": section_artifact,
            "deviation_level1_rows": art_l1,
            "deviation_level2_rows": art_l2,
            "metadata_comparison": art_meta,
        }

        return StudySimilarityResult(
            study_design_similarity=total,
            study_pair=(inp.study_id_a, inp.study_id_b),
            raw_scores=raw,
            weights={
                "entity_type": w.entity_type,
                "section_distribution": w.section_distribution,
                "entity_deviation": w.entity_deviation,
                "protocol_embedding": w.protocol_embedding,
                "metadata": w.metadata,
            },
            component_breakdown=breakdown,
            artifacts=artifacts,
        )
