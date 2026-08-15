"""Milvus V2 schema、白名单和 PDS child chunk 构建辅助。"""

from __future__ import annotations

import hashlib
import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any, Iterable, Mapping, Sequence

from .parent_document_store import CanonicalChunk, ParentDocumentStore, text_hash


V2_SCHEMA_VERSION = "milvus_v2_schema_v1"
V2_COLLECTION_PREFIX = "cooking_knowledge_v2_"
V2_FIELDS = (
    ("id", "VARCHAR(150)", True),
    ("vector", "FLOAT_VECTOR", False),
    ("text", "VARCHAR(15000)", False),
    ("parent_id", "VARCHAR(100)", False),
    ("node_id", "VARCHAR(100)", False),
    ("node_type", "VARCHAR(100)", False),
    ("category", "VARCHAR(100)", False),
    ("cuisine_type", "VARCHAR(200)", False),
    ("doc_type", "VARCHAR(50)", False),
    ("chunk_index", "INT64", False),
    ("total_chunks", "INT64", False),
    ("section_title", "VARCHAR(500)", False),
    ("build_id", "VARCHAR(64)", False),
    ("text_hash", "VARCHAR(64)", False),
)

_VARCHAR_LIMITS = {
    name: int(type_name[8:-1])
    for name, type_name, _primary in V2_FIELDS
    if type_name.startswith("VARCHAR")
}


class ArtifactMismatchError(ValueError):
    """PDS/Milvus 联合工件不一致。"""


class CollectionGuardError(ValueError):
    """集合目标不在显式白名单内。"""


def create_milvus_client(uri: str, database: str) -> Any:
    """以显式 URI/database 创建 V2 客户端，不沿用旧集合的隐式连接。"""

    if not uri or not database or database == "*":
        raise CollectionGuardError("V2 Milvus client 必须绑定显式 URI 与 database")
    try:
        from pymilvus import MilvusClient
    except ImportError as error:
        raise RuntimeError("V2 Milvus client 需要安装 pymilvus") from error
    return MilvusClient(uri=uri, db_name=database)


def validate_v2_collection_name(collection: str, build_id: str) -> str:
    expected = f"{V2_COLLECTION_PREFIX}{build_id[:12]}"
    if collection != expected:
        raise CollectionGuardError(f"V2 collection 必须为 {expected}")
    return collection


