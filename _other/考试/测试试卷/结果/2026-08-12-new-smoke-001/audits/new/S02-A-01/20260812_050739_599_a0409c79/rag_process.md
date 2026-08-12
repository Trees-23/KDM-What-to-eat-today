# RAG Process

audit_id: 20260812_050739_599_a0409c79
timestamp: 2026-08-12T05:07:39.600
## Request
- original_query: 回锅肉的第 1 步应该怎么做？
- original_query_hash: a488329948e4c411
- session_id: 2026-08-12-new-smoke-001:new:S02-A-01
- request_mode: stream
- request_start: 2026-08-12T05:07:39.600
- evaluation_sample_id: 20260812_050739_599_a0409c79
- experiment_id: 2026-08-12-new-smoke-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:07:39.601
- end: 2026-08-12T05:07:39.601
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:07:39.601
- end: 2026-08-12T05:07:39.601
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 15
- enhanced_query_length: 15
- enhanced_query_hash: a488329948e4c411

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:07:39.605
- end: 2026-08-12T05:07:39.605
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-12T05:07:39.605+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T05:07:39.702
- end: 2026-08-12T05:07:39.702
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-12T05:07:39.605+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:07:39.702
- end: 2026-08-12T05:07:39.702
- duration_ms: 0
- entity_id: 201002350
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-12T05:07:39.705
- end: 2026-08-12T05:07:39.705
- duration_ms: 0
- recipe_id: 201002350
- step_id: 201002360

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:07:39.707
- end: 2026-08-12T05:07:39.707
- duration_ms: 0
- parent_id: 201002350
- build_id: pds_2a8c0807733eb8022a623659
- anchor_id: 201002360
- chunk_count: 3

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T05:07:39.707
- end: 2026-08-12T05:07:39.707
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
- chunk_count: 102
- redacted_field: 1916
- total_duration_ms: 4023
- fallback_used: False

## Final Output
- answer_chars: 158
- answer_hash: 679314b6f42bfc98
- success: True

## Request Complete
- request_end: 2026-08-12T05:07:43.758
- request_duration_ms: 4157
- success: True
- final_source: generation

