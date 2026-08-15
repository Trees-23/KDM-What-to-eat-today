# RAG Process

audit_id: 20260811_195055_451_0b07dd5c
timestamp: 2026-08-11T19:50:55.452
## Request
- original_query: 想做一道适合夏天的凉菜。请展示推荐依据；如果意图无法由资料支持，不要把推测写成事实。
- original_query_hash: c2268069bb0a9925
- session_id: 2026-08-12-真实考试-001:new:S06-C-02
- request_mode: stream
- request_start: 2026-08-11T19:50:55.452
- evaluation_sample_id: 20260811_195055_451_0b07dd5c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:50:55.452
- end: 2026-08-11T19:50:55.452
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:50:55.453
- end: 2026-08-11T19:50:55.453
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 42
- enhanced_query_length: 42
- enhanced_query_hash: c2268069bb0a9925

## Event / entity_direct
- stage: entity_direct
- status: entity_not_found
- start: 2026-08-11T19:50:55.468
- end: 2026-08-11T19:50:55.468
- duration_ms: 0
- candidate_count: 0
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_NOT_FOUND', '未定位到同名实体；未调用全库向量检索。']
- vector_search_calls: 0

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-11T19:50:55.468
- end: 2026-08-11T19:50:55.468
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
- request_end: 2026-08-11T19:50:55.480
- request_duration_ms: 28
- success: True
- final_source: generation

