# RAG Process

audit_id: 20260813_211627_125_1c64e5c1
timestamp: 2026-08-13T21:16:27.126
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:16:27.126
- end: 2026-08-13T21:16:27.126
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:16:30.561
- end: 2026-08-13T21:16:30.561
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3435
- attempt_count: 1
- response_hash: f6bddb982769344c9fd8ebc44f4777cc726c5e88bfbc2cf100f9a02fbed6aa8b
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:16:30.571
- end: 2026-08-13T21:16:30.571
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 26f67e4276e5e3ae393e720125ec5c97e34bdb546f1c1818614d295d6f37a8ea
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:16:30.572
- end: 2026-08-13T21:16:30.572
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:16:30.572+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:16:30.572
- end: 2026-08-13T21:16:30.572
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:16:30.572+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:16:30.572
- request_duration_ms: 3446
- success: True
- final_source: compile_terminal

