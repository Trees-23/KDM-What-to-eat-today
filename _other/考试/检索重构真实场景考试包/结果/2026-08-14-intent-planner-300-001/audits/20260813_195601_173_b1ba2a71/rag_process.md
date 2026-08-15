# RAG Process

audit_id: 20260813_195601_173_b1ba2a71
timestamp: 2026-08-13T19:56:01.176
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:56:01.177
- end: 2026-08-13T19:56:01.177
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 13

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:56:04.670
- end: 2026-08-13T19:56:04.670
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: PREFERENCE_RECOMMEND
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': ['SICHUAN_STYLE'], 'ingredients': ['番茄'], 'preferences': ['LIGHT_FEEL'], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3494
- attempt_count: 1
- response_hash: 98d19a2ee57b0f476a39c2524512180b3feaced167dae150ac035d8bb36a3557
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:56:04.703
- end: 2026-08-13T19:56:04.703
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T19:56:04.703+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:56:04.706
- end: 2026-08-13T19:56:04.706
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T19:56:04.703+00:00
- result_count: 32

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:56:04.711
- end: 2026-08-13T19:56:04.711
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:56:04.711+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:56:04.713
- end: 2026-08-13T19:56:04.713
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:56:04.711+00:00
- result_count: 2

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T19:56:04.713
- end: 2026-08-13T19:56:04.713
- duration_ms: 0
- compile_action: NO_PREFERENCE_RESULTS
- reason: HARD_SCOPE_EMPTY
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T19:56:04.713
- request_duration_ms: 3536
- success: True
- final_source: compile_terminal

