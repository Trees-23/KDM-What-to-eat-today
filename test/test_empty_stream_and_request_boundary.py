from __future__ import annotations

import tempfile
import sys
import types
from dataclasses import dataclass
from pathlib import Path

from rag_modules.generation_integration import GenerationIntegrationModule
from rag_modules.rag_audit import RAGAuditManager
from rag_modules.retrieval_contracts import EvidenceBundle
from rag_modules.web_service_handler import WebServiceHandler


class _FakeRequest:
    def __init__(self, payload): self.payload = payload
    def get_json(self): return self.payload


def install_fake_flask(payload):
    flask = types.ModuleType("flask")
    flask.request = _FakeRequest(payload)
    flask.jsonify = lambda value: value
    flask.Response = lambda iterable, mimetype=None: types.SimpleNamespace(iterable=iterable, mimetype=mimetype, headers={})
    flask.send_from_directory = lambda *_args, **_kwargs: None
    sys.modules["flask"] = flask


@dataclass
class _Config:
    top_k: int = 2
    enable_rag_audit: bool = True
    rag_audit_root_dir: str = ""
    rag_audit_max_content_chars: int = 1000
    retrieval_intent_planner_enabled: bool = True


class _Cache:
    def __init__(self): self.session_contexts = {}; self.added_cache = []; self.added_contexts = []; self.cache_checks = []; self.context_reads = []
    def check_semantic_cache(self, *args): self.cache_checks.append(args); return None
    def get_context_for_query(self, session, query): self.context_reads.append((session, query)); return "history " + query
    def add_to_semantic_cache(self, *args): self.added_cache.append(args)
    def add_to_context(self, *args): self.added_contexts.append(args)


class _Generation:
    def __init__(self): self.calls = []
    def generate_adaptive_answer(self, *args, **kwargs): self.calls.append(args); return "generated"
    def generate_adaptive_answer_stream(self, *args, **kwargs): self.calls.append(args); yield "generated"


class _TerminalSystem:
    def __init__(self, root, action="ENTITY_NOT_FOUND"):
        self.config = _Config(rag_audit_root_dir=str(root)); self.cache_manager = _Cache(); self.generation_module = _Generation(); self.retrieval_calls = []
        self.action = action
    def retrieve_for_generation(self, query, top_k, audit_run=None, **_kwargs):
        self.retrieval_calls.append((query, top_k))
        return EvidenceBundle(None, (), (), (), (self.action, "INTENT_NON_EXECUTE")), None


class _EmptyStreamModule(GenerationIntegrationModule):
    def __init__(self):
        self.model_name = "test"; self.temperature = 0; self.max_tokens = 10
        self.base_url = "https://example.invalid"
        self.client = type("Client", (), {"chat": type("Chat", (), {"completions": type("C", (), {"create": staticmethod(lambda **_: iter(()))})()})()})()
    def generate_adaptive_answer(self, *_args, **_kwargs): return ""


def test_empty_stream_is_a_failure_not_a_successful_empty_answer():
    with tempfile.TemporaryDirectory() as tmp:
        audit = RAGAuditManager(enabled=True, root_dir=Path(tmp)).create_run()
        chunks = list(_EmptyStreamModule().generate_adaptive_answer_stream("问题", [] , max_retries=1, audit_run=audit))
        assert chunks and "网络错误" in chunks[-1]
        text = (audit.run_dir / "rag_process.md").read_text(encoding="utf-8")
        assert "GENERATION_EMPTY_STREAM" in text
        assert "- success: True" not in text


def test_planner_terminal_uses_original_user_message_and_skips_generation_cache_context():
    with tempfile.TemporaryDirectory() as tmp:
        install_fake_flask({"message": "清淡晚餐", "evaluation_constraints": "不要断言低脂", "session_id": "s1"})
        system = _TerminalSystem(Path(tmp))
        response = WebServiceHandler(system)._handle_chat_request()
        assert "ENTITY_NOT_FOUND" in response["response"]
        assert system.retrieval_calls[0][0] == "清淡晚餐"
        assert system.generation_module.calls == []
        assert system.cache_manager.added_cache == []
        assert system.cache_manager.added_contexts == []
        assert system.cache_manager.cache_checks == []
        assert system.cache_manager.context_reads == []


def test_every_non_execute_compile_action_skips_stream_generation_cache_and_session_writes():
    for action in ("PLANNER_LOW_CONFIDENCE", "CLARIFY_OR_OUT_OF_SCOPE", "NUTRITION_EVIDENCE_INSUFFICIENT", "GRAPH_UNAVAILABLE"):
        with tempfile.TemporaryDirectory() as tmp:
            install_fake_flask({"message": "测试请求", "session_id": "s1"})
            system = _TerminalSystem(Path(tmp), action=action)
            response = WebServiceHandler(system)._handle_stream_request()
            chunks = list(response.iterable)

            assert any(action in chunk for chunk in chunks)
            assert system.retrieval_calls == [("测试请求", 2)]
            assert system.generation_module.calls == []
            assert system.cache_manager.cache_checks == []
            assert system.cache_manager.context_reads == []
            assert system.cache_manager.added_cache == []
            assert system.cache_manager.added_contexts == []
