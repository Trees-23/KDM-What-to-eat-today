# RAG Process

audit_id: 20260811_195054_983_33f2c2df
timestamp: 2026-08-11T19:50:54.984
## Request
- original_query: 家里人不太能吃辣，晚餐有什么选择，帮我找几个贴近这个需求的做法。
- original_query_hash: c6d5cce12fe86efa
- session_id: 2026-08-12-真实考试-001:new:S06-B-03
- request_mode: stream
- request_start: 2026-08-11T19:50:54.984
- evaluation_sample_id: 20260811_195054_983_33f2c2df
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:50:54.984
- end: 2026-08-11T19:50:54.984
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:50:54.985
- end: 2026-08-11T19:50:54.985
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 32
- enhanced_query_length: 32
- enhanced_query_hash: c6d5cce12fe86efa

## Event / entity_direct
- stage: entity_direct
- status: entity_not_found
- start: 2026-08-11T19:50:55.004
- end: 2026-08-11T19:50:55.004
- duration_ms: 0
- candidate_count: 0
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_NOT_FOUND', '未定位到同名实体；未调用全库向量检索。']
- vector_search_calls: 0

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-11T19:50:55.004
- end: 2026-08-11T19:50:55.004
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
- request_end: 2026-08-11T19:50:55.019
- request_duration_ms: 35
- success: True
- final_source: generation

