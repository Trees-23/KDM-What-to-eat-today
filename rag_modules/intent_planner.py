"""受限 LLM 意图理解器：只输出 IntentCandidate，不拥有任何执行权。"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass
from typing import Any

from .intent_candidate import INTENT_CANDIDATE_VERSION, IntentCandidate, IntentCandidateValidationError


PLANNER_VERSION = "v1"
PLANNER_MIN_CONFIDENCE = 0.70


@dataclass(frozen=True)
class PlannerResult:
    status: str
    candidate: IntentCandidate | None = None
    reason: str | None = None
    latency_ms: int = 0
    response_hash: str | None = None
    response_format: str | None = None

    @property
    def executable(self) -> bool:
        return self.status == "VALID" and self.candidate is not None


class IntentPlanner:
    """将可信 user_message 归为有限需求单，绝不创建 QueryPlan。"""

    def __init__(
        self,
        client: Any,
        *,
        model: str,
        timeout_seconds: float = 8.0,
        min_confidence: float = PLANNER_MIN_CONFIDENCE,
    ) -> None:
        if client is None:
            raise ValueError("IntentPlanner 需要已初始化的 LLM client")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("planner model 不能为空")
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds 必须为正数")
        if not 0 <= min_confidence <= 1:
            raise ValueError("min_confidence 必须在 0 到 1 之间")
        self.client = client
        self.model = model.strip()
        self.timeout_seconds = timeout_seconds
        self.min_confidence = min_confidence

    def plan(self, user_message: str, *, audit_run: Any = None) -> PlannerResult:
        if not isinstance(user_message, str) or not user_message.strip():
            return self._record(PlannerResult("PLANNER_INVALID_OUTPUT", reason="EMPTY_USER_MESSAGE"), audit_run)
        started_at = time.monotonic()
        try:
            response, response_format = self._request_candidate(user_message, "json_schema")
            raw = self._response_content(response)
        except Exception as error:
            if self._is_unsupported_json_schema_error(error):
                try:
                    # 兼容只支持 JSON object 的 OpenAI 兼容端点；本地仍执行同一份严格 schema 校验。
                    response, response_format = self._request_candidate(user_message, "json_object")
                    raw = self._response_content(response)
                except Exception as fallback_error:
                    return self._record(
                        PlannerResult(
                            "PLANNER_UNAVAILABLE",
                            reason=type(fallback_error).__name__,
                            latency_ms=self._latency_ms(started_at),
                            response_format="json_object",
                        ),
                        audit_run,
                    )
            else:
                return self._record(
                    PlannerResult(
                        "PLANNER_UNAVAILABLE",
                        reason=type(error).__name__,
                        latency_ms=self._latency_ms(started_at),
                        response_format="json_schema",
                    ),
                    audit_run,
                )
        if not raw or not raw.strip():
            return self._record(
                PlannerResult(
                    "PLANNER_INVALID_OUTPUT",
                    reason="EMPTY_RESPONSE",
                    latency_ms=self._latency_ms(started_at),
                    response_format=response_format,
                ),
                audit_run,
            )
        response_hash = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        try:
            decoded = json.loads(raw)
            candidate = IntentCandidate.parse_untrusted(decoded)
        except (json.JSONDecodeError, IntentCandidateValidationError, ValueError, TypeError) as error:
            return self._record(
                PlannerResult(
                    "PLANNER_INVALID_OUTPUT",
                    reason=type(error).__name__,
                    latency_ms=self._latency_ms(started_at),
                    response_hash=response_hash,
                    response_format=response_format,
                ),
                audit_run,
            )
        if candidate.confidence < self.min_confidence:
            return self._record(
                PlannerResult(
                    "PLANNER_LOW_CONFIDENCE",
                    candidate=candidate,
                    reason="LOW_CONFIDENCE",
                    latency_ms=self._latency_ms(started_at),
                    response_hash=response_hash,
                    response_format=response_format,
                ),
                audit_run,
            )
        return self._record(
            PlannerResult(
                "VALID",
                candidate=candidate,
                latency_ms=self._latency_ms(started_at),
                response_hash=response_hash,
                response_format=response_format,
            ),
            audit_run,
        )

    @staticmethod
    def _response_content(response: Any) -> str:
        choices = getattr(response, "choices", None)
        if not choices:
            return ""
        message = getattr(choices[0], "message", None)
        content = getattr(message, "content", None)
        return content if isinstance(content, str) else ""

    def _request_candidate(self, user_message: str, response_format_type: str) -> tuple[Any, str]:
        if response_format_type == "json_schema":
            response_format: dict[str, object] = {
                "type": "json_schema",
                "json_schema": {
                    "name": "intent_candidate_v1",
                    "strict": True,
                    "schema": IntentCandidate.json_schema(),
                },
            }
        elif response_format_type == "json_object":
            response_format = {"type": "json_object"}
        else:
            raise ValueError("不支持的 planner 响应格式")
        return (
            self.client.chat.completions.create(
                model=self.model,
                temperature=0,
                max_tokens=700,
                timeout=self.timeout_seconds,
                response_format=response_format,
                messages=[
                    {"role": "system", "content": self._system_prompt()},
                    {"role": "user", "content": user_message.strip()},
                ],
            ),
            response_format_type,
        )

    @staticmethod
    def _is_unsupported_json_schema_error(error: Exception) -> bool:
        message = str(error).casefold()
        return "json_schema" in message and any(
            marker in message for marker in ("unsupported", "not support", "invalid", "not allowed")
        )

    @staticmethod
    def _latency_ms(started_at: float) -> int:
        return max(0, round((time.monotonic() - started_at) * 1000))

    def _record(self, result: PlannerResult, audit_run: Any) -> PlannerResult:
        if audit_run is not None and hasattr(audit_run, "record_event"):
            candidate = result.candidate
            audit_run.record_event(
                "intent_planner",
                status=result.status,
                planner_version=PLANNER_VERSION,
                planner_model=self.model,
                candidate_version=INTENT_CANDIDATE_VERSION,
                candidate_intent=candidate.intent if candidate else None,
                confidence=candidate.confidence if candidate else None,
                normalized_slots=candidate.slots.model_dump(mode="json") if candidate else None,
                latency_ms=result.latency_ms,
                response_hash=result.response_hash,
                response_format=result.response_format,
                reason=result.reason,
            )
        return result

    @staticmethod
    def _system_prompt() -> str:
        return """你是受限的意图理解器。只返回符合给定 JSON Schema 的对象。
你只能描述用户本轮需求，不能输出任何数据库或检索执行信息。
禁止输出：任何 ID、Cypher、SQL、查询、过滤器、collection、template、范围、排序、候选数、证据等级或营养结论。
少油、清淡、不腻只可映射为软偏好 LOW_OIL_FEEL/LIGHT_FEEL，绝不是低脂或医疗结论。
严格脂肪、热量阈值或医疗饮食请求必须是 STRICT_NUTRITION。多个互不从属任务、未知枚举或无法表达的组合使用 CLARIFY_OR_OUT_OF_SCOPE。"""
