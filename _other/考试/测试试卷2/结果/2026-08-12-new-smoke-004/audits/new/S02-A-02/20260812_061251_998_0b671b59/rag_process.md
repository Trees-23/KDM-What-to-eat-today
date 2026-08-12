# RAG Process

audit_id: 20260812_061251_998_0b671b59
timestamp: 2026-08-12T06:12:51.999
## Request
- original_query: 清蒸鳜鱼的第 1 步应该怎么做？
- original_query_hash: d834747786eb4802
- session_id: 2026-08-12-new-smoke-004:new:S02-A-02
- request_mode: stream
- request_start: 2026-08-12T06:12:51.999
- evaluation_sample_id: 20260812_061251_998_0b671b59
- experiment_id: 2026-08-12-new-smoke-004
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T06:12:51.999
- end: 2026-08-12T06:12:51.999
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T06:12:51.999
- end: 2026-08-12T06:12:51.999
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: d834747786eb4802

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T06:12:52.003
- end: 2026-08-12T06:12:52.003
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-12T06:12:52.003+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T06:12:52.005
- end: 2026-08-12T06:12:52.005
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-12T06:12:52.003+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T06:12:52.005
- end: 2026-08-12T06:12:52.005
- duration_ms: 0
- entity_id: 201002821
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-12T06:12:52.008
- end: 2026-08-12T06:12:52.008
- duration_ms: 0
- recipe_id: 201002821
- step_id: 201002829

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T06:12:52.010
- end: 2026-08-12T06:12:52.010
- duration_ms: 0
- parent_id: 201002821
- build_id: pds_2a8c0807733eb8022a623659
- anchor_id: 201002829
- chunk_count: 3

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T06:12:52.010
- end: 2026-08-12T06:12:52.010
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
- context_chars: 1394
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
- chunk_count: 89
- redacted_field: 3444
- total_duration_ms: 5355
- fallback_used: False

## Final Output
- answer_chars: 115
- answer_hash: 7aca502f8e069c32
- success: True

## Request Complete
- request_end: 2026-08-12T06:12:57.386
- request_duration_ms: 5387
- success: True
- final_source: generation

