# RAG Process

audit_id: 20260814_161109_165_0f61b271
timestamp: 2026-08-14T16:11:09.166
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:11:09.168
- end: 2026-08-14T16:11:09.168
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 25

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:11:16.456
- end: 2026-08-14T16:11:16.456
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: PREFERENCE_RECOMMEND
- confidence: 0.9
- normalized_slots: {'step_number': None, 'cuisines': ['SICHUAN_STYLE'], 'ingredients': ['豆腐'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 7288
- attempt_count: 1
- response_hash: f4a4077427eb418206be03f678d6041ba328b3126a14d1185479f6d1f6638da3
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / recommendation_constraints
- stage: recommendation_constraints
- status: compiled
- start: 2026-08-14T16:11:16.486
- end: 2026-08-14T16:11:16.486
- duration_ms: 0
- policy_version: recommendation_constraints_v1
- hard_filters: {'cuisines': ['SICHUAN_STYLE'], 'verified_ingredient_ids': ['201003918'], 'methods': [], 'excluded_methods': [], 'required_cooking_appliances': [], 'excluded_cooking_appliances': [], 'exclusive_cooking_appliances': [], 'max_total_minutes': None}
- soft_preferences: {'methods': [], 'tools': [], 'preferences': [], 'meal_context': [], 'prefer_shorter_time': False, 'target_servings': None}
- decisions: []
- clarification_reason: None

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:11:16.501
- end: 2026-08-14T16:11:16.501
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-14T16:11:16.501+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T16:11:16.508
- end: 2026-08-14T16:11:16.508
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-14T16:11:16.501+00:00
- result_count: 32

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:11:16.513
- end: 2026-08-14T16:11:16.513
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:11:16.513+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T16:11:16.518
- end: 2026-08-14T16:11:16.518
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:11:16.513+00:00
- result_count: 3

## Event / intent_compile
- stage: intent_compile
- status: TERMINAL
- start: 2026-08-14T16:11:16.519
- end: 2026-08-14T16:11:16.519
- duration_ms: 0
- compile_action: NO_PREFERENCE_RESULTS
- reason: HARD_SCOPE_EMPTY
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': []}

## Request Complete
- request_end: 2026-08-14T16:11:16.519
- request_duration_ms: 7351
- success: True
- final_source: compile_terminal

