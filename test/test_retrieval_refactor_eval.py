import json
from pathlib import Path

from scripts.run_retrieval_eval import _expanded_cases, evaluate


ROOT = Path(__file__).resolve().parents[1]


def test_cases_expand_to_frozen_minimum_and_pass_with_matching_evidence():
    cases = json.loads((ROOT / "eval/retrieval_refactor_cases.yaml").read_text(encoding="utf-8"))
    thresholds = json.loads((ROOT / "eval/retrieval_release_thresholds.yaml").read_text(encoding="utf-8"))
    expanded = _expanded_cases(cases)
    rows = [
        {"evaluation_id": item["evaluation_id"], "retrieved_parent_ids": item.get("gold_parent_ids", []),
         "evidence": [item["required_evidence"]], "graph_status": item.get("required_graph_status"), "latency_ms": 10, "variant": "new"}
        for item in expanded
    ]
    report = evaluate(cases, thresholds, rows, "new")
    assert len(expanded) == 50
    assert report["valid"] is True


def test_forbidden_assertion_blocks_release():
    cases = {"cases": [{"id": "x", "gold_parent_ids": [], "required_evidence": "graph_not_found", "forbidden_assertions": ["text_as_relation_proof"]}], "paraphrase_repetitions": 1}
    thresholds = {"min_case_count": 1, "recall_at_5_min": 0, "mrr_at_5_min": 0, "evidence_completeness_min": 1, "forbidden_assertion_count_max": 0, "strict_nutrition_misclaim_count_max": 0, "baseline_p95_latency_ms": 100, "p95_latency_ratio_max": 1.2}
    report = evaluate(cases, thresholds, [{"evaluation_id": "x-p1", "evidence": ["graph_not_found"], "assertions": ["text_as_relation_proof"]}])
    assert report["valid"] is False
    assert "forbidden_assertion_count" in report["errors"]
