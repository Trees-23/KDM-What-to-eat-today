# RAG Process

audit_id: 20260814_162306_206_45d94e7c
timestamp: 2026-08-14T16:23:06.207
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:23:06.207
- end: 2026-08-14T16:23:06.207
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 13

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:23:13.075
- end: 2026-08-14T16:23:13.075
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.9
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6868
- attempt_count: 1
- response_hash: f808da30fc6faaeb7e215954d4baa79e08e94f4e76441097bf3c1f3358c7cdb8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-14T16:23:13.096
- end: 2026-08-14T16:23:13.096
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-14T16:23:13.097
- request_duration_ms: 6890
- success: True
- final_source: compile_terminal

