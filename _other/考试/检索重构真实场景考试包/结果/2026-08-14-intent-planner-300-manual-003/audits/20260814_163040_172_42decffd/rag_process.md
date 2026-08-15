# RAG Process

audit_id: 20260814_163040_172_42decffd
timestamp: 2026-08-14T16:30:40.182
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:30:40.182
- end: 2026-08-14T16:30:40.182
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:30:43.775
- end: 2026-08-14T16:30:43.775
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['玉米'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3593
- attempt_count: 1
- response_hash: 7b98300dde1a50b8d32de7ed31453965641fa2cc18b02c2855c8d77050b3ec39
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:30:43.791
- end: 2026-08-14T16:30:43.791
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: beeec1f7389a977fb34f293f824f0b9c7da26f25a8e09dcbd0de14472c4fee0c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:30:43.791
- end: 2026-08-14T16:30:43.791
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:30:43.791+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:30:43.791
- end: 2026-08-14T16:30:43.791
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:30:43.791+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:30:43.792
- request_duration_ms: 3609
- success: True
- final_source: compile_terminal

