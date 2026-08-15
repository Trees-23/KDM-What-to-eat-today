# RAG Process

audit_id: 20260814_212148_315_a78129ce
timestamp: 2026-08-14T21:21:48.316
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T21:21:48.316
- end: 2026-08-14T21:21:48.316
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 9

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T21:21:51.955
- end: 2026-08-14T21:21:51.955
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['大白菜'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3639
- attempt_count: 1
- response_hash: 217ff5463d9585a4a83c853e5c8648ea4cb1c1e44fd9618e1b11ed0f7834a3f5
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T21:21:51.963
- end: 2026-08-14T21:21:51.963
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 6e836f1ecb30340f4beeeb514281972a455ce329e87961eb8c69bab606b880bb
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T21:21:51.964
- end: 2026-08-14T21:21:51.964
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:21:51.964+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T21:21:51.964
- end: 2026-08-14T21:21:51.964
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:21:51.964+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T21:21:51.964
- request_duration_ms: 3648
- success: True
- final_source: compile_terminal

