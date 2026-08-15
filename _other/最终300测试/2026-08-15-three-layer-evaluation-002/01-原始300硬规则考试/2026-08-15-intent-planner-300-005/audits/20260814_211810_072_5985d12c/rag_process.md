# RAG Process

audit_id: 20260814_211810_072_5985d12c
timestamp: 2026-08-14T21:18:10.072
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T21:18:10.072
- end: 2026-08-14T21:18:10.072
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T21:18:14.402
- end: 2026-08-14T21:18:14.402
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.92
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4329
- attempt_count: 1
- response_hash: e23a014a5513685d57a8cd330f9896512f3e72f04ad36714ba59c674486426d0
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-14T21:18:14.451
- end: 2026-08-14T21:18:14.451
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-14T21:18:14.451
- request_duration_ms: 4379
- success: True
- final_source: compile_terminal

