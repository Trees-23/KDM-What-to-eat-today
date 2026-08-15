from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from common import SAFETY_SCENARIOS, is_s05c, read_json, score_total, weights_for, write_json


def validate(quality_path: Path, rag_path: Path, cases_path: Path, output: Path, stability_path: Path | None = None, fixture_path: Path | None = None) -> dict[str, Any]:
    quality, rag = read_json(quality_path), read_json(rag_path)
    cases = {row["case_id"]: row for row in __import__("common").read_jsonl(cases_path)}
    errors, limitations = [], ["SINGLE_MODEL_REVIEW_RISK"]
    for record in quality["cases"]:
        if record["status"] in {"VALID", "AUTO_DISAGREEMENT"}:
            expected = score_total(record["scores"], record["weights"])
            if expected != record["total_score_100"]: errors.append(f"QUALITY_FORMULA:{record['case_id']}")
    for record in rag["cases"]:
        case = cases[record["case_id"]]
        if is_s05c(case["case_id"]) or case["scenario_id"] in SAFETY_SCENARIOS:
            if record["status"] != "N/A": errors.append(f"SAFETY_RAG_STATUS:{case['case_id']}")
        if record["status"] == "RAG_UNVERIFIED": limitations.append("RAG_UNVERIFIED")
    if any(row["status"] == "QUALITY_UNVERIFIED" for row in quality["cases"]): limitations.append("QUALITY_UNVERIFIED")
    stability = read_json(stability_path) if stability_path and stability_path.exists() else None
    if stability:
        if not stability.get("passed", False): errors.append("STABILITY_FAILED")
    else: errors.append("STABILITY_MISSING")
    fixture = read_json(fixture_path) if fixture_path and fixture_path.exists() else None
    if fixture:
        if not fixture.get("passed", False): errors.append("ANTI_BIAS_FIXTURE_FAILED")
    else: errors.append("ANTI_BIAS_FIXTURE_MISSING")
    conclusion = "NOT_READY" if errors else ("AUTO_BASELINE_WITH_LIMITATIONS" if limitations else "READY_FOR_AUTO_BASELINE")
    report = {"conclusion": conclusion, "passed": not errors, "errors": errors, "limitations": sorted(set(limitations)), "quality_summary": quality["summary"], "rag_summary": rag["summary"], "stability": stability, "fixtures": fixture}
    write_json(output, report); return report


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--quality", type=Path, required=True); parser.add_argument("--rag", type=Path, required=True); parser.add_argument("--cases", type=Path, required=True); parser.add_argument("--output", type=Path, required=True); parser.add_argument("--stability", type=Path); parser.add_argument("--fixtures", type=Path)
    args = parser.parse_args(); report = validate(args.quality, args.rag, args.cases, args.output, args.stability, args.fixtures); print(report["conclusion"]); return 0 if report["conclusion"] != "NOT_READY" else 2


if __name__ == "__main__": raise SystemExit(main())
