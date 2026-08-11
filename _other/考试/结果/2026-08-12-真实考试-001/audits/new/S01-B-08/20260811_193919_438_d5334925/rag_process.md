# RAG Process

audit_id: 20260811_193919_438_d5334925
timestamp: 2026-08-11T19:39:19.438
## Request
- original_query: 凉拌黄瓜从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 3a5cbfd63d2f53f7
- session_id: 2026-08-12-真实考试-001:new:S01-B-08
- request_mode: stream
- request_start: 2026-08-11T19:39:19.439
- evaluation_sample_id: 20260811_193919_438_d5334925
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:39:19.439
- end: 2026-08-11T19:39:19.439
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:39:19.440
- end: 2026-08-11T19:39:19.440
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: 3a5cbfd63d2f53f7

## Event / entity_direct
- stage: entity_direct
- status: ambiguous
- start: 2026-08-11T19:39:19.444
- end: 2026-08-11T19:39:19.444
- duration_ms: 0
- candidate_count: 2
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_AMBIGUOUS', '实体候选并列，未自动选择且未调用全库向量检索。']
- vector_search_calls: 0

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-11T19:39:19.444
- end: 2026-08-11T19:39:19.444
- duration_ms: 0
- candidate_count: 2
- graph_fact_statuses: []
- text_evidence_count: 0
- limitations: ['ENTITY_AMBIGUOUS', '实体候选并列，未自动选择且未调用全库向量检索。']
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 125
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
- request_end: 2026-08-11T19:39:19.456
- request_duration_ms: 17
- success: True
- final_source: generation

