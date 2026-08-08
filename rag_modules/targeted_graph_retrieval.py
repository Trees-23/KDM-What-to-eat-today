"""阶段 3 的固定白名单 Neo4j 查询执行器。"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Mapping

from .query_plan import TEMPLATE_BY_INTENT, QueryPlan
from .query_plan_validator import QueryPlanValidator
from .retrieval_contracts import GraphFact


TEMPLATE_SPECS = {
    "recipe_step_anchor_v1": {
        "direction": "Recipe - CONTAINS_STEP -> CookingStep",
        "relationship_type": "CONTAINS_STEP",
        "node_keys": ("recipe_id", "step_id"),
        "edge": ("recipe_id", "step_id", "CONTAINS_STEP"),
        "query": """// recipe_step_anchor_v1
MATCH (r:Recipe {nodeId: $recipe_id})-[rel:CONTAINS_STEP]->(step:CookingStep)
WHERE (($step_id IS NOT NULL AND step.nodeId = $step_id)
   OR ($step_number IS NOT NULL AND coalesce(rel.stepOrder, step.stepNumber) = $step_number))
RETURN r.nodeId AS recipe_id, step.nodeId AS step_id,
       coalesce(rel.stepOrder, step.stepNumber) AS step_order
ORDER BY step_order
LIMIT $limit""",
    },
    "ingredient_recipes_v1": {
        "direction": "Ingredient <- REQUIRES - Recipe",
        "relationship_type": "REQUIRES",
        "node_keys": ("ingredient_id", "recipe_id"),
        "edge": ("recipe_id", "ingredient_id", "REQUIRES"),
        "query": """// ingredient_recipes_v1
MATCH (ingredient:Ingredient {nodeId: $ingredient_id})<-[:REQUIRES]-(recipe:Recipe)
RETURN ingredient.nodeId AS ingredient_id, ingredient.name AS ingredient_name,
       recipe.nodeId AS recipe_id, recipe.name AS recipe_name
ORDER BY recipe.nodeId
LIMIT $limit""",
    },
    "ingredient_vegetable_pairs_v1": {
        "direction": "Ingredient <- REQUIRES - Recipe - REQUIRES -> Ingredient",
        "relationship_type": "REQUIRES",
        "node_keys": ("ingredient_id", "recipe_id", "vegetable_id"),
        "edge": (
            ("recipe_id", "ingredient_id", "REQUIRES"),
            ("recipe_id", "vegetable_id", "REQUIRES"),
        ),
        "query": """// ingredient_vegetable_pairs_v1
MATCH (ingredient:Ingredient {nodeId: $ingredient_id})<-[:REQUIRES]-(recipe:Recipe)-[:REQUIRES]->(vegetable:Ingredient)
WHERE vegetable.nodeId <> $ingredient_id AND vegetable.category = $vegetable_category
RETURN ingredient.nodeId AS ingredient_id, ingredient.name AS ingredient_name,
       recipe.nodeId AS recipe_id, recipe.name AS recipe_name,
       vegetable.nodeId AS vegetable_id, vegetable.name AS vegetable_name,
       vegetable.category AS vegetable_category
ORDER BY recipe.nodeId, vegetable.nodeId
LIMIT $limit""",
    },
    "technique_chunks_v1": {
        "direction": "TechniqueDoc - HAS_CHUNK -> TechniqueChunk",
        "relationship_type": "HAS_CHUNK",
        "node_keys": ("technique_doc_id", "technique_chunk_id"),
        "edge": ("technique_doc_id", "technique_chunk_id", "HAS_CHUNK"),
        "query": """// technique_chunks_v1
MATCH (doc:TechniqueDoc {nodeId: $technique_doc_id})-[rel:HAS_CHUNK]->(chunk:TechniqueChunk)
RETURN doc.nodeId AS technique_doc_id, chunk.nodeId AS technique_chunk_id,
       coalesce(rel.chunkOrder, chunk.chunkIndex) AS chunk_order,
       chunk.title AS chunk_title
ORDER BY chunk_order
LIMIT $limit""",
    },
    "recipe_cuisine_filter_v1": {
        "direction": "Recipe property cuisineType filter",
        "relationship_type": "PROPERTY_FILTER",
        "node_keys": ("recipe_id",),
        "edge": (),
        "query": """// recipe_cuisine_filter_v1
MATCH (recipe:Recipe)
WHERE recipe.nodeId IN $recipe_ids AND recipe.cuisineType = $cuisine_type
RETURN recipe.nodeId AS recipe_id, recipe.name AS recipe_name,
       recipe.cuisineType AS cuisine_type
