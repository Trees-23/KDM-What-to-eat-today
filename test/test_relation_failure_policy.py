from __future__ import annotations

from rag_modules.evidence_builder import EvidenceBuilder
from rag_modules.retrieval_contracts import EvidenceBundle, GraphFact


def test_relation_failure_fact_stays_out_of_verified_graph_section_and_is_not_text_proof():
    missing = GraphFact(
        fact_id="ingredient-recipes:missing",
        template_id="ingredient_recipes_v1",
        node_ids=(),
        edges=(),
        properties={"relationship_type": "REQUIRES"},
        status="not_found",
    )
    bundle = EvidenceBuilder.merge_graph_facts(
        EvidenceBundle(None, (), (), (), ("当前图谱未找到该关系。",)),
        (missing,),
    )

    sections = EvidenceBuilder.sections(bundle)

    assert bundle.verified_graph_facts == ()
    assert "无已验证图事实" in sections.verified_graph_facts
    assert "当前图谱未找到该关系" in sections.limitations


def test_graph_service_failure_is_explicitly_unavailable():
    unavailable = GraphFact(
        fact_id="ingredient-pairs:unavailable",
        template_id="ingredient_vegetable_pairs_v1",
        node_ids=(),
        edges=(),
        properties={"relationship_type": "REQUIRES", "error_type": "ServiceUnavailable"},
        status="unavailable",
    )

    assert unavailable.status == "unavailable"
    assert unavailable.node_ids == ()
