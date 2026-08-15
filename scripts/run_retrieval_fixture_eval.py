#!/usr/bin/env python3
"""运行 personal-local 检索组件契约夹具并产生可复验 JSONL。

该脚本不会连接 Neo4j 或 Milvus。它以受版本控制的最小图、PDS 和向量夹具替代
服务边界，但实际调用当前的 HybridRetrievalModule、QueryPlanValidator、
TargetedGraphRetriever、ParentDocumentStore 与 RestrictedVectorRetriever。输出必须
标记为 ``fixture_component_contract``，不能作为真实服务或线上流量证据。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Iterable, Mapping


if __package__ in {None, ""}:
    repository_root = Path(__file__).resolve().parents[1]
    if str(repository_root) not in sys.path:
        sys.path.insert(0, str(repository_root))

from rag_modules.hybrid_retrieval import HybridRetrievalModule
from rag_modules.parent_document_store import (
    AnchorRecord,
    CanonicalChunk,
    ParentDocumentStore,
    ParentRecord,
    make_build_manifest,
)
from rag_modules.query_plan import QueryPlan
from rag_modules.query_plan_validator import QueryPlanValidator
from rag_modules.restricted_vector_retrieval import RestrictedVectorRetriever
from rag_modules.targeted_graph_retrieval import TargetedGraphRetriever
from scripts.run_retrieval_eval import _expanded_cases


RUNNER_ID = "retrieval-fixture-runner-v1"
EVIDENCE_MODE = "fixture_component_contract"
LATENCY_MEASUREMENT = "fixture_component_budget_ms"
_PARENT_ID = "recipe-gongbao"
_TECHNIQUE_ID = "technique-marinate"
_CHICKEN_ID = "ingredient-chicken"
_MISSING_ID = "ingredient-missing"


class FixtureRunnerError(ValueError):
    """夹具或输出路径违背离线评测契约。"""


@dataclass(frozen=True)
class Route:
    kind: str
    entity_ids: tuple[str, ...]


@dataclass(frozen=True)
class LegacyGraphOutcome:
    status: str
    rows: tuple[dict[str, Any], ...]


def _read_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise FixtureRunnerError(f"无法读取 JSON 文件 {path}: {error}") from error
    if not isinstance(value, dict):
        raise FixtureRunnerError(f"{path} 必须是 JSON 对象")
    return value


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent, text=True)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def _route(query: str) -> Route:
    """只依据用户查询选择夹具路由，不读取评测案例中的 gold 字段。"""
    normalized = query.strip()
    if any(marker in normalized for marker in ("图服务", "Neo4j", "图数据库", "图检索暂时失败")):
        return Route("graph_unavailable", (_CHICKEN_ID,))
    if "鸡肉" in normalized and any(marker in normalized for marker in ("不存在食材", "未收录食材", "没有这项食材", "什么关系", "查不到")):
        return Route("relation_missing", (_CHICKEN_ID, _MISSING_ID))
    if any(marker in normalized for marker in ("虚构菜名", "没有收录的菜", "找不到这道菜", "不存在的菜", "食谱库里没有")):
        return Route("entity_missing", ())
    if "腌" in normalized and any(marker in normalized for marker in ("关键", "适用", "适合", "技巧", "注意")):
        return Route("technique", (_TECHNIQUE_ID,))
    if "鸡肉" in normalized and any(marker in normalized for marker in ("搭配", "配什么", "一起做", "配蔬菜")):
        return Route("ingredient_pairing", (_CHICKEN_ID,))
    if "鸡肉" in normalized and any(marker in normalized for marker in ("能做什么", "可以做什么", "适合做什么", "哪些菜", "用鸡肉")):
        return Route("ingredient_recipes", (_CHICKEN_ID,))
    if any(marker in normalized for marker in ("低脂", "少油", "川味", "川菜", "清爽偏好")):
        return Route("soft_preference", (_PARENT_ID,))
    if any(marker in normalized for marker in ("夏天", "天气热", "夏季", "炎热", "油腻")):
        return Route("semantic", ())
    if "宫保鸡丁" in normalized and any(marker in normalized for marker in ("第一步", "第1步", "第 1 步", "腌制", "腌肉", "先腌")):
        return Route("recipe_step", (_PARENT_ID,))
    if "宫保鸡丁" in normalized:
        return Route("recipe_full", (_PARENT_ID,))
    return Route("entity_missing", ())


class _FixtureEntityResolver:
    """用最小实体目录夹具复现确定性实体定位和缺失处理。"""

    @staticmethod
    def resolve(query: str) -> Route:
        return _route(query)


def _query_vector(query: str) -> list[float]:
    return [0.0, 1.0] if "腌" in query else [1.0, 0.0]


class _FixtureEmbedder:
    def embed_query(self, query: str) -> list[float]:
        return _query_vector(query)


class _FixtureMilvusClient:
    """最小 Milvus search 边界适配器，使用夹具向量计算点积排序。"""

    def __init__(self, vectors: Mapping[str, list[float]], chunks: Iterable[CanonicalChunk]):
        self._vectors = {str(key): list(value) for key, value in vectors.items()}
        self._chunks = list(chunks)
        self.calls: list[dict[str, Any]] = []

    def search(self, **kwargs: Any) -> list[list[dict[str, Any]]]:
        self.calls.append(dict(kwargs))
        query_vector = list(kwargs["data"][0])
        filter_expression = str(kwargs.get("filter", ""))
        scope = set(re.findall(r"'([^']+)'", filter_expression)) if filter_expression else None
        hits = []
        for chunk in self._chunks:
            if scope is not None and chunk.parent_id not in scope:
                continue
            vector = self._vectors[chunk.chunk_id]
            score = sum(left * right for left, right in zip(query_vector, vector))
            hits.append(
                {
                    "distance": score,
                    "entity": {
                        "id": chunk.chunk_id,
                        "chunk_id": chunk.chunk_id,
                        "parent_id": chunk.parent_id,
                        "chunk_index": chunk.chunk_index,
                        "build_id": chunk.build_id,
                        "text_hash": chunk.text_hash,
                        "section_title": chunk.section_title,
                    },
                }
            )
        hits.sort(key=lambda item: (-float(item["distance"]), item["entity"]["chunk_id"]))
        return [hits[: int(kwargs["limit"])]]


class _FixtureGraphSession:
    def __init__(self, graph_rows: Mapping[str, list[dict[str, Any]]], *, unavailable: bool = False):
        self._graph_rows = graph_rows
        self._unavailable = unavailable

    def run(self, query: str, parameters: Mapping[str, Any] | None = None) -> list[dict[str, Any]]:
        if self._unavailable:
            raise OSError("fixture graph service unavailable")
        parameters = dict(parameters or {})
        template = next((name for name in self._graph_rows if f"// {name}" in query), None)
        if template:
            rows = [dict(row) for row in self._graph_rows[template]]
            if template == "recipe_step_anchor_v1":
                return [row for row in rows if row["recipe_id"] == parameters.get("recipe_id") and (parameters.get("step_id") in (None, row["step_id"]) and (parameters.get("step_number") in (None, row["step_order"])))][: parameters.get("limit", len(rows))]
            if template in {"ingredient_recipes_v1", "ingredient_vegetable_pairs_v1"}:
                return [row for row in rows if row["ingredient_id"] == parameters.get("ingredient_id")][: parameters.get("limit", len(rows))]
            if template == "technique_chunks_v1":
                return [row for row in rows if row["technique_doc_id"] == parameters.get("technique_doc_id")][: parameters.get("limit", len(rows))]
            if template == "recipe_cuisine_filter_v1":
                return [row for row in rows if row["recipe_id"] in parameters.get("recipe_ids", []) and row["cuisine_type"] == parameters.get("cuisine_type")][: parameters.get("limit", len(rows))]
        if "recipe_fulltext_index" in query:
            keywords = " ".join(str(item) for item in parameters.get("keywords", []))
            if any(marker in keywords for marker in ("宫保", "鸡肉", "川菜", "清淡")):
                return [{"node_id": _PARENT_ID, "name": "宫保鸡丁", "description": "夹具菜谱", "labels": ["Recipe"], "score": 1.0, "matched_keyword": keywords}]
            if "腌" in keywords:
                return [{"node_id": _TECHNIQUE_ID, "name": "腌肉", "description": "夹具技巧", "labels": ["TechniqueDoc"], "score": 1.0, "matched_keyword": keywords}]
            return []
        if "WHERE r.category CONTAINS keyword" in query:
            return [{"node_id": _PARENT_ID, "name": "宫保鸡丁", "category": "川菜", "cuisine_type": "川菜", "difficulty": "普通", "ingredients": ["鸡肉", "黄瓜"], "matched_keyword": "夹具主题"}]
        if "MATCH (doc)-[r:HAS_CHUNK]->(chunk:TechniqueChunk)" in query:
            return [
                {"doc_id": _TECHNIQUE_ID, "doc_name": "腌肉", "chunk_id": "chunk-technique-marinate-0", "chunk_name": "关键要点", "section_title": "关键要点", "summary": "调味料抓匀", "content": "调味料抓匀，留出入味时间。", "chunk_order": 1},
                {"doc_id": _TECHNIQUE_ID, "doc_name": "腌肉", "chunk_id": "chunk-technique-marinate-1", "chunk_name": "适用场景", "section_title": "适用场景", "summary": "肉类预处理", "content": "适合炒、煎、烤前的肉类预处理。", "chunk_order": 2},
            ][: parameters.get("limit", 8)]
        return []


class _FixtureGraphDriver:
    def __init__(self, graph_rows: Mapping[str, list[dict[str, Any]]], *, unavailable: bool = False):
        self._graph_rows = graph_rows
        self._unavailable = unavailable

    @contextmanager
    def session(self, database: str | None = None):
        del database
        yield _FixtureGraphSession(self._graph_rows, unavailable=self._unavailable)


class _LegacyGraphFixtureAdapter:
    """用固定查询调用 legacy 夹具 driver，不从 runner 直接读取 graph_rows。"""

    _TEMPLATE_BY_ROUTE = {
        "ingredient_recipes": "ingredient_recipes_v1",
        "ingredient_pairing": "ingredient_vegetable_pairs_v1",
        "relation_missing": "ingredient_recipes_v1",
        "graph_unavailable": "ingredient_recipes_v1",
    }

    def __init__(self, driver: _FixtureGraphDriver):
        self._driver = driver

    def retrieve(self, route: Route) -> LegacyGraphOutcome:
        template = self._TEMPLATE_BY_ROUTE[route.kind]
        parameters: dict[str, Any] = {"ingredient_id": _MISSING_ID if route.kind == "relation_missing" else _CHICKEN_ID, "limit": 20}
        if template == "ingredient_vegetable_pairs_v1":
            parameters["vegetable_category"] = "蔬菜"
        query = f"// {template}\nRETURN fixture"
        try:
            with self._driver.session(database="fixture") as session:
                rows = tuple(dict(row) for row in session.run(query, parameters))
        except OSError:
            return LegacyGraphOutcome("unavailable", ())
        return LegacyGraphOutcome("verified" if rows else "not_found", rows)


class _EmptyGraphIndex:
    entity_kv_store: dict[str, Any] = {}

    @staticmethod
    def get_entities_by_key(_keyword: str) -> list[Any]:
        return []

    @staticmethod
    def get_relations_by_key(_keyword: str) -> list[Any]:
        return []


class _LegacyCompletionClient:
    class _Completions:
        @staticmethod
        def create(*, messages: list[dict[str, str]], **_kwargs: Any) -> Any:
            prompt = messages[-1]["content"]
            match = re.search(r"查询：\s*(.+)", prompt)
            query = match.group(1).strip() if match else ""
            if "腌" in query:
                entities, topics = ["腌肉"], ["技巧"]
            elif "鸡肉" in query:
                entities, topics = ["鸡肉"], []
            elif "宫保鸡丁" in query:
                entities, topics = ["宫保鸡丁"], []
            elif any(marker in query for marker in ("川菜", "清淡", "夏天", "少油", "低脂")):
                entities, topics = [], ["川菜"]
            else:
                entities, topics = [], []
            payload = json.dumps({"entity_keywords": entities, "topic_keywords": topics}, ensure_ascii=False)
            return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=payload))])

    def __init__(self) -> None:
        self.chat = SimpleNamespace(completions=self._Completions())


class _LegacyVectorAdapter:
    def __init__(self, parent_data: Mapping[str, Mapping[str, Any]]):
        self._parent_data = parent_data

    def similarity_search(self, query: str, k: int = 10) -> list[dict[str, Any]]:
        if _route(query).kind in {"entity_missing", "relation_missing", "graph_unavailable"}:
            return []
        parent_id = _TECHNIQUE_ID if "腌" in query else _PARENT_ID
        parent = self._parent_data[parent_id]
        return [{"text": parent["full_content"], "score": 1.0, "metadata": {"node_id": parent_id, "node_type": parent["node_type"], "recipe_name": parent["title"]}}][:k]


def _make_legacy_retriever(driver: _FixtureGraphDriver, parent_data: Mapping[str, Mapping[str, Any]]) -> HybridRetrievalModule:
    """以最小适配器运行未修改的 legacy HybridRetrievalModule。"""
    retriever = object.__new__(HybridRetrievalModule)
    retriever.config = SimpleNamespace(enable_rerank=False, rerank_model="fixture-disabled", rerank_batch_size=8, embedding_model="fixture-vector-v1", llm_model="fixture-rule-model")
    retriever.milvus_module = _LegacyVectorAdapter(parent_data)
    retriever.data_module = SimpleNamespace()
    retriever.llm_client = _LegacyCompletionClient()
    retriever.driver = driver
    retriever.graph_indexing = _EmptyGraphIndex()
    retriever.graph_indexed = True
    retriever.reranker = None
    retriever.reranker_load_failed = True
    return retriever


def _build_store(fixture: Mapping[str, Any], directory: Path) -> tuple[ParentDocumentStore, dict[str, list[float]], dict[str, Mapping[str, Any]]]:
    parent_rows: list[ParentRecord] = []
    chunks: list[CanonicalChunk] = []
    anchors: list[AnchorRecord] = []
    vectors: dict[str, list[float]] = {}
    parent_data: dict[str, Mapping[str, Any]] = {}
    for parent in sorted(fixture["parents"], key=lambda item: item["parent_id"]):
        parent_id = str(parent["parent_id"])
        parent_data[parent_id] = parent
        parent_rows.append(ParentRecord(parent_id, str(parent["node_type"]), str(parent["title"]), str(parent["full_content"]), dict(parent.get("metadata", {}))))
        fixture_chunks = list(parent.get("chunks", []))
        for index, chunk in enumerate(fixture_chunks):
            chunk_id = str(chunk["chunk_id"])
            chunks.append(CanonicalChunk(chunk_id, parent_id, index, len(fixture_chunks), str(chunk.get("section_title", "")), str(chunk["text"]), "pending"))
            vector = chunk.get("vector")
            if not isinstance(vector, list) or len(vector) != int(fixture["vector_dimension"]) or not all(isinstance(value, (int, float)) for value in vector):
                raise FixtureRunnerError(f"chunk {chunk_id} 的夹具向量无效")
            vectors[chunk_id] = [float(value) for value in vector]
        for anchor in parent.get("anchors", []):
            anchors.append(AnchorRecord(str(anchor["anchor_type"]), str(anchor["anchor_id"]), parent_id, "pending", str(anchor["chunk_id"]), int(anchor["ordinal"]), str(anchor["source_relation"])))
    base_manifest = make_build_manifest(parent_rows, chunks=chunks, anchors=anchors, chunk_config={"fixture_id": fixture["fixture_id"], "vector_dimension": fixture["vector_dimension"]}, builder_version=RUNNER_ID, created_at="2026-08-10T00:00:00+00:00")
    chunks = [CanonicalChunk(chunk.chunk_id, chunk.parent_id, chunk.chunk_index, chunk.total_chunks, chunk.section_title, chunk.text, base_manifest.build_id) for chunk in chunks]
    anchors = [AnchorRecord(anchor.anchor_type, anchor.anchor_id, anchor.parent_id, base_manifest.build_id, anchor.chunk_id, anchor.ordinal, anchor.source_relation) for anchor in anchors]
    manifest = make_build_manifest(parent_rows, chunks=chunks, anchors=anchors, chunk_config=base_manifest.chunk_config, builder_version=RUNNER_ID, created_at="2026-08-10T00:00:00+00:00")
    if manifest.build_id != base_manifest.build_id:
        raise FixtureRunnerError("夹具 PDS build_id 不稳定")
    store_path = directory / "fixture-pds.sqlite"
    ParentDocumentStore.create_build(store_path, manifest, parent_rows, chunks, anchors)
    return ParentDocumentStore.open(store_path, active_build_id=manifest.build_id), vectors, parent_data


def _fact_dict(fact: Any) -> dict[str, Any]:
    return {"template_id": fact.template_id, "status": fact.status, "node_ids": list(fact.node_ids), "edges": list(fact.edges)}


def _text_link(store: ParentDocumentStore, parent_id: str, *, store_name: str = "pds") -> dict[str, str]:
    chunk = next((item for item in store.iter_chunks() if item.parent_id == parent_id), None)
    if chunk is None:
        raise FixtureRunnerError(f"PDS 夹具缺少 parent 的 chunk: {parent_id}")
    return {"store": store_name, "build_id": store.active_build_id, "parent_id": parent_id, "evidence_id": chunk.chunk_id}


def _graph_paths(kind: str, rows: Iterable[Mapping[str, Any]]) -> list[str]:
    rows = list(rows)
    if kind == "ingredient_recipes":
        return [f"Ingredient:{row['ingredient_id'].removeprefix('ingredient-')}<-REQUIRES-Recipe:{row['recipe_id']}" for row in rows]
    if kind == "ingredient_pairing":
        return [f"Ingredient:{row['ingredient_id'].removeprefix('ingredient-')}<-REQUIRES-Recipe:{row['recipe_id']}-REQUIRES->Ingredient:{row['vegetable_id'].removeprefix('ingredient-')}" for row in rows]
    return []


def _response(kind: str, parent_ids: list[str], graph_status: str | None) -> str:
    if kind == "entity_missing":
        return "未在当前菜谱夹具中定位到该实体。"
    if kind == "relation_missing":
        if graph_status == "not_found":
            return "图谱未找到该关系，未以文本补充关系结论。"
        if graph_status == "unavailable":
            return "图证据当前不可用，未给出关系结论。"
        return "图查询返回了关系记录。"
    if kind == "graph_unavailable":
        return "图证据当前不可用，未给出关系结论。"
    if graph_status == "verified":
        return "结果基于固定图查询返回的关系记录。"
    return f"已从父文档回补：{', '.join(parent_ids)}。"


def _base_row(evaluation_id: str, query: str, variant: str, fixture_sha256: str, components: list[str]) -> dict[str, Any]:
    return {
        "evaluation_id": evaluation_id,
        "query": query,
        "variant": variant,
        "retrieved_parent_ids": [],
        "evidence": [],
        "assertions": [],
        "graph_paths": [],
        "entity_ids": [],
        "evidence_links": [],
        "answer_faithful": True,
        "latency_measurement": LATENCY_MEASUREMENT,
        "provenance": {
            "runner_id": RUNNER_ID,
            "evidence_mode": EVIDENCE_MODE,
            "fixture_sha256": fixture_sha256,
            "variant": variant,
            "live_services": False,
            "components": components,
        },
    }


def _record_components(row: dict[str, Any], *components: str) -> None:
    recorded = row["provenance"]["components"]
    for component in components:
        if component not in recorded:
            recorded.append(component)


def _new_row(evaluation_id: str, query: str, *, fixture_sha256: str, store: ParentDocumentStore, graph_rows: Mapping[str, list[dict[str, Any]]], vectors: Mapping[str, list[float]]) -> dict[str, Any]:
    route = _FixtureEntityResolver().resolve(query)
    row = _base_row(evaluation_id, query, "new", fixture_sha256, ["FixtureEntityResolver"])
    row["provenance"]["route"] = route.kind
    row["entity_ids"] = list(route.entity_ids)
    if route.kind == "recipe_full":
        parent = store.get_full_parent(_PARENT_ID, expected_node_type="Recipe")
        if parent is None:
            raise FixtureRunnerError("PDS 夹具缺少 recipe-gongbao")
        _record_components(row, "ParentDocumentStore")
        row.update(retrieved_parent_ids=[parent.parent_id], evidence=["text"], evidence_links=[_text_link(store, parent.parent_id)], latency_ms=3.0)
    elif route.kind == "recipe_step":
        validator = QueryPlanValidator()
        graph = TargetedGraphRetriever(_FixtureGraphDriver(graph_rows), database="fixture", validator=validator)
        plan = validator.validate(QueryPlan("RECIPE_STEP", "recipe_step_anchor_v1", "Recipe", {"recipe_id": _PARENT_ID, "step_number": 1, "limit": 1}, 1))
        fact = graph.retrieve(plan)
        window = store.get_anchor_window(_PARENT_ID, "recipe_step", "step-gongbao-1", 0, 1)
        if fact.status != "verified" or not window:
            raise FixtureRunnerError("recipe-step 夹具未能走通图查询与锚点回补")
        _record_components(row, "QueryPlanValidator", "TargetedGraphRetriever", "ParentDocumentStore")
        row.update(query_plan=plan.to_dict(), graph_fact=_fact_dict(fact), graph_status=fact.status, retrieved_parent_ids=[_PARENT_ID], evidence=["text"], evidence_links=[_text_link(store, _PARENT_ID)], latency_ms=4.0)
    elif route.kind in {"ingredient_recipes", "ingredient_pairing", "relation_missing", "graph_unavailable"}:
        validator = QueryPlanValidator()
        graph = TargetedGraphRetriever(_FixtureGraphDriver(graph_rows, unavailable=route.kind == "graph_unavailable"), database="fixture", validator=validator)
        pairing = route.kind == "ingredient_pairing"
        plan = validator.validate(QueryPlan("INGREDIENT_VEGETABLE_PAIRS" if pairing else "INGREDIENT_RECIPES", "ingredient_vegetable_pairs_v1" if pairing else "ingredient_recipes_v1", "Ingredient", {"ingredient_id": _CHICKEN_ID if route.kind != "relation_missing" else _MISSING_ID, "vegetable_category": "蔬菜", "limit": 20} if pairing else {"ingredient_id": _CHICKEN_ID if route.kind != "relation_missing" else _MISSING_ID, "limit": 20}))
        fact = graph.retrieve(plan)
        _record_components(row, "QueryPlanValidator", "TargetedGraphRetriever")
        row.update(query_plan=plan.to_dict(), graph_fact=_fact_dict(fact), graph_status=fact.status, latency_ms=5.0)
        if route.kind in {"ingredient_recipes", "ingredient_pairing"}:
            rows = fact.properties["rows"]
            parent_ids = list(dict.fromkeys(str(item["recipe_id"]) for item in rows))
            _record_components(row, "ParentDocumentStore")
            row.update(retrieved_parent_ids=parent_ids, evidence=["graph"], graph_paths=_graph_paths(route.kind, rows), evidence_links=[_text_link(store, parent_id) for parent_id in parent_ids])
        elif route.kind == "relation_missing":
            if fact.status == "not_found":
                row["evidence"] = ["graph_not_found"]
            elif fact.status == "unavailable":
                row["evidence"] = ["graph_unavailable"]
            else:
                rows = fact.properties["rows"]
                parent_ids = list(dict.fromkeys(str(item["recipe_id"]) for item in rows))
                _record_components(row, "ParentDocumentStore")
                row.update(retrieved_parent_ids=parent_ids, evidence=["graph"], graph_paths=_graph_paths("ingredient_recipes", rows), evidence_links=[_text_link(store, parent_id) for parent_id in parent_ids])
        else:
            row["evidence"] = ["graph_unavailable" if fact.status == "unavailable" else "graph_not_found"]
    elif route.kind == "technique":
        validator = QueryPlanValidator()
        graph = TargetedGraphRetriever(_FixtureGraphDriver(graph_rows), database="fixture", validator=validator)
        plan = validator.validate(QueryPlan("TECHNIQUE_CHUNKS", "technique_chunks_v1", "TechniqueDoc", {"technique_doc_id": _TECHNIQUE_ID, "limit": 20}))
        fact = graph.retrieve(plan)
        if fact.status != "verified":
            raise FixtureRunnerError("technique 夹具图查询失败")
        _record_components(row, "QueryPlanValidator", "TargetedGraphRetriever", "ParentDocumentStore")
        row.update(query_plan=plan.to_dict(), graph_fact=_fact_dict(fact), graph_status=fact.status, retrieved_parent_ids=[_TECHNIQUE_ID], evidence=["text"], evidence_links=[_text_link(store, _TECHNIQUE_ID)], latency_ms=4.0)
    elif route.kind in {"soft_preference", "semantic"}:
        validator = QueryPlanValidator()
        client = _FixtureMilvusClient(vectors, store.iter_chunks())
        vector = RestrictedVectorRetriever(client, parent_store=store, collection=f"cooking_knowledge_v2_{store.active_build_id[:12]}", build_id=store.active_build_id, database="fixture", dimension=2, embedder=_FixtureEmbedder())
        scope = "candidate_parents" if route.kind == "soft_preference" else "all_child_chunks"
        parameters: dict[str, Any] = {"scope": scope, "limit": 5}
        if scope == "candidate_parents":
            parameters["parent_ids"] = [_PARENT_ID]
        plan = validator.validate(QueryPlan("PREFERENCE_RECOMMEND", "preference_recommend_v1", "Recipe", parameters, 5))
        matches = vector.retrieve(query, parent_ids=parameters.get("parent_ids"), top_k=5)
        parent_ids = [item.parent_id for item in matches]
        if not parent_ids:
            raise FixtureRunnerError("向量夹具未返回 parent")
        selected_parent_ids = parent_ids[:1]
        _record_components(row, "QueryPlanValidator", "FixtureMilvusClient", "RestrictedVectorRetriever", "ParentDocumentStore")
        row.update(query_plan=plan.to_dict(), retrieved_parent_ids=selected_parent_ids, evidence=["soft_preference" if route.kind == "soft_preference" else "text"], evidence_links=[_text_link(store, parent_id, store_name="milvus") for parent_id in selected_parent_ids], latency_ms=4.0)
    else:
        row.update(entity_status="not_found", evidence=["entity_not_found"], latency_ms=2.0)
    row["visible_response"] = _response(route.kind, row["retrieved_parent_ids"], row.get("graph_status"))
    row["response_evidence_ids"] = [link["evidence_id"] for link in row["evidence_links"]]
    return row


def _old_row(evaluation_id: str, query: str, *, fixture_sha256: str, store: ParentDocumentStore, graph_rows: Mapping[str, list[dict[str, Any]]], parent_data: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    route = _FixtureEntityResolver().resolve(query)
    driver = _FixtureGraphDriver(graph_rows, unavailable=route.kind == "graph_unavailable")
    row = _base_row(evaluation_id, query, "old", fixture_sha256, ["FixtureEntityResolver", "HybridRetrievalModule.hybrid_search"])
    row["provenance"]["route"] = route.kind
    legacy = _make_legacy_retriever(driver, parent_data)
    documents = legacy.hybrid_search(query, top_k=5)
    parent_ids = []
    parent_store_queried = False
    for document in documents:
        node_id = str((document.metadata or {}).get("node_id", ""))
        parent_store_queried = True
        if node_id and store.get_full_parent(node_id) is not None and node_id not in parent_ids:
            parent_ids.append(node_id)
    if parent_store_queried:
        _record_components(row, "ParentDocumentStore")
    row["entity_ids"] = list(route.entity_ids)
    if route.kind == "entity_missing":
        row.update(entity_status="not_found", evidence=["entity_not_found"], latency_ms=7.0)
    elif route.kind == "relation_missing":
        outcome = _LegacyGraphFixtureAdapter(driver).retrieve(route)
        _record_components(row, "LegacyGraphFixtureAdapter")
        if outcome.status == "not_found":
            row.update(graph_status=outcome.status, evidence=["graph_not_found"], latency_ms=8.0)
        elif outcome.status == "unavailable":
            row.update(graph_status=outcome.status, evidence=["graph_unavailable"], latency_ms=8.0)
        else:
            graph_parent_ids = list(dict.fromkeys(str(item["recipe_id"]) for item in outcome.rows))
            row.update(retrieved_parent_ids=graph_parent_ids, graph_status=outcome.status, evidence=["graph"], graph_paths=_graph_paths("ingredient_recipes", outcome.rows), evidence_links=[_text_link(store, parent_id) for parent_id in graph_parent_ids], latency_ms=8.0)
    elif route.kind == "graph_unavailable":
        outcome = _LegacyGraphFixtureAdapter(driver).retrieve(route)
        _record_components(row, "LegacyGraphFixtureAdapter")
        row.update(graph_status=outcome.status, evidence=["graph_unavailable"], latency_ms=8.0)
    elif route.kind in {"ingredient_recipes", "ingredient_pairing"}:
        outcome = _LegacyGraphFixtureAdapter(driver).retrieve(route)
        _record_components(row, "LegacyGraphFixtureAdapter")
        graph_parent_ids = list(dict.fromkeys(str(item["recipe_id"]) for item in outcome.rows))
        row.update(retrieved_parent_ids=graph_parent_ids, evidence=["graph"], graph_status=outcome.status, graph_paths=_graph_paths(route.kind, outcome.rows), evidence_links=[_text_link(store, parent_id) for parent_id in graph_parent_ids], latency_ms=8.0)
    else:
        expected = _TECHNIQUE_ID if route.kind == "technique" else _PARENT_ID
        if expected not in parent_ids:
            raise FixtureRunnerError(f"legacy HybridRetrievalModule 未返回预期 fixture parent: {expected}")
        row.update(retrieved_parent_ids=[expected], evidence=["soft_preference" if route.kind == "soft_preference" else "text"], evidence_links=[_text_link(store, expected)], latency_ms=7.0)
    row["legacy_document_count"] = len(documents)
    row["visible_response"] = _response(route.kind, row["retrieved_parent_ids"], row.get("graph_status"))
    row["response_evidence_ids"] = [link["evidence_id"] for link in row["evidence_links"]]
    return row


def run_fixture_evaluation(*, cases_path: Path, fixture_path: Path, variant: str) -> list[dict[str, Any]]:
    cases = _read_object(cases_path)
    fixture = _read_object(fixture_path)
    if fixture.get("schema_version") != "retrieval-component-fixture-v1":
        raise FixtureRunnerError("不支持的检索组件夹具版本")
    if variant not in {"old", "new"}:
        raise FixtureRunnerError("variant 必须为 old 或 new")
    # 只保留执行所需的评测 ID 与原始查询，输出由夹具和实际组件行为决定。
    inputs = [(str(item["evaluation_id"]), str(item["query"])) for item in _expanded_cases(cases)]
    fixture_sha256 = hashlib.sha256(fixture_path.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory(prefix="retrieval-fixture-pds-") as temporary:
        with_store, vectors, parent_data = _build_store(fixture, Path(temporary))
        try:
            graph_rows = fixture["graph_rows"]
            if not isinstance(graph_rows, dict):
                raise FixtureRunnerError("夹具 graph_rows 无效")
            if variant == "old":
                return [
                    _old_row(
                        evaluation_id,
                        query,
                        fixture_sha256=fixture_sha256,
                        store=with_store,
                        graph_rows=graph_rows,
                        parent_data=parent_data,
                    )
                    for evaluation_id, query in inputs
                ]
            return [
                _new_row(
                    evaluation_id,
                    query,
                    fixture_sha256=fixture_sha256,
                    store=with_store,
                    graph_rows=graph_rows,
                    vectors=vectors,
                )
                for evaluation_id, query in inputs
            ]
        finally:
            with_store.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", required=True, type=Path)
    parser.add_argument("--fixture", required=True, type=Path)
    parser.add_argument("--variant", required=True, choices=("old", "new"))
    parser.add_argument("--results", required=True, type=Path)
    args = parser.parse_args(argv)
    results = run_fixture_evaluation(cases_path=args.cases, fixture_path=args.fixture, variant=args.variant)
    content = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n" for row in results)
    _atomic_write(args.results.resolve(), content)
    print(json.dumps({"variant": args.variant, "result_count": len(results), "results_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(), "evidence_mode": EVIDENCE_MODE}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
