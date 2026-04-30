# Clinical Design Entity Recomendation

Minimal proof-of-concept for:
- multi-signal **study similarity** (components A–E), and
- similarity-driven **entity recommendations** (top-K, missing entities, co-occurrence, rerank hooks).




Similarity and recommendations assume clinical documents are already digitized into a knowledge graph (sections/chunks exist as nodes). Entity nodes are then added on top of those source sections, and standardized into canonical ids for cross-study comparison.

## Notebooks

- `notebooks/study_similarity_components.ipynb` — step through A–E, then the full weighted score.
- `notebooks/recommendations.ipynb` — top-K, missing entities, co-occurrence filtering, reranking.


## Extension

Implement `ProtocolGraphSource` (and optionally `EntityStandardizationPipeline`) against your property graph and wire real matrices into `StudySimilarityInput` / the recommendation functions.
