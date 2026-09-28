"""Neo4j driver helpers."""

from __future__ import annotations

from neo4j import GraphDatabase

from src.config import Neo4jSettings, load_settings


_DRIVER = None


def connect(settings: Neo4jSettings | None = None):
    global _DRIVER
    settings = settings or load_settings()
    if _DRIVER is None:
        _DRIVER = GraphDatabase.driver(settings.uri, auth=(settings.user, settings.password))
        _DRIVER.verify_connectivity()
    return _DRIVER, settings
