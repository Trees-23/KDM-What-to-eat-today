# RAG Process

audit_id: 20260813_202714_249_f93120e2
timestamp: 2026-08-13T20:27:14.260
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:27:14.260
- end: 2026-08-13T20:27:14.260
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 38

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:27:17.210
- end: 2026-08-13T20:27:17.210
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3591
- attempt_count: 1
- response_hash: bc518305dcfa8062d868030588c4f8fb0b98f60bc3870411dc55e942b02b3c66
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: CLARIFY
- start: 2026-08-13T20:27:17.215
- end: 2026-08-13T20:27:17.215
- duration_ms: 0
- compile_action: CLARIFY_OR_OUT_OF_SCOPE
- reason: ENTITY_AMBIGUOUS
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T20:27:17.216
- request_duration_ms: 2955
- success: True
- final_source: compile_terminal

