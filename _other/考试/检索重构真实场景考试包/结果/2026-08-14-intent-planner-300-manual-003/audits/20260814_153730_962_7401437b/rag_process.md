# RAG Process

audit_id: 20260814_153730_962_7401437b
timestamp: 2026-08-14T15:37:30.962
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:37:30.962
- end: 2026-08-14T15:37:30.962
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:37:38.112
- end: 2026-08-14T15:37:38.112
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['鸡蛋'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 7150
- attempt_count: 1
- response_hash: 74c109f590de0d7a6d3b71144a000ba992567387309f9a084682fbd98a557f9d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:37:38.165
- end: 2026-08-14T15:37:38.165
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 18ba07c3e1078f43f68ee84f8a9497df330f3a1c58bc835c49be86737af797fa
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:37:38.166
- end: 2026-08-14T15:37:38.166
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T15:37:38.166+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:37:38.180
- end: 2026-08-14T15:37:38.180
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T15:37:38.166+00:00
- result_count: 50

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.181
- end: 2026-08-14T15:37:38.181
- duration_ms: 0
- entity_id: 201000001
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.204
- end: 2026-08-14T15:37:38.204
- duration_ms: 0
- parent_id: 201000001
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.205
- end: 2026-08-14T15:37:38.205
- duration_ms: 0
- entity_id: 201000290
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.218
- end: 2026-08-14T15:37:38.218
- duration_ms: 0
- parent_id: 201000290
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.218
- end: 2026-08-14T15:37:38.218
- duration_ms: 0
- entity_id: 201000411
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.225
- end: 2026-08-14T15:37:38.225
- duration_ms: 0
- parent_id: 201000411
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.226
- end: 2026-08-14T15:37:38.226
- duration_ms: 0
- entity_id: 201000519
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.232
- end: 2026-08-14T15:37:38.232
- duration_ms: 0
- parent_id: 201000519
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.232
- end: 2026-08-14T15:37:38.232
- duration_ms: 0
- entity_id: 201000539
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.239
- end: 2026-08-14T15:37:38.239
- duration_ms: 0
- parent_id: 201000539
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.239
- end: 2026-08-14T15:37:38.239
- duration_ms: 0
- entity_id: 201000550
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.246
- end: 2026-08-14T15:37:38.246
- duration_ms: 0
- parent_id: 201000550
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.246
- end: 2026-08-14T15:37:38.246
- duration_ms: 0
- entity_id: 201000571
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.254
- end: 2026-08-14T15:37:38.254
- duration_ms: 0
- parent_id: 201000571
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.254
- end: 2026-08-14T15:37:38.254
- duration_ms: 0
- entity_id: 201000605
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.263
- end: 2026-08-14T15:37:38.263
- duration_ms: 0
- parent_id: 201000605
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.263
- end: 2026-08-14T15:37:38.263
- duration_ms: 0
- entity_id: 201000628
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.270
- end: 2026-08-14T15:37:38.270
- duration_ms: 0
- parent_id: 201000628
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.270
- end: 2026-08-14T15:37:38.270
- duration_ms: 0
- entity_id: 201000644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.277
- end: 2026-08-14T15:37:38.277
- duration_ms: 0
- parent_id: 201000644
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.277
- end: 2026-08-14T15:37:38.277
- duration_ms: 0
- entity_id: 201000661
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.283
- end: 2026-08-14T15:37:38.283
- duration_ms: 0
- parent_id: 201000661
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.283
- end: 2026-08-14T15:37:38.283
- duration_ms: 0
- entity_id: 201000670
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.290
- end: 2026-08-14T15:37:38.290
- duration_ms: 0
- parent_id: 201000670
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.291
- end: 2026-08-14T15:37:38.291
- duration_ms: 0
- entity_id: 201000687
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.297
- end: 2026-08-14T15:37:38.297
- duration_ms: 0
- parent_id: 201000687
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.298
- end: 2026-08-14T15:37:38.298
- duration_ms: 0
- entity_id: 201000706
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.304
- end: 2026-08-14T15:37:38.304
- duration_ms: 0
- parent_id: 201000706
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.304
- end: 2026-08-14T15:37:38.304
- duration_ms: 0
- entity_id: 201000730
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.312
- end: 2026-08-14T15:37:38.312
- duration_ms: 0
- parent_id: 201000730
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.312
- end: 2026-08-14T15:37:38.312
- duration_ms: 0
- entity_id: 201000744
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.319
- end: 2026-08-14T15:37:38.319
- duration_ms: 0
- parent_id: 201000744
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.319
- end: 2026-08-14T15:37:38.319
- duration_ms: 0
- entity_id: 201000755
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.328
- end: 2026-08-14T15:37:38.328
- duration_ms: 0
- parent_id: 201000755
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.329
- end: 2026-08-14T15:37:38.329
- duration_ms: 0
- entity_id: 201000922
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.338
- end: 2026-08-14T15:37:38.338
- duration_ms: 0
- parent_id: 201000922
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.338
- end: 2026-08-14T15:37:38.338
- duration_ms: 0
- entity_id: 201000953
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.350
- end: 2026-08-14T15:37:38.350
- duration_ms: 0
- parent_id: 201000953
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.350
- end: 2026-08-14T15:37:38.350
- duration_ms: 0
- entity_id: 201000979
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.358
- end: 2026-08-14T15:37:38.358
- duration_ms: 0
- parent_id: 201000979
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.358
- end: 2026-08-14T15:37:38.358
- duration_ms: 0
- entity_id: 201000999
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.365
- end: 2026-08-14T15:37:38.365
- duration_ms: 0
- parent_id: 201000999
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.365
- end: 2026-08-14T15:37:38.365
- duration_ms: 0
- entity_id: 201001031
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.372
- end: 2026-08-14T15:37:38.372
- duration_ms: 0
- parent_id: 201001031
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.372
- end: 2026-08-14T15:37:38.372
- duration_ms: 0
- entity_id: 201001069
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.380
- end: 2026-08-14T15:37:38.380
- duration_ms: 0
- parent_id: 201001069
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.380
- end: 2026-08-14T15:37:38.380
- duration_ms: 0
- entity_id: 201001122
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.387
- end: 2026-08-14T15:37:38.387
- duration_ms: 0
- parent_id: 201001122
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.388
- end: 2026-08-14T15:37:38.388
- duration_ms: 0
- entity_id: 201001606
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.394
- end: 2026-08-14T15:37:38.394
- duration_ms: 0
- parent_id: 201001606
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.395
- end: 2026-08-14T15:37:38.395
- duration_ms: 0
- entity_id: 201001644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.401
- end: 2026-08-14T15:37:38.401
- duration_ms: 0
- parent_id: 201001644
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.402
- end: 2026-08-14T15:37:38.402
- duration_ms: 0
- entity_id: 201001727
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.408
- end: 2026-08-14T15:37:38.408
- duration_ms: 0
- parent_id: 201001727
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.408
- end: 2026-08-14T15:37:38.408
- duration_ms: 0
- entity_id: 201001916
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.416
- end: 2026-08-14T15:37:38.416
- duration_ms: 0
- parent_id: 201001916
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.416
- end: 2026-08-14T15:37:38.416
- duration_ms: 0
- entity_id: 201001934
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.423
- end: 2026-08-14T15:37:38.423
- duration_ms: 0
- parent_id: 201001934
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.423
- end: 2026-08-14T15:37:38.423
- duration_ms: 0
- entity_id: 201002162
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.431
- end: 2026-08-14T15:37:38.431
- duration_ms: 0
- parent_id: 201002162
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.431
- end: 2026-08-14T15:37:38.431
- duration_ms: 0
- entity_id: 201002179
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.438
- end: 2026-08-14T15:37:38.438
- duration_ms: 0
- parent_id: 201002179
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.438
- end: 2026-08-14T15:37:38.438
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.444
- end: 2026-08-14T15:37:38.444
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.444
- end: 2026-08-14T15:37:38.444
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.451
- end: 2026-08-14T15:37:38.451
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.451
- end: 2026-08-14T15:37:38.451
- duration_ms: 0
- entity_id: 201003138
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.458
- end: 2026-08-14T15:37:38.458
- duration_ms: 0
- parent_id: 201003138
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.458
- end: 2026-08-14T15:37:38.458
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.465
- end: 2026-08-14T15:37:38.465
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.465
- end: 2026-08-14T15:37:38.465
- duration_ms: 0
- entity_id: 201003777
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.473
- end: 2026-08-14T15:37:38.473
- duration_ms: 0
- parent_id: 201003777
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.473
- end: 2026-08-14T15:37:38.473
- duration_ms: 0
- entity_id: 201003844
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.480
- end: 2026-08-14T15:37:38.480
- duration_ms: 0
- parent_id: 201003844
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.480
- end: 2026-08-14T15:37:38.480
- duration_ms: 0
- entity_id: 201003862
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.488
- end: 2026-08-14T15:37:38.488
- duration_ms: 0
- parent_id: 201003862
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.488
- end: 2026-08-14T15:37:38.488
- duration_ms: 0
- entity_id: 201003931
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.495
- end: 2026-08-14T15:37:38.495
- duration_ms: 0
- parent_id: 201003931
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.495
- end: 2026-08-14T15:37:38.495
- duration_ms: 0
- entity_id: 201004017
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.502
- end: 2026-08-14T15:37:38.502
- duration_ms: 0
- parent_id: 201004017
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.503
- end: 2026-08-14T15:37:38.503
- duration_ms: 0
- entity_id: 201004058
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.509
- end: 2026-08-14T15:37:38.509
- duration_ms: 0
- parent_id: 201004058
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.510
- end: 2026-08-14T15:37:38.510
- duration_ms: 0
- entity_id: 201004076
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.516
- end: 2026-08-14T15:37:38.516
- duration_ms: 0
- parent_id: 201004076
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.517
- end: 2026-08-14T15:37:38.517
- duration_ms: 0
- entity_id: 201004088
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.523
- end: 2026-08-14T15:37:38.523
- duration_ms: 0
- parent_id: 201004088
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.524
- end: 2026-08-14T15:37:38.524
- duration_ms: 0
- entity_id: 201004117
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.530
- end: 2026-08-14T15:37:38.530
- duration_ms: 0
- parent_id: 201004117
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.530
- end: 2026-08-14T15:37:38.530
- duration_ms: 0
- entity_id: 201004172
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.537
- end: 2026-08-14T15:37:38.537
- duration_ms: 0
- parent_id: 201004172
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.537
- end: 2026-08-14T15:37:38.537
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.544
- end: 2026-08-14T15:37:38.544
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.544
- end: 2026-08-14T15:37:38.544
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.551
- end: 2026-08-14T15:37:38.551
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.551
- end: 2026-08-14T15:37:38.551
- duration_ms: 0
- entity_id: 201004282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.558
- end: 2026-08-14T15:37:38.558
- duration_ms: 0
- parent_id: 201004282
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.558
- end: 2026-08-14T15:37:38.558
- duration_ms: 0
- entity_id: 201004341
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.565
- end: 2026-08-14T15:37:38.565
- duration_ms: 0
- parent_id: 201004341
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:37:38.565
- end: 2026-08-14T15:37:38.565
- duration_ms: 0
- entity_id: 201004384
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:37:38.577
- end: 2026-08-14T15:37:38.576
- duration_ms: 0
- parent_id: 201004384
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 55761
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 50
- limitation_count: 0
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Generation Config
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 24688
- response_chars: 787
- response_hash: c08d4d9979fda61d

## Final Output
- answer_chars: 787
- answer_hash: c08d4d9979fda61d
- success: True

## Request Complete
- request_end: 2026-08-14T15:38:03.268
- request_duration_ms: 32305
- success: True
- final_source: generation