def pds_manifest_sha256(parent_store: ParentDocumentStore, build_id: str) -> str:
    """计算 PDS build manifest 的稳定摘要，供联合 artifact 绑定。"""

    manifest = parent_store.get_build_manifest(build_id)
    payload = json.dumps(asdict(manifest), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _type_name(value: Any) -> str:
    """兼容 pymilvus DataType 枚举和测试替身。"""

    name = getattr(value, "name", None)
    if name:
        return str(name)
    text = str(value)
    return text.rsplit(".", 1)[-1]


def _normalized_fields(fields: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    normalized = []
    for field in fields:
        normalized.append(
            {
                "name": str(field.get("name", "")),
                "type": _type_name(field.get("type", "")),
                "primary_key": bool(field.get("is_primary", False)),
                "params": {str(key): str(value) for key, value in dict(field.get("params", {})).items()},
            }
        )
    return normalized


@dataclass(frozen=True)
class MilvusV2Schema:
    dimension: int = 512
    embedding_model: str = "BAAI/bge-small-zh-v1.5"
    index_type: str = "HNSW"
    metric_type: str = "COSINE"
    hnsw_m: int = 16
    ef_construction: int = 200
    ef_search: int = 64

    @property
    def schema_hash(self) -> str:
        payload = {
            "version": V2_SCHEMA_VERSION,
            "fields": V2_FIELDS,
            "dimension": self.dimension,
            "embedding_model": self.embedding_model,
            "index_type": self.index_type,
            "metric_type": self.metric_type,
            "hnsw_m": self.hnsw_m,
            "ef_construction": self.ef_construction,
            "ef_search": self.ef_search,
        }
        return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()

    def to_dict(self) -> dict[str, Any]:
        return {
            "version": V2_SCHEMA_VERSION,
            "fields": [
                {"name": name, "type": type_name, "primary_key": primary}
                for name, type_name, primary in V2_FIELDS
            ],
            "dimension": self.dimension,
            "embedding_model": self.embedding_model,
            "index_type": self.index_type,
            "metric_type": self.metric_type,
            "hnsw": {"M": self.hnsw_m, "efConstruction": self.ef_construction, "ef": self.ef_search},
            "schema_hash": self.schema_hash,
        }

    def validate_description(self, description: Mapping[str, Any]) -> None:
        fields = description.get("fields")
        if not isinstance(fields, Sequence):
            # 兼容仅用于单元测试的简略 description；真实 Milvus 必须返回 fields。
            if description.get("schema_hash") == self.schema_hash and description.get("dimension") == self.dimension:
                return
            raise ArtifactMismatchError("Milvus describe_collection 缺少 schema fields")
        expected = []
        for name, type_name, primary in V2_FIELDS:
            params: dict[str, str] = {}
            if type_name == "FLOAT_VECTOR":
                actual_type = "FLOAT_VECTOR"
                params["dim"] = str(self.dimension)
            elif type_name.startswith("VARCHAR"):
                actual_type = "VARCHAR"
                params["max_length"] = type_name[8:-1]
            else:
                actual_type = type_name
            expected.append({"name": name, "type": actual_type, "primary_key": primary, "params": params})
        if _normalized_fields(fields) != expected:
            raise ArtifactMismatchError("Milvus collection schema 与冻结 V2 schema 不一致")


@dataclass(frozen=True)
class RetrievalArtifactManifest:
    pds_build_id: str
    pds_manifest_sha256: str
    milvus_database: str
    milvus_collection: str
    milvus_schema_hash: str
    milvus_build_id: str
    created_at: str
    rollback_database: str
    rollback_collection: str
    rollback_pds_build: str

    def __post_init__(self) -> None:
        if self.pds_build_id != self.milvus_build_id:
            raise ArtifactMismatchError("PDS 与 Milvus build_id 不一致")
        for field_name in self.__dataclass_fields__:
            if not str(getattr(self, field_name)).strip():
                raise ValueError(f"manifest 字段不能为空: {field_name}")

    def to_dict(self) -> dict[str, str]:
        return dict(self.__dict__)

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "RetrievalArtifactManifest":
        return cls(**{name: value[name] for name in cls.__dataclass_fields__})

    def sha256(self) -> str:
        return hashlib.sha256(json.dumps(self.to_dict(), sort_keys=True, ensure_ascii=False).encode()).hexdigest()

    def write_atomic(self, path: str | os.PathLike[str]) -> Path:
        destination = Path(path).expanduser().resolve()
        destination.parent.mkdir(parents=True, exist_ok=True)
        with NamedTemporaryFile(mode="w", encoding="utf-8", dir=destination.parent, delete=False) as temp:
            json.dump(self.to_dict(), temp, ensure_ascii=False, sort_keys=True, indent=2)
            temp.write("\n")
            temp.flush()
            os.fsync(temp.fileno())
            temporary = Path(temp.name)
        os.replace(temporary, destination)
        return destination

    @classmethod
    def read(cls, path: str | os.PathLike[str]) -> "RetrievalArtifactManifest":
        value = json.loads(Path(path).read_text(encoding="utf-8"))
        if not isinstance(value, Mapping):
            raise ValueError("artifact manifest 必须是对象")
        return cls.from_dict(value)

    def validate_runtime(
        self,
        *,
        pds_build_id: str,
        pds_manifest_sha256: str | None = None,
        milvus_database: str,
        milvus_collection: str,
        schema_hash: str,
    ) -> None:
        expected = {
            "pds_build_id": pds_build_id,
            "milvus_database": milvus_database,
            "milvus_collection": milvus_collection,
            "milvus_schema_hash": schema_hash,
        }
        for name, actual in expected.items():
            if getattr(self, name) != actual:
                raise ArtifactMismatchError(f"artifact manifest 不一致: {name}")
        if pds_manifest_sha256 is not None and self.pds_manifest_sha256 != pds_manifest_sha256:
            raise ArtifactMismatchError("artifact manifest 不一致: pds_manifest_sha256")


def build_milvus_entities(
    chunks: Iterable[CanonicalChunk],
    *,
    parent_store: ParentDocumentStore,
    build_id: str,
    vectors: Sequence[Sequence[float]],
    dimension: int,
) -> list[dict[str, Any]]:
    """从同一 PDS build 生成 V2 行；不截断正文或隐式改写字段。"""
    chunk_rows = list(chunks)
    if len(chunk_rows) != len(vectors):
        raise ValueError("chunk 与 embedding 数量不一致")
    entities: list[dict[str, Any]] = []
    for chunk, vector in zip(chunk_rows, vectors):
        if chunk.build_id != build_id:
            raise ArtifactMismatchError(f"chunk build_id 不一致: {chunk.chunk_id}")
        if len(vector) != dimension:
            raise ValueError(f"向量维度错误: {chunk.chunk_id}")
        parent = parent_store.get_full_parent(chunk.parent_id)
        if parent is None or parent.build_id != build_id:
            raise ArtifactMismatchError(f"chunk parent 不属于指定 PDS build: {chunk.chunk_id}")
        metadata = dict(parent.metadata)
        actual_text_hash = text_hash(chunk.text)
        if chunk.text_hash != actual_text_hash:
            raise ArtifactMismatchError(f"chunk text_hash 不一致: {chunk.chunk_id}")
        entity = {
            "id": chunk.chunk_id,
            "vector": list(vector),
            "text": chunk.text,
            "parent_id": chunk.parent_id,
            "node_id": str(metadata.get("node_id", chunk.parent_id)),
            "node_type": parent.node_type,
            "category": str(metadata.get("category", "")),
            "cuisine_type": str(metadata.get("cuisine_type", "")),
            "doc_type": str(metadata.get("doc_type", parent.node_type)),
            "chunk_index": chunk.chunk_index,
            "total_chunks": chunk.total_chunks,
            "section_title": chunk.section_title,
            "build_id": chunk.build_id,
            "text_hash": actual_text_hash,
        }
        for field_name, limit in _VARCHAR_LIMITS.items():
            if len(str(entity[field_name])) > limit:
                raise ValueError(f"V2 字段超长: {chunk.chunk_id}.{field_name}")
        entities.append(entity)
    return entities


class MilvusV2IndexBuilder:
    """V2 collection 构建器；目标已存在时失败，永不调用 drop_collection。"""

    def __init__(self, client: Any, *, parent_store: ParentDocumentStore, database: str, collection: str, build_id: str, dimension: int = 512, embedding_model: str = "BAAI/bge-small-zh-v1.5"):
        validate_v2_collection_name(collection, build_id)
        self.client = client
        self.parent_store = parent_store
        self.database = database
        self.collection = collection
        self.build_id = build_id
        self.schema = MilvusV2Schema(dimension=dimension, embedding_model=embedding_model)

    def verify_source(self) -> dict[str, Any]:
        chunks = list(self.parent_store.iter_chunks(self.build_id))
        if not chunks:
            raise ValueError("PDS build 没有 CanonicalChunk")
        linkage = self.parent_store.validate_chunk_linkage(
            [
                {"chunk_id": chunk.chunk_id, "parent_id": chunk.parent_id, "build_id": chunk.build_id, "text_hash": chunk.text_hash}
                for chunk in chunks
            ]
        )
        if not linkage.valid:
            raise ArtifactMismatchError(f"PDS linkage 校验失败: {linkage}")
        return {"build_id": self.build_id, "chunk_count": len(chunks), "schema_hash": self.schema.schema_hash}

    def build(self, vectors: Sequence[Sequence[float]], *, confirm_create: bool = False) -> dict[str, Any]:
        if not confirm_create:
            raise PermissionError("创建 V2 collection 需要显式 confirm_create")
        source = self.verify_source()
        if self.client.has_collection(collection_name=self.collection):
            raise CollectionGuardError(f"目标 collection 已存在，拒绝复用: {self.collection}")
        chunks = list(self.parent_store.iter_chunks(self.build_id))
        entities = build_milvus_entities(
            chunks,
            parent_store=self.parent_store,
            build_id=self.build_id,
            vectors=vectors,
            dimension=self.schema.dimension,
        )
        try:
            from pymilvus import DataType
        except ImportError as error:
            raise RuntimeError("创建 V2 collection 需要安装 pymilvus") from error
        schema = self.client.create_schema(auto_id=False, enable_dynamic_field=False)
        for name, type_name, primary in V2_FIELDS:
            if type_name == "FLOAT_VECTOR":
                schema.add_field(field_name=name, datatype=DataType.FLOAT_VECTOR, dim=self.schema.dimension)
            elif type_name.startswith("VARCHAR"):
                schema.add_field(
                    field_name=name,
                    datatype=DataType.VARCHAR,
                    max_length=int(type_name[8:-1]),
                    is_primary=primary,
                )
            elif type_name == "INT64":
                schema.add_field(field_name=name, datatype=DataType.INT64)
        self.client.create_collection(collection_name=self.collection, schema=schema, consistency_level="Strong")
        self.client.insert(collection_name=self.collection, data=entities)
        self.client.flush(collection_name=self.collection)
        index_params = self.client.prepare_index_params()
        index_params.add_index(
            field_name="vector",
            index_type=self.schema.index_type,
            metric_type=self.schema.metric_type,
            params={"M": self.schema.hnsw_m, "efConstruction": self.schema.ef_construction},
        )
        self.client.create_index(
            collection_name=self.collection,
            index_params=index_params,
        )
        self.client.load_collection(collection_name=self.collection)
        return self.verify_existing(
            expected_row_count=len(entities),
            sample_vector=vectors[0],
        )

    def verify_existing(
        self,
        *,
        expected_row_count: int | None = None,
        sample_vector: Sequence[float] | None = None,
    ) -> dict[str, Any]:
        """只读校验新建 V2 collection；用于创建后和失败恢复后审计。"""

        source = self.verify_source()
        if not self.client.has_collection(collection_name=self.collection):
            raise CollectionGuardError(f"V2 collection 不存在: {self.collection}")
        description = self.client.describe_collection(self.collection)
        self.schema.validate_description(description)
        stats = self.client.get_collection_stats(self.collection)
        required_row_count = source["chunk_count"] if expected_row_count is None else expected_row_count
        if int(stats.get("row_count", -1)) != required_row_count:
            raise ArtifactMismatchError("V2 collection 行数与 PDS CanonicalChunk 数不一致")
        indexes = self.client.list_indexes(self.collection)
        if not indexes:
            raise ArtifactMismatchError("V2 collection 未创建向量索引")
        index = self.client.describe_index(self.collection, indexes[0])
        if (
            index.get("field_name") != "vector"
            or index.get("index_type") != self.schema.index_type
            or index.get("metric_type") != self.schema.metric_type
            or str(index.get("M")) != str(self.schema.hnsw_m)
            or str(index.get("efConstruction")) != str(self.schema.ef_construction)
        ):
            raise ArtifactMismatchError("V2 collection 索引与冻结 HNSW/COSINE 参数不一致")
        report = {**source, "collection": self.collection, "row_count": required_row_count}
        if sample_vector is not None:
            if len(sample_vector) != self.schema.dimension:
                raise ValueError("样本向量维度与 V2 schema 不一致")
            expected_chunk = next(self.parent_store.iter_chunks(self.build_id))
            raw_hits = self.client.search(
                collection_name=self.collection,
                data=[list(sample_vector)],
                anns_field="vector",
                limit=1,
                output_fields=["id"],
                search_params={"metric_type": self.schema.metric_type, "params": {"ef": self.schema.ef_search}},
            )
            hits = raw_hits[0] if isinstance(raw_hits, Sequence) and raw_hits else ()
            if not hits:
                raise ArtifactMismatchError("V2 collection 样本向量检索没有返回命中")
            first = hits[0]
            entity = first.get("entity", first) if isinstance(first, Mapping) else getattr(first, "entity", first)
            if isinstance(entity, Mapping):
                actual_chunk_id = str(entity.get("id", first.get("id", "") if isinstance(first, Mapping) else ""))
            else:
                actual_chunk_id = str(getattr(entity, "id", getattr(first, "id", "")))
            if actual_chunk_id != expected_chunk.chunk_id:
                raise ArtifactMismatchError("V2 collection 样本向量检索未返回对应 CanonicalChunk")
            report["sample_search"] = "verified"
        return report
