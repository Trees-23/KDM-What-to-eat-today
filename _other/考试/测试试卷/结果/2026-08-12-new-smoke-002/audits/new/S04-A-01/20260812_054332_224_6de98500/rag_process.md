# RAG Process

audit_id: 20260812_054332_224_6de98500
timestamp: 2026-08-12T05:43:32.224
## Request
- original_query: 家里有牛肉，知识库里能做哪些菜？
- original_query_hash: d6b623295d0d1c45
- session_id: 2026-08-12-new-smoke-002:new:S04-A-01
- request_mode: stream
- request_start: 2026-08-12T05:43:32.224
- evaluation_sample_id: 20260812_054332_224_6de98500
- experiment_id: 2026-08-12-new-smoke-002
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:43:32.225
- end: 2026-08-12T05:43:32.225
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:43:32.225
- end: 2026-08-12T05:43:32.225
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: d6b623295d0d1c45

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:43:32.229
- end: 2026-08-12T05:43:32.229
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-12T05:43:32.229+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T05:43:32.232
- end: 2026-08-12T05:43:32.232
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-12T05:43:32.229+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:43:32.232
- end: 2026-08-12T05:43:32.232
- duration_ms: 0
- entity_id: 201001630
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:43:32.240
- end: 2026-08-12T05:43:32.240
- duration_ms: 0
- parent_id: 201001630
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:43:32.240
- end: 2026-08-12T05:43:32.240
- duration_ms: 0
- entity_id: 201002555
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:43:32.246
- end: 2026-08-12T05:43:32.246
- duration_ms: 0
- parent_id: 201002555
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:43:32.246
- end: 2026-08-12T05:43:32.246
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:43:32.252
- end: 2026-08-12T05:43:32.252
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:43:32.252
- end: 2026-08-12T05:43:32.252
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:43:32.258
- end: 2026-08-12T05:43:32.258
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:43:32.259
- end: 2026-08-12T05:43:32.259
- duration_ms: 0
- entity_id: 201003314
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:43:32.265
- end: 2026-08-12T05:43:32.265
- duration_ms: 0
- parent_id: 201003314
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T05:43:32.265
- end: 2026-08-12T05:43:32.265
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
- context_chars: 6627
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 1
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
- redacted_field: 16090
- total_duration_ms: 16092
- fallback_used: False

## Final Output
- answer_chars: 478
- answer_hash: 26f2db6cea6abc94
- success: True

## Request Complete
- request_end: 2026-08-12T05:43:48.378
- request_duration_ms: 16154
- success: True
- final_source: generation

