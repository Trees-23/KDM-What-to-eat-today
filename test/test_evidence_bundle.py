from __future__ import annotations

import json

import pytest

from rag_modules.retrieval_contracts import (
    EntityCandidate,
    EvidenceBundle,
    GraphFact,
    TextEvidence,
)


def _bundle() -> EvidenceBundle:
    return EvidenceBundle(
        query_plan=None,
        entity_candidates=(
            EntityCandidate(
                node_id="201002454",
                node_type="Recipe",
                display_name="宫保鸡丁",
                match_kind="exact_name",
                score=1.0,
                ambiguity=False,
            ),
        ),
        graph_facts=(
            GraphFact(
                fact_id="entity:201002454",
                template_id="entity_resolution_v1",
                node_ids=("201002454",),
                edges=(),
                properties={"display_name": "宫保鸡丁"},
                status="verified",
            ),
        ),
        text_evidence=(
            TextEvidence(
                parent_id="201002454",
                build_id="build-test",
                chunk_ids=("201002454:chunk:0",),
                anchor_ids=(),
                text="# 宫保鸡丁\n完整步骤",
                origin="parent_store",
            ),
        ),
        limitations=("仅根据正文证据回答做法。",),
    )


def test_evidence_bundle_round_trips_without_mixing_evidence_columns():
    bundle = _bundle()

    restored = EvidenceBundle.from_dict(json.loads(bundle.to_json()))

    assert restored == bundle
    assert restored.verified_graph_facts[0].template_id == "entity_resolution_v1"
    assert restored.text_evidence[0].origin == "parent_store"


@pytest.mark.parametrize(
    "factory",
    [
        lambda: EntityCandidate("", "Recipe", "菜", "exact_name", 1.0, False),
        lambda: EntityCandidate("id", "Unknown", "菜", "exact_name", 1.0, False),
        lambda: EntityCandidate("id", "Recipe", "菜", "semantic", 1.0, False),
        lambda: GraphFact("fact", "fixed", (), (), {}, "verified"),
        lambda: GraphFact("fact", "fixed", (), (), {}, "invented"),
        lambda: GraphFact("fact", "fixed", ("node",), ({"from": "node"},), {"text": "正文"}, "verified"),
        lambda: GraphFact("fact", "fixed", ("node",), (("from", "node"),), {}, "verified"),
        lambda: TextEvidence("parent", "build", (), (), "正文", "parent_store"),
        lambda: TextEvidence("parent", "build", ("chunk",), (), "正文", "unknown"),
    ],
)
def test_evidence_contract_rejects_illegal_states(factory):
    with pytest.raises(ValueError):
        factory()


def test_unavailable_graph_fact_keeps_explicit_status_without_text_proof():
    bundle = EvidenceBundle(
        query_plan=None,
        entity_candidates=(),
        graph_facts=(
            GraphFact(
                fact_id="recipe-step:201002454",
                template_id="recipe_step_anchor_v1",
                node_ids=(),
                edges=(),
                properties={},
                status="unavailable",
            ),
        ),
        text_evidence=(),
        limitations=("图证据不可用。",),
    )

    assert bundle.verified_graph_facts == ()
    assert bundle.graph_facts[0].status == "unavailable"
