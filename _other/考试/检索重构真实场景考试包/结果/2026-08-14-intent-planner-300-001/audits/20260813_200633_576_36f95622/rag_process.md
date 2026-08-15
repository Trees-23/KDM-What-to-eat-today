# RAG Process

audit_id: 20260813_200633_576_36f95622
timestamp: 2026-08-13T20:06:33.585
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:06:33.585
- end: 2026-08-13T20:06:33.585
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:06:37.136
- end: 2026-08-13T20:06:37.136
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['青蟹'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3550
- attempt_count: 1
- response_hash: 3015b3a6a5412443e30c4fd1722358c0a3558a8f89f175827b5c548d201b0f6d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:06:37.141
- end: 2026-08-13T20:06:37.141
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 3eb9f7b6182492631e09b722b1375a0336f34f621882f18a55db9ec9e5347e17
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:06:37.142
- end: 2026-08-13T20:06:37.142
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:06:37.142+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T20:06:37.142
- end: 2026-08-13T20:06:37.142
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:06:37.142+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T20:06:37.142
- request_duration_ms: 3556
- success: True
- final_source: compile_terminal

