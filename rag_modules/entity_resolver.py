"""固定优先级的 Neo4j 实体解析器，不依赖或调用全库向量检索。"""

from __future__ import annotations

import re
from dataclasses import replace
from typing import Any, Iterable, Mapping, Sequence

from .retrieval_contracts import ENTITY_TYPES, EntityCandidate


_ENTITY_CONFIG = {
    "Recipe": {"label": "Recipe", "fulltext_index": "recipe_fulltext_index"},
    "Ingredient": {"label": "Ingredient", "fulltext_index": "ingredient_fulltext_index"},
    "CookingStep": {"label": "CookingStep", "fulltext_index": "cookingstep_fulltext_index"},
    "TechniqueDoc": {"label": "TechniqueDoc", "fulltext_index": "technique_doc_fulltext_index"},
    "TechniqueChunk": {"label": "TechniqueChunk", "fulltext_index": "technique_chunk_fulltext_index"},
}


class EntityResolver:
    """按精确名称、治理别名、已验证全文索引依次定位实体。"""

    def __init__(self, driver: Any, *, database: str | None = None, max_candidates: int = 5) -> None:
        if driver is None:
            raise ValueError("EntityResolver 需要已初始化的 Neo4j driver")
        if max_candidates < 1 or max_candidates > 20:
            raise ValueError("max_candidates 必须在 1 到 20 之间")
        self.driver = driver
        self.database = database
        self.max_candidates = max_candidates

    def resolve(self, query_text: str, expected_types: Sequence[str]) -> list[EntityCandidate]:
        normalized = self._normalize_query(query_text)
        entity_types = self._validate_expected_types(expected_types)
        if not normalized:
            return []

        for match_kind, score, template in (
            ("exact_name", 1.0, self._exact_query),
            ("governed_alias", 0.95, self._alias_query),
            ("fulltext", None, self._fulltext_query),
        ):
            candidates = self._run_priority(template, normalized, entity_types, match_kind, score)
            if candidates:
                return self._mark_ambiguity(candidates)
        return []

    @staticmethod
    def _normalize_query(query_text: str) -> str:
        if not isinstance(query_text, str):
            raise ValueError("query_text 必须是字符串")
        normalized = re.sub(r"[？?！!。．，,；;：:\n\r]+", " ", query_text).strip()
        return re.sub(r"\s+", " ", normalized)

    @staticmethod
    def _validate_expected_types(expected_types: Sequence[str]) -> tuple[str, ...]:
        if isinstance(expected_types, (str, bytes)) or not expected_types:
            raise ValueError("expected_types 必须是非空实体类型序列")
        types = tuple(expected_types)
        if len(set(types)) != len(types) or any(item not in ENTITY_TYPES for item in types):
            raise ValueError("expected_types 包含不受支持的实体类型")
        return types

    def _run_priority(self, template, query_text: str, entity_types: Iterable[str], match_kind: str, fixed_score: float | None) -> list[EntityCandidate]:
        candidates: list[EntityCandidate] = []
        for node_type in entity_types:
            config = _ENTITY_CONFIG[node_type]
            query, parameters = template(config, query_text)
            rows = self._run(query, parameters)
            for row in rows:
                node_id = self._value(row, "node_id")
                display_name = self._value(row, "display_name") or node_id
                if not node_id:
                    continue
                # Neo4j 全文索引的分词可能会为完全无关的长句返回弱候选。
                # 阶段 2 只接受查询中可验证地出现了候选名称的全文回退，宁可保守
                # 返回未定位，也不把模糊全文命中静默升级成实体直达。
                if match_kind == "fulltext" and not self._query_contains_name(query_text, str(display_name)):
                    continue
                raw_score = self._value(row, "score", 0.0)
                score = fixed_score if fixed_score is not None else self._fulltext_score(raw_score)
                candidates.append(
                    EntityCandidate(
                        node_id=str(node_id),
                        node_type=node_type,
                        display_name=str(display_name),
                        match_kind=match_kind,
                        score=score,
                        ambiguity=False,
                    )
                )
        return self._deduplicate(candidates)

    def _run(self, query: str, parameters: Mapping[str, Any]):
        try:
            session_context = self.driver.session(database=self.database) if self.database else self.driver.session()
        except TypeError:
            session_context = self.driver.session()
        with session_context as session:
            return list(session.run(query, dict(parameters)))

    def _exact_query(self, config: Mapping[str, str], query_text: str) -> tuple[str, dict[str, Any]]:
        label = config["label"]
        return (
            f"""// entity_exact_name_v1
MATCH (node:{label})
WHERE toLower(trim($query_text)) = toLower(trim(coalesce(node.name, '')))
   OR (size(trim(coalesce(node.name, ''))) >= 2
       AND toLower($query_text) CONTAINS toLower(trim(node.name)))
RETURN node.nodeId AS node_id, coalesce(node.name, node.title, node.nodeId) AS display_name
ORDER BY node.nodeId
LIMIT $limit""",
            {"query_text": query_text, "limit": self.max_candidates},
        )

    def _alias_query(self, config: Mapping[str, str], query_text: str) -> tuple[str, dict[str, Any]]:
        label = config["label"]
        return (
            f"""// entity_alias_v1
MATCH (node:{label})
WHERE (size(trim(toString(coalesce(node.preferredTerm, '')))) >= 2
       AND toLower($query_text) CONTAINS toLower(trim(toString(node.preferredTerm))))
   OR (size(trim(toString(coalesce(node.synonyms, '')))) >= 2
       AND toLower($query_text) CONTAINS toLower(trim(toString(node.synonyms))))
RETURN node.nodeId AS node_id, coalesce(node.name, node.title, node.nodeId) AS display_name
ORDER BY node.nodeId
LIMIT $limit""",
            {"query_text": query_text, "limit": self.max_candidates},
        )

    def _fulltext_query(self, config: Mapping[str, str], query_text: str) -> tuple[str, dict[str, Any]]:
        index_name = config["fulltext_index"]
        label = config["label"]
        return (
            f"""// entity_fulltext_v1
CALL db.index.fulltext.queryNodes('{index_name}', $query_text)
YIELD node, score
WHERE node:{label}
RETURN node.nodeId AS node_id, coalesce(node.name, node.title, node.nodeId) AS display_name, score
ORDER BY score DESC, node.nodeId
LIMIT $limit""",
            {"query_text": query_text, "limit": self.max_candidates},
        )

    @staticmethod
    def _value(row: Any, key: str, default: Any = "") -> Any:
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
    def _fulltext_score(raw_score: Any) -> float:
        try:
            raw = float(raw_score)
        except (TypeError, ValueError):
            return 0.0
        if raw <= 0:
            return 0.0
        return min(raw / (raw + 1.0), 1.0)

    @staticmethod
    def _query_contains_name(query_text: str, display_name: str) -> bool:
        normalized_query = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "", query_text).lower()
        normalized_name = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "", display_name).lower()
        return len(normalized_name) >= 2 and normalized_name in normalized_query

    @staticmethod
    def _deduplicate(candidates: Iterable[EntityCandidate]) -> list[EntityCandidate]:
        by_id: dict[str, EntityCandidate] = {}
        for candidate in candidates:
            current = by_id.get(candidate.node_id)
            if current is None or candidate.score > current.score:
                by_id[candidate.node_id] = candidate
        return sorted(by_id.values(), key=lambda item: (-item.score, item.node_id))

    @staticmethod
    def _mark_ambiguity(candidates: list[EntityCandidate]) -> list[EntityCandidate]:
        if not candidates:
            return []
        top_score = candidates[0].score
        ambiguous = sum(abs(candidate.score - top_score) < 1e-9 for candidate in candidates) > 1
        return [replace(candidate, ambiguity=ambiguous) for candidate in candidates]
