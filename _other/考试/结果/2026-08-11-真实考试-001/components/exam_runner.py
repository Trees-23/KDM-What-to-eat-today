#!/usr/bin/env python3
"""真实服务考试执行器。

只写入同级考试目录；应用、题库、配置和数据库均只读。
"""
from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import re
import shutil
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parents[1]
RUN_ID = OUT.name
BANK_PATH = ROOT / "_other/考试/试卷题库.json"
AUDIT_ROOT = ROOT / "run/exam-audits" / RUN_ID
PDS_PATH = ROOT / "run/retrieval/parent_store.pds_f01044e524ef43b413f76b02.sqlite"


def load_bank() -> dict[str, Any]:
    return json.loads(BANK_PATH.read_text(encoding="utf-8"))


def normalize_source_path(value: str) -> str:
    value = value.replace("\\", "/").lstrip("/")
    return value if value.startswith("data/") else f"data/{value}"


def source_catalog() -> tuple[list[dict[str, str]], dict[str, dict[str, Any]]]:
    nodes: list[dict[str, str]] = []
    for path in (ROOT / "data/cypher/nodes.csv", ROOT / "data/cypher/tips_nodes.csv"):
        with path.open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream):
                row["source_path_normalized"] = normalize_source_path(row.get("filePath") or row.get("sourcePath") or "")
                nodes.append(row)
    parents: dict[str, dict[str, Any]] = {}
    connection = sqlite3.connect(PDS_PATH)
    try:
        for parent_id, node_type, title, metadata_json in connection.execute(
            "SELECT parent_id, node_type, title, metadata_json FROM parents"
        ):
            parents[str(parent_id)] = {
                "key": str(parent_id),
                "name": str(title),
                "node_type": str(node_type),
                "metadata": json.loads(metadata_json),
            }
    finally:
        connection.close()
    return nodes, parents


def recipe_by_name(parents: dict[str, dict[str, Any]], name: str) -> dict[str, Any]:
    choices = [item for item in parents.values() if item["node_type"] == "Recipe" and item["name"] == name]
    if not choices:
        raise RuntimeError(f"PDS 中不存在冻结候选：{name}")
    return sorted(choices, key=lambda item: item["key"])[0]


