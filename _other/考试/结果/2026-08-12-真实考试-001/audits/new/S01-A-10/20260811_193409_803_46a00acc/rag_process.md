# RAG Process

audit_id: 20260811_193409_803_46a00acc
timestamp: 2026-08-11T19:34:09.804
## Request
- original_query: 请给出红烧鱼头的完整做法，包括主要食材和步骤。
- original_query_hash: 17c614bdb263acba
- session_id: 2026-08-12-真实考试-001:new:S01-A-10
- request_mode: stream
- request_start: 2026-08-11T19:34:09.805
- evaluation_sample_id: 20260811_193409_803_46a00acc
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:34:09.806
- end: 2026-08-11T19:34:09.806
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:34:09.806
- end: 2026-08-11T19:34:09.806
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: 17c614bdb263acba

## Event / entity_direct
- stage: entity_direct
- status: ambiguous
- start: 2026-08-11T19:34:09.818
- end: 2026-08-11T19:34:09.818
- duration_ms: 0
- candidate_count: 2
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_AMBIGUOUS', '实体候选并列，未自动选择且未调用全库向量检索。']
- vector_search_calls: 0

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-11T19:34:09.818
- end: 2026-08-11T19:34:09.818
- duration_ms: 0
- candidate_count: 2
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_AMBIGUOUS', '实体候选并列，未自动选择且未调用全库向量检索。']
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 125
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 0
- text_evidence_count: 0
- limitation_count: 2
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Request Complete
- request_end: 2026-08-11T19:34:09.832
- request_duration_ms: 26
- success: True
- final_source: generation

