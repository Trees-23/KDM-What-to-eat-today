# RAG Process

audit_id: 20260813_211432_539_96256b8d
timestamp: 2026-08-13T21:14:32.540
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:14:32.540
- end: 2026-08-13T21:14:32.540
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 18

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:14:36.176
- end: 2026-08-13T21:14:36.176
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3636
- attempt_count: 1
- response_hash: 3a457a95b6fe17d627a6001b381c1078432576dac38cd06996dfb4f9a65202af
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T21:14:36.184
- end: 2026-08-13T21:14:36.184
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T21:14:36.185
- request_duration_ms: 3644
- success: True
- final_source: compile_terminal

