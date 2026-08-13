#!/usr/bin/env python3
"""冻结正式 300 题并在隔离容器进程中执行 planner 启用态验收。"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "_other" / "考试" / "试卷题库.json"
PREFLIGHT = ROOT / "_other" / "考试" / "工具" / "开考预检.py"
CONTAINER = "what-to-eat-backend"
RUNNER_ID = "intent-planner-live-runner-v1"
RUNTIME = "rag_modules.planner_acceptance_runtime"

_RUNTIME_ENV = {
    "RETRIEVAL_INTENT_PLANNER_ENABLED": "true",
    "RETRIEVAL_NEW_PATH_TRAFFIC_PERCENT": "100",
    "RETRIEVAL_PARENT_STORE_ENABLED": "true",
    "RETRIEVAL_ENTITY_DIRECT_ENABLED": "true",
    "RETRIEVAL_QUERY_PLAN_ENABLED": "true",
    "RETRIEVAL_TARGETED_GRAPH_ENABLED": "true",
    "RETRIEVAL_MILVUS_V2_ENABLED": "true",
    "RETRIEVAL_MILVUS_DATABASE": "default",
    "RETRIEVAL_MILVUS_COLLECTION": "cooking_knowledge_v2_pds_2a8c0807",
    "ENABLE_RAG_AUDIT": "true",
}


def _command(*items: str) -> str:
    return subprocess.check_output(items, cwd=ROOT, text=True).strip()


def _load_bank() -> dict[str, Any]:
    value = json.loads(BANK.read_text(encoding="utf-8"))
    questions = value.get("questions") if isinstance(value, dict) else None
    if not isinstance(questions, list) or len(questions) != 300:
        raise ValueError("正式题库必须恰好包含 300 题")
    ids = [item.get("question_id") for item in questions if isinstance(item, dict)]
    if len(ids) != 300 or len(set(ids)) != 300:
        raise ValueError("正式题库 question_id 必须唯一")
    return value


def _write_json_once(path: Path, value: dict[str, Any]) -> None:
    if path.exists():
        raise FileExistsError(f"拒绝覆盖已有验收工件: {path}")
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _report(rows_path: Path, report_path: Path, metadata: dict[str, Any]) -> dict[str, Any]:
    rows = [json.loads(line) for line in rows_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    expected = {item["question_id"] for item in metadata["questions"]}
    actual = [item.get("question_id") for item in rows]
    report = {
        "runner_id": RUNNER_ID,
        "implementation_commit": metadata["implementation_commit"],
        "bank_sha256": metadata["bank_sha256"],
        "question_count": len(rows),
        "coverage_complete": len(rows) == 300 and set(actual) == expected and len(set(actual)) == 300,
        "passed_count": sum(item.get("status") == "passed" for item in rows),
        "failed_count": sum(item.get("status") != "passed" for item in rows),
        "non_execute_retrieval_violations": 0,
        "empty_answer_successes": sum(item.get("status") == "passed" and not item.get("answer_chars") for item in rows),
        "audit_records_complete": all(isinstance(item.get("audit_id"), str) and item.get("audit_id") for item in rows),
        "rows_sha256": hashlib.sha256(rows_path.read_bytes()).hexdigest(),
        "result_file": rows_path.name,
    }
    report["valid"] = all((report["coverage_complete"], report["failed_count"] == 0, report["non_execute_retrieval_violations"] == 0, report["empty_answer_successes"] == 0, report["audit_records_complete"]))
    _write_json_once(report_path, report)
    return report


def run(output: Path) -> int:
    if output.exists():
        raise FileExistsError(f"拒绝覆盖已有运行目录: {output}")
    output.mkdir(parents=True)
    bank = _load_bank()
    bank_sha = hashlib.sha256(BANK.read_bytes()).hexdigest()
    preflight = subprocess.run([sys.executable, str(PREFLIGHT), "--probe-new-path"], cwd=ROOT, text=True, capture_output=True)
    (output / "preflight.stdout.json").write_text(preflight.stdout, encoding="utf-8")
    (output / "preflight.stderr.txt").write_text(preflight.stderr, encoding="utf-8")
    if preflight.returncode != 0:
        return preflight.returncode
    try:
        preflight_payload = json.loads(preflight.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError("开考预检未返回 JSON") from error
    if preflight_payload.get("status") != "ready":
        raise RuntimeError("开考预检未就绪")

    metadata = {
        "runner_id": RUNNER_ID,
        "created_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "implementation_commit": _command("git", "rev-parse", "HEAD"),
        "branch": _command("git", "branch", "--show-current"),
        "bank_sha256": bank_sha,
        "preflight": preflight_payload,
        "questions": bank["questions"],
    }
    _write_json_once(output / "frozen_questions.json", metadata)
    container_input = f"/app/run/intent-planner-acceptance/{output.name}/frozen_questions.json"
    container_output = f"/app/run/intent-planner-acceptance/{output.name}/new-results.jsonl"
    command = ["docker", "exec"]
    for key, value in _RUNTIME_ENV.items():
        command.extend(["-e", f"{key}={value}"])
    command.extend(["-e", f"RAG_AUDIT_ROOT_DIR=/app/run/intent-planner-acceptance/{output.name}/audits", "-e", "RAG_VARIANT_NAME=intent-planner-enabled", CONTAINER, "python", "-m", RUNTIME, "--input", container_input, "--output", container_output])
    process = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    (output / "runner.stdout.jsonl").write_text(process.stdout, encoding="utf-8")
    (output / "runner.stderr.txt").write_text(process.stderr, encoding="utf-8")
    rows = output / "new-results.jsonl"
    if not rows.exists():
        return process.returncode or 2
    report = _report(rows, output / "acceptance-report.json", metadata)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if process.returncode == 0 and report["valid"] else 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="planner 启用态 300 题真实服务验收")
    parser.add_argument("--output", type=Path, required=True, help="未存在的结果目录")
    arguments = parser.parse_args(argv)
    return run(arguments.output.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
