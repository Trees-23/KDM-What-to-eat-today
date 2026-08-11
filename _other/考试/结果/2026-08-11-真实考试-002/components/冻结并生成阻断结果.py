#!/usr/bin/env python3
"""在真实服务预检阻断后冻结 gold 并写出可复核的 blocked 结果。

此脚本只读题库、CSV、PDS 和 git 元数据；仅写入所在运行目录。
"""
from __future__ import annotations

import csv
import hashlib
import json
import sqlite3
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parents[1]
RUN_ID = OUT.name
BANK_PATH = ROOT / "_other/考试/试卷题库.json"
PDS_PATH = ROOT / "run/retrieval/parent_store.pds_f01044e524ef43b413f76b02.sqlite"

# 语义题在请求前按源 Markdown/PDS 的可复核标题冻结，顺序对应各场景题库顺序。
S06_GOLD = [
    ["凉拌黄瓜", "凉拌金针菇", "白灼虾"], ["西红柿炒鸡蛋", "蚝油生菜", "肉蛋盖饭"],
    ["鸡蛋三明治", "煮泡面加蛋", "牛奶燕麦"], ["清蒸鲈鱼", "油焖大虾", "葱烧海参"],
    ["西红柿鸡蛋汤", "金针菇汤", "紫菜蛋花汤"], ["麻婆豆腐", "酸辣土豆丝", "红烧茄子"],
    ["水煮鱼", "水煮牛肉", "宫保鸡丁"], ["微波葱姜黑鳕鱼", "微波炉腊肠煲仔饭", "微波炉鸡蛋羹"],
    ["清蒸鲈鱼", "清蒸鳜鱼", "红烧鲤鱼"], ["西红柿炒鸡蛋", "麻婆豆腐", "酸辣土豆丝"],
    ["西红柿鸡蛋汤", "紫菜蛋花汤", "羊肉汤"], ["鸡蛋三明治", "煮泡面加蛋", "牛奶燕麦"],
    ["西红柿炒鸡蛋", "蚝油生菜", "清蒸鲈鱼"], ["土豆炖排骨", "简易红烧肉", "羊排焖面"],
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


def load_bank() -> dict[str, Any]:
    return json.loads(BANK_PATH.read_text(encoding="utf-8"))


def source_path(row: dict[str, str]) -> str:
    value = (row.get("filePath") or row.get("sourcePath") or "").replace("\\", "/").lstrip("/")
    return value if value.startswith("data/") else f"data/{value}"


def load_catalog() -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, dict[str, Any]]]:
    nodes: list[dict[str, str]] = []
    for relative in ("data/cypher/nodes.csv", "data/cypher/tips_nodes.csv"):
        with (ROOT / relative).open(encoding="utf-8", newline="") as stream:
            nodes.extend(csv.DictReader(stream))
    with (ROOT / "data/cypher/relationships.csv").open(encoding="utf-8", newline="") as stream:
        relationships = list(csv.DictReader(stream))
    parents: dict[str, dict[str, Any]] = {}
    with sqlite3.connect(PDS_PATH) as connection:
        for parent_id, node_type, title, metadata_json in connection.execute(
            "SELECT parent_id, node_type, title, metadata_json FROM parents"
        ):
            parents[str(parent_id)] = {
                "key": str(parent_id), "node_type": str(node_type), "name": str(title),
                "metadata": json.loads(metadata_json),
            }
    return nodes, relationships, parents


def exact_recipe(nodes: list[dict[str, str]], name: str) -> dict[str, Any]:
    matches = sorted(
        (item for item in nodes if item.get("labels") == "Recipe" and item.get("name") == name),
        key=lambda item: item["nodeId"],
    )
    if not matches:
        raise RuntimeError(f"源节点中缺少语义 gold：{name}")
    node = matches[0]
    return {"key": node["nodeId"], "name": node["name"], "sourcePath": source_path(node)}


