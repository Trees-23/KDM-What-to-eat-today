from __future__ import annotations

import importlib

from rag_modules.evidence_builder import EvidenceBuilder
from rag_modules.nutrition_policy import SOFT_PREFERENCE_POLICY
from rag_modules.recommendation_evidence import RecommendationEvidence
from rag_modules.retrieval_contracts import EvidenceBundle


def test_soft_preference_policy_keeps_strict_mode_disabled_and_marks_low_fat_as_unverified_preference():
    decision = SOFT_PREFERENCE_POLICY.assess("推荐低脂川菜")

    assert SOFT_PREFERENCE_POLICY.strict_mode_available is False
    assert decision is not None
    assert decision.evidence.level == "soft_preference"
    assert decision.evidence.policy_version == "nutrition_soft_preference_v1"
    assert "不能验证严格低脂" in decision.evidence.missing_reason
    assert decision.requires_cuisine_scope is True


def test_soft_preference_policy_rejects_threshold_strict_and_medical_requests_without_candidates():
    for query in (
        "推荐严格低脂川菜",
        "推荐每份脂肪不超过 5 克的川菜",
        "高血脂患者能吃什么川菜？",
        "推荐低热量川菜",
    ):
        decision = SOFT_PREFERENCE_POLICY.assess(query)

        assert decision is not None
        assert decision.requires_evidence_insufficient is True
        assert decision.evidence.level == "evidence_insufficient"
        assert "可信营养数值或治理标签" in decision.evidence.missing_reason


def test_soft_preference_policy_does_not_promote_summer_light_meal_to_nutrition_claim():
    assert SOFT_PREFERENCE_POLICY.assess("夏天吃什么清淡的？") is None


def test_config_cannot_enable_strict_nutrition_without_governed_policy(monkeypatch):
    monkeypatch.setenv("RETRIEVAL_STRICT_NUTRITION_ENABLED", "true")
    import config as config_module

    reloaded = importlib.reload(config_module)

    assert reloaded.GraphRAGConfig().retrieval_strict_nutrition_enabled is False


def test_recommendation_evidence_round_trips_and_is_rendered_as_a_separate_section():
    evidence = RecommendationEvidence(
        level="soft_preference",
        policy_version="nutrition_soft_preference_v1",
        source_status="missing_governed_nutrition_source",
        missing_reason="当前资料不能验证严格低脂。",
        claim_scope="少油/清爽偏好",
    )
    bundle = EvidenceBundle(
        query_plan=None,
        entity_candidates=(),
        graph_facts=(),
        text_evidence=(),
        limitations=("NUTRITION_SOFT_PREFERENCE_ONLY",),
        recommendation_evidence=evidence,
    )

    restored = EvidenceBundle.from_json(bundle.to_json())
    context = EvidenceBuilder.context(restored)

    assert restored.recommendation_evidence == evidence
    assert "推荐证据等级" in context
    assert "nutrition_soft_preference_v1" in context
