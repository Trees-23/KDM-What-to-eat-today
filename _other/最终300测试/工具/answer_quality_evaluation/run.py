#!/usr/bin/env python3
"""Create, run, resume, and verify the final 300 single-judge package."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

from evaluator import (
    SCORE_FIELDS,
    ScoreValidationError,
    answer_type,
    applicable_dimensions,
    canonical_sha256,
    json_line_append,
    load_jsonl,
    sha256_file,
    validate_and_score,
)


ROOT = Path(__file__).resolve().parents[4]
FINAL_ROOT = ROOT / "_other/最终300测试"
SOURCE = ROOT / "_other/考试/检索重构真实场景考试包/结果/2026-08-15-intent-planner-300-005"
CONFIG = FINAL_ROOT / "配置"
PROMPT_PATH = CONFIG / "answer-quality-judge-prompt-v1.md"
RUBRIC_PATH = CONFIG / "answer-quality-rubric-v1.json"
SCHEMA_PATH = CONFIG / "answer-quality-output-schema-v1.json"


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def git_value(*args: str) -> str | None:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else None


def redact_base_url(value: str) -> str:
    return re.sub(r"(https?://)[^/@]+@", r"\1***@", value)


def regular_manifest(root: Path) -> list[dict[str, Any]]:
    return [
        {"path": path.relative_to(root).as_posix(), "size_bytes": path.stat().st_size, "sha256": sha256_file(path)}
        for path in sorted((path for path in root.rglob("*") if path.is_file()), key=lambda path: path.as_posix())
    ]


def source_rows() -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    rows = load_jsonl(SOURCE / "new-results.jsonl")
    events = [entry for entry in load_jsonl(SOURCE / "runner.stdout.jsonl", skip_invalid=True) if entry.get("event") == "question_result"]
    return rows, {entry["question_id"]: entry for entry in events}


def source_integrity() -> tuple[bool, dict[str, Any]]:
    rows, events = source_rows()
    ids = [row.get("question_id") for row in rows]
    checks = {
        "source_exists": SOURCE.is_dir(),
        "source_file_count": len(regular_manifest(SOURCE)),
        "new_results_count": len(rows) == 300,
        "unique_question_ids": len(ids) == 300 and len(set(ids)) == 300,
        "all_passed": all(row.get("status") == "passed" for row in rows),
        "answer_event_count": len(events) == 300,
        "answer_event_mapping": set(ids) == set(events),
        "all_answers_nonempty": all(isinstance(event.get("answer"), str) and event["answer"].strip() for event in events.values()),
    }
    return all(checks.values()), {"status": "SOURCE_INTEGRITY_PASSED" if all(checks.values()) else "SOURCE_INTEGRITY_FAILED", "checks": checks}


def evidence_for(audit_id: str) -> tuple[list[dict[str, str]], list[str]]:
    text_path = SOURCE / "audits" / audit_id / "recall_content.md"
    if not text_path.exists():
        return [], ["未找到来源 recall_content.md。"]
    text = text_path.read_text(encoding="utf-8")
    match = re.search(r"## Evidence / 正文证据\n(.*?)(?=\n## Evidence /|\Z)", text, re.S)
    excerpt = (match.group(1).strip() if match else text.strip())[:6000]
    limitations_match = re.search(r"## Evidence / 限制与不可证明项\n(.*?)(?=\n## |\Z)", text, re.S)
    limitations = [line.removeprefix("- ").strip() for line in limitations_match.group(1).splitlines() if line.startswith("-")] if limitations_match else []
    return ([{"id": f"{audit_id}:recall_content", "excerpt": excerpt}] if excerpt else []), limitations


def make_cases() -> list[dict[str, Any]]:
    rows, events = source_rows()
    cases = []
    for row in sorted(rows, key=lambda item: item["position"]):
        event = events[row["question_id"]]
        evidence, audited_limitations = evidence_for(row["audit_id"])
        limitations = list(row.get("limitations") or []) + audited_limitations
        cases.append({
            "case_id": row["question_id"], "position": row["position"], "scenario_id": row["scenario_id"],
            "difficulty_code": row["difficulty_code"], "source_status": row["status"], "user_question": event["user_message"],
            "final_answer": event["answer"], "audit_id": row["audit_id"], "final_evidence": evidence,
            "limitations": limitations, "source_locations": {
                "result_row": "new-results.jsonl", "answer_event": "runner.stdout.jsonl",
                "audit": f"audits/{row['audit_id']}/recall_content.md",
            },
            "field_status": {"final_answer": "present", "final_evidence": "present" if evidence else "missing", "limitations": "present" if limitations else "none"},
        })
    return cases


def setup_package(run_dir: Path) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)
    source_copy = run_dir / "01-原始300硬规则考试" / SOURCE.name
    source_copy.parent.mkdir(parents=True, exist_ok=True)
    if not source_copy.exists():
        shutil.copytree(SOURCE, source_copy)
    source_manifest = regular_manifest(SOURCE)
    copy_manifest = regular_manifest(source_copy)
    ok, report = source_integrity()
    report.update({"source": str(SOURCE.relative_to(ROOT)), "copied_to": str(source_copy.relative_to(run_dir)), "source_manifest_sha256": canonical_sha256(source_manifest), "copy_manifest_sha256": canonical_sha256(copy_manifest), "copy_matches_source": source_manifest == copy_manifest})
    report["status"] = "SOURCE_INTEGRITY_PASSED" if ok and report["copy_matches_source"] else "SOURCE_INTEGRITY_FAILED"
    (run_dir / "01-原始300硬规则考试" / "source-copy-manifest.json").write_text(json.dumps(source_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    inputs = run_dir / "02-评测输入与硬指标"
    inputs.mkdir(exist_ok=True)
    cases = make_cases() if report["status"] == "SOURCE_INTEGRITY_PASSED" else []
    (inputs / "evaluation-cases.jsonl").write_text("".join(json.dumps(case, ensure_ascii=False, sort_keys=True) + "\n" for case in cases), encoding="utf-8")
    (inputs / "source-integrity-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    hard = [{"case_id": row["question_id"], "status": row["status"], "audit_id": row["audit_id"]} for row in source_rows()[0]]
    (inputs / "hard-scorecard-reference.json").write_text(json.dumps(hard, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    rag = run_dir / "03-RAG指标"
    rag.mkdir(exist_ok=True)
    (rag / "本期暂缓说明.md").write_text("# 本期暂缓\n\n本轮只评价用户看到的最终回答。由于缺少逐题冻结的相关性 gold，不计算 Recall、Precision、MRR 或 nDCG，不生成 RAG 分数或 gold。\n", encoding="utf-8")
    quality = run_dir / "04-回答效果评分"
    basis = quality / "评分依据"
    basis.mkdir(parents=True, exist_ok=True)
    manifests = []
    for path in (PROMPT_PATH, RUBRIC_PATH, SCHEMA_PATH):
        shutil.copy2(path, basis / path.name)
        manifests.append({"path": path.name, "sha256": sha256_file(path), "size_bytes": path.stat().st_size})
    (basis / "judge-config-manifest.json").write_text(json.dumps({"created_at": now(), "files": manifests}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    gate = run_dir / "05-自动验收与结论"
    gate.mkdir(exist_ok=True)
    baseline = {"branch": git_value("branch", "--show-current"), "test_branch_baseline_sha": git_value("merge-base", "HEAD", "origin/main"), "origin_main_sha": git_value("rev-parse", "origin/main"), "started_at": now(), "pr_url": None, "gate_result": "PASSED" if report["status"] == "SOURCE_INTEGRITY_PASSED" else "FAILED"}
    (gate / "branch-baseline.json").write_text(json.dumps(baseline, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def judge_input(case: dict[str, Any], rubric: dict[str, Any]) -> dict[str, Any]:
    kind = answer_type(case["case_id"])
    return {"case_id": case["case_id"], "scenario_id": case["scenario_id"], "answer_type": kind, "user_question": case["user_question"], "final_answer": case["final_answer"], "evidence": case["final_evidence"], "limitations": case["limitations"], "applicable_dimensions": applicable_dimensions(kind, rubric), "rubric_version": rubric["version"], "output_schema_version": "answer-quality-output-schema-v1"}


def request_score(client: OpenAI, model: str, prompt: str, schema: dict[str, Any], judge_payload: dict[str, Any], timeout: float) -> dict[str, Any]:
    # Some compatible endpoints reject valid JSON Schema keywords such as uniqueItems.
    # The frozen schema remains the local acceptance authority for every reply.
    response = client.chat.completions.create(model=model, temperature=0, timeout=timeout, response_format={"type": "json_object"}, messages=[{"role": "system", "content": prompt}, {"role": "user", "content": json.dumps(judge_payload, ensure_ascii=False)}])
    content = response.choices[0].message.content
    if not content:
        raise ScoreValidationError("empty model response")
    return json.loads(content)


def score_case(case: dict[str, Any], client: OpenAI, model: str, prompt: str, rubric: dict[str, Any], schema: dict[str, Any], attempts: int, timeout: float) -> dict[str, Any]:
    payload = judge_input(case, rubric)
    input_hash = canonical_sha256(payload)
    record: dict[str, Any] = {"case_id": case["case_id"], "position": case["position"], "scenario_id": case["scenario_id"], "difficulty_code": case["difficulty_code"], "answer_type": payload["answer_type"], "judge_input_sha256": input_hash, "status": "PENDING", "attempts": []}
    for number in range(1, attempts + 1):
        start = time.monotonic()
        try:
            reply = request_score(client, model, prompt, schema, payload, timeout)
            score = validate_and_score(reply, payload["answer_type"], rubric, schema, {item["id"] for item in payload["evidence"]})
            record.update({"status": "SCORED", "score": score, "model": model})
            record["attempts"].append({"attempt": number, "status": "success", "duration_ms": round((time.monotonic() - start) * 1000)})
            return record
        except Exception as error:  # Records real technical and validation errors without scores.
            record["attempts"].append({"attempt": number, "status": "error", "error_type": type(error).__name__, "message": str(error)[:1000], "duration_ms": round((time.monotonic() - start) * 1000)})
    record.update({"status": "QUALITY_UNVERIFIED", "score": {field: None for field in (*SCORE_FIELDS, "total_score_100")}, "error": record["attempts"][-1]})
    return record


def run_scores(run_dir: Path, limit: int | None = None, retry_unverified: bool = False) -> None:
    load_dotenv(ROOT / ".env")
    api_key, base_url, model = os.getenv("OPENAI_API_KEY"), os.getenv("OPENAI_BASE_URL"), os.getenv("LLM_MODEL")
    if not api_key or not base_url or not model:
        raise RuntimeError(".env must provide OPENAI_API_KEY, OPENAI_BASE_URL, and LLM_MODEL")
    prompt, rubric, schema = PROMPT_PATH.read_text(encoding="utf-8"), json.loads(RUBRIC_PATH.read_text(encoding="utf-8")), json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    cases = load_jsonl(run_dir / "02-评测输入与硬指标" / "evaluation-cases.jsonl")
    scores_path = run_dir / "04-回答效果评分" / "checkpoints.jsonl"
    existing = {item["case_id"]: item for item in load_jsonl(scores_path) if item["status"] == "SCORED"}
    if not retry_unverified:
        existing.update({item["case_id"]: item for item in load_jsonl(scores_path) if item["status"] == "QUALITY_UNVERIFIED"})
    pending = [case for case in cases if case["case_id"] not in existing]
    if limit is not None:
        pending = pending[:limit]
    client = OpenAI(api_key=api_key, base_url=base_url)
    for case in pending:
        json_line_append(scores_path, {"case_id": case["case_id"], "position": case["position"], "status": "PENDING", "recorded_at": now(), "judge_input_sha256": canonical_sha256(judge_input(case, rubric))})
        result = score_case(case, client, model, prompt, rubric, schema, attempts=3, timeout=90)
        result["completed_at"] = now()
        json_line_append(scores_path, result)
        if result["status"] != "SCORED" and case["position"] <= 3:
            break
    config = {"model": model, "base_url": redact_base_url(base_url), "timeout_seconds": 90, "max_attempts": 3, "concurrency": 1, "prompt_sha256": sha256_file(PROMPT_PATH), "rubric_sha256": sha256_file(RUBRIC_PATH), "schema_sha256": sha256_file(SCHEMA_PATH)}
    (run_dir / "04-回答效果评分" / "run-config.json").write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def finalize(run_dir: Path) -> dict[str, Any]:
    rubric, schema = json.loads(RUBRIC_PATH.read_text(encoding="utf-8")), json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    cases = load_jsonl(run_dir / "02-评测输入与硬指标" / "evaluation-cases.jsonl")
    history = load_jsonl(run_dir / "04-回答效果评分" / "checkpoints.jsonl")
    terminal = {record["case_id"]: record for record in history if record["status"] in {"SCORED", "QUALITY_UNVERIFIED"}}
    errors: list[str] = []
    source_report = json.loads((run_dir / "02-评测输入与硬指标" / "source-integrity-report.json").read_text(encoding="utf-8"))
    if source_report["status"] != "SOURCE_INTEGRITY_PASSED": errors.append("source integrity failed")
    if len(cases) != 300: errors.append("evaluation cases is not 300")
    if len(terminal) != len(cases): errors.append("not every case has a terminal record")
    success_ids = [record["case_id"] for record in history if record["status"] == "SCORED"]
    if len(success_ids) != len(set(success_ids)): errors.append("a case has more than one successful score")
    for record in terminal.values():
        if record["status"] == "SCORED":
            try:
                judge_reply = {field: value for field, value in record["score"].items() if field != "total_score_100"}
                validate_and_score(judge_reply, record["answer_type"], rubric, schema, set())
            except ScoreValidationError as error: errors.append(f"{record['case_id']}: {error}")
    scored = [record for record in terminal.values() if record["status"] == "SCORED"]
    unverified = [record for record in terminal.values() if record["status"] == "QUALITY_UNVERIFIED"]
    by_scenario: dict[str, dict[str, Any]] = {}
    by_difficulty: dict[str, dict[str, Any]] = {}
    tag_counts = Counter(tag for record in scored for tag in record["score"]["issue_tags"])
    for name, key in (("scenario", "scenario_id"), ("difficulty", "difficulty_code")):
        groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for record in scored: groups[record[key]].append(record)
        target = by_scenario if name == "scenario" else by_difficulty
        for group, records in sorted(groups.items()): target[group] = {"valid_count": len(records), "average_score_100": round(sum(item["score"]["total_score_100"] for item in records) / len(records), 2)}
    if errors or not scored and not unverified:
        conclusion = "NOT_READY"
    elif len(scored) == 300 and not unverified:
        conclusion = "READY_FOR_AUTO_BASELINE"
    else:
        conclusion = "AUTO_BASELINE_WITH_LIMITATIONS"
    summary = {"conclusion": conclusion, "valid_count": len(scored), "quality_unverified_count": len(unverified), "average_score_100": round(sum(item["score"]["total_score_100"] for item in scored) / len(scored), 2) if scored else None, "by_scenario": by_scenario, "by_difficulty": by_difficulty, "issue_tags": dict(tag_counts), "validation_errors": errors}
    quality = run_dir / "04-回答效果评分"
    (quality / "quality-scorecard.json").write_text(json.dumps({"records": [terminal[case["case_id"]] for case in cases if case["case_id"] in terminal], "summary": summary}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    validation = {"status": "PASSED" if not errors else "FAILED", "checks": {"source_integrity": source_report["status"], "case_count": len(cases), "terminal_count": len(terminal), "single_success_per_case": len(success_ids) == len(set(success_ids)), "rag_deferred_note_exists": (run_dir / "03-RAG指标/本期暂缓说明.md").exists()}, "errors": errors}
    gate = run_dir / "05-自动验收与结论"
    (gate / "validation-report.json").write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (run_dir / "final-conclusion.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lowest = min(by_scenario.items(), key=lambda item: item[1]["average_score_100"]) if by_scenario else None
    overview = f"# 最终 300 测试总览\n\n- 硬规则：来源运行 300/300 通过，完整副本哈希已核验。\n- 回答效果：有效 {len(scored)} 题，未验证 {len(unverified)} 题；全体均分：{summary['average_score_100']}。\n- 最低场景：{lowest[0] + ' / ' + str(lowest[1]['average_score_100']) if lowest else '无'}。\n- 常见问题标签：{', '.join(tag_counts.most_common(5)[i][0] for i in range(min(5, len(tag_counts)))) or '无'}。\n- RAG：本期暂缓，未计算任何 RAG 分数或 gold。\n- 自动验收结论：`{conclusion}`。\n"
    (run_dir / "00-最终总览.md").write_text(overview, encoding="utf-8")
    manifest = regular_manifest(run_dir)
    (run_dir / "package-manifest.json").write_text(json.dumps({"created_at": now(), "files": manifest}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("setup", "run", "finalize", "all"))
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--retry-unverified", action="store_true")
    args = parser.parse_args()
    run_dir = FINAL_ROOT / "运行结果" / args.run_id
    if args.command in {"setup", "all"}: setup_package(run_dir)
    if args.command in {"run", "all"}: run_scores(run_dir, args.limit, args.retry_unverified)
    if args.command in {"finalize", "all"}: print(json.dumps(finalize(run_dir), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