def freeze_manifest() -> dict[str, Any]:
    bank = load_bank()
    nodes, relationships, parents = load_catalog()
    by_id = {row["nodeId"]: row for row in nodes if row.get("nodeId")}
    by_name_type: dict[tuple[str, str], list[dict[str, str]]] = {}
    by_source_type: dict[tuple[str, str], list[dict[str, str]]] = {}
    for node in nodes:
        by_name_type.setdefault((node.get("name", ""), node.get("labels", "")), []).append(node)
        by_source_type.setdefault((source_path(node), node.get("labels", "")), []).append(node)
    requires = [row for row in relationships if row.get("relationshipType") == "801000001"]
    outgoing: dict[str, list[dict[str, str]]] = {}
    for relation in requires:
        outgoing.setdefault(relation["startNodeId"], []).append(relation)
    scenario_index: dict[str, int] = {"S06": 0, "S07": 0}
    frozen: list[dict[str, Any]] = []

    for question in bank["questions"]:
        scenario = question["scenario_id"]
        target = question["contract"]["gold_target"]
        record: dict[str, Any] = {
            "question_id": question["question_id"], "scenario_id": scenario,
            "contract": question["contract"], "gold_items": [], "entity_resolution": [], "graph_paths": [],
        }
        if scenario in {"S01", "S02", "S03"}:
            matches = by_source_type.get((target["source_path"], target["entity_type"]), [])
            if len(matches) != 1:
                raise RuntimeError(f"{question['question_id']} sourcePath 未唯一解析：{len(matches)}")
            node = matches[0]
            item = {"key": node["nodeId"], "name": target["entity_name"], "sourcePath": target["source_path"], "relevance": 3}
            record["entity_resolution"] = [item]
            record["gold_items"] = [item]
        elif scenario in {"S04", "S05"}:
            ingredients = sorted(by_name_type.get((target["entity_name"], "Ingredient"), []), key=lambda row: row["nodeId"])
            if not ingredients:
                raise RuntimeError(f"{question['question_id']} 食材未解析")
            record["entity_resolution"] = [
                {"key": item["nodeId"], "name": item["name"], "node_type": "Ingredient", "sourcePath": source_path(item)}
                for item in ingredients
            ]
            graph_paths: list[dict[str, Any]] = []
            for ingredient in ingredients:
                for relation in requires:
                    if relation["endNodeId"] != ingredient["nodeId"]:
                        continue
                    recipe = by_id.get(relation["startNodeId"])
                    if not recipe or recipe.get("labels") != "Recipe":
                        continue
                    base = {
                        "nodes": [ingredient["nodeId"], recipe["nodeId"]],
                        "edges": [{"from": recipe["nodeId"], "to": ingredient["nodeId"], "type": "REQUIRES", "relationshipId": relation["relationshipId"]}],
                        "recipe": recipe["name"], "sourcePath": source_path(recipe),
                    }
                    if scenario == "S04":
                        graph_paths.append(base)
                    else:
                        for other in outgoing.get(recipe["nodeId"], []):
                            vegetable = by_id.get(other["endNodeId"])
                            if other["endNodeId"] == ingredient["nodeId"] or not vegetable:
                                continue
                            if vegetable.get("labels") == "Ingredient" and vegetable.get("category") == "蔬菜":
                                graph_paths.append({
                                    **base, "nodes": [ingredient["nodeId"], recipe["nodeId"], vegetable["nodeId"]],
                                    "edges": base["edges"] + [{"from": recipe["nodeId"], "to": vegetable["nodeId"], "type": "REQUIRES", "relationshipId": other["relationshipId"]}],
                                    "vegetable": vegetable["name"],
                                })
            is_zero_path = target.get("expected_verified_graph_paths") == 0
            if is_zero_path:
                if not any(relation["endNodeId"] == item["nodeId"] for item in ingredients for relation in requires) or graph_paths:
                    raise RuntimeError(f"{question['question_id']} S05 C 零路径契约不成立")
                record["zero_path_evidence"] = {
                    "path_count": 0, "method": "只读 CSV 多跳计数；Neo4j 稳定 nodeId 聚合验证记录于 preflight.md",
                    "query_shape": "Ingredient <- REQUIRES - Recipe - REQUIRES -> Ingredient(category=蔬菜)",
                }
            else:
                if not graph_paths:
                    raise RuntimeError(f"{question['question_id']} 缺少规定图路径")
                record["graph_paths"] = graph_paths
                seen: set[str] = set()
                for graph in graph_paths:
                    recipe_id = graph["nodes"][1]
                    if recipe_id not in seen:
                        seen.add(recipe_id)
                        record["gold_items"].append({"key": recipe_id, "name": graph["recipe"], "sourcePath": graph["sourcePath"], "relevance": 3})
        elif scenario in {"S06", "S07"}:
            index = scenario_index[scenario]
            scenario_index[scenario] += 1
            titles = (S06_GOLD if scenario == "S06" else S07_GOLD)[index]
            record["gold_items"] = [
                {
                    "key": item["key"], "name": item["name"], "relevance": relevance,
                    "sourcePath": item["sourcePath"],
                    "reason": f"请求前按稳定图节点、源 Markdown 分类/做法与题干直接程度冻结；相关性为 {relevance}。",
                }
                for relevance, item in zip((3, 2, 1), (exact_recipe(nodes, title) for title in titles))
            ]
            record["gold_reason"] = "3/2/1 分别代表直接、近似和宽松匹配；排序固定于本 manifest，不受本次检索或回答影响。"
        elif scenario == "S08":
            matches = by_name_type.get((target["entity_name"], "Recipe"), [])
            if matches:
                raise RuntimeError(f"{question['question_id']} 虚构菜名意外存在")
            record["absence_check"] = {"entity_name": target["entity_name"], "matches": 0, "source": "nodes.csv + tips_nodes.csv"}
        elif scenario == "S09":
            known = sorted(by_name_type.get((target["known_entity_name"], "Ingredient"), []), key=lambda row: row["nodeId"])
            missing = by_name_type.get((target["missing_entity_name"], "Ingredient"), [])
            if not known or missing:
                raise RuntimeError(f"{question['question_id']} S09 已知/虚构食材前置条件不成立")
            record["entity_resolution"] = [{"key": item["nodeId"], "name": item["name"], "node_type": "Ingredient"} for item in known]
            record["absence_check"] = {"entity_name": target["missing_entity_name"], "matches": 0, "source": "nodes.csv + tips_nodes.csv"}
        elif scenario == "S10":
            known = sorted(by_name_type.get((target["entity_name"], "Ingredient"), []), key=lambda row: row["nodeId"])
            if not known:
                raise RuntimeError(f"{question['question_id']} S10 已知食材不存在")
            record["entity_resolution"] = [{"key": item["nodeId"], "name": item["name"], "node_type": "Ingredient"} for item in known]
        frozen.append(record)

    return {
        "run_id": RUN_ID, "bank_sha256": hashlib.sha256(BANK_PATH.read_bytes()).hexdigest(),
        "frozen_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "implementation_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "gold_manifest_closed": True,
        "source_of_truth": {
            "nodes": "data/cypher/nodes.csv + data/cypher/tips_nodes.csv",
            "relationships": "data/cypher/relationships.csv",
            "pds": str(PDS_PATH.relative_to(ROOT)),
        },
        "questions": frozen,
    }


