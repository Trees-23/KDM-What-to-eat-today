# RAG Process

audit_id: 20260813_224234_230_4d91e4b1
timestamp: 2026-08-13T22:42:34.231
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:42:34.232
- end: 2026-08-13T22:42:34.232
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:42:37.885
- end: 2026-08-13T22:42:37.885
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3653
- attempt_count: 1
- response_hash: f6f4ef8fd8d1fc54feac11638ea2172157f5c5177e72d0e6a8db3f1c9327fca1
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T22:42:37.904
- end: 2026-08-13T22:42:37.904
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T22:42:37.904
- request_duration_ms: 3672
- success: True
- final_source: compile_terminal