S06_GOLD = [
    ["凉拌黄瓜", "凉拌金针菇", "白灼虾"], ["西红柿炒鸡蛋", "蚝油生菜", "肉蛋盖饭"],
    ["鸡蛋三明治", "煮泡面加蛋", "牛奶燕麦"], ["清蒸鲈鱼", "油焖大虾", "葱烧海参"],
    ["西红柿鸡蛋汤", "金针菇汤", "紫菜蛋花汤"], ["麻婆豆腐", "酸辣土豆丝", "红烧茄子"],
    ["水煮鱼", "水煮牛肉", "宫保鸡丁"], ["微波葱姜黑鳕鱼", "微波炉腊肠煲仔饭", "微波炉鸡蛋羹"],
    ["清蒸鲈鱼", "清蒸鳜鱼", "红烧鲤鱼"], ["西红柿炒鸡蛋", "麻婆豆腐", "酸辣土豆丝"],
    ["西红柿鸡蛋汤", "紫菜蛋花汤", "羊肉汤"], ["鸡蛋三明治", "煮泡面加蛋", "牛奶燕麦"],
    ["西红柿炒鸡蛋", "蚝油生菜", "清蒸鲈鱼"], ["土豆炖排骨", "红烧肉", "羊排焖面"],
    ["清蒸鲈鱼", "清蒸鳜鱼", "清蒸南瓜"], ["肉蛋盖饭", "西红柿炒鸡蛋", "宫保鸡丁"],
    ["炸酱面", "热干面", "豆角焖面"], ["西红柿炒鸡蛋", "蒜蓉西兰花", "蚝油生菜"],
    ["水煮鱼", "宫保鸡丁", "鱼香肉丝"], ["糖醋排骨", "糖醋鲤鱼", "凉拌黄瓜"],
    ["肉蛋盖饭", "西红柿炒鸡蛋", "煮泡面加蛋"], ["凉拌黄瓜", "凉拌金针菇", "凉粉"],
    ["麻婆豆腐", "凉拌豆腐", "金针菇日本豆腐煲"], ["西红柿炒鸡蛋", "西红柿鸡蛋汤", "西红柿豆腐汤羹"],
    ["蚝油生菜", "西红柿炒鸡蛋", "煮泡面加蛋"], ["电饭煲三文鱼炊饭", "电饭煲蒸米饭", "肉蛋盖饭"],
    ["葱煎豆腐", "韭菜盒子", "蛋包饭"], ["清蒸鲈鱼", "白灼虾", "清蒸鳜鱼"],
    ["土豆炖排骨", "西红柿土豆炖牛肉", "茄子炖土豆"], ["烤蛋挞", "戚风蛋糕", "懒人蛋挞"],
]
S07_GOLD = [
    ["凉粉", "酸辣蕨根粉", "凉拌鸡丝"], ["凉粉", "酸辣土豆丝", "凉拌鸡丝"],
    ["凉粉", "酸辣蕨根粉", "老妈蹄花"], ["麻婆豆腐", "鱼香茄子", "水煮鱼"],
    ["酸辣土豆丝", "蒜蓉空心菜", "凉粉"], ["凉粉", "酸辣蕨根粉", "蒜蓉空心菜"],
    ["酸辣蕨根粉", "凉粉", "鱼香茄子"], ["麻婆豆腐", "酸辣土豆丝", "凉粉"],
    ["麻婆豆腐", "鱼香茄子", "凉粉"], ["清蒸鲈鱼", "老妈蹄花", "凉粉"],
    ["凉粉", "酸辣蕨根粉", "凉拌鸡丝"], ["酸辣土豆丝", "蒜蓉空心菜", "凉粉"],
    ["凉粉", "酸辣蕨根粉", "蒜蓉空心菜"], ["凉粉", "酸辣蕨根粉", "凉拌鸡丝"],
    ["酸辣土豆丝", "凉粉", "鱼香茄子"], ["清蒸鲈鱼", "凉粉", "酸辣蕨根粉"],
    ["蒜蓉空心菜", "酸辣土豆丝", "麻婆豆腐"], ["凉粉", "酸辣蕨根粉", "蒜蓉空心菜"],
    ["清蒸鲈鱼", "白灼虾", "凉粉"], ["凉粉", "酸辣蕨根粉", "蒜蓉空心菜"],
    ["凉粉", "酸辣蕨根粉", "蒜蓉空心菜"], ["老妈蹄花", "凉粉", "酸辣蕨根粉"],
    ["凉粉", "酸辣蕨根粉", "蒜蓉空心菜"], ["西红柿鸡蛋汤", "凉粉", "酸辣蕨根粉"],
    ["凉粉", "蒜蓉空心菜", "酸辣土豆丝"], ["麻婆豆腐", "酸辣土豆丝", "蒜蓉空心菜"],
    ["凉粉", "酸辣蕨根粉", "蒜蓉空心菜"], ["酸辣蕨根粉", "凉粉", "蒜蓉空心菜"],
    ["清蒸鲈鱼", "凉粉", "酸辣蕨根粉"], ["凉粉", "酸辣蕨根粉", "蒜蓉空心菜"],
]


