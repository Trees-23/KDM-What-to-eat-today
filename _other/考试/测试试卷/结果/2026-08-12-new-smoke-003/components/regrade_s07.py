#!/usr/bin/env python3
"""仅重算第三轮既有 S07 回答的严格营养否定语义，保留原始 SSE 与审计。"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE.parent
RUNNER = HERE / "smoke_runner.py"

spec = importlib.util.spec_from_file_location("smoke_runner", RUNNER)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)

bank = json.loads((OUT.parents[2] / "试卷题库.json").read_text(encoding="utf-8"))
questions = {item["question_id"]: item for item in bank["questions"]}
rows = [json.loads(line) for line in (OUT / "new.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
for row in rows:
    if row["question_id"] != "S07-A-01":
        continue
    audit_id = row["audit_id"]
    if not audit_id:
        raise RuntimeError("S07 缺少审计 ID，不能重新判定")
    audit = module.audit_data("S07-A-01", audit_id)
    row["route"]["observed"] = audit["route"]
    row["path"]["vector_scope"]["observed_route"] = audit["route"]
    row["checks"] = module.checks(questions[row["question_id"]], row["answer"], audit, "completed")
    row["status"] = "completed" if not row["checks"]["strict_nutrition_misreport_count"] else "blocked"
    row["checks"] = module.checks(questions[row["question_id"]], row["answer"], audit, row["status"])
    row["exam_note"] = "监考规则复核：原始回答中的“并非已验证的低脂选择”为否定语义，不构成严格营养断言。"
    break
else:
    raise RuntimeError("未找到 S07-A-01")

(OUT / "new.jsonl").write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")
print("S07-A-01 regraded from original SSE and audit")
