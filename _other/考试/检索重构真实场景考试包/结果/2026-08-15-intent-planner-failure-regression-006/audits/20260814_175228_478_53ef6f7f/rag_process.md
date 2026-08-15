# RAG Process

audit_id: 20260814_175228_478_53ef6f7f
timestamp: 2026-08-14T17:52:28.478
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T17:52:28.479
- end: 2026-08-14T17:52:28.479
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T17:52:32.425
- end: 2026-08-14T17:52:32.425
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: PREFERENCE_RECOMMEND
- confidence: 0.86
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3946
- attempt_count: 1
- response_hash: e42063ebaf85b3806ab185fdb59eb0cda94699142c721aff976556e40fe1384b
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-14T17:52:32.476
- end: 2026-08-14T17:52:32.476
- duration_ms: 0
- compile_action: ENTITY_NOT_FOUND
- reason: INGREDIENT_NOT_FOUND
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-14T17:52:32.476
- request_duration_ms: 3997
- success: True
- final_source: compile_terminal

