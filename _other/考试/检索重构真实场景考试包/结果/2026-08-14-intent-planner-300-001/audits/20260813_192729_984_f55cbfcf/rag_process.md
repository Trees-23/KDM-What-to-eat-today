# RAG Process

audit_id: 20260813_192729_984_f55cbfcf
timestamp: 2026-08-13T19:27:29.984
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:27:29.985
- end: 2026-08-13T19:27:29.985
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:27:33.833
- end: 2026-08-13T19:27:33.833
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['土豆'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3848
- attempt_count: 1
- response_hash: a7982b147ffd761a30b083f1f010a1e1050ac60c1e8bc78b186508f67ab41a7b
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:27:33.840
- end: 2026-08-13T19:27:33.840
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 0c4d511ef3bb366ebc11daa4919872543eb40da4eda5a78aa74eb53b4f1aefba
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:27:33.840
- end: 2026-08-13T19:27:33.840
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:27:33.840+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:27:33.845
- end: 2026-08-13T19:27:33.845
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:27:33.840+00:00
- result_count: 16

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.845
- end: 2026-08-13T19:27:33.845
- duration_ms: 0
- entity_id: 201001891
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.859
- end: 2026-08-13T19:27:33.859
- duration_ms: 0
- parent_id: 201001891
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.859
- end: 2026-08-13T19:27:33.859
- duration_ms: 0
- entity_id: 201002122
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.872
- end: 2026-08-13T19:27:33.872
- duration_ms: 0
- parent_id: 201002122
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.872
- end: 2026-08-13T19:27:33.872
- duration_ms: 0
- entity_id: 201002309
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.884
- end: 2026-08-13T19:27:33.884
- duration_ms: 0
- parent_id: 201002309
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.885
- end: 2026-08-13T19:27:33.885
- duration_ms: 0
- entity_id: 201002369
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.898
- end: 2026-08-13T19:27:33.898
- duration_ms: 0
- parent_id: 201002369
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.898
- end: 2026-08-13T19:27:33.898
- duration_ms: 0
- entity_id: 201002575
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.912
- end: 2026-08-13T19:27:33.912
- duration_ms: 0
- parent_id: 201002575
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.913
- end: 2026-08-13T19:27:33.913
- duration_ms: 0
- entity_id: 201002647
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.924
- end: 2026-08-13T19:27:33.924
- duration_ms: 0
- parent_id: 201002647
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.925
- end: 2026-08-13T19:27:33.925
- duration_ms: 0
- entity_id: 201002920
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.935
- end: 2026-08-13T19:27:33.935
- duration_ms: 0
- parent_id: 201002920
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.935
- end: 2026-08-13T19:27:33.935
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.944
- end: 2026-08-13T19:27:33.944
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.945
- end: 2026-08-13T19:27:33.945
- duration_ms: 0
- entity_id: 201003275
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.951
- end: 2026-08-13T19:27:33.951
- duration_ms: 0
- parent_id: 201003275
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.951
- end: 2026-08-13T19:27:33.951
- duration_ms: 0
- entity_id: 201003355
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.958
- end: 2026-08-13T19:27:33.958
- duration_ms: 0
- parent_id: 201003355
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.958
- end: 2026-08-13T19:27:33.958
- duration_ms: 0
- entity_id: 201004525
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.966
- end: 2026-08-13T19:27:33.966
- duration_ms: 0
- parent_id: 201004525
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.967
- end: 2026-08-13T19:27:33.967
- duration_ms: 0
- entity_id: 201004898
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.974
- end: 2026-08-13T19:27:33.974
- duration_ms: 0
- parent_id: 201004898
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.974
- end: 2026-08-13T19:27:33.974
- duration_ms: 0
- entity_id: 201005092
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.981
- end: 2026-08-13T19:27:33.981
- duration_ms: 0
- parent_id: 201005092
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.981
- end: 2026-08-13T19:27:33.981
- duration_ms: 0
- entity_id: 201005195
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.987
- end: 2026-08-13T19:27:33.987
- duration_ms: 0
- parent_id: 201005195
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.987
- end: 2026-08-13T19:27:33.987
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:33.994
- end: 2026-08-13T19:27:33.994
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:33.994
- end: 2026-08-13T19:27:33.994
- duration_ms: 0
- entity_id: 201005422
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:34.000
- end: 2026-08-13T19:27:34.000
- duration_ms: 0
- parent_id: 201005422
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 20976
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 16
- limitation_count: 0
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Generation Config
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 8873
- response_chars: 358
- response_hash: 5ba58349e8370312

## Final Output
- answer_chars: 358
- answer_hash: 5ba58349e8370312
- success: True

## Request Complete
- request_end: 2026-08-13T19:27:42.875
- request_duration_ms: 12890
- success: True
- final_source: generation

