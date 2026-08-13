# RAG Process

audit_id: 20260813_211343_672_d9e011f7
timestamp: 2026-08-13T21:13:43.673
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:13:43.673
- end: 2026-08-13T21:13:43.673
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:13:48.280
- end: 2026-08-13T21:13:48.280
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4607
- attempt_count: 1
- response_hash: 5a2173cf2afb681ca97fb227cf2b5bdef319c865b0a3b946ad3447780e9fccce
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T21:13:48.295
- end: 2026-08-13T21:13:48.294
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T21:13:48.295
- request_duration_ms: 4622
- success: True
- final_source: compile_terminal

