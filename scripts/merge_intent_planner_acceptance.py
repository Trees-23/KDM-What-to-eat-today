#!/usr/bin/env python3
"""合并一次全量基线与后续冻结失败集的逐题验收记录。

该工具只重用已有 JSONL 中的可审计结果，不运行模型、图或向量检索。输出明确标记为
聚合台账，不能替代第 9.5 节要求的单次最终 300 题全量验收。
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "_other" / "考试" / "试卷题库.json"


def _read_rows(directory: Path) -> tuple[list[dict[str, Any]], str]:
    path = directory / "new-results.jsonl"
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return rows, hashlib.sha256(path.read_bytes()).hexdigest()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="合并 planner 验收逐题记录")
    parser.add_argument("--base", type=Path, required=True, help="300 题全量基线目录")
    parser.add_argument("--regression", action="append", type=Path, required=True, help="按时间顺序提供失败集回归目录")
    parser.add_argument("--output", type=Path, required=True, help="不存在的聚合输出目录")
    args = parser.parse_args(argv)
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"拒绝覆盖已有聚合工件: {output}")

    bank = json.loads(BANK.read_text(encoding="utf-8"))
    questions = bank.get("questions", [])
    question_ids = [item.get("question_id") for item in questions]
    if len(question_ids) != 300 or len(set(question_ids)) != 300:
        raise ValueError("官方题库必须恰好有 300 条唯一题号")

    sources: list[dict[str, Any]] = []
    merged: dict[str, dict[str, Any]] = {}
    for directory in [args.base, *args.regression]:
        source = directory.resolve()
        rows, rows_sha256 = _read_rows(source)
        source_record = {"directory": str(source), "result_file": "new-results.jsonl", "rows_sha256": rows_sha256, "row_count": len(rows)}
        sources.append(source_record)
        for row in rows:
            question_id = row.get("question_id")
            if question_id not in question_ids:
                raise ValueError(f"来源含非官方题号: {question_id}")
            copied = dict(row)
            copied["aggregate_source"] = source_record
            merged[str(question_id)] = copied

    missing = [question_id for question_id in question_ids if question_id not in merged]
    if missing:
        raise ValueError(f"聚合后缺少题号: {missing}")
    rows = [merged[str(question_id)] for question_id in question_ids]
    output.mkdir(parents=True)
    rows_path = output / "new-results.jsonl"
    rows_path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")
    failed = [row for row in rows if row.get("status") != "passed"]
    report = {
        "runner_id": "intent-planner-aggregate-ledger-v1",
        "execution_mode": "aggregate_ledger",
        "created_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "bank_sha256": hashlib.sha256(BANK.read_bytes()).hexdigest(),
        "question_count": len(rows),
        "coverage_complete": len(rows) == 300 and len({row["question_id"] for row in rows}) == 300,
        "passed_count": sum(row.get("status") == "passed" for row in rows),
        "failed_count": len(failed),
        "audit_records_complete": all(isinstance(row.get("audit_id"), str) and row["audit_id"] for row in rows),
        "rows_sha256": hashlib.sha256(rows_path.read_bytes()).hexdigest(),
        "sources": sources,
        "valid_for_final_acceptance": False,
        "limitation": "聚合台账复用历史逐题结果；不是单次最终 300 题全量执行。",
    }
    (output / "acceptance-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {"runner_id": report["runner_id"], "bank_sha256": report["bank_sha256"], "question_count": 300, "failed_count": len(failed), "failure_result_file": "new-results.jsonl", "failures": failed}
    (output / "failure-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
