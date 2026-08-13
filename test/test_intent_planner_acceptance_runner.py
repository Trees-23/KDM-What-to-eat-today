from __future__ import annotations

import importlib.util
import json
import time
from pathlib import Path

import pytest

from rag_modules.planner_acceptance_runtime import (
    QUESTION_TIMEOUT_SECONDS,
    _QuestionTimeoutError,
    _acceptance_request,
    _question_timeout,
    _status_for,
)
from rag_modules.retrieval_contracts import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = ROOT / "scripts" / "run_intent_planner_acceptance.py"
RUNTIME_PATH = ROOT / "rag_modules" / "planner_acceptance_runtime.py"


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_live_acceptance_runner_freezes_exactly_the_official_300_questions():
    runner = _load(RUNNER_PATH, "intent_planner_acceptance_runner")
    bank = runner._load_bank()

    assert len(bank["questions"]) == 300
    assert len({item["question_id"] for item in bank["questions"]}) == 300
    assert runner._RUNTIME_ENV["RETRIEVAL_INTENT_PLANNER_ENABLED"] == "true"
    assert runner._RUNTIME_ENV["ENABLE_RAG_AUDIT"] == "true"
    assert runner._RUNTIME_ENV["RETRIEVAL_MILVUS_V2_ENABLED"] == "true"


def test_live_acceptance_runner_applies_isolated_runtime_overrides_without_dropping_required_flags():
    runner = _load(RUNNER_PATH, "intent_planner_acceptance_runtime_env")

    environment = runner._runtime_environment([
        "NEO4J_URI=bolt://isolated:7687",
        "RETRIEVAL_PARENT_STORE_PATH=/app/run/isolated",
    ])

    assert environment["RETRIEVAL_INTENT_PLANNER_ENABLED"] == "true"
    assert environment["NEO4J_URI"] == "bolt://isolated:7687"
    assert environment["RETRIEVAL_PARENT_STORE_PATH"] == "/app/run/isolated"
    with pytest.raises(ValueError, match="KEY"):
        runner._runtime_environment(["neo4j_uri=bolt://isolated:7687"])
    with pytest.raises(ValueError, match="KEY=VALUE"):
        runner._runtime_environment(["NEO4J_URI"])


def test_live_acceptance_report_rejects_incomplete_or_failed_rows(tmp_path):
    runner = _load(RUNNER_PATH, "intent_planner_acceptance_report")
    questions = [{"question_id": f"q-{number}"} for number in range(300)]
    metadata = {"implementation_commit": "a" * 40, "bank_sha256": "b" * 64, "questions": questions}
    rows = tmp_path / "rows.jsonl"
    rows.write_text(json.dumps({"question_id": "q-0", "status": "passed", "answer_chars": 1, "audit_id": "audit"}) + "\n", encoding="utf-8")

    report = runner._report(rows, tmp_path / "report.json", metadata)

    assert report["coverage_complete"] is False
    assert report["valid"] is False


def test_live_acceptance_failure_summary_collects_failed_questions_with_audit_references(tmp_path):
    runner = _load(RUNNER_PATH, "intent_planner_acceptance_failure_summary")
    metadata = {"implementation_commit": "a" * 40, "bank_sha256": "b" * 64}
    rows = tmp_path / "rows.jsonl"
    rows.write_text(
        "\n".join(
            (
                json.dumps({"question_id": "q-pass", "status": "passed"}),
                json.dumps({"question_id": "q-fail", "scenario_id": "S06", "difficulty_code": "B", "input": "失败题", "status": "failed", "failures": ["empty_answer"], "limitations": ["VECTOR_UNAVAILABLE"], "query_plan": None, "audit_id": "audit-1", "audit_dir": "/audit-1"}),
            )
        ) + "\n",
        encoding="utf-8",
    )

    summary = runner._failure_summary(rows, tmp_path / "failure-summary.json", metadata)

    assert summary["question_count"] == 2
    assert summary["failed_count"] == 1
    assert summary["failures"] == [{"question_id": "q-fail", "scenario_id": "S06", "difficulty_code": "B", "input": "失败题", "failures": ["empty_answer"], "limitations": ["VECTOR_UNAVAILABLE"], "query_plan": None, "audit_id": "audit-1", "audit_dir": "/audit-1"}]


def test_failure_regression_freezes_only_source_failures_from_the_official_bank(tmp_path, monkeypatch):
    runner = _load(RUNNER_PATH, "intent_planner_failure_regression")
    monkeypatch.setattr(runner, "BANK", tmp_path / "bank.json")
    bank = {
        "questions": [
            {"question_id": f"q-{number}", "question": f"题目 {number}"}
            for number in range(300)
        ]
    }
    runner.BANK.write_text(json.dumps(bank), encoding="utf-8")
    source_rows = tmp_path / "new-results.jsonl"
    source_rows.write_text(json.dumps({"question_id": "q-8", "status": "failed"}) + "\n", encoding="utf-8")
    summary_path = tmp_path / "failure-summary.json"
    summary_path.write_text(
        json.dumps(
            {
                "bank_sha256": __import__("hashlib").sha256(runner.BANK.read_bytes()).hexdigest(),
                "implementation_commit": "a" * 40,
                "failure_result_file": source_rows.name,
                "failed_count": 2,
                "failures": [{"question_id": "q-8"}, {"question_id": "q-299"}],
            }
        ),
        encoding="utf-8",
    )

    metadata, _ = runner._load_failure_regression_questions(summary_path)

    assert metadata["execution_mode"] == "failure_regression"
    assert [question["question_id"] for question in metadata["questions"]] == ["q-8", "q-299"]
    assert metadata["source_failure_summary"]["source_rows_sha256"]


