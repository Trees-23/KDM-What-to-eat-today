# RAG Process

audit_id: 20260811_194821_073_aa5bd6a8
timestamp: 2026-08-11T19:48:21.073
## Request
- original_query: 有米饭可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: 57534d04268415b3
- session_id: 2026-08-12-真实考试-001:new:S04-B-08
- request_mode: stream
- request_start: 2026-08-11T19:48:21.073
- evaluation_sample_id: 20260811_194821_073_aa5bd6a8
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:48:21.074
- end: 2026-08-11T19:48:21.074
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:48:21.074
- end: 2026-08-11T19:48:21.074
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: 57534d04268415b3

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:48:21.077
- end: 2026-08-11T19:48:21.077
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:48:21.077+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:48:21.079
- end: 2026-08-11T19:48:21.079
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:48:21.077+00:00
- result_count: 5

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:48:21.079
- end: 2026-08-11T19:48:21.079
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
- context_chars: 1287
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
- chunk_count: 135
- redacted_field: 3497
- total_duration_ms: 5991
- fallback_used: False

## Final Output
- answer_chars: 194
- answer_hash: cacd375f2578dd99
- success: True

## Request Complete
- request_end: 2026-08-11T19:48:27.082
- request_duration_ms: 6008
- success: True
- final_source: generation

