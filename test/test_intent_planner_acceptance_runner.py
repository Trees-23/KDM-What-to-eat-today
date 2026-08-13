from __future__ import annotations

import importlib.util
import json
from pathlib import Path


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


def test_live_acceptance_report_rejects_incomplete_or_failed_rows(tmp_path):
    runner = _load(RUNNER_PATH, "intent_planner_acceptance_report")
    questions = [{"question_id": f"q-{number}"} for number in range(300)]
    metadata = {"implementation_commit": "a" * 40, "bank_sha256": "b" * 64, "questions": questions}
    rows = tmp_path / "rows.jsonl"
    rows.write_text(json.dumps({"question_id": "q-0", "status": "passed", "answer_chars": 1, "audit_id": "audit"}) + "\n", encoding="utf-8")

    report = runner._report(rows, tmp_path / "report.json", metadata)

    assert report["coverage_complete"] is False
    assert report["valid"] is False


def test_runtime_requires_planner_enabled_and_uses_isolated_s10_graph_fault():
    source = RUNTIME_PATH.read_text(encoding="utf-8")

    assert 'RETRIEVAL_INTENT_PLANNER_ENABLED' in source
    assert 'system.targeted_graph_retriever.driver = _UnavailableGraphDriver()' in source
    assert 'system._cleanup()' in source
    assert 'GENERATION_TIMEOUT_SECONDS = 60.0' in source
    assert 'with output_path.open("a", encoding="utf-8") as handle:' in source
