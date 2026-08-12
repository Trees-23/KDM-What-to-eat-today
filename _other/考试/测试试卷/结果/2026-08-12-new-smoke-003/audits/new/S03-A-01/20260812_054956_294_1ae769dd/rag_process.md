# RAG Process

audit_id: 20260812_054956_294_1ae769dd
timestamp: 2026-08-12T05:49:56.294
## Request
- original_query: 请说明“如何决策吃什么”这个技巧的关键要点和适用情形。
- original_query_hash: a20e75c819e5e1b7
- session_id: 2026-08-12-new-smoke-003:new:S03-A-01
- request_mode: stream
- request_start: 2026-08-12T05:49:56.295
- evaluation_sample_id: 20260812_054956_294_1ae769dd
- experiment_id: 2026-08-12-new-smoke-003
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:49:56.295
- end: 2026-08-12T05:49:56.295
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:49:56.296
- end: 2026-08-12T05:49:56.296
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: a20e75c819e5e1b7

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:49:56.299
- end: 2026-08-12T05:49:56.299
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-12T05:49:56.299+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T05:49:56.302
- end: 2026-08-12T05:49:56.302
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-12T05:49:56.299+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:49:56.302
- end: 2026-08-12T05:49:56.302
- duration_ms: 0
- entity_id: tipdoc_820d789ff48e
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:49:56.313
- end: 2026-08-12T05:49:56.313
- duration_ms: 0
- parent_id: tipdoc_820d789ff48e
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 8

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T05:49:56.313
- end: 2026-08-12T05:49:56.313
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
- context_chars: 2915
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
- chunk_count: 580
- redacted_field: 2163
- total_duration_ms: 13539
- fallback_used: False

## Final Output
- answer_chars: 836
- answer_hash: 4ffb3bf54e37eabd
- success: True

## Request Complete
- request_end: 2026-08-12T05:50:09.900
- request_duration_ms: 13605
- success: True
- final_source: generation

