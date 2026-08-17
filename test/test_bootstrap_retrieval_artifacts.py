from argparse import Namespace
from pathlib import Path
from types import SimpleNamespace

from scripts import bootstrap_retrieval_artifacts as bootstrap


def _args(tmp_path: Path) -> Namespace:
    return Namespace(
        neo4j_uri="bolt://neo4j",
        neo4j_user="neo4j",
        neo4j_password="secret",
        neo4j_database="neo4j",
        milvus_uri="http://milvus",
        milvus_database="default",
        output_dir=tmp_path,
        embedding_model="test-model",
        dimension=512,
    )


def test_bootstrap_creates_and_publishes_new_artifact(tmp_path, monkeypatch):
    build_id = "pds_123456789012345678901234"
    writes = []

    class Materializer:
        def __init__(self, **_kwargs):
            pass

        def materialize_from_neo4j(self):
            return SimpleNamespace(
                manifest=SimpleNamespace(build_id=build_id),
                write=lambda path, **kwargs: writes.append((path, kwargs)),
            )

        def close(self):
            pass

    class Store:
        def __enter__(self):
            return self

        def __exit__(self, *_args):
            pass

        def iter_chunks(self, _build_id):
            return [SimpleNamespace(text="菜谱正文")]

    class Stores:
        @staticmethod
        def open(*_args, **_kwargs):
            return Store()

        @staticmethod
        def publish_existing_build(*_args, **_kwargs):
            raise AssertionError("新 build 不应复用现有 PDS")

    class Client:
        def has_collection(self, **_kwargs):
            return False

    class Builder:
        def __init__(self, _client, **kwargs):
            self.collection = kwargs["collection"]

        def build(self, vectors, *, confirm_create):
            assert vectors == [[0.1] * 512]
            assert confirm_create
            return {"chunk_count": 1, "schema_hash": "schema-hash"}

    monkeypatch.setattr(bootstrap, "ParentDocumentMaterializer", Materializer)
    monkeypatch.setattr(bootstrap, "ParentDocumentStore", Stores)
    monkeypatch.setattr(bootstrap, "create_milvus_client", lambda *_args: Client())
    monkeypatch.setattr(bootstrap, "MilvusV2IndexBuilder", Builder)
    monkeypatch.setattr(bootstrap, "_embed", lambda _texts, _model: [[0.1] * 512])
    monkeypatch.setattr(bootstrap, "pds_manifest_sha256", lambda *_args: "pds-hash")

    result = bootstrap.bootstrap(_args(tmp_path))

    assert writes
    assert result["pds"] == "created"
    assert result["milvus"] == "created"
    assert result["collection"] == "cooking_knowledge_v2_pds_12345678"
    assert (tmp_path / "retrieval_artifact_manifest.json").is_file()


def test_bootstrap_reuses_existing_collection_without_embedding(tmp_path, monkeypatch):
    build_id = "pds_abcdef012345678901234567"
    store_path = tmp_path / f"parent_store.{build_id}.sqlite"
    store_path.touch()
    reused = []

    class Materializer:
        def __init__(self, **_kwargs):
            pass

        def materialize_from_neo4j(self):
            return SimpleNamespace(manifest=SimpleNamespace(build_id=build_id))

        def close(self):
            pass

    class Store:
        def __enter__(self):
            return self

        def __exit__(self, *_args):
            pass

    class Stores:
        @staticmethod
        def open(*_args, **_kwargs):
            return Store()

        @staticmethod
        def publish_existing_build(*args):
            reused.append(args)

    class Client:
        def has_collection(self, **_kwargs):
            return True

    class Builder:
        def __init__(self, _client, **_kwargs):
            pass

        def verify_existing(self):
            return {"chunk_count": 3, "schema_hash": "schema-hash"}

    monkeypatch.setattr(bootstrap, "ParentDocumentMaterializer", Materializer)
    monkeypatch.setattr(bootstrap, "ParentDocumentStore", Stores)
    monkeypatch.setattr(bootstrap, "create_milvus_client", lambda *_args: Client())
    monkeypatch.setattr(bootstrap, "MilvusV2IndexBuilder", Builder)
    monkeypatch.setattr(bootstrap, "_embed", lambda *_args: (_ for _ in ()).throw(AssertionError("不应重新向量化")))
    monkeypatch.setattr(bootstrap, "pds_manifest_sha256", lambda *_args: "pds-hash")

    result = bootstrap.bootstrap(_args(tmp_path))

    assert reused
    assert result["pds"] == "reused"
    assert result["milvus"] == "reused"
