# RAG Process

audit_id: 20260812_054952_028_02191fa6
timestamp: 2026-08-12T05:49:52.028
## Request
- original_query: 回锅肉的第 1 步应该怎么做？
- original_query_hash: a488329948e4c411
- session_id: 2026-08-12-new-smoke-003:new:S02-A-01
- request_mode: stream
- request_start: 2026-08-12T05:49:52.028
- evaluation_sample_id: 20260812_054952_028_02191fa6
- experiment_id: 2026-08-12-new-smoke-003
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:49:52.029
- end: 2026-08-12T05:49:52.029
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:49:52.029
- end: 2026-08-12T05:49:52.029
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 15
- enhanced_query_length: 15
- enhanced_query_hash: a488329948e4c411

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:49:52.033
- end: 2026-08-12T05:49:52.033
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-12T05:49:52.033+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T05:49:52.035
- end: 2026-08-12T05:49:52.035
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-12T05:49:52.033+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:49:52.035
- end: 2026-08-12T05:49:52.035
- duration_ms: 0
- entity_id: 201002350
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-12T05:49:52.037
- end: 2026-08-12T05:49:52.037
- duration_ms: 0
- recipe_id: 201002350
- step_id: 201002360

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:49:52.038
- end: 2026-08-12T05:49:52.038
- duration_ms: 0
- parent_id: 201002350
- build_id: pds_2a8c0807733eb8022a623659
- anchor_id: 201002360
- chunk_count: 3

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T05:49:52.038
- end: 2026-08-12T05:49:52.038
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- graph_fact_status: verified
- graph_fact_count: 1
- limitations: []
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1616
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 1
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
- chunk_count: 80
- redacted_field: 2483
- total_duration_ms: 4235
- fallback_used: False

## Final Output
- answer_chars: 107
- answer_hash: 9246b79e664b2e6b
- success: True

## Request Complete
- request_end: 2026-08-12T05:49:56.288
- request_duration_ms: 4259
- success: True
- final_source: generation

