#!/usr/bin/env python3
"""真实服务考试的只读开考预检。

本工具不写数据库、不调用聊天 API，也不创建考试结果。它将题库、导入 CSV、
Neo4j、PDS 和 Milvus V2 交叉核验，避免监考时因中文终端编码或手工 Cypher
条件与运行时模板不一致而误判。
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import subprocess
import sys
import urllib.request
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

from neo4j import GraphDatabase


EXAM_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = EXAM_ROOT.parents[1]
GENERATOR_PATH = EXAM_ROOT / "工具" / "生成试卷.py"
NODES_PATH = PROJECT_ROOT / "data" / "cypher" / "nodes.csv"
TIPS_NODES_PATH = PROJECT_ROOT / "data" / "cypher" / "tips_nodes.csv"
_NEW_PATH_PROBE_ENV = {
    "RETRIEVAL_INTENT_PLANNER_ENABLED": "false",
    "RETRIEVAL_NEW_PATH_TRAFFIC_PERCENT": "100",
    "RETRIEVAL_PARENT_STORE_ENABLED": "true",
    "RETRIEVAL_ENTITY_DIRECT_ENABLED": "true",
    "RETRIEVAL_QUERY_PLAN_ENABLED": "true",
    "RETRIEVAL_TARGETED_GRAPH_ENABLED": "true",
    "RETRIEVAL_MILVUS_V2_ENABLED": "true",
}


@dataclass(frozen=True)
class StaticNode:
    node_id: str
    label: str
    name: str
    source_path: str | None = None


def _load_generator():
    spec = importlib.util.spec_from_file_location("exam_bank_generator", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("无法加载题库生成器")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _normalize_source_path(value: str | None) -> str:
    normalized = (value or "").replace("\\", "/").lstrip("/")
    return normalized if normalized.startswith("data/") else f"data/{normalized}"


def _read_static_nodes() -> list[StaticNode]:
    nodes: list[StaticNode] = []
    with NODES_PATH.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            if row.get("labels") in {"Recipe", "Ingredient", "CookingStep"} and row.get("nodeId") and row.get("name"):
                source_path = _normalize_source_path(row.get("filePath")) if row.get("filePath") else None
                nodes.append(StaticNode(row["nodeId"], row["labels"], row["name"], source_path))
    with TIPS_NODES_PATH.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            if row.get("labels") == "TechniqueDoc" and row.get("nodeId") and row.get("name"):
                nodes.append(StaticNode(row["nodeId"], "TechniqueDoc", row["name"], _normalize_source_path(row.get("sourcePath"))))
    return nodes


def _index_static_nodes(nodes: Iterable[StaticNode]) -> dict[tuple[str, str, str | None], list[StaticNode]]:
    indexed: dict[tuple[str, str, str | None], list[StaticNode]] = defaultdict(list)
    for node in nodes:
        indexed[(node.label, node.name, node.source_path)].append(node)
    return indexed


def _node_for_target(
    indexed: dict[tuple[str, str, str | None], list[StaticNode]],
    target: dict[str, Any],
) -> StaticNode:
    label = str(target.get("entity_type", ""))
    name = str(target.get("entity_name", ""))
    source_path = target.get("source_path")
    normalized_source = _normalize_source_path(str(source_path)) if source_path else None
    candidates = indexed.get((label, name, normalized_source), [])
    if len(candidates) != 1:
        raise ValueError(f"静态实体无法唯一解析: {label}/{name}/{normalized_source}")
    return candidates[0]


def _question_targets(questions: list[dict[str, Any]], indexed: dict[tuple[str, str, str | None], list[StaticNode]]) -> dict[str, StaticNode]:
    resolved: dict[str, StaticNode] = {}
    for question in questions:
        target = question["contract"]["gold_target"]
        if question["scenario_id"] in {"S01", "S02", "S03", "S04", "S05"}:
            resolved[question["question_id"]] = _node_for_target(indexed, target)
        elif question["scenario_id"] == "S10":
            resolved[question["question_id"]] = _node_for_target(
                indexed,
                {"entity_type": target["entity_type"], "entity_name": target["entity_name"]},
            )
        elif question["scenario_id"] == "S09":
            resolved[question["question_id"]] = _node_for_target(
                indexed,
                {"entity_type": target["known_entity_type"], "entity_name": target["known_entity_name"]},
            )
    return resolved


def _bank_sha256() -> str:
    return hashlib.sha256((EXAM_ROOT / "试卷题库.json").read_bytes()).hexdigest()


def _healthcheck(url: str) -> dict[str, Any]:
    with urllib.request.urlopen(url, timeout=10) as response:  # nosec B310 - user-selected local health URL
        payload = json.loads(response.read().decode("utf-8"))
    if response.status != 200 or payload.get("status") != "healthy":
        raise RuntimeError(f"/health 返回异常: {payload}")
    return payload


def _runtime_nodes(driver: Any, expected: dict[str, StaticNode]) -> dict[str, dict[str, Any]]:
    ids = sorted({node.node_id for node in expected.values()})
    with driver.session(database="neo4j") as session:
        rows = list(
            session.run(
                """
                MATCH (node)
                WHERE node.nodeId IN $ids
                RETURN node.nodeId AS node_id, labels(node) AS labels, node.name AS name,
                       node.filePath AS file_path, node.sourcePath AS source_path
                """,
                ids=ids,
            )
        )
    return {str(row["node_id"]): dict(row) for row in rows}


def _verify_runtime_nodes(expected: dict[str, StaticNode], actual: dict[str, dict[str, Any]]) -> list[str]:
    failures: list[str] = []
    for question_id, node in expected.items():
        row = actual.get(node.node_id)
        if row is None:
            failures.append(f"{question_id}: Neo4j 缺少 nodeId={node.node_id}")
            continue
        if node.label not in row.get("labels", []):
            failures.append(f"{question_id}: Neo4j 标签不符，期望 {node.label}，实际 {row.get('labels')}")
        if row.get("name") != node.name:
            failures.append(f"{question_id}: Neo4j 名称不符，期望 {node.name}，实际 {row.get('name')}")
        if node.source_path:
            runtime_path = row.get("source_path") or row.get("file_path")
            if _normalize_source_path(runtime_path) != node.source_path:
                failures.append(f"{question_id}: Neo4j sourcePath 不符，期望 {node.source_path}，实际 {runtime_path}")
    return failures


def _graph_path_counts(driver: Any, nodes: dict[str, StaticNode]) -> tuple[Counter[str], Counter[str]]:
    ingredient_ids = sorted({node.node_id for node in nodes.values() if node.label == "Ingredient"})
    with driver.session(database="neo4j") as session:
        direct_rows = list(
            session.run(
                """
                MATCH (ingredient:Ingredient)<-[:REQUIRES]-(recipe:Recipe)
                WHERE ingredient.nodeId IN $ids
                RETURN ingredient.nodeId AS ingredient_id, count(DISTINCT recipe) AS path_count
                """,
                ids=ingredient_ids,
            )
        )
        pair_rows = list(
            session.run(
                """
                MATCH (ingredient:Ingredient)<-[:REQUIRES]-(recipe:Recipe)-[vegetable_requirement:REQUIRES]->(vegetable:Ingredient)
                WHERE ingredient.nodeId IN $ids
                  AND vegetable.nodeId <> ingredient.nodeId
                  AND coalesce(vegetable_requirement.ingredientCategory, vegetable.category) = '蔬菜'
                RETURN ingredient.nodeId AS ingredient_id, count(DISTINCT [recipe.nodeId, vegetable.nodeId]) AS path_count
                """,
                ids=ingredient_ids,
            )
        )
    direct = Counter({str(row["ingredient_id"]): int(row["path_count"]) for row in direct_rows})
    pairs = Counter({str(row["ingredient_id"]): int(row["path_count"]) for row in pair_rows})
    return direct, pairs


def _verify_graph_contracts(questions: list[dict[str, Any]], nodes: dict[str, StaticNode], direct: Counter[str], pairs: Counter[str]) -> list[str]:
    failures: list[str] = []
    for question in questions:
        scenario = question["scenario_id"]
        if scenario not in {"S04", "S05"}:
            continue
        node = nodes[question["question_id"]]
        target = question["contract"]["gold_target"]
        if scenario == "S04" and direct[node.node_id] < int(target.get("minimum_verified_graph_paths", 1)):
            failures.append(f"{question['question_id']}: 食材到菜谱路径不足 ({direct[node.node_id]})")
        if scenario == "S05":
            if target.get("expected_verified_graph_paths") == 0:
                if direct[node.node_id] == 0 or pairs[node.node_id] != 0:
                    failures.append(f"{question['question_id']}: 零路径反例不成立，direct={direct[node.node_id]} pairs={pairs[node.node_id]}")
            elif pairs[node.node_id] < int(target.get("minimum_verified_graph_paths", 1)):
                failures.append(f"{question['question_id']}: 食材-菜谱-蔬菜路径不足 ({pairs[node.node_id]})")
    return failures


def _verify_missing_entities(driver: Any, questions: list[dict[str, Any]]) -> list[str]:
    missing_recipes = sorted({question["contract"]["gold_target"]["entity_name"] for question in questions if question["scenario_id"] == "S08"})
    missing_ingredients = sorted({question["contract"]["gold_target"]["missing_entity_name"] for question in questions if question["scenario_id"] == "S09"})
    with driver.session(database="neo4j") as session:
        recipes = [str(row["name"]) for row in session.run("MATCH (node:Recipe) WHERE node.name IN $names RETURN node.name AS name", names=missing_recipes)]
        ingredients = [str(row["name"]) for row in session.run("MATCH (node:Ingredient) WHERE node.name IN $names RETURN node.name AS name", names=missing_ingredients)]
    failures = []
    if recipes:
        failures.append(f"S08 虚构菜名意外存在: {', '.join(sorted(recipes))}")
    if ingredients:
        failures.append(f"S09 虚构食材意外存在: {', '.join(sorted(ingredients))}")
    return failures


def _verify_retrieval_artifact() -> dict[str, Any]:
    sys.path.insert(0, str(PROJECT_ROOT))
    from rag_modules.milvus_v2_index import MilvusV2Schema, RetrievalArtifactManifest, create_milvus_client, pds_manifest_sha256
    from rag_modules.parent_document_store import ParentDocumentStore

    manifest_path = PROJECT_ROOT / "run" / "retrieval" / "retrieval_artifact_manifest.json"
    active_pointer = PROJECT_ROOT / "run" / "retrieval" / "parent_store.active"
    manifest = RetrievalArtifactManifest.read(manifest_path)
    # 由 PDS 自己解释相对路径和容器可移植的绝对路径，预检不得另行拼接路径。
    store = ParentDocumentStore.open(active_pointer.parent, active_pointer=active_pointer)
    try:
        manifest.validate_runtime(
            pds_build_id=store.active_build_id,
            pds_manifest_sha256=pds_manifest_sha256(store, store.active_build_id),
            milvus_database=manifest.milvus_database,
            milvus_collection=manifest.milvus_collection,
            schema_hash=MilvusV2Schema().schema_hash,
        )
        client = create_milvus_client("http://localhost:19530", manifest.milvus_database)
        schema = MilvusV2Schema()
        schema.validate_description(client.describe_collection(collection_name=manifest.milvus_collection))
        stats = client.get_collection_stats(collection_name=manifest.milvus_collection)
        row_count = int(stats.get("row_count", 0))
        expected_rows = store.health_check()["chunk_count"]
        if row_count != expected_rows:
            raise RuntimeError(f"Milvus V2 行数不匹配: {row_count} != PDS chunk_count {expected_rows}")
        return {
            "manifest": manifest.to_dict(),
            "pds": store.health_check(),
            "milvus_row_count": row_count,
        }
    finally:
        store.close()


def _new_path_probe_environment(artifact: dict[str, Any]) -> dict[str, str]:
    """将容器演练绑定到刚通过预检的活动联合工件。"""

    manifest = artifact.get("manifest") if isinstance(artifact, dict) else None
    if not isinstance(manifest, dict):
        raise ValueError("活动 retrieval artifact 缺少 manifest")
    database = manifest.get("milvus_database")
    collection = manifest.get("milvus_collection")
    if not isinstance(database, str) or not database or not isinstance(collection, str) or not collection:
        raise ValueError("活动 retrieval artifact 缺少 Milvus 目标")
    return {
        **_NEW_PATH_PROBE_ENV,
        "RETRIEVAL_MILVUS_DATABASE": database,
        "RETRIEVAL_MILVUS_COLLECTION": collection,
    }


def _probe_new_path(questions: list[dict[str, Any]], artifact: dict[str, Any]) -> list[str]:
    """不调用聊天 API 或模型，只演练新路径的检索组件。"""

    selected_ids = ("S01-A-01", "S03-A-01", "S04-A-01", "S05-A-01", "S05-C-01")
    question_text = {question["question_id"]: question["question"] for question in questions if question["question_id"] in selected_ids}
    if set(question_text) != set(selected_ids):
        return ["题库缺少新路径演练题"]
    probe_program = f'''import json
import threading
from main import AdvancedGraphRAGSystem

queries = {json.dumps(question_text, ensure_ascii=False)!r}
system = AdvancedGraphRAGSystem()
try:
    system.initialize_system()
    result = {{
        "initialized": {{
            "entity_direct": system.entity_direct_retriever is not None,
            "targeted_graph": system.targeted_graph_retriever is not None,
            "restricted_vector": system.restricted_vector_retriever is not None,
        }},
        "queries": {{}},
    }}
    def retrieve_from_request_thread(question_id, query):
        bundle, _ = system.retrieve_for_generation(query, system.config.top_k)
        result["queries"][question_id] = {{
            "has_text": bool(bundle.text_evidence),
            "graph_statuses": sorted({{fact.status for fact in bundle.graph_facts}}),
        }}

    for question_id, query in json.loads(queries).items():
        worker_error = []
        def run_request():
            try:
                retrieve_from_request_thread(question_id, query)
            except Exception as error:
                worker_error.append(f"{{type(error).__name__}}: {{error}}")
        worker = threading.Thread(target=run_request)
        worker.start()
        worker.join()
        if worker_error:
            raise RuntimeError(f"{{question_id}} 请求线程演练失败: {{worker_error[0]}}")
    print("__EXAM_PROBE__=" + json.dumps(result, ensure_ascii=False))
finally:
    system._cleanup()
'''
    try:
        command = ["docker", "exec"]
        for name, value in _new_path_probe_environment(artifact).items():
            command.extend(["-e", f"{name}={value}"])
        command.extend(["what-to-eat-backend", "python", "-c", probe_program])
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=90,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return [f"无法在 backend 容器演练新路径: {type(error).__name__}: {error}"]
    marker = next((line.removeprefix("__EXAM_PROBE__=") for line in completed.stdout.splitlines() if line.startswith("__EXAM_PROBE__=")), None)
    if completed.returncode != 0 or marker is None:
        detail = (completed.stderr or completed.stdout).strip().splitlines()[-1:] or ["无诊断输出"]
        return [f"backend 容器新路径演练失败: {' '.join(detail)}"]
    try:
        result = json.loads(marker)
    except json.JSONDecodeError as error:
        return [f"backend 容器演练结果无法解析: {error}"]
    failures: list[str] = []
    initialized = result.get("initialized", {})
    if not all(initialized.get(name) is True for name in ("entity_direct", "targeted_graph", "restricted_vector")):
        failures.append(f"新路径组件未全部初始化: {initialized}")
    checks = {
        "S01-A-01": "text",
        "S03-A-01": "technique_verified",
        "S04-A-01": "graph_verified",
        "S05-A-01": "graph_verified",
        "S05-C-01": "graph_not_found",
    }
    query_results = result.get("queries", {})
    for question_id, kind in checks.items():
        observation = query_results.get(question_id, {})
        statuses = set(observation.get("graph_statuses", []))
        if kind == "text" and not observation.get("has_text"):
            failures.append(f"{question_id}: 实体直达未回补 PDS 正文")
        elif kind == "technique_verified" and ("verified" not in statuses or not observation.get("has_text")):
            failures.append(f"{question_id}: 技巧图路径或 PDS 回补不可用")
        elif kind == "graph_verified" and "verified" not in statuses:
            failures.append(f"{question_id}: 正向目标图路径未验证")
        elif kind == "graph_not_found" and statuses != {"not_found"}:
            failures.append(f"{question_id}: 零路径反例状态异常: {sorted(statuses)}")
    return failures


def run_preflight(*, health_url: str, probe_new_path: bool) -> dict[str, Any]:
    generator = _load_generator()
    questions = generator._build_questions()
    generator._validate_static_sources(questions)
    generator._validate_graph_targets(questions)
    static_nodes = _read_static_nodes()
    indexed = _index_static_nodes(static_nodes)
    expected = _question_targets(questions, indexed)
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "all-in-rag"))
    failures: list[str] = []
    try:
        health = _healthcheck(health_url)
        runtime_nodes = _runtime_nodes(driver, expected)
        failures.extend(_verify_runtime_nodes(expected, runtime_nodes))
        direct, pairs = _graph_path_counts(driver, expected)
        failures.extend(_verify_graph_contracts(questions, expected, direct, pairs))
        failures.extend(_verify_missing_entities(driver, questions))
    finally:
        driver.close()
    artifact = _verify_retrieval_artifact()
    if probe_new_path:
        failures.extend(_probe_new_path(questions, artifact))
    return {
        "status": "ready" if not failures else "blocked",
        "bank_sha256": _bank_sha256(),
        "question_count": len(questions),
        "health": health,
        "resolved_runtime_targets": len(expected),
        "artifact": artifact,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="真实服务考试只读开考预检")
    parser.add_argument("--health-url", default="http://localhost:8000/health")
    parser.add_argument("--probe-new-path", action="store_true", help="额外演练不调用模型的新路径组件")
    args = parser.parse_args()
    try:
        report = run_preflight(health_url=args.health_url, probe_new_path=args.probe_new_path)
    except Exception as error:
        report = {"status": "blocked", "failures": [f"预检异常: {type(error).__name__}: {error}"]}
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if report["status"] == "ready" else 1


if __name__ == "__main__":
    raise SystemExit(main())
