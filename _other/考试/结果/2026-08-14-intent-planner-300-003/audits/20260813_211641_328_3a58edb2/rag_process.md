# RAG Process

audit_id: 20260813_211641_328_3a58edb2
timestamp: 2026-08-13T21:16:41.330
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:16:41.330
- end: 2026-08-13T21:16:41.330
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:16:44.860
- end: 2026-08-13T21:16:44.860
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3530
- attempt_count: 1
- response_hash: b622257475bd5b42861c5b49ec31c1f58fef70fe8c4879e3963a85322558060b
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:16:44.863
- end: 2026-08-13T21:16:44.863
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 45e97a845eca82470999f7a950d563d21d600438c454ecaaba62d8b2e5f3d813
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:16:44.863
- end: 2026-08-13T21:16:44.863
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:16:44.863+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:16:44.863
- end: 2026-08-13T21:16:44.863
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:16:44.863+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:16:44.863
- request_duration_ms: 3533
- success: True
- final_source: compile_terminal

