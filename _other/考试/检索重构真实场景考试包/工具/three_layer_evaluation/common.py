from __future__ import annotations

import hashlib
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

SOURCE_RUN_ID = "2026-08-15-intent-planner-300-005"
PARSER_VERSION = "three-layer-evaluation-v1"
RANKING_METRICS = ("recall", "precision", "hit_rate", "mrr", "ndcg")
SAFETY_SCENARIOS = {"S08", "S09", "S10"}


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path, strict: bool = True) -> list[dict[str, Any]]:
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                if strict:
                    raise
                continue
            row["_source_line"] = line_no
            rows.append(row)
    return rows


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def manifest(root: Path) -> list[dict[str, Any]]:
    entries = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        data = path.read_bytes()
        entries.append({"relative_path": str(path.relative_to(root)), "size_bytes": len(data), "sha256": sha256_bytes(data)})
    return entries


def scenario_from_case(case_id: str) -> str:
    return case_id.split("-")[0]


def is_s05c(case_id: str) -> bool:
    return case_id.startswith("S05-C")


def ranking_not_applicable(case_id: str, scenario: str, no_results: bool = False) -> bool:
    return is_s05c(case_id) or scenario in SAFETY_SCENARIOS or no_results


def weights_for(case_id: str, scenario: str) -> dict[str, int | None]:
    if scenario in {"S06", "S07"}:
        return {"task_score": 25, "preference_score": 35, "evidence_expression_score": 20, "boundary_expression_score": None, "readability_score": 20}
    if is_s05c(case_id) or scenario in SAFETY_SCENARIOS:
        return {"task_score": 30, "preference_score": None, "evidence_expression_score": None, "boundary_expression_score": 45, "readability_score": 25}
    return {"task_score": 40, "preference_score": None, "evidence_expression_score": 25, "boundary_expression_score": None, "readability_score": 35}


def score_total(scores: dict[str, int | None], weights: dict[str, int | None]) -> float:
    return round(sum(weight * (scores[name] - 1) / 4 for name, weight in weights.items() if weight is not None and scores[name] is not None), 2)


def ranking_scores(ranked_ids: list[str], relevance: dict[str, int], k: int = 5) -> dict[str, float]:
    top = ranked_ids[:k]
    binary_relevant = {item for item, value in relevance.items() if value > 0}
    hits = [item for item in top if item in binary_relevant]
    recall = len(set(hits)) / len(binary_relevant) if binary_relevant else 0.0
    precision = len(hits) / k
    first = next((index + 1 for index, item in enumerate(top) if item in binary_relevant), None)
    mrr = 1 / first if first else 0.0
    dcg = sum((2 ** relevance.get(item, 0) - 1) / math.log2(index + 2) for index, item in enumerate(top))
    ideal = sorted(relevance.values(), reverse=True)[:k]
    idcg = sum((2 ** value - 1) / math.log2(index + 2) for index, value in enumerate(ideal))
    return {"recall": round(recall, 6), "precision": round(precision, 6), "hit_rate": float(bool(hits)), "mrr": round(mrr, 6), "ndcg": round(dcg / idcg, 6) if idcg else 0.0}


def audit_map(source: Path) -> dict[str, Path]:
    return {path.parent.name: path.parent for path in source.joinpath("audits").rglob("rag_process.md")}


def extract_trace(path: Path) -> dict[str, Any]:
    if not path or not path.exists():
        return {"candidate_top30": [], "final_top5": [], "final_evidence": [], "limitations": []}
    text = path.read_text(encoding="utf-8")
    result: dict[str, Any] = {"candidate_top30": [], "final_top5": [], "final_evidence": [], "limitations": []}
    for key in ("candidate_top30", "final_top5"):
        match = re.search(rf"- {key}: (\[.*?\])\n", text, re.S)
        if match:
            try:
                import ast
                result[key] = ast.literal_eval(match.group(1))
            except (SyntaxError, ValueError):
                result[f"{key}_parse_error"] = True
    recall = path.with_name("recall_content.md")
    if recall.exists():
        recall_text = recall.read_text(encoding="utf-8")
        result["final_evidence"] = re.findall(r"parent_id=([^\s]+)", recall_text)
        result["recall_content_sha256"] = sha256_text(recall_text)
        result["evidence_excerpt"] = recall_text[:6000]
    return result


def candidate_ids(items: list[dict[str, Any]]) -> list[str]:
    return [str(item.get("parent_id", "")) for item in items if item.get("parent_id") is not None]


def route_status(row: dict[str, Any], contract: dict[str, Any]) -> str:
    route = (contract or {}).get("expected_route")
    if not route:
        return "NOT_APPLICABLE"
    events = row.get("planner_events") or []
    text = json.dumps(events, ensure_ascii=False)
    return "PRESENT" if route.lower() in text.lower() else "MISSING"


def summarize_statuses(values: Iterable[str]) -> dict[str, int]:
    return dict(sorted(Counter(values).items()))
