# RAG Process

audit_id: 20260812_055009_906_b8c5479f
timestamp: 2026-08-12T05:50:09.906
## Request
- original_query: 家里有牛肉，知识库里能做哪些菜？
- original_query_hash: d6b623295d0d1c45
- session_id: 2026-08-12-new-smoke-003:new:S04-A-01
- request_mode: stream
- request_start: 2026-08-12T05:50:09.907
- evaluation_sample_id: 20260812_055009_906_b8c5479f
- experiment_id: 2026-08-12-new-smoke-003
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T05:50:09.907
- end: 2026-08-12T05:50:09.907
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T05:50:09.907
- end: 2026-08-12T05:50:09.907
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: d6b623295d0d1c45

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T05:50:09.911
- end: 2026-08-12T05:50:09.911
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-12T05:50:09.911+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-12T05:50:09.913
- end: 2026-08-12T05:50:09.913
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-12T05:50:09.911+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:50:09.913
- end: 2026-08-12T05:50:09.913
- duration_ms: 0
- entity_id: 201001630
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:50:09.921
- end: 2026-08-12T05:50:09.921
- duration_ms: 0
- parent_id: 201001630
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:50:09.921
- end: 2026-08-12T05:50:09.921
- duration_ms: 0
- entity_id: 201002555
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:50:09.927
- end: 2026-08-12T05:50:09.927
- duration_ms: 0
- parent_id: 201002555
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:50:09.928
- end: 2026-08-12T05:50:09.928
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:50:09.934
- end: 2026-08-12T05:50:09.934
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:50:09.934
- end: 2026-08-12T05:50:09.934
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:50:09.941
- end: 2026-08-12T05:50:09.941
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-12T05:50:09.941
- end: 2026-08-12T05:50:09.941
- duration_ms: 0
- entity_id: 201003314
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-12T05:50:09.948
- end: 2026-08-12T05:50:09.948
- duration_ms: 0
- parent_id: 201003314
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-12T05:50:09.948
- end: 2026-08-12T05:50:09.948
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
- chunk_count: 302
- redacted_field: 5757
- total_duration_ms: 12761
- fallback_used: False

## Final Output
- answer_chars: 393
- answer_hash: 0fdc402d49dca156
- success: True

## Request Complete
- request_end: 2026-08-12T05:50:22.720
- request_duration_ms: 12813
- success: True
- final_source: generation

