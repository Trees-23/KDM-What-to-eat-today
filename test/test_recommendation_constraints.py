from rag_modules.intent_candidate import IntentCandidate
from rag_modules.recommendation_constraints import RecommendationConstraintCompiler


def candidate(*, tools=(), methods=(), preferences=(), servings=None):
    return IntentCandidate(
        intent="PREFERENCE_RECOMMEND", confidence=.9,
        slots={"step_number": None, "cuisines": [], "ingredients": [], "preferences": list(preferences),
               "meal_context": [], "tools": list(tools), "methods": list(methods), "servings": servings,
               "time_budget_minutes": None, "nutrition_constraint": None},
    )


def test_local_words_not_model_slots_decide_tool_strength():
    compiler = RecommendationConstraintCompiler()
    only = compiler.compile("我家里只有微波炉，只能用微波炉做什么菜？", candidate(tools=("MICROWAVE",)))
    assert only.hard_filters.required_cooking_appliances == ("MICROWAVE",)
    assert only.hard_filters.exclusive_cooking_appliances == ("MICROWAVE",)
    soft = compiler.compile("优先推荐能用微波炉做的早餐", candidate(tools=("MICROWAVE",)))
    assert not soft.hard_filters.required_cooking_appliances
    assert soft.soft_preferences.tools == ("MICROWAVE",)
    excluded = compiler.compile("不能用微波炉完成的晚餐", candidate(tools=("MICROWAVE",)))
    assert excluded.hard_filters.excluded_cooking_appliances == ("MICROWAVE",)


def test_methods_support_stir_fry_and_conflicts_are_clarified():
    compiler = RecommendationConstraintCompiler()
    stir = compiler.compile("我必须吃爆炒的菜", candidate(methods=("STIR_FRY",)))
    assert stir.hard_filters.methods == ("STIR_FRY",)
    exclusive = compiler.compile("我只要蒸菜，不要油炸也不要炒", candidate(methods=("STEAM", "FRY", "STIR_FRY")))
    assert exclusive.hard_filters.methods == ("STEAM",)
    assert {"FRY", "STIR_FRY"} <= set(exclusive.hard_filters.excluded_methods)
    conflict = compiler.compile("我必须蒸制，但又完全不要蒸制", candidate(methods=("STEAM",)))
    assert conflict.clarification_reason == "CONSTRAINT_CONFLICT_METHOD"


def test_time_is_local_hard_constraint_and_other_slots_remain_soft():
    spec = RecommendationConstraintCompiler().compile(
        "30 分钟内做两个人吃的简单晚餐", candidate(preferences=("FEW_STEPS",), servings=2)
    )
    assert spec.hard_filters.max_total_minutes == 30
    assert spec.soft_preferences.target_servings == 2
    assert spec.soft_preferences.prefer_shorter_time
