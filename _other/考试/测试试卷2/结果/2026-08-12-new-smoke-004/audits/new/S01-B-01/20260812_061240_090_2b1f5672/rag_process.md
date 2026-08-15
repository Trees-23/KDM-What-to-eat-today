# RAG Process

audit_id: 20260812_061240_090_2b1f5672
timestamp: 2026-08-12T06:12:40.091
## Request
- original_query: 西红柿炒鸡蛋从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 2f75a61622dcdec8
- session_id: 2026-08-12-new-smoke-004:new:S01-B-01
- request_mode: stream
- request_start: 2026-08-12T06:12:40.091
- evaluation_sample_id: 20260812_061240_090_2b1f5672
- experiment_id: 2026-08-12-new-smoke-004
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T06:12:40.091
- end: 2026-08-12T06:12:40.091
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T06:12:40.092
- end: 2026-08-12T06:12:40.092
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 28
- enhanced_query_length: 28
- enhanced_query_hash: 2f75a61622dcdec8

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T06:12:40.102
- end: 2026-08-12T06:12:40.102
- duration_ms: 0
- entity_id: 201005181
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T06:12:40.114
- end: 2026-08-12T06:12:40.114
- duration_ms: 0
- parent_id: 201005181
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct
- stage: entity_direct
- status: selected
- start: 2026-08-12T06:12:40.115
- end: 2026-08-12T06:12:40.115
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
- context_chars: 1151
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
- chunk_count: 483
- redacted_field: 3070
- total_duration_ms: 11854
- fallback_used: False

## Final Output
- answer_chars: 628
- answer_hash: 914a86b92076e5fa
- success: True

## Request Complete
- request_end: 2026-08-12T06:12:51.993
- request_duration_ms: 11902
- success: True
- final_source: generation

