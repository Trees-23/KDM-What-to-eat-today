# RAG Process

audit_id: 20260814_212100_450_d11e8004
timestamp: 2026-08-14T21:21:00.451
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T21:21:00.451
- end: 2026-08-14T21:21:00.451
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 7

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T21:21:04.591
- end: 2026-08-14T21:21:04.591
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['虾'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4140
- attempt_count: 1
- response_hash: d3296cdac7233384203c29d460621005dbe5d5aa09c644470d30236b58622a9d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T21:21:04.609
- end: 2026-08-14T21:21:04.609
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: a7f0ebc6e455415114ea01b7167b88b25107fd706779f78fa6b832c68d5bca92
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T21:21:04.609
- end: 2026-08-14T21:21:04.609
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:21:04.609+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T21:21:04.609
- end: 2026-08-14T21:21:04.609
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:21:04.609+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T21:21:04.609
- request_duration_ms: 4158
- success: True
- final_source: compile_terminal

