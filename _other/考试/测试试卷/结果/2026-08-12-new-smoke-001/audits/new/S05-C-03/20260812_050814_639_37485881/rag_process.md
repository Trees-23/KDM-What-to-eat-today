# RAG Process

audit_id: 20260812_050814_639_37485881
timestamp: 2026-08-12T05:08:14.639
## Request
- original_query: 只给出图中能验证的新鲜玉米与蔬菜搭配；没有路径时请说明无法证明。
- original_query_hash: f253a61e1feb471f
- session_id: 2026-08-12-new-smoke-001:new:S05-C-03
- request_mode: stream
- request_start: 2026-08-12T05:08:14.640
- evaluation_sample_id: 20260812_050814_639_37485881
- experiment_id: 2026-08-12-new-smoke-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:08:14.640
- end: 2026-08-12T05:08:14.640
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:08:14.640
- end: 2026-08-12T05:08:14.640
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 32
- enhanced_query_length: 32
- enhanced_query_hash: f253a61e1feb471f

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:08:14.645
- end: 2026-08-12T05:08:14.645
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-12T05:08:14.645+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-12T05:08:14.648
- end: 2026-08-12T05:08:14.648
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-12T05:08:14.645+00:00
- result_count: 0

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:08:14.648
- end: 2026-08-12T05:08:14.648
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-12T05:08:14.648+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T05:08:14.653
- end: 2026-08-12T05:08:14.653
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-12T05:08:14.648+00:00
- result_count: 5

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T05:08:14.654
- end: 2026-08-12T05:08:14.654
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- graph_fact_status: verified
- graph_fact_count: 2
- limitations: []
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1897
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
- chunk_count: 93
- redacted_field: 2143
- total_duration_ms: 4190
- fallback_used: False

## Final Output
- answer_chars: 119
- answer_hash: 00c1f73d8e7a6212
- success: True

## Request Complete
- request_end: 2026-08-12T05:08:18.863
- request_duration_ms: 4223
- success: True
- final_source: generation

