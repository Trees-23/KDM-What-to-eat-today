# RAG Process

audit_id: 20260813_221013_165_5ac48be1
timestamp: 2026-08-13T22:10:13.165
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:10:13.166
- end: 2026-08-13T22:10:13.166
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:10:16.603
- end: 2026-08-13T22:10:16.603
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['牛肉'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3437
- attempt_count: 1
- response_hash: 2348f68b670e7602eb92172a3f884a7877fc7481b673d43ee5786047727a328f
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:10:16.609
- end: 2026-08-13T22:10:16.609
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 672f8712d63595517752fc9482cb688f7f59c98c1b1afa051ef15b56b870feb0
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:10:16.610
- end: 2026-08-13T22:10:16.610
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:10:16.610+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:10:16.613
- end: 2026-08-13T22:10:16.613
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:10:16.610+00:00
- result_count: 8

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:16.613
- end: 2026-08-13T22:10:16.613
- duration_ms: 0
- entity_id: 201001630
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:16.623
- end: 2026-08-13T22:10:16.623
- duration_ms: 0
- parent_id: 201001630
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:16.623
- end: 2026-08-13T22:10:16.623
- duration_ms: 0
- entity_id: 201002555
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:16.631
- end: 2026-08-13T22:10:16.631
- duration_ms: 0
- parent_id: 201002555
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:16.631
- end: 2026-08-13T22:10:16.631
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:16.639
- end: 2026-08-13T22:10:16.639
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:16.639
- end: 2026-08-13T22:10:16.639
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:16.646
- end: 2026-08-13T22:10:16.646
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:16.646
- end: 2026-08-13T22:10:16.646
- duration_ms: 0
- entity_id: 201003314
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:16.653
- end: 2026-08-13T22:10:16.653
- duration_ms: 0
- parent_id: 201003314
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:16.653
- end: 2026-08-13T22:10:16.653
- duration_ms: 0
- entity_id: 201003507
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:16.659
- end: 2026-08-13T22:10:16.659
- duration_ms: 0
- parent_id: 201003507
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:16.660
- end: 2026-08-13T22:10:16.660
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:16.666
- end: 2026-08-13T22:10:16.666
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:16.666
- end: 2026-08-13T22:10:16.666
- duration_ms: 0
- entity_id: 201003793
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:16.673
- end: 2026-08-13T22:10:16.673
- duration_ms: 0
- parent_id: 201003793
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 10513
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 8
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
- duration_ms: 11134
- response_chars: 478
- response_hash: b7973bdc9585cd54

## Final Output
- answer_chars: 478
- answer_hash: b7973bdc9585cd54
- success: True

## Request Complete
- request_end: 2026-08-13T22:10:27.809
- request_duration_ms: 14643
- success: True
- final_source: generation

