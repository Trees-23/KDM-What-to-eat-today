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


class _SchemaFallbackClient(_Client):
    def __init__(self, content):
        super().__init__(content)
        self._schema_rejected = False

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if kwargs["response_format"]["type"] == "json_schema" and not self._schema_rejected:
            self._schema_rejected = True
            raise RuntimeError("response_format json_schema is unsupported")
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=self.content))])


class _RetryClient(_Client):
    def __init__(self, content, *, failures=1):
        super().__init__(content)
        self.remaining_failures = failures

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if self.remaining_failures:
            self.remaining_failures -= 1
            raise TimeoutError("temporary timeout")
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


def test_planner_retries_two_transient_failures_with_a_bounded_attempt_count():
    client = _RetryClient(_payload(), failures=2)
    audit = _Audit()

    result = IntentPlanner(client, model="test-model", max_attempts=3).plan("清淡晚餐", audit_run=audit)

    assert result.executable
    assert result.attempt_count == 3
    assert len(client.calls) == 3
    assert audit.events[0][2]["attempt_count"] == 3


def test_schema_capability_fallback_keeps_local_candidate_validation_and_audit_format():
    client = _SchemaFallbackClient(_payload())
    audit = _Audit()

    result = IntentPlanner(client, model="test-model").plan("清淡晚餐", audit_run=audit)

    assert result.executable
    assert result.response_format == "json_object"
    assert [call["response_format"]["type"] for call in client.calls] == ["json_schema", "json_object"]
    assert audit.events[0][2]["response_format"] == "json_object"


def test_schema_capability_fallback_does_not_accept_invalid_json_object():
    result = IntentPlanner(_SchemaFallbackClient('{"recipe_id":"forged"}'), model="test-model").plan("清淡晚餐")

    assert result.status == "PLANNER_INVALID_OUTPUT"
    assert not result.executable


def test_planner_prompt_freezes_generalized_preference_relationship_and_constraint_boundaries():
    prompt = IntentPlanner._system_prompt()

    assert "泛类食材只是偏好" in prompt
    assert "TECHNIQUE_SECTION" in prompt
    assert "保留 A、B 两个用户原话提及" in prompt
    assert "问句外壳" in prompt
    assert "没有已验证路径的要求不改变意图类型" in prompt
    assert "故障注入" in prompt
