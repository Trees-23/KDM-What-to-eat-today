# RAG Process

audit_id: 20260811_194956_744_73587bcb
timestamp: 2026-08-11T19:49:56.744
## Request
- original_query: 做排骨相关菜时，知识图谱里有哪些蔬菜搭配？
- original_query_hash: af8e25fe34ad09e9
- session_id: 2026-08-12-真实考试-001:new:S05-B-01
- request_mode: stream
- request_start: 2026-08-11T19:49:56.745
- evaluation_sample_id: 20260811_194956_744_73587bcb
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:49:56.745
- end: 2026-08-11T19:49:56.745
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:49:56.746
- end: 2026-08-11T19:49:56.746
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: af8e25fe34ad09e9

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:49:56.749
- end: 2026-08-11T19:49:56.749
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-11T19:49:56.749+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:49:56.750
- end: 2026-08-11T19:49:56.750
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-11T19:49:56.749+00:00
- result_count: 5

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:49:56.751
- end: 2026-08-11T19:49:56.751
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- graph_fact_status: verified
- graph_fact_count: 1
- limitations: []
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1967
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
- chunk_count: 1
- redacted_field: 4952
- total_duration_ms: 4953
- fallback_used: False

## Final Output
- answer_chars: 196
- answer_hash: 0f4006c4d8ba3aa1
- success: True

## Request Complete
- request_end: 2026-08-11T19:50:01.727
- request_duration_ms: 4982
- success: True
- final_source: generation

