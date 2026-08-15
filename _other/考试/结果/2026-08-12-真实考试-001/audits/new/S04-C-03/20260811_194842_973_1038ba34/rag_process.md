# RAG Process

audit_id: 20260811_194842_973_1038ba34
timestamp: 2026-08-11T19:48:42.973
## Request
- original_query: 黄瓜能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: d27ed852fdc08588
- session_id: 2026-08-12-真实考试-001:new:S04-C-03
- request_mode: stream
- request_start: 2026-08-11T19:48:42.973
- evaluation_sample_id: 20260811_194842_973_1038ba34
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:48:42.974
- end: 2026-08-11T19:48:42.974
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:48:42.975
- end: 2026-08-11T19:48:42.975
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: d27ed852fdc08588

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:48:42.980
- end: 2026-08-11T19:48:42.980
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:48:42.980+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:48:42.982
- end: 2026-08-11T19:48:42.982
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:48:42.980+00:00
- result_count: 5

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:48:42.983
- end: 2026-08-11T19:48:42.983
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
- context_chars: 1284
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
- chunk_count: 85
- redacted_field: 2131
- total_duration_ms: 3913
- fallback_used: False

## Final Output
- answer_chars: 124
- answer_hash: 4af52f28ccaedb45
- success: True

## Request Complete
- request_end: 2026-08-11T19:48:46.923
- request_duration_ms: 3949
- success: True
- final_source: generation

