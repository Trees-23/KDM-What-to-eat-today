# RAG Process

audit_id: 20260811_195054_348_1d435a02
timestamp: 2026-08-11T19:50:54.348
## Request
- original_query: 天气热，想做一道清爽不腻的晚饭。请推荐知识库中最合适的菜，并说明依据。
- original_query_hash: 972c852ccbacab42
- session_id: 2026-08-12-真实考试-001:new:S06-A-01
- request_mode: stream
- request_start: 2026-08-11T19:50:54.349
- evaluation_sample_id: 20260811_195054_348_1d435a02
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:50:54.350
- end: 2026-08-11T19:50:54.350
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:50:54.350
- end: 2026-08-11T19:50:54.350
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: 972c852ccbacab42

## Event / entity_direct
- stage: entity_direct
- status: entity_not_found
- start: 2026-08-11T19:50:54.379
- end: 2026-08-11T19:50:54.379
- duration_ms: 0
- candidate_count: 0
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_NOT_FOUND', '未定位到同名实体；未调用全库向量检索。']
- vector_search_calls: 0

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-11T19:50:54.379
- end: 2026-08-11T19:50:54.379
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
- request_end: 2026-08-11T19:50:54.400
- request_duration_ms: 50
- success: True
- final_source: generation

