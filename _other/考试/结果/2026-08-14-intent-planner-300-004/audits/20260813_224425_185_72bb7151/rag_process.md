# RAG Process

audit_id: 20260813_224425_185_72bb7151
timestamp: 2026-08-13T22:44:25.185
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:44:25.185
- end: 2026-08-13T22:44:25.185
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:44:28.719
- end: 2026-08-13T22:44:28.719
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4307
- attempt_count: 1
- response_hash: 0ac226d04a8742ca452cfbc2a797c40be324305e9c6c44e91618458ae8049acc
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T22:44:28.741
- end: 2026-08-13T22:44:28.741
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T22:44:28.741
- request_duration_ms: 3555
- success: True
- final_source: compile_terminal

