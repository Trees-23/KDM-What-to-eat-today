# RAG Process

audit_id: 20260812_050800_261_1bdb0574
timestamp: 2026-08-12T05:08:00.262
## Request
- original_query: 家里有牛肉，知识库里能做哪些菜？
- original_query_hash: d6b623295d0d1c45
- session_id: 2026-08-12-new-smoke-001:new:S04-A-01
- request_mode: stream
- request_start: 2026-08-12T05:08:00.262
- evaluation_sample_id: 20260812_050800_261_1bdb0574
- experiment_id: 2026-08-12-new-smoke-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:08:00.263
- end: 2026-08-12T05:08:00.263
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:08:00.263
- end: 2026-08-12T05:08:00.263
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: d6b623295d0d1c45

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:08:00.268
- end: 2026-08-12T05:08:00.268
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-12T05:08:00.268+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T05:08:00.271
- end: 2026-08-12T05:08:00.271
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-12T05:08:00.268+00:00
- result_count: 5

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T05:08:00.271
- end: 2026-08-12T05:08:00.271
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
- context_chars: 1295
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
- chunk_count: 114
- redacted_field: 5681
- total_duration_ms: 8872
- fallback_used: False

## Final Output
- answer_chars: 158
- answer_hash: ce74d8e7a436e468
- success: True

## Request Complete
- request_end: 2026-08-12T05:08:09.169
- request_duration_ms: 8906
- success: True
- final_source: generation

