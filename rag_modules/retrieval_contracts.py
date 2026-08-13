"""阶段 2 的检索证据契约。

这些对象是新检索链路的边界：图事实与正文证据始终分开保存，不能用
正文片段补造 ``GraphFact.status=verified`` 的关系结论。
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from .recommendation_evidence import RecommendationEvidence


ENTITY_TYPES = frozenset({"Recipe", "Ingredient", "CookingStep", "TechniqueDoc", "TechniqueChunk"})
MATCH_KINDS = frozenset({"exact_name", "governed_alias", "fulltext"})
GRAPH_FACT_STATUSES = frozenset({"verified", "not_found", "unavailable"})
TEXT_EVIDENCE_ORIGINS = frozenset({"parent_store", "milvus_child"})


def _required_text(value: Any, field_name: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise ValueError(f"{field_name} 不能为空")
    return text


def _string_tuple(value: Sequence[Any], field_name: str, *, allow_empty: bool = True) -> tuple[str, ...]:
    if isinstance(value, (str, bytes)):
        raise ValueError(f"{field_name} 必须是序列，不能是字符串")
    result = tuple(_required_text(item, field_name) for item in value)
    if not allow_empty and not result:
        raise ValueError(f"{field_name} 至少包含一项")
    return result


def _mapping_tuple(value: Sequence[Mapping[str, Any]], field_name: str) -> tuple[Mapping[str, Any], ...]:
    if isinstance(value, (str, bytes)):
        raise ValueError(f"{field_name} 必须是映射序列")
    result = []
    for item in value:
        if not isinstance(item, Mapping):
            raise ValueError(f"{field_name} 只能包含映射")
        result.append(dict(item))
    return tuple(result)


@dataclass(frozen=True)
class EntityCandidate:
    """已定位的图实体候选，绝不代表可以静默选择它。"""

    node_id: str
    node_type: str
    display_name: str
    match_kind: str
    score: float
    ambiguity: bool

    def __post_init__(self) -> None:
        object.__setattr__(self, "node_id", _required_text(self.node_id, "node_id"))
        object.__setattr__(self, "display_name", _required_text(self.display_name, "display_name"))
        if self.node_type not in ENTITY_TYPES:
            raise ValueError(f"不支持的 node_type: {self.node_type}")
        if self.match_kind not in MATCH_KINDS:
            raise ValueError(f"不支持的 match_kind: {self.match_kind}")
        try:
            score = float(self.score)
        except (TypeError, ValueError) as error:
            raise ValueError("score 必须是数值") from error
        if not math.isfinite(score) or not 0.0 <= score <= 1.0:
            raise ValueError("score 必须在 0 到 1 之间")
        object.__setattr__(self, "score", score)
        if not isinstance(self.ambiguity, bool):
            raise ValueError("ambiguity 必须是布尔值")

    def to_dict(self) -> dict[str, Any]:
        return {
            "node_id": self.node_id,
            "node_type": self.node_type,
            "display_name": self.display_name,
            "match_kind": self.match_kind,
            "score": self.score,
            "ambiguity": self.ambiguity,
        }

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "EntityCandidate":
        return cls(**dict(value))


@dataclass(frozen=True)
class GraphFact:
    """固定模板产生的图事实；正文不能写入此对象来证明关系。"""

    fact_id: str
    template_id: str
    node_ids: tuple[str, ...]
    edges: tuple[Mapping[str, Any], ...]
    properties: Mapping[str, Any]
    status: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "fact_id", _required_text(self.fact_id, "fact_id"))
        object.__setattr__(self, "template_id", _required_text(self.template_id, "template_id"))
        object.__setattr__(self, "node_ids", _string_tuple(self.node_ids, "node_ids"))
        object.__setattr__(self, "edges", _mapping_tuple(self.edges, "edges"))
        if not isinstance(self.properties, Mapping):
            raise ValueError("properties 必须是映射")
        if self.status not in GRAPH_FACT_STATUSES:
            raise ValueError(f"不支持的 GraphFact.status: {self.status}")
        if self.status == "verified" and {"text", "content", "page_content"} & set(self.properties):
            raise ValueError("verified GraphFact 不能携带正文文本字段")
        object.__setattr__(self, "properties", dict(self.properties))
        if self.status == "verified" and not self.node_ids:
            raise ValueError("verified GraphFact 必须包含 node_ids")

    def to_dict(self) -> dict[str, Any]:
        return {
            "fact_id": self.fact_id,
            "template_id": self.template_id,
            "node_ids": list(self.node_ids),
            "edges": [dict(edge) for edge in self.edges],
            "properties": dict(self.properties),
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "GraphFact":
        return cls(
            fact_id=value["fact_id"],
            template_id=value["template_id"],
            node_ids=tuple(value["node_ids"]),
            edges=tuple(value["edges"]),
            properties=value["properties"],
            status=value["status"],
        )


@dataclass(frozen=True)
class TextEvidence:
    """经 PDS 回补的正文证据。"""

    parent_id: str
    build_id: str
    chunk_ids: tuple[str, ...]
    anchor_ids: tuple[str, ...]
    text: str
    origin: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "parent_id", _required_text(self.parent_id, "parent_id"))
        object.__setattr__(self, "build_id", _required_text(self.build_id, "build_id"))
        object.__setattr__(self, "chunk_ids", _string_tuple(self.chunk_ids, "chunk_ids", allow_empty=False))
        object.__setattr__(self, "anchor_ids", _string_tuple(self.anchor_ids, "anchor_ids"))
        object.__setattr__(self, "text", _required_text(self.text, "text"))
        if self.origin not in TEXT_EVIDENCE_ORIGINS:
            raise ValueError(f"不支持的 TextEvidence.origin: {self.origin}")

    def to_dict(self) -> dict[str, Any]:
        return {
            "parent_id": self.parent_id,
            "build_id": self.build_id,
            "chunk_ids": list(self.chunk_ids),
            "anchor_ids": list(self.anchor_ids),
            "text": self.text,
            "origin": self.origin,
        }

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "TextEvidence":
        return cls(
            parent_id=value["parent_id"],
            build_id=value["build_id"],
            chunk_ids=tuple(value["chunk_ids"]),
            anchor_ids=tuple(value["anchor_ids"]),
            text=value["text"],
            origin=value["origin"],
        )


@dataclass(frozen=True)
class EvidenceBundle:
    """把计划、实体、图事实、正文和限制明确分栏的传递对象。"""

    query_plan: Mapping[str, Any] | None
    entity_candidates: tuple[EntityCandidate, ...]
    graph_facts: tuple[GraphFact, ...]
    text_evidence: tuple[TextEvidence, ...]
    limitations: tuple[str, ...]
    recommendation_evidence: RecommendationEvidence | None = None
    claim_policy: Mapping[str, Sequence[str]] | None = None

    def __post_init__(self) -> None:
        if self.query_plan is not None and not isinstance(self.query_plan, Mapping):
            raise ValueError("query_plan 必须是映射或 None")
        object.__setattr__(self, "query_plan", dict(self.query_plan) if self.query_plan is not None else None)
        object.__setattr__(self, "entity_candidates", tuple(self.entity_candidates))
        object.__setattr__(self, "graph_facts", tuple(self.graph_facts))
        object.__setattr__(self, "text_evidence", tuple(self.text_evidence))
        if not all(isinstance(item, EntityCandidate) for item in self.entity_candidates):
            raise ValueError("entity_candidates 只能包含 EntityCandidate")
        if not all(isinstance(item, GraphFact) for item in self.graph_facts):
            raise ValueError("graph_facts 只能包含 GraphFact")
        if not all(isinstance(item, TextEvidence) for item in self.text_evidence):
            raise ValueError("text_evidence 只能包含 TextEvidence")
        object.__setattr__(self, "limitations", _string_tuple(self.limitations, "limitations"))
        if self.recommendation_evidence is not None and not isinstance(
            self.recommendation_evidence, RecommendationEvidence
        ):
            raise ValueError("recommendation_evidence 必须是 RecommendationEvidence 或 None")
        if self.claim_policy is not None:
            if not isinstance(self.claim_policy, Mapping):
                raise ValueError("claim_policy 必须是映射或 None")
            allowed = {"hard_constraints", "soft_preferences", "display_requests", "forbidden_claims"}
            if set(self.claim_policy) - allowed:
                raise ValueError("claim_policy 包含未声明字段")
            policy: dict[str, tuple[str, ...]] = {}
            for key, value in self.claim_policy.items():
                if key not in allowed:
                    continue
                policy[key] = _string_tuple(value, f"claim_policy.{key}")
            object.__setattr__(self, "claim_policy", policy)

    @property
    def verified_graph_facts(self) -> tuple[GraphFact, ...]:
        return tuple(fact for fact in self.graph_facts if fact.status == "verified")

    @property
    def requires_legacy_fallback(self) -> bool:
        return "parent-store-unavailable" in self.limitations

    def to_dict(self) -> dict[str, Any]:
        return {
            "query_plan": dict(self.query_plan) if self.query_plan is not None else None,
            "entity_candidates": [candidate.to_dict() for candidate in self.entity_candidates],
            "graph_facts": [fact.to_dict() for fact in self.graph_facts],
            "text_evidence": [evidence.to_dict() for evidence in self.text_evidence],
            "limitations": list(self.limitations),
            "recommendation_evidence": (
                self.recommendation_evidence.to_dict() if self.recommendation_evidence is not None else None
            ),
            "claim_policy": (
                {key: list(values) for key, values in self.claim_policy.items()}
                if self.claim_policy is not None
                else None
            ),
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, sort_keys=True)

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "EvidenceBundle":
        return cls(
            query_plan=value.get("query_plan"),
            entity_candidates=tuple(EntityCandidate.from_dict(item) for item in value["entity_candidates"]),
            graph_facts=tuple(GraphFact.from_dict(item) for item in value["graph_facts"]),
            text_evidence=tuple(TextEvidence.from_dict(item) for item in value["text_evidence"]),
            limitations=tuple(value["limitations"]),
            recommendation_evidence=(
                RecommendationEvidence.from_dict(value["recommendation_evidence"])
                if value.get("recommendation_evidence") is not None
                else None
            ),
            claim_policy=value.get("claim_policy"),
        )

    @classmethod
    def from_json(cls, payload: str) -> "EvidenceBundle":
        decoded = json.loads(payload)
        if not isinstance(decoded, Mapping):
            raise ValueError("EvidenceBundle JSON 必须是对象")
        return cls.from_dict(decoded)
