from __future__ import annotations

from config import GraphRAGConfig


def test_planner_is_disabled_by_default_and_has_a_bounded_network_timeout(monkeypatch):
    monkeypatch.delenv("RETRIEVAL_INTENT_PLANNER_ENABLED", raising=False)
    monkeypatch.delenv("RETRIEVAL_INTENT_PLANNER_TIMEOUT_SECONDS", raising=False)
    config = GraphRAGConfig()
    assert config.retrieval_intent_planner_enabled is False
    assert config.retrieval_intent_planner_timeout_seconds == 30
