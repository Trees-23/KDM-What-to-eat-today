# RAG Process

audit_id: 20260811_195055_556_95b812c2
timestamp: 2026-08-11T19:50:55.557
## Request
- original_query: 想做带番茄风味的菜。请展示推荐依据；如果意图无法由资料支持，不要把推测写成事实。
- original_query_hash: aedc978d564d7733
- session_id: 2026-08-12-真实考试-001:new:S06-C-04
- request_mode: stream
- request_start: 2026-08-11T19:50:55.558
- evaluation_sample_id: 20260811_195055_556_95b812c2
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:50:55.558
- end: 2026-08-11T19:50:55.558
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:50:55.558
- end: 2026-08-11T19:50:55.558
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 40
- enhanced_query_length: 40
- enhanced_query_hash: aedc978d564d7733

## Event / entity_direct
- stage: entity_direct
- status: entity_not_found
- start: 2026-08-11T19:50:55.578
- end: 2026-08-11T19:50:55.578
- duration_ms: 0
- candidate_count: 0
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_NOT_FOUND', '未定位到同名实体；未调用全库向量检索。']
- vector_search_calls: 0

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-11T19:50:55.578
- end: 2026-08-11T19:50:55.578
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
- request_end: 2026-08-11T19:50:55.606
- request_duration_ms: 48
- success: True
- final_source: generation

