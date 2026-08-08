"""阶段 2 的实体直达 PDS 检索。

本模块只允许固定、参数化的锚点定位器。它既不接收任意 Cypher，也不持有
Milvus 客户端，因此明确实体命中不可能退化为全库向量检索。
"""

from __future__ import annotations

import re
from typing import Any, Mapping

from .parent_document_store import ParentDocumentStore, TextEvidenceSource
from .retrieval_contracts import EntityCandidate, EvidenceBundle, GraphFact, TextEvidence


class EntityDirectRetriever:
    """将已经定位的 Recipe/Technique 实体回补为 PDS 正文证据。"""

    _MAX_WINDOW = 2

    def __init__(self, parent_store: ParentDocumentStore, driver: Any, *, database: str | None = None) -> None:
        if parent_store is None:
            raise ValueError("EntityDirectRetriever 需要已打开的 ParentDocumentStore")
        if driver is None:
            raise ValueError("EntityDirectRetriever 需要已初始化的 Neo4j driver")
        self.parent_store = parent_store
        self.driver = driver
        self.database = database

    def retrieve(self, entity: EntityCandidate, request_scope: str | Mapping[str, Any], audit_run: Any = None) -> EvidenceBundle:
        if not isinstance(entity, EntityCandidate):
            raise ValueError("entity 必须是 EntityCandidate")
        if entity.ambiguity:
            return self._bundle(
                entity,
                limitations=("ENTITY_AMBIGUOUS", "实体候选并列，未自动选择任一实体。"),
            )

        scope = self._parse_scope(entity, request_scope)
        self._audit(audit_run, "entity_direct_request", status="started", entity_id=entity.node_id, scope=scope["scope"])
        if scope["scope"] in {"RECIPE_FULL", "TECHNIQUE_FULL"}:
            return self._retrieve_full(entity, scope, audit_run)
        if scope["scope"] == "RECIPE_STEP":
            return self._retrieve_recipe_step(entity, scope, audit_run)
        return self._retrieve_technique_section(entity, scope, audit_run)

    def _retrieve_full(self, entity: EntityCandidate, scope: Mapping[str, Any], audit_run: Any) -> EvidenceBundle:
        expected_type = "Recipe" if scope["scope"] == "RECIPE_FULL" else "TechniqueDoc"
        try:
            parent = self.parent_store.get_full_parent(entity.node_id, expected_node_type=expected_type)
            if parent is None:
                self._audit(audit_run, "entity_direct_pds", status="not_found", parent_id=entity.node_id)
                return self._bundle(
                    entity,
                    graph_facts=(self._entity_fact(entity),),
                    limitations=("PARENT_DOCUMENT_NOT_FOUND", "已定位实体，但当前 PDS build 未包含对应正文。"),
                )
            chunk_ids = tuple(
                chunk.chunk_id
                for chunk in self.parent_store.iter_chunks(parent.build_id)
                if chunk.parent_id == parent.parent_id
            )
            if not chunk_ids:
                raise ValueError(f"PDS 父文档没有可验证 chunk: {parent.parent_id}")
            text_evidence = TextEvidence(
                parent_id=parent.parent_id,
                build_id=parent.build_id,
                chunk_ids=chunk_ids,
                anchor_ids=(),
                text=parent.full_content,
                origin="parent_store",
            )
            fact = self._entity_fact(entity)
            self._audit(
                audit_run,
                "entity_direct_pds",
                status="verified",
                parent_id=parent.parent_id,
                build_id=parent.build_id,
                chunk_count=len(chunk_ids),
            )
            return self._bundle(entity, graph_facts=(fact,), text_evidence=(text_evidence,))
        except Exception as error:
            self._audit(audit_run, "entity_direct_pds", status="unavailable", error_type=type(error).__name__)
            return self._bundle(
                entity,
                graph_facts=(self._entity_fact(entity),),
                limitations=("parent-store-unavailable", "父文档库不可用，已关闭实体直达并应回退旧检索路径。"),
            )

    def _retrieve_recipe_step(self, entity: EntityCandidate, scope: Mapping[str, Any], audit_run: Any) -> EvidenceBundle:
        try:
            row = self._single(
                """// recipe_step_anchor_v1
MATCH (r:Recipe {nodeId: $recipe_id})-[c:CONTAINS_STEP]->(s:CookingStep)
WHERE ($step_id IS NOT NULL AND s.nodeId = $step_id)
   OR ($step_id IS NULL AND c.stepOrder = $step_number)
RETURN s.nodeId AS step_id, c.stepOrder AS step_order, s.stepNumber AS step_number
ORDER BY c.stepOrder, s.nodeId
LIMIT 1""",
                {
                    "recipe_id": entity.node_id,
                    "step_id": scope["step_id"],
                    "step_number": scope["step_number"],
                },
            )
        except Exception as error:
            fact = GraphFact(
                fact_id=f"recipe-step:{entity.node_id}",
                template_id="recipe_step_anchor_v1",
                node_ids=(),
                edges=(),
                properties={},
                status="unavailable",
            )
            self._audit(audit_run, "recipe_step_anchor", status="unavailable", error_type=type(error).__name__)
            return self._bundle(entity, graph_facts=(self._entity_fact(entity), fact), limitations=("graph-unavailable",))

        if row is None or not self._value(row, "step_id"):
            fact = GraphFact(
                fact_id=f"recipe-step:{entity.node_id}",
                template_id="recipe_step_anchor_v1",
                node_ids=(),
                edges=(),
                properties={"recipe_id": entity.node_id},
                status="not_found",
            )
            self._audit(audit_run, "recipe_step_anchor", status="not_found", recipe_id=entity.node_id)
            return self._bundle(entity, graph_facts=(self._entity_fact(entity), fact), limitations=("STEP_NOT_FOUND",))

        step_id = str(self._value(row, "step_id"))
        fact = GraphFact(
            fact_id=f"recipe-step:{entity.node_id}:{step_id}",
            template_id="recipe_step_anchor_v1",
            node_ids=(entity.node_id, step_id),
            edges=(
                {
                    "from": entity.node_id,
                    "relationship": "CONTAINS_STEP",
                    "to": step_id,
                    "direction": "outbound",
                },
            ),
            properties={
                "step_order": self._value(row, "step_order"),
                "step_number": self._value(row, "step_number"),
            },
            status="verified",
        )
        self._audit(audit_run, "recipe_step_anchor", status="verified", recipe_id=entity.node_id, step_id=step_id)
        return self._hydrate_anchor(
            entity,
            parent_id=entity.node_id,
            anchor_type="CookingStep",
            anchor_id=step_id,
            before=scope["before"],
            after=scope["after"],
            graph_facts=(self._entity_fact(entity), fact),
            audit_run=audit_run,
        )

    def _retrieve_technique_section(self, entity: EntityCandidate, scope: Mapping[str, Any], audit_run: Any) -> EvidenceBundle:
        chunk_id = scope["chunk_id"] if entity.node_type == "TechniqueDoc" else entity.node_id
        try:
            row = self._single(
                """// technique_chunk_anchor_v1
MATCH (t:TechniqueDoc)-[c:HAS_CHUNK]->(chunk:TechniqueChunk {nodeId: $chunk_id})
WHERE ($document_id IS NULL OR t.nodeId = $document_id)
RETURN t.nodeId AS document_id, chunk.nodeId AS chunk_id, c.chunkOrder AS chunk_order
ORDER BY c.chunkOrder, chunk.nodeId
LIMIT 1""",
                {"document_id": entity.node_id if entity.node_type == "TechniqueDoc" else None, "chunk_id": chunk_id},
            )
        except Exception as error:
            fact = GraphFact(
                fact_id=f"technique-chunk:{chunk_id}",
                template_id="technique_chunk_anchor_v1",
                node_ids=(),
                edges=(),
                properties={},
                status="unavailable",
            )
            self._audit(audit_run, "technique_chunk_anchor", status="unavailable", error_type=type(error).__name__)
            return self._bundle(entity, graph_facts=(self._entity_fact(entity), fact), limitations=("graph-unavailable",))
        if row is None or not self._value(row, "document_id"):
            fact = GraphFact(
                fact_id=f"technique-chunk:{chunk_id}",
                template_id="technique_chunk_anchor_v1",
                node_ids=(),
                edges=(),
                properties={},
                status="not_found",
            )
            self._audit(audit_run, "technique_chunk_anchor", status="not_found", chunk_id=chunk_id)
            return self._bundle(entity, graph_facts=(self._entity_fact(entity), fact), limitations=("TECHNIQUE_CHUNK_NOT_FOUND",))

        document_id = str(self._value(row, "document_id"))
        verified = GraphFact(
            fact_id=f"technique-chunk:{document_id}:{chunk_id}",
            template_id="technique_chunk_anchor_v1",
            node_ids=(document_id, chunk_id),
            edges=({"from": document_id, "relationship": "HAS_CHUNK", "to": chunk_id, "direction": "outbound"},),
            properties={"chunk_order": self._value(row, "chunk_order")},
            status="verified",
        )
        return self._hydrate_anchor(
            entity,
            parent_id=document_id,
            anchor_type="TechniqueChunk",
            anchor_id=chunk_id,
            before=scope["before"],
            after=scope["after"],
            graph_facts=(self._entity_fact(entity), verified),
            audit_run=audit_run,
        )

    def _hydrate_anchor(
        self,
        entity: EntityCandidate,
        *,
        parent_id: str,
        anchor_type: str,
        anchor_id: str,
        before: int,
        after: int,
        graph_facts: tuple[GraphFact, ...],
        audit_run: Any,
    ) -> EvidenceBundle:
        try:
            rows = self.parent_store.get_anchor_window(parent_id, anchor_type, anchor_id, before, after)
            if not rows:
                self._audit(audit_run, "entity_direct_pds", status="not_found", parent_id=parent_id, anchor_id=anchor_id)
                return self._bundle(
                    entity,
                    graph_facts=graph_facts,
                    limitations=("PDS_ANCHOR_NOT_FOUND", "图锚点已定位，但 PDS 中没有对应正文窗口。"),
                )
            evidence = self._window_evidence(rows)
            text_evidence = (evidence,)
            if anchor_type == "CookingStep" and "## 所需食材" not in evidence.text:
                ingredient_context = self._recipe_ingredient_context(parent_id)
                if ingredient_context is not None:
                    text_evidence += (ingredient_context,)
            self._audit(
                audit_run,
                "entity_direct_pds",
                status="verified",
                parent_id=parent_id,
                build_id=evidence.build_id,
                anchor_id=anchor_id,
                chunk_count=sum(len(item.chunk_ids) for item in text_evidence),
            )
            return self._bundle(entity, graph_facts=graph_facts, text_evidence=text_evidence)
        except Exception as error:
            self._audit(audit_run, "entity_direct_pds", status="unavailable", error_type=type(error).__name__)
            return self._bundle(
                entity,
                graph_facts=graph_facts,
                limitations=("parent-store-unavailable", "父文档库不可用，已关闭实体直达并应回退旧检索路径。"),
            )

    @staticmethod
    def _window_evidence(rows: list[TextEvidenceSource]) -> TextEvidence:
        first = rows[0]
        if any(row.parent_id != first.parent_id or row.build_id != first.build_id for row in rows):
            raise ValueError("PDS 窗口混入了不同 parent/build")
        chunk_ids = tuple(row.chunk_id for row in rows)
        anchor_ids = tuple(sorted({anchor for row in rows for anchor in row.anchor_ids}))
        return TextEvidence(
            parent_id=first.parent_id,
            build_id=first.build_id,
            chunk_ids=chunk_ids,
            anchor_ids=anchor_ids,
            text="\n\n".join(row.text for row in rows),
            origin="parent_store",
        )

    def _recipe_ingredient_context(self, parent_id: str) -> TextEvidence | None:
        """从同一 PDS parent 提取步骤回答所需的食材段，不扫描 Markdown 源目录。"""
        parent = self.parent_store.get_full_parent(parent_id, expected_node_type="Recipe")
        if parent is None:
            return None
        match = re.search(r"(?ms)^## 所需食材\s*$\n?(.*?)(?=^## |\Z)", parent.full_content)
        if match is None or not match.group(0).strip():
            return None
        chunk_ids = tuple(
            chunk.chunk_id
            for chunk in self.parent_store.iter_chunks(parent.build_id)
            if chunk.parent_id == parent_id and "## 所需食材" in chunk.text
        )
        if not chunk_ids:
            return None
        return TextEvidence(
            parent_id=parent_id,
            build_id=parent.build_id,
            chunk_ids=chunk_ids,
            anchor_ids=(),
            text=match.group(0).strip(),
            origin="parent_store",
        )

    @staticmethod
    def _entity_fact(entity: EntityCandidate) -> GraphFact:
        return GraphFact(
            fact_id=f"entity:{entity.node_id}",
            template_id="entity_resolution_v1",
            node_ids=(entity.node_id,),
            edges=(),
            properties={"node_type": entity.node_type, "display_name": entity.display_name, "match_kind": entity.match_kind},
            status="verified",
        )

    @staticmethod
    def _bundle(
        entity: EntityCandidate,
        *,
        graph_facts: tuple[GraphFact, ...] = (),
        text_evidence: tuple[TextEvidence, ...] = (),
        limitations: tuple[str, ...] = (),
    ) -> EvidenceBundle:
        return EvidenceBundle(
            query_plan=None,
            entity_candidates=(entity,),
            graph_facts=graph_facts,
            text_evidence=text_evidence,
            limitations=limitations,
        )

    def _parse_scope(self, entity: EntityCandidate, request_scope: str | Mapping[str, Any]) -> dict[str, Any]:
        if isinstance(request_scope, str):
            raw = {"scope": request_scope}
        elif isinstance(request_scope, Mapping):
            raw = dict(request_scope)
        else:
            raise ValueError("request_scope 必须是字符串或映射")
        scope = raw.get("scope")
        if not isinstance(scope, str):
            raise ValueError("request_scope.scope 必须是字符串")
        allowed = {"scope", "step_id", "step_number", "chunk_id", "before", "after"}
        unexpected = set(raw) - allowed
        if unexpected:
            raise ValueError(f"实体直达定位器拒绝未授权参数: {sorted(unexpected)}")
        if entity.node_type == "Recipe" and scope == "RECIPE_FULL":
            self._only_keys(raw, {"scope"})
            return {"scope": scope}
        if entity.node_type == "Recipe" and scope == "RECIPE_STEP":
            self._only_keys(raw, {"scope", "step_id", "step_number", "before", "after"})
            step_id = raw.get("step_id")
            step_number = raw.get("step_number")
            if bool(step_id) == (step_number is not None):
                raise ValueError("RECIPE_STEP 必须且只能提供 step_id 或 step_number")
            if step_id is not None and (not isinstance(step_id, str) or not step_id.strip()):
                raise ValueError("step_id 必须是非空字符串")
            if step_number is not None and (not isinstance(step_number, int) or isinstance(step_number, bool) or step_number < 1):
                raise ValueError("step_number 必须是正整数")
            return {
                "scope": scope,
                "step_id": step_id.strip() if isinstance(step_id, str) else None,
                "step_number": step_number,
                "before": self._window_value(raw.get("before", 1), "before"),
                "after": self._window_value(raw.get("after", 1), "after"),
            }
        if entity.node_type == "TechniqueDoc" and scope == "TECHNIQUE_FULL":
            self._only_keys(raw, {"scope"})
            return {"scope": scope}
        if entity.node_type == "TechniqueDoc" and scope == "TECHNIQUE_SECTION":
            self._only_keys(raw, {"scope", "chunk_id", "before", "after"})
            chunk_id = raw.get("chunk_id")
            if not isinstance(chunk_id, str) or not chunk_id.strip():
                raise ValueError("TECHNIQUE_SECTION 需要 chunk_id")
            return {"scope": scope, "chunk_id": chunk_id.strip(), "before": self._window_value(raw.get("before", 1), "before"), "after": self._window_value(raw.get("after", 1), "after")}
        if entity.node_type == "TechniqueChunk" and scope == "TECHNIQUE_SECTION":
            self._only_keys(raw, {"scope", "before", "after"})
            return {"scope": scope, "chunk_id": entity.node_id, "before": self._window_value(raw.get("before", 1), "before"), "after": self._window_value(raw.get("after", 1), "after")}
        raise ValueError(f"实体类型 {entity.node_type} 不支持请求范围 {scope}")

    @staticmethod
    def _only_keys(raw: Mapping[str, Any], allowed: set[str]) -> None:
        extras = set(raw) - allowed
        if extras:
            raise ValueError(f"请求范围不接受参数: {sorted(extras)}")

    @classmethod
    def _window_value(cls, value: Any, name: str) -> int:
        if not isinstance(value, int) or isinstance(value, bool) or not 0 <= value <= cls._MAX_WINDOW:
            raise ValueError(f"{name} 必须是 0 到 {cls._MAX_WINDOW} 的整数")
        return value

    def _single(self, query: str, parameters: Mapping[str, Any]) -> Any | None:
        try:
            session_context = self.driver.session(database=self.database) if self.database else self.driver.session()
        except TypeError:
            session_context = self.driver.session()
        with session_context as session:
            rows = list(session.run(query, dict(parameters)))
        return rows[0] if rows else None

    @staticmethod
    def _value(row: Any, key: str, default: Any = None) -> Any:
        if isinstance(row, Mapping):
            return row.get(key, default)
        try:
            return row.get(key, default)
        except AttributeError:
            try:
                return row[key]
            except (KeyError, TypeError):
                return default

    @staticmethod
    def _audit(audit_run: Any, stage: str, *, status: str, **fields: Any) -> None:
        if audit_run is not None and hasattr(audit_run, "record_event"):
            audit_run.record_event(stage, status=status, **fields)
