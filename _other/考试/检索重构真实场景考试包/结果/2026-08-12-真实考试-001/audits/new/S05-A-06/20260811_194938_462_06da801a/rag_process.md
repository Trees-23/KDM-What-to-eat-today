# RAG Process

audit_id: 20260811_194938_462_06da801a
timestamp: 2026-08-11T19:49:38.463
## Request
- original_query: 茄子适合搭配什么蔬菜？
- original_query_hash: 5716758c2886a42d
- session_id: 2026-08-12-真实考试-001:new:S05-A-06
- request_mode: stream
- request_start: 2026-08-11T19:49:38.464
- evaluation_sample_id: 20260811_194938_462_06da801a
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:49:38.464
- end: 2026-08-11T19:49:38.464
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:49:38.464
- end: 2026-08-11T19:49:38.464
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 11
- enhanced_query_length: 11
- enhanced_query_hash: 5716758c2886a42d

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:49:38.470
- end: 2026-08-11T19:49:38.470
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-11T19:49:38.470+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:49:38.472
- end: 2026-08-11T19:49:38.472
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-11T19:49:38.470+00:00
- result_count: 5

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:49:38.472
- end: 2026-08-11T19:49:38.472
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
- context_chars: 1875
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
- chunk_count: 138
- redacted_field: 2765
- total_duration_ms: 5358
- fallback_used: False

## Final Output
- answer_chars: 171
- answer_hash: f8c303e1ea4b1f4e
- success: True

## Request Complete
- request_end: 2026-08-11T19:49:43.851
- request_duration_ms: 5387
- success: True
- final_source: generation

