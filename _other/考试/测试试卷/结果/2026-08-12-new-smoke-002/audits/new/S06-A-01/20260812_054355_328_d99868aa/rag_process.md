# RAG Process

audit_id: 20260812_054355_328_d99868aa
timestamp: 2026-08-12T05:43:55.329
## Request
- original_query: 天气热，想做一道清爽不腻的晚饭。请推荐知识库中最合适的菜，并说明依据。
- original_query_hash: 972c852ccbacab42
- session_id: 2026-08-12-new-smoke-002:new:S06-A-01
- request_mode: stream
- request_start: 2026-08-12T05:43:55.329
- evaluation_sample_id: 20260812_054355_328_d99868aa
- experiment_id: 2026-08-12-new-smoke-002
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:43:55.329
- end: 2026-08-12T05:43:55.329
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:43:55.330
- end: 2026-08-12T05:43:55.330
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: 972c852ccbacab42

## Event / restricted_vector
- stage: restricted_vector
- status: selected
- start: 2026-08-12T05:43:55.587
- end: 2026-08-12T05:43:55.587
- duration_ms: 0
- parent_count: 5
- vector_scope: all_child_chunks

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 7950
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 0
- text_evidence_count: 5
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
- chunk_count: 1
- redacted_field: 15561
- total_duration_ms: 15564
- fallback_used: False

## Final Output
- answer_chars: 682
- answer_hash: 7b5828487f684d5f
- success: True

## Request Complete
- request_end: 2026-08-12T05:44:11.175
- request_duration_ms: 15846
- success: True
- final_source: generation

