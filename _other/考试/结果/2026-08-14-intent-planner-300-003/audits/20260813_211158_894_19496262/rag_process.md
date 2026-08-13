# RAG Process

audit_id: 20260813_211158_894_19496262
timestamp: 2026-08-13T21:11:58.895
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:11:58.895
- end: 2026-08-13T21:11:58.895
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 13

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:12:03.235
- end: 2026-08-13T21:12:03.235
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4340
- attempt_count: 1
- response_hash: 89f46404714bec605283edca23d14be33cf77d101416ede2b73c0f2b2bed100f
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T21:12:03.260
- end: 2026-08-13T21:12:03.260
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T21:12:03.260
- request_duration_ms: 4365
- success: True
- final_source: compile_terminal

