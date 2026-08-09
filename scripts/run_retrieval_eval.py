"""离线校验检索重构案例的证据、召回和禁止断言。"""

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
    cases = payload.get("cases")
    repeats = payload.get("paraphrase_repetitions", 1)
    if not isinstance(cases, list) or not isinstance(repeats, int) or repeats < 1:
        raise ValueError("案例文件无效")
    expanded = []
    for case in cases:
        if not isinstance(case, dict) or not case.get("id"):
            raise ValueError("每个案例必须有 id")
        for ordinal in range(1, repeats + 1):
            item = dict(case)
            item["evaluation_id"] = f"{case['id']}-p{ordinal}"
            expanded.append(item)
    return expanded


def evaluate(cases_payload: dict[str, Any], thresholds: dict[str, Any], rows: list[dict[str, Any]], variant: str | None = None) -> dict[str, Any]:
    if variant:
        rows = [row for row in rows if row.get("variant") == variant]
    cases = _expanded_cases(cases_payload)
    by_id = {str(row.get("evaluation_id")): row for row in rows if isinstance(row, dict)}
    outcomes = []
    reciprocal_ranks = []
    recalls = []
    forbidden = 0
    nutrition_misclaims = 0
    latencies = []
    for case in cases:
        row = by_id.get(case["evaluation_id"], {})
        ranked = list(row.get("retrieved_parent_ids") or [])[:5]
        gold = set(case.get("gold_parent_ids") or [])
        rank = next((index + 1 for index, parent_id in enumerate(ranked) if parent_id in gold), None)
        recalls.append(1.0 if not gold or rank else 0.0)
        reciprocal_ranks.append(0.0 if rank is None else 1.0 / rank)
        evidence = set(row.get("evidence") or [])
        graph_status = row.get("graph_status")
        complete = case.get("required_evidence") in evidence and (
            not case.get("required_graph_status") or graph_status == case["required_graph_status"]
        )
        assertions = set(row.get("assertions") or [])
        violations = sorted(assertions & set(case.get("forbidden_assertions") or []))
        forbidden += len(violations)
        nutrition_misclaims += int("strict_nutrition_misclaim" in assertions)
        latency = row.get("latency_ms")
        if isinstance(latency, (int, float)) and latency >= 0:
            latencies.append(float(latency))
        outcomes.append({"evaluation_id": case["evaluation_id"], "complete": complete, "violations": violations})
    p95 = quantiles(latencies, n=100, method="inclusive")[94] if len(latencies) >= 2 else (latencies[0] if latencies else None)
    metrics = {
        "case_count": len(cases), "recall_at_5": sum(recalls) / len(cases), "mrr_at_5": sum(reciprocal_ranks) / len(cases),
        "evidence_completeness": sum(item["complete"] for item in outcomes) / len(cases), "forbidden_assertion_count": forbidden,
        "strict_nutrition_misclaim_count": nutrition_misclaims, "p95_latency_ms": p95,
    }
    errors = []
    for key, metric, comparator in (("recall_at_5_min", "recall_at_5", "min"), ("mrr_at_5_min", "mrr_at_5", "min"), ("evidence_completeness_min", "evidence_completeness", "min")):
        if metrics[metric] < thresholds[key]: errors.append(metric)
    if metrics["case_count"] < thresholds["min_case_count"]: errors.append("case_count")
    if forbidden > thresholds["forbidden_assertion_count_max"]: errors.append("forbidden_assertion_count")
    if nutrition_misclaims > thresholds["strict_nutrition_misclaim_count_max"]: errors.append("strict_nutrition_misclaim_count")
    baseline = thresholds.get("baseline_p95_latency_ms")
    if p95 is None or not isinstance(baseline, (int, float)) or p95 > baseline * thresholds["p95_latency_ratio_max"]:
        errors.append("p95_latency_ms")
    return {"valid": not errors, "metrics": metrics, "errors": errors, "outcomes": outcomes}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", required=True, type=Path); parser.add_argument("--thresholds", required=True, type=Path)
    parser.add_argument("--results", required=True, type=Path); parser.add_argument("--report", required=True, type=Path); parser.add_argument("--variant", choices=("old", "new"))
    args = parser.parse_args(argv)
    rows = [json.loads(line) for line in args.results.read_text(encoding="utf-8").splitlines() if line.strip()]
    report = evaluate(_load_json(args.cases), _load_json(args.thresholds), rows, args.variant)
    report["variant"] = args.variant
    args.report.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"valid": report["valid"], "metrics": report["metrics"]}, ensure_ascii=False, sort_keys=True))
    return 0 if report["valid"] else 2


if __name__ == "__main__": raise SystemExit(main())
