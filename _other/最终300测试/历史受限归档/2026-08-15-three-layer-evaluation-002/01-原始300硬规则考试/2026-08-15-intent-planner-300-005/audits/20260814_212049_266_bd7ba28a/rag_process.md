# RAG Process

audit_id: 20260814_212049_266_bd7ba28a
timestamp: 2026-08-14T21:20:49.267
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T21:20:49.267
- end: 2026-08-14T21:20:49.267
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T21:20:52.892
- end: 2026-08-14T21:20:52.892
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['土豆'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3624
- attempt_count: 1
- response_hash: 3b9ce58b22b37d3d74e848ad581b92af91b7a611a6ba08f017e898d746c22712
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T21:20:52.899
- end: 2026-08-14T21:20:52.899
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 0c4d511ef3bb366ebc11daa4919872543eb40da4eda5a78aa74eb53b4f1aefba
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T21:20:52.900
- end: 2026-08-14T21:20:52.900
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:20:52.900+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T21:20:52.900
- end: 2026-08-14T21:20:52.900
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:20:52.900+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T21:20:52.900
- request_duration_ms: 3632
- success: True
- final_source: compile_terminal

