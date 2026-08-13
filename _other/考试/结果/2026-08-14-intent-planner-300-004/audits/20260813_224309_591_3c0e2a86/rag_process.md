# RAG Process

audit_id: 20260813_224309_591_3c0e2a86
timestamp: 2026-08-13T22:43:09.591
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:43:09.592
- end: 2026-08-13T22:43:09.592
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:43:14.066
- end: 2026-08-13T22:43:14.066
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4474
- attempt_count: 1
- response_hash: 64958900a1ed3ed27ed13b7c89ca10e452a57db18537dba2e70c6c74ebbd65c1
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T22:43:14.079
- end: 2026-08-13T22:43:14.079
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T22:43:14.079
- request_duration_ms: 4487
- success: True
- final_source: compile_terminal

