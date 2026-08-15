# RAG Process

audit_id: 20260814_162825_241_42d16dfa
timestamp: 2026-08-14T16:28:25.243
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:28:25.243
- end: 2026-08-14T16:28:25.243
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 35

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:28:31.021
- end: 2026-08-14T16:28:31.021
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.94
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5778
- attempt_count: 1
- response_hash: 824807d1a900dabaf316f03ac5ca7a69da98997696479bce81c1d03fa6cb6ce5
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-14T16:28:31.060
- end: 2026-08-14T16:28:31.060
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-14T16:28:31.061
- request_duration_ms: 5817
- success: True
- final_source: compile_terminal

