# RAG Process

audit_id: 20260813_211308_952_51f6624d
timestamp: 2026-08-13T21:13:08.953
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:13:08.954
- end: 2026-08-13T21:13:08.954
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 27

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:13:12.479
- end: 2026-08-13T21:13:12.479
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: ENTITY_LOOKUP
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3525
- attempt_count: 1
- response_hash: 34387a6c5b1a401032e152699ba77700fbfe8608d92e04a249dea79d29739653
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T21:13:12.501
- end: 2026-08-13T21:13:12.501
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T21:13:12.501
- request_duration_ms: 3547
- success: True
- final_source: compile_terminal

