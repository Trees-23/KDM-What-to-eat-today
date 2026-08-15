# RAG Process

audit_id: 20260814_212112_545_8f307714
timestamp: 2026-08-14T21:21:12.545
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T21:21:12.546
- end: 2026-08-14T21:21:12.546
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T21:21:16.195
- end: 2026-08-14T21:21:16.195
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['排骨'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3649
- attempt_count: 1
- response_hash: 5ed5df9b8af7f618e924a2fc8659f5abac47b9877a19143e17e277004ef04751
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T21:21:16.203
- end: 2026-08-14T21:21:16.203
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 110a18a4c5639d69a5e6c3191e82653acaaf393d8241c48c80442ed42c462a8d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T21:21:16.203
- end: 2026-08-14T21:21:16.203
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:21:16.203+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T21:21:16.204
- end: 2026-08-14T21:21:16.204
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:21:16.203+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T21:21:16.204
- request_duration_ms: 3657
- success: True
- final_source: compile_terminal

