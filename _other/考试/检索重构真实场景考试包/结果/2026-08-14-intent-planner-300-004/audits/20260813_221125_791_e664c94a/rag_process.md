# RAG Process

audit_id: 20260813_221125_791_e664c94a
timestamp: 2026-08-13T22:11:25.791
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:11:25.791
- end: 2026-08-13T22:11:25.791
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:11:29.292
- end: 2026-08-13T22:11:29.292
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3501
- attempt_count: 1
- response_hash: 48acd9bfa389518bb6650d59adba69d5384c9a95a49670657526d467a6117824
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:11:29.295
- end: 2026-08-13T22:11:29.295
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 0c4d511ef3bb366ebc11daa4919872543eb40da4eda5a78aa74eb53b4f1aefba
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:11:29.295
- end: 2026-08-13T22:11:29.295
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:11:29.295+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:11:29.298
- end: 2026-08-13T22:11:29.298
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:11:29.295+00:00
- result_count: 16

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.298
- end: 2026-08-13T22:11:29.298
- duration_ms: 0
- entity_id: 201001891
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.305
- end: 2026-08-13T22:11:29.305
- duration_ms: 0
- parent_id: 201001891
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.306
- end: 2026-08-13T22:11:29.306
- duration_ms: 0
- entity_id: 201002122
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.313
- end: 2026-08-13T22:11:29.313
- duration_ms: 0
- parent_id: 201002122
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.313
- end: 2026-08-13T22:11:29.313
- duration_ms: 0
- entity_id: 201002309
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.319
- end: 2026-08-13T22:11:29.319
- duration_ms: 0
- parent_id: 201002309
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.320
- end: 2026-08-13T22:11:29.320
- duration_ms: 0
- entity_id: 201002369
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.326
- end: 2026-08-13T22:11:29.326
- duration_ms: 0
- parent_id: 201002369
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.326
- end: 2026-08-13T22:11:29.326
- duration_ms: 0
- entity_id: 201002575
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.332
- end: 2026-08-13T22:11:29.332
- duration_ms: 0
- parent_id: 201002575
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.332
- end: 2026-08-13T22:11:29.332
- duration_ms: 0
- entity_id: 201002647
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.339
- end: 2026-08-13T22:11:29.339
- duration_ms: 0
- parent_id: 201002647
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.339
- end: 2026-08-13T22:11:29.339
- duration_ms: 0
- entity_id: 201002920
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.345
- end: 2026-08-13T22:11:29.345
- duration_ms: 0
- parent_id: 201002920
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.346
- end: 2026-08-13T22:11:29.346
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.353
- end: 2026-08-13T22:11:29.353
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.353
- end: 2026-08-13T22:11:29.353
- duration_ms: 0
- entity_id: 201003275
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.362
- end: 2026-08-13T22:11:29.362
- duration_ms: 0
- parent_id: 201003275
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.363
- end: 2026-08-13T22:11:29.363
- duration_ms: 0
- entity_id: 201003355
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.373
- end: 2026-08-13T22:11:29.373
- duration_ms: 0
- parent_id: 201003355
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.373
- end: 2026-08-13T22:11:29.373
- duration_ms: 0
- entity_id: 201004525
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.380
- end: 2026-08-13T22:11:29.380
- duration_ms: 0
- parent_id: 201004525
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.381
- end: 2026-08-13T22:11:29.381
- duration_ms: 0
- entity_id: 201004898
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.388
- end: 2026-08-13T22:11:29.388
- duration_ms: 0
- parent_id: 201004898
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.388
- end: 2026-08-13T22:11:29.388
- duration_ms: 0
- entity_id: 201005092
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.396
- end: 2026-08-13T22:11:29.396
- duration_ms: 0
- parent_id: 201005092
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.396
- end: 2026-08-13T22:11:29.396
- duration_ms: 0
- entity_id: 201005195
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.407
- end: 2026-08-13T22:11:29.407
- duration_ms: 0
- parent_id: 201005195
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.408
- end: 2026-08-13T22:11:29.408
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.415
- end: 2026-08-13T22:11:29.415
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:29.415
- end: 2026-08-13T22:11:29.415
- duration_ms: 0
- entity_id: 201005422
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:29.421
- end: 2026-08-13T22:11:29.421
- duration_ms: 0
- parent_id: 201005422
- build_id: pds_8ed95d0ee2ef5e64d703abd6
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
- duration_ms: 12973
- response_chars: 556
- response_hash: 039d6544d3cfaf82

## Final Output
- answer_chars: 556
- answer_hash: 039d6544d3cfaf82
- success: True

## Request Complete
- request_end: 2026-08-13T22:11:42.396
- request_duration_ms: 16605
- success: True
- final_source: generation

