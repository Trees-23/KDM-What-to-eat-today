"""
RAG audit utilities.

This module owns the audit run directory, the two Markdown audit files, and
best-effort append APIs used by the RAG pipeline. Audit failures are always
downgraded to warnings so the user-facing QA path can continue.
"""

import hashlib
import logging
import os
import re
import secrets
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, Optional
from urllib.parse import urlparse

logger = logging.getLogger(__name__)


PROCESS_FILE = "rag_process.md"
RECALL_FILE = "recall_content.md"

_SENSITIVE_KEY_PATTERN = re.compile(
    r"(api[_-]?key|authorization|bearer|token|secret|password)", re.IGNORECASE
)
_PROCESS_CONTENT_KEY_PATTERN = re.compile(
    r"(^|_)(content|context|prompt|answer|response|document|documents|page_content|full_text)($|_)",
    re.IGNORECASE,
)
_BEARER_PATTERN = re.compile(r"Bearer\s+[A-Za-z0-9._~+/=-]+", re.IGNORECASE)
_OPENAI_KEY_PATTERN = re.compile(r"\bsk-[A-Za-z0-9_-]{8,}\b")


def _project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _iso_now() -> str:
    return datetime.now().isoformat(timespec="milliseconds")


def _duration_ms(start: datetime, end: Optional[datetime] = None) -> int:
    end = end or datetime.now()
    return max(0, int((end - start).total_seconds() * 1000))


def _hash_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def sanitize_value(value: Any) -> Any:
    """Return a serializable value safe for process audit output."""
    if value is None or isinstance(value, (int, float, bool)):
        return value
    if isinstance(value, dict):
        return {
            sanitize_key(str(k)): "[REDACTED]" if _SENSITIVE_KEY_PATTERN.search(str(k)) else sanitize_value(v)
            for k, v in value.items()
        }
    if isinstance(value, (list, tuple, set)):
        return [sanitize_value(item) for item in value]

    text = str(value)
    text = _BEARER_PATTERN.sub("[REDACTED_AUTH]", text)
    text = _OPENAI_KEY_PATTERN.sub("sk-[REDACTED]", text)
    return text


def sanitize_content_text(value: Any) -> str:
    """Sanitize text that is intentionally written to recall_content.md."""
    return str(sanitize_value(value))


def summarize_process_value(key: str, value: Any) -> Any:
    """Prevent long retrieved/generated body text from entering rag_process.md."""
    safe_value = sanitize_value(value)
    key_text = str(key)
    if key_text.endswith(("_chars", "_hash", "_length", "_count", "_version", "_name")):
        return safe_value
    if _PROCESS_CONTENT_KEY_PATTERN.search(key_text):
        text = "" if safe_value is None else str(safe_value)
        return f"[BODY_REDACTED chars={len(text)} sha256_16={_hash_text(text)}]"
    return safe_value


def sanitize_key(key: str) -> str:
    if _SENSITIVE_KEY_PATTERN.search(key):
        return "redacted_field"
    return key


def safe_base_url_host(base_url: str) -> str:
    """Expose only the host part of an API base URL."""
    try:
        parsed = urlparse(base_url)
        return parsed.netloc or parsed.path
    except Exception:
        return "[invalid-url]"


def format_process_fields(fields: Dict[str, Any]) -> str:
    lines = []
    for key, value in fields.items():
        safe_value = summarize_process_value(str(key), value)
        safe_key = sanitize_key(str(key))
        if isinstance(safe_value, (dict, list)):
            safe_value = repr(safe_value)
        lines.append(f"- {safe_key}: {safe_value}")
    return "\n".join(lines)


@dataclass
class AuditEvent:
    stage: str
    status: str = "started"
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration_ms: Optional[int] = None

    def to_fields(self) -> Dict[str, Any]:
        start = self.start_time or datetime.now()
        end = self.end_time
        fields: Dict[str, Any] = {
            "stage": self.stage,
            "status": self.status,
            "start": start.isoformat(timespec="milliseconds"),
        }
        if end is not None:
            fields["end"] = end.isoformat(timespec="milliseconds")
        if self.duration_ms is not None:
            fields["duration_ms"] = self.duration_ms
        elif end is not None:
            fields["duration_ms"] = _duration_ms(start, end)
        return fields


class NullAuditRun:
    """Disabled audit object with the same public API as RAGAuditRun."""

    enabled = False
    audit_id = ""
    run_dir = None

    def append_process(self, *_args, **_kwargs) -> None:
        return

    def append_recall(self, *_args, **_kwargs) -> None:
        return

    def record_event(self, *_args, **_kwargs) -> None:
        return

    def record_error(self, *_args, **_kwargs) -> None:
        return

    def write_documents(self, *_args, **_kwargs) -> None:
        return

    def finish_request(self, *_args, **_kwargs) -> None:
        return


NULL_AUDIT_RUN = NullAuditRun()


