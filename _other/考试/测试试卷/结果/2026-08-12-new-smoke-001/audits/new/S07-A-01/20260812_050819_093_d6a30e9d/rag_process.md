# RAG Process

audit_id: 20260812_050819_093_d6a30e9d
timestamp: 2026-08-12T05:08:19.094
## Request
- original_query: 想吃川菜但口感清爽。请推荐几个可考虑的菜。
- original_query_hash: 821badeb7b47a5d5
- session_id: 2026-08-12-new-smoke-001:new:S07-A-01
- request_mode: stream
- request_start: 2026-08-12T05:08:19.094
- evaluation_sample_id: 20260812_050819_093_d6a30e9d
- experiment_id: 2026-08-12-new-smoke-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:08:19.094
- end: 2026-08-12T05:08:19.094
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:08:19.094
- end: 2026-08-12T05:08:19.094
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 821badeb7b47a5d5

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:08:19.120
- end: 2026-08-12T05:08:19.120
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-12T05:08:19.120+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T05:08:19.166
- end: 2026-08-12T05:08:19.166
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-12T05:08:19.120+00:00
- result_count: 32

## Event / restricted_vector
- stage: restricted_vector
- status: selected
- start: 2026-08-12T05:08:19.499
- end: 2026-08-12T05:08:19.499
- duration_ms: 0
- parent_count: 5
- vector_scope: candidate_parents

## Event / nutrition_recommendation
- stage: nutrition_recommendation
- status: soft-preference-selected
- start: 2026-08-12T05:08:19.499
- end: 2026-08-12T05:08:19.499
- duration_ms: 0
- evidence_level: soft_preference
- policy_version: nutrition_soft_preference_v1
- source_status: missing_governed_nutrition_source
- missing_reason: 当前资料不能验证严格低脂；仅可作为少油/清爽偏好参考。
- claim_scope: 少油/清爽偏好
- text_evidence_count: 5
- limitations: ['NUTRITION_SOFT_PREFERENCE_ONLY', '当前资料不能验证严格低脂；仅可作为少油/清爽偏好参考。']

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 5801
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 0
- text_evidence_count: 5
- limitation_count: 2
- recommendation_evidence_level: soft_preference
- recommendation_policy_version: nutrition_soft_preference_v1

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
- chunk_count: 445
- redacted_field: 2687
- total_duration_ms: 14649
- fallback_used: False

## Final Output
- answer_chars: 552
- answer_hash: 168ac7d4426c63e6
- success: True

## Request Complete
- request_end: 2026-08-12T05:08:34.162
- request_duration_ms: 15068
- success: True
- final_source: generation

