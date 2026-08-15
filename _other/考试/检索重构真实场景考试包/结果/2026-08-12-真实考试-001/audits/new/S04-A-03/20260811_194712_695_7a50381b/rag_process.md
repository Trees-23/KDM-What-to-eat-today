# RAG Process

audit_id: 20260811_194712_695_7a50381b
timestamp: 2026-08-11T19:47:12.696
## Request
- original_query: 家里有鸡肉，知识库里能做哪些菜？
- original_query_hash: 2b70893df36e6191
- session_id: 2026-08-12-真实考试-001:new:S04-A-03
- request_mode: stream
- request_start: 2026-08-11T19:47:12.696
- evaluation_sample_id: 20260811_194712_695_7a50381b
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:47:12.697
- end: 2026-08-11T19:47:12.697
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:47:12.698
- end: 2026-08-11T19:47:12.698
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: 2b70893df36e6191

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:47:12.719
- end: 2026-08-11T19:47:12.719
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:47:12.719+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:47:12.724
- end: 2026-08-11T19:47:12.724
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:47:12.719+00:00
- result_count: 1

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:47:12.724
- end: 2026-08-11T19:47:12.724
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
- chunk_count: 86
- redacted_field: 2089
- total_duration_ms: 4212
- fallback_used: False

## Final Output
- answer_chars: 123
- answer_hash: 6d0c9fa449ada432
- success: True

## Request Complete
- request_end: 2026-08-11T19:47:16.959
- request_duration_ms: 4263
- success: True
- final_source: generation

