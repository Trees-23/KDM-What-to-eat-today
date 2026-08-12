# RAG Process

audit_id: 20260812_061325_997_16913e2c
timestamp: 2026-08-12T06:13:25.998
## Request
- original_query: 家里有猪肉，知识库里能做哪些菜？
- original_query_hash: bd80c36fa5adad68
- session_id: 2026-08-12-new-smoke-004:new:S04-A-02
- request_mode: stream
- request_start: 2026-08-12T06:13:25.998
- evaluation_sample_id: 20260812_061325_997_16913e2c
- experiment_id: 2026-08-12-new-smoke-004
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T06:13:25.999
- end: 2026-08-12T06:13:25.999
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T06:13:25.999
- end: 2026-08-12T06:13:25.999
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: bd80c36fa5adad68

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T06:13:26.008
- end: 2026-08-12T06:13:26.008
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-12T06:13:26.008+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T06:13:26.030
- end: 2026-08-12T06:13:26.030
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-12T06:13:26.008+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T06:13:26.031
- end: 2026-08-12T06:13:26.031
- duration_ms: 0
- entity_id: 201001780
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T06:13:26.043
- end: 2026-08-12T06:13:26.043
- duration_ms: 0
- parent_id: 201001780
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T06:13:26.044
- end: 2026-08-12T06:13:26.044
- duration_ms: 0
- entity_id: 201003372
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T06:13:26.051
- end: 2026-08-12T06:13:26.051
- duration_ms: 0
- parent_id: 201003372
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T06:13:26.051
- end: 2026-08-12T06:13:26.051
- duration_ms: 0
- entity_id: 201004709
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T06:13:26.058
- end: 2026-08-12T06:13:26.058
- duration_ms: 0
- parent_id: 201004709
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T06:13:26.058
- end: 2026-08-12T06:13:26.058
- duration_ms: 0
- template_id: ingredient_recipes_v1
- graph_fact_status: verified
- graph_fact_count: 1
- limitations: []
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 3751
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 3
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
- chunk_count: 277
- redacted_field: 3019
- total_duration_ms: 8746
- fallback_used: False

## Final Output
- answer_chars: 366
- answer_hash: 2b1e81d06629816e
- success: True

## Request Complete
- request_end: 2026-08-12T06:13:34.849
- request_duration_ms: 8851
- success: True
- final_source: generation

