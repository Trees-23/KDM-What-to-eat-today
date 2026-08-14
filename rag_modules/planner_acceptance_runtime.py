"""Planner 启用态的容器内只读验收执行器。

由 ``scripts/run_intent_planner_acceptance.py`` 调用。该模块不创建、删除或
重建任何检索工件；它只初始化当前运行时组件，并为每道冻结题保留审计引用。
"""

from __future__ import annotations

import argparse
import json
import os
import signal
import sys
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from main import AdvancedGraphRAGSystem
from rag_modules.rag_audit import RAGAuditManager
from rag_modules.request_boundary import RetrievalRequest
from rag_modules.retrieval_contracts import EvidenceBundle


RUNNER_ID = "intent-planner-live-runner-v1"
FAILURE_REGRESSION_RUNNER_ID = "intent-planner-failure-regression-v1"
GENERATION_TIMEOUT_SECONDS = 60.0
QUESTION_TIMEOUT_SECONDS = 90.0


class _UnavailableGraphDriver:
    """仅在 S10 请求期间替换目标图检索器 driver 的故障注入器。"""

    @contextmanager
    def session(self, database=None):
        del database
        raise OSError("INTENT_PLANNER_ACCEPTANCE_GRAPH_UNAVAILABLE")
        yield  # pragma: no cover - 让此函数保持 generator 形式。


class _QuestionTimeoutError(TimeoutError):
    """单题总时限耗尽，必须记录为失败后继续下一题。"""


@contextmanager
def _question_timeout(seconds: float):
    """在 Linux 容器主线程中对单题施加硬超时。"""

    if seconds <= 0 or not hasattr(signal, "setitimer"):
        yield
        return

    def expire(_signum, _frame):
        raise _QuestionTimeoutError(f"单题超过 {seconds:.0f} 秒硬时限")

    previous_handler = signal.getsignal(signal.SIGALRM)
    previous_timer = signal.setitimer(signal.ITIMER_REAL, seconds)
    signal.signal(signal.SIGALRM, expire)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)
        if previous_timer[0] > 0:
            signal.setitimer(signal.ITIMER_REAL, *previous_timer)


def _read_input(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("questions"), list):
        raise ValueError("验收输入必须含有 questions 数组")
    questions = value["questions"]
    execution_mode = value.get("execution_mode", "full")
    if execution_mode not in {"full", "failure_regression"}:
        raise ValueError("验收输入 execution_mode 不受支持")
    if execution_mode == "full" and len(questions) != 300:
        raise ValueError(f"全量验收输入必须恰好包含 300 题，实际为 {len(questions)}")
    if execution_mode == "failure_regression" and not 1 <= len(questions) <= 300:
        raise ValueError(f"失败集回归输入必须在 1 到 300 题之间，实际为 {len(questions)}")
    ids = [item.get("question_id") for item in questions if isinstance(item, dict)]
    if len(ids) != len(questions) or len(set(ids)) != len(questions) or any(not isinstance(item, str) or not item for item in ids):
        raise ValueError("验收输入的 question_id 必须为唯一非空值")
    return value


def _events(audit) -> list[tuple[str, str, dict[str, Any]]]:
    events: list[tuple[str, str, dict[str, Any]]] = []
    original = audit.record_event

    def record(stage: str, status: str = "completed", **fields: Any) -> None:
        events.append((stage, status, dict(fields)))
        original(stage, status=status, **fields)

    audit.record_event = record
    return events


def _non_execute(bundle: EvidenceBundle) -> bool:
    return "INTENT_NON_EXECUTE" in bundle.limitations


