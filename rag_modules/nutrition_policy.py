"""阶段 5 的营养声明策略。

当前项目没有可审计的每份营养数值、治理标签或可复算营养链路，因此只
允许少油/清爽偏好推荐。这个模块将该缺口作为版本化策略，而不是由调用方
根据菜谱正文或向量相似度临时猜测。
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .recommendation_evidence import RecommendationEvidence


SOFT_PREFERENCE_POLICY_VERSION = "nutrition_soft_preference_v1"


@dataclass(frozen=True)
class NutritionDecision:
    """一次请求在当前治理策略下的可用证据与边界。"""

    evidence: RecommendationEvidence
    requires_cuisine_scope: bool
    requires_evidence_insufficient: bool


@dataclass(frozen=True)
class NutritionPolicy:
    """冻结的软偏好出口；严格模式必须有独立治理数据才可另行替换。"""

    policy_version: str = SOFT_PREFERENCE_POLICY_VERSION
    governed_nutrition_source_available: bool = False

    @property
    def strict_mode_available(self) -> bool:
        return self.governed_nutrition_source_available

    def assess(self, query: str) -> NutritionDecision | None:
        text = (query or "").strip()
        if not self._is_nutrition_request(text):
            return None
        if self._requires_hard_evidence(text):
            return NutritionDecision(
                evidence=RecommendationEvidence(
                    level="evidence_insufficient",
                    policy_version=self.policy_version,
                    source_status="missing_governed_nutrition_source",
                    missing_reason="当前没有可信营养数值或治理标签，不能验证严格低脂、脂肪克数或医疗饮食条件。",
                    claim_scope="不得给出满足营养约束的候选",
                ),
                requires_cuisine_scope="川菜" in text,
                requires_evidence_insufficient=True,
            )
        return NutritionDecision(
            evidence=RecommendationEvidence(
                level="soft_preference",
                policy_version=self.policy_version,
                source_status="missing_governed_nutrition_source",
                missing_reason="当前资料不能验证严格低脂；仅可作为少油/清爽偏好参考。",
                claim_scope="少油/清爽偏好",
            ),
            requires_cuisine_scope="川菜" in text,
            requires_evidence_insufficient=False,
        )

    @staticmethod
    def _is_nutrition_request(text: str) -> bool:
        return any(
            marker in text
            for marker in (
                "低脂",
                "脂肪",
                "控脂",
                "减脂",
                "低热量",
                "医疗",
                "医嘱",
                "患者",
                "治疗",
                "高血脂",
                "糖尿病",
                "冠心病",
            )
        )

    @staticmethod
    def _requires_hard_evidence(text: str) -> bool:
        strict_markers = (
            "严格",
            "控脂",
            "脂肪克数",
            "脂肪含量",
            "每份",
            "医疗",
            "医嘱",
            "患者",
            "治疗",
            "高血脂",
            "糖尿病",
            "冠心病",
            "低热量",
        )
        if any(marker in text for marker in strict_markers):
            return True
        return bool(re.search(r"(?:脂肪|低脂|减脂).{0,12}(?:\\d+\\s*(?:克|g)|克)", text, re.IGNORECASE))


SOFT_PREFERENCE_POLICY = NutritionPolicy()
