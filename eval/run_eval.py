#!/usr/bin/env python3
"""Run evaluation from user_input JSONL to RAGAS output/result JSONL files."""

import argparse
import json
import math
import os
import re
import sys
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Sequence

import requests


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESS_FILE = "rag_process.md"
RECALL_FILE = "recall_content.md"


if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


@dataclass
class EvalResult:
    id: str
    user_input: str
    reference: Optional[str]
    category: str
    expected_strategy_hint: str
    session_id: str
    response: str
    retrieved_contexts: List[str]
    metadata: Dict
    scores: Dict
    status: str
    error: Optional[str]
    latency_ms: int
    reference_contexts: List[str] = field(default_factory=list)
    expected_answer_keywords: List[str] = field(default_factory=list)
    expected_context_keywords: List[str] = field(default_factory=list)

    def to_json(self) -> Dict:
        return {
            "id": self.id,
            "user_input": self.user_input,
            "reference": self.reference,
            "category": self.category,
            "expected_strategy_hint": self.expected_strategy_hint,
            "session_id": self.session_id,
            "response": self.response,
            "retrieved_contexts": self.retrieved_contexts,
            "reference_contexts": self.reference_contexts,
            "expected_answer_keywords": self.expected_answer_keywords,
            "expected_context_keywords": self.expected_context_keywords,
            "metadata": self.metadata,
            "scores": self.scores,
            "status": self.status,
            "error": self.error,
            "latency_ms": self.latency_ms,
        }


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def load_jsonl(path: Path) -> List[Dict]:
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        row = json.loads(line)
        if "user_input" not in row:
            raise ValueError(f"{path}:{line_no} missing user_input")
        rows.append(row)
    return rows


def project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def write_jsonl(rows: Iterable[EvalResult], path: Path) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row.to_json(), ensure_ascii=False) + "\n")
            count += 1
    return count


