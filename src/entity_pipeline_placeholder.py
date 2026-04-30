"""Stub pipeline: raw clinical mentions -> section links -> LLM standardization -> canonical graph."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class EntityStandardizationPipeline(ABC):
    """
    Upstream of similarity/recommendations: assumes clinical documents are already digitized in a knowledge graph, then populates CanonicalEntity links from those graph-backed sections.

    Graph story (typical):
    1. Start from graph-backed clinical documents (TextChunk/section nodes already exist).
    2. Extract raw mentions from section text (NER / rules / …).
    3. Attach mention nodes to the exact TextChunk / section they came from.
    4. LLM (or rules) map mentions to a standardized / canonical entity id shared across studies.
    5. Canonical node connects to all raw occurrences and to each StudyRecord that uses it.
    """

    @abstractmethod
    def extract_raw_mentions(self, source_document_id: str, text: str, section_ref: str) -> list[dict[str, Any]]:
        """Return mention dicts (offsets, span text, provisional type, …)."""

    @abstractmethod
    def link_mention_to_section(self, mention_id: str, chunk_id: str) -> None:
        """Persist MENTION_IN (or equivalent) in the graph."""

    @abstractmethod
    def standardize_mentions(self, mentions: list[dict[str, Any]]) -> dict[str, str]:
        """Map mention_id -> canonical_entity_id (LLM / ontology lookup)."""

    @abstractmethod
    def ensure_canonical_links(self, canonical_id: str, study_id: str, chunk_ids: list[str]) -> None:
        """Ensure standardized entity links to study and source chunks for traversal."""


class StubEntityStandardizationPipeline(EntityStandardizationPipeline):
    def extract_raw_mentions(self, source_document_id: str, text: str, section_ref: str) -> list[dict[str, Any]]:
        raise NotImplementedError("Plug in extraction from clinical protocol sources.")

    def link_mention_to_section(self, mention_id: str, chunk_id: str) -> None:
        raise NotImplementedError("Persist graph edges mention -> TextChunk.")

    def standardize_mentions(self, mentions: list[dict[str, Any]]) -> dict[str, str]:
        raise NotImplementedError("Call LLM / resolver to canonical ids.")

    def ensure_canonical_links(self, canonical_id: str, study_id: str, chunk_ids: list[str]) -> None:
        raise NotImplementedError("Write CanonicalEntity -> StudyRecord / chunk links.")
