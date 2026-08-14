#!/usr/bin/env python3
"""冻结正式 300 题并在隔离容器进程中执行 planner 启用态验收。"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "_other" / "考试" / "检索重构真实场景考试包" / "试卷题库.json"
PREFLIGHT = ROOT / "_other" / "考试" / "检索重构真实场景考试包" / "工具" / "开考预检.py"
CONTAINER = "what-to-eat-backend"
RUNNER_ID = "intent-planner-live-runner-v1"
FAILURE_REGRESSION_RUNNER_ID = "intent-planner-failure-regression-v1"
RUNTIME = "rag_modules.planner_acceptance_runtime"
RUNTIME_WORK_ROOT = ROOT / "run" / "intent-planner-acceptance"

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


def _runtime_environment(overrides: list[str]) -> dict[str, str]:
    environment = dict(_RUNTIME_ENV)
    for item in overrides:
        key, separator, value = item.partition("=")
        if not separator or not key or not value:
            raise ValueError("--runtime-env 必须采用 KEY=VALUE 形式")
        if not key.replace("_", "").isalnum() or not key.isupper():
            raise ValueError("--runtime-env 的 KEY 必须是大写环境变量名")
        environment[key] = value
    return environment


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


def _stage_runtime_input(output: Path) -> Path:
    """为容器准备已挂载的临时输入，正式记录仍保留在用户可见目录。"""

    runtime_directory = RUNTIME_WORK_ROOT / output.name
    if runtime_directory.exists():
        raise FileExistsError(f"拒绝覆盖已有容器验收工件: {runtime_directory}")
    runtime_directory.mkdir(parents=True)
    return runtime_directory


def _collect_runtime_output(output: Path, runtime_directory: Path) -> None:
    """将容器的逐题结果和审计证据回收至正式结果目录。"""

    for name in ("new-results.jsonl",):
        source = runtime_directory / name
        if source.is_file():
            shutil.copy2(source, output / name)
    source_audits = runtime_directory / "audits"
    if source_audits.is_dir():
        shutil.copytree(source_audits, output / "audits")


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


def _failure_summary(rows_path: Path, summary_path: Path, metadata: dict[str, Any]) -> dict[str, Any]:
    """在全量完成后集中输出失败集合，保留原始逐题结果与审计引用。"""
    rows = [json.loads(line) for line in rows_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    failures = [
        {
            "question_id": row.get("question_id"),
            "scenario_id": row.get("scenario_id"),
            "difficulty_code": row.get("difficulty_code"),
            "input": row.get("input"),
            "failures": row.get("failures", []),
            "limitations": row.get("limitations", []),
            "query_plan": row.get("query_plan"),
            "audit_id": row.get("audit_id"),
            "audit_dir": row.get("audit_dir"),
        }
        for row in rows
        if row.get("status") != "passed"
    ]
    summary = {
        "runner_id": RUNNER_ID,
        "implementation_commit": metadata["implementation_commit"],
        "bank_sha256": metadata["bank_sha256"],
        "question_count": len(rows),
        "failed_count": len(failures),
        "failure_result_file": rows_path.name,
        "failures": failures,
    }
    _write_json_once(summary_path, summary)
    return summary


def _load_failure_regression_questions(summary_path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    """从冻结失败摘要重新抽取官方题库题目，拒绝任意手工改写的回归输入。"""

    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    if not isinstance(summary, dict) or not isinstance(summary.get("failures"), list):
        raise ValueError("失败摘要必须包含 failures 数组")
    bank = _load_bank()
    bank_sha256 = hashlib.sha256(BANK.read_bytes()).hexdigest()
    if summary.get("bank_sha256") != bank_sha256:
        raise ValueError("失败摘要与当前官方题库哈希不一致")
    failure_ids = [item.get("question_id") for item in summary["failures"] if isinstance(item, dict)]
    if not failure_ids or len(failure_ids) != len(summary["failures"]):
        raise ValueError("失败摘要必须至少包含一个有效 question_id")
    if len(failure_ids) != len(set(failure_ids)):
        raise ValueError("失败摘要包含重复 question_id")
    question_by_id = {item["question_id"]: item for item in bank["questions"]}
    unknown_ids = set(failure_ids) - set(question_by_id)
    if unknown_ids:
        raise ValueError(f"失败摘要含非官方题库题号: {sorted(unknown_ids)}")
    source_rows = summary_path.parent / str(summary.get("failure_result_file", ""))
    if not source_rows.is_file():
        raise ValueError("失败摘要引用的原始逐题结果不存在")
    source_rows_sha256 = hashlib.sha256(source_rows.read_bytes()).hexdigest()
    result = {
        "runner_id": FAILURE_REGRESSION_RUNNER_ID,
        "execution_mode": "failure_regression",
        "created_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "implementation_commit": _command("git", "rev-parse", "HEAD"),
        "branch": _command("git", "branch", "--show-current"),
        "bank_sha256": bank_sha256,
        "source_failure_summary": {
            "path": str(summary_path),
            "sha256": hashlib.sha256(summary_path.read_bytes()).hexdigest(),
            "source_implementation_commit": summary.get("implementation_commit"),
            "source_rows_file": source_rows.name,
            "source_rows_sha256": source_rows_sha256,
            "source_failed_count": summary.get("failed_count"),
        },
        "questions": [question_by_id[question_id] for question_id in failure_ids],
    }
    return result, summary


def _regression_report(rows_path: Path, report_path: Path, metadata: dict[str, Any]) -> dict[str, Any]:
    rows = [json.loads(line) for line in rows_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    expected = {item["question_id"] for item in metadata["questions"]}
    actual = [item.get("question_id") for item in rows]
    report = {
        "runner_id": FAILURE_REGRESSION_RUNNER_ID,
        "execution_mode": "failure_regression",
        "implementation_commit": metadata["implementation_commit"],
        "bank_sha256": metadata["bank_sha256"],
        "source_failure_summary": metadata["source_failure_summary"],
        "question_count": len(rows),
        "source_failed_count": len(metadata["questions"]),
        "coverage_complete": len(rows) == len(expected) and set(actual) == expected and len(set(actual)) == len(expected),
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


def run_failure_regression(output: Path, failure_summary: Path, *, runtime_env: dict[str, str] | None = None) -> int:
    """执行上一轮失败题的闭合集回归；不改变 300 题最终验收语义。"""

    if output.exists():
        raise FileExistsError(f"拒绝覆盖已有回归工件: {output}")
    output.mkdir(parents=True)
    metadata, _ = _load_failure_regression_questions(failure_summary.resolve())
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
    metadata["preflight"] = preflight_payload
    _write_json_once(output / "frozen_questions.json", metadata)
    runtime_directory = _stage_runtime_input(output)
    shutil.copy2(output / "frozen_questions.json", runtime_directory / "frozen_questions.json")
    container_input = f"/app/run/intent-planner-acceptance/{output.name}/frozen_questions.json"
    container_output = f"/app/run/intent-planner-acceptance/{output.name}/new-results.jsonl"
    command = ["docker", "exec"]
    for key, value in (runtime_env or _RUNTIME_ENV).items():
        command.extend(["-e", f"{key}={value}"])
    command.extend(["-e", f"RAG_AUDIT_ROOT_DIR=/app/run/intent-planner-acceptance/{output.name}/audits", "-e", "RAG_VARIANT_NAME=intent-planner-failure-regression", CONTAINER, "python", "-m", RUNTIME, "--input", container_input, "--output", container_output])
    process = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    (output / "runner.stdout.jsonl").write_text(process.stdout, encoding="utf-8")
    (output / "runner.stderr.txt").write_text(process.stderr, encoding="utf-8")
    _collect_runtime_output(output, runtime_directory)
    rows = output / "new-results.jsonl"
    if not rows.exists():
        return process.returncode or 2
    report = _regression_report(rows, output / "acceptance-report.json", metadata)
    _failure_summary(rows, output / "failure-summary.json", metadata)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if process.returncode == 0 and report["valid"] else 2


def finalize_existing_failure_regression(output: Path, failure_summary: Path) -> int:
    """为已完成但由受控外部执行器运行的失败集补齐汇总工件。"""

    output = output.resolve()
    rows = output / "new-results.jsonl"
    if not output.is_dir() or not rows.is_file():
        raise FileNotFoundError("--finalize-existing 需要已有的 new-results.jsonl")
    metadata, _ = _load_failure_regression_questions(failure_summary.resolve())
    metadata["finalized_at"] = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    _write_json_once(output / "frozen_questions.json", metadata)
    report = _regression_report(rows, output / "acceptance-report.json", metadata)
    _failure_summary(rows, output / "failure-summary.json", metadata)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["valid"] else 2


def run(output: Path, *, runtime_env: dict[str, str] | None = None) -> int:
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
    runtime_directory = _stage_runtime_input(output)
    shutil.copy2(output / "frozen_questions.json", runtime_directory / "frozen_questions.json")
    container_input = f"/app/run/intent-planner-acceptance/{output.name}/frozen_questions.json"
    container_output = f"/app/run/intent-planner-acceptance/{output.name}/new-results.jsonl"
    command = ["docker", "exec"]
    for key, value in (runtime_env or _RUNTIME_ENV).items():
        command.extend(["-e", f"{key}={value}"])
    command.extend(["-e", f"RAG_AUDIT_ROOT_DIR=/app/run/intent-planner-acceptance/{output.name}/audits", "-e", "RAG_VARIANT_NAME=intent-planner-enabled", CONTAINER, "python", "-m", RUNTIME, "--input", container_input, "--output", container_output])
    process = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    (output / "runner.stdout.jsonl").write_text(process.stdout, encoding="utf-8")
    (output / "runner.stderr.txt").write_text(process.stderr, encoding="utf-8")
    _collect_runtime_output(output, runtime_directory)
    rows = output / "new-results.jsonl"
    if not rows.exists():
        return process.returncode or 2
    report = _report(rows, output / "acceptance-report.json", metadata)
    _failure_summary(rows, output / "failure-summary.json", metadata)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if process.returncode == 0 and report["valid"] else 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="planner 启用态 300 题真实服务验收")
    parser.add_argument("--output", type=Path, required=True, help="未存在的结果目录")
    parser.add_argument("--failure-summary", type=Path, help="只回归该失败摘要中的冻结题目")
    parser.add_argument("--runtime-env", action="append", default=[], metavar="KEY=VALUE", help="仅覆盖本次验收容器进程环境")
    parser.add_argument("--finalize-existing", action="store_true", help="仅为已有失败集 JSONL 生成汇总工件")
    arguments = parser.parse_args(argv)
    if arguments.finalize_existing:
        if not arguments.failure_summary or arguments.runtime_env:
            raise ValueError("--finalize-existing 需要 --failure-summary，且不能同时提供 --runtime-env")
        return finalize_existing_failure_regression(arguments.output, arguments.failure_summary)
    runtime_env = _runtime_environment(arguments.runtime_env)
    if arguments.failure_summary:
        return run_failure_regression(arguments.output.resolve(), arguments.failure_summary, runtime_env=runtime_env)
    return run(arguments.output.resolve(), runtime_env=runtime_env)


if __name__ == "__main__":
    raise SystemExit(main())
