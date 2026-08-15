# RAG Process

audit_id: 20260812_054919_826_d689f5d5
timestamp: 2026-08-12T05:49:19.827
## Request
- original_query: 请给出清蒸鲈鱼的完整做法，包括主要食材和步骤。
- original_query_hash: a5dd296e5aae3d11
- session_id: 2026-08-12-new-smoke-003:new:S01-A-01
- request_mode: stream
- request_start: 2026-08-12T05:49:19.827
- evaluation_sample_id: 20260812_054919_826_d689f5d5
- experiment_id: 2026-08-12-new-smoke-003
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:49:19.828
- end: 2026-08-12T05:49:19.828
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:49:19.828
- end: 2026-08-12T05:49:19.828
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: a5dd296e5aae3d11

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:49:19.835
- end: 2026-08-12T05:49:19.835
- duration_ms: 0
- entity_id: 201000257
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:49:19.844
- end: 2026-08-12T05:49:19.844
- duration_ms: 0
- parent_id: 201000257
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-12T05:49:19.844
- end: 2026-08-12T05:49:19.844
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
- chunk_count: 527
- redacted_field: 4051
- total_duration_ms: 13918
- fallback_used: False

## Final Output
- answer_chars: 715
- answer_hash: 36f01c22e54f5052
- success: True

## Request Complete
- request_end: 2026-08-12T05:49:33.794
- request_duration_ms: 13966
- success: True
- final_source: generation