def write_score_jsonl(rows: Iterable[EvalResult], path: Path) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            if not row.scores:
                continue
            handle.write(
                json.dumps(
                    {
                        "id": row.id,
                        "user_input": row.user_input,
                        "category": row.category,
                        "expected_strategy_hint": row.expected_strategy_hint,
                        "metadata": row.metadata,
                        "scores": row.scores,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
            count += 1
    return count


def snapshot_audit_dirs(run_dir: Path) -> set:
    if not run_dir.exists():
        return set()
    return {
        path.name
        for path in run_dir.iterdir()
        if path.is_dir() and (path / PROCESS_FILE).exists() and (path / RECALL_FILE).exists()
    }


def find_new_audit_id(run_dir: Path, before: set) -> Optional[str]:
    after = snapshot_audit_dirs(run_dir)
    new_ids = sorted(after - before)
    if new_ids:
        return new_ids[-1]
    if after:
        latest = max((run_dir / audit_id for audit_id in after), key=lambda path: path.stat().st_mtime)
        return latest.name
    return None


def call_chat_api(api_url: str, user_input: str, session_id: str, timeout: int) -> str:
    response = requests.post(
        api_url,
        json={"message": user_input, "session_id": session_id},
        timeout=timeout,
    )
    response.raise_for_status()
    return str(response.json().get("response", ""))


def parse_process_fields(text: str) -> Dict[str, str]:
    fields: Dict[str, str] = {}
    for line in text.splitlines():
        if not line.startswith("- ") or ": " not in line:
            continue
        key, value = line[2:].split(": ", 1)
        fields[key.strip()] = value.strip()
    return fields


def extract_contexts(recall_text: str) -> List[str]:
    marker = "## Final Prompt Context"
    start = recall_text.find(marker)
    section = recall_text[start + len(marker):] if start >= 0 else recall_text
    blocks = re.findall(r"```text\n(.*?)\n```", section, flags=re.DOTALL)
    return [block.strip() for block in blocks if block.strip()]


def _int_field(fields: Dict[str, str], key: str) -> Optional[int]:
    value = fields.get(key)
    if value is None:
        return None
    try:
        return int(value)
    except ValueError:
        return None


def _bool_field(fields: Dict[str, str], key: str) -> Optional[bool]:
    value = fields.get(key)
    if value is None:
        return None
    if value.lower() in {"true", "1", "yes"}:
        return True
    if value.lower() in {"false", "0", "no"}:
        return False
    return None


def read_audit_sample(run_dir: Path, audit_id: Optional[str]) -> Dict:
    if not audit_id:
        return {"retrieved_contexts": [], "metadata": {}}

    audit_dir = run_dir / audit_id
    process_path = audit_dir / PROCESS_FILE
    recall_path = audit_dir / RECALL_FILE
    if not process_path.exists() or not recall_path.exists():
        return {"retrieved_contexts": [], "metadata": {"audit_id": audit_id}}

    fields = parse_process_fields(process_path.read_text(encoding="utf-8"))
    recall_text = recall_path.read_text(encoding="utf-8")
    error_stage = fields.get("stage") if fields.get("status") == "error" else None
    return {
        "user_input": fields.get("original_query", ""),
        "retrieved_contexts": extract_contexts(recall_text),
        "metadata": {
            "audit_id": audit_id,
            "evaluation_sample_id": fields.get("evaluation_sample_id") or audit_id,
            "experiment_id": fields.get("experiment_id"),
            "variant_name": fields.get("variant_name"),
            "config_hash": fields.get("config_hash"),
            "strategy": fields.get("selected_strategy") or fields.get("strategy"),
            "top_k": _int_field(fields, "top_k"),
            "candidate_k": _int_field(fields, "candidate_k"),
            "rerank_model": fields.get("rerank_model") or fields.get("model"),
            "embedding_model": fields.get("embedding_model"),
            "generation_model": fields.get("model_name"),
            "prompt_version": fields.get("prompt_template_version"),
            "routing_duration_ms": _int_field(fields, "duration_ms"),
            "retrieval_duration_ms": _int_field(fields, "hybrid_total_duration_ms")
            or _int_field(fields, "graph_total_duration_ms"),
            "generation_duration_ms": _int_field(fields, "total_duration_ms")
            or _int_field(fields, "duration_ms"),
            "duration_ms": _int_field(fields, "request_duration_ms")
            or _int_field(fields, "hybrid_total_duration_ms")
            or _int_field(fields, "graph_total_duration_ms"),
            "error_stage": error_stage,
            "fallback_used": _bool_field(fields, "fallback_used"),
        },
    }


def run_one_sample(
    sample: Dict,
    api_url: str,
    run_dir: Path,
    timeout: int,
    session_prefix: str,
    requester: Callable[[str, str, str, int], str] = call_chat_api,
) -> EvalResult:
    sample_id = str(sample.get("id") or uuid.uuid4().hex[:8])
    user_input = str(sample["user_input"])
    session_id = f"{session_prefix}-{sample_id}"
    before = snapshot_audit_dirs(run_dir)
    started_at = time.time()

    try:
        response = requester(api_url, user_input, session_id, timeout)
        status = "success"
        error = None
    except Exception as exc:
        response = ""
        status = "error"
        error = f"{type(exc).__name__}: {exc}"

    latency_ms = int((time.time() - started_at) * 1000)
    audit_id = find_new_audit_id(run_dir, before)
    audit_sample = read_audit_sample(run_dir, audit_id)
    metadata = audit_sample.get("metadata", {})
    metadata.update(
        {
            "eval_id": sample_id,
            "category": sample.get("category", ""),
            "expected_strategy_hint": sample.get("expected_strategy_hint", ""),
            "eval_session_id": session_id,
            "eval_status": status,
            "eval_latency_ms": latency_ms,
        }
    )
    return EvalResult(
        id=sample_id,
        user_input=user_input,
        reference=sample.get("reference"),
        category=str(sample.get("category", "")),
        expected_strategy_hint=str(sample.get("expected_strategy_hint", "")),
        session_id=session_id,
        response=response,
        retrieved_contexts=audit_sample.get("retrieved_contexts", []),
        reference_contexts=list(sample.get("reference_contexts") or []),
        expected_answer_keywords=list(sample.get("expected_answer_keywords") or []),
        expected_context_keywords=list(sample.get("expected_context_keywords") or []),
        metadata=metadata,
        scores={},
        status=status,
        error=error,
        latency_ms=latency_ms,
    )


def run_samples(
    input_path: Path,
    api_url: str,
    run_dir: Path,
    output_path: Path,
    timeout: int,
    session_prefix: str,
) -> int:
    results = [
        run_one_sample(
            sample,
            api_url=api_url,
            run_dir=run_dir,
            timeout=timeout,
            session_prefix=session_prefix,
        )
        for sample in load_jsonl(input_path)
    ]
    return write_jsonl(results, output_path)


def build_ragas_dataset(rows: List[EvalResult]):
    try:
        from ragas import EvaluationDataset, SingleTurnSample
    except ImportError as exc:
        raise RuntimeError("ragas is not installed in this Python environment") from exc

    samples = []
    fields = getattr(SingleTurnSample, "model_fields", None) or getattr(SingleTurnSample, "__fields__", {})
    for row in rows:
        sample_kwargs = {
            "user_input": row.user_input,
            "response": row.response,
            "retrieved_contexts": row.retrieved_contexts,
        }
        if row.reference:
            sample_kwargs["reference"] = row.reference
        if row.reference_contexts and "reference_contexts" in fields:
            sample_kwargs["reference_contexts"] = row.reference_contexts
        samples.append(SingleTurnSample(**sample_kwargs))
    return EvaluationDataset(samples=samples)


def _metric_class(module, names: List[str]):
    for name in names:
        cls = getattr(module, name, None)
        if cls is not None:
            return cls
    return None


def select_metrics(include_reference_metrics: bool, metric_names: Optional[List[str]] = None):
    try:
        import ragas.metrics as ragas_metrics
    except ImportError as exc:
        raise RuntimeError("ragas metrics are not available in this Python environment") from exc

    metric_names = metric_names or ["faithfulness", "answer_relevancy"]
    metric_aliases = {
        "response_relevancy": "answer_relevancy",
        "answer_similarity": "semantic_similarity",
    }
    metric_names = [metric_aliases.get(name, name) for name in metric_names]
    metrics = []
    unsupported = []
    factories = {
        "faithfulness": ["Faithfulness"],
        "answer_relevancy": ["ResponseRelevancy", "AnswerRelevancy"],
        "context_precision": ["LLMContextPrecisionWithReference", "ContextPrecision"],
        "context_recall": ["LLMContextRecall", "ContextRecall"],
        "answer_correctness": ["FactualCorrectness", "AnswerCorrectness"],
        "semantic_similarity": ["SemanticSimilarity", "AnswerSimilarity"],
    }
    reference_required = {
        "context_precision",
        "context_recall",
        "answer_correctness",
        "semantic_similarity",
    }
    for metric_name in metric_names:
        if metric_name in reference_required and not include_reference_metrics:
            unsupported.append(f"{metric_name} requires reference")
            continue
        cls = _metric_class(ragas_metrics, factories.get(metric_name, []))
        if cls is None:
            unsupported.append(metric_name)
            continue
        metrics.append(cls())
    if unsupported:
        raise ValueError(f"Unsupported or unavailable RAGAS metrics: {unsupported}")
    return metrics


def _message_role(message) -> str:
    role = getattr(message, "type", None) or getattr(message, "role", None) or "user"
    return {"human": "user", "ai": "assistant", "system": "system", "chat": "user"}.get(role, role)


def _message_content(message) -> str:
    content = getattr(message, "content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict):
                parts.append(str(item.get("text") or item.get("content") or ""))
            else:
                parts.append(str(item))
        return "\n".join(part for part in parts if part)
    return str(content)


def _extract_responses_text(data: Dict) -> str:
    if isinstance(data.get("output_text"), str):
        return data["output_text"]
    parts = []
    for output in data.get("output", []) or []:
        for content in output.get("content", []) or []:
            if isinstance(content, dict) and isinstance(content.get("text"), str):
                parts.append(content["text"])
    if parts:
        return "\n".join(parts)
    choices = data.get("choices") or []
    if choices:
        message = choices[0].get("message") or {}
        if isinstance(message.get("content"), str):
            return message["content"]
    return ""


def _extract_chat_text(data: Dict) -> str:
    choices = data.get("choices") or []
    if not choices:
        return ""
    return (choices[0].get("message") or {}).get("content") or ""


def build_custom_http_judge_llm(
    model: str,
    base_url: str,
    api_key: str,
    endpoint: str,
    timeout: int,
):
    try:
        from langchain_core.callbacks.manager import CallbackManagerForLLMRun
        from langchain_core.language_models.chat_models import BaseChatModel
        from langchain_core.messages import AIMessage
        from langchain_core.outputs import ChatGeneration, ChatResult
    except ImportError as exc:
        raise RuntimeError("langchain-core is required for the custom RAGAS judge client") from exc

    class CustomHTTPJudgeChatModel(BaseChatModel):
        model_name: str
        base_url: str
        api_key: str
        endpoint: str = "responses"
        timeout: int = 180

        @property
        def _llm_type(self) -> str:
            return f"custom-http-{self.endpoint}"

        def _generate(
            self,
            messages: Sequence,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs,
        ) -> ChatResult:
            if self.endpoint == "responses":
                text = self._call_responses(messages, stop=stop, **kwargs)
            elif self.endpoint == "chat":
                text = self._call_chat_completions(messages, stop=stop, **kwargs)
            else:
                raise ValueError(f"Unsupported RAGAS_JUDGE_CLIENT={self.endpoint!r}")
            return ChatResult(generations=[ChatGeneration(message=AIMessage(content=text))])

        def _headers(self) -> Dict[str, str]:
            return {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }

        def _raise_for_error(self, response: requests.Response) -> None:
            if response.status_code < 400:
                return
            try:
                data = response.json()
                error = data.get("error")
                if isinstance(error, dict):
                    message = error.get("message") or response.text
                elif isinstance(error, str):
                    message = error
                else:
                    message = response.text
            except Exception:
                message = response.text
            raise RuntimeError(f"Judge API HTTP {response.status_code}: {message}")

        def _call_responses(self, messages: Sequence, stop: Optional[List[str]] = None, **kwargs) -> str:
            payload = {
                "model": self.model_name,
                "input": [
                    {"role": _message_role(message), "content": _message_content(message)}
                    for message in messages
                ],
            }
            if stop:
                payload["stop"] = stop
            if kwargs.get("temperature") is not None:
                payload["temperature"] = kwargs["temperature"]
            response = requests.post(
                f"{self.base_url.rstrip('/')}/responses",
                headers=self._headers(),
                json=payload,
                timeout=self.timeout,
            )
            self._raise_for_error(response)
            return _extract_responses_text(response.json())

        def _call_chat_completions(self, messages: Sequence, stop: Optional[List[str]] = None, **kwargs) -> str:
            payload = {
                "model": self.model_name,
                "messages": [
                    {"role": _message_role(message), "content": _message_content(message)}
                    for message in messages
                ],
                "temperature": kwargs.get("temperature", 0),
            }
            if stop:
                payload["stop"] = stop
            response = requests.post(
                f"{self.base_url.rstrip('/')}/chat/completions",
                headers=self._headers(),
                json=payload,
                timeout=self.timeout,
            )
            self._raise_for_error(response)
            return _extract_chat_text(response.json())

    return CustomHTTPJudgeChatModel(
        model_name=model,
        base_url=base_url,
        api_key=api_key,
        endpoint=endpoint,
        timeout=timeout,
    )


def build_judge_llm(
    model: str,
    base_url: str = None,
    api_key: str = None,
    client: str = "langchain",
    timeout: int = 180,
):
    if client in {"responses", "chat"}:
        if not base_url or not api_key:
            raise ValueError("RAGAS custom HTTP judge requires base_url and api_key")
        return build_custom_http_judge_llm(model, base_url, api_key, client, timeout)

    try:
        from langchain_openai import ChatOpenAI
    except ImportError as exc:
        raise RuntimeError("langchain-openai is required to run RAGAS LLM metrics") from exc

    kwargs = {"model": model, "temperature": 0, "timeout": timeout}
    if base_url:
        kwargs["base_url"] = base_url
    if api_key:
        kwargs["api_key"] = api_key
    return ChatOpenAI(**kwargs)


def _extract_embedding_vectors(data: Dict) -> List[List[float]]:
    items = data.get("data") or []
    if not isinstance(items, list):
        return []
    ordered = sorted(
        (item for item in items if isinstance(item, dict) and "embedding" in item),
        key=lambda item: item.get("index", 0),
    )
    return [item["embedding"] for item in ordered]


def build_custom_http_embeddings(
    model: str,
    base_url: str,
    api_key: str,
    timeout: int,
):
    try:
        from langchain_core.embeddings import Embeddings
    except ImportError as exc:
        raise RuntimeError("langchain-core is required for the custom RAGAS embeddings client") from exc

    class CustomHTTPEmbeddings(Embeddings):
        def embed_documents(self, texts: List[str]) -> List[List[float]]:
            response = requests.post(
                f"{base_url.rstrip('/')}/embeddings",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json={"model": model, "input": texts},
                timeout=timeout,
            )
            if response.status_code >= 400:
                raise RuntimeError(f"Embedding API HTTP {response.status_code}: {response.text}")
            vectors = _extract_embedding_vectors(response.json())
            if len(vectors) != len(texts):
                raise RuntimeError(f"Embedding API returned {len(vectors)} vectors for {len(texts)} inputs")
            return vectors

        def embed_query(self, text: str) -> List[float]:
            return self.embed_documents([text])[0]

    return CustomHTTPEmbeddings()


def build_judge_embeddings(
    model: str,
    base_url: str = None,
    api_key: str = None,
    timeout: int = 180,
):
    def build_local_embeddings(local_model_path: Path):
        try:
            from langchain_huggingface import HuggingFaceEmbeddings
            return HuggingFaceEmbeddings(model_name=str(local_model_path))
        except ImportError:
            pass

        try:
            from langchain_core.embeddings import Embeddings
            from sentence_transformers import SentenceTransformer
        except ImportError as exc:
            raise RuntimeError(
                "Local RAGAS embeddings require langchain-huggingface, "
                "or langchain-core plus sentence-transformers"
            ) from exc

        class LocalSentenceTransformerEmbeddings(Embeddings):
            def __init__(self, model_path: Path):
                self.model = SentenceTransformer(str(model_path))

            def embed_documents(self, texts: List[str]) -> List[List[float]]:
                return self.model.encode(texts, normalize_embeddings=True).tolist()

            def embed_query(self, text: str) -> List[float]:
                return self.embed_documents([text])[0]

        return LocalSentenceTransformerEmbeddings(local_model_path)

    model_path = project_path(Path(model))
    if model_path.exists():
        return build_local_embeddings(model_path)

    if not base_url:
        local_candidate = PROJECT_ROOT / model
        if local_candidate.exists():
            return build_local_embeddings(local_candidate)

    if not api_key:
        raise ValueError("answer_relevancy requires either a local embedding model path or an embedding api key")

    if base_url:
        return build_custom_http_embeddings(
            model=model,
            base_url=base_url,
            api_key=api_key,
            timeout=timeout,
        )

    try:
        from langchain_openai import OpenAIEmbeddings
    except ImportError as exc:
        raise RuntimeError("langchain-openai is required for default OpenAI embeddings") from exc

    return OpenAIEmbeddings(model=model, api_key=api_key, timeout=timeout)


def build_run_config(max_workers: Optional[int] = None, timeout: Optional[int] = None):
    if not max_workers and not timeout:
        return None
    try:
        from ragas.run_config import RunConfig
    except ImportError:
        return None

    kwargs = {}
    if max_workers:
        kwargs["max_workers"] = max_workers
    if timeout:
        kwargs["timeout"] = timeout
    return RunConfig(**kwargs)


def all_metric_scores_nan(rows: List[EvalResult]) -> bool:
    metric_values = []
    for row in rows:
        for value in row.scores.values():
            if isinstance(value, (int, float)):
                metric_values.append(value)
    return bool(metric_values) and all(math.isnan(value) for value in metric_values)


def canonical_metric_name(name: str) -> str:
    camel_spaced = re.sub(r"(?<!^)(?=[A-Z])", "_", name.strip())
    normalized = camel_spaced.lower()
    normalized = re.sub(r"[^a-z0-9]+", "_", normalized).strip("_")
    aliases = {
        "response_relevancy": "answer_relevancy",
        "answer_relevance": "answer_relevancy",
        "answer_similarity": "semantic_similarity",
        "semantic_similarity": "semantic_similarity",
        "l_l_m_context_precision_with_reference": "context_precision",
        "llm_context_precision_with_reference": "context_precision",
        "context_precision_with_reference": "context_precision",
        "context_precision": "context_precision",
        "l_l_m_context_recall": "context_recall",
        "llm_context_recall": "context_recall",
        "context_recall": "context_recall",
        "factual_correctness": "answer_correctness",
        "factual_correctness_mode_precision": "answer_correctness",
        "factual_correctness_mode_recall": "answer_correctness",
        "factual_correctness_mode_f1": "answer_correctness",
        "answer_correctness": "answer_correctness",
        "faithfulness": "faithfulness",
    }
    return aliases.get(normalized, normalized)


def canonical_metric_names(names: List[str]) -> List[str]:
    return [canonical_metric_name(name) for name in names]


def missing_metric_scores(rows: List[EvalResult], metric_names: List[str]) -> List[str]:
    metric_names = canonical_metric_names(metric_names)
    missing = []
    for row in rows:
        for metric_name in metric_names:
            value = row.scores.get(metric_name)
            if value is None or (isinstance(value, float) and math.isnan(value)):
                missing.append(f"{row.id}:{metric_name}")
    return missing


def assert_metric_scores_complete(rows: List[EvalResult], metric_names: List[str]) -> None:
    missing = missing_metric_scores(rows, metric_names)
    if missing:
        raise RuntimeError(
            "RAGAS metric scores are incomplete or NaN: "
            + ", ".join(missing[:10])
            + (" ..." if len(missing) > 10 else "")
        )


def score_with_ragas(
    rows: List[EvalResult],
    model: str,
    base_url: str = None,
    api_key: str = None,
    client: str = "langchain",
    metric_names: Optional[List[str]] = None,
    limit: Optional[int] = None,
    max_workers: Optional[int] = None,
    timeout: Optional[int] = None,
    fail_on_all_nan: bool = True,
    fail_on_missing_metrics: bool = True,
    embedding_model: str = "bge-small-zh-v1.5",
    embedding_base_url: str = None,
    embedding_api_key: str = None,
) -> int:
    try:
        from ragas import evaluate
    except ImportError as exc:
        raise RuntimeError("ragas is not installed in this Python environment") from exc

    valid_rows = [
        row
        for row in rows
        if row.user_input and row.response and row.retrieved_contexts and row.status == "success"
    ]
    if limit:
        valid_rows = valid_rows[:limit]
    if not valid_rows:
        return 0

    include_reference_metrics = all(row.reference for row in valid_rows)
    metric_names = metric_names or ["faithfulness", "answer_relevancy"]
    metric_names = canonical_metric_names(metric_names)
    dataset = build_ragas_dataset(valid_rows)
    metrics = select_metrics(include_reference_metrics, metric_names=metric_names)
    llm = build_judge_llm(model, base_url=base_url, api_key=api_key, client=client, timeout=timeout or 180)
    run_config = build_run_config(max_workers=max_workers, timeout=timeout)
    evaluate_kwargs = {"dataset": dataset, "metrics": metrics, "llm": llm}
    embedding_metrics = {"answer_relevancy", "semantic_similarity"}
    if embedding_metrics.intersection(metric_names):
        evaluate_kwargs["embeddings"] = build_judge_embeddings(
            model=embedding_model,
            base_url=embedding_base_url,
            api_key=embedding_api_key,
            timeout=timeout or 180,
        )
    if run_config is not None:
        evaluate_kwargs["run_config"] = run_config
    result = evaluate(**evaluate_kwargs)

    try:
        scores = result.to_pandas().to_dict(orient="records")
    except Exception:
        scores = json.loads(result.json())

    for row, score in zip(valid_rows, scores):
        row.scores = {
            canonical_metric_name(key): value
            for key, value in score.items()
            if key not in {
                "user_input",
                "response",
                "retrieved_contexts",
                "reference",
                "reference_contexts",
            }
        }
    if fail_on_all_nan:
        if all_metric_scores_nan(valid_rows):
            raise RuntimeError("RAGAS wrote rows, but every metric score is NaN. Check the judge LLM/API config.")
    missing = missing_metric_scores(valid_rows, metric_names or [])
    if missing:
        for row in valid_rows:
            row.metadata["ragas_missing_metrics"] = missing_metric_scores([row], metric_names or [])
        if fail_on_missing_metrics:
            raise RuntimeError(
                "RAGAS metric scores are incomplete or NaN: "
                + ", ".join(missing[:10])
                + (" ..." if len(missing) > 10 else "")
            )
    return len(valid_rows)


def main() -> int:
    load_dotenv(PROJECT_ROOT / ".env")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("eval/user_input/eval_dataset.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("eval/ragas_data_output/eval_results.jsonl"))
    parser.add_argument("--score-output", type=Path, default=Path("eval/result/ragas_scores.jsonl"))
    parser.add_argument("--api-url", default=os.getenv("RAGAS_EVAL_API_URL", "http://localhost:8000/api/chat"))
    parser.add_argument("--run-dir", type=Path, default=Path(os.getenv("RAGAS_EVAL_RUN_DIR", "run")))
    parser.add_argument("--timeout", type=int, default=int(os.getenv("RAGAS_EVAL_TIMEOUT", "180")))
    parser.add_argument("--session-prefix", default=f"eval-{uuid.uuid4().hex[:8]}")
    parser.add_argument("--skip-ragas", action="store_true", help="Only run the app and write responses/context.")
    parser.add_argument("--model", default=os.getenv("RAGAS_JUDGE_MODEL") or os.getenv("LLM_MODEL") or "gpt-4o-mini")
    parser.add_argument("--base-url", default=os.getenv("RAGAS_OPENAI_BASE_URL") or os.getenv("OPENAI_BASE_URL"))
    parser.add_argument("--api-key", default=os.getenv("RAGAS_OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY"))
    parser.add_argument("--client", choices=["langchain", "responses", "chat"], default=os.getenv("RAGAS_JUDGE_CLIENT", "langchain"))
    parser.add_argument("--metrics", default=os.getenv("RAGAS_METRICS", "faithfulness,answer_relevancy"))
    parser.add_argument("--embedding-model", default=os.getenv("RAGAS_EMBEDDING_MODEL", "bge-small-zh-v1.5"))
    parser.add_argument("--embedding-base-url", default=os.getenv("RAGAS_EMBEDDING_BASE_URL"))
    parser.add_argument("--embedding-api-key", default=os.getenv("RAGAS_EMBEDDING_API_KEY") or os.getenv("RAGAS_OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY"))
    parser.add_argument("--limit", type=int, default=int(os.getenv("RAGAS_EVAL_LIMIT", "0")) or None)
    parser.add_argument("--max-workers", type=int, default=int(os.getenv("RAGAS_MAX_WORKERS", "1")))
    parser.add_argument("--judge-timeout", type=int, default=int(os.getenv("RAGAS_JUDGE_TIMEOUT", "180")))
    parser.add_argument("--allow-all-nan", action="store_true")
    parser.add_argument("--allow-missing-metrics", action="store_true")
    args = parser.parse_args()
    input_path = project_path(args.input)
    output_path = project_path(args.output)
    score_output_path = project_path(args.score_output)
    run_dir = project_path(args.run_dir)

    rows = [
        run_one_sample(
            sample,
            api_url=args.api_url,
            run_dir=run_dir,
            timeout=args.timeout,
            session_prefix=args.session_prefix,
        )
        for sample in load_jsonl(input_path)
    ]
    score_error = None
    if not args.skip_ragas:
        try:
            score_with_ragas(
                rows,
                model=args.model,
                base_url=args.base_url,
                api_key=args.api_key,
                client=args.client,
                metric_names=[name.strip() for name in args.metrics.split(",") if name.strip()],
                limit=args.limit,
                max_workers=args.max_workers,
                timeout=args.judge_timeout,
                fail_on_all_nan=not args.allow_all_nan,
                fail_on_missing_metrics=not args.allow_missing_metrics,
                embedding_model=args.embedding_model,
                embedding_base_url=args.embedding_base_url,
                embedding_api_key=args.embedding_api_key,
            )
        except Exception as exc:
            score_error = exc
        score_count = write_score_jsonl(rows, score_output_path)
        print(f"wrote {score_count} score rows to {score_output_path}")
    count = write_jsonl(rows, output_path)
    print(f"wrote {count} RAGAS data rows to {output_path}")
    if score_error is not None:
        raise score_error
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
