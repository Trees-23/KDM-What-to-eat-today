# RAG Process

audit_id: 20260811_195058_403_d6dbea00
timestamp: 2026-08-11T19:50:58.404
## Request
- original_query: 知识库里有云岚14号幻味砂锅这道菜吗？如果有请给做法。
- original_query_hash: 7e14ffc0a43f447d
- session_id: 2026-08-12-真实考试-001:new:S08-B-04
- request_mode: stream
- request_start: 2026-08-11T19:50:58.404
- evaluation_sample_id: 20260811_195058_403_d6dbea00
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:50:58.405
- end: 2026-08-11T19:50:58.405
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:50:58.405
- end: 2026-08-11T19:50:58.405
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: 7e14ffc0a43f447d

## Event / entity_direct
- stage: entity_direct
- status: entity_not_found
- start: 2026-08-11T19:50:58.429
- end: 2026-08-11T19:50:58.429
- duration_ms: 0
- candidate_count: 0
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_NOT_FOUND', '未定位到同名实体；未调用全库向量检索。']
- vector_search_calls: 0

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-11T19:50:58.430
- end: 2026-08-11T19:50:58.430
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
- request_end: 2026-08-11T19:50:58.464
- request_duration_ms: 60
- success: True
- final_source: generation

