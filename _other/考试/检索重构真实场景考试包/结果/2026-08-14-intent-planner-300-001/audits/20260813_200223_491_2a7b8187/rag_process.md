# RAG Process

audit_id: 20260813_200223_491_2a7b8187
timestamp: 2026-08-13T20:02:23.492
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:02:23.493
- end: 2026-08-13T20:02:23.492
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 27

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:02:31.426
- end: 2026-08-13T20:02:31.426
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 7933
- attempt_count: 1
- response_hash: 94e5b4a52c981fd5fbc1b4651f351316f3f51879c877d38de5f7c7ddd25f913e
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T20:02:31.469
- end: 2026-08-13T20:02:31.469
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T20:02:31.469
- request_duration_ms: 7976
- success: True
- final_source: compile_terminal

