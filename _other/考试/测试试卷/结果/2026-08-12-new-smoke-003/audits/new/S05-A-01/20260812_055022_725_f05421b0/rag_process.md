# RAG Process

audit_id: 20260812_055022_725_f05421b0
timestamp: 2026-08-12T05:50:22.726
## Request
- original_query: 牛肉适合搭配什么蔬菜？
- original_query_hash: 1b8dadc5fd66eafa
- session_id: 2026-08-12-new-smoke-003:new:S05-A-01
- request_mode: stream
- request_start: 2026-08-12T05:50:22.726
- evaluation_sample_id: 20260812_055022_725_f05421b0
- experiment_id: 2026-08-12-new-smoke-003
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:50:22.726
- end: 2026-08-12T05:50:22.726
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:50:22.727
- end: 2026-08-12T05:50:22.727
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 11
- enhanced_query_length: 11
- enhanced_query_hash: 1b8dadc5fd66eafa

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:50:22.730
- end: 2026-08-12T05:50:22.730
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-12T05:50:22.730+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T05:50:22.733
- end: 2026-08-12T05:50:22.733
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-12T05:50:22.730+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:50:22.733
- end: 2026-08-12T05:50:22.733
- duration_ms: 0
- entity_id: 201001630
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:50:22.740
- end: 2026-08-12T05:50:22.740
- duration_ms: 0
- parent_id: 201001630
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:50:22.741
- end: 2026-08-12T05:50:22.741
- duration_ms: 0
- entity_id: 201002555
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:50:22.747
- end: 2026-08-12T05:50:22.747
- duration_ms: 0
- parent_id: 201002555
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T05:50:22.747
- end: 2026-08-12T05:50:22.747
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
- chunk_count: 245
- redacted_field: 1869
- total_duration_ms: 7210
- fallback_used: False

## Final Output
- answer_chars: 302
- answer_hash: 9d8638fc22b78968
- success: True

## Request Complete
- request_end: 2026-08-12T05:50:29.971
- request_duration_ms: 7245
- success: True
- final_source: generation