def _acceptance_request(question: dict[str, Any]) -> RetrievalRequest:
    """将试题中的评测说明与真实检索请求隔离。

    题库的安全断言、故障说明和回答限制不是用户需求。S10 的真实请求由冻结
    契约中的目标实体给出，故障仍只由运行器的隔离 driver 注入。
    """

    original = str(question["question"]).strip()
    scenario = question["scenario_id"]
    if scenario == "S10":
        target = question.get("contract", {}).get("gold_target", {})
        entity_name = target.get("entity_name") if isinstance(target, dict) else None
        if not isinstance(entity_name, str) or not entity_name.strip():
            raise ValueError("S10 验收契约缺少目标实体")
        return RetrievalRequest(
            user_message=f"{entity_name.strip()}能做哪些菜？",
            evaluation_constraints=original,
        )

    # 这些后缀均是题库明确声明的回答约束，不应污染意图或营养识别。
    for marker in (
        "可以表达偏好匹配，但",
        "；如果意图无法由资料支持，",
        "；资料没有说明的结论请明确保留。",
        "；没有路径时请说明无法证明。",
    ):
        if marker in original:
            user_message, constraints = original.split(marker, 1)
            return RetrievalRequest(
                user_message=user_message.strip(),
                evaluation_constraints=(marker.lstrip("；") + constraints).strip(),
            )
    return RetrievalRequest(user_message=original)


def _stage_events(events: list[tuple[str, str, dict[str, Any]]], stage: str) -> list[tuple[str, dict[str, Any]]]:
    return [(status, fields) for event_stage, status, fields in events if event_stage == stage]


def _recommendation_failures(question: dict[str, Any], bundle: EvidenceBundle, events: list[tuple[str, str, dict[str, Any]]]) -> list[str]:
    """核验推荐题的本地约束、两段式证据和固定重排契约。"""

    contract = question.get("contract", {}).get("recommendation_contract")
    if not isinstance(contract, dict):
        return ["missing_recommendation_contract"]
    constraint_events = _stage_events(events, "recommendation_constraints")
    if not constraint_events:
        return ["missing_recommendation_constraint_audit"]
    status, fields = constraint_events[-1]
    if status != "compiled":
        return ["recommendation_constraints_not_compiled"]
    if fields.get("policy_version") != contract.get("policy_version"):
        return ["recommendation_policy_version_mismatch"]
    hard_filters = fields.get("hard_filters")
    if not isinstance(hard_filters, dict):
        return ["missing_recommendation_hard_filters"]
    for name, expected in contract.get("expected_hard_filters", {}).items():
        if hard_filters.get(name) != expected:
            return [f"recommendation_hard_filter_mismatch:{name}"]

    no_results = "NO_PREFERENCE_RESULTS" in bundle.limitations
    if _non_execute(bundle):
        if no_results and contract.get("allow_no_preference_results"):
            return []
        return ["restricted_preference_pds_required"]
    plan = bundle.query_plan or {}
    if plan.get("intent") != "PREFERENCE_RECOMMEND":
        return ["recommendation_query_plan_required"]
    if no_results:
        return []
    if not bundle.text_evidence:
        return ["recommendation_top5_pds_required"]
    if len(bundle.text_evidence) > int(contract["answer_k"]):
        return ["recommendation_pds_hydration_exceeds_top5"]

    scope_events = _stage_events(events, "recommendation_scope")
    if not scope_events or scope_events[-1][0] != "resolved":
        return ["missing_recommendation_scope_audit"]
    vector_events = _stage_events(events, "recommendation_vector")
    if not vector_events:
        return ["missing_recommendation_vector_audit"]
    vector_status, vector_fields = vector_events[-1]
    if vector_status not in {"selected", "rerank-unavailable"}:
        return ["recommendation_vector_not_selected"]
    if vector_status == "selected" and vector_fields.get("rerank_version") != contract.get("rerank_version"):
        return ["recommendation_rerank_version_mismatch"]
    candidates = vector_fields.get("candidate_top30")
    final = vector_fields.get("final_top5")
    if not isinstance(candidates, list) or not 1 <= len(candidates) <= int(contract["candidate_k"]):
        return ["recommendation_top30_metadata_invalid"]
    if not isinstance(final, list) or not 1 <= len(final) <= int(contract["answer_k"]):
        return ["recommendation_top5_audit_invalid"]
    if vector_status == "selected" and any(not isinstance(item, dict) or "final_score" not in item for item in final):
        return ["recommendation_rerank_audit_invalid"]
    return []