def test_failure_regression_report_rejects_rows_outside_frozen_failure_set(tmp_path):
    runner = _load(RUNNER_PATH, "intent_planner_failure_regression_report")
    metadata = {
        "implementation_commit": "a" * 40,
        "bank_sha256": "b" * 64,
        "source_failure_summary": {"sha256": "c" * 64},
        "questions": [{"question_id": "q-fail"}],
    }
    rows = tmp_path / "rows.jsonl"
    rows.write_text(json.dumps({"question_id": "q-other", "status": "passed", "answer_chars": 1, "audit_id": "audit"}) + "\n", encoding="utf-8")

    report = runner._regression_report(rows, tmp_path / "report.json", metadata)

    assert report["execution_mode"] == "failure_regression"
    assert report["source_failed_count"] == 1
    assert report["coverage_complete"] is False
    assert report["valid"] is False


def test_finalize_existing_failure_regression_writes_auditable_summary(tmp_path, monkeypatch):
    runner = _load(RUNNER_PATH, "intent_planner_finalize_existing")
    bank = tmp_path / "bank.json"
    bank.write_text(json.dumps({"questions": [{"question_id": f"q-{number}"} for number in range(300)]}), encoding="utf-8")
    monkeypatch.setattr(runner, "BANK", bank)
    source = tmp_path / "source"
    source.mkdir()
    (source / "new-results.jsonl").write_text(json.dumps({"question_id": "q-1", "status": "failed"}) + "\n", encoding="utf-8")
    summary = source / "failure-summary.json"
    summary.write_text(json.dumps({"bank_sha256": __import__("hashlib").sha256(bank.read_bytes()).hexdigest(), "implementation_commit": "a" * 40, "failure_result_file": "new-results.jsonl", "failed_count": 1, "failures": [{"question_id": "q-1"}]}), encoding="utf-8")
    output = tmp_path / "output"
    output.mkdir()
    (output / "new-results.jsonl").write_text(json.dumps({"question_id": "q-1", "status": "passed", "answer_chars": 4, "audit_id": "audit-1"}) + "\n", encoding="utf-8")

    assert runner.finalize_existing_failure_regression(output, summary) == 0
    assert json.loads((output / "acceptance-report.json").read_text(encoding="utf-8"))["passed_count"] == 1
    assert json.loads((output / "failure-summary.json").read_text(encoding="utf-8"))["failed_count"] == 0


def test_runtime_requires_planner_enabled_and_uses_isolated_s10_graph_fault():
    source = RUNTIME_PATH.read_text(encoding="utf-8")

    assert 'RETRIEVAL_INTENT_PLANNER_ENABLED' in source
    assert 'system.targeted_graph_retriever.driver = _UnavailableGraphDriver()' in source
    assert 'system._cleanup()' in source
    assert 'GENERATION_TIMEOUT_SECONDS = 60.0' in source
    assert 'with output_path.open("a", encoding="utf-8") as handle:' in source
    assert 'execution_mode == "failure_regression"' in source


def test_runtime_isolates_exam_constraints_before_planner_and_nutrition_input():
    preference = _acceptance_request(
        {
            "scenario_id": "S07",
            "question": "想喝一碗清淡些的川味汤。可以表达偏好匹配，但没有受治理营养来源时不要断言低脂。",
        }
    )
    fault = _acceptance_request(
        {
            "scenario_id": "S10",
            "question": "图服务暂不可用时，牛肉能做哪些菜？",
            "contract": {"gold_target": {"entity_name": "牛肉"}},
        }
    )

    assert preference.planner_input == "想喝一碗清淡些的川味汤。"
    assert "低脂" not in preference.nutrition_input
    assert fault.planner_input == "牛肉能做哪些菜？"
    assert fault.evaluation_constraints == "图服务暂不可用时，牛肉能做哪些菜？"


def test_runtime_accepts_local_strict_nutrition_gate_without_planner_event():
    failures = _status_for(
        {"scenario_id": "S07", "contract": {"gold_target": {}}},
        EvidenceBundle(None, (), (), (), ("NUTRITION_EVIDENCE_INSUFFICIENT", "INTENT_NON_EXECUTE")),
        [("intent_compile", "TERMINAL", {"compile_action": "NUTRITION_EVIDENCE_INSUFFICIENT"})],
        "当前没有受治理营养数据。",
    )

    assert "missing_planner_or_compile_audit" not in failures


def test_runtime_question_timeout_interrupts_a_single_question():
    started = time.monotonic()
    with pytest.raises(_QuestionTimeoutError):
        with _question_timeout(0.01):
            time.sleep(0.1)

    assert QUESTION_TIMEOUT_SECONDS >= 60
    assert time.monotonic() - started < 0.08
