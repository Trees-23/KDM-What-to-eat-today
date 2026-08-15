# RAG Process

audit_id: 20260813_204108_901_bb71258a
timestamp: 2026-08-13T20:41:08.911
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:41:08.911
- end: 2026-08-13T20:41:08.911
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:41:12.505
- end: 2026-08-13T20:41:12.505
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3593
- attempt_count: 1
- response_hash: 59e0406540d311c209949b9ec2a4e9f03ae92452d3d546646cac03137eb87638
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:41:12.508
- end: 2026-08-13T20:41:12.508
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 18ba07c3e1078f43f68ee84f8a9497df330f3a1c58bc835c49be86737af797fa
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:41:12.508
- end: 2026-08-13T20:41:12.508
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:41:12.508+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:41:12.513
- end: 2026-08-13T20:41:12.513
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:41:12.508+00:00
- result_count: 50

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.513
- end: 2026-08-13T20:41:12.513
- duration_ms: 0
- entity_id: 201000001
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.524
- end: 2026-08-13T20:41:12.524
- duration_ms: 0
- parent_id: 201000001
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.524
- end: 2026-08-13T20:41:12.524
- duration_ms: 0
- entity_id: 201000290
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.536
- end: 2026-08-13T20:41:12.536
- duration_ms: 0
- parent_id: 201000290
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.537
- end: 2026-08-13T20:41:12.537
- duration_ms: 0
- entity_id: 201000411
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.546
- end: 2026-08-13T20:41:12.546
- duration_ms: 0
- parent_id: 201000411
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.546
- end: 2026-08-13T20:41:12.546
- duration_ms: 0
- entity_id: 201000519
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.552
- end: 2026-08-13T20:41:12.552
- duration_ms: 0
- parent_id: 201000519
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.552
- end: 2026-08-13T20:41:12.552
- duration_ms: 0
- entity_id: 201000539
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.559
- end: 2026-08-13T20:41:12.559
- duration_ms: 0
- parent_id: 201000539
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.559
- end: 2026-08-13T20:41:12.559
- duration_ms: 0
- entity_id: 201000550
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.568
- end: 2026-08-13T20:41:12.568
- duration_ms: 0
- parent_id: 201000550
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.568
- end: 2026-08-13T20:41:12.568
- duration_ms: 0
- entity_id: 201000571
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.579
- end: 2026-08-13T20:41:12.579
- duration_ms: 0
- parent_id: 201000571
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.580
- end: 2026-08-13T20:41:12.580
- duration_ms: 0
- entity_id: 201000605
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.587
- end: 2026-08-13T20:41:12.587
- duration_ms: 0
- parent_id: 201000605
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.587
- end: 2026-08-13T20:41:12.587
- duration_ms: 0
- entity_id: 201000628
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.594
- end: 2026-08-13T20:41:12.594
- duration_ms: 0
- parent_id: 201000628
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.594
- end: 2026-08-13T20:41:12.594
- duration_ms: 0
- entity_id: 201000644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.601
- end: 2026-08-13T20:41:12.601
- duration_ms: 0
- parent_id: 201000644
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.601
- end: 2026-08-13T20:41:12.601
- duration_ms: 0
- entity_id: 201000661
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.608
- end: 2026-08-13T20:41:12.608
- duration_ms: 0
- parent_id: 201000661
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.608
- end: 2026-08-13T20:41:12.608
- duration_ms: 0
- entity_id: 201000670
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.616
- end: 2026-08-13T20:41:12.616
- duration_ms: 0
- parent_id: 201000670
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.616
- end: 2026-08-13T20:41:12.616
- duration_ms: 0
- entity_id: 201000687
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.623
- end: 2026-08-13T20:41:12.623
- duration_ms: 0
- parent_id: 201000687
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.623
- end: 2026-08-13T20:41:12.623
- duration_ms: 0
- entity_id: 201000706
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.629
- end: 2026-08-13T20:41:12.629
- duration_ms: 0
- parent_id: 201000706
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.630
- end: 2026-08-13T20:41:12.630
- duration_ms: 0
- entity_id: 201000730
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.636
- end: 2026-08-13T20:41:12.636
- duration_ms: 0
- parent_id: 201000730
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.636
- end: 2026-08-13T20:41:12.636
- duration_ms: 0
- entity_id: 201000744
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.642
- end: 2026-08-13T20:41:12.642
- duration_ms: 0
- parent_id: 201000744
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.642
- end: 2026-08-13T20:41:12.642
- duration_ms: 0
- entity_id: 201000755
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.649
- end: 2026-08-13T20:41:12.649
- duration_ms: 0
- parent_id: 201000755
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.650
- end: 2026-08-13T20:41:12.650
- duration_ms: 0
- entity_id: 201000922
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.659
- end: 2026-08-13T20:41:12.659
- duration_ms: 0
- parent_id: 201000922
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.659
- end: 2026-08-13T20:41:12.659
- duration_ms: 0
- entity_id: 201000953
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.673
- end: 2026-08-13T20:41:12.673
- duration_ms: 0
- parent_id: 201000953
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.673
- end: 2026-08-13T20:41:12.673
- duration_ms: 0
- entity_id: 201000979
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.688
- end: 2026-08-13T20:41:12.688
- duration_ms: 0
- parent_id: 201000979
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.688
- end: 2026-08-13T20:41:12.688
- duration_ms: 0
- entity_id: 201000999
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.697
- end: 2026-08-13T20:41:12.697
- duration_ms: 0
- parent_id: 201000999
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.697
- end: 2026-08-13T20:41:12.697
- duration_ms: 0
- entity_id: 201001031
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.705
- end: 2026-08-13T20:41:12.705
- duration_ms: 0
- parent_id: 201001031
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.705
- end: 2026-08-13T20:41:12.705
- duration_ms: 0
- entity_id: 201001069
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.713
- end: 2026-08-13T20:41:12.713
- duration_ms: 0
- parent_id: 201001069
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.714
- end: 2026-08-13T20:41:12.714
- duration_ms: 0
- entity_id: 201001122
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.720
- end: 2026-08-13T20:41:12.720
- duration_ms: 0
- parent_id: 201001122
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.720
- end: 2026-08-13T20:41:12.720
- duration_ms: 0
- entity_id: 201001606
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.726
- end: 2026-08-13T20:41:12.726
- duration_ms: 0
- parent_id: 201001606
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.726
- end: 2026-08-13T20:41:12.726
- duration_ms: 0
- entity_id: 201001644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.733
- end: 2026-08-13T20:41:12.733
- duration_ms: 0
- parent_id: 201001644
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.733
- end: 2026-08-13T20:41:12.733
- duration_ms: 0
- entity_id: 201001727
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.739
- end: 2026-08-13T20:41:12.739
- duration_ms: 0
- parent_id: 201001727
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.739
- end: 2026-08-13T20:41:12.739
- duration_ms: 0
- entity_id: 201001916
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.746
- end: 2026-08-13T20:41:12.746
- duration_ms: 0
- parent_id: 201001916
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.746
- end: 2026-08-13T20:41:12.746
- duration_ms: 0
- entity_id: 201001934
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.753
- end: 2026-08-13T20:41:12.753
- duration_ms: 0
- parent_id: 201001934
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.754
- end: 2026-08-13T20:41:12.754
- duration_ms: 0
- entity_id: 201002162
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.760
- end: 2026-08-13T20:41:12.760
- duration_ms: 0
- parent_id: 201002162
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.760
- end: 2026-08-13T20:41:12.760
- duration_ms: 0
- entity_id: 201002179
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.766
- end: 2026-08-13T20:41:12.766
- duration_ms: 0
- parent_id: 201002179
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.767
- end: 2026-08-13T20:41:12.767
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.773
- end: 2026-08-13T20:41:12.773
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.773
- end: 2026-08-13T20:41:12.773
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.780
- end: 2026-08-13T20:41:12.780
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.780
- end: 2026-08-13T20:41:12.780
- duration_ms: 0
- entity_id: 201003138
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.786
- end: 2026-08-13T20:41:12.786
- duration_ms: 0
- parent_id: 201003138
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.786
- end: 2026-08-13T20:41:12.786
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.794
- end: 2026-08-13T20:41:12.793
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.794
- end: 2026-08-13T20:41:12.794
- duration_ms: 0
- entity_id: 201003777
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.802
- end: 2026-08-13T20:41:12.802
- duration_ms: 0
- parent_id: 201003777
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.802
- end: 2026-08-13T20:41:12.802
- duration_ms: 0
- entity_id: 201003844
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.815
- end: 2026-08-13T20:41:12.815
- duration_ms: 0
- parent_id: 201003844
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.815
- end: 2026-08-13T20:41:12.815
- duration_ms: 0
- entity_id: 201003862
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.823
- end: 2026-08-13T20:41:12.823
- duration_ms: 0
- parent_id: 201003862
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.823
- end: 2026-08-13T20:41:12.823
- duration_ms: 0
- entity_id: 201003931
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.830
- end: 2026-08-13T20:41:12.830
- duration_ms: 0
- parent_id: 201003931
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.830
- end: 2026-08-13T20:41:12.830
- duration_ms: 0
- entity_id: 201004017
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.840
- end: 2026-08-13T20:41:12.840
- duration_ms: 0
- parent_id: 201004017
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.840
- end: 2026-08-13T20:41:12.840
- duration_ms: 0
- entity_id: 201004058
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.848
- end: 2026-08-13T20:41:12.848
- duration_ms: 0
- parent_id: 201004058
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.848
- end: 2026-08-13T20:41:12.848
- duration_ms: 0
- entity_id: 201004076
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.855
- end: 2026-08-13T20:41:12.855
- duration_ms: 0
- parent_id: 201004076
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.855
- end: 2026-08-13T20:41:12.855
- duration_ms: 0
- entity_id: 201004088
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.861
- end: 2026-08-13T20:41:12.861
- duration_ms: 0
- parent_id: 201004088
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.861
- end: 2026-08-13T20:41:12.861
- duration_ms: 0
- entity_id: 201004117
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.868
- end: 2026-08-13T20:41:12.868
- duration_ms: 0
- parent_id: 201004117
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.868
- end: 2026-08-13T20:41:12.868
- duration_ms: 0
- entity_id: 201004172
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.875
- end: 2026-08-13T20:41:12.875
- duration_ms: 0
- parent_id: 201004172
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.875
- end: 2026-08-13T20:41:12.875
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.881
- end: 2026-08-13T20:41:12.881
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.881
- end: 2026-08-13T20:41:12.881
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.888
- end: 2026-08-13T20:41:12.888
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.888
- end: 2026-08-13T20:41:12.888
- duration_ms: 0
- entity_id: 201004282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.895
- end: 2026-08-13T20:41:12.895
- duration_ms: 0
- parent_id: 201004282
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.895
- end: 2026-08-13T20:41:12.895
- duration_ms: 0
- entity_id: 201004341
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.901
- end: 2026-08-13T20:41:12.901
- duration_ms: 0
- parent_id: 201004341
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:12.901
- end: 2026-08-13T20:41:12.901
- duration_ms: 0
- entity_id: 201004384
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:12.907
- end: 2026-08-13T20:41:12.907
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
- duration_ms: 13816
- response_chars: 601
- response_hash: 6013524c3973ab5a

## Final Output
- answer_chars: 601
- answer_hash: 6013524c3973ab5a
- success: True

## Request Complete
- request_end: 2026-08-13T20:41:26.726
- request_duration_ms: 17814
- success: True
- final_source: generation

