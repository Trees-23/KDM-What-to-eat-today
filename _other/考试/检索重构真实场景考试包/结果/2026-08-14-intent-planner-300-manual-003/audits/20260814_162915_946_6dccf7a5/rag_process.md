# RAG Process

audit_id: 20260814_162915_946_6dccf7a5
timestamp: 2026-08-14T16:29:15.947
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:29:15.947
- end: 2026-08-14T16:29:15.947
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:29:21.130
- end: 2026-08-14T16:29:21.130
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['猪肉'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5182
- attempt_count: 1
- response_hash: 2647f0bbc14098295769d6f3e54488ad4493d7901199d413399a98c518f48597
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:29:21.141
- end: 2026-08-14T16:29:21.141
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: f6b8b036635df75a09eec0e7691b6c666fc00a1539a3ee17db1d41bb596cb45c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:29:21.141
- end: 2026-08-14T16:29:21.141
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:29:21.141+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:29:21.141
- end: 2026-08-14T16:29:21.141
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:29:21.141+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:29:21.141
- request_duration_ms: 5194
- success: True
- final_source: compile_terminal

