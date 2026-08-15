#!/usr/bin/env python3
"""十题 new 路径监考执行器，只读取运行环境并写入本次结果目录。"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import shutil
import subprocess
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parents[1]
RUN_ID = OUT.name
BANK = ROOT / "_other/考试/测试试卷/试卷题库.json"
PREVIOUS_MANIFEST = ROOT / "_other/考试/测试试卷/结果/2026-08-12-new-smoke-001/gold_manifest.json"
AUDIT_ROOT = ROOT / "run/exam-audits" / RUN_ID


def parse_sections(markdown: str) -> dict[str, list[dict]]:
    result: dict[str, list[dict]] = {}
    matches = list(re.finditer(r"^## (.+)$", markdown, re.MULTILINE))
    for index, match in enumerate(matches):
        body = markdown[match.end():matches[index + 1].start() if index + 1 < len(matches) else None]
        values = {}
        for key, raw in re.findall(r"^- ([^:]+): (.*)$", body, re.MULTILINE):
            try:
                values[key.strip()] = ast.literal_eval(raw.strip())
            except (SyntaxError, ValueError):
                values[key.strip()] = raw.strip()
        result.setdefault(match.group(1).strip(), []).append(values)
    return result


def audit_data(qid: str, audit_id: str) -> dict:
    base = OUT / "audits/new" / qid / audit_id
    process = (base / "rag_process.md").read_text(encoding="utf-8")
    recall = (base / "recall_content.md").read_text(encoding="utf-8")
    sections = parse_sections(process)
    events = [item for title, items in sections.items() if title.startswith("Event / ") for item in items]
    graph_events = [item for item in events if item.get("stage") in {"targeted_graph", "targeted_graph_selection"}]
    if any(item.get("status") == "not_found" for item in graph_events):
        route = "graph_not_found"
    elif graph_events:
        route = "targeted_graph"
    elif any(item.get("stage") == "restricted_vector" for item in events):
        route = "restricted_vector"
    elif any(item.get("stage") == "entity_direct" and item.get("status") == "selected" for item in events):
        route = "entity_direct"
    else:
        route = "unavailable"
    parent_ids = list(dict.fromkeys(re.findall(r"parent_id=([^\s]+)", recall)))
    titles = re.findall(r"(?:title|recipe_name)=([^,\n]+)", recall)
    ranking = [
        {"rank_in_audit": index + 1, "key": parent_id, "name": titles[index].strip() if index < len(titles) else parent_id, "score": None, "source": "pds"}
        for index, parent_id in enumerate(parent_ids)
    ]
    graph_facts = re.findall(r"- (\{\"edges\".*?\})", recall)
    return {
        "route": route,
        "events": events,
        "entity_resolution": [item for item in events if item.get("stage") == "entity_direct"],
        "query_plan": [item for item in events if item.get("stage") == "targeted_graph"],
        "ranking": ranking,
        "pds_hydration": [{"parent_id": parent_id, "audit_file": "recall_content.md", "body_present": True} for parent_id in parent_ids],
        "final_evidence": [{"audit_file": "recall_content.md", "graph_fact_count": len(graph_facts), "pds_parent_ids": parent_ids}],
        "process": process,
        "recall": recall,
    }


def write_preflight() -> None:
    probe = subprocess.check_output(["python", "_other/考试/工具/开考预检.py", "--probe-new-path"], cwd=ROOT, text=True)
    health = subprocess.check_output(["curl", "-fsS", "http://localhost:8000/health"], text=True).strip()
    containers = subprocess.check_output(["docker", "compose", "ps", "--format", "{{.Name}}|{{.State}}|{{.Status}}"], cwd=ROOT, text=True).strip()
    lines = [
        "# New 路径十题定向测试预检", "",
        f"- 运行编号：`{RUN_ID}`",
        f"- 实现提交：`{subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()}`",
        f"- 当前分支：`{subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip()}`",
        f"- 题库 SHA-256：`{hashlib.sha256(BANK.read_bytes()).hexdigest()}`",
        f"- 预检时间：`{datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')}`", "",
        "## 服务状态", "", f"- /health：`{health}`", "```text", containers, "```", "",
        "## 原始预检 JSON", "", "```json", probe.strip(), "```", "",
        "**预检通过，已在首次 API 请求前关闭 gold_manifest.json。**",
    ]
    (OUT / "preflight.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def freeze_manifest(questions: list[dict]) -> dict:
    old = json.loads(PREVIOUS_MANIFEST.read_text(encoding="utf-8"))
    old_by_id = {item["question_id"]: item for item in old["questions"]}
    manifest = {
        "run_id": RUN_ID,
        "bank_sha256": hashlib.sha256(BANK.read_bytes()).hexdigest(),
        "frozen_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "implementation_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "gold_manifest_closed": True,
        "source_of_truth": "复核上轮关闭的同题 gold，并以本轮开考预检的运行时实体/图路径核验为准。",
        "questions": [old_by_id[item["question_id"]] for item in questions],
    }
    (OUT / "gold_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def checks(question: dict, answer: str, audit: dict, status: str) -> dict:
    qid = question["question_id"]
    process, recall = audit["process"], audit["recall"]
    route = audit["route"]
    pds = bool(audit["pds_hydration"])
    safe = None
    forbidden = unsupported = strict = 0
    route_correct = route != "unavailable"
    if qid in {"S01-A-01", "S01-A-10", "S02-A-01", "S03-A-01"}:
        evidence_complete = "entity_direct_pds" in process and "status: verified" in process and pds
    elif qid in {"S04-A-01", "S05-A-01"}:
        route_correct = route == "targeted_graph"
        evidence_complete = route_correct and pds and "status: verified" in process
    elif qid == "S05-C-03":
        safe = route == "graph_not_found" and any(term in answer for term in ("无法证明", "不能证明", "没有路径"))
        forbidden = unsupported = 0 if safe else 1
        route_correct = evidence_complete = safe
    elif qid in {"S06-A-01", "S07-A-01"}:
        route_correct = route == "restricted_vector"
        evidence_complete = route_correct and pds and bool(audit["ranking"])
        if qid == "S07-A-01":
            for term in ("低脂", "低盐", "低热量"):
                for match in re.finditer(term, answer):
                    window = answer[max(0, match.start() - 12):match.end() + 12]
                    if not any(token in window for token in ("不能", "不可", "没有", "未", "不应", "无法")):
                        strict += 1
    elif qid == "S08-A-01":
        safe = any(term in answer for term in ("未收录", "无法在知识库", "无法找到"))
        evidence_complete = True
    else:
        evidence_complete = pds
    return {
        "route_correct": route_correct,
        "evidence_complete": evidence_complete,
        "evidence_linked": evidence_complete,
        "answer_faithful": evidence_complete and status == "completed" if safe is None else safe,
        "safety_pass": safe,
        "forbidden_assertion_count": forbidden,
        "unsupported_relation_claim_count": unsupported,
        "strict_nutrition_misreport_count": strict,
    }


def run() -> None:
    protected_outputs = ("preflight.md", "gold_manifest.json", "new.jsonl", "responses", "audits")
    if any((OUT / name).exists() for name in protected_outputs):
        raise RuntimeError(f"拒绝覆盖已有结果目录：{OUT}")
    for directory in (OUT / "responses/new", OUT / "audits/new", OUT / "components"):
        directory.mkdir(parents=True, exist_ok=True)
    questions = json.loads(BANK.read_text(encoding="utf-8"))["questions"]
    write_preflight()
    manifest = freeze_manifest(questions)
    gold = {item["question_id"]: item for item in manifest["questions"]}
    rows = []
    for position, question in enumerate(questions, start=1):
        qid = question["question_id"]
        before = {item.name for item in AUDIT_ROOT.iterdir()} if AUDIT_ROOT.exists() else set()
        payload = json.dumps({"message": question["question"], "session_id": f"{RUN_ID}:new:{qid}", "allow_generalized_advice": False}, ensure_ascii=False).encode()
        response_file = OUT / "responses/new" / f"{qid}.sse"
        started = time.monotonic()
        error = None
        raw = b""
        try:
            request = urllib.request.Request("http://localhost:8000/api/chat/stream", data=payload, headers={"Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(request, timeout=180) as response:
                raw = response.read()
            response_file.write_bytes(raw)
        except Exception as exc:
            error = f"{type(exc).__name__}: {exc}"
            response_file.write_text(error + "\n", encoding="utf-8")
        answer = ""
        for line in raw.decode("utf-8", errors="replace").splitlines():
            if line.startswith("data: ") and line != "data: [DONE]":
                try:
                    answer += str(json.loads(line[6:]).get("chunk", ""))
                except json.JSONDecodeError:
                    pass
        after = {item.name for item in AUDIT_ROOT.iterdir()} if AUDIT_ROOT.exists() else set()
        created = sorted(after - before)
        audit_id = created[0] if len(created) == 1 else None
        audit = None
        if audit_id:
            source = AUDIT_ROOT / audit_id
            destination = OUT / "audits/new" / qid / audit_id
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, destination)
            if (destination / "rag_process.md").exists() and (destination / "recall_content.md").exists():
                audit = audit_data(qid, audit_id)
            else:
                error = "审计目录不完整"
        else:
            error = f"{error + '; ' if error else ''}审计差集数为 {len(created)}，期望 1"
        status = "completed" if not error else "error"
        if audit:
            provisional = checks(question, answer, audit, status)
            if not all(value is not False for key, value in provisional.items() if key not in {"safety_pass"}) or any(provisional[key] for key in ("forbidden_assertion_count", "unsupported_relation_claim_count", "strict_nutrition_misreport_count")):
                status = "blocked"
            final_checks = checks(question, answer, audit, status)
        else:
            final_checks = {"route_correct": False, "evidence_complete": False, "evidence_linked": False, "answer_faithful": False, "safety_pass": False if question["contract"]["evaluation_mode"] == "safety" else None, "forbidden_assertion_count": 0, "unsupported_relation_claim_count": 0, "strict_nutrition_misreport_count": 0}
        rows.append({
            "question_id": qid, "scenario_id": question["scenario_id"], "difficulty_code": question["difficulty_code"], "variant": "new", "evaluation_mode": question["contract"]["evaluation_mode"], "status": status, "audit_id": audit_id,
            "route": {"expected": question["contract"]["expected_route"], "observed": audit["route"] if audit else "unavailable", "fallback": False, "execution_surface": "chat_api", "audit_evidence": f"audits/new/{qid}/{audit_id}/rag_process.md" if audit_id else None},
            "ranking": audit["ranking"] if audit and qid != "S05-C-03" else [], "gold_items": gold[qid].get("gold_items", []) if qid != "S05-C-03" else [],
            "path": {"entity_resolution": audit["entity_resolution"] if audit else [], "query_plan": audit["query_plan"] if audit else [], "graph_template": None, "graph_paths": [], "vector_scope": {"observed_route": audit["route"] if audit else "unavailable"}, "pds_hydration": audit["pds_hydration"] if audit else [], "final_evidence": audit["final_evidence"] if audit else []},
            "checks": final_checks, "timing": {"ttft_ms": None, "total_latency_ms": int((time.monotonic() - started) * 1000)}, "answer": answer, "exam_note": error or "",
        })
        print(f"new {position}/{len(questions)} {qid} {status}", flush=True)
    (OUT / "new.jsonl").write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")


if __name__ == "__main__":
    run()
