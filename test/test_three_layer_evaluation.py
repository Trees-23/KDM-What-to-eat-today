import sys
from pathlib import Path

import pytest

TOOL_DIR = Path(__file__).resolve().parents[1] / "_other/考试/检索重构真实场景考试包/工具/three_layer_evaluation"
sys.path.insert(0, str(TOOL_DIR))

from common import ranking_not_applicable, ranking_scores, score_total, weights_for


def test_ranking_scores_match_hand_calculation():
    values = ranking_scores(["a", "b", "c"], {"a": 3, "c": 1, "d": 2}, 3)
    assert values["recall"] == pytest.approx(2 / 3, abs=1e-6)
    assert values["precision"] == pytest.approx(2 / 3, abs=1e-6)
    assert values["hit_rate"] == 1.0
    assert values["mrr"] == 1.0
    assert 0 < values["ndcg"] <= 1


def test_safety_and_s05c_ranking_are_not_applicable():
    assert ranking_not_applicable("S05-C-01", "S05")
    assert ranking_not_applicable("S08-A-01", "S08")
    assert not ranking_not_applicable("S06-A-01", "S06")


def test_quality_weight_formula_and_scenario_weights():
    weights = weights_for("S06-A-01", "S06")
    scores = {"task_score": 5, "preference_score": 5, "evidence_expression_score": 5, "boundary_expression_score": None, "readability_score": 5}
    assert score_total(scores, weights) == 100
    refusal = weights_for("S08-A-01", "S08")
    assert refusal["boundary_expression_score"] == 45
    assert refusal["evidence_expression_score"] is None
