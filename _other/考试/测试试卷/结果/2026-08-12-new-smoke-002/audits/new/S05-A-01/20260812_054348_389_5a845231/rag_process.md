# RAG Process

audit_id: 20260812_054348_389_5a845231
timestamp: 2026-08-12T05:43:48.390
## Request
- original_query: 牛肉适合搭配什么蔬菜？
- original_query_hash: 1b8dadc5fd66eafa
- session_id: 2026-08-12-new-smoke-002:new:S05-A-01
- request_mode: stream
- request_start: 2026-08-12T05:43:48.390
- evaluation_sample_id: 20260812_054348_389_5a845231
- experiment_id: 2026-08-12-new-smoke-002
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:43:48.391
- end: 2026-08-12T05:43:48.391
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:43:48.391
- end: 2026-08-12T05:43:48.391
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 11
- enhanced_query_length: 11
- enhanced_query_hash: 1b8dadc5fd66eafa

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:43:48.399
- end: 2026-08-12T05:43:48.399
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-12T05:43:48.399+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T05:43:48.404
- end: 2026-08-12T05:43:48.404
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-12T05:43:48.399+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:43:48.405
- end: 2026-08-12T05:43:48.405
- duration_ms: 0
- entity_id: 201001630
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:43:48.418
- end: 2026-08-12T05:43:48.418
- duration_ms: 0
- parent_id: 201001630
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:43:48.418
- end: 2026-08-12T05:43:48.418
- duration_ms: 0
- entity_id: 201002555
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:43:48.430
- end: 2026-08-12T05:43:48.430
- duration_ms: 0
- parent_id: 201002555
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T05:43:48.431
- end: 2026-08-12T05:43:48.431
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
- context_chars: 3772
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 2
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
- chunk_count: 211
- redacted_field: 2505
- total_duration_ms: 6857
- fallback_used: False

## Final Output
- answer_chars: 261
- answer_hash: 4f9339eb3e5e5e3d
- success: True

## Request Complete
- request_end: 2026-08-12T05:43:55.297
- request_duration_ms: 6907
- success: True
- final_source: generation

