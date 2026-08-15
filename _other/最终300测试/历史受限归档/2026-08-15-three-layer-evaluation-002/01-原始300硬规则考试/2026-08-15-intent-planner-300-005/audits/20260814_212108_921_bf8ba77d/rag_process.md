# RAG Process

audit_id: 20260814_212108_921_bf8ba77d
timestamp: 2026-08-14T21:21:08.921
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T21:21:08.921
- end: 2026-08-14T21:21:08.921
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T21:21:12.528
- end: 2026-08-14T21:21:12.528
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['鳜鱼'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3606
- attempt_count: 1
- response_hash: 5fdeea947b02fbc08077d1d334dded5342935fc77d791ac42b18e00f0d4c100a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T21:21:12.543
- end: 2026-08-14T21:21:12.543
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 45e97a845eca82470999f7a950d563d21d600438c454ecaaba62d8b2e5f3d813
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T21:21:12.543
- end: 2026-08-14T21:21:12.543
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:21:12.543+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T21:21:12.544
- end: 2026-08-14T21:21:12.544
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:21:12.543+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T21:21:12.544
- request_duration_ms: 3622
- success: True
- final_source: compile_terminal

