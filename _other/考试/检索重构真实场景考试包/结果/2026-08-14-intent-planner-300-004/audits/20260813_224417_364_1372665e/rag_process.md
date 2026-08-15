# RAG Process

audit_id: 20260813_224417_364_1372665e
timestamp: 2026-08-13T22:44:17.364
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:44:17.365
- end: 2026-08-13T22:44:17.365
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 24

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:44:20.971
- end: 2026-08-13T22:44:20.971
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3605
- attempt_count: 1
- response_hash: 1f30b939740416e2f16a2ca13ca84ecd6021822eb17e484a734dec45ef275bb4
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T22:44:20.999
- end: 2026-08-13T22:44:20.999
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T22:44:20.999
- request_duration_ms: 3633
- success: True
- final_source: compile_terminal

