# RAG Process

audit_id: 20260812_050743_762_4eb8f906
timestamp: 2026-08-12T05:07:43.762
## Request
- original_query: 请说明“如何决策吃什么”这个技巧的关键要点和适用情形。
- original_query_hash: a20e75c819e5e1b7
- session_id: 2026-08-12-new-smoke-001:new:S03-A-01
- request_mode: stream
- request_start: 2026-08-12T05:07:43.762
- evaluation_sample_id: 20260812_050743_762_4eb8f906
- experiment_id: 2026-08-12-new-smoke-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:07:43.763
- end: 2026-08-12T05:07:43.763
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:07:43.764
- end: 2026-08-12T05:07:43.764
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: a20e75c819e5e1b7

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:07:43.767
- end: 2026-08-12T05:07:43.767
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-12T05:07:43.767+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T05:07:43.770
- end: 2026-08-12T05:07:43.770
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-12T05:07:43.767+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:07:43.770
- end: 2026-08-12T05:07:43.770
- duration_ms: 0
- entity_id: tipdoc_820d789ff48e
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:07:43.777
- end: 2026-08-12T05:07:43.777
- duration_ms: 0
- parent_id: tipdoc_820d789ff48e
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 8

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T05:07:43.777
- end: 2026-08-12T05:07:43.777
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
- chunk_count: 711
- redacted_field: 3769
- total_duration_ms: 16456
- fallback_used: False

## Final Output
- answer_chars: 1060
- answer_hash: 69707f03f1003f2f
- success: True

## Request Complete
- request_end: 2026-08-12T05:08:00.255
- request_duration_ms: 16493
- success: True
- final_source: generation

