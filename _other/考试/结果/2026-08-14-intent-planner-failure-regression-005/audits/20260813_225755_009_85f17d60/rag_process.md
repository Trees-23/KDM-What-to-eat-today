# RAG Process

audit_id: 20260813_225755_009_85f17d60
timestamp: 2026-08-13T22:57:55.018
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:57:55.019
- end: 2026-08-13T22:57:55.019
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 13

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:57:59.823
- end: 2026-08-13T22:57:59.823
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: PREFERENCE_RECOMMEND
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': ['SICHUAN_STYLE'], 'ingredients': ['番茄'], 'preferences': ['LIGHT_FEEL'], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4803
- attempt_count: 1
- response_hash: 957d2452d07197205931ffca78c61ae63e81695b4364bbb45503b9189ee04218
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:57:59.917
- end: 2026-08-13T22:57:59.917
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T22:57:59.917+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:57:59.923
- end: 2026-08-13T22:57:59.923
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T22:57:59.917+00:00
- result_count: 32

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:57:59.930
- end: 2026-08-13T22:57:59.930
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:57:59.930+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:57:59.935
- end: 2026-08-13T22:57:59.935
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:57:59.930+00:00
- result_count: 12

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T22:57:59.935
- end: 2026-08-13T22:57:59.935
- duration_ms: 0
- compile_action: NO_PREFERENCE_RESULTS
- reason: HARD_SCOPE_EMPTY
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T22:57:59.935
- request_duration_ms: 4916
- success: True
- final_source: compile_terminal

