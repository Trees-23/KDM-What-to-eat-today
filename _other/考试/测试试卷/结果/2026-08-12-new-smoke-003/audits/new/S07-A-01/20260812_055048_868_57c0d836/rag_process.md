# RAG Process

audit_id: 20260812_055048_868_57c0d836
timestamp: 2026-08-12T05:50:48.869
## Request
- original_query: 想吃川菜但口感清爽。请推荐几个可考虑的菜。
- original_query_hash: 821badeb7b47a5d5
- session_id: 2026-08-12-new-smoke-003:new:S07-A-01
- request_mode: stream
- request_start: 2026-08-12T05:50:48.869
- evaluation_sample_id: 20260812_055048_868_57c0d836
- experiment_id: 2026-08-12-new-smoke-003
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:50:48.870
- end: 2026-08-12T05:50:48.870
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:50:48.870
- end: 2026-08-12T05:50:48.870
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 821badeb7b47a5d5

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:50:48.917
- end: 2026-08-12T05:50:48.917
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-12T05:50:48.917+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T05:50:48.924
- end: 2026-08-12T05:50:48.924
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-12T05:50:48.917+00:00
- result_count: 32

## Event / restricted_vector
- stage: restricted_vector
- status: selected
- start: 2026-08-12T05:50:49.387
- end: 2026-08-12T05:50:49.387
- duration_ms: 0
- parent_count: 5
- vector_scope: candidate_parents

## Event / nutrition_recommendation
- stage: nutrition_recommendation
- status: soft-preference-selected
- start: 2026-08-12T05:50:49.388
- end: 2026-08-12T05:50:49.388
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
- chunk_count: 572
- redacted_field: 4301
- total_duration_ms: 15625
- fallback_used: False

## Final Output
- answer_chars: 737
- answer_hash: e6ffe0ff904d9615
- success: True

## Request Complete
- request_end: 2026-08-12T05:51:05.024
- request_duration_ms: 16154
- success: True
- final_source: generation

