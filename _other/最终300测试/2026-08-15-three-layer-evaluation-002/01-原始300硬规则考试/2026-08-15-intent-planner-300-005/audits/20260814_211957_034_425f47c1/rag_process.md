# RAG Process

audit_id: 20260814_211957_034_425f47c1
timestamp: 2026-08-14T21:19:57.034
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T21:19:57.034
- end: 2026-08-14T21:19:57.034
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 35

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T21:20:00.860
- end: 2026-08-14T21:20:00.860
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3826
- attempt_count: 1
- response_hash: c00c5e947a72d8efdce9609833ba3dc5d048eaaadde5ce8969a733c0a48bb0de
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-14T21:20:00.889
- end: 2026-08-14T21:20:00.889
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-14T21:20:00.889
- request_duration_ms: 3854
- success: True
- final_source: compile_terminal

