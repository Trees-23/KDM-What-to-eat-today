# RAG Process

audit_id: 20260811_194835_641_ddbaf5fc
timestamp: 2026-08-11T19:48:35.641
## Request
- original_query: 花菜能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: 9779d4c48c4a79b8
- session_id: 2026-08-12-真实考试-001:new:S04-C-01
- request_mode: stream
- request_start: 2026-08-11T19:48:35.642
- evaluation_sample_id: 20260811_194835_641_ddbaf5fc
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:48:35.642
- end: 2026-08-11T19:48:35.642
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:48:35.642
- end: 2026-08-11T19:48:35.642
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 9779d4c48c4a79b8

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:48:35.646
- end: 2026-08-11T19:48:35.646
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:48:35.646+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:48:35.647
- end: 2026-08-11T19:48:35.647
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:48:35.646+00:00
- result_count: 2

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:48:35.647
- end: 2026-08-11T19:48:35.647
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
- context_chars: 720
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
- chunk_count: 55
- redacted_field: 1837
- total_duration_ms: 4140
- fallback_used: False

## Final Output
- answer_chars: 76
- answer_hash: b48af7e55585fa16
- success: True

## Request Complete
- request_end: 2026-08-11T19:48:39.802
- request_duration_ms: 4160
- success: True
- final_source: generation

