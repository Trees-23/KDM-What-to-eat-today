"""阶段 5 的推荐证据等级契约。"""

from __future__ import annotations

from dataclasses import dataclass


RECOMMENDATION_EVIDENCE_LEVELS = frozenset(
    {"hard_nutrition", "soft_preference", "evidence_insufficient", "evidence_unavailable"}
)


@dataclass(frozen=True)
class RecommendationEvidence:
    """推荐结论可声明的范围，独立于正文相似度。"""

    level: str
    policy_version: str
    source_status: str
    missing_reason: str
    claim_scope: str

    def __post_init__(self) -> None:
        if self.level not in RECOMMENDATION_EVIDENCE_LEVELS:
            raise ValueError(f"不支持的推荐证据等级: {self.level}")
        for field_name in ("policy_version", "source_status", "missing_reason", "claim_scope"):
            if not str(getattr(self, field_name) or "").strip():
                raise ValueError(f"{field_name} 不能为空")

    def to_dict(self) -> dict[str, str]:
        return {
            "level": self.level,
            "policy_version": self.policy_version,
            "source_status": self.source_status,
            "missing_reason": self.missing_reason,
            "claim_scope": self.claim_scope,
        }

    @classmethod
    def from_dict(cls, value: dict[str, str]) -> "RecommendationEvidence":
        return cls(
            level=value["level"],
            policy_version=value["policy_version"],
            source_status=value["source_status"],
            missing_reason=value["missing_reason"],
            claim_scope=value["claim_scope"],
        )
