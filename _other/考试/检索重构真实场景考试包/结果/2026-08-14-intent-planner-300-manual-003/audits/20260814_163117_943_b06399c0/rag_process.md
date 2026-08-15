# RAG Process

audit_id: 20260814_163117_943_b06399c0
timestamp: 2026-08-14T16:31:17.944
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:31:17.944
- end: 2026-08-14T16:31:17.944
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:31:21.535
- end: 2026-08-14T16:31:21.535
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3591
- attempt_count: 1
- response_hash: d76d618df926ee36fa44897fe866a3d917c7e4f9f0e54c42a70f7bcaf7258301
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:31:21.550
- end: 2026-08-14T16:31:21.550
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 8eac1850c425a36f563174d816ccf01dda0e57906076e8bb174a17eeae660735
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:31:21.551
- end: 2026-08-14T16:31:21.551
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:31:21.551+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:31:21.551
- end: 2026-08-14T16:31:21.551
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:31:21.551+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:31:21.551
- request_duration_ms: 3607
- success: True
- final_source: compile_terminal

