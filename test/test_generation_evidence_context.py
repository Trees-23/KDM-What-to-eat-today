from __future__ import annotations

import types

from rag_modules.generation_integration import GenerationIntegrationModule
from rag_modules.recommendation_evidence import RecommendationEvidence
from rag_modules.retrieval_contracts import EvidenceBundle, GraphFact, TextEvidence


class CapturingClient:
    def __init__(self):
        self.calls = []
        self.chat = types.SimpleNamespace(completions=types.SimpleNamespace(create=self.create))

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return types.SimpleNamespace(
            choices=[types.SimpleNamespace(message=types.SimpleNamespace(content="回答"))]
        )


class GenerationModuleForTest(GenerationIntegrationModule):
    def __init__(self):
        self.model_name = "test-model"
        self.temperature = 0.1
        self.max_tokens = 128
        self.base_url = "https://api.example.test/v1"
        self.client = CapturingClient()


def test_generation_uses_physically_separated_evidence_sections_and_hides_unverified_graph_claims():
    bundle = EvidenceBundle(
        query_plan=None,
        entity_candidates=(),
        graph_facts=(
            GraphFact(
                fact_id="step-1",
                template_id="recipe_step_anchor_v1",
                node_ids=("recipe-1", "step-1"),
                edges=({"from": "recipe-1", "relationship": "CONTAINS_STEP", "to": "step-1"},),
                properties={"step_order": 1},
                status="verified",
            ),
            GraphFact(
                fact_id="missing-edge",
                template_id="ingredient_pair_v1",
                node_ids=(),
                edges=(),
                properties={"forbidden_text": "文本不能证明关系"},
                status="not_found",
            ),
        ),
        text_evidence=(
            TextEvidence(
                parent_id="recipe-1",
                build_id="build-test",
                chunk_ids=("recipe-1:chunk:0",),
                anchor_ids=("step-1",),
                text="正文中的腌制步骤",
                origin="parent_store",
            ),
        ),
        limitations=("图谱未找到其他关系。",),
    )
    module = GenerationModuleForTest()

    answer = module.generate_adaptive_answer("第一步怎么做？", bundle)
    prompt = module.client.calls[0]["messages"][0]["content"]

    assert answer == "回答"
    assert "已验证图事实" in prompt
    assert "正文证据" in prompt
    assert "限制与不可证明项" in prompt
    assert "CONTAINS_STEP" in prompt
    assert "正文中的腌制步骤" in prompt
    assert "文本不能证明关系" not in prompt


def test_generation_returns_deterministic_message_for_missing_entity_without_calling_llm():
    bundle = EvidenceBundle(
        query_plan=None,
        entity_candidates=(),
        graph_facts=(),
        text_evidence=(),
        limitations=("ENTITY_NOT_FOUND",),
    )
    module = GenerationModuleForTest()

    answer = module.generate_adaptive_answer("不存在的菜怎么做？", bundle)

    assert "知识库未收录" in answer
    assert module.client.calls == []


def test_generation_does_not_fill_in_step_text_when_only_graph_location_is_available():
    bundle = EvidenceBundle(
        query_plan={"intent": "RECIPE_STEP", "template_id": "recipe_step_anchor_v1"},
        entity_candidates=(),
        graph_facts=(
            GraphFact(
                fact_id="step-1",
                template_id="recipe_step_anchor_v1",
                node_ids=("recipe-1", "step-1"),
                edges=({"from": "recipe-1", "relationship": "CONTAINS_STEP", "to": "step-1"},),
                properties={"step_order": 1},
                status="verified",
            ),
        ),
        text_evidence=(),
        limitations=("PDS_TEXT_UNAVAILABLE",),
    )
    module = GenerationModuleForTest()

    answer = module.generate_adaptive_answer("第一步怎么腌？", bundle)

    assert "父文档正文当前不可用" in answer
    assert module.client.calls == []


def test_generation_relation_not_found_explicitly_states_that_the_relation_cannot_be_proven():
    bundle = EvidenceBundle(
        query_plan=None,
        entity_candidates=(),
        graph_facts=(),
        text_evidence=(),
        limitations=("GRAPH_RELATION_NOT_FOUND",),
    )
    module = GenerationModuleForTest()

    answer = module.generate_adaptive_answer("新鲜玉米和蔬菜能否搭配？", bundle)

    assert "无法证明" in answer
    assert module.client.calls == []


def test_generation_rejects_strict_nutrition_request_without_calling_llm():
    bundle = EvidenceBundle(
        query_plan={"intent": "PREFERENCE_RECOMMEND", "template_id": "preference_recommend_v1"},
        entity_candidates=(),
        graph_facts=(),
        text_evidence=(),
        limitations=("NUTRITION_EVIDENCE_INSUFFICIENT",),
        recommendation_evidence=RecommendationEvidence(
            level="evidence_insufficient",
            policy_version="nutrition_soft_preference_v1",
            source_status="missing_governed_nutrition_source",
            missing_reason="没有可信营养数据。",
            claim_scope="不得给出满足营养约束的候选",
        ),
    )
    module = GenerationModuleForTest()

    answer = module.generate_adaptive_answer("每份脂肪不超过 5 克的川菜", bundle)

    assert "无法验证严格低脂" in answer
    assert module.client.calls == []


def test_generation_prompt_marks_soft_preference_as_non_nutrition_claim():
    bundle = EvidenceBundle(
        query_plan={"intent": "PREFERENCE_RECOMMEND", "template_id": "preference_recommend_v1"},
        entity_candidates=(),
        graph_facts=(),
        text_evidence=(
            TextEvidence(
                parent_id="recipe-1",
                build_id="build-test",
                chunk_ids=("recipe-1:chunk:0",),
                anchor_ids=(),
                text="少油烹饪提示。",
                origin="parent_store",
            ),
        ),
        limitations=("NUTRITION_SOFT_PREFERENCE_ONLY", "当前资料不能验证严格低脂。"),
        recommendation_evidence=RecommendationEvidence(
            level="soft_preference",
            policy_version="nutrition_soft_preference_v1",
            source_status="missing_governed_nutrition_source",
            missing_reason="当前资料不能验证严格低脂。",
            claim_scope="少油/清爽偏好",
        ),
    )
    module = GenerationModuleForTest()

    module.generate_adaptive_answer("推荐低脂川菜", bundle)
    prompt = module.client.calls[0]["messages"][0]["content"]

    assert "推荐证据等级" in prompt
    assert "soft_preference" in prompt
    assert "不能声称已验证低脂" in prompt


def test_generation_replaces_forbidden_claim_with_pds_backed_safe_summary():
    bundle = EvidenceBundle(
        query_plan={"intent": "PREFERENCE_RECOMMEND", "template_id": "preference_recommend_v1"},
        entity_candidates=(),
        graph_facts=(),
        text_evidence=(
            TextEvidence("recipe-1", "build-test", ("recipe-1:chunk:0",), (), "# 清蒸鱼的做法\n正文", "parent_store"),
        ),
        limitations=(),
        claim_policy={"forbidden_claims": ("低脂", "低热量", "低盐", "医疗适用")},
    )
    module = GenerationModuleForTest()
    module.client.create = lambda **kwargs: types.SimpleNamespace(
        choices=[types.SimpleNamespace(message=types.SimpleNamespace(content="这道菜低脂且低盐。"))]
    )
    module.client.chat.completions.create = module.client.create

    answer = module.generate_adaptive_answer("推荐清淡菜", bundle)

    assert "清蒸鱼" in answer
    assert not any(term in answer for term in ("低脂", "低热量", "低盐", "医疗适用"))
