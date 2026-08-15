# RAG Process

audit_id: 20260811_194658_104_120bef34
timestamp: 2026-08-11T19:46:58.105
## Request
- original_query: 我想学煮，它的关键要点和适用场景是什么？
- original_query_hash: 8e54aa9768cf33f7
- session_id: 2026-08-12-真实考试-001:new:S03-B-05
- request_mode: stream
- request_start: 2026-08-11T19:46:58.106
- evaluation_sample_id: 20260811_194658_104_120bef34
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:46:58.107
- end: 2026-08-11T19:46:58.107
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:46:58.108
- end: 2026-08-11T19:46:58.108
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: 8e54aa9768cf33f7

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: not_found
- start: 2026-08-11T19:46:58.124
- end: 2026-08-11T19:46:58.124
- duration_ms: 0
- template_id: None
- graph_fact_status: None
- graph_fact_count: 0
- limitations: ['ENTITY_NOT_FOUND', '未定位到关系查询中的同名实体；未调用全库向量检索。']
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 127
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
- request_end: 2026-08-11T19:46:58.150
- request_duration_ms: 43
- success: True
- final_source: generation

