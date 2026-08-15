# RAG Process

audit_id: 20260814_203613_131_923ee077
timestamp: 2026-08-14T20:36:13.131
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:36:13.132
- end: 2026-08-14T20:36:13.132
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:36:16.784
- end: 2026-08-14T20:36:16.784
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.94
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['鸡蛋'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3652
- attempt_count: 1
- response_hash: 36357fd36d8099dc4403d6957310ae5cdf7fda024e2bf67b1bee19ae97540047
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:36:16.794
- end: 2026-08-14T20:36:16.794
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 18ba07c3e1078f43f68ee84f8a9497df330f3a1c58bc835c49be86737af797fa
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:36:16.794
- end: 2026-08-14T20:36:16.794
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:36:16.794+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:36:16.806
- end: 2026-08-14T20:36:16.806
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:36:16.794+00:00
- result_count: 50

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.806
- end: 2026-08-14T20:36:16.806
- duration_ms: 0
- entity_id: 201000001
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.813
- end: 2026-08-14T20:36:16.813
- duration_ms: 0
- parent_id: 201000001
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.813
- end: 2026-08-14T20:36:16.813
- duration_ms: 0
- entity_id: 201000290
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.819
- end: 2026-08-14T20:36:16.819
- duration_ms: 0
- parent_id: 201000290
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.819
- end: 2026-08-14T20:36:16.819
- duration_ms: 0
- entity_id: 201000411
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.825
- end: 2026-08-14T20:36:16.825
- duration_ms: 0
- parent_id: 201000411
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.825
- end: 2026-08-14T20:36:16.825
- duration_ms: 0
- entity_id: 201000519
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.831
- end: 2026-08-14T20:36:16.831
- duration_ms: 0
- parent_id: 201000519
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.831
- end: 2026-08-14T20:36:16.831
- duration_ms: 0
- entity_id: 201000539
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.837
- end: 2026-08-14T20:36:16.837
- duration_ms: 0
- parent_id: 201000539
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.837
- end: 2026-08-14T20:36:16.837
- duration_ms: 0
- entity_id: 201000550
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.843
- end: 2026-08-14T20:36:16.843
- duration_ms: 0
- parent_id: 201000550
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.843
- end: 2026-08-14T20:36:16.843
- duration_ms: 0
- entity_id: 201000571
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.849
- end: 2026-08-14T20:36:16.849
- duration_ms: 0
- parent_id: 201000571
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.849
- end: 2026-08-14T20:36:16.849
- duration_ms: 0
- entity_id: 201000605
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.855
- end: 2026-08-14T20:36:16.855
- duration_ms: 0
- parent_id: 201000605
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.855
- end: 2026-08-14T20:36:16.855
- duration_ms: 0
- entity_id: 201000628
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.862
- end: 2026-08-14T20:36:16.862
- duration_ms: 0
- parent_id: 201000628
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.862
- end: 2026-08-14T20:36:16.862
- duration_ms: 0
- entity_id: 201000644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.869
- end: 2026-08-14T20:36:16.869
- duration_ms: 0
- parent_id: 201000644
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.869
- end: 2026-08-14T20:36:16.869
- duration_ms: 0
- entity_id: 201000661
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.875
- end: 2026-08-14T20:36:16.875
- duration_ms: 0
- parent_id: 201000661
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.875
- end: 2026-08-14T20:36:16.875
- duration_ms: 0
- entity_id: 201000670
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.881
- end: 2026-08-14T20:36:16.881
- duration_ms: 0
- parent_id: 201000670
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.881
- end: 2026-08-14T20:36:16.881
- duration_ms: 0
- entity_id: 201000687
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.887
- end: 2026-08-14T20:36:16.887
- duration_ms: 0
- parent_id: 201000687
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.887
- end: 2026-08-14T20:36:16.887
- duration_ms: 0
- entity_id: 201000706
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.893
- end: 2026-08-14T20:36:16.893
- duration_ms: 0
- parent_id: 201000706
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.893
- end: 2026-08-14T20:36:16.893
- duration_ms: 0
- entity_id: 201000730
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.899
- end: 2026-08-14T20:36:16.899
- duration_ms: 0
- parent_id: 201000730
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.900
- end: 2026-08-14T20:36:16.900
- duration_ms: 0
- entity_id: 201000744
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.906
- end: 2026-08-14T20:36:16.906
- duration_ms: 0
- parent_id: 201000744
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.906
- end: 2026-08-14T20:36:16.906
- duration_ms: 0
- entity_id: 201000755
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.912
- end: 2026-08-14T20:36:16.912
- duration_ms: 0
- parent_id: 201000755
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.912
- end: 2026-08-14T20:36:16.912
- duration_ms: 0
- entity_id: 201000922
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.918
- end: 2026-08-14T20:36:16.918
- duration_ms: 0
- parent_id: 201000922
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.918
- end: 2026-08-14T20:36:16.918
- duration_ms: 0
- entity_id: 201000953
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.924
- end: 2026-08-14T20:36:16.924
- duration_ms: 0
- parent_id: 201000953
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.924
- end: 2026-08-14T20:36:16.924
- duration_ms: 0
- entity_id: 201000979
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.930
- end: 2026-08-14T20:36:16.930
- duration_ms: 0
- parent_id: 201000979
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.930
- end: 2026-08-14T20:36:16.930
- duration_ms: 0
- entity_id: 201000999
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.936
- end: 2026-08-14T20:36:16.936
- duration_ms: 0
- parent_id: 201000999
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.936
- end: 2026-08-14T20:36:16.936
- duration_ms: 0
- entity_id: 201001031
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.942
- end: 2026-08-14T20:36:16.942
- duration_ms: 0
- parent_id: 201001031
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.942
- end: 2026-08-14T20:36:16.942
- duration_ms: 0
- entity_id: 201001069
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.948
- end: 2026-08-14T20:36:16.948
- duration_ms: 0
- parent_id: 201001069
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.948
- end: 2026-08-14T20:36:16.948
- duration_ms: 0
- entity_id: 201001122
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.954
- end: 2026-08-14T20:36:16.954
- duration_ms: 0
- parent_id: 201001122
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.954
- end: 2026-08-14T20:36:16.954
- duration_ms: 0
- entity_id: 201001606
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.960
- end: 2026-08-14T20:36:16.960
- duration_ms: 0
- parent_id: 201001606
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.960
- end: 2026-08-14T20:36:16.960
- duration_ms: 0
- entity_id: 201001644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.966
- end: 2026-08-14T20:36:16.966
- duration_ms: 0
- parent_id: 201001644
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.966
- end: 2026-08-14T20:36:16.966
- duration_ms: 0
- entity_id: 201001727
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.972
- end: 2026-08-14T20:36:16.972
- duration_ms: 0
- parent_id: 201001727
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.972
- end: 2026-08-14T20:36:16.972
- duration_ms: 0
- entity_id: 201001916
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.978
- end: 2026-08-14T20:36:16.978
- duration_ms: 0
- parent_id: 201001916
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.978
- end: 2026-08-14T20:36:16.978
- duration_ms: 0
- entity_id: 201001934
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.984
- end: 2026-08-14T20:36:16.984
- duration_ms: 0
- parent_id: 201001934
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.984
- end: 2026-08-14T20:36:16.984
- duration_ms: 0
- entity_id: 201002162
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.990
- end: 2026-08-14T20:36:16.990
- duration_ms: 0
- parent_id: 201002162
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.990
- end: 2026-08-14T20:36:16.990
- duration_ms: 0
- entity_id: 201002179
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:16.996
- end: 2026-08-14T20:36:16.996
- duration_ms: 0
- parent_id: 201002179
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:16.997
- end: 2026-08-14T20:36:16.997
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.003
- end: 2026-08-14T20:36:17.003
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.003
- end: 2026-08-14T20:36:17.003
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.009
- end: 2026-08-14T20:36:17.009
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.009
- end: 2026-08-14T20:36:17.009
- duration_ms: 0
- entity_id: 201003138
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.015
- end: 2026-08-14T20:36:17.015
- duration_ms: 0
- parent_id: 201003138
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.015
- end: 2026-08-14T20:36:17.015
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.022
- end: 2026-08-14T20:36:17.022
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.022
- end: 2026-08-14T20:36:17.022
- duration_ms: 0
- entity_id: 201003777
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.028
- end: 2026-08-14T20:36:17.028
- duration_ms: 0
- parent_id: 201003777
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.028
- end: 2026-08-14T20:36:17.028
- duration_ms: 0
- entity_id: 201003844
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.035
- end: 2026-08-14T20:36:17.035
- duration_ms: 0
- parent_id: 201003844
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.035
- end: 2026-08-14T20:36:17.035
- duration_ms: 0
- entity_id: 201003862
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.041
- end: 2026-08-14T20:36:17.041
- duration_ms: 0
- parent_id: 201003862
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.041
- end: 2026-08-14T20:36:17.041
- duration_ms: 0
- entity_id: 201003931
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.047
- end: 2026-08-14T20:36:17.047
- duration_ms: 0
- parent_id: 201003931
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.047
- end: 2026-08-14T20:36:17.047
- duration_ms: 0
- entity_id: 201004017
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.053
- end: 2026-08-14T20:36:17.053
- duration_ms: 0
- parent_id: 201004017
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.053
- end: 2026-08-14T20:36:17.053
- duration_ms: 0
- entity_id: 201004058
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.061
- end: 2026-08-14T20:36:17.061
- duration_ms: 0
- parent_id: 201004058
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.061
- end: 2026-08-14T20:36:17.061
- duration_ms: 0
- entity_id: 201004076
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.069
- end: 2026-08-14T20:36:17.069
- duration_ms: 0
- parent_id: 201004076
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.069
- end: 2026-08-14T20:36:17.069
- duration_ms: 0
- entity_id: 201004088
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.078
- end: 2026-08-14T20:36:17.078
- duration_ms: 0
- parent_id: 201004088
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.078
- end: 2026-08-14T20:36:17.078
- duration_ms: 0
- entity_id: 201004117
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.085
- end: 2026-08-14T20:36:17.085
- duration_ms: 0
- parent_id: 201004117
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.085
- end: 2026-08-14T20:36:17.085
- duration_ms: 0
- entity_id: 201004172
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.091
- end: 2026-08-14T20:36:17.091
- duration_ms: 0
- parent_id: 201004172
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.092
- end: 2026-08-14T20:36:17.091
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.098
- end: 2026-08-14T20:36:17.098
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.098
- end: 2026-08-14T20:36:17.098
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.106
- end: 2026-08-14T20:36:17.106
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.107
- end: 2026-08-14T20:36:17.107
- duration_ms: 0
- entity_id: 201004282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.115
- end: 2026-08-14T20:36:17.115
- duration_ms: 0
- parent_id: 201004282
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.115
- end: 2026-08-14T20:36:17.115
- duration_ms: 0
- entity_id: 201004341
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.123
- end: 2026-08-14T20:36:17.123
- duration_ms: 0
- parent_id: 201004341
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:17.123
- end: 2026-08-14T20:36:17.123
- duration_ms: 0
- entity_id: 201004384
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:17.129
- end: 2026-08-14T20:36:17.129
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
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 22770
- response_chars: 962
- response_hash: 4ff68a930f979b4b

## Final Output
- answer_chars: 962
- answer_hash: 4ff68a930f979b4b
- success: True

## Request Complete
- request_end: 2026-08-14T20:36:39.901
- request_duration_ms: 26769
- success: True
- final_source: generation

