# RAG Process

audit_id: 20260811_194905_030_ef7b67da
timestamp: 2026-08-11T19:49:05.031
## Request
- original_query: 菠菜能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: bca8defadcd60bbc
- session_id: 2026-08-12-真实考试-001:new:S04-C-09
- request_mode: stream
- request_start: 2026-08-11T19:49:05.031
- evaluation_sample_id: 20260811_194905_030_ef7b67da
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:49:05.032
- end: 2026-08-11T19:49:05.032
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:49:05.032
- end: 2026-08-11T19:49:05.032
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: bca8defadcd60bbc

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:49:05.035
- end: 2026-08-11T19:49:05.035
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:49:05.035+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:49:05.037
- end: 2026-08-11T19:49:05.037
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:49:05.035+00:00
- result_count: 1

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:49:05.037
- end: 2026-08-11T19:49:05.037
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
- context_chars: 532
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
- chunk_count: 57
- redacted_field: 2402
- total_duration_ms: 3591
- fallback_used: False

## Final Output
- answer_chars: 81
- answer_hash: d820142102284bfe
- success: True

## Request Complete
- request_end: 2026-08-11T19:49:08.649
- request_duration_ms: 3618
- success: True
- final_source: generation

