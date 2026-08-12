# RAG Process

audit_id: 20260812_050641_284_81e1c413
timestamp: 2026-08-12T05:06:41.284
## Request
- original_query: 请给出清蒸鲈鱼的完整做法，包括主要食材和步骤。
- original_query_hash: a5dd296e5aae3d11
- session_id: 2026-08-12-new-smoke-001:new:S01-A-01
- request_mode: stream
- request_start: 2026-08-12T05:06:41.285
- evaluation_sample_id: 20260812_050641_284_81e1c413
- experiment_id: 2026-08-12-new-smoke-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:06:41.286
- end: 2026-08-12T05:06:41.286
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:06:41.286
- end: 2026-08-12T05:06:41.286
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: a5dd296e5aae3d11

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:06:41.295
- end: 2026-08-12T05:06:41.295
- duration_ms: 0
- entity_id: 201000257
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:06:41.311
- end: 2026-08-12T05:06:41.311
- duration_ms: 0
- parent_id: 201000257
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-12T05:06:41.311
- end: 2026-08-12T05:06:41.311
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 1
- limitations: []
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1215
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
- chunk_count: 577
- redacted_field: 6664
- total_duration_ms: 25398
- fallback_used: False

## Final Output
- answer_chars: 768
- answer_hash: 99ebe669901308ac
- success: True

## Request Complete
- request_end: 2026-08-12T05:07:06.756
- request_duration_ms: 25471
- success: True
- final_source: generation

