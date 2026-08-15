# RAG Process

audit_id: 20260811_194831_397_d8719e91
timestamp: 2026-08-11T19:48:31.397
## Request
- original_query: 有大白菜可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: bb1966b4a52e5e32
- session_id: 2026-08-12-真实考试-001:new:S04-B-10
- request_mode: stream
- request_start: 2026-08-11T19:48:31.397
- evaluation_sample_id: 20260811_194831_397_d8719e91
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:48:31.398
- end: 2026-08-11T19:48:31.398
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:48:31.398
- end: 2026-08-11T19:48:31.398
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: bb1966b4a52e5e32

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:48:31.402
- end: 2026-08-11T19:48:31.402
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:48:31.402+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:48:31.405
- end: 2026-08-11T19:48:31.405
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:48:31.402+00:00
- result_count: 1

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:48:31.405
- end: 2026-08-11T19:48:31.405
- duration_ms: 0
- template_id: ingredient_recipes_v1
- graph_fact_status: verified
- graph_fact_count: 1
- limitations: []
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 535
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 0
- limitation_count: 0
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Generation Config
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: True
- timeout: 60
- max_retries: 3

## Generation Stream
- status: success
- chunk_count: 101
- redacted_field: 2195
- total_duration_ms: 4217
- fallback_used: False

## Final Output
- answer_chars: 147
- answer_hash: 7551b93433abcd93
- success: True

## Request Complete
- request_end: 2026-08-11T19:48:35.633
- request_duration_ms: 4235
- success: True
- final_source: generation

