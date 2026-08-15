# RAG Process

audit_id: 20260811_195058_628_bc75cd4a
timestamp: 2026-08-11T19:50:58.628
## Request
- original_query: 知识库里有云岚18号幻味砂锅这道菜吗？如果有请给做法。
- original_query_hash: c53067a4b7ee4de4
- session_id: 2026-08-12-真实考试-001:new:S08-B-08
- request_mode: stream
- request_start: 2026-08-11T19:50:58.629
- evaluation_sample_id: 20260811_195058_628_bc75cd4a
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:50:58.630
- end: 2026-08-11T19:50:58.630
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:50:58.630
- end: 2026-08-11T19:50:58.630
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: c53067a4b7ee4de4

## Event / entity_direct
- stage: entity_direct
- status: entity_not_found
- start: 2026-08-11T19:50:58.643
- end: 2026-08-11T19:50:58.643
- duration_ms: 0
- candidate_count: 0
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_NOT_FOUND', '未定位到同名实体；未调用全库向量检索。']
- vector_search_calls: 0

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-11T19:50:58.643
- end: 2026-08-11T19:50:58.643
- duration_ms: 0
- candidate_count: 0
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_NOT_FOUND', '未定位到同名实体；未调用全库向量检索。']
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 121
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
- request_end: 2026-08-11T19:50:58.664
- request_duration_ms: 34
- success: True
- final_source: generation

