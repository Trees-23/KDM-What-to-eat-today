# RAG Process

audit_id: 20260813_213222_372_9723b9eb
timestamp: 2026-08-13T21:32:22.373
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:32:22.373
- end: 2026-08-13T21:32:22.373
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 13

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:32:31.393
- end: 2026-08-13T21:32:31.393
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: PREFERENCE_RECOMMEND
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': ['SICHUAN_STYLE'], 'ingredients': ['番茄'], 'preferences': ['LIGHT_FEEL'], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 9738
- attempt_count: 1
- response_hash: 77d58bfab4df0377da67b27619dac0d87e60d6d2de654ae77ad5ca191c8e8dd5
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:32:31.443
- end: 2026-08-13T21:32:31.443
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T21:32:31.443+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T21:32:31.448
- end: 2026-08-13T21:32:31.448
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T21:32:31.443+00:00
- result_count: 32

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:32:31.451
- end: 2026-08-13T21:32:31.451
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:32:31.451+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T21:32:31.453
- end: 2026-08-13T21:32:31.453
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:32:31.451+00:00
- result_count: 2

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-13T21:32:31.453
- end: 2026-08-13T21:32:31.453
- duration_ms: 0
- compile_action: NO_PREFERENCE_RESULTS
- reason: HARD_SCOPE_EMPTY
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-13T21:32:31.453
- request_duration_ms: 9080
- success: True
- final_source: compile_terminal

