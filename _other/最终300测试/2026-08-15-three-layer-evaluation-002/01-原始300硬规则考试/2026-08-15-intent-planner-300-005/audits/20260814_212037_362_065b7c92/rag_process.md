# RAG Process

audit_id: 20260814_212037_362_065b7c92
timestamp: 2026-08-14T21:20:37.362
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T21:20:37.363
- end: 2026-08-14T21:20:37.363
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T21:20:41.030
- end: 2026-08-14T21:20:41.030
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['鸡肉'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3667
- attempt_count: 1
- response_hash: d3e162034f2da28b1fe680d737fe1e3a5c55cc852c3de97a55652547529b3b70
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T21:20:41.050
- end: 2026-08-14T21:20:41.050
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: d65d39911bb7e5ed6e7b5ed509d24bc21fe5ec5b581f03e378fea8f209d33b5e
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T21:20:41.051
- end: 2026-08-14T21:20:41.051
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:20:41.051+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T21:20:41.051
- end: 2026-08-14T21:20:41.051
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:20:41.051+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T21:20:41.051
- request_duration_ms: 3687
- success: True
- final_source: compile_terminal

