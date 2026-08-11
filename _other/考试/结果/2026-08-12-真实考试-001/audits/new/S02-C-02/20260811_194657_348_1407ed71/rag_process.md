# RAG Process

audit_id: 20260811_194657_348_1407ed71
timestamp: 2026-08-11T19:46:57.349
## Request
- original_query: 只回答电饭煲三文鱼炊饭的第 1 步，并说明它来自哪一条菜谱步骤；不要混入后续步骤。
- original_query_hash: 8ba1014665c63da6
- session_id: 2026-08-12-真实考试-001:new:S02-C-02
- request_mode: stream
- request_start: 2026-08-11T19:46:57.349
- evaluation_sample_id: 20260811_194657_348_1407ed71
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:46:57.350
- end: 2026-08-11T19:46:57.350
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:46:57.351
- end: 2026-08-11T19:46:57.351
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 41
- enhanced_query_length: 41
- enhanced_query_hash: 8ba1014665c63da6

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: not_found
- start: 2026-08-11T19:46:57.356
- end: 2026-08-11T19:46:57.356
- duration_ms: 0
- template_id: None
- graph_fact_status: None
- graph_fact_count: 0
- limitations: ['ENTITY_AMBIGUOUS', '关系查询实体候选并列，未自动选择。']
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 119
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
- request_end: 2026-08-11T19:46:57.377
- request_duration_ms: 27
- success: True
- final_source: generation

