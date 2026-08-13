from __future__ import annotations

import json
from types import SimpleNamespace

from rag_modules.intent_planner import IntentPlanner


def _payload(*, confidence=0.9, extra=None):
    value = {
        "intent": "PREFERENCE_RECOMMEND",
        "confidence": confidence,
        "entity_mentions": [],
        "slots": {
            "step_number": None,
            "cuisines": [],
            "ingredients": [],
            "preferences": ["FEW_STEPS", "HOMESTYLE"],
            "meal_context": ["DINNER"],
            "tools": [],
            "methods": [],
            "servings": None,
            "time_budget_minutes": None,
            "nutrition_constraint": None,
        },
    }
    value.update(extra or {})
    return json.dumps(value)


class _Client:
    def __init__(self, content=None, error=None):
        self.content = content
        self.error = error
        self.calls = []
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=self.create))

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if self.error:
            raise self.error
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=self.content))])


class _Audit:
    def __init__(self):
        self.events = []

    def record_event(self, stage, status="completed", **fields):
        self.events.append((stage, status, fields))


def test_planner_only_receives_user_message_and_returns_valid_candidate_with_audit_hash():
    client = _Client(_payload())
    audit = _Audit()

    result = IntentPlanner(client, model="test-model").plan("下班很晚，想找准备步骤少的家常菜", audit_run=audit)

    assert result.executable
    assert result.candidate.intent == "PREFERENCE_RECOMMEND"
    assert client.calls[0]["messages"][-1]["content"] == "下班很晚，想找准备步骤少的家常菜"
    assert client.calls[0]["temperature"] == 0
    assert audit.events[0][1] == "VALID"
    assert audit.events[0][2]["response_hash"] == result.response_hash


def test_invalid_json_empty_response_and_execution_field_fail_closed():
    for content, expected in (("not json", "PLANNER_INVALID_OUTPUT"), ("", "PLANNER_INVALID_OUTPUT"), (_payload(extra={"recipe_id": "fake"}), "PLANNER_INVALID_OUTPUT")):
        result = IntentPlanner(_Client(content), model="test-model").plan("清淡晚餐")
        assert result.status == expected
        assert not result.executable


def test_timeout_and_low_confidence_are_structured_non_executable_results():
    unavailable = IntentPlanner(_Client(error=TimeoutError("timeout")), model="test-model").plan("清淡晚餐")
    low_confidence = IntentPlanner(_Client(_payload(confidence=0.2)), model="test-model").plan("清淡晚餐")

    assert unavailable.status == "PLANNER_UNAVAILABLE"
    assert low_confidence.status == "PLANNER_LOW_CONFIDENCE"
    assert not unavailable.executable
    assert not low_confidence.executable


def test_planner_uses_configured_timeout_without_expanding_execution_authority():
    client = _Client(_payload())
    IntentPlanner(client, model="test-model", timeout_seconds=30).plan("清淡晚餐")
    assert client.calls[0]["timeout"] == 30
