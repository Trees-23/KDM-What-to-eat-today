# RAG Process

audit_id: 20260813_224149_250_8aef320b
timestamp: 2026-08-13T22:41:49.251
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:41:49.251
- end: 2026-08-13T22:41:49.251
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 27

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:41:54.360
- end: 2026-08-13T22:41:54.360
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5109
- attempt_count: 1
- response_hash: 211f8aa41e1d126584d8f75b678da20606b53801297785664e8fe2482c607e6e
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T22:41:54.376
- end: 2026-08-13T22:41:54.376
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T22:41:54.376
- request_duration_ms: 5125
- success: True
- final_source: compile_terminal

