#!/usr/bin/env python3
"""将独立监考生成的 JSONL 结果汇总为总评与逐题路径报告。"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import median
from typing import Any, Iterable


RANK_CUTOFFS = (1, 3, 5)
REQUIRED_RESULT_FIELDS = frozenset(
    {
        "question_id", "scenario_id", "difficulty_code", "variant", "evaluation_mode", "status",
        "route", "path", "checks", "timing",
    }
)
REQUIRED_PATH_FIELDS = frozenset(
    {
        "entity_resolution", "query_plan", "graph_template", "graph_paths", "vector_scope",
        "pds_hydration", "final_evidence",
    }
)
REQUIRED_CHECK_FIELDS = frozenset(
    {
        "route_correct", "evidence_complete", "evidence_linked", "answer_faithful", "safety_pass",
        "forbidden_assertion_count", "unsupported_relation_claim_count", "strict_nutrition_misreport_count",
    }
)
REQUIRED_TIMING_FIELDS = frozenset({"ttft_ms", "total_latency_ms"})


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} 必须是 JSON 对象")
    return value


def _load_jsonl(paths: Iterable[Path]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in paths:
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number} 必须是 JSON 对象")
            value["_result_file"] = str(path)
            value["_result_line"] = line_number
            rows.append(value)
    return rows


def _finite(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    converted = float(value)
    return converted if math.isfinite(converted) else None


def _ratio(numerator: int, denominator: int) -> float | None:
    return numerator / denominator if denominator else None


def _format_number(value: float | None) -> str:
    return "-" if value is None else f"{value:.3f}"


def _p95(values: list[float]) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    index = max(0, math.ceil(len(ordered) * 0.95) - 1)
    return ordered[index]


def _ranking_items(row: dict[str, Any]) -> list[dict[str, Any]]:
    ranking = row.get("ranking")
    if not isinstance(ranking, list):
        return []
    unique: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in ranking:
        if not isinstance(item, dict) or not isinstance(item.get("key"), str) or item["key"] in seen:
            continue
        seen.add(item["key"])
        unique.append(item)
    return unique


def _gold_items(row: dict[str, Any]) -> list[dict[str, Any]]:
    gold = row.get("gold_items")
    if not isinstance(gold, list):
        return []
    valid = []
    for item in gold:
        if not isinstance(item, dict) or not isinstance(item.get("key"), str):
            continue
        relevance = _finite(item.get("relevance"))
        if relevance is not None and relevance > 0:
            valid.append({"key": item["key"], "relevance": relevance})
    return valid


def _ranking_metrics(row: dict[str, Any]) -> dict[str, float] | None:
    if row.get("status") != "completed":
        return None
    gold = _gold_items(row)
    if not gold:
        return None
    ranking = _ranking_items(row)
    relevance_by_key = {item["key"]: item["relevance"] for item in gold}
    values = [relevance_by_key.get(item["key"], 0.0) for item in ranking[:5]]
    relevant_gold_count = len(relevance_by_key)
    metrics: dict[str, float] = {}
    for cutoff in RANK_CUTOFFS:
        top = values[:cutoff]
        metrics[f"recall_at_{cutoff}"] = sum(value > 0 for value in top) / relevant_gold_count
        metrics[f"precision_at_{cutoff}"] = sum(value > 0 for value in top) / cutoff
        metrics[f"hit_rate_at_{cutoff}"] = 1.0 if any(value > 0 for value in top) else 0.0
    rank = next((index + 1 for index, value in enumerate(values) if value > 0), None)
    metrics["mrr_at_5"] = 0.0 if rank is None else 1.0 / rank
    dcg = sum((2**value - 1) / math.log2(index + 2) for index, value in enumerate(values))
    ideal = sorted(relevance_by_key.values(), reverse=True)[:5]
    idcg = sum((2**value - 1) / math.log2(index + 2) for index, value in enumerate(ideal))
    metrics["ndcg_at_5"] = dcg / idcg if idcg else 0.0
    return metrics


def _boolean_check(row: dict[str, Any], key: str) -> bool | None:
    checks = row.get("checks")
    return checks.get(key) if isinstance(checks, dict) and isinstance(checks.get(key), bool) else None


def _row_issues(row: dict[str, Any]) -> list[str]:
    issues = [f"缺少顶层字段 {key}" for key in sorted(REQUIRED_RESULT_FIELDS - set(row))]
    if row.get("variant") not in {"old", "new"}:
        issues.append("variant 不是 old/new")
    if row.get("status") not in {"completed", "blocked", "error"}:
        issues.append("status 非法")
    path = row.get("path")
    if not isinstance(path, dict):
        issues.append("path 不是对象")
    else:
        issues.extend(f"path 缺少 {key}" for key in sorted(REQUIRED_PATH_FIELDS - set(path)))
    checks = row.get("checks")
    if not isinstance(checks, dict):
        issues.append("checks 不是对象")
    else:
        issues.extend(f"checks 缺少 {key}" for key in sorted(REQUIRED_CHECK_FIELDS - set(checks)))
    timing = row.get("timing")
    if not isinstance(timing, dict):
        issues.append("timing 不是对象")
    else:
        issues.extend(f"timing 缺少 {key}" for key in sorted(REQUIRED_TIMING_FIELDS - set(timing)))
    if not isinstance(row.get("route"), dict):
        issues.append("route 不是对象")
    if row.get("evaluation_mode") == "ranking" and row.get("status") == "completed":
        if not isinstance(row.get("ranking"), list):
            issues.append("已完成排名题缺少 ranking")
        if not isinstance(row.get("gold_items"), list):
            issues.append("已完成排名题缺少 gold_items")
    return issues


def _group_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    ranking_rows = [row for row in rows if _ranking_metrics(row) is not None]
    safety_rows = [row for row in rows if row.get("evaluation_mode") == "safety" and row.get("status") == "completed"]
    completed = [row for row in rows if row.get("status") == "completed"]
    blocked = [row for row in rows if row.get("status") == "blocked"]
    errors = [row for row in rows if row.get("status") == "error"]
    values: dict[str, list[float]] = defaultdict(list)
    for row in ranking_rows:
        for key, value in (_ranking_metrics(row) or {}).items():
            values[key].append(value)
    for check_key, metric_name in (
        ("route_correct", "route_accuracy"),
        ("evidence_complete", "evidence_completeness"),
        ("evidence_linked", "evidence_linkage"),
        ("answer_faithful", "answer_faithfulness"),
    ):
        checks = [_boolean_check(row, check_key) for row in ranking_rows]
        valid = [value for value in checks if value is not None]
        if valid:
            values[metric_name].append(sum(valid) / len(valid))
    safety = [_boolean_check(row, "safety_pass") for row in safety_rows]
    safety_valid = [value for value in safety if value is not None]
    if safety_valid:
        values["safety_pass_rate"].append(sum(safety_valid) / len(safety_valid))
    forbidden = []
    relation_claims = []
    strict_nutrition_claims = []
    ttft = []
    total_latency = []
    for row in rows:
        checks = row.get("checks") if isinstance(row.get("checks"), dict) else {}
        forbidden_value = _finite(checks.get("forbidden_assertion_count"))
        if forbidden_value is not None:
            forbidden.append(forbidden_value)
        relation_value = _finite(checks.get("unsupported_relation_claim_count"))
        if relation_value is not None:
            relation_claims.append(relation_value)
        strict_nutrition_value = _finite(checks.get("strict_nutrition_misreport_count"))
        if strict_nutrition_value is not None:
            strict_nutrition_claims.append(strict_nutrition_value)
        timing = row.get("timing") if isinstance(row.get("timing"), dict) else {}
        ttft_value = _finite(timing.get("ttft_ms"))
        total_value = _finite(timing.get("total_latency_ms"))
        if ttft_value is not None:
            ttft.append(ttft_value)
        if total_value is not None:
            total_latency.append(total_value)
    result = {key: sum(items) / len(items) for key, items in values.items() if items}
    result.update(
        {
            "row_count": len(rows),
            "completed_count": len(completed),
            "blocked_count": len(blocked),
            "error_count": len(errors),
            "ranking_count": len(ranking_rows),
            "safety_count": len(safety_rows),
            "forbidden_assertion_count": sum(forbidden) if forbidden else None,
            "unsupported_relation_claim_count": sum(relation_claims) if relation_claims else None,
            "strict_nutrition_misreport_count": sum(strict_nutrition_claims) if strict_nutrition_claims else None,
            "ttft_p50_ms": median(ttft) if ttft else None,
            "ttft_p95_ms": _p95(ttft),
            "total_latency_p50_ms": median(total_latency) if total_latency else None,
            "total_latency_p95_ms": _p95(total_latency),
        }
    )
    return result


def _markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    line = "| " + " | ".join(headers) + " |"
    divider = "| " + " | ".join("---" for _ in headers) + " |"
    return "\n".join([line, divider] + ["| " + " | ".join(row) + " |" for row in rows])


def _summary_table(metrics: dict[str, Any]) -> list[str]:
    keys = [
        "recall_at_1", "recall_at_3", "recall_at_5", "precision_at_1", "precision_at_3", "precision_at_5",
        "mrr_at_5", "ndcg_at_5", "hit_rate_at_5", "route_accuracy", "evidence_completeness", "evidence_linkage",
        "answer_faithfulness", "safety_pass_rate", "forbidden_assertion_count", "unsupported_relation_claim_count",
        "ttft_p50_ms", "ttft_p95_ms", "total_latency_p50_ms", "total_latency_p95_ms",
    ]
    return [f"- `{key}`：{_format_number(_finite(metrics.get(key)))}" for key in keys]


def _render_detail(rows: list[dict[str, Any]], questions_by_id: dict[str, dict[str, Any]]) -> str:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("question_id", "<missing>"))].append(row)
    lines = ["# 路径与召回明细", "", "本文件保留每题各变体的检索路径、候选、PDS 回补、最终证据和回答，用于人工复核。", ""]
    for question_id in sorted(grouped):
        question = questions_by_id.get(question_id, {})
        lines.extend([f"## {question_id}", "", f"- 题干：{question.get('question', '<题库中不存在>')}", f"- 场景：{question.get('scenario_id', '-')}", f"- 难度：{question.get('difficulty_name', '-')}", ""])
        for row in sorted(grouped[question_id], key=lambda item: str(item.get("variant", ""))):
            path = row.get("path") if isinstance(row.get("path"), dict) else {}
            ranking = _ranking_items(row)
            lines.extend([f"### 变体：{row.get('variant', '<missing>')}", "", f"- 状态：{row.get('status', '<missing>')}", f"- 审计 ID：{row.get('audit_id', '<missing>')}", f"- 观测路由：{json.dumps(row.get('route', {}), ensure_ascii=False)}", f"- 实体解析：{json.dumps(path.get('entity_resolution', []), ensure_ascii=False)}", f"- QueryPlan：{json.dumps(path.get('query_plan', {}), ensure_ascii=False)}", f"- 图模板：{path.get('graph_template', '-')}", f"- 图路径：{json.dumps(path.get('graph_paths', []), ensure_ascii=False)}", f"- 向量范围：{json.dumps(path.get('vector_scope', {}), ensure_ascii=False)}", "", "#### 排名候选", ""])
            if ranking:
                lines.append(_markdown_table(["rank", "key", "name", "score", "source"], [[str(index), str(item.get("key", "")), str(item.get("name", "")), str(item.get("score", "")), str(item.get("source", ""))] for index, item in enumerate(ranking, start=1)]))
            else:
                lines.append("_无排名候选或该题属于安全场景。_")
            lines.extend(["", "#### PDS 回补与最终证据", "", f"- PDS 回补：{json.dumps(path.get('pds_hydration', []), ensure_ascii=False)}", f"- 最终证据：{json.dumps(path.get('final_evidence', []), ensure_ascii=False)}", f"- 检查结果：{json.dumps(row.get('checks', {}), ensure_ascii=False)}", "", "#### 最终回答", "", "```text", str(row.get("answer", "")), "```", ""])
    return "\n".join(lines)


def _render_summary(bank: dict[str, Any], rows: list[dict[str, Any]]) -> str:
    questions = bank.get("questions") if isinstance(bank.get("questions"), list) else []
    question_ids = {item.get("question_id") for item in questions if isinstance(item, dict)}
    expected = len(question_ids)
    variants = sorted({str(row.get("variant")) for row in rows if row.get("variant")})
    duplicate_keys: list[str] = []
    seen: set[tuple[str, str]] = set()
    for row in rows:
        key = (str(row.get("question_id")), str(row.get("variant")))
        if key in seen:
            duplicate_keys.append("/".join(key))
        seen.add(key)
    unknown = sorted({str(row.get("question_id")) for row in rows if row.get("question_id") not in question_ids})
    row_issues = [
        (str(row.get("question_id", "<missing>")), str(row.get("variant", "<missing>")), issue)
        for row in rows
        for issue in _row_issues(row)
    ]
    lines = ["# 检索重构真实场景考试总评", "", "## 执行完整性", "", f"- 题库声明题数：`{expected}`", f"- 已发现变体：`{', '.join(variants) if variants else '无'}`", f"- 结果行数：`{len(rows)}`", f"- 重复题目/变体行：`{len(duplicate_keys)}`", f"- 不在题库中的结果行：`{len(unknown)}`", f"- 关键字段格式问题：`{len(row_issues)}`", ""]
    if row_issues:
        lines.extend(["### 格式问题示例", ""])
        lines.extend(f"- `{question_id}` / `{variant}`：{issue}" for question_id, variant, issue in row_issues[:20])
        lines.append("")
    coverage_rows = []
    for variant in variants:
        variant_rows = [row for row in rows if row.get("variant") == variant]
        actual = {str(row.get("question_id")) for row in variant_rows}
        completed_count = sum(row.get("status") == "completed" for row in variant_rows)
        blocked_count = sum(row.get("status") == "blocked" for row in variant_rows)
        error_count = sum(row.get("status") == "error" for row in variant_rows)
        coverage_rows.append([variant, str(len(actual)), str(expected), _format_number(_ratio(len(actual), expected)), str(len(question_ids - actual)), str(completed_count), str(blocked_count), str(error_count)])
    lines.extend(["## 变体覆盖率", "", _markdown_table(["变体", "已记录题", "应完成题", "记录覆盖率", "缺失题", "完成行", "blocked", "error"], coverage_rows) if coverage_rows else "_尚未写入结果。_", ""])
    all_by_variant: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        all_by_variant[str(row.get("variant", "<missing>"))].append(row)
    lines.extend(["## 总体指标", "", "以下排名与安全指标仅统计状态为 `completed` 的可评分行；`blocked` 和 `error` 会在覆盖率中保留，不能被当作通过。", ""])
    metric_rows = []
    for variant in variants:
        metrics = _group_metrics(all_by_variant[variant])
        metric_rows.append([variant, _format_number(_finite(metrics.get("recall_at_5"))), _format_number(_finite(metrics.get("mrr_at_5"))), _format_number(_finite(metrics.get("ndcg_at_5"))), _format_number(_finite(metrics.get("route_accuracy"))), _format_number(_finite(metrics.get("evidence_linkage"))), _format_number(_finite(metrics.get("safety_pass_rate"))), _format_number(_finite(metrics.get("total_latency_p95_ms")))])
    lines.extend([_markdown_table(["变体", "Recall@5", "MRR@5", "nDCG@5", "路由准确率", "证据链接率", "安全通过率", "P95 总耗时 ms"], metric_rows) if metric_rows else "_尚未写入结果。_", ""])
    lines.extend(["## 完整指标", ""])
    detail_metric_keys = [
        "recall_at_1", "recall_at_3", "recall_at_5", "precision_at_1", "precision_at_3", "precision_at_5",
        "hit_rate_at_1", "hit_rate_at_3", "hit_rate_at_5", "mrr_at_5", "ndcg_at_5", "route_accuracy",
        "evidence_completeness", "evidence_linkage", "answer_faithfulness", "safety_pass_rate",
    ]
    for variant in variants:
        metrics = _group_metrics(all_by_variant[variant])
        lines.append(f"### {variant}")
        lines.append("")
        lines.extend(f"- `{key}`：{_format_number(_finite(metrics.get(key)))}" for key in detail_metric_keys)
        lines.append(f"- `forbidden_assertion_count`：{_format_number(_finite(metrics.get('forbidden_assertion_count')))}")
        lines.append(f"- `unsupported_relation_claim_count`：{_format_number(_finite(metrics.get('unsupported_relation_claim_count')))}")
        lines.append(f"- `strict_nutrition_misreport_count`：{_format_number(_finite(metrics.get('strict_nutrition_misreport_count')))}")
        lines.append("")
    lines.extend(["## 按场景与难度", ""])
    scenario_rows = []
    for scenario in bank.get("scenarios", []):
        if not isinstance(scenario, dict):
            continue
        scenario_id = scenario.get("id")
        for difficulty in ("A", "B", "C"):
            for variant in variants:
                subset = [row for row in all_by_variant[variant] if row.get("scenario_id") == scenario_id and row.get("difficulty_code") == difficulty]
                metrics = _group_metrics(subset)
                scenario_rows.append([str(scenario_id), difficulty, variant, str(len(subset)), _format_number(_finite(metrics.get("recall_at_5"))), _format_number(_finite(metrics.get("ndcg_at_5"))), _format_number(_finite(metrics.get("safety_pass_rate"))), _format_number(_finite(metrics.get("total_latency_p95_ms")))])
    lines.extend([_markdown_table(["场景", "卷", "变体", "结果行", "Recall@5", "nDCG@5", "安全通过率", "P95 ms"], scenario_rows) if scenario_rows else "_尚未写入结果。_", ""])
    lines.extend(["## 解释与结论", "", "- Recall@K 是已找回相关 gold 数 / 全部相关 gold 数；Hit Rate@K 仅表示前 K 是否至少命中一项，二者不可混用。", "- 排名指标只对有冻结 gold relevance 的成功场景计算；安全场景不硬套 Recall 或 nDCG。", "- 若覆盖率不是 1.000、存在 blocked/error、存在重复结果、存在未知题目、关键字段格式问题，或审计/路径字段缺失，则本次考试不得标记为通过。", "- `路径与召回明细.md` 是逐题人工复核入口；总评不得替代逐题证据。", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="汇总真实场景考试 JSONL 结果")
    parser.add_argument("--bank", type=Path, required=True, help="试卷题库 JSON")
    parser.add_argument("--results", type=Path, nargs="+", required=True, help="一个或多个逐题 JSONL 结果")
    parser.add_argument("--output-dir", type=Path, required=True, help="总评和明细输出目录")
    args = parser.parse_args()
    bank = _load_json(args.bank)
    rows = _load_jsonl(args.results)
    questions = bank.get("questions") if isinstance(bank.get("questions"), list) else []
    questions_by_id = {item.get("question_id"): item for item in questions if isinstance(item, dict) and isinstance(item.get("question_id"), str)}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "考试结果总评.md").write_text(_render_summary(bank, rows), encoding="utf-8")
    (args.output_dir / "路径与召回明细.md").write_text(_render_detail(rows, questions_by_id), encoding="utf-8")
    print(f"rows={len(rows)}")
    print(f"output_dir={args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
