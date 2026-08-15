# RAG Process

audit_id: 20260813_211518_141_843754cf
timestamp: 2026-08-13T21:15:18.143
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:15:18.144
- end: 2026-08-13T21:15:18.144
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 23

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:15:22.204
- end: 2026-08-13T21:15:22.204
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4060
- attempt_count: 1
- response_hash: 19a9eb7b46632a48bd2367f0d676f924f1374c4624cc4b0e376496c32c62157f
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T21:15:22.217
- end: 2026-08-13T21:15:22.217
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T21:15:22.217
- request_duration_ms: 4073
- success: True
- final_source: compile_terminal

