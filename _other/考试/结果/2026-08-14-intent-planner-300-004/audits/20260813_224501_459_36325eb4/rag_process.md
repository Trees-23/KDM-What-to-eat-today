# RAG Process

audit_id: 20260813_224501_459_36325eb4
timestamp: 2026-08-13T22:45:01.459
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:45:01.460
- end: 2026-08-13T22:45:01.460
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:45:04.951
- end: 2026-08-13T22:45:04.951
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3491
- attempt_count: 1
- response_hash: ef19c8e2ebe7d2a864f0429055749d9611459b3f7472fbc561b213ec5b7b0d73
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:45:04.954
- end: 2026-08-13T22:45:04.954
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 672f8712d63595517752fc9482cb688f7f59c98c1b1afa051ef15b56b870feb0
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:45:04.954
- end: 2026-08-13T22:45:04.954
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:45:04.954+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T22:45:04.964
- end: 2026-08-13T22:45:04.964
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:45:04.954+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T22:45:04.964
- request_duration_ms: 3503
- success: True
- final_source: compile_terminal

