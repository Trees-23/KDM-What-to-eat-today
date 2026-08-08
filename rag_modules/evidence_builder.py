"""将阶段 2 证据契约渲染为生成层需要的物理分栏上下文。"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Iterable

from .retrieval_contracts import EvidenceBundle, GraphFact, TextEvidence


@dataclass(frozen=True)
class EvidencePromptSections:
    verified_graph_facts: str
    text_evidence: str
    limitations: str


class EvidenceBuilder:
    """唯一允许把 EvidenceBundle 交给生成提示词的适配器。"""

    @staticmethod
    def sections(bundle: EvidenceBundle) -> EvidencePromptSections:
        return EvidencePromptSections(
            verified_graph_facts=EvidenceBuilder._render_graph_facts(bundle.verified_graph_facts),
            text_evidence=EvidenceBuilder._render_text_evidence(bundle.text_evidence),
            limitations=EvidenceBuilder._render_limitations(bundle.limitations),
        )

    @staticmethod
    def context(bundle: EvidenceBundle) -> str:
        sections = EvidenceBuilder.sections(bundle)
        return "\n\n".join(
            (
                "## 已验证图事实\n" + sections.verified_graph_facts,
                "## 正文证据\n" + sections.text_evidence,
                "## 限制与不可证明项\n" + sections.limitations,
            )
        )

    @staticmethod
    def _render_graph_facts(facts: Iterable[GraphFact]) -> str:
        rows = []
        for fact in facts:
            rows.append(
                "- "
                + json.dumps(
                    {
                        "template_id": fact.template_id,
                        "node_ids": list(fact.node_ids),
                        "edges": [dict(edge) for edge in fact.edges],
                        "properties": dict(fact.properties),
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )
        return "\n".join(rows) if rows else "- 无已验证图事实。"

    @staticmethod
    def _render_text_evidence(evidences: Iterable[TextEvidence]) -> str:
        rows = []
        for evidence in evidences:
            rows.extend(
                (
                    f"### parent_id={evidence.parent_id} build_id={evidence.build_id}",
                    f"来源：{evidence.origin}；chunk_ids={','.join(evidence.chunk_ids)}；anchor_ids={','.join(evidence.anchor_ids) or '无'}",
                    evidence.text,
                )
            )
        return "\n\n".join(rows) if rows else "- 无可用正文证据。"

    @staticmethod
    def _render_limitations(limitations: Iterable[str]) -> str:
        rows = [f"- {item}" for item in limitations]
        return "\n".join(rows) if rows else "- 无额外限制。"
