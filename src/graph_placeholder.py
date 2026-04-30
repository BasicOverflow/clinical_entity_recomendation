"""Stub protocol graph access — implement for Neo4j / your property graph."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

import numpy as np


class ProtocolGraphSource(ABC):
    """
    Fetch graph-backed slices needed for similarity/recommendations.

    Assumption: clinical documents are already digitized into the knowledge graph
    (section/chunk nodes exist), and entity nodes are linked on top of those sections.
    """

    @abstractmethod
    def fetch_entity_counts(self, study_id: str) -> dict[str, int]:
        """Canonical entity id -> total mention count linked to this study."""

    @abstractmethod
    def fetch_section_entity_counts(self, study_id: str, section_mapping: list[tuple[str, str]]) -> tuple[np.ndarray, dict[str, np.ndarray]]:
        """
        Returns (section_totals_per_mapped_column, entity_by_section[entity] -> len(mapping) counts).
        Column order must match section_mapping. Counts come from entity nodes attached
        to graph section/chunk nodes for this study.
        """

    @abstractmethod
    def fetch_nonentity_chunk_embeddings(self, study_id: str) -> list[np.ndarray]:
        """Embeddings for TextChunk nodes under the protocol with no entity mention edges."""

    @abstractmethod
    def fetch_metadata(self, study_id: str) -> dict[str, Any]:
        """Study-level metadata fields (phase, indication, …)."""


class StubProtocolGraphSource(ProtocolGraphSource):
    def fetch_entity_counts(self, study_id: str) -> dict[str, int]:
        raise NotImplementedError("Wire to your graph: StudyRecord -> CanonicalEntity counts.")

    def fetch_section_entity_counts(self, study_id: str, section_mapping: list[tuple[str, str]]) -> tuple[np.ndarray, dict[str, np.ndarray]]:
        raise NotImplementedError("Wire outline/TextChunk attribution + mapping columns.")

    def fetch_nonentity_chunk_embeddings(self, study_id: str) -> list[np.ndarray]:
        raise NotImplementedError("Return chunk_embedding vectors for non-entity chunks.")

    def fetch_metadata(self, study_id: str) -> dict[str, Any]:
        raise NotImplementedError("Return study metadata node/row as dict.")
