from __future__ import annotations

from dataclasses import replace
import json
import sys
import types

import pytest

from rag_modules.milvus_v2_index import (
    ArtifactMismatchError,
    CollectionGuardError,
    MilvusV2Schema,
    V2_FIELDS,
    build_milvus_entities,
    validate_v2_collection_name,
)
from rag_modules.parent_document_materializer import ParentDocumentMaterializer, SourceParent
from rag_modules.parent_document_store import ParentDocumentStore


class _FakeSchema:
    def __init__(self):
        self.fields = []

    def add_field(self, field_name, datatype, **kwargs):
        self.fields.append({"name": field_name, "type": datatype, "params": kwargs, "is_primary": kwargs.get("is_primary", False)})


class _FakeIndexParams:
    def __init__(self):
        self.items = []

    def add_index(self, **kwargs):
        self.items.append(kwargs)


class _FakeMilvusClient:
    def __init__(self):
        self.schema = None
        self.created = []
        self.inserted = []
        self.indexes = []
        self.exists = False

    def has_collection(self, **_kwargs):
        return self.exists

    def create_schema(self, **_kwargs):
        self.schema = _FakeSchema()
        return self.schema

    def create_collection(self, **kwargs):
        self.created.append(kwargs)
        self.exists = True

    def insert(self, **kwargs):
        self.inserted.extend(kwargs["data"])

    def flush(self, **_kwargs):
        return None

    def prepare_index_params(self):
        return _FakeIndexParams()

    def create_index(self, **kwargs):
        self.indexes = kwargs["index_params"].items

    def load_collection(self, **_kwargs):
        return None

    def search(self, **_kwargs):
        return [[{"id": self.inserted[0]["id"]}]]

    def describe_collection(self, _collection):
        type_map = {"VARCHAR": types.SimpleNamespace(name="VARCHAR"), "FLOAT_VECTOR": types.SimpleNamespace(name="FLOAT_VECTOR"), "INT64": types.SimpleNamespace(name="INT64")}
        return {
            "fields": [
                {"name": field["name"], "type": type_map[field["type"]], "params": {key: value for key, value in field["params"].items() if key != "is_primary"}, "is_primary": field["is_primary"]}
                for field in self.schema.fields
            ]
        }

    def get_collection_stats(self, _collection):
        return {"row_count": len(self.inserted)}

    def list_indexes(self, _collection):
        return ["vector_index"]

    def describe_index(self, _collection, _index):
        return {"field_name": "vector", "index_type": "HNSW", "metric_type": "COSINE", "M": "16", "efConstruction": "200"}


def test_builder_uses_schema_add_field_and_never_reuses_collection(tmp_path, monkeypatch):
    store, result = _store(tmp_path)
    fake_module = types.SimpleNamespace(
        DataType=types.SimpleNamespace(VARCHAR="VARCHAR", FLOAT_VECTOR="FLOAT_VECTOR", INT64="INT64")
    )
    monkeypatch.setitem(sys.modules, "pymilvus", fake_module)
    from rag_modules.milvus_v2_index import MilvusV2IndexBuilder

    client = _FakeMilvusClient()
    builder = MilvusV2IndexBuilder(
        client,
        parent_store=store,
        database="default",
        collection=f"cooking_knowledge_v2_{result.manifest.build_id[:12]}",
        build_id=result.manifest.build_id,
    )
    report = builder.build([[0.1] * 512], confirm_create=True)
    assert report["row_count"] == 1
    assert report["sample_search"] == "verified"
    assert len(client.schema.fields) == len(MilvusV2Schema().to_dict()["fields"])
    assert client.indexes[0]["index_type"] == "HNSW"
    store.close()


def _store(tmp_path):
    result = ParentDocumentMaterializer(chunk_size=200, chunk_overlap=10).materialize_documents(
        [SourceParent("recipe-1", "Recipe", "测试", "# 测试\n正文", {"node_id": "recipe-1", "category": "川菜"})]
    )
    path = tmp_path / "pds.sqlite"
    pointer = tmp_path / "active.json"
    result.write(str(path), publish=True, active_pointer=str(pointer))
    return ParentDocumentStore.open(path, active_pointer=pointer), result


def test_schema_is_frozen_and_hash_changes_with_dimension():
    schema = MilvusV2Schema()
    assert schema.to_dict()["version"] == "milvus_v2_schema_v1"
    assert schema.to_dict()["dimension"] == 512
    assert schema.to_dict()["index_type"] == "HNSW"
    assert schema.to_dict()["metric_type"] == "COSINE"
    assert schema.schema_hash != MilvusV2Schema(dimension=768).schema_hash


def test_collection_name_must_bind_to_new_build():
    assert validate_v2_collection_name("cooking_knowledge_v2_pds_build123", "pds_build123") == "cooking_knowledge_v2_pds_build123"
    with pytest.raises(CollectionGuardError):
        validate_v2_collection_name("cooking_knowledge", "pds_build123")


def test_build_entities_preserves_chunk_linkage_and_rejects_mismatch(tmp_path):
    store, result = _store(tmp_path)
    chunk = result.chunks[0]
    entities = build_milvus_entities([chunk], parent_store=store, build_id=result.manifest.build_id, vectors=[[0.1] * 512], dimension=512)
    assert entities[0]["id"] == chunk.chunk_id
    assert entities[0]["parent_id"] == "recipe-1"
    assert entities[0]["text_hash"] == chunk.text_hash
    with pytest.raises(ArtifactMismatchError):
        build_milvus_entities([replace(chunk, build_id="wrong")], parent_store=store, build_id=result.manifest.build_id, vectors=[[0.1] * 512], dimension=512)
    store.close()


def test_build_cli_verify_existing_is_read_only(tmp_path, monkeypatch, capsys):
    store, result = _store(tmp_path)
    fake_module = types.SimpleNamespace(
        DataType=types.SimpleNamespace(VARCHAR="VARCHAR", FLOAT_VECTOR="FLOAT_VECTOR", INT64="INT64")
    )
    monkeypatch.setitem(sys.modules, "pymilvus", fake_module)
    from scripts import build_milvus_v2

    client = _FakeMilvusClient()
    client.exists = True
    client.schema = _FakeSchema()
    for name, type_name, primary in V2_FIELDS:
        if type_name == "FLOAT_VECTOR":
            client.schema.add_field(field_name=name, datatype="FLOAT_VECTOR", dim=512)
        elif type_name.startswith("VARCHAR"):
            client.schema.add_field(field_name=name, datatype="VARCHAR", max_length=int(type_name[8:-1]), is_primary=primary)
        else:
            client.schema.add_field(field_name=name, datatype=type_name)
    client.inserted = build_milvus_entities(
        list(store.iter_chunks(result.manifest.build_id)),
        parent_store=store,
        build_id=result.manifest.build_id,
        vectors=[[0.1] * 512 for _ in result.chunks],
        dimension=512,
    )
    monkeypatch.setattr(build_milvus_v2, "_new_client", lambda _uri, _database: client)
    collection = f"cooking_knowledge_v2_{result.manifest.build_id[:12]}"
    argv = [
        "--database", "default", "--allowed-database", "default", "--uri", "http://milvus",
        "--collection", collection, "--allowed-collection", collection,
        "--parent-store", str(tmp_path / "pds.sqlite"), "--parent-store-build", result.manifest.build_id,
        "--verify-existing",
    ]
    assert build_milvus_v2.main(argv) == 0
    output = json.loads(capsys.readouterr().out)
    assert output["collection"] == collection
    assert not client.created
    store.close()
