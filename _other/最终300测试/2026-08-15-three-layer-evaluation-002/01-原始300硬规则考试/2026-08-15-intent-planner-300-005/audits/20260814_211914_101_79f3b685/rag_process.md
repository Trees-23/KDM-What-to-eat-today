# RAG Process

audit_id: 20260814_211914_101_79f3b685
timestamp: 2026-08-14T21:19:14.102
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T21:19:14.102
- end: 2026-08-14T21:19:14.102
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 23

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T21:19:20.414
- end: 2026-08-14T21:19:20.414
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['青蟹', '星雾紫萝15'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6312
- attempt_count: 1
- response_hash: e99be4290749eb715577456cea3895d318a1469246128f3d90df9f2d2ed9b2e0
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-14T21:19:20.441
- end: 2026-08-14T21:19:20.441
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: ENTITY_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-14T21:19:20.441
- request_duration_ms: 6339
- success: True
- final_source: compile_terminal

