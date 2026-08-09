import json
from pathlib import Path

import pytest

from scripts.run_retrieval_eval import _expanded_cases, evaluate, main


ROOT = Path(__file__).resolve().parents[1]


def _matching_rows(expanded, variant, latency_ms=10):
    return [
        {
            "evaluation_id": item["evaluation_id"],
            "retrieved_parent_ids": item.get("gold_parent_ids", []),
            "evidence": [item["required_evidence"]],
            "graph_status": item.get("required_graph_status"),
            "graph_paths": item.get("gold_relation_paths", []),
            "answer_faithful": True,
            "entity_status": "not_found" if item.get("intent") == "ENTITY_MISSING" else None,
            "evidence_links": [{"store": "pds", "build_id": "build-test", "parent_id": item["gold_parent_ids"][0], "evidence_id": item["evaluation_id"]}] if item.get("requires_evidence_link") else [],
            "latency_ms": latency_ms,
            "variant": variant,
        }
        for item in expanded
    ]


def test_cases_expand_to_frozen_minimum_with_distinct_fixed_paraphrases():
    cases = json.loads((ROOT / "eval/retrieval_refactor_cases.yaml").read_text(encoding="utf-8"))
    thresholds = json.loads((ROOT / "eval/retrieval_release_thresholds.yaml").read_text(encoding="utf-8"))
    expanded = _expanded_cases(cases)
    old_report = evaluate(cases, thresholds, _matching_rows(expanded, "old"), "old")
    old_report["variant"] = "old"
    new_report = evaluate(
        cases,
        thresholds,
        _matching_rows(expanded, "new"),
        "new",
        old_report,
        require_baseline=True,
    )

    assert len(expanded) == 50
    assert len({item["query"] for item in expanded}) == 50
    assert old_report["valid"] is True
    assert new_report["valid"] is True
    assert new_report["comparison"]["p95_latency_ratio"] == 1.0


def test_forbidden_assertion_and_strict_nutrition_misclaim_block_release_with_source():
    cases = {
        "required_case_count": 1,
        "paraphrase_repetitions": 1,
        "cases": [{"id": "x", "paraphrases": ["测试问题"], "gold_parent_ids": [], "required_evidence": "graph_not_found", "forbidden_assertions": ["text_as_relation_proof"]}],
    }
    thresholds = {
        "min_case_count": 1,
        "result_coverage_min": 1,
        "latency_coverage_min": 1,
        "evidence_completeness_min": 1,
        "forbidden_assertion_count_max": 0,
        "strict_nutrition_misclaim_count_max": 0,
        "fault_injection_violation_count_max": 0,
    }
    report = evaluate(
        cases,
        thresholds,
        [{
            "evaluation_id": "x-p1",
            "evidence": ["graph_not_found"],
            "assertions": ["text_as_relation_proof", "strict_low_fat_claim"],
            "answer_faithful": True,
            "latency_ms": 10,
        }],
    )

    assert report["valid"] is False
    assert "forbidden_assertion_count" in report["errors"]
    assert "strict_nutrition_misclaim_count" in report["errors"]
    assert report["strict_nutrition_misclaims"] == [{"evaluation_id": "x-p1", "assertion": "strict_low_fat_claim", "source": "assertions", "evidence_verified": False, "valid": False}]
    assert report["strict_nutrition_claims"] == report["strict_nutrition_misclaims"]


def test_new_path_requires_old_baseline_and_blocks_metric_regression():
    cases = {
        "required_case_count": 1,
        "paraphrase_repetitions": 1,
        "cases": [{"id": "x", "paraphrases": ["测试问题"], "gold_parent_ids": ["recipe-x"], "required_evidence": "text", "forbidden_assertions": []}],
    }
    thresholds = {
        "min_case_count": 1,
        "result_coverage_min": 1,
        "latency_coverage_min": 1,
        "evidence_completeness_min": 1,
        "forbidden_assertion_count_max": 0,
        "strict_nutrition_misclaim_count_max": 0,
        "fault_injection_violation_count_max": 0,
        "new_vs_old": {"recall_at_5_max_regression": 0.02, "mrr_at_5_max_regression": 0.02, "p95_latency_ratio_max": 1.2},
    }
    old_report = evaluate(cases, thresholds, [{"evaluation_id": "x-p1", "retrieved_parent_ids": ["recipe-x"], "evidence": ["text"], "answer_faithful": True, "latency_ms": 100, "variant": "old"}], "old")
    old_report["variant"] = "old"
    old_report["cases_schema_version"] = cases.get("schema_version")
    old_report["thresholds_schema_version"] = thresholds.get("schema_version")
    missing_baseline = evaluate(cases, thresholds, _matching_rows(_expanded_cases(cases), "new"), "new", require_baseline=True)
    regressed = evaluate(cases, thresholds, [{"evaluation_id": "x-p1", "retrieved_parent_ids": [], "evidence": ["text"], "answer_faithful": True, "latency_ms": 121, "variant": "new"}], "new", old_report, require_baseline=True)

    assert "baseline_report_required" in missing_baseline["errors"]
    assert "recall_at_5_regression" in regressed["errors"]
    assert "mrr_at_5_regression" in regressed["errors"]
    assert "p95_latency_ms" in regressed["errors"]


