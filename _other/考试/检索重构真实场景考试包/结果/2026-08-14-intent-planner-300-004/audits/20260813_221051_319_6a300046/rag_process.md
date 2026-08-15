# RAG Process

audit_id: 20260813_221051_319_6a300046
timestamp: 2026-08-13T22:10:51.320
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:10:51.321
- end: 2026-08-13T22:10:51.321
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:10:54.916
- end: 2026-08-13T22:10:54.916
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3595
- attempt_count: 1
- response_hash: 74d82ed308a5d97886a00ce037eba6a8058fd1e5c4f64299888a7fa3990f90e8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:10:54.921
- end: 2026-08-13T22:10:54.921
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 18ba07c3e1078f43f68ee84f8a9497df330f3a1c58bc835c49be86737af797fa
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:10:54.922
- end: 2026-08-13T22:10:54.922
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:10:54.922+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:10:54.929
- end: 2026-08-13T22:10:54.929
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:10:54.922+00:00
- result_count: 50

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:54.929
- end: 2026-08-13T22:10:54.929
- duration_ms: 0
- entity_id: 201000001
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:54.940
- end: 2026-08-13T22:10:54.940
- duration_ms: 0
- parent_id: 201000001
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:54.940
- end: 2026-08-13T22:10:54.940
- duration_ms: 0
- entity_id: 201000290
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:54.947
- end: 2026-08-13T22:10:54.947
- duration_ms: 0
- parent_id: 201000290
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:54.947
- end: 2026-08-13T22:10:54.947
- duration_ms: 0
- entity_id: 201000411
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:54.954
- end: 2026-08-13T22:10:54.954
- duration_ms: 0
- parent_id: 201000411
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:54.954
- end: 2026-08-13T22:10:54.954
- duration_ms: 0
- entity_id: 201000519
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:54.963
- end: 2026-08-13T22:10:54.963
- duration_ms: 0
- parent_id: 201000519
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:54.964
- end: 2026-08-13T22:10:54.964
- duration_ms: 0
- entity_id: 201000539
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:54.971
- end: 2026-08-13T22:10:54.971
- duration_ms: 0
- parent_id: 201000539
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:54.971
- end: 2026-08-13T22:10:54.971
- duration_ms: 0
- entity_id: 201000550
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:54.979
- end: 2026-08-13T22:10:54.979
- duration_ms: 0
- parent_id: 201000550
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:54.979
- end: 2026-08-13T22:10:54.979
- duration_ms: 0
- entity_id: 201000571
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:54.987
- end: 2026-08-13T22:10:54.987
- duration_ms: 0
- parent_id: 201000571
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:54.987
- end: 2026-08-13T22:10:54.987
- duration_ms: 0
- entity_id: 201000605
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:54.993
- end: 2026-08-13T22:10:54.993
- duration_ms: 0
- parent_id: 201000605
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:54.994
- end: 2026-08-13T22:10:54.994
- duration_ms: 0
- entity_id: 201000628
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.002
- end: 2026-08-13T22:10:55.002
- duration_ms: 0
- parent_id: 201000628
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.002
- end: 2026-08-13T22:10:55.002
- duration_ms: 0
- entity_id: 201000644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.011
- end: 2026-08-13T22:10:55.011
- duration_ms: 0
- parent_id: 201000644
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.012
- end: 2026-08-13T22:10:55.012
- duration_ms: 0
- entity_id: 201000661
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.021
- end: 2026-08-13T22:10:55.021
- duration_ms: 0
- parent_id: 201000661
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.021
- end: 2026-08-13T22:10:55.021
- duration_ms: 0
- entity_id: 201000670
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.028
- end: 2026-08-13T22:10:55.028
- duration_ms: 0
- parent_id: 201000670
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.028
- end: 2026-08-13T22:10:55.028
- duration_ms: 0
- entity_id: 201000687
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.035
- end: 2026-08-13T22:10:55.035
- duration_ms: 0
- parent_id: 201000687
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.035
- end: 2026-08-13T22:10:55.035
- duration_ms: 0
- entity_id: 201000706
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.042
- end: 2026-08-13T22:10:55.042
- duration_ms: 0
- parent_id: 201000706
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.042
- end: 2026-08-13T22:10:55.042
- duration_ms: 0
- entity_id: 201000730
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.050
- end: 2026-08-13T22:10:55.050
- duration_ms: 0
- parent_id: 201000730
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.050
- end: 2026-08-13T22:10:55.050
- duration_ms: 0
- entity_id: 201000744
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.056
- end: 2026-08-13T22:10:55.056
- duration_ms: 0
- parent_id: 201000744
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.056
- end: 2026-08-13T22:10:55.056
- duration_ms: 0
- entity_id: 201000755
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.063
- end: 2026-08-13T22:10:55.063
- duration_ms: 0
- parent_id: 201000755
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.063
- end: 2026-08-13T22:10:55.063
- duration_ms: 0
- entity_id: 201000922
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.069
- end: 2026-08-13T22:10:55.069
- duration_ms: 0
- parent_id: 201000922
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.069
- end: 2026-08-13T22:10:55.069
- duration_ms: 0
- entity_id: 201000953
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.076
- end: 2026-08-13T22:10:55.076
- duration_ms: 0
- parent_id: 201000953
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.076
- end: 2026-08-13T22:10:55.076
- duration_ms: 0
- entity_id: 201000979
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.082
- end: 2026-08-13T22:10:55.082
- duration_ms: 0
- parent_id: 201000979
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.082
- end: 2026-08-13T22:10:55.082
- duration_ms: 0
- entity_id: 201000999
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.088
- end: 2026-08-13T22:10:55.088
- duration_ms: 0
- parent_id: 201000999
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.089
- end: 2026-08-13T22:10:55.089
- duration_ms: 0
- entity_id: 201001031
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.095
- end: 2026-08-13T22:10:55.095
- duration_ms: 0
- parent_id: 201001031
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.095
- end: 2026-08-13T22:10:55.095
- duration_ms: 0
- entity_id: 201001069
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.104
- end: 2026-08-13T22:10:55.104
- duration_ms: 0
- parent_id: 201001069
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.104
- end: 2026-08-13T22:10:55.104
- duration_ms: 0
- entity_id: 201001122
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.114
- end: 2026-08-13T22:10:55.114
- duration_ms: 0
- parent_id: 201001122
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.114
- end: 2026-08-13T22:10:55.114
- duration_ms: 0
- entity_id: 201001606
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.124
- end: 2026-08-13T22:10:55.124
- duration_ms: 0
- parent_id: 201001606
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.124
- end: 2026-08-13T22:10:55.124
- duration_ms: 0
- entity_id: 201001644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.133
- end: 2026-08-13T22:10:55.133
- duration_ms: 0
- parent_id: 201001644
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.133
- end: 2026-08-13T22:10:55.133
- duration_ms: 0
- entity_id: 201001727
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.143
- end: 2026-08-13T22:10:55.143
- duration_ms: 0
- parent_id: 201001727
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.143
- end: 2026-08-13T22:10:55.143
- duration_ms: 0
- entity_id: 201001916
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.152
- end: 2026-08-13T22:10:55.152
- duration_ms: 0
- parent_id: 201001916
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.153
- end: 2026-08-13T22:10:55.153
- duration_ms: 0
- entity_id: 201001934
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.159
- end: 2026-08-13T22:10:55.159
- duration_ms: 0
- parent_id: 201001934
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.159
- end: 2026-08-13T22:10:55.159
- duration_ms: 0
- entity_id: 201002162
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.165
- end: 2026-08-13T22:10:55.165
- duration_ms: 0
- parent_id: 201002162
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.165
- end: 2026-08-13T22:10:55.165
- duration_ms: 0
- entity_id: 201002179
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.171
- end: 2026-08-13T22:10:55.171
- duration_ms: 0
- parent_id: 201002179
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.172
- end: 2026-08-13T22:10:55.172
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.178
- end: 2026-08-13T22:10:55.178
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.178
- end: 2026-08-13T22:10:55.178
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.184
- end: 2026-08-13T22:10:55.184
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.184
- end: 2026-08-13T22:10:55.184
- duration_ms: 0
- entity_id: 201003138
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.192
- end: 2026-08-13T22:10:55.192
- duration_ms: 0
- parent_id: 201003138
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.192
- end: 2026-08-13T22:10:55.192
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.202
- end: 2026-08-13T22:10:55.202
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.203
- end: 2026-08-13T22:10:55.203
- duration_ms: 0
- entity_id: 201003777
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.215
- end: 2026-08-13T22:10:55.215
- duration_ms: 0
- parent_id: 201003777
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.216
- end: 2026-08-13T22:10:55.216
- duration_ms: 0
- entity_id: 201003844
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.228
- end: 2026-08-13T22:10:55.228
- duration_ms: 0
- parent_id: 201003844
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.229
- end: 2026-08-13T22:10:55.229
- duration_ms: 0
- entity_id: 201003862
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.240
- end: 2026-08-13T22:10:55.240
- duration_ms: 0
- parent_id: 201003862
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.240
- end: 2026-08-13T22:10:55.240
- duration_ms: 0
- entity_id: 201003931
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.252
- end: 2026-08-13T22:10:55.252
- duration_ms: 0
- parent_id: 201003931
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.253
- end: 2026-08-13T22:10:55.253
- duration_ms: 0
- entity_id: 201004017
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.267
- end: 2026-08-13T22:10:55.267
- duration_ms: 0
- parent_id: 201004017
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.267
- end: 2026-08-13T22:10:55.267
- duration_ms: 0
- entity_id: 201004058
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.277
- end: 2026-08-13T22:10:55.277
- duration_ms: 0
- parent_id: 201004058
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.277
- end: 2026-08-13T22:10:55.277
- duration_ms: 0
- entity_id: 201004076
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.285
- end: 2026-08-13T22:10:55.285
- duration_ms: 0
- parent_id: 201004076
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.285
- end: 2026-08-13T22:10:55.285
- duration_ms: 0
- entity_id: 201004088
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.291
- end: 2026-08-13T22:10:55.291
- duration_ms: 0
- parent_id: 201004088
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.292
- end: 2026-08-13T22:10:55.292
- duration_ms: 0
- entity_id: 201004117
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.298
- end: 2026-08-13T22:10:55.298
- duration_ms: 0
- parent_id: 201004117
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.298
- end: 2026-08-13T22:10:55.298
- duration_ms: 0
- entity_id: 201004172
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.304
- end: 2026-08-13T22:10:55.304
- duration_ms: 0
- parent_id: 201004172
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.305
- end: 2026-08-13T22:10:55.305
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.311
- end: 2026-08-13T22:10:55.311
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.312
- end: 2026-08-13T22:10:55.312
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.318
- end: 2026-08-13T22:10:55.318
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.319
- end: 2026-08-13T22:10:55.319
- duration_ms: 0
- entity_id: 201004282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.325
- end: 2026-08-13T22:10:55.325
- duration_ms: 0
- parent_id: 201004282
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.325
- end: 2026-08-13T22:10:55.325
- duration_ms: 0
- entity_id: 201004341
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.332
- end: 2026-08-13T22:10:55.332
- duration_ms: 0
- parent_id: 201004341
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:55.332
- end: 2026-08-13T22:10:55.332
- duration_ms: 0
- entity_id: 201004384
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:55.338
- end: 2026-08-13T22:10:55.338
- duration_ms: 0
- parent_id: 201004384
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 55758
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
- duration_ms: 16024
- response_chars: 703
- response_hash: c90be0da8abf2df3

## Final Output
- answer_chars: 703
- answer_hash: c90be0da8abf2df3
- success: True

## Request Complete
- request_end: 2026-08-13T22:11:11.364
- request_duration_ms: 20043
- success: True
- final_source: generation

