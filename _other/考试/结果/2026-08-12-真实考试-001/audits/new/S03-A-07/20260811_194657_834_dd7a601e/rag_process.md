# RAG Process

audit_id: 20260811_194657_834_dd7a601e
timestamp: 2026-08-11T19:46:57.835
## Request
- original_query: 请说明“蒸（米）/炖（使用电饭煲/高压锅/电压力锅）”这个技巧的关键要点和适用情形。
- original_query_hash: c393fcfd7bbdc6a9
- session_id: 2026-08-12-真实考试-001:new:S03-A-07
- request_mode: stream
- request_start: 2026-08-11T19:46:57.835
- evaluation_sample_id: 20260811_194657_834_dd7a601e
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:46:57.836
- end: 2026-08-11T19:46:57.836
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:46:57.836
- end: 2026-08-11T19:46:57.836
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 42
- enhanced_query_length: 42
- enhanced_query_hash: c393fcfd7bbdc6a9

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:46:57.839
- end: 2026-08-11T19:46:57.839
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-11T19:46:57.839+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:46:57.847
- end: 2026-08-11T19:46:57.847
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-11T19:46:57.839+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:46:57.847
- end: 2026-08-11T19:46:57.847
- duration_ms: 0
- entity_id: tipdoc_4ba80da791e4
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:46:57.847
- end: 2026-08-11T19:46:57.847
- duration_ms: 0
- error_type: ProgrammingError

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:46:57.847
- end: 2026-08-11T19:46:57.847
- duration_ms: 0
- template_id: technique_chunks_v1
- graph_fact_status: verified
- graph_fact_count: 1
- limitations: ['parent-store-unavailable']
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1725
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 0
- limitation_count: 1
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Request Complete
- request_end: 2026-08-11T19:46:57.863
- request_duration_ms: 27
- success: True
- final_source: generation

