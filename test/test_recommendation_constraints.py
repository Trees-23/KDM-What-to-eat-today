from rag_modules.intent_candidate import IntentCandidate
from rag_modules.recommendation_constraints import RecommendationConstraintCompiler


def candidate(*, tools=(), methods=(), preferences=(), servings=None, flavor_ingredients=()):
    return IntentCandidate(
        intent="PREFERENCE_RECOMMEND", confidence=.9,
        slots={"step_number": None, "cuisines": [], "ingredients": [], "flavor_ingredients": list(flavor_ingredients), "preferences": list(preferences),
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


def test_adjacent_do_not_want_phrase_is_a_hard_exclusion_only_for_its_object():
    compiler = RecommendationConstraintCompiler()
    spec = compiler.compile("不想吃油炸，蒸菜也行", candidate(methods=("FRY", "STEAM")))

    assert spec.hard_filters.excluded_methods == ("FRY",)
    assert spec.soft_preferences.methods == ("STEAM",)


def test_local_method_vocabulary_prevents_model_slot_omission_from_bypassing_exclusion():
    spec = RecommendationConstraintCompiler().compile("不想吃油炸，推荐别的川味做法", candidate())

    assert spec.hard_filters.excluded_methods == ("FRY",)
    assert {item["value"] for item in spec.decisions if item["field"] == "method"} == {"FRY"}


def test_flavor_semantics_extracts_generic_suffixes_and_governed_compounds_as_soft_candidates():
    compiler = RecommendationConstraintCompiler()

    tomato = compiler.analyze_flavor("想做带番茄风味的菜", candidate())
    garlic = compiler.analyze_flavor("想吃蒜香味", candidate())
    spicy = compiler.analyze_flavor("麻辣口味", candidate(flavor_ingredients=("花椒",)))
    spec = compiler.compile("想做带番茄风味的菜", candidate(), flavor_terms=tomato.terms)

    assert tomato.terms == ("番茄风味",)
    assert tomato.component_candidates == ("番茄",)
    assert garlic.component_candidates == ("大蒜",)
    assert spicy.component_candidates == ("花椒", "辣椒")
    assert spec.hard_filters.verified_ingredient_ids == ()
    assert spec.soft_preferences.flavor_terms == ("番茄风味",)


def test_time_is_local_hard_constraint_and_other_slots_remain_soft():
    spec = RecommendationConstraintCompiler().compile(
        "30 分钟内做两个人吃的简单晚餐", candidate(preferences=("FEW_STEPS",), servings=2)
    )
    assert spec.hard_filters.max_total_minutes == 30
    assert spec.soft_preferences.target_servings == 2
    assert spec.soft_preferences.prefer_shorter_time
