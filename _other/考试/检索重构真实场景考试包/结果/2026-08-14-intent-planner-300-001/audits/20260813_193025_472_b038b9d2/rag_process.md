# RAG Process

audit_id: 20260813_193025_472_b038b9d2
timestamp: 2026-08-13T19:30:25.472
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:30:25.473
- end: 2026-08-13T19:30:25.473
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:30:29.460
- end: 2026-08-13T19:30:29.460
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['米饭'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3987
- attempt_count: 1
- response_hash: 58aedb6784fdbd9b4a61305ca525e7d531097715832fbbecdfbb1247feef5ef6
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:30:29.476
- end: 2026-08-13T19:30:29.476
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 9aedaa8d2d7664e5c2bd13246518a7450b6d35d3b197ac0eb2e609255f2d5578
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:30:29.476
- end: 2026-08-13T19:30:29.476
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:30:29.476+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:30:29.480
- end: 2026-08-13T19:30:29.480
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:30:29.476+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:30:29.480
- end: 2026-08-13T19:30:29.480
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:30:29.495
- end: 2026-08-13T19:30:29.495
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:30:29.495
- end: 2026-08-13T19:30:29.495
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:30:29.510
- end: 2026-08-13T19:30:29.510
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:30:29.510
- end: 2026-08-13T19:30:29.510
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:30:29.520
- end: 2026-08-13T19:30:29.519
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:30:29.520
- end: 2026-08-13T19:30:29.520
- duration_ms: 0
- entity_id: 201004588
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:30:29.527
- end: 2026-08-13T19:30:29.527
- duration_ms: 0
- parent_id: 201004588
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:30:29.527
- end: 2026-08-13T19:30:29.527
- duration_ms: 0
- entity_id: 201004801
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:30:29.533
- end: 2026-08-13T19:30:29.533
- duration_ms: 0
- parent_id: 201004801
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 6469
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
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
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 14518
- response_chars: 468
- response_hash: fe10fbeb9f71b5b7

## Final Output
- answer_chars: 468
- answer_hash: fe10fbeb9f71b5b7
- success: True

## Request Complete
- request_end: 2026-08-13T19:30:44.054
- request_duration_ms: 18580
- success: True
- final_source: generation

