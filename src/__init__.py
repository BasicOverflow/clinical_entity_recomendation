"""Study similarity (multi-signal) and entity recommendation helpers."""

from src.engine import (
    DEFAULT_METADATA_FIELDS,
    SimilarityWeights,
    StudySimilarityEngine,
    StudySimilarityInput,
    StudySimilarityResult,
)
from src.components import cosine_similarity, row_proportions
from src.components.deviation import (
    entity_deviation_combined,
    entity_deviation_level1,
    entity_deviation_level2,
)
from src.entity_pipeline_placeholder import (
    EntityStandardizationPipeline,
    StubEntityStandardizationPipeline,
)
from src.components.entity_type import (
    entity_type_similarity,
    entity_type_similarity_from_matrix,
)
from src.graph_placeholder import ProtocolGraphSource, StubProtocolGraphSource
from src.components.metadata import metadata_similarity
from src.components.protocol_embedding import protocol_embedding_similarity
from src.components.section_distribution import (
    section_distribution_similarity,
    section_distribution_similarity_from_matrix,
)
from src import recommendations

__all__ = [
    "DEFAULT_METADATA_FIELDS",
    "SimilarityWeights",
    "StudySimilarityEngine",
    "StudySimilarityInput",
    "StudySimilarityResult",
    "EntityStandardizationPipeline",
    "StubEntityStandardizationPipeline",
    "ProtocolGraphSource",
    "StubProtocolGraphSource",
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
    "recommendations",
]
