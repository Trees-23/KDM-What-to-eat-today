# RAG Process

audit_id: 20260811_194658_584_00d90325
timestamp: 2026-08-11T19:46:58.584
## Request
- original_query: 只根据“辅料技巧”技巧章节的关键要点回答；资料没有说明的结论请明确保留。
- original_query_hash: f9d2d9415a89af77
- session_id: 2026-08-12-真实考试-001:new:S03-C-09
- request_mode: stream
- request_start: 2026-08-11T19:46:58.584
- evaluation_sample_id: 20260811_194658_584_00d90325
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:46:58.585
- end: 2026-08-11T19:46:58.585
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:46:58.585
- end: 2026-08-11T19:46:58.585
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: f9d2d9415a89af77

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:46:58.587
- end: 2026-08-11T19:46:58.587
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-11T19:46:58.587+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:46:58.589
- end: 2026-08-11T19:46:58.589
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-11T19:46:58.587+00:00
- result_count: 2

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:46:58.589
- end: 2026-08-11T19:46:58.589
- duration_ms: 0
- entity_id: tipdoc_42a8d9f8ff95
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:46:58.589
- end: 2026-08-11T19:46:58.589
- duration_ms: 0
- error_type: ProgrammingError

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:46:58.589
- end: 2026-08-11T19:46:58.589
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
- context_chars: 882
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
- request_end: 2026-08-11T19:46:58.603
- request_duration_ms: 18
- success: True
- final_source: generation

