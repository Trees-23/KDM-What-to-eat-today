# RAG Process

audit_id: 20260814_162623_416_7f438cb1
timestamp: 2026-08-14T16:26:23.416
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:26:23.416
- end: 2026-08-14T16:26:23.416
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:26:29.236
- end: 2026-08-14T16:26:29.236
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5819
- attempt_count: 1
- response_hash: b2d2da7f23bc5c0850922569b69979a43d47d2dc2a1b70e6f6b47bd930eddc58
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-14T16:26:29.268
- end: 2026-08-14T16:26:29.268
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-14T16:26:29.268
- request_duration_ms: 5852
- success: True
- final_source: compile_terminal

