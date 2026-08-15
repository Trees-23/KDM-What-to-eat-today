# RAG Process

audit_id: 20260814_162526_573_a9e2d911
timestamp: 2026-08-14T16:25:26.575
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:25:26.575
- end: 2026-08-14T16:25:26.575
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:25:31.421
- end: 2026-08-14T16:25:31.421
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4846
- attempt_count: 1
- response_hash: bc2d36e9a4fd068ee99f5bb571ad489673b9bf32f3a87b5f155147a6eea887c0
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-14T16:25:31.428
- end: 2026-08-14T16:25:31.428
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-14T16:25:31.428
- request_duration_ms: 4853
- success: True
- final_source: compile_terminal

