# RAG Process

audit_id: 20260812_061257_395_d7261800
timestamp: 2026-08-12T06:12:57.396
## Request
- original_query: 请说明“做菜专业术语”这个技巧的关键要点和适用情形。
- original_query_hash: ace57f005f71a6d6
- session_id: 2026-08-12-new-smoke-004:new:S03-A-02
- request_mode: stream
- request_start: 2026-08-12T06:12:57.396
- evaluation_sample_id: 20260812_061257_395_d7261800
- experiment_id: 2026-08-12-new-smoke-004
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T06:12:57.397
- end: 2026-08-12T06:12:57.397
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T06:12:57.397
- end: 2026-08-12T06:12:57.397
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: ace57f005f71a6d6

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T06:12:57.400
- end: 2026-08-12T06:12:57.400
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-12T06:12:57.400+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T06:12:57.434
- end: 2026-08-12T06:12:57.434
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-12T06:12:57.400+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T06:12:57.434
- end: 2026-08-12T06:12:57.434
- duration_ms: 0
- entity_id: tipdoc_fdb80333cd59
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T06:12:57.448
- end: 2026-08-12T06:12:57.448
- duration_ms: 0
- parent_id: tipdoc_fdb80333cd59
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T06:12:57.448
- end: 2026-08-12T06:12:57.448
- duration_ms: 0
- template_id: technique_chunks_v1
- graph_fact_status: verified
- graph_fact_count: 1
- limitations: []
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 6059
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
- chunk_count: 1256
- redacted_field: 3929
- total_duration_ms: 28496
- fallback_used: False

## Final Output
- answer_chars: 1618
- answer_hash: 350169c36b620660
- success: True

## Request Complete
- request_end: 2026-08-12T06:13:25.979
- request_duration_ms: 28583
- success: True
- final_source: generation

