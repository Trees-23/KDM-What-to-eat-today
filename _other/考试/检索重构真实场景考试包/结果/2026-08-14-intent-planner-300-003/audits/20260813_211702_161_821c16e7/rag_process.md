# RAG Process

audit_id: 20260813_211702_161_821c16e7
timestamp: 2026-08-13T21:17:02.163
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:17:02.163
- end: 2026-08-13T21:17:02.163
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:17:05.710
- end: 2026-08-13T21:17:05.710
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3546
- attempt_count: 1
- response_hash: 8212c221c8ae7e7fc985cff5b9e4cfd177a97f2ebe7f898b842a3d4c948bccd2
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:17:05.714
- end: 2026-08-13T21:17:05.714
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 3eb9f7b6182492631e09b722b1375a0336f34f621882f18a55db9ec9e5347e17
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:17:05.714
- end: 2026-08-13T21:17:05.714
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:05.714+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:17:05.714
- end: 2026-08-13T21:17:05.714
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:05.714+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:17:05.715
- request_duration_ms: 3551
- success: True
- final_source: compile_terminal

