"""离线校验检索重构案例的证据、召回、延迟和禁止断言。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import quantiles
from typing import Any


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} 必须是对象")
    return value


def _expanded_cases(payload: dict[str, Any]) -> list[dict[str, Any]]:
    """以评审过的固定释义展开案例，拒绝机械重复同一查询。"""
    cases = payload.get("cases")
    repeats = payload.get("paraphrase_repetitions", 1)
    if not isinstance(cases, list) or not isinstance(repeats, int) or repeats < 1:
        raise ValueError("案例文件无效")
    if not cases:
        raise ValueError("案例文件不能为空")

    expanded = []
    case_ids: set[str] = set()
    queries: set[str] = set()
    for case in cases:
        if not isinstance(case, dict) or not isinstance(case.get("id"), str) or not case["id"]:
            raise ValueError("每个案例必须有 id")
        if case["id"] in case_ids:
            raise ValueError(f"案例 id 重复: {case['id']}")
        case_ids.add(case["id"])
        paraphrases = case.get("paraphrases")
        if not isinstance(paraphrases, list) or len(paraphrases) != repeats:
            raise ValueError(f"案例 {case['id']} 必须提供 {repeats} 条固定释义")
        if any(not isinstance(query, str) or not query.strip() for query in paraphrases):
            raise ValueError(f"案例 {case['id']} 的固定释义无效")
        if len(set(paraphrases)) != len(paraphrases):
            raise ValueError(f"案例 {case['id']} 的固定释义不能重复")
        for ordinal, query in enumerate(paraphrases, start=1):
            if query in queries:
                raise ValueError(f"固定释义在案例间重复: {query}")
            queries.add(query)
            item = dict(case)
            item["query"] = query
            item["evaluation_id"] = f"{case['id']}-p{ordinal}"
            expanded.append(item)

    required_count = payload.get("required_case_count")
    if required_count is not None and (not isinstance(required_count, int) or required_count != len(expanded)):
        raise ValueError("案例数量不符合 required_case_count")
    return expanded


def _strict_nutrition_claim_audit(row: dict[str, Any]) -> list[dict[str, Any]]:
    """返回严格营养断言的来源与验证结果，供报告审计。"""
    claims = []
    assertions = row.get("assertions") or []
    if isinstance(assertions, list):
        for assertion in assertions:
            if isinstance(assertion, str) and assertion in {"strict_nutrition_misclaim", "strict_low_fat_claim"}:
                claims.append({"assertion": str(assertion), "source": "assertions", "evidence_verified": False, "valid": False})

    nutrition_claims = row.get("nutrition_claims") or []
    if not isinstance(nutrition_claims, list):
        return claims + [{"assertion": "invalid_nutrition_claim", "source": "nutrition_claims", "evidence_verified": False, "valid": False}]
    for claim in nutrition_claims:
        if not isinstance(claim, dict) or claim.get("strict") is not True:
            continue
        assertion = claim.get("assertion")
        source = claim.get("evidence_source")
        valid = isinstance(assertion, str) and bool(assertion) and isinstance(source, str) and bool(source.strip()) and claim.get("evidence_verified") is True
        claims.append({
            "assertion": str(assertion or "strict_nutrition_claim"),
            "source": str(source or "missing"),
            "evidence_verified": claim.get("evidence_verified") is True,
            "policy_version": str(claim.get("policy_version") or ""),
            "valid": valid and bool(str(claim.get("policy_version") or "")) and str(source or "").startswith("governed:"),
        })
    return claims


def _baseline_metrics(baseline_report: dict[str, Any] | None) -> dict[str, float] | None:
    if not isinstance(baseline_report, dict):
        return None
    metrics = baseline_report.get("metrics")
    if not isinstance(metrics, dict):
        return None
    required = ("case_count", "recall_at_5", "mrr_at_5", "p95_latency_ms")
    if any(not isinstance(metrics.get(metric), (int, float)) for metric in required):
        return None
    return {metric: float(metrics[metric]) for metric in required}


def _evidence_links_valid(case: dict[str, Any], row: dict[str, Any], ranked: list[Any]) -> bool:
    links = row.get("evidence_links")
    if not isinstance(links, list) or not links:
        return False
    acceptable = set(case.get("acceptable_parent_ids") or case.get("gold_parent_ids") or [])
    retrieved = set(ranked)
    for link in links:
        if not isinstance(link, dict):
            return False
        if link.get("store") not in {"pds", "milvus"}:
            return False
        if not isinstance(link.get("build_id"), str) or not link["build_id"].strip():
            return False
        if not isinstance(link.get("parent_id"), str) or link["parent_id"] not in acceptable or link["parent_id"] not in retrieved:
            return False
        if not isinstance(link.get("evidence_id"), str) or not link["evidence_id"].strip():
            return False
    return True


def _fault_injection_violations(case: dict[str, Any], row: dict[str, Any], ranked: list[Any]) -> list[str]:
    expectation = case.get("fault_injection_expectation")
    if not expectation:
        return []
    violations = []
    if expectation == "entity_not_found_without_guess":
        if ranked or row.get("entity_status") != "not_found":
            violations.append("fault_injection_entity_guess")
    elif expectation == "graph_not_found_without_text_relation_proof":
        if row.get("graph_status") != "not_found" or row.get("graph_paths"):
            violations.append("fault_injection_relation_claim")
    elif expectation == "graph_unavailable_without_relation_claim":
        if row.get("graph_status") != "unavailable" or row.get("graph_paths"):
            violations.append("fault_injection_unavailable_claim")
    else:
        violations.append("unknown_fault_injection_expectation")
    return violations


def _string_list(value: Any) -> list[str]:
    return list(value) if isinstance(value, list) and all(isinstance(item, str) for item in value) else []


def _result_schema_valid(row: dict[str, Any]) -> bool:
    if any(not isinstance(row.get(field, []), list) or not all(isinstance(item, str) for item in row.get(field, [])) for field in ("retrieved_parent_ids", "evidence", "assertions", "graph_paths")):
        return False
    if "evidence_links" in row and not isinstance(row["evidence_links"], list):
        return False
    if "nutrition_claims" in row and not isinstance(row["nutrition_claims"], list):
        return False
    return row.get("graph_status") is None or isinstance(row["graph_status"], str)


def evaluate(
    cases_payload: dict[str, Any],
    thresholds: dict[str, Any],
    rows: list[dict[str, Any]],
    variant: str | None = None,
    baseline_report: dict[str, Any] | None = None,
    require_baseline: bool = False,
) -> dict[str, Any]:
    if variant:
        rows = [row for row in rows if isinstance(row, dict) and row.get("variant") == variant]
    cases = _expanded_cases(cases_payload)
    by_id: dict[str, dict[str, Any]] = {}
    duplicate_result_ids = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        evaluation_id = row.get("evaluation_id")
        if not isinstance(evaluation_id, str):
            continue
        if evaluation_id in by_id:
            duplicate_result_ids.append(evaluation_id)
        else:
            by_id[evaluation_id] = row

    outcomes = []
    reciprocal_ranks = []
    recalls = []
    forbidden = 0
    nutrition_misclaims = []
    nutrition_claims = []
    latencies = []
    missing_result_ids = []
    invalid_result_ids = []
    fault_injection_violations = []
    relation_path_violations = []
    relation_checks = []
    faithfulness_checks = []
    linkage_checks = []
    for case in cases:
        row = by_id.get(case["evaluation_id"])
        if row is None:
            missing_result_ids.append(case["evaluation_id"])
            row = {}
        if not _result_schema_valid(row):
            invalid_result_ids.append(case["evaluation_id"])
        ranked = _string_list(row.get("retrieved_parent_ids"))[:5]
        gold = set(case.get("acceptable_parent_ids") or case.get("gold_parent_ids") or [])
        rank = next((index + 1 for index, parent_id in enumerate(ranked) if parent_id in gold), None)
        recalls.append(1.0 if not gold or rank else 0.0)
        reciprocal_ranks.append(0.0 if rank is None else 1.0 / rank)
        evidence = set(_string_list(row.get("evidence")))
        graph_status = row.get("graph_status")
        complete = case.get("required_evidence") in evidence and (
            not case.get("required_graph_status") or graph_status == case["required_graph_status"]
        )
        claim_audit = _strict_nutrition_claim_audit(row)
        allowed_nutrition_claims = set(case.get("allowed_strict_nutrition_assertions") or [])
        for claim in claim_audit:
            claim["valid"] = claim["valid"] and claim["assertion"] in allowed_nutrition_claims
        assertions = set(_string_list(row.get("assertions")))
        assertions.update(claim["assertion"] for claim in claim_audit)
        violations = sorted(assertions & set(case.get("forbidden_assertions") or []))
        forbidden += len(violations)
        for claim in claim_audit:
            nutrition_claims.append({"evaluation_id": case["evaluation_id"], **claim})
        for violation in (claim for claim in claim_audit if not claim["valid"]):
            nutrition_misclaims.append({"evaluation_id": case["evaluation_id"], **violation})
        expected_paths = set(case.get("gold_relation_paths") or [])
        actual_paths = set(_string_list(row.get("graph_paths")))
        relation_correct = None
        if expected_paths:
            relation_correct = bool(expected_paths & actual_paths) and actual_paths <= expected_paths
            relation_checks.append(relation_correct)
        if actual_paths - expected_paths:
            relation_path_violations.append({"evaluation_id": case["evaluation_id"], "paths": sorted(actual_paths - expected_paths)})
        faithful = row.get("answer_faithful") is True
        faithfulness_checks.append(faithful)
        linkage_complete = None
        if case.get("requires_evidence_link") is True:
            linkage_complete = _evidence_links_valid(case, row, ranked)
            linkage_checks.append(linkage_complete)
        fault_violations = _fault_injection_violations(case, row, ranked)
        fault_injection_violations.extend({"evaluation_id": case["evaluation_id"], "assertion": item} for item in fault_violations)
        latency = row.get("latency_ms")
        if isinstance(latency, (int, float)) and latency >= 0:
            latencies.append(float(latency))
        outcomes.append(
            {
                "evaluation_id": case["evaluation_id"],
                "query": case["query"],
                "complete": complete,
                "violations": violations,
                "relation_path_correct": relation_correct,
                "answer_faithful": faithful,
                "evidence_linked": linkage_complete,
                "fault_injection_violations": fault_violations,
            }
        )

    p95 = quantiles(latencies, n=100, method="inclusive")[94] if len(latencies) >= 2 else (latencies[0] if latencies else None)
    case_count = len(cases)
    metrics = {
        "case_count": case_count,
        "result_coverage": (case_count - len(missing_result_ids)) / case_count,
        "latency_coverage": len(latencies) / case_count,
        "recall_at_5": sum(recalls) / case_count,
        "mrr_at_5": sum(reciprocal_ranks) / case_count,
        "evidence_completeness": sum(item["complete"] for item in outcomes) / case_count,
        "relation_path_correctness": sum(relation_checks) / len(relation_checks) if relation_checks else 1.0,
        "answer_faithfulness": sum(faithfulness_checks) / case_count,
        "evidence_linkage": sum(linkage_checks) / len(linkage_checks) if linkage_checks else 1.0,
        "forbidden_assertion_count": forbidden,
        "strict_nutrition_misclaim_count": len(nutrition_misclaims),
        "fault_injection_violation_count": len(fault_injection_violations),
        "relation_path_violation_count": len(relation_path_violations),
        "p95_latency_ms": p95,
    }
    errors = []
    if metrics["case_count"] < thresholds["min_case_count"]:
        errors.append("case_count")
    for threshold, metric in (
        ("result_coverage_min", "result_coverage"),
        ("latency_coverage_min", "latency_coverage"),
        ("evidence_completeness_min", "evidence_completeness"),
        ("relation_path_correctness_min", "relation_path_correctness"),
        ("answer_faithfulness_min", "answer_faithfulness"),
        ("evidence_linkage_min", "evidence_linkage"),
    ):
        if metrics[metric] < thresholds.get(threshold, 1.0):
            errors.append(metric)
    if forbidden > thresholds["forbidden_assertion_count_max"]:
        errors.append("forbidden_assertion_count")
    if len(nutrition_misclaims) > thresholds["strict_nutrition_misclaim_count_max"]:
        errors.append("strict_nutrition_misclaim_count")
    if len(fault_injection_violations) > thresholds.get("fault_injection_violation_count_max", 0):
        errors.append("fault_injection_violation_count")
    if relation_path_violations:
        errors.append("relation_path_violation_count")
    if duplicate_result_ids:
        errors.append("duplicate_evaluation_id")
    if invalid_result_ids:
        errors.append("invalid_result_schema")

    comparison = None
    comparison_thresholds = thresholds.get("new_vs_old")
    baseline_metrics = _baseline_metrics(baseline_report)
    if variant == "new" and (require_baseline or baseline_report is not None):
        baseline_valid = isinstance(baseline_report, dict) and baseline_report.get("valid") is True
        baseline_variant = isinstance(baseline_report, dict) and baseline_report.get("variant") == "old"
        same_cases = isinstance(baseline_report, dict) and baseline_report.get("cases_schema_version") == cases_payload.get("schema_version")
        same_thresholds = isinstance(baseline_report, dict) and baseline_report.get("thresholds_schema_version") == thresholds.get("schema_version")
        same_case_count = baseline_metrics is not None and baseline_metrics.get("case_count", metrics["case_count"]) == metrics["case_count"]
        if not isinstance(comparison_thresholds, dict) or baseline_metrics is None or not baseline_valid or not baseline_variant or not same_cases or not same_thresholds or not same_case_count:
            errors.append("baseline_report_required")
        elif baseline_metrics["p95_latency_ms"] <= 0:
            errors.append("baseline_p95_latency_ms")
        else:
            comparison = {
                "baseline_variant": comparison_thresholds.get("baseline_variant", "old"),
                "baseline_metrics": baseline_metrics,
                "recall_at_5_regression": baseline_metrics["recall_at_5"] - metrics["recall_at_5"],
                "mrr_at_5_regression": baseline_metrics["mrr_at_5"] - metrics["mrr_at_5"],
                "p95_latency_ratio": metrics["p95_latency_ms"] / baseline_metrics["p95_latency_ms"] if metrics["p95_latency_ms"] is not None else None,
            }
            if comparison["recall_at_5_regression"] > comparison_thresholds["recall_at_5_max_regression"]:
                errors.append("recall_at_5_regression")
            if comparison["mrr_at_5_regression"] > comparison_thresholds["mrr_at_5_max_regression"]:
                errors.append("mrr_at_5_regression")
            if comparison["p95_latency_ratio"] is None or comparison["p95_latency_ratio"] > comparison_thresholds["p95_latency_ratio_max"]:
                errors.append("p95_latency_ms")

    return {
        "valid": not errors,
        "metrics": metrics,
        "errors": errors,
        "outcomes": outcomes,
        "missing_result_ids": missing_result_ids,
        "duplicate_result_ids": duplicate_result_ids,
        "invalid_result_ids": invalid_result_ids,
        "strict_nutrition_misclaims": nutrition_misclaims,
        "strict_nutrition_claims": nutrition_claims,
        "relation_path_violations": relation_path_violations,
        "comparison": comparison,
        "cases_schema_version": cases_payload.get("schema_version"),
        "thresholds_schema_version": thresholds.get("schema_version"),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", required=True, type=Path)
    parser.add_argument("--thresholds", required=True, type=Path)
    parser.add_argument("--results", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--variant", required=True, choices=("old", "new"))
    parser.add_argument("--baseline-report", type=Path)
    args = parser.parse_args(argv)
    rows = [json.loads(line) for line in args.results.read_text(encoding="utf-8").splitlines() if line.strip()]
    baseline_report = _load_json(args.baseline_report) if args.baseline_report else None
    report = evaluate(
        _load_json(args.cases),
        _load_json(args.thresholds),
        rows,
        args.variant,
        baseline_report,
        require_baseline=args.variant == "new",
    )
    report["variant"] = args.variant
    report["baseline_report"] = args.baseline_report.name if args.baseline_report else None
    args.report.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"valid": report["valid"], "metrics": report["metrics"], "errors": report["errors"]}, ensure_ascii=False, sort_keys=True))
    return 0 if report["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
