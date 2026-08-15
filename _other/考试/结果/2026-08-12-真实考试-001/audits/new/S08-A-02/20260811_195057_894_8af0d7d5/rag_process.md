# RAG Process

audit_id: 20260811_195057_894_8af0d7d5
timestamp: 2026-08-11T19:50:57.895
## Request
- original_query: 云岚02号幻味砂锅怎么做？
- original_query_hash: bf63f7ae536908e5
- session_id: 2026-08-12-真实考试-001:new:S08-A-02
- request_mode: stream
- request_start: 2026-08-11T19:50:57.895
- evaluation_sample_id: 20260811_195057_894_8af0d7d5
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:50:57.895
- end: 2026-08-11T19:50:57.895
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:50:57.896
- end: 2026-08-11T19:50:57.896
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 13
- enhanced_query_length: 13
- enhanced_query_hash: bf63f7ae536908e5

## Event / entity_direct
- stage: entity_direct
- status: entity_not_found
- start: 2026-08-11T19:50:57.908
- end: 2026-08-11T19:50:57.908
- duration_ms: 0
- candidate_count: 0
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_NOT_FOUND', '未定位到同名实体；未调用全库向量检索。']
- vector_search_calls: 0

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-11T19:50:57.908
- end: 2026-08-11T19:50:57.908
- duration_ms: 0
- candidate_count: 0
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_NOT_FOUND', '未定位到同名实体；未调用全库向量检索。']
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 121
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 0
- text_evidence_count: 0
- limitation_count: 2
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Request Complete
- request_end: 2026-08-11T19:50:57.920
- request_duration_ms: 25
- success: True
- final_source: generation

