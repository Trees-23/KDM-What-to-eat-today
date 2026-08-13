"""HTTP/API 请求的可信输入边界。"""

from __future__ import annotations

from dataclasses import dataclass


class RequestBoundaryError(ValueError):
    """调用方没有提供可信用户问题时抛出。"""


@dataclass(frozen=True)
class RetrievalRequest:
    """只允许 user_message 进入 planner 与营养预检。"""

    user_message: str
    evaluation_constraints: str | None = None
    system_instructions: str | None = None
    conversation_context: dict[str, object] | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.user_message, str) or not self.user_message.strip():
            raise RequestBoundaryError("user_message 必须是非空字符串")
        if len(self.user_message) > 4000:
            raise RequestBoundaryError("user_message 超过最大长度")

    @property
    def planner_input(self) -> str:
        return self.user_message.strip()

    @property
    def nutrition_input(self) -> str:
        return self.user_message.strip()
