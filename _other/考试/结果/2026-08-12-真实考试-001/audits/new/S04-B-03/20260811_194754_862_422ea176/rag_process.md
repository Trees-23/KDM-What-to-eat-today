# RAG Process

audit_id: 20260811_194754_862_422ea176
timestamp: 2026-08-11T19:47:54.863
## Request
- original_query: 有羊肉可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: 42e8edcebc5ff17f
- session_id: 2026-08-12-真实考试-001:new:S04-B-03
- request_mode: stream
- request_start: 2026-08-11T19:47:54.863
- evaluation_sample_id: 20260811_194754_862_422ea176
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:47:54.864
- end: 2026-08-11T19:47:54.864
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:47:54.864
- end: 2026-08-11T19:47:54.864
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: 42e8edcebc5ff17f

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:47:54.868
- end: 2026-08-11T19:47:54.868
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:47:54.868+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:47:54.870
- end: 2026-08-11T19:47:54.870
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:47:54.868+00:00
- result_count: 1

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:47:54.870
- end: 2026-08-11T19:47:54.870
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
- context_chars: 530
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
- chunk_count: 141
- redacted_field: 5946
- total_duration_ms: 9002
- fallback_used: False

## Final Output
- answer_chars: 211
- answer_hash: 4587fb60e4f637e5
- success: True

## Request Complete
- request_end: 2026-08-11T19:48:03.902
- request_duration_ms: 9038
- success: True
- final_source: generation

