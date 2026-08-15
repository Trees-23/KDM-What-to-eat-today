from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path

from common import read_json


def render(hard_path: Path, rag_path: Path, quality_path: Path, validation_path: Path, output: Path) -> None:
    hard, rag, quality, validation = map(read_json, (hard_path, rag_path, quality_path, validation_path))
    scenario_scores: dict[str, list[float]] = defaultdict(list)
    tags = Counter()
    for row in quality["cases"]:
        if row["status"] in {"VALID", "AUTO_DISAGREEMENT"}:
            scenario_scores[row["scenario_id"]].append(row["total_score_100"])
            tags.update(row.get("issue_tags", []))
    lines = ["# 三层评测总览", "", f"自动验收结论：`{validation['conclusion']}`。三层成绩不合成为单一总分。", "", "## 硬规则引用", f"- 既有考试状态：{hard['status_counts']}。", f"- 题目数：{hard['case_count']}；本评测未重跑或重判硬规则。", "", "## RAG 指标", f"- 可计算：{rag['summary']['computable']}；N/A：{rag['summary']['na']}；未验证：{rag['summary']['unverified']}。", "- `DERIVED_AI_GOLD_V1` 仅表示 `TOP30_ONLY` 候选池内 Top5 选择/排序，绝不表示全库 Recall。", "", "## 回答效果", f"- 有效：{quality['summary']['VALID'] + quality['summary']['AUTO_DISAGREEMENT']}；未验证：{quality['summary']['QUALITY_UNVERIFIED']}；自动分歧：{quality['summary']['AUTO_DISAGREEMENT']}。"]
    for scenario in sorted(scenario_scores): lines.append(f"- {scenario} 平均分：{sum(scenario_scores[scenario]) / len(scenario_scores[scenario]):.2f}（{len(scenario_scores[scenario])} 题）")
    if tags: lines += ["", "## 常见问题标签"] + [f"- {tag}: {count}" for tag, count in tags.most_common()]
    lines += ["", "## 限制", *[f"- {item}" for item in validation["limitations"]], "", "## 改进方向", "- RAG 未验证题需补齐可追溯的冻结 gold 或审计候选序列。", "- 回答效果为 AI 自动基线；应优先复查低分、自动分歧与问题标签集中的场景。"]
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--hard", type=Path, required=True); parser.add_argument("--rag", type=Path, required=True); parser.add_argument("--quality", type=Path, required=True); parser.add_argument("--validation", type=Path, required=True); parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(); render(args.hard, args.rag, args.quality, args.validation, args.output); return 0


if __name__ == "__main__": raise SystemExit(main())