class RAGAuditRun:
    """Best-effort per-query audit run."""

    enabled = True

    def __init__(
        self,
        root_dir: Path,
        max_content_chars: int = 4000,
        audit_id: Optional[str] = None,
        created_at: Optional[datetime] = None,
    ):
        self.created_at = created_at or datetime.now()
        self.short_id = secrets.token_hex(4)
        timestamp = self.created_at.strftime("%Y%m%d_%H%M%S_%f")[:-3]
        self.audit_id = audit_id or f"{timestamp}_{self.short_id}"
        self.root_dir = root_dir
        self.run_dir = root_dir / self.audit_id
        self.max_content_chars = max(0, int(max_content_chars))
        self.process_path = self.run_dir / PROCESS_FILE
        self.recall_path = self.run_dir / RECALL_FILE
        self._request_start: Optional[datetime] = None
        self._available = False
        self._initialize_files()

    def _initialize_files(self) -> None:
        try:
            self.run_dir.mkdir(parents=True, exist_ok=False)
            self.process_path.write_text(
                "\n".join(
                    [
                        "# RAG Process",
                        "",
                        f"audit_id: {self.audit_id}",
                        f"timestamp: {_iso_now()}",
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            self.recall_path.write_text(
                "\n".join(
                    [
                        "# Recall Content",
                        "",
                        f"audit_id: {self.audit_id}",
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            self._available = True
        except Exception as exc:
            logger.warning("RAG audit initialization failed: %s", exc)
            self._available = False

    def _append(self, path: Path, text: str) -> None:
        if not self._available:
            return
        try:
            with path.open("a", encoding="utf-8") as handle:
                handle.write(text)
                if not text.endswith("\n"):
                    handle.write("\n")
        except Exception as exc:
            logger.warning("RAG audit append failed for %s: %s", path, exc)

    def append_process(self, heading: str, fields: Optional[Dict[str, Any]] = None) -> None:
        body = f"## {heading}\n"
        if fields:
            body += format_process_fields(fields)
            body += "\n"
        body += "\n"
        self._append(self.process_path, body)

    def append_recall(self, heading: str, body: str) -> None:
        self._append(self.recall_path, f"## {heading}\n{body.rstrip()}\n\n")

    def record_event(
        self,
        stage: str,
        status: str = "completed",
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        **fields: Any,
    ) -> None:
        event = AuditEvent(
            stage=stage,
            status=status,
            start_time=start_time,
            end_time=end_time or datetime.now(),
        ).to_fields()
        event.update(fields)
        self.append_process(f"Event / {stage}", event)

    def record_error(self, stage: str, error: BaseException, **fields: Any) -> None:
        payload = {
            "stage": stage,
            "status": "error",
            "error_type": type(error).__name__,
            "error_message": str(error),
        }
        payload.update(fields)
        self.append_process("Errors", payload)

    def mark_request_start(self) -> datetime:
        self._request_start = datetime.now()
        return self._request_start

    def finish_request(self, success: bool = True, **fields: Any) -> None:
        end_time = datetime.now()
        payload = {
            "request_end": end_time.isoformat(timespec="milliseconds"),
            "request_duration_ms": _duration_ms(self._request_start or self.created_at, end_time),
            "success": success,
        }
        payload.update(fields)
        self.append_process("Request Complete", payload)

    def truncate_content(self, content: Any) -> str:
        text = sanitize_content_text("" if content is None else content)
        if len(text) <= self.max_content_chars:
            return text
        digest = _hash_text(text)
        return (
            text[: self.max_content_chars]
            + f"\n\n[TRUNCATED original_chars={len(text)} sha256_16={digest}]"
        )

    def write_documents(
        self,
        heading: str,
        documents: Iterable[Any],
        source: str,
        content_getter: Optional[Any] = None,
    ) -> None:
        parts = []
        for index, doc in enumerate(documents):
            content = content_getter(doc) if content_getter else getattr(doc, "page_content", "")
            metadata = getattr(doc, "metadata", {}) or {}
            metadata_summary = _summarize_metadata(metadata)
            parts.extend(
                [
                    f"### result_order={index}",
                    f"source: {source}",
                    f"metadata_summary: {metadata_summary}",
                    "",
                    "```text",
                    self.truncate_content(content),
                    "```",
                    "",
                ]
            )
        if not parts:
            parts.append("_no content_")
        self.append_recall(heading, "\n".join(parts))


class RAGAuditManager:
    """Factory for per-request audit runs."""

    def __init__(self, enabled: bool = True, root_dir: Optional[Path] = None, max_content_chars: int = 4000):
        self.enabled = enabled
        self.root_dir = Path(root_dir) if root_dir else _project_root() / "run"
        self.max_content_chars = int(max_content_chars)

    @classmethod
    def from_config(cls, config: Any) -> "RAGAuditManager":
        return cls(
            enabled=bool(getattr(config, "enable_rag_audit", False)),
            root_dir=Path(getattr(config, "rag_audit_root_dir", _project_root() / "run")),
            max_content_chars=int(getattr(config, "rag_audit_max_content_chars", 4000)),
        )

    def create_run(self) -> RAGAuditRun:
        if not self.enabled:
            return NULL_AUDIT_RUN
        try:
            return RAGAuditRun(
                root_dir=self.root_dir,
                max_content_chars=self.max_content_chars,
            )
        except Exception as exc:
            logger.warning("RAG audit run creation failed: %s", exc)
            return NULL_AUDIT_RUN


def _summarize_metadata(metadata: Dict[str, Any]) -> str:
    safe_metadata = sanitize_value(metadata)
    if not safe_metadata:
        return "none"
    preferred_keys = [
        "node_id",
        "chunk_id",
        "recipe_name",
        "category",
        "score",
        "retrieval_level",
        "search_type",
        "search_source",
        "route_strategy",
    ]
    parts = []
    for key in preferred_keys:
        if key in safe_metadata:
            parts.append(f"{key}={safe_metadata[key]}")
    if not parts:
        for key, value in list(safe_metadata.items())[:8]:
            if isinstance(value, (dict, list)):
                value = f"{type(value).__name__}[{len(value)}]"
            parts.append(f"{key}={value}")
    return ", ".join(parts)


def query_hash(query: str) -> str:
    return _hash_text(query or "")
