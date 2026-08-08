import sys
import tempfile
import types
import unittest
from dataclasses import dataclass
from pathlib import Path

from rag_modules.web_service_handler import WebServiceHandler
from rag_modules.retrieval_contracts import EvidenceBundle


class FakeRequest:
    def __init__(self, payload):
        self.payload = payload

    def get_json(self):
        return self.payload


class FakeResponse:
    def __init__(self, iterable, mimetype=None):
        self.iterable = iterable
        self.mimetype = mimetype
        self.headers = {}


def install_fake_flask(payload):
    fake_flask = types.ModuleType("flask")
    fake_flask.request = FakeRequest(payload)
    fake_flask.jsonify = lambda value: value
    fake_flask.Response = FakeResponse
    fake_flask.send_from_directory = lambda *_args, **_kwargs: None
    sys.modules["flask"] = fake_flask


@dataclass
class Config:
    top_k: int = 2
    enable_rag_audit: bool = True
    rag_audit_root_dir: str = ""
    rag_audit_max_content_chars: int = 4000


class FakeCacheManager:
    def __init__(self, cached_response=None, enhanced_query=None):
        self.cached_response = cached_response
        self.enhanced_query = enhanced_query
        self.session_contexts = {"s1": [{"query": "old", "response": "old answer"}]}
        self.added_contexts = []
        self.added_cache = []

    def check_semantic_cache(self, query, session_id):
        return self.cached_response

    def get_context_for_query(self, session_id, query):
        return self.enhanced_query or query

    def add_to_context(self, session_id, query, response):
        self.added_contexts.append((session_id, query, response))

    def add_to_semantic_cache(self, query, response, session_id):
        self.added_cache.append((query, response, session_id))


class FakeQueryRouter:
    def __init__(self):
        self.calls = []

    def route_query(self, query, top_k, audit_run=None):
        self.calls.append((query, top_k))
        return [], object()


class FakeGenerationModule:
    def __init__(self):
        self.calls = []

    def generate_adaptive_answer(self, query, documents, audit_run=None):
        self.calls.append((query, documents))
        return "generated answer"

    def generate_adaptive_answer_stream(self, query, documents, audit_run=None):
        self.calls.append((query, documents))
        yield "gen"
        yield " stream"


class FakeRAGSystem:
    def __init__(self, audit_root, cached_response=None, enhanced_query=None):
        self.config = Config(rag_audit_root_dir=str(audit_root))
        self.cache_manager = FakeCacheManager(cached_response=cached_response, enhanced_query=enhanced_query)
        self.query_router = FakeQueryRouter()
        self.generation_module = FakeGenerationModule()


class FakeEntityDirectRAGSystem(FakeRAGSystem):
    def __init__(self, audit_root):
        super().__init__(audit_root)
        self.retrieval_calls = []

    def retrieve_for_generation(self, query, top_k, audit_run=None, *, allow_generalized_advice=False):
        self.retrieval_calls.append((query, top_k, audit_run, allow_generalized_advice))
        return EvidenceBundle(
            query_plan=None,
            entity_candidates=(),
            graph_facts=(),
            text_evidence=(),
            limitations=("ENTITY_NOT_FOUND",),
        ), None


class WebAuditA3Test(unittest.TestCase):
    def latest_process_text(self, root):
        dirs = sorted(Path(root).iterdir())
        self.assertTrue(dirs)
        return (dirs[-1] / "rag_process.md").read_text(encoding="utf-8")

    def latest_recall_text(self, root):
        dirs = sorted(Path(root).iterdir())
        self.assertTrue(dirs)
        return (dirs[-1] / "recall_content.md").read_text(encoding="utf-8")

    def test_non_stream_request_records_request_cache_context_and_finish(self):
        with tempfile.TemporaryDirectory() as tmp:
            install_fake_flask({"message": "推荐低脂菜", "session_id": "s1"})
            rag_system = FakeRAGSystem(Path(tmp), enhanced_query="当前问题: 推荐低脂菜")
            handler = WebServiceHandler(rag_system)

            response = handler._handle_chat_request()

            self.assertEqual(response["response"], "generated answer")
            self.assertEqual(response["query"], "推荐低脂菜")
            self.assertEqual(rag_system.query_router.calls, [("当前问题: 推荐低脂菜", 2)])

            process_text = self.latest_process_text(tmp)
            self.assertIn("- original_query: 推荐低脂菜", process_text)
            self.assertIn("- session_id: s1", process_text)
            self.assertIn("- request_mode: non_stream", process_text)
            self.assertIn("- stage: cache_check", process_text)
            self.assertIn("- cache_hit: False", process_text)
            self.assertIn("- stage: context_enhancement", process_text)
            self.assertIn("- final_source: generation", process_text)

    def test_cache_hit_records_final_source_and_skips_retrieval(self):
        with tempfile.TemporaryDirectory() as tmp:
            install_fake_flask({"message": "宫保鸡丁怎么做", "session_id": "s1"})
            rag_system = FakeRAGSystem(Path(tmp), cached_response="cached answer")
            handler = WebServiceHandler(rag_system)

            response = handler._handle_chat_request()

            self.assertTrue(response["from_cache"])
            self.assertEqual(response["response"], "cached answer")
            self.assertEqual(rag_system.query_router.calls, [])
            self.assertEqual(rag_system.generation_module.calls, [])

            process_text = self.latest_process_text(tmp)
            recall_text = self.latest_recall_text(tmp)
            self.assertIn("- cache_hit: True", process_text)
            self.assertIn("- final_source: cache", process_text)
            self.assertIn("- response_chars: 13", process_text)
            self.assertNotIn("cached answer", process_text)
            self.assertNotIn("cached answer", recall_text)

    def test_stream_request_preserves_sse_shape_and_records_stream_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            install_fake_flask({"message": "鸡肉搭配什么", "session_id": "s1"})
            rag_system = FakeRAGSystem(Path(tmp), enhanced_query="当前问题: 鸡肉搭配什么")
            handler = WebServiceHandler(rag_system)

            response = handler._handle_stream_request()
            chunks = list(response.iterable)

            self.assertEqual(response.mimetype, "text/event-stream")
            self.assertIn('data: {"chunk": "gen"}\n\n', chunks)
            self.assertIn("data: [DONE]\n\n", chunks)
            self.assertEqual(rag_system.query_router.calls, [("当前问题: 鸡肉搭配什么", 2)])

            process_text = self.latest_process_text(tmp)
            self.assertIn("- request_mode: stream", process_text)
            self.assertIn("- cache_hit: False", process_text)
            self.assertIn("- final_source: generation", process_text)

    def test_web_paths_pass_only_explicit_generalized_advice_authorization(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit_root = Path(tmp)
            install_fake_flask(
                {
                    "message": "有蓝莓红烧肉这道菜吗？",
                    "session_id": "s1",
                    "allow_generalized_advice": True,
                }
            )
            non_stream_system = FakeEntityDirectRAGSystem(audit_root)
            response = WebServiceHandler(non_stream_system)._handle_chat_request()

            self.assertEqual(response["response"], "generated answer")
            self.assertTrue(non_stream_system.retrieval_calls[0][3])

            install_fake_flask(
                {
                    "message": "有蓝莓红烧肉这道菜吗？",
                    "session_id": "s1",
                    "allow_generalized_advice": "true",
                }
            )
            stream_system = FakeEntityDirectRAGSystem(audit_root)
            response = WebServiceHandler(stream_system)._handle_stream_request()
            list(response.iterable)

            self.assertFalse(stream_system.retrieval_calls[0][3])


if __name__ == "__main__":
    unittest.main()