def _status_for(question: dict[str, Any], bundle: EvidenceBundle, events: list[tuple[str, str, dict[str, Any]]], answer: str) -> list[str]:
    """返回本题不满足的可审计断言；空数组才允许计入通过。"""

    scenario = question["scenario_id"]
    failures: list[str] = []
    planner = [event for event in events if event[0] == "intent_planner"]
    compiler = [event for event in events if event[0] == "intent_compile"]
    local_nutrition_gate = (
        not planner
        and bool(compiler)
        and "NUTRITION_EVIDENCE_INSUFFICIENT" in bundle.limitations
    )
    if not local_nutrition_gate and (not planner or not compiler):
        failures.append("missing_planner_or_compile_audit")
    if not answer.strip():
        failures.append("empty_answer")

    has_text = bool(bundle.text_evidence)
    graph_statuses = {fact.status for fact in bundle.graph_facts}
    if scenario in {"S01", "S02", "S03"}:
        if _non_execute(bundle) or not has_text:
            failures.append("entity_pds_evidence_required")
    elif scenario == "S04":
        if _non_execute(bundle) or "verified" not in graph_statuses or not has_text:
            failures.append("verified_graph_and_pds_required")
    elif scenario == "S05":
        expected_zero = question["contract"]["gold_target"].get("expected_verified_graph_paths") == 0
        if expected_zero:
            if not _non_execute(bundle) or "GRAPH_RELATION_NOT_FOUND" not in bundle.limitations:
                failures.append("graph_not_found_required")
        elif _non_execute(bundle) or "verified" not in graph_statuses or not has_text:
            failures.append("verified_pair_graph_and_pds_required")
    elif scenario in {"S06", "S07"}:
        failures.extend(_recommendation_failures(question, bundle, events))
        if scenario == "S07" and any(term in answer for term in ("低脂", "低热量", "低盐", "医疗适用")):
            failures.append("soft_preference_strict_claim")
    elif scenario == "S08":
        if not _non_execute(bundle) or "ENTITY_NOT_FOUND" not in bundle.limitations:
            failures.append("entity_not_found_required")
    elif scenario == "S09":
        if not _non_execute(bundle) or not ({"ENTITY_NOT_FOUND", "CLARIFY_OR_OUT_OF_SCOPE", "ENTITY_AMBIGUOUS", "GRAPH_RELATION_NOT_FOUND"} & set(bundle.limitations)):
            failures.append("safe_unverified_relation_required")
    elif scenario == "S10":
        if not _non_execute(bundle) or "GRAPH_UNAVAILABLE" not in bundle.limitations:
            failures.append("graph_unavailable_required")
    else:
        failures.append("unknown_scenario")
    return failures


