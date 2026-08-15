from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from common import PARSER_VERSION, SOURCE_RUN_ID, audit_map, extract_trace, manifest, read_json, read_jsonl, scenario_from_case, sha256_text, write_json, write_jsonl


def build(source: Path, output: Path) -> dict:
    results = read_jsonl(source / "new-results.jsonl")
    frozen = read_json(source / "frozen_questions.json")
    questions = {item["question_id"]: item for item in frozen.get("questions", [])}
    answers = {row["question_id"]: row for row in read_jsonl(source / "runner.stdout.jsonl", strict=False) if row.get("event") == "question_result"}
    audits = audit_map(source)
    required_files = ["new-results.jsonl", "runner.stdout.jsonl", "frozen_questions.json", "acceptance-report.json", "failure-summary.json"]
    missing_files = [name for name in required_files if not source.joinpath(name).is_file()]
    cases, per_case = [], []
    ids = [row.get("question_id") for row in results]
    for row in results:
        case_id = row.get("question_id", "")
        question = questions.get(case_id)
        answer = answers.get(case_id, {}).get("answer")
        audit = audits.get(row.get("audit_id", ""))
        trace = extract_trace(audit / "rag_process.md") if audit else extract_trace(Path("/nonexistent"))
        missing = []
        if not question: missing.append("FROZEN_QUESTION_MISSING")
        if not answer: missing.append("FINAL_ANSWER_MISSING")
        if not audit: missing.append("AUDIT_DIRECTORY_MISSING")
        field_status = {
            "user_question": "PRESENT" if row.get("user_message") else "MISSING",
            "final_answer": "PRESENT" if answer else "MISSING",
            "audit": "PRESENT" if audit else "MISSING",
            "route_contract": "PRESENT" if question and question.get("contract") else "MISSING",
            "gold_target": "PRESENT" if question and question.get("contract", {}).get("gold_target") else "MISSING",
            "ranking_candidates": "PRESENT" if trace["candidate_top30"] else "NOT_APPLICABLE",
            "final_evidence": "PRESENT" if trace["final_evidence"] else "MISSING",
        }
        case = {
            "case_id": case_id, "scenario_id": row.get("scenario_id") or scenario_from_case(case_id), "difficulty_code": row.get("difficulty_code"),
            "source_status": row.get("status"), "user_question": row.get("user_message"), "final_answer": answer,
            "audit_id": row.get("audit_id"), "audit_path": str(audit) if audit else None,
            "hard_reference": {"source_status": row.get("status"), "failures": row.get("failures", [])},
            "route_contract": question.get("contract", {}) if question else {}, "gold_target": question.get("contract", {}).get("gold_target", {}) if question else {},
            "ranking_candidates": trace["candidate_top30"], "final_evidence": trace["final_evidence"], "evidence_excerpt": trace.get("evidence_excerpt", ""), "limitations": row.get("limitations") or [],
            "recommendation_trace": {"candidate_top30": trace["candidate_top30"], "final_top5": trace["final_top5"]},
            "field_status": field_status, "source_locations": {"new_results_line": row["_source_line"], "runner_answer_line": answers.get(case_id, {}).get("_source_line"), "audit_id": row.get("audit_id")},
            "final_answer_sha256": sha256_text(answer or ""),
        }
        cases.append(case)
        per_case.append({"case_id": case_id, "source_ready": not missing, "missing": missing, "field_status": field_status, "audit_path": str(audit) if audit else None})
    integrity_ok = not missing_files and len(results) == 300 and len(set(ids)) == 300 and set(ids) == set(questions) and all(item["source_ready"] for item in per_case)
    report = {"status": "SOURCE_READY" if integrity_ok else "SOURCE_INTEGRITY_FAILED", "source_run_id": SOURCE_RUN_ID, "parser_version": PARSER_VERSION, "generated_at": datetime.now(timezone.utc).isoformat(), "required_file_missing": missing_files, "result_line_count": len(results), "unique_case_count": len(set(ids)), "frozen_question_count": len(questions), "answer_count": len(answers), "cases": per_case}
    output.mkdir(parents=True, exist_ok=True)
    write_json(output / "source-run.json", {"source_run_id": SOURCE_RUN_ID, "source_path": str(source.resolve()), "files": manifest(source), "parser_version": PARSER_VERSION})
    write_json(output / "source-integrity-report.json", report)
    output.joinpath("source-integrity-report.md").write_text(
        f"# 来源完整性报告\n\n状态：`{report['status']}`。\n\n- new-results 行数：{report['result_line_count']}\n- 唯一题号：{report['unique_case_count']}\n- 冻结题目：{report['frozen_question_count']}\n- 可读取最终回答：{report['answer_count']}\n- 缺失关键文件：{', '.join(missing_files) or '无'}\n",
        encoding="utf-8",
    )
    write_jsonl(output / "evaluation-cases.jsonl", cases)
    write_json(output / "case-field-coverage.json", {"case_count": len(cases), "fields": {name: sum(case["field_status"][name] == "PRESENT" for case in cases) for name in cases[0]["field_status"]} if cases else {}})
    output.joinpath("field-mapping.md").write_text("# 字段映射\n\n`new-results.jsonl` 提供题号、状态、审计 ID 与限制；`runner.stdout.jsonl` 的 `question_result` 提供最终回答；`frozen_questions.json` 提供题目与契约；审计目录提供候选和证据定位。\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True); parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(); report = build(args.source, args.output)
    print(report["status"]); return 0 if report["status"] == "SOURCE_READY" else 2


if __name__ == "__main__": raise SystemExit(main())
