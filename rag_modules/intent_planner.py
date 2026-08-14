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
    attempt_count: int = 0
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
        timeout_seconds: float = 20.0,
        max_attempts: int = 3,
        min_confidence: float = PLANNER_MIN_CONFIDENCE,
    ) -> None:
        if client is None:
            raise ValueError("IntentPlanner 需要已初始化的 LLM client")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("planner model 不能为空")
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds 必须为正数")
        if not isinstance(max_attempts, int) or not 1 <= max_attempts <= 3:
            raise ValueError("max_attempts 必须在 1 到 3 之间")
        if not 0 <= min_confidence <= 1:
            raise ValueError("min_confidence 必须在 0 到 1 之间")
        self.client = client
        self.model = model.strip()
        self.timeout_seconds = timeout_seconds
        self.max_attempts = max_attempts
        self.min_confidence = min_confidence

    def plan(self, user_message: str, *, audit_run: Any = None) -> PlannerResult:
        if not isinstance(user_message, str) or not user_message.strip():
            return self._record(PlannerResult("PLANNER_INVALID_OUTPUT", reason="EMPTY_USER_MESSAGE"), audit_run)
        started_at = time.monotonic()
        attempt_count = 0
        try:
            response, response_format, attempt_count = self._request_with_retries(user_message, "json_schema")
            raw = self._response_content(response)
        except Exception as error:
            if self._is_unsupported_json_schema_error(error):
                try:
                    # 兼容只支持 JSON object 的 OpenAI 兼容端点；本地仍执行同一份严格 schema 校验。
                    response, response_format, attempt_count = self._request_with_retries(user_message, "json_object")
                    raw = self._response_content(response)
                except Exception as fallback_error:
                    return self._record(
                        PlannerResult(
                            "PLANNER_UNAVAILABLE",
                            reason=type(fallback_error).__name__,
                            latency_ms=self._latency_ms(started_at),
                            attempt_count=attempt_count or self.max_attempts,
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
                        attempt_count=attempt_count or self.max_attempts,
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
                    attempt_count=attempt_count,
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
                    attempt_count=attempt_count,
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
                    attempt_count=attempt_count,
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
                attempt_count=attempt_count,
                response_hash=response_hash,
                response_format=response_format,
            ),
            audit_run,
        )

    def _request_with_retries(self, user_message: str, response_format_type: str) -> tuple[Any, str, int]:
        """只重试瞬时 planner 请求失败，绝不改变候选单或执行权限。"""
        last_error: Exception | None = None
        for attempt in range(1, self.max_attempts + 1):
            try:
                response, response_format = self._request_candidate(user_message, response_format_type)
                return response, response_format, attempt
            except Exception as error:
                if self._is_unsupported_json_schema_error(error):
                    raise
                last_error = error
        assert last_error is not None
        raise last_error

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
                attempt_count=result.attempt_count,
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
严格脂肪、热量阈值或医疗饮食请求必须是 STRICT_NUTRITION。
只要用户是在推荐、寻找、比较“适合/贴近/可考虑”的菜，而没有给出必须精确定位的具体菜名、食材名或章节标题，就使用 PREFERENCE_RECOMMEND；场景、口味、器具、菜系、做法、人数和泛类食材只是偏好。工具仅可填 MICROWAVE、RICE_COOKER；做法仅可填 STEAM、BOIL、FRY、STEW、STIR_FRY，其中“炒、煸炒、爆炒”均为 STIR_FRY。你只负责标出用户提到了什么，绝不能判断“必须、不要、只用”等条件的强弱；该判断由本地程序根据原话完成。不要把“鱼、海鲜、肉菜、蔬菜、豆制品、面食、素菜”等泛类当成必须解析的稳定实体。
用户明确要学习或只依据某个技巧章节时，使用 TECHNIQUE_SECTION，并只把章节标题原文放入 entity_mentions。用户询问 A 与 B 的搭配或关系时，使用 INGREDIENT_VEGETABLE_PAIRS，并保留 A、B 两个用户原话提及，不能遗漏其中任一项。
例如“我想学使用某种器具，它的关键要点是什么”中的“使用某种器具”是唯一的章节标题；“只根据‘某技巧’章节回答”中的引号内容是唯一的章节标题。不要把“我想学”“关键要点”“只根据”等问句外壳放入 entity_mentions。
例如“某食材能做哪些菜”是 INGREDIENT_RECIPES，entity_mentions 只包含该食材；“只给出图中能验证的某食材与蔬菜搭配”是 INGREDIENT_VEGETABLE_PAIRS，entity_mentions 只包含该食材。没有已验证路径的要求不改变意图类型。
“服务不可用、故障注入、没有路径时不要猜测、资料没有说明时保留”等是系统或评测约束，不是用户意图；只根据其中的实际烹饪问题分类。多个互不从属任务、未知枚举或无法表达的组合使用 CLARIFY_OR_OUT_OF_SCOPE。"""
