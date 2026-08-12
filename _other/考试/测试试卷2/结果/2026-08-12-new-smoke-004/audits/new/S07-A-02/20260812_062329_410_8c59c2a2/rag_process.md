# RAG Process

audit_id: 20260812_062329_410_8c59c2a2
timestamp: 2026-08-12T06:23:29.410
## Request
- original_query: 想找少油感觉的川味晚餐。请推荐几个可考虑的菜。
- original_query_hash: f7cb8317eb782f37
- session_id: 2026-08-12-new-smoke-004:new:S07-A-02
- request_mode: stream
- request_start: 2026-08-12T06:23:29.410
- evaluation_sample_id: 20260812_062329_410_8c59c2a2
- experiment_id: 2026-08-12-new-smoke-004
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T06:23:29.411
- end: 2026-08-12T06:23:29.411
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T06:23:29.411
- end: 2026-08-12T06:23:29.411
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: f7cb8317eb782f37

## Event / entity_direct
- stage: entity_direct
- status: entity_not_found
- start: 2026-08-12T06:23:29.496
- end: 2026-08-12T06:23:29.496
- duration_ms: 0
- candidate_count: 0
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_NOT_FOUND', '未定位到同名实体；未调用全库向量检索。']
- vector_search_calls: 0

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-12T06:23:29.496
- end: 2026-08-12T06:23:29.496
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
- request_end: 2026-08-12T06:23:29.532
- request_duration_ms: 121
- success: True
- final_source: generation

