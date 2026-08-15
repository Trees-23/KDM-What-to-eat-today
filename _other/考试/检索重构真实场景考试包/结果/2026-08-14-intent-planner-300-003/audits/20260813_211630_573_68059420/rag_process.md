# RAG Process

audit_id: 20260813_211630_573_68059420
timestamp: 2026-08-13T21:16:30.574
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:16:30.575
- end: 2026-08-13T21:16:30.575
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 9

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:16:34.849
- end: 2026-08-13T21:16:34.849
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4274
- attempt_count: 1
- response_hash: d7f9b5dc6ef1413ed2aa44a3c5cb3ece0a8b4bef15d624999c096fc7d3c9ac23
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:16:34.856
- end: 2026-08-13T21:16:34.856
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: dc18a1b1340818bc8ba14689731d3932a55ed07d2d3f03a8f230b38a6770e0ff
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:16:34.856
- end: 2026-08-13T21:16:34.856
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:16:34.856+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:16:34.857
- end: 2026-08-13T21:16:34.857
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:16:34.856+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:16:34.857
- request_duration_ms: 4281
- success: True
- final_source: compile_terminal

