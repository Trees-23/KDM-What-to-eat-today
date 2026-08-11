# RAG Process

audit_id: 20260811_194949_121_25209ec0
timestamp: 2026-08-11T19:49:49.121
## Request
- original_query: 虾适合搭配什么蔬菜？
- original_query_hash: 7f746847edc889e2
- session_id: 2026-08-12-真实考试-001:new:S05-A-08
- request_mode: stream
- request_start: 2026-08-11T19:49:49.121
- evaluation_sample_id: 20260811_194949_121_25209ec0
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:49:49.122
- end: 2026-08-11T19:49:49.122
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:49:49.123
- end: 2026-08-11T19:49:49.123
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 10
- enhanced_query_length: 10
- enhanced_query_hash: 7f746847edc889e2

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: not_found
- start: 2026-08-11T19:49:49.279
- end: 2026-08-11T19:49:49.279
- duration_ms: 0
- template_id: None
- graph_fact_status: None
- graph_fact_count: 0
- limitations: ['ENTITY_NOT_FOUND', '未定位到关系查询中的同名实体；未调用全库向量检索。']
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 127
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
- request_end: 2026-08-11T19:49:49.288
- request_duration_ms: 167
- success: True
- final_source: generation

