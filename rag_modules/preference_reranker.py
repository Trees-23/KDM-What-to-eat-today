"""推荐候选的确定性、可审计重排器。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from .recommendation_constraints import ConstraintSpec
from .restricted_vector_retrieval import CandidateMetadata


RERANK_VERSION = "recommendation_rerank_v1"


@dataclass(frozen=True)
class RerankedCandidate:
    candidate: CandidateMetadata
    final_score: float
    adjustments: Mapping[str, float]

    def audit_dict(self) -> dict[str, object]:
        return {
            "parent_id": self.candidate.parent_id,
            "best_chunk_score": self.candidate.best_chunk_score,
            "coverage_bonus": self.candidate.coverage_bonus,
            "retrieval_score": self.candidate.retrieval_score,
            "rerank_adjustments": dict(self.adjustments),
            "final_score": self.final_score,
            "attribute_provenance": self.candidate.metadata.get("attribute_provenance", {}),
            "unknown_cooking_appliance": self.candidate.metadata.get("unknown_cooking_appliance"),
        }


class PreferenceReranker:
    """严格执行 recommendation_rerank_v1 表，不接受模型权重或排序表达式。"""

    version = RERANK_VERSION

    def rank(self, candidates: Sequence[CandidateMetadata], spec: ConstraintSpec) -> list[RerankedCandidate]:
        rows = list(candidates)
        if not rows:
            return []
        scores = [row.retrieval_score for row in rows]
        low, high = min(scores), max(scores)
        ranked: list[RerankedCandidate] = []
        for row in rows:
            normalized = .5 if high == low else (row.retrieval_score - low) / (high - low)
            adjustments: dict[str, float] = {"base_retrieval": 70 * normalized}
            methods = set(row.metadata.get("recipe_methods") or ())
            if "LIGHT_FEEL" in spec.soft_preferences.preferences:
                if "FRY" in methods:
                    adjustments["light_feel_conflict"] = -20
                elif {"STEAM", "BOIL"} & methods:
                    adjustments["light_feel_match"] = 10
            if "FEW_STEPS" in spec.soft_preferences.preferences:
                steps, minutes = row.metadata.get("step_count"), row.metadata.get("total_minutes")
                if isinstance(steps, int) and steps <= 6:
                    adjustments["few_steps"] = 6
                if isinstance(minutes, int) and minutes <= 25:
                    adjustments["few_steps_time"] = 6
                elif isinstance(minutes, int) and minutes > 60:
                    adjustments["few_steps_long_time"] = -6
            servings = row.metadata.get("servings_count")
            target = spec.soft_preferences.target_servings
            if isinstance(target, int) and isinstance(servings, int):
                if servings == target:
                    adjustments["servings_exact"] = 4
                elif abs(servings - target) == 1:
                    adjustments["servings_near"] = 1
            ranked.append(RerankedCandidate(row, sum(adjustments.values()), adjustments))
        return sorted(ranked, key=lambda item: (-item.final_score, -item.candidate.retrieval_score, item.candidate.parent_id))
