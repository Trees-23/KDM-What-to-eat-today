# RAG Process

audit_id: 20260813_191355_301_bbe0681e
timestamp: 2026-08-13T19:13:55.301
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:13:55.311
- end: 2026-08-13T19:13:55.311
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 38

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:13:59.678
- end: 2026-08-13T19:13:59.678
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4367
- attempt_count: 1
- response_hash: 141eae2e48dffd4a3f3c48626c3247bbbdde7c1b7b3ac44d4171c4f9fea7b0d2
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: CLARIFY
- start: 2026-08-13T19:13:59.687
- end: 2026-08-13T19:13:59.687
- duration_ms: 0
- compile_action: CLARIFY_OR_OUT_OF_SCOPE
- reason: ENTITY_AMBIGUOUS
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T19:13:59.687
- request_duration_ms: 4375
- success: True
- final_source: compile_terminal

