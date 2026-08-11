# RAG Process

audit_id: 20260811_195006_162_acc13138
timestamp: 2026-08-11T19:50:06.162
## Request
- original_query: 做鸭肉相关菜时，知识图谱里有哪些蔬菜搭配？
- original_query_hash: 28c3cddfe4ffa5ef
- session_id: 2026-08-12-真实考试-001:new:S05-B-03
- request_mode: stream
- request_start: 2026-08-11T19:50:06.163
- evaluation_sample_id: 20260811_195006_162_acc13138
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:50:06.164
- end: 2026-08-11T19:50:06.164
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:50:06.164
- end: 2026-08-11T19:50:06.164
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 28c3cddfe4ffa5ef

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:50:06.167
- end: 2026-08-11T19:50:06.167
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-11T19:50:06.167+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:50:06.171
- end: 2026-08-11T19:50:06.171
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-11T19:50:06.167+00:00
- result_count: 5

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:50:06.171
- end: 2026-08-11T19:50:06.171
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- graph_fact_status: verified
- graph_fact_count: 1
- limitations: []
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1893
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 0
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
- chunk_count: 150
- redacted_field: 5973
- total_duration_ms: 9071
- fallback_used: False

## Final Output
- answer_chars: 194
- answer_hash: 67b4fee46fe78e2e
- success: True

## Request Complete
- request_end: 2026-08-11T19:50:15.267
- request_duration_ms: 9103
- success: True
- final_source: generation