ORDER BY recipe.nodeId
LIMIT $limit""",
    },
}


class TargetedGraphRetriever:
    """只执行 QueryPlanValidator 已允许的固定模板。"""

    def __init__(self, driver: Any, *, database: str | None = None, validator: QueryPlanValidator | None = None):
        if driver is None:
            raise ValueError("TargetedGraphRetriever 需要 Neo4j driver")
        self.driver = driver
        self.database = database
        self.validator = validator or QueryPlanValidator()

    def retrieve(self, plan: QueryPlan | Mapping[str, Any], audit_run: Any = None) -> GraphFact:
        validated = self.validator.validate(plan)
        spec = TEMPLATE_SPECS[validated.template_id]
        timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
        parameters = self._query_parameters(validated)
        self._audit(audit_run, "started", validated, timestamp)
        try:
            rows = self._run(spec["query"], parameters)
        except Exception as error:
            fact = self._fact(
                validated,
                spec,
                rows=(),
                status="unavailable",
                timestamp=timestamp,
                error_type=type(error).__name__,
            )
            self._audit(audit_run, "unavailable", validated, timestamp, error_type=type(error).__name__)
            return fact
        status = "verified" if rows else "not_found"
        fact = self._fact(validated, spec, rows, status=status, timestamp=timestamp)
        self._audit(audit_run, status, validated, timestamp, result_count=len(rows))
        return fact

    @classmethod
    def unavailable_fact(
        cls,
        plan: QueryPlan | Mapping[str, Any],
        *,
        audit_run: Any = None,
        error_type: str = "FeatureFlagDisabled",
    ) -> GraphFact:
        """在图查询未启用时保留受校验计划的显式不可用状态。"""
        validated = QueryPlanValidator().validate(plan)
        timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
        fact = cls._fact(
            validated,
            TEMPLATE_SPECS[validated.template_id],
            rows=(),
            status="unavailable",
            timestamp=timestamp,
            error_type=error_type,
        )
        cls._audit(audit_run, "unavailable", validated, timestamp, error_type=error_type)
        return fact

    @classmethod
    def unavailable_for_intent(
        cls,
        intent: str,
        *,
        audit_run: Any = None,
        error_type: str = "EntityResolverUnavailable",
    ) -> GraphFact:
        """实体解析服务失败且没有稳定 ID 时，返回不含猜测 ID 的不可用事实。"""
        template_id = TEMPLATE_BY_INTENT.get(intent)
        if template_id is None:
            raise ValueError(f"不支持的目标图 intent: {intent}")
        spec = TEMPLATE_SPECS[template_id]
        timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
        fact = GraphFact(
            fact_id=f"{template_id}:{timestamp}",
            template_id=template_id,
            node_ids=(),
            edges=(),
            properties={
                "direction": spec["direction"],
                "relationship_type": spec["relationship_type"],
                "database_timestamp": timestamp,
                "rows": (),
                "max_candidates": 0,
                "error_type": error_type,
            },
            status="unavailable",
        )
        if audit_run is not None and hasattr(audit_run, "record_event"):
            audit_run.record_event(
                "targeted_graph",
                status="unavailable",
                template_id=template_id,
                intent=intent,
                database_timestamp=timestamp,
                error_type=error_type,
            )
        return fact

    @staticmethod
    def _query_parameters(plan: QueryPlan) -> dict[str, Any]:
        parameters = dict(plan.parameters)
        parameters.setdefault("limit", plan.max_candidates)
        if plan.template_id == "recipe_step_anchor_v1":
            parameters.setdefault("step_id", None)
            parameters.setdefault("step_number", None)
        return parameters

    def _run(self, query: str, parameters: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        try:
            context = self.driver.session(database=self.database) if self.database else self.driver.session()
        except TypeError:
            context = self.driver.session()
        with context as session:
            result = session.run(query, dict(parameters))
            return [self._row_to_dict(row) for row in result]

    @staticmethod
    def _row_to_dict(row: Any) -> dict[str, Any]:
        if isinstance(row, Mapping):
            return dict(row)
        if hasattr(row, "data"):
            return dict(row.data())
        try:
            return {key: row[key] for key in row.keys()}
        except (AttributeError, KeyError, TypeError):
            raise ValueError("Neo4j 返回行不是可转换映射")

    @classmethod
    def _fact(
        cls,
        plan: QueryPlan,
        spec: Mapping[str, Any],
        rows: Any,
        *,
        status: str,
        timestamp: str,
        error_type: str | None = None,
    ) -> GraphFact:
        rows = [dict(row) for row in rows]
        node_ids: list[str] = []
        edges: list[dict[str, str]] = []
        edge_spec = spec["edge"]
        if edge_spec and isinstance(edge_spec[0], str):
            edge_spec = (edge_spec,)
        for row in rows:
            for key in spec["node_keys"]:
                value = row.get(key)
                if value is not None and str(value) not in node_ids:
                    node_ids.append(str(value))
            for source_key, target_key, relation in edge_spec:
                source = row.get(source_key)
                target = row.get(target_key)
                if source is not None and target is not None:
                    edge = {"from": str(source), "relationship": relation, "to": str(target)}
                    if edge not in edges:
                        edges.append(edge)
        properties: dict[str, Any] = {
            "direction": spec["direction"],
            "relationship_type": spec["relationship_type"],
            "database_timestamp": timestamp,
            "rows": rows,
            "max_candidates": plan.max_candidates,
        }
        if error_type:
            properties["error_type"] = error_type
        return GraphFact(
            fact_id=f"{plan.template_id}:{timestamp}",
            template_id=plan.template_id,
            node_ids=tuple(node_ids) if status == "verified" else (),
            edges=tuple(edges) if status == "verified" else (),
            properties=properties,
            status=status,
        )

    @staticmethod
    def _audit(audit_run: Any, status: str, plan: QueryPlan, timestamp: str, **fields: Any) -> None:
        if audit_run is not None and hasattr(audit_run, "record_event"):
            audit_run.record_event(
                "targeted_graph",
                status=status,
                template_id=plan.template_id,
                intent=plan.intent,
                database_timestamp=timestamp,
                **fields,
            )
