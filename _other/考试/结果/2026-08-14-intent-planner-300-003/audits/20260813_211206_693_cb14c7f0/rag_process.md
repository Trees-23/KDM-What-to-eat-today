# RAG Process

audit_id: 20260813_211206_693_cb14c7f0
timestamp: 2026-08-13T21:12:06.695
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:12:06.695
- end: 2026-08-13T21:12:06.695
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 13

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:12:10.473
- end: 2026-08-13T21:12:10.473
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3778
- attempt_count: 1
- response_hash: 98147ef507b4f9f4a281ab8832773e26ec3afe0d603d38623b19c0feca9467d7
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T21:12:10.480
- end: 2026-08-13T21:12:10.480
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T21:12:10.480
- request_duration_ms: 3785
- success: True
- final_source: compile_terminal

