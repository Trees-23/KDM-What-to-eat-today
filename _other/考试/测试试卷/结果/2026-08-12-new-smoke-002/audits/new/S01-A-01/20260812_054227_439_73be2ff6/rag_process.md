# RAG Process

audit_id: 20260812_054227_439_73be2ff6
timestamp: 2026-08-12T05:42:27.440
## Request
- original_query: 请给出清蒸鲈鱼的完整做法，包括主要食材和步骤。
- original_query_hash: a5dd296e5aae3d11
- session_id: 2026-08-12-new-smoke-002:new:S01-A-01
- request_mode: stream
- request_start: 2026-08-12T05:42:27.440
- evaluation_sample_id: 20260812_054227_439_73be2ff6
- experiment_id: 2026-08-12-new-smoke-002
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:42:27.440
- end: 2026-08-12T05:42:27.440
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:42:27.441
- end: 2026-08-12T05:42:27.441
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: a5dd296e5aae3d11

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:42:27.447
- end: 2026-08-12T05:42:27.447
- duration_ms: 0
- entity_id: 201000257
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:42:27.456
- end: 2026-08-12T05:42:27.456
- duration_ms: 0
- parent_id: 201000257
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-12T05:42:27.457
- end: 2026-08-12T05:42:27.457
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
- chunk_count: 542
- redacted_field: 7347
- total_duration_ms: 19447
- fallback_used: False

## Final Output
- answer_chars: 719
- answer_hash: b1eeaaf304828ed7
- success: True

## Request Complete
- request_end: 2026-08-12T05:42:46.952
- request_duration_ms: 19512
- success: True
- final_source: generation