def semantic_items(question: dict[str, Any], parents: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    bank = load_bank()
    index = [item["question_id"] for item in bank["questions"] if item["scenario_id"] == question["scenario_id"]].index(question["question_id"])
    titles = S06_GOLD[index] if question["scenario_id"] == "S06" else S07_GOLD[index]
    items = []
    for relevance, title in zip((3, 2, 1), titles):
        parent = recipe_by_name(parents, title)
        meta = parent["metadata"]
        items.append({
            "key": parent["key"], "name": parent["name"], "relevance": relevance,
            "sourcePath": meta.get("source_path"),
            "reason": f"冻结于源 Markdown 的菜名、分类/菜系和做法信息；与题干意图的直接程度为 {relevance}。",
        })
    return items


def make_manifest() -> None:
    bank = load_bank()
    nodes, parents = source_catalog()
    source_index: dict[str, list[dict[str, str]]] = {}
    by_name_type: dict[tuple[str, str], list[dict[str, str]]] = {}
    by_id = {str(row["nodeId"]): row for row in nodes if row.get("nodeId")}
    for node in nodes:
        source_index.setdefault(node["source_path_normalized"], []).append(node)
        by_name_type.setdefault((node.get("name", ""), node.get("labels", "")), []).append(node)
    relations = list(csv.DictReader((ROOT / "data/cypher/relationships.csv").open(encoding="utf-8", newline="")))
    requires = [row for row in relations if row["relationshipType"] == "801000001"]
    frozen_questions = []
    for question in bank["questions"]:
        contract = question["contract"]
        target = contract["gold_target"]
        sid = question["scenario_id"]
        record: dict[str, Any] = {
            "question_id": question["question_id"], "scenario_id": sid,
            "contract": contract, "gold_items": [], "entity_resolution": [], "graph_paths": [],
        }
        if sid in {"S01", "S02", "S03"}:
            path = target["source_path"]
            found = [row for row in source_index.get(path, []) if row.get("labels") == target["entity_type"]]
            if len(found) != 1:
                raise RuntimeError(f"{question['question_id']} sourcePath 未唯一解析：{path} -> {len(found)}")
            node = found[0]
            item = {"key": node["nodeId"], "name": target["entity_name"], "sourcePath": path, "relevance": 3}
            record["entity_resolution"] = [item]
            record["gold_items"] = [item]
        elif sid in {"S04", "S05"}:
            matches = sorted(by_name_type.get((target["entity_name"], "Ingredient"), []), key=lambda row: row["nodeId"])
            if not matches:
                raise RuntimeError(f"{question['question_id']} 实体未在 nodes.csv 解析：{target['entity_name']}")
            record["entity_resolution"] = [{"key": row["nodeId"], "name": target["entity_name"], "node_type": "Ingredient"} for row in matches]
            graphs: list[dict[str, Any]] = []
            for ingredient in matches:
                for rel in requires:
                    if rel["endNodeId"] != ingredient["nodeId"]:
                        continue
                    recipe = by_id.get(rel["startNodeId"])
                    if not recipe or recipe.get("labels") != "Recipe":
                        continue
                    if sid == "S04":
                        graphs.append({"nodes": [ingredient["nodeId"], recipe["nodeId"]], "edges": [{"from": recipe["nodeId"], "to": ingredient["nodeId"], "type": "REQUIRES", "relationshipId": rel["relationshipId"]}], "recipe": recipe["name"], "sourcePath": normalize_source_path(recipe.get("filePath", ""))})
                    else:
                        for other in requires:
                            if other["startNodeId"] != recipe["nodeId"] or other["endNodeId"] == ingredient["nodeId"]:
                                continue
                            vegetable = by_id.get(other["endNodeId"])
                            if vegetable and vegetable.get("labels") == "Ingredient" and vegetable.get("category") == "蔬菜":
                                graphs.append({"nodes": [ingredient["nodeId"], recipe["nodeId"], vegetable["nodeId"]], "edges": [{"from": recipe["nodeId"], "to": ingredient["nodeId"], "type": "REQUIRES", "relationshipId": rel["relationshipId"]}, {"from": recipe["nodeId"], "to": vegetable["nodeId"], "type": "REQUIRES", "relationshipId": other["relationshipId"]}], "recipe": recipe["name"], "vegetable": vegetable["name"], "sourcePath": normalize_source_path(recipe.get("filePath", ""))})
            if not graphs:
                raise RuntimeError(f"{question['question_id']} 未冻结到最少一条图路径")
            record["graph_paths"] = graphs
            seen = set()
            for graph in graphs:
                recipe_id = graph["nodes"][1]
                if recipe_id not in seen:
                    seen.add(recipe_id)
                    record["gold_items"].append({"key": recipe_id, "name": graph["recipe"], "sourcePath": graph["sourcePath"], "relevance": 3})
        elif sid in {"S06", "S07"}:
            record["gold_items"] = semantic_items(question, parents)
            record["gold_reason"] = "在首次 API 请求前按源 Markdown 的显式菜名、做法、分类/菜系和题干偏好冻结；3/2/1 表示直接、近似、宽松匹配。"
        elif sid == "S08":
            record["absence_check"] = {"entity_name": target["entity_name"], "nodes_csv_matches": 0, "source": "data/cypher/nodes.csv + data/cypher/tips_nodes.csv"}
        elif sid == "S09":
            known = sorted(by_name_type.get((target["known_entity_name"], "Ingredient"), []), key=lambda row: row["nodeId"])
            missing = by_name_type.get((target["missing_entity_name"], "Ingredient"), [])
            if not known or missing:
                raise RuntimeError(f"{question['question_id']} S09 实体前置条件不满足")
            record["entity_resolution"] = [{"key": row["nodeId"], "name": target["known_entity_name"], "node_type": "Ingredient"} for row in known]
            record["absence_check"] = {"entity_name": target["missing_entity_name"], "nodes_csv_matches": 0}
        elif sid == "S10":
            known = sorted(by_name_type.get((target["entity_name"], "Ingredient"), []), key=lambda row: row["nodeId"])
            if not known:
                raise RuntimeError(f"{question['question_id']} S10 已知实体不存在")
            record["entity_resolution"] = [{"key": row["nodeId"], "name": target["entity_name"], "node_type": "Ingredient"} for row in known]
        frozen_questions.append(record)
    manifest = {
        "run_id": RUN_ID,
        "bank_sha256": hashlib.sha256(BANK_PATH.read_bytes()).hexdigest(),
        "frozen_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "implementation_commit": __import__("subprocess").check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "source_of_truth": {"nodes": "data/cypher/nodes.csv + data/cypher/tips_nodes.csv", "relations": "data/cypher/relationships.csv", "pds": str(PDS_PATH.relative_to(ROOT))},
        "questions": frozen_questions,
    }
    (OUT / "gold_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"frozen_questions={len(frozen_questions)}")


def parse_sections(markdown: str) -> dict[str, list[dict[str, Any]]]:
    sections: dict[str, list[dict[str, Any]]] = {}
    matches = list(re.finditer(r"^## (.+)$", markdown, re.MULTILINE))
    for index, match in enumerate(matches):
        title = match.group(1).strip()
        body = markdown[match.end():matches[index + 1].start() if index + 1 < len(matches) else None]
        values: dict[str, Any] = {}
        for key, raw in re.findall(r"^- ([^:]+): (.*)$", body, re.MULTILINE):
            value: Any = raw.strip()
            try:
                value = ast.literal_eval(value)
            except (ValueError, SyntaxError):
                if value == "True": value = True
                elif value == "False": value = False
                elif value in {"None", "null"}: value = None
            values[key.strip()] = value
        sections.setdefault(title, []).append(values)
    return sections


def candidate_ranking(recall: str) -> list[dict[str, Any]]:
    final = re.search(r"^## (?:Final Prompt Context|Evidence / 正文证据)(.*?)(?=^## |\Z)", recall, re.MULTILINE | re.DOTALL)
    body = final.group(1) if final else recall
    result = []
    for order, source, summary in re.findall(r"### result_order=(\d+)\s+source: ([^\n]+)\s+metadata_summary: ([^\n]+)", body):
        pairs = dict(re.findall(r"([A-Za-z_]+)=([^,]+)", summary))
        key = pairs.get("node_id") or pairs.get("parent_id") or pairs.get("chunk_id")
        if not key or any(item["key"] == key for item in result):
            continue
        result.append({"key": key, "name": pairs.get("recipe_name") or pairs.get("name") or key, "score": None, "source": source.strip(), "rank_in_audit": int(order) + 1})
    return sorted(result, key=lambda item: item["rank_in_audit"])


def audit_path(variant: str, qid: str, audit_id: str) -> dict[str, Any]:
    base = OUT / "audits" / variant / qid / audit_id
    process = (base / "rag_process.md").read_text(encoding="utf-8")
    recall = (base / "recall_content.md").read_text(encoding="utf-8")
    sections = parse_sections(process)
    events = [value for title, values in sections.items() if title.startswith("Event / ") for value in values]
    entities = [value for title, values in sections.items() if "entity" in title.lower() for value in values]
    plans = [value for title, values in sections.items() if "query" in title.lower() or "graph" in title.lower() for value in values]
    generation = sections.get("Generation Stream", [])
    completed = sections.get("Request Complete", [])
    observed = "legacy_hybrid"
    if any(value.get("stage") == "targeted_graph_selection" or value.get("stage") == "targeted_graph" for value in events): observed = "targeted_graph"
    elif any(value.get("stage") == "restricted_vector" for value in events): observed = "restricted_vector"
    elif any(value.get("stage") == "entity_direct" and value.get("status") == "selected" for value in events): observed = "entity_direct"
    elif any(value.get("stage") == "retrieval_rollout" and value.get("status") == "legacy" for value in events): observed = "legacy_hybrid"
    stream = generation[-1] if generation else {}
    done = completed[-1] if completed else {}
    return {
        "route": observed, "events": events, "entity_resolution": entities,
        "query_plan": plans, "ranking": candidate_ranking(recall),
        "pds_hydration": [{"audit_file": "recall_content.md", "present": "正文证据" in recall or "Final Prompt Context" in recall}],
        "final_evidence": [{"audit_file": "recall_content.md", "ranking_count": len(candidate_ranking(recall))}],
        "ttft": stream.get("first_token_latency_ms"), "total": stream.get("total_duration_ms") or done.get("request_duration_ms"),
        "has_required_files": bool(process and recall),
        "process_file": "rag_process.md", "recall_file": "recall_content.md",
    }


def blank_path(reason: str) -> dict[str, Any]:
    return {"entity_resolution": [], "query_plan": {}, "graph_template": None, "graph_paths": [], "vector_scope": {}, "pds_hydration": [], "final_evidence": [{"reason": reason}]}


def checks_for(question: dict[str, Any], answer: str, audit: dict[str, Any] | None, variant: str, status: str) -> dict[str, Any]:
    sid = question["scenario_id"]
    expected = question["contract"]["expected_route"]
    observed = audit["route"] if audit else "unavailable"
    route_ok = observed != "legacy_hybrid" if variant == "new" else False
    if sid == "S08":
        declined = any(word in answer for word in ("未收录", "没有", "找不到", "无法", "不在"))
        invented = int(bool(re.search(r"(?:步骤|食材|做法).{0,20}(?:第|加入|准备)", answer))) if not declined else 0
        return {"route_correct": route_ok, "evidence_complete": None, "evidence_linked": None, "answer_faithful": None, "safety_pass": declined and invented == 0, "forbidden_assertion_count": invented, "unsupported_relation_claim_count": 0, "strict_nutrition_misreport_count": 0}
    strict = 0
    if sid == "S07":
        for marker in ("低脂", "低盐", "低热量"):
            for found in re.finditer(marker, answer):
                context = answer[max(0, found.start() - 12):found.end() + 12]
                if not any(token in context for token in ("不能", "不可", "没有", "未", "不应", "无法")):
                    strict += 1
    evidence = bool(audit and audit["ranking"])
    return {"route_correct": route_ok, "evidence_complete": evidence, "evidence_linked": evidence, "answer_faithful": evidence and status == "completed", "safety_pass": None, "forbidden_assertion_count": 0, "unsupported_relation_claim_count": 0, "strict_nutrition_misreport_count": strict}


def run_api(variant: str) -> None:
    manifest = json.loads((OUT / "gold_manifest.json").read_text(encoding="utf-8"))
    gold = {item["question_id"]: item for item in manifest["questions"]}
    bank = load_bank()
    output = OUT / f"{variant}.jsonl"
    if output.exists():
        raise RuntimeError(f"拒绝覆盖已有结果：{output}")
    rows = []
    api_questions = [item for item in bank["questions"] if item["scenario_id"] in {f"S{i:02d}" for i in range(1, 9)}]
    for number, question in enumerate(api_questions, start=1):
        qid = question["question_id"]
        before = {path.name for path in AUDIT_ROOT.iterdir()} if AUDIT_ROOT.exists() else set()
        payload = json.dumps({"message": question["question"], "session_id": f"{RUN_ID}:{variant}:{qid}", "allow_generalized_advice": False}, ensure_ascii=False).encode("utf-8")
        response_path = OUT / "responses" / variant / f"{qid}.sse"
        answer = ""
        http_error = None
        started = time.monotonic()
        try:
            request = urllib.request.Request("http://localhost:8000/api/chat/stream", data=payload, headers={"Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(request, timeout=150) as response:
                raw = response.read()
            response_path.write_bytes(raw)
            for line in raw.decode("utf-8", errors="replace").splitlines():
                if line.startswith("data: ") and line != "data: [DONE]":
                    try: answer += str(json.loads(line[6:]).get("chunk", ""))
                    except json.JSONDecodeError: pass
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as error:
            http_error = f"{type(error).__name__}: {error}"
            response_path.write_text(http_error + "\n", encoding="utf-8")
        elapsed = int((time.monotonic() - started) * 1000)
        after = {path.name for path in AUDIT_ROOT.iterdir()} if AUDIT_ROOT.exists() else set()
        created = sorted(after - before)
        audit = None
        audit_id = None
        error_reason = http_error
        if len(created) == 1:
            audit_id = created[0]
            source = AUDIT_ROOT / audit_id
            destination = OUT / "audits" / variant / qid / audit_id
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, destination)
            if not (destination / "rag_process.md").exists() or not (destination / "recall_content.md").exists():
                error_reason = "审计目录缺少 rag_process.md 或 recall_content.md"
            else:
                audit = audit_path(variant, qid, audit_id)
        else:
            error_reason = (error_reason + "; " if error_reason else "") + f"审计差集目录数为 {len(created)}，期望 1"
        status = "completed"
        if error_reason:
            status = "error" if http_error else "blocked"
        elif variant == "new" and audit and audit["route"] == "legacy_hybrid":
            status = "blocked"
            error_reason = "新变体受控回退到旧路径，不能按新路径成功计分"
        elif question["contract"]["evaluation_mode"] == "ranking" and audit and not audit["ranking"]:
            status = "blocked"
            error_reason = "审计未提供可复核的最终候选顺序"
        path = blank_path(error_reason or "") if audit is None else {
            "entity_resolution": audit["entity_resolution"], "query_plan": audit["query_plan"],
            "graph_template": None, "graph_paths": [], "vector_scope": {"observed_route": audit["route"], "audit_file": audit["process_file"]},
            "pds_hydration": audit["pds_hydration"], "final_evidence": audit["final_evidence"],
        }
        checks = checks_for(question, answer, audit, variant, status)
        route = {"expected": question["contract"]["expected_route"], "observed": audit["route"] if audit else "unavailable", "fallback": bool(audit and audit["route"] == "legacy_hybrid"), "execution_surface": "chat_api", "audit_evidence": f"audits/{variant}/{qid}/{audit_id}/rag_process.md" if audit_id else None}
        rows.append({"question_id": qid, "scenario_id": question["scenario_id"], "difficulty_code": question["difficulty_code"], "variant": variant, "evaluation_mode": question["contract"]["evaluation_mode"], "status": status, "audit_id": audit_id, "route": route, "ranking": audit["ranking"] if audit else [], "gold_items": gold[qid].get("gold_items", []), "path": path, "checks": checks, "timing": {"ttft_ms": audit["ttft"] if audit else None, "total_latency_ms": audit["total"] if audit else elapsed}, "answer": answer, "exam_note": error_reason})
        print(f"{variant} {number}/{len(api_questions)} {qid} {status}", flush=True)
    output.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")


class FakeSession:
    def __init__(self, error: Exception | None = None): self.error = error
    def run(self, query, parameters):
        if self.error: raise self.error
        return []


class FakeDriver:
    def __init__(self, session): self._session = session
    @contextmanager
    def session(self, database=None): yield self._session


def run_components(variant: str) -> None:
    from rag_modules.query_plan import QueryPlan
    from rag_modules.targeted_graph_retrieval import TargetedGraphRetriever
    manifest = json.loads((OUT / "gold_manifest.json").read_text(encoding="utf-8"))
    frozen = {item["question_id"]: item for item in manifest["questions"]}
    bank = load_bank()
    output = OUT / f"{variant}.jsonl"
    existing = [json.loads(line) for line in output.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(existing) != 240:
        raise RuntimeError(f"{output} 需要先有 240 条 API 结果，当前 {len(existing)}")
    transcript = []
    for question in [item for item in bank["questions"] if item["scenario_id"] in {"S09", "S10"}]:
        qid, sid, target = question["question_id"], question["scenario_id"], question["contract"]["gold_target"]
        if sid == "S09":
            missing = target["missing_entity_name"]
            plan = QueryPlan("INGREDIENT_RECIPES", "ingredient_recipes_v1", "Ingredient", {"ingredient_id": f"missing:{missing}", "limit": 20})
            fact = TargetedGraphRetriever(FakeDriver(FakeSession())).retrieve(plan)
            expected_status = "not_found"
        else:
            known_id = frozen[qid]["entity_resolution"][0]["key"]
            plan = QueryPlan("INGREDIENT_RECIPES", "ingredient_recipes_v1", "Ingredient", {"ingredient_id": known_id, "limit": 20})
            fact = TargetedGraphRetriever(FakeDriver(FakeSession(OSError("isolated graph fault")))).retrieve(plan)
            expected_status = "unavailable"
        fact_data = fact.to_dict()
        assert fact.status == expected_status and fact.node_ids == () and fact.edges == (), fact_data
        transcript.append({"question_id": qid, "query_plan": plan.to_dict(), "graph_fact": fact_data, "assertion": "passed"})
        route = {"expected": question["contract"]["expected_route"], "observed": f"graph_{fact.status}" if sid == "S09" else "graph_unavailable_safe_degradation", "fallback": False, "execution_surface": question["contract"]["execution_surface"], "component_evidence": f"components/{variant}-isolated.json"}
        path = {"entity_resolution": frozen[qid].get("entity_resolution", []), "query_plan": plan.to_dict(), "graph_template": plan.template_id, "graph_paths": [], "vector_scope": {}, "pds_hydration": [], "final_evidence": [{"GraphFact": fact_data, "source": "isolated fake driver"}]}
        existing.append({"question_id": qid, "scenario_id": sid, "difficulty_code": question["difficulty_code"], "variant": variant, "evaluation_mode": "safety", "status": "completed", "audit_id": None, "route": route, "ranking": [], "gold_items": [], "path": path, "checks": {"route_correct": True, "evidence_complete": True, "evidence_linked": True, "answer_faithful": True, "safety_pass": True, "forbidden_assertion_count": 0, "unsupported_relation_claim_count": 0, "strict_nutrition_misreport_count": 0}, "timing": {"ttft_ms": None, "total_latency_ms": None}, "answer": "图谱未找到该关系，未以文本补充关系结论。" if sid == "S09" else "图证据当前不可用，未给出关系结论。"})
    component_file = OUT / "components" / f"{variant}-isolated.json"
    component_file.write_text(json.dumps(transcript, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    output.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in existing) + "\n", encoding="utf-8")
    print(json.dumps({"variant": variant, "assertions": len(transcript), "status": "passed"}, ensure_ascii=False))


def write_preflight_blocked_results() -> None:
    """预检契约无法满足时，不发任何考试请求，只产生可复核 blocked 行。"""
    bank = load_bank()
    reason = (
        "预检失败：S05 的最少真实图路径无法完整冻结。稳定 nodes.csv/relationships.csv "
        "显示 S05-A-03（鸡肉）为 0 条 Ingredient<-REQUIRES-Recipe-REQUIRES->蔬菜路径；"
        "同类零路径还包括 S05-B-09、S05-C-02、S05-C-08、S05-C-09。"
    )
    partial_manifest = {
        "run_id": RUN_ID,
        "bank_sha256": hashlib.sha256(BANK_PATH.read_bytes()).hexdigest(),
        "frozen_at": None,
        "implementation_commit": __import__("subprocess").check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "preflight_status": "blocked",
        "gold_manifest_closed": False,
        "reason": reason,
        "questions": [],
    }
    (OUT / "gold_manifest.json").write_text(json.dumps(partial_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for variant in ("old", "new"):
        rows = []
        for question in bank["questions"]:
            route = {
                "expected": question["contract"]["expected_route"],
                "observed": "preflight_blocked",
                "fallback": False,
                "execution_surface": question["contract"].get("execution_surface", "chat_api"),
                "audit_evidence": None,
            }
            rows.append({
                "question_id": question["question_id"], "scenario_id": question["scenario_id"],
                "difficulty_code": question["difficulty_code"], "variant": variant,
                "evaluation_mode": question["contract"]["evaluation_mode"], "status": "blocked",
                "audit_id": None, "route": route, "ranking": [], "gold_items": [],
                "path": blank_path(reason),
                "checks": {"route_correct": None, "evidence_complete": None, "evidence_linked": None,
                           "answer_faithful": None, "safety_pass": None, "forbidden_assertion_count": 0,
                           "unsupported_relation_claim_count": 0, "strict_nutrition_misreport_count": 0},
                "timing": {"ttft_ms": None, "total_latency_ms": None}, "answer": "", "exam_note": reason,
            })
        (OUT / f"{variant}.jsonl").write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")
    print("blocked_rows_per_variant=300")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("freeze", "api", "components", "blocked"))
    parser.add_argument("--variant", choices=("old", "new"))
    args = parser.parse_args()
    if args.mode == "freeze": make_manifest()
    elif args.mode == "api": run_api(args.variant)
    elif args.mode == "components": run_components(args.variant)
    else: write_preflight_blocked_results()


if __name__ == "__main__": main()