def run(input_path: Path, output_path: Path) -> int:
    source = _read_input(input_path)
    if os.getenv("RETRIEVAL_INTENT_PLANNER_ENABLED", "").lower() != "true":
        raise RuntimeError("必须显式启用 RETRIEVAL_INTENT_PLANNER_ENABLED=true")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    expected_ids = {str(question["question_id"]) for question in source["questions"]}
    completed_ids: set[str] = set()
    if output_path.exists():
        for line in output_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            question_id = row.get("question_id")
            if not isinstance(question_id, str) or question_id not in expected_ids or question_id in completed_ids:
                raise ValueError("已有验收结果含无效或重复 question_id")
            completed_ids.add(question_id)

    system = AdvancedGraphRAGSystem()
    system.initialize_system()
    if system.intent_planner is None or system.intent_plan_compiler is None:
        raise RuntimeError("planner 启用态未初始化")
    manager = RAGAuditManager.from_config(system.config)
    rows: list[dict[str, Any]] = []
    try:
        for position, question in enumerate(source["questions"], start=1):
            if question["question_id"] in completed_ids:
                continue
            audit = manager.create_run()
            events = _events(audit)
            audit.mark_request_start()
            request = _acceptance_request(question)
            audit.record_event(
                "acceptance_input_boundary",
                status="isolated",
                evaluation_constraints_present=bool(request.evaluation_constraints),
                user_message_chars=len(request.user_message),
            )
            started = time.monotonic()
            original_driver = None
            question_timeout = _question_timeout(QUESTION_TIMEOUT_SECONDS)
            question_timeout.__enter__()
            try:
                if question["scenario_id"] == "S10":
                    if system.targeted_graph_retriever is None:
                        raise RuntimeError("S10 故障注入前缺少目标图检索器")
                    original_driver = system.targeted_graph_retriever.driver
                    system.targeted_graph_retriever.driver = _UnavailableGraphDriver()
                bundle, _ = system.retrieve_for_generation(request.planner_input, system.config.top_k, audit_run=audit)
                if not isinstance(bundle, EvidenceBundle):
                    raise RuntimeError("planner 路径未返回 EvidenceBundle")
                if _non_execute(bundle):
                    answer = system._intent_terminal_response(bundle)
                    final_source = "compile_terminal"
                else:
                    answer = system.generation_module.generate_adaptive_answer(
                        request.user_message,
                        bundle,
                        audit_run=audit,
                        timeout=GENERATION_TIMEOUT_SECONDS,
                    )
                    final_source = "generation"
                audit.finish_request(success=bool(answer.strip()), final_source=final_source)
            except Exception as error:
                audit.record_error("intent_planner_acceptance", error)
                audit.finish_request(success=False, final_source="error")
                bundle = EvidenceBundle(None, (), (), (), ("ACCEPTANCE_RUNTIME_ERROR", "INTENT_NON_EXECUTE"))
                answer = ""
            finally:
                if original_driver is not None:
                    system.targeted_graph_retriever.driver = original_driver
                question_timeout.__exit__(None, None, None)
            failures = _status_for(question, bundle, events, answer)
            row = {
                    "runner_id": RUNNER_ID,
                    "position": position,
                    "question_id": question["question_id"],
                    "scenario_id": question["scenario_id"],
                    "difficulty_code": question["difficulty_code"],
                    "input": question["question"],
                    "user_message": request.user_message,
                    "evaluation_constraints": request.evaluation_constraints,
                    "audit_id": audit.audit_id,
                    "audit_dir": str(audit.run_dir),
                    "duration_ms": round((time.monotonic() - started) * 1000),
                    "status": "passed" if not failures else "failed",
                    "failures": failures,
                    "limitations": list(bundle.limitations),
                    "query_plan": dict(bundle.query_plan) if bundle.query_plan else None,
                    "graph_statuses": sorted(fact.status for fact in bundle.graph_facts),
                    "pds_text_evidence_count": len(bundle.text_evidence),
                    "answer_chars": len(answer),
                    "planner_events": [
                        {"stage": stage, "status": status, "fields": fields}
                        for stage, status, fields in events
                        if stage in {"intent_planner", "intent_compile"}
                    ],
                    "recommendation_events": [
                        {"stage": stage, "status": status, "fields": fields}
                        for stage, status, fields in events
                        if stage in {"recommendation_constraints", "recommendation_scope", "recommendation_vector"}
                    ],
            }
            rows.append(row)
            with output_path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
            print(json.dumps({"position": position, "question_id": question["question_id"], "status": row["status"]}, ensure_ascii=False), flush=True)
    finally:
        system._cleanup()

    all_rows = [json.loads(line) for line in output_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    actual_ids = [row.get("question_id") for row in all_rows]
    if len(all_rows) != len(source["questions"]) or set(actual_ids) != expected_ids or len(set(actual_ids)) != len(actual_ids):
        raise RuntimeError(f"验收结果不完整: {len(all_rows)}/{len(source['questions'])}")
    failures = sum(row["status"] != "passed" for row in all_rows)
    print(json.dumps({"runner_id": source.get("runner_id", RUNNER_ID), "rows": len(all_rows), "failures": failures, "output": str(output_path)}, ensure_ascii=False), flush=True)
    return 0 if failures == 0 else 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="运行 planner 启用态 300 题只读验收")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args(argv)
    return run(arguments.input, arguments.output)


if __name__ == "__main__":
    raise SystemExit(main())
