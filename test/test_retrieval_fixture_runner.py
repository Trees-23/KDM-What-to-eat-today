import copy
import hashlib
import json
from pathlib import Path

from scripts.run_retrieval_eval import evaluate
from scripts.run_retrieval_fixture_eval import EVIDENCE_MODE, run_fixture_evaluation


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "eval/retrieval_refactor_cases.yaml"
FIXTURE = ROOT / "eval/retrieval_component_fixture_v1.json"
THRESHOLDS = ROOT / "eval/retrieval_release_thresholds.yaml"


def test_fixture_runner_executes_old_and_new_components_without_reading_gold_fields(tmp_path):
    old_rows = run_fixture_evaluation(cases_path=CASES, fixture_path=FIXTURE, variant="old")
    new_rows = run_fixture_evaluation(cases_path=CASES, fixture_path=FIXTURE, variant="new")

    altered_cases = json.loads(CASES.read_text(encoding="utf-8"))
    altered_cases = copy.deepcopy(altered_cases)
    for case in altered_cases["cases"]:
        for field in tuple(case):
            if field.startswith("gold_") or field == "acceptable_parent_ids":
                case[field] = [f"forged-{field}"]
    altered_cases_path = tmp_path / "altered-cases.json"
    altered_cases_path.write_text(json.dumps(altered_cases, ensure_ascii=False), encoding="utf-8")

    assert len(old_rows) == len(new_rows) == 50
    assert run_fixture_evaluation(cases_path=altered_cases_path, fixture_path=FIXTURE, variant="old") == old_rows
    assert run_fixture_evaluation(cases_path=altered_cases_path, fixture_path=FIXTURE, variant="new") == new_rows
    assert all(row["provenance"]["evidence_mode"] == EVIDENCE_MODE for row in old_rows + new_rows)
    assert all(row["provenance"]["live_services"] is False for row in old_rows + new_rows)
    assert any("HybridRetrievalModule.hybrid_search" in row["provenance"]["components"] for row in old_rows)
    assert any("RestrictedVectorRetriever" in row["provenance"]["components"] for row in new_rows)


def test_fixture_provenance_is_bound_to_runner_fixture_variant_and_route_components():
    cases = {"required_case_count": 1, "paraphrase_repetitions": 1, "cases": [{"id": "x", "paraphrases": ["不存在的菜怎么做"], "gold_parent_ids": [], "required_evidence": "entity_not_found", "forbidden_assertions": []}]}
    thresholds = {"min_case_count": 1, "result_coverage_min": 1, "latency_coverage_min": 1, "evidence_completeness_min": 1, "forbidden_assertion_count_max": 0, "strict_nutrition_misclaim_count_max": 0}
    expected_provenance = {"runner_id": "fixture-runner", "fixture_sha256": "a" * 64, "variant": "old", "component_requirements": {"entity_missing": ["FixtureEntityResolver"]}}
    row = {"evaluation_id": "x-p1", "variant": "old", "retrieved_parent_ids": [], "evidence": ["entity_not_found"], "assertions": [], "graph_paths": [], "entity_ids": [], "evidence_links": [], "answer_faithful": True, "latency_ms": 1, "provenance": {"evidence_mode": EVIDENCE_MODE, "runner_id": "fixture-runner", "fixture_sha256": "a" * 64, "variant": "old", "route": "entity_missing", "live_services": False, "components": ["FixtureEntityResolver"]}}

    passing = evaluate(cases, thresholds, [row], required_evidence_mode=EVIDENCE_MODE, expected_provenance=expected_provenance)
    forged = copy.deepcopy(row)
    forged["provenance"].update(runner_id="forged-runner", fixture_sha256="0" * 64, components=["forged-component"])
    report = evaluate(cases, thresholds, [forged], required_evidence_mode=EVIDENCE_MODE, expected_provenance=expected_provenance)

    assert passing["valid"] is True
    assert "runner_provenance_required" in report["errors"]


def test_checked_in_fixture_evidence_has_matching_hashes_and_explicit_limitations():
    artifact_dir = ROOT / "eval/artifacts/retrieval-fixture-v1"
    manifest = json.loads((artifact_dir / "manifest.json").read_text(encoding="utf-8"))

    for item in manifest["inputs"].values():
        path = ROOT / item["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]
    for item in manifest["artifacts"].values():
        path = artifact_dir / item["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]

    new_report = json.loads((artifact_dir / "new-report.json").read_text(encoding="utf-8"))
    assert manifest["evidence_mode"] == EVIDENCE_MODE
    assert new_report["valid"] is True
    assert new_report["required_evidence_mode"] == EVIDENCE_MODE
    assert new_report["comparison"]["p95_latency_gate"] == "not_applicable_fixture_component_budget"
    assert "new_vs_old.p95_latency_ratio_max" in new_report["skipped_thresholds"]
    assert any("不连接真实 Neo4j" in item for item in manifest["limitations"])
