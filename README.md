# Clinical Design Entity Recommendation

A public demo of study-to-study similarity and entity recommendation. It loads protocols, statistical analysis plans, and clinical study reports posted on [ClinicalTrials.gov](https://clinicaltrials.gov) into a Neo4j database you already run, then walks the same pipeline as a graph-backed recommendation engine.

The corpus is 25 completed interventional trials that published a protocol and a statistical analysis plan. Pfizer-sponsored trials are excluded. A clinical study report node is created from a posted study-report file when one exists, and otherwise from the posted results summary.

## Setup

Neo4j must already be running. Put the connection in `.env` (this file is not committed):

```
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=
NEO4J_DATABASE=neo4j
```

The loader writes only nodes tagged `corpus = "public-ctg"` and refuses a database name used by the internal study graph.

Set `LLM_API_KEY` and optional `LLM_BASE_URL` for an OpenAI-compatible LangChain chat model. `LLM_MODEL` selects the model name. There is no local extractor.

The downloaded studies already live in `corpus/`. Load them with:

```
pip install -r requirements.txt
python -m src.loader
```

## Notebooks

- `notebooks/ingest.ipynb` — connect to the existing graph and load the public studies, then show protocol and CSR coverage.
- `notebooks/entity_extraction.ipynb` — run the LangChain chain that reads section content and links mentions to canonical entities shared across studies.
- `notebooks/study_sim_demo.ipynb` — step through entity counts, section alignment, deviation, protocol embeddings, metadata, and the weighted similarity score.
- `notebooks/dumb_recomendations_experiments.ipynb` — missing entities and co-occurrence, then frequency, deviation, network, and specialized-network reranks.
- `notebooks/smart_recomendations.ipynb` — one engine call that reranks recommendations with the specialized network score.
- `notebooks/how_to_use_engine.ipynb` — short examples for comparing studies, top-n neighbors, artifacts, custom weights, and a candidate subset.
