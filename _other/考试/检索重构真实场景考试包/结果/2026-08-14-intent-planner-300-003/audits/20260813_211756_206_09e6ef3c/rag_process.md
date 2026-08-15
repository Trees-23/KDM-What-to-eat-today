# RAG Process

audit_id: 20260813_211756_206_09e6ef3c
timestamp: 2026-08-13T21:17:56.207
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:17:56.207
- end: 2026-08-13T21:17:56.207
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 9

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:18:00.602
- end: 2026-08-13T21:18:00.602
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4394
- attempt_count: 1
- response_hash: 065534f3151a588fd0c28a9f3df305c0c0da3cda6f7bc2789b74ed1b23e9b7a1
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:18:00.605
- end: 2026-08-13T21:18:00.605
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 7df3f0dc5749160777e03a4f4a37bffd31853b180dbeaf40c8e7ff02c1954e55
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:18:00.605
- end: 2026-08-13T21:18:00.605
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:18:00.605+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:18:00.605
- end: 2026-08-13T21:18:00.605
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:18:00.605+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:18:00.606
- request_duration_ms: 4398
- success: True
- final_source: compile_terminal

