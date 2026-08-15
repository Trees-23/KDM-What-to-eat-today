# RAG Process

audit_id: 20260813_224642_944_9a3d839d
timestamp: 2026-08-13T22:46:42.945
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:46:42.956
- end: 2026-08-13T22:46:42.956
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:46:48.358
- end: 2026-08-13T22:46:48.358
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5401
- attempt_count: 1
- response_hash: acd6f797b1f35ae63a154eb4b91ec76fdee3e76792e89a19b0b2ccc41fe36857
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:46:48.361
- end: 2026-08-13T22:46:48.361
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 2772892dfb4d87f8a38115265dc4bac51f60809ee2740138c36b4d5169d5c78d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:46:48.361
- end: 2026-08-13T22:46:48.361
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:46:48.361+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T22:46:48.361
- end: 2026-08-13T22:46:48.361
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:46:48.361+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T22:46:48.361
- request_duration_ms: 5404
- success: True
- final_source: compile_terminal

