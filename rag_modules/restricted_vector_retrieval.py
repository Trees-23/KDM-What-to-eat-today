"""只允许 child chunk 检索并在 parent 级别聚合、回补正文。"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from .milvus_v2_index import ArtifactMismatchError, validate_v2_collection_name
from .parent_document_store import ParentDocumentStore
from .retrieval_contracts import TextEvidence


@dataclass(frozen=True)
class VectorHit:
    chunk_id: str
    parent_id: str
    score: float
    chunk_index: int
    text_hash: str
    build_id: str
    section_title: str


@dataclass(frozen=True)
class ParentAggregate:
    parent_id: str
    score: float
    coverage: int
    chunk_ids: tuple[str, ...]
    text_evidence: TextEvidence


class RestrictedVectorRetriever:
    """Milvus V2 查询适配器；空 parent scope 永远拒绝。"""

    _ID_PATTERN = re.compile(r"^[A-Za-z0-9_.:-]{1,150}$")
    _MAX_FILTER_PARENTS_PER_SEARCH = 20

    def __init__(self, client: Any, *, parent_store: ParentDocumentStore, collection: str, build_id: str, database: str = "default", dimension: int = 512, embedder: Any = None):
        if client is None or parent_store is None:
            raise ValueError("受限向量检索需要 Milvus client 和 PDS")
        validate_v2_collection_name(collection, build_id)
        self.client = client
        self.parent_store = parent_store
        self.collection = collection
        self.build_id = build_id
        self.database = database
        self.dimension = dimension
        self.embedder = embedder
        if self.parent_store.active_build_id != build_id:
            raise ArtifactMismatchError("受限向量检索 build_id 与 PDS active build 不一致")

    def retrieve(
        self,
        query: str,
        *,
        parent_ids: Sequence[str] | None = None,
        expected_parent_type: str | None = None,
        top_k: int = 5,
        query_vector: Sequence[float] | None = None,
    ) -> list[ParentAggregate]:
        if top_k < 1 or top_k > 50:
            raise ValueError("top_k 超出范围")
        if expected_parent_type is not None and expected_parent_type not in {"Recipe", "TechniqueDoc"}:
            raise ValueError("expected_parent_type 不在受限向量检索白名单中")
        if parent_ids is not None:
            parent_ids = tuple(dict.fromkeys(str(item) for item in parent_ids))
            if not parent_ids:
                raise ValueError("parent scope 为空，拒绝退化为全库检索")
            for parent_id in parent_ids:
                if not self._ID_PATTERN.fullmatch(parent_id):
                    raise ValueError("parent_id 不在白名单格式中")
        if query_vector is None:
            if self.embedder is None:
                raise ValueError("未提供 query_vector 或 embedder")
            query_vector = self.embedder.embed_query(query)
        if len(query_vector) != self.dimension:
            raise ValueError("query_vector 维度与 V2 schema 不一致")
        kwargs = {
            "collection_name": self.collection,
            "data": [list(query_vector)],
            "anns_field": "vector",
            "limit": min(50, max(top_k * 4, top_k)),
            "output_fields": ["id", "parent_id", "chunk_index", "build_id", "text_hash", "section_title"],
            "search_params": {"metric_type": "COSINE", "params": {"ef": 64}},
        }
        # Milvus 2.3 HNSW can return an empty result for a valid long ``in``
        # expression. Split only the already verified local parent scope and
        # aggregate it locally; this never expands the scope to the corpus.
        scopes = (
            tuple(
                parent_ids[index:index + self._MAX_FILTER_PARENTS_PER_SEARCH]
                for index in range(0, len(parent_ids), self._MAX_FILTER_PARENTS_PER_SEARCH)
            )
            if parent_ids is not None
            else (None,)
        )
        hits: list[VectorHit] = []
        for scope in scopes:
            request = dict(kwargs)
            filter_expr = self._filter(scope)
            if filter_expr:
                request["filter"] = filter_expr
            hits.extend(self._normalize_hits(self.client.search(**request)))
        report = self.parent_store.validate_chunk_linkage([hit.__dict__ for hit in hits])
        if not report.valid:
            raise ArtifactMismatchError(f"Milvus/PDS linkage 不一致: {report}")
        return self._aggregate(hits, top_k, expected_parent_type=expected_parent_type)

    @classmethod
    def _normalize_hits(cls, result: Any) -> list[VectorHit]:
        rows = result[0] if isinstance(result, (list, tuple)) and result else result
        normalized: list[VectorHit] = []
        for item in rows or []:
            entity = item.get("entity", item) if isinstance(item, Mapping) else item.entity
            get = entity.get if isinstance(entity, Mapping) else lambda key, default=None: entity.get(key, default)
            chunk_id = str(get("chunk_id", item.get("id", "") if isinstance(item, Mapping) else ""))
            parent_id = str(get("parent_id", ""))
            build_id = str(get("build_id", ""))
            text_hash_value = str(get("text_hash", ""))
            score = float(item.get("distance", item.get("score", 0.0)) if isinstance(item, Mapping) else item.distance)
            chunk_index = int(get("chunk_index", 0))
            section_title = str(get("section_title", ""))
            if not chunk_id or not parent_id or not build_id:
                raise ArtifactMismatchError("Milvus hit 缺少 linkage 字段")
            normalized.append(VectorHit(chunk_id, parent_id, score, chunk_index, text_hash_value, build_id, section_title))
        return normalized

    def _aggregate(
        self,
        hits: Sequence[VectorHit],
        top_k: int,
        *,
        expected_parent_type: str | None = None,
    ) -> list[ParentAggregate]:
        grouped: dict[str, list[VectorHit]] = {}
        for hit in hits:
            if hit.build_id != self.build_id:
                raise ArtifactMismatchError("Milvus hit build_id 与 active build 不一致")
            grouped.setdefault(hit.parent_id, []).append(hit)
        ranked = []
        for parent_id, parent_hits in grouped.items():
            unique = {hit.chunk_id: hit for hit in parent_hits}
            ordered = sorted(unique.values(), key=lambda hit: (-hit.score, hit.chunk_index, hit.chunk_id))
            section_coverage = len({hit.section_title or f"chunk:{hit.chunk_index}" for hit in ordered})
            adjacent_pairs = sum(
                1
                for previous, current in zip(
                    sorted(ordered, key=lambda hit: hit.chunk_index),
                    sorted(ordered, key=lambda hit: hit.chunk_index)[1:],
                )
                if current.chunk_index - previous.chunk_index <= 1
            )
            score = ordered[0].score + min(section_coverage, 5) * 0.001 + min(adjacent_pairs, 5) * 0.0001
            parent = self.parent_store.get_full_parent(parent_id)
            if parent is None or parent.build_id != self.build_id:
                raise ArtifactMismatchError(f"无法从 PDS 回补 parent: {parent_id}")
            if expected_parent_type is not None and parent.node_type != expected_parent_type:
                continue
            evidence = TextEvidence(
                parent_id=parent.parent_id,
                build_id=parent.build_id,
                chunk_ids=tuple(hit.chunk_id for hit in sorted(unique.values(), key=lambda hit: hit.chunk_index)),
                anchor_ids=(),
                text=parent.full_content,
                origin="parent_store",
            )
            ranked.append(ParentAggregate(parent_id, score, section_coverage, evidence.chunk_ids, evidence))
        ranked.sort(key=lambda item: (-item.score, -item.coverage, item.parent_id))
        return ranked[:top_k]

    @staticmethod
    def _filter(parent_ids: Sequence[str] | None) -> str:
        if parent_ids is None:
            return ""
        escaped = ["'" + value.replace("\\", "\\\\").replace("'", "\\'") + "'" for value in parent_ids]
        return "parent_id in [" + ", ".join(escaped) + "]"