def test_fault_injection_fake_links_and_soft_strict_claims_cannot_bypass_release():
    cases = json.loads((ROOT / "eval/retrieval_refactor_cases.yaml").read_text(encoding="utf-8"))
    thresholds = json.loads((ROOT / "eval/retrieval_release_thresholds.yaml").read_text(encoding="utf-8"))
    expanded = _expanded_cases(cases)

    fault_rows = _matching_rows(expanded, "old")
    for item, row in zip(expanded, fault_rows):
        if item.get("fault_injection_expectation"):
            row["retrieved_parent_ids"] = ["guessed-parent"]
            row["graph_paths"] = ["forged-path"]
    fault_report = evaluate(cases, thresholds, fault_rows, "old")

    fake_link_rows = _matching_rows(expanded, "old")
    for item, row in zip(expanded, fake_link_rows):
        if item.get("requires_evidence_link"):
            row["evidence_links"] = ["fake"]
    fake_link_report = evaluate(cases, thresholds, fake_link_rows, "old")

    strict_claim_rows = _matching_rows(expanded, "old")
    for item, row in zip(expanded, strict_claim_rows):
        if item["intent"] == "SOFT_PREFERENCE":
            row["nutrition_claims"] = [{"strict": True, "assertion": "strict_low_fat_claim", "evidence_source": "fake", "evidence_verified": True}]
    strict_claim_report = evaluate(cases, thresholds, strict_claim_rows, "old")

    assert "fault_injection_violation_count" in fault_report["errors"]
    assert "evidence_linkage" in fake_link_report["errors"]
    assert "forbidden_assertion_count" in strict_claim_report["errors"]


def test_new_path_rejects_untrusted_or_wrong_baseline_report():
    cases = json.loads((ROOT / "eval/retrieval_refactor_cases.yaml").read_text(encoding="utf-8"))
    thresholds = json.loads((ROOT / "eval/retrieval_release_thresholds.yaml").read_text(encoding="utf-8"))
    expanded = _expanded_cases(cases)
    baseline = evaluate(cases, thresholds, _matching_rows(expanded, "old"), "old")
    forged_baseline = {"variant": "new", "valid": False, "metrics": baseline["metrics"], "cases_schema_version": cases["schema_version"], "thresholds_schema_version": thresholds["schema_version"]}
    report = evaluate(cases, thresholds, _matching_rows(expanded, "new"), "new", forged_baseline, require_baseline=True)

    assert "baseline_report_required" in report["errors"]


def test_duplicate_empty_cases_and_malformed_result_rows_fail_closed():
    with pytest.raises(ValueError, match="不能为空"):
        _expanded_cases({"cases": [], "paraphrase_repetitions": 1})
    with pytest.raises(ValueError, match="id 重复"):
        _expanded_cases({"cases": [{"id": "x", "paraphrases": ["一"]}, {"id": "x", "paraphrases": ["二"]}], "paraphrase_repetitions": 1})

    cases = {"required_case_count": 1, "paraphrase_repetitions": 1, "cases": [{"id": "x", "paraphrases": ["测试问题"], "gold_parent_ids": [], "required_evidence": "entity_not_found", "forbidden_assertions": []}]}
    thresholds = {"min_case_count": 1, "result_coverage_min": 1, "latency_coverage_min": 1, "evidence_completeness_min": 1, "forbidden_assertion_count_max": 0, "strict_nutrition_misclaim_count_max": 0}
    report = evaluate(cases, thresholds, [{"evaluation_id": "x-p1", "retrieved_parent_ids": "not-a-list", "evidence": {"entity_not_found": True}, "assertions": [{}], "latency_ms": 1, "answer_faithful": True}])

    assert "invalid_result_schema" in report["errors"]


def test_cli_writes_comparison_report_and_nonzero_on_latency_regression(tmp_path):
    cases_path = ROOT / "eval/retrieval_refactor_cases.yaml"
    thresholds_path = ROOT / "eval/retrieval_release_thresholds.yaml"
    expanded = _expanded_cases(json.loads(cases_path.read_text(encoding="utf-8")))
    results_path = tmp_path / "results.jsonl"
    old_report_path = tmp_path / "old-report.json"
    new_report_path = tmp_path / "new-report.json"

    results_path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in _matching_rows(expanded, "old", 100)) + "\n", encoding="utf-8")
    assert main(["--cases", str(cases_path), "--thresholds", str(thresholds_path), "--results", str(results_path), "--report", str(old_report_path), "--variant", "old"]) == 0

    results_path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in _matching_rows(expanded, "new", 121)) + "\n", encoding="utf-8")
    assert main(["--cases", str(cases_path), "--thresholds", str(thresholds_path), "--results", str(results_path), "--report", str(new_report_path), "--variant", "new", "--baseline-report", str(old_report_path)]) == 2
    new_report = json.loads(new_report_path.read_text(encoding="utf-8"))
    assert new_report["comparison"]["baseline_metrics"]["p95_latency_ms"] == 100.0
    assert "p95_latency_ms" in new_report["errors"]
