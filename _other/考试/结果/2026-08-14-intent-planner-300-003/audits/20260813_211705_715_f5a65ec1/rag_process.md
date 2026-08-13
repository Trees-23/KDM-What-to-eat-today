# RAG Process

audit_id: 20260813_211705_715_f5a65ec1
timestamp: 2026-08-13T21:17:05.717
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:17:05.718
- end: 2026-08-13T21:17:05.718
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:17:08.589
- end: 2026-08-13T21:17:08.589
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3526
- attempt_count: 1
- response_hash: 796d921a2fd37d44c1ca25f0145547249f5907d1c582d5ad574e03617b4c122e
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:17:08.592
- end: 2026-08-13T21:17:08.592
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 370144f87365ea87eb0e31aac0ddee6c40cf6a652df6dd418e5c3a8c3a2dbf20
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:17:08.592
- end: 2026-08-13T21:17:08.592
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:08.592+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:17:08.592
- end: 2026-08-13T21:17:08.592
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:08.592+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:17:08.592
- request_duration_ms: 2874
- success: True
- final_source: compile_terminal

