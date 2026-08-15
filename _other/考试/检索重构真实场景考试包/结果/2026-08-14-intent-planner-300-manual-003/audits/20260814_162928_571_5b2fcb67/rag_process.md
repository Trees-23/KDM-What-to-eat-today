# RAG Process

audit_id: 20260814_162928_571_5b2fcb67
timestamp: 2026-08-14T16:29:28.572
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:29:28.572
- end: 2026-08-14T16:29:28.572
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:29:34.173
- end: 2026-08-14T16:29:34.173
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['豆腐'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5600
- attempt_count: 1
- response_hash: 2cd4333138d9b2aa7f8197ab7360756a6ef4c5033f30df6bc04d1d0ab13e793a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:29:34.189
- end: 2026-08-14T16:29:34.189
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 890120a2c84ebcc96303fb60436e87ae67dcaf7fe8cdee30bdb0c5058265a249
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:29:34.189
- end: 2026-08-14T16:29:34.189
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:29:34.189+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:29:34.189
- end: 2026-08-14T16:29:34.189
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:29:34.189+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:29:34.189
- request_duration_ms: 5616
- success: True
- final_source: compile_terminal

