"""Connection settings for an already running Neo4j server."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

CORPUS_TAG = "public-ctg"
BLOCKED_DATABASES = {"t2dm", "cgpt"}


@dataclass(frozen=True)
class Neo4jSettings:
    uri: str
    user: str
    password: str
    database: str


def load_settings() -> Neo4jSettings:
    load_dotenv(override=False)
    database = os.getenv("NEO4J_DATABASE", "neo4j")
    uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    if database.lower() in BLOCKED_DATABASES or "pfizer.com" in uri.lower():
        raise RuntimeError("Refusing to write this public corpus into a company study database.")
    password = os.getenv("NEO4J_PASSWORD")
    if not password:
        raise RuntimeError("Set NEO4J_PASSWORD for the existing Neo4j server.")
    return Neo4jSettings(
        uri=uri,
        user=os.getenv("NEO4J_USER", "neo4j"),
        password=password,
        database=database,
    )
