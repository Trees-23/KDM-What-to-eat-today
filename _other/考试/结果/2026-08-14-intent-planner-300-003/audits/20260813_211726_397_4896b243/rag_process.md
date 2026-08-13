# RAG Process

audit_id: 20260813_211726_397_4896b243
timestamp: 2026-08-13T21:17:26.398
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:17:26.398
- end: 2026-08-13T21:17:26.398
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 9

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:17:31.837
- end: 2026-08-13T21:17:31.837
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5439
- attempt_count: 1
- response_hash: 501e1fa8a1e7c98fdd0cd68a23a60a9cab810f2bdf2b23da4759b7917f9bdb5d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:17:31.840
- end: 2026-08-13T21:17:31.840
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 58cb008445dfe787889b9299f8ca816668e4b830116e873a821c8a831964b7bb
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:17:31.841
- end: 2026-08-13T21:17:31.841
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:31.841+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:17:31.841
- end: 2026-08-13T21:17:31.841
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:31.841+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:17:31.841
- request_duration_ms: 5442
- success: True
- final_source: compile_terminal

