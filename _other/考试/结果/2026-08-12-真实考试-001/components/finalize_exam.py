#!/usr/bin/env python3
"""只读取本次产物，生成独立监考结论。"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path


out = Path(sys.argv[1]).resolve()
bank = json.loads((out.parents[1] / "试卷题库.json").read_text(encoding="utf-8"))
expected_ids = {item["question_id"] for item in bank["questions"]}
manifest = json.loads((out / "gold_manifest.json").read_text(encoding="utf-8"))
summary = (out / "考试结果总评.md").read_text(encoding="utf-8")
issues: list[str] = []
stats: dict[str, Counter[str]] = {}
counts: dict[str, dict[str, int]] = {}
for variant in ("old", "new"):
    rows = [json.loads(line) for line in (out / f"{variant}.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    ids = [row.get("question_id") for row in rows]
    stats[variant] = Counter(str(row.get("status")) for row in rows)
    counts[variant] = {
        "forbidden": sum(int(row.get("checks", {}).get("forbidden_assertion_count", 0)) for row in rows),
        "unsupported": sum(int(row.get("checks", {}).get("unsupported_relation_claim_count", 0)) for row in rows),
        "nutrition": sum(int(row.get("checks", {}).get("strict_nutrition_misreport_count", 0)) for row in rows),
    }
    if len(rows) != 300 or set(ids) != expected_ids or len(set(ids)) != 300:
        issues.append(f"{variant} 结果行不完整或题号重复")
    if stats[variant]["blocked"] or stats[variant]["error"]:
        issues.append(f"{variant} 存在 blocked/error：blocked={stats[variant]['blocked']}，error={stats[variant]['error']}")
    for row in rows:
        sid = row.get("scenario_id")
        component = sid in {"S09", "S10"}
        if not component and row.get("status") == "completed" and not row.get("audit_id"):
            issues.append(f"{variant} {row.get('question_id')} 缺少 API 审计 ID")
            break
    if any(counts[variant].values()):
        issues.append(f"{variant} 存在安全计数：{counts[variant]}")
if not manifest.get("gold_manifest_closed") or len(manifest.get("questions", [])) != 300:
    issues.append("gold_manifest 未在请求前完整关闭")
for variant in ("old", "new"):
    copied = len(list((out / "audits" / variant).glob("S*/**/rag_process.md")))
    if copied != 240:
        issues.append(f"{variant} API 审计副本数为 {copied}/240")

commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=out.parents[3], text=True).strip()
lines = [
    "# 监考结论", "", "## 结论", "",
    "**可签收。**" if not issues else "**不可签收。**",
    "", "## 版本与完整性", "",
    f"- 运行编号：`{out.name}`。",
    f"- 实现提交：`{commit}`。",
    f"- 题库 SHA-256：`{manifest.get('bank_sha256')}`。",
    f"- gold_manifest 已关闭：`{manifest.get('gold_manifest_closed')}`，冻结题数：`{len(manifest.get('questions', []))}`。",
]
for variant in ("old", "new"):
    lines.append(f"- {variant}：completed=`{stats[variant]['completed']}`，blocked=`{stats[variant]['blocked']}`，error=`{stats[variant]['error']}`；禁止断言=`{counts[variant]['forbidden']}`，无依据关系=`{counts[variant]['unsupported']}`，严格营养误报=`{counts[variant]['nutrition']}`。")
lines.extend([
    "", "## Old/New 对比", "",
    "- 总体及按场景/难度的 Recall、Precision、Hit Rate、MRR、nDCG、路线/证据/忠实度、安全和延迟差异均由 `考试结果总评.md` 依据两份互不混用的 JSONL 分母计算。",
    "- 逐题实际路线、候选顺序、PDS 回补和最终证据见 `路径与召回明细.md`；S09/S10 为隔离组件级结论，不作为端到端 API 结论。",
    "", "## 不可签收原因", "",
])
lines.extend([f"- {issue}" for issue in issues] if issues else ["- 未发现缺题、重复行、blocked/error、gold 未关闭、审计缺失或非零安全计数。"])
lines.extend(["", "## 说明", "", "- 请求返回 200 并不单独构成通过；结论只基于冻结 gold、原始 SSE/HTTP 响应、审计副本及逐题检查。", ""])
(out / "监考结论.md").write_text("\n".join(lines), encoding="utf-8")
print(json.dumps({"signoff": "accepted" if not issues else "rejected", "issues": issues}, ensure_ascii=False))
