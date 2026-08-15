# RAG Process

audit_id: 20260814_212151_965_3f42fa43
timestamp: 2026-08-14T21:21:51.965
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T21:21:51.965
- end: 2026-08-14T21:21:51.965
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T21:21:55.671
- end: 2026-08-14T21:21:55.671
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3706
- attempt_count: 1
- response_hash: 8a915cdc63643cd7fb7b39b372600436342ec685dad33e6017bb8ba43478cfda
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T21:21:55.685
- end: 2026-08-14T21:21:55.685
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 97b08cfe77feae6bbfc35a14cee179b916ea17421914ab40d814ace6d4810855
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T21:21:55.686
- end: 2026-08-14T21:21:55.686
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:21:55.686+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T21:21:55.686
- end: 2026-08-14T21:21:55.686
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:21:55.686+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T21:21:55.686
- request_duration_ms: 3720
- success: True
- final_source: compile_terminal

