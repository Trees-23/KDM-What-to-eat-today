# RAG Process

audit_id: 20260814_212044_696_e9376cb2
timestamp: 2026-08-14T21:20:44.697
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T21:20:44.697
- end: 2026-08-14T21:20:44.697
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T21:20:49.243
- end: 2026-08-14T21:20:49.243
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['豆腐'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4546
- attempt_count: 1
- response_hash: 2a0e79861798e5888bccbe7b2386036e590ec73b9918eaf2d1ba852ed4a8d93a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T21:20:49.265
- end: 2026-08-14T21:20:49.265
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 890120a2c84ebcc96303fb60436e87ae67dcaf7fe8cdee30bdb0c5058265a249
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T21:20:49.265
- end: 2026-08-14T21:20:49.265
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:20:49.265+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T21:20:49.265
- end: 2026-08-14T21:20:49.265
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:20:49.265+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T21:20:49.265
- request_duration_ms: 4568
- success: True
- final_source: compile_terminal

