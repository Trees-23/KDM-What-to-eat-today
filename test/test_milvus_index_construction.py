from types import SimpleNamespace

from rag_modules.milvus_index_construction import MilvusIndexConstructionModule


class _Embeddings:
    def embed_documents(self, texts):
        return [[0.1] * 512 for _ in texts]


class _Client:
    def __init__(self, *, reported_rows=None):
        self.inserted = []
        self.flushed = False
        self.loaded = False
        self.reported_rows = reported_rows

    def insert(self, *, collection_name, data):
        self.inserted.extend(data)

    def flush(self, *, collection_name):
        self.flushed = True

    def get_collection_stats(self, collection_name):
        count = len(self.inserted) if self.reported_rows is None else self.reported_rows
        return {"row_count": count}

    def load_collection(self, collection_name):
        self.loaded = True


def _module(client):
    module = object.__new__(MilvusIndexConstructionModule)
    module.client = client
    module.embeddings = _Embeddings()
    module.collection_name = "cooking_knowledge"
    module.create_collection = lambda force_recreate: True
    module.create_index = lambda: client.flushed
    return module


def _chunks():
    return [
        SimpleNamespace(
            page_content="测试文本",
            metadata={"chunk_id": "chunk-1", "difficulty": 0},
        )
    ]


def test_build_vector_index_flushes_before_index_and_loads_collection():
    client = _Client()

    assert _module(client).build_vector_index(_chunks()) is True

    assert client.flushed is True
    assert client.loaded is True
    assert len(client.inserted) == 1


def test_build_vector_index_rejects_unpersisted_row_count():
    client = _Client(reported_rows=0)

    assert _module(client).build_vector_index(_chunks()) is False

    assert client.flushed is True
    assert client.loaded is False
