# RAG Process

audit_id: 20260812_050809_176_83878031
timestamp: 2026-08-12T05:08:09.177
## Request
- original_query: 牛肉适合搭配什么蔬菜？
- original_query_hash: 1b8dadc5fd66eafa
- session_id: 2026-08-12-new-smoke-001:new:S05-A-01
- request_mode: stream
- request_start: 2026-08-12T05:08:09.177
- evaluation_sample_id: 20260812_050809_176_83878031
- experiment_id: 2026-08-12-new-smoke-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:08:09.178
- end: 2026-08-12T05:08:09.178
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:08:09.179
- end: 2026-08-12T05:08:09.179
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 11
- enhanced_query_length: 11
- enhanced_query_hash: 1b8dadc5fd66eafa

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:08:09.186
- end: 2026-08-12T05:08:09.186
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-12T05:08:09.186+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T05:08:09.194
- end: 2026-08-12T05:08:09.194
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-12T05:08:09.186+00:00
- result_count: 5

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T05:08:09.194
- end: 2026-08-12T05:08:09.194
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
- context_chars: 1896
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
- redacted_field: 5425
- total_duration_ms: 5426
- fallback_used: False

## Final Output
- answer_chars: 211
- answer_hash: 91237817973d9874
- success: True

## Request Complete
- request_end: 2026-08-12T05:08:14.634
- request_duration_ms: 5456
- success: True
- final_source: generation

