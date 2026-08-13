# RAG Process

audit_id: 20260813_211203_261_0eb311e3
timestamp: 2026-08-13T21:12:03.261
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:12:03.261
- end: 2026-08-13T21:12:03.261
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 13

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:12:06.661
- end: 2026-08-13T21:12:06.661
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3400
- attempt_count: 1
- response_hash: 495b930b41bd9631893e4234b741f53171aab1ed78c643c7002fdc8b293a1cfc
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T21:12:06.693
- end: 2026-08-13T21:12:06.692
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T21:12:06.693
- request_duration_ms: 3431
- success: True
- final_source: compile_terminal

