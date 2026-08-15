# RAG Process

audit_id: 20260813_192657_271_02f396f5
timestamp: 2026-08-13T19:26:57.272
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:26:57.272
- end: 2026-08-13T19:26:57.272
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:27:01.075
- end: 2026-08-13T19:27:01.075
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['鸡蛋'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3802
- attempt_count: 1
- response_hash: 7247ecb61cd6dee2f6c530c6b91fb938f12b529e3b48f86e6f07823d53fba1fe
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:27:01.081
- end: 2026-08-13T19:27:01.081
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 18ba07c3e1078f43f68ee84f8a9497df330f3a1c58bc835c49be86737af797fa
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:27:01.081
- end: 2026-08-13T19:27:01.081
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:27:01.081+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:27:01.086
- end: 2026-08-13T19:27:01.086
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:27:01.081+00:00
- result_count: 50

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.086
- end: 2026-08-13T19:27:01.086
- duration_ms: 0
- entity_id: 201000001
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.093
- end: 2026-08-13T19:27:01.093
- duration_ms: 0
- parent_id: 201000001
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.093
- end: 2026-08-13T19:27:01.093
- duration_ms: 0
- entity_id: 201000290
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.099
- end: 2026-08-13T19:27:01.099
- duration_ms: 0
- parent_id: 201000290
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.099
- end: 2026-08-13T19:27:01.099
- duration_ms: 0
- entity_id: 201000411
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.106
- end: 2026-08-13T19:27:01.106
- duration_ms: 0
- parent_id: 201000411
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.106
- end: 2026-08-13T19:27:01.106
- duration_ms: 0
- entity_id: 201000519
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.112
- end: 2026-08-13T19:27:01.112
- duration_ms: 0
- parent_id: 201000519
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.112
- end: 2026-08-13T19:27:01.112
- duration_ms: 0
- entity_id: 201000539
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.118
- end: 2026-08-13T19:27:01.118
- duration_ms: 0
- parent_id: 201000539
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.118
- end: 2026-08-13T19:27:01.118
- duration_ms: 0
- entity_id: 201000550
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.124
- end: 2026-08-13T19:27:01.124
- duration_ms: 0
- parent_id: 201000550
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.124
- end: 2026-08-13T19:27:01.124
- duration_ms: 0
- entity_id: 201000571
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.130
- end: 2026-08-13T19:27:01.130
- duration_ms: 0
- parent_id: 201000571
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.130
- end: 2026-08-13T19:27:01.130
- duration_ms: 0
- entity_id: 201000605
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.136
- end: 2026-08-13T19:27:01.136
- duration_ms: 0
- parent_id: 201000605
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.136
- end: 2026-08-13T19:27:01.136
- duration_ms: 0
- entity_id: 201000628
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.142
- end: 2026-08-13T19:27:01.142
- duration_ms: 0
- parent_id: 201000628
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.142
- end: 2026-08-13T19:27:01.142
- duration_ms: 0
- entity_id: 201000644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.148
- end: 2026-08-13T19:27:01.148
- duration_ms: 0
- parent_id: 201000644
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.148
- end: 2026-08-13T19:27:01.148
- duration_ms: 0
- entity_id: 201000661
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.154
- end: 2026-08-13T19:27:01.154
- duration_ms: 0
- parent_id: 201000661
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.154
- end: 2026-08-13T19:27:01.154
- duration_ms: 0
- entity_id: 201000670
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.161
- end: 2026-08-13T19:27:01.161
- duration_ms: 0
- parent_id: 201000670
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.161
- end: 2026-08-13T19:27:01.161
- duration_ms: 0
- entity_id: 201000687
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.167
- end: 2026-08-13T19:27:01.167
- duration_ms: 0
- parent_id: 201000687
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.167
- end: 2026-08-13T19:27:01.167
- duration_ms: 0
- entity_id: 201000706
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.175
- end: 2026-08-13T19:27:01.175
- duration_ms: 0
- parent_id: 201000706
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.175
- end: 2026-08-13T19:27:01.175
- duration_ms: 0
- entity_id: 201000730
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.181
- end: 2026-08-13T19:27:01.181
- duration_ms: 0
- parent_id: 201000730
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.181
- end: 2026-08-13T19:27:01.181
- duration_ms: 0
- entity_id: 201000744
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.188
- end: 2026-08-13T19:27:01.188
- duration_ms: 0
- parent_id: 201000744
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.188
- end: 2026-08-13T19:27:01.188
- duration_ms: 0
- entity_id: 201000755
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.194
- end: 2026-08-13T19:27:01.194
- duration_ms: 0
- parent_id: 201000755
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.194
- end: 2026-08-13T19:27:01.194
- duration_ms: 0
- entity_id: 201000922
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.201
- end: 2026-08-13T19:27:01.201
- duration_ms: 0
- parent_id: 201000922
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.201
- end: 2026-08-13T19:27:01.201
- duration_ms: 0
- entity_id: 201000953
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.207
- end: 2026-08-13T19:27:01.207
- duration_ms: 0
- parent_id: 201000953
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.207
- end: 2026-08-13T19:27:01.207
- duration_ms: 0
- entity_id: 201000979
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.213
- end: 2026-08-13T19:27:01.213
- duration_ms: 0
- parent_id: 201000979
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.214
- end: 2026-08-13T19:27:01.214
- duration_ms: 0
- entity_id: 201000999
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.220
- end: 2026-08-13T19:27:01.220
- duration_ms: 0
- parent_id: 201000999
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.220
- end: 2026-08-13T19:27:01.220
- duration_ms: 0
- entity_id: 201001031
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.227
- end: 2026-08-13T19:27:01.227
- duration_ms: 0
- parent_id: 201001031
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.227
- end: 2026-08-13T19:27:01.227
- duration_ms: 0
- entity_id: 201001069
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.233
- end: 2026-08-13T19:27:01.233
- duration_ms: 0
- parent_id: 201001069
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.233
- end: 2026-08-13T19:27:01.233
- duration_ms: 0
- entity_id: 201001122
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.239
- end: 2026-08-13T19:27:01.239
- duration_ms: 0
- parent_id: 201001122
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.240
- end: 2026-08-13T19:27:01.240
- duration_ms: 0
- entity_id: 201001606
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.246
- end: 2026-08-13T19:27:01.246
- duration_ms: 0
- parent_id: 201001606
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.246
- end: 2026-08-13T19:27:01.246
- duration_ms: 0
- entity_id: 201001644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.252
- end: 2026-08-13T19:27:01.252
- duration_ms: 0
- parent_id: 201001644
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.252
- end: 2026-08-13T19:27:01.252
- duration_ms: 0
- entity_id: 201001727
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.258
- end: 2026-08-13T19:27:01.258
- duration_ms: 0
- parent_id: 201001727
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.258
- end: 2026-08-13T19:27:01.258
- duration_ms: 0
- entity_id: 201001916
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.265
- end: 2026-08-13T19:27:01.265
- duration_ms: 0
- parent_id: 201001916
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.265
- end: 2026-08-13T19:27:01.265
- duration_ms: 0
- entity_id: 201001934
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.271
- end: 2026-08-13T19:27:01.271
- duration_ms: 0
- parent_id: 201001934
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.271
- end: 2026-08-13T19:27:01.271
- duration_ms: 0
- entity_id: 201002162
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.278
- end: 2026-08-13T19:27:01.278
- duration_ms: 0
- parent_id: 201002162
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.278
- end: 2026-08-13T19:27:01.278
- duration_ms: 0
- entity_id: 201002179
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.284
- end: 2026-08-13T19:27:01.284
- duration_ms: 0
- parent_id: 201002179
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.284
- end: 2026-08-13T19:27:01.284
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.290
- end: 2026-08-13T19:27:01.290
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.291
- end: 2026-08-13T19:27:01.291
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.297
- end: 2026-08-13T19:27:01.297
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.297
- end: 2026-08-13T19:27:01.297
- duration_ms: 0
- entity_id: 201003138
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.303
- end: 2026-08-13T19:27:01.303
- duration_ms: 0
- parent_id: 201003138
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.303
- end: 2026-08-13T19:27:01.303
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.309
- end: 2026-08-13T19:27:01.309
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.309
- end: 2026-08-13T19:27:01.309
- duration_ms: 0
- entity_id: 201003777
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.315
- end: 2026-08-13T19:27:01.315
- duration_ms: 0
- parent_id: 201003777
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.316
- end: 2026-08-13T19:27:01.316
- duration_ms: 0
- entity_id: 201003844
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.322
- end: 2026-08-13T19:27:01.322
- duration_ms: 0
- parent_id: 201003844
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.322
- end: 2026-08-13T19:27:01.322
- duration_ms: 0
- entity_id: 201003862
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.327
- end: 2026-08-13T19:27:01.327
- duration_ms: 0
- parent_id: 201003862
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.328
- end: 2026-08-13T19:27:01.328
- duration_ms: 0
- entity_id: 201003931
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.333
- end: 2026-08-13T19:27:01.333
- duration_ms: 0
- parent_id: 201003931
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.334
- end: 2026-08-13T19:27:01.334
- duration_ms: 0
- entity_id: 201004017
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.339
- end: 2026-08-13T19:27:01.339
- duration_ms: 0
- parent_id: 201004017
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.339
- end: 2026-08-13T19:27:01.339
- duration_ms: 0
- entity_id: 201004058
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.345
- end: 2026-08-13T19:27:01.345
- duration_ms: 0
- parent_id: 201004058
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.345
- end: 2026-08-13T19:27:01.345
- duration_ms: 0
- entity_id: 201004076
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.352
- end: 2026-08-13T19:27:01.352
- duration_ms: 0
- parent_id: 201004076
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.352
- end: 2026-08-13T19:27:01.352
- duration_ms: 0
- entity_id: 201004088
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.358
- end: 2026-08-13T19:27:01.358
- duration_ms: 0
- parent_id: 201004088
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.358
- end: 2026-08-13T19:27:01.358
- duration_ms: 0
- entity_id: 201004117
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.364
- end: 2026-08-13T19:27:01.364
- duration_ms: 0
- parent_id: 201004117
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.364
- end: 2026-08-13T19:27:01.364
- duration_ms: 0
- entity_id: 201004172
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.372
- end: 2026-08-13T19:27:01.372
- duration_ms: 0
- parent_id: 201004172
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.373
- end: 2026-08-13T19:27:01.373
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.385
- end: 2026-08-13T19:27:01.385
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.385
- end: 2026-08-13T19:27:01.385
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.395
- end: 2026-08-13T19:27:01.395
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.395
- end: 2026-08-13T19:27:01.395
- duration_ms: 0
- entity_id: 201004282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.408
- end: 2026-08-13T19:27:01.408
- duration_ms: 0
- parent_id: 201004282
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.408
- end: 2026-08-13T19:27:01.408
- duration_ms: 0
- entity_id: 201004341
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.419
- end: 2026-08-13T19:27:01.419
- duration_ms: 0
- parent_id: 201004341
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:01.420
- end: 2026-08-13T19:27:01.420
- duration_ms: 0
- entity_id: 201004384
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:01.427
- end: 2026-08-13T19:27:01.427
- duration_ms: 0
- parent_id: 201004384
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 55757
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 13952
- response_chars: 693
- response_hash: c71d21cc8d5825a5

## Final Output
- answer_chars: 693
- answer_hash: c71d21cc8d5825a5
- success: True

## Request Complete
- request_end: 2026-08-13T19:27:15.381
- request_duration_ms: 18109
- success: True
- final_source: generation

