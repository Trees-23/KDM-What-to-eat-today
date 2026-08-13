# RAG Process

audit_id: 20260813_215200_827_bf8b3fd1
timestamp: 2026-08-13T21:52:00.827
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:52:00.828
- end: 2026-08-13T21:52:00.828
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 35

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:52:04.404
- end: 2026-08-13T21:52:04.404
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3576
- attempt_count: 1
- response_hash: 6f8e70dfeae969426cdc909d2af986f973e4e84edf5482ee2d9ebd733ef05092
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: CLARIFY
- start: 2026-08-13T21:52:04.409
- end: 2026-08-13T21:52:04.409
- duration_ms: 0
- compile_action: CLARIFY_OR_OUT_OF_SCOPE
- reason: ENTITY_AMBIGUOUS
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T21:52:04.410
- request_duration_ms: 3582
- success: True
- final_source: compile_terminal

