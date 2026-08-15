# RAG Process

audit_id: 20260813_200623_839_8badcddd
timestamp: 2026-08-13T20:06:23.840
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:06:23.841
- end: 2026-08-13T20:06:23.841
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:06:30.750
- end: 2026-08-13T20:06:30.750
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6910
- attempt_count: 1
- response_hash: 7df18d473e0bb22a579e7d557f0cd8fa1bfc25d4d1f49575dc51793a034c30a8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:06:30.757
- end: 2026-08-13T20:06:30.757
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: a46c56a1e4e8c53aaa3109e7b1f39ce80094a841031c3d71b1589c8356e86876
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:06:30.757
- end: 2026-08-13T20:06:30.757
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:06:30.757+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T20:06:30.757
- end: 2026-08-13T20:06:30.757
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:06:30.757+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T20:06:30.757
- request_duration_ms: 6916
- success: True
- final_source: compile_terminal

