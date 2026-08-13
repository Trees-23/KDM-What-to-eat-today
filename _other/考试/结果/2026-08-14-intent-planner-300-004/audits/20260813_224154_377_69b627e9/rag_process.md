# RAG Process

audit_id: 20260813_224154_377_69b627e9
timestamp: 2026-08-13T22:41:54.378
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:41:54.379
- end: 2026-08-13T22:41:54.379
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 27

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:41:59.712
- end: 2026-08-13T22:41:59.712
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: ENTITY_LOOKUP
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5333
- attempt_count: 1
- response_hash: fa4e2612ad08508c5f67f6ce35e8f462c92ea63e3be1ff163d8d24ea8ea033a9
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T22:41:59.736
- end: 2026-08-13T22:41:59.736
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T22:41:59.736
- request_duration_ms: 5357
- success: True
- final_source: compile_terminal