def blocked_row(question: dict[str, Any], variant: str, gold: dict[str, Any], reason: str) -> dict[str, Any]:
    contract = question["contract"]
    return {
        "question_id": question["question_id"], "scenario_id": question["scenario_id"],
        "difficulty_code": question["difficulty_code"], "variant": variant,
        "evaluation_mode": contract["evaluation_mode"], "status": "blocked", "audit_id": None,
        "route": {
            "expected": contract["expected_route"], "observed": "preflight_blocked_runtime_dependency",
            "fallback": False, "execution_surface": contract.get("execution_surface", "chat_api"),
            "audit_evidence": None,
        },
        "ranking": [], "gold_items": gold.get("gold_items", []),
        "path": {
            "entity_resolution": gold.get("entity_resolution", []), "query_plan": {}, "graph_template": None,
            "graph_paths": gold.get("graph_paths", []), "vector_scope": {}, "pds_hydration": [],
            "final_evidence": [{"reason": reason, "source": "preflight.md"}],
        },
        "checks": {
            "route_correct": None, "evidence_complete": None, "evidence_linked": None,
            "answer_faithful": None, "safety_pass": None, "forbidden_assertion_count": 0,
            "unsupported_relation_claim_count": 0, "strict_nutrition_misreport_count": 0,
        },
        "timing": {"ttft_ms": None, "total_latency_ms": None}, "answer": "", "exam_note": reason,
    }


def main() -> None:
    if (OUT / "gold_manifest.json").exists() or (OUT / "old.jsonl").exists() or (OUT / "new.jsonl").exists():
        raise RuntimeError("拒绝覆盖已有本次运行产物")
    manifest = freeze_manifest()
    (OUT / "gold_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    reason = "预检阻断：milvus-standalone、milvus-minio、milvus-etcd 均已退出，backend 无法连接 Milvus 并持续重启；/health 未成功。因此未启动 old/new 变体、未发送 API 请求，也未运行隔离组件。"
    frozen = {item["question_id"]: item for item in manifest["questions"]}
    bank = load_bank()
    for variant in ("old", "new"):
        rows = [blocked_row(question, variant, frozen[question["question_id"]], reason) for question in bank["questions"]]
        (OUT / f"{variant}.jsonl").write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")
        (OUT / "responses" / variant / "未执行说明.md").write_text("预检在请求前阻断；没有 HTTP/SSE 响应可保留。\n", encoding="utf-8")
        (OUT / "audits" / variant / "未执行说明.md").write_text("预检在请求前阻断；没有运行时审计目录可复制。\n", encoding="utf-8")
    (OUT / "components" / "未执行说明.md").write_text("预检在 API/组件考试开始前阻断；S09/S10 未运行，未伪造组件脚本输出或断言。\n", encoding="utf-8")
    print(json.dumps({"gold_questions": len(manifest["questions"]), "old_rows": 300, "new_rows": 300, "status": "preflight_blocked"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
