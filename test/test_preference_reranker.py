from rag_modules.preference_reranker import PreferenceReranker
from rag_modules.recommendation_constraints import ConstraintSpec, SoftRecipePreferences
from rag_modules.restricted_vector_retrieval import CandidateMetadata


def candidate(parent_id, score, **metadata):
    return CandidateMetadata(parent_id, parent_id, score, .001, score + .001, 1, (parent_id + ":0",), metadata)


def test_reranker_applies_fixed_scores_and_stable_tie_breaks():
    spec = ConstraintSpec(
        intent="PREFERENCE_RECOMMEND",
        soft_preferences=SoftRecipePreferences(preferences=("LIGHT_FEEL", "FEW_STEPS"), target_servings=2),
    )
    result = PreferenceReranker().rank([
        candidate("fried", .9, recipe_methods=["FRY"], step_count=8, total_minutes=70, servings_count=2),
        candidate("steam", .8, recipe_methods=["STEAM"], step_count=4, total_minutes=20, servings_count=2),
    ], spec)
    assert result[0].candidate.parent_id == "fried"
    steam = next(item for item in result if item.candidate.parent_id == "steam")
    fried = next(item for item in result if item.candidate.parent_id == "fried")
    assert steam.adjustments["light_feel_match"] == 10
    assert fried.adjustments["light_feel_conflict"] == -20
    assert fried.adjustments["few_steps_long_time"] == -6
    assert steam.audit_dict()["best_chunk_score"] == .8


def test_unknown_soft_metadata_does_not_gain_or_lose_points():
    result = PreferenceReranker().rank(
        [candidate("b", .5), candidate("a", .5)],
        ConstraintSpec(intent="PREFERENCE_RECOMMEND", soft_preferences=SoftRecipePreferences(preferences=("FEW_STEPS",))),
    )
    assert [item.candidate.parent_id for item in result] == ["a", "b"]
    assert all(set(item.adjustments) == {"base_retrieval"} for item in result)
