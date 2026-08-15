# RAG Process

audit_id: 20260813_200713_662_1d56f49c
timestamp: 2026-08-13T20:07:13.663
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:07:13.664
- end: 2026-08-13T20:07:13.664
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:07:17.287
- end: 2026-08-13T20:07:17.287
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3622
- attempt_count: 1
- response_hash: 98ee5567cb5dc57a8369a5e5848418d709487ba7be5245aa5dd10d36cabe539e
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:07:17.290
- end: 2026-08-13T20:07:17.290
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 2a356182272177af57ee55f6f61040941cdc431cba8d5e0ebf827fe50e7aaa56
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:07:17.291
- end: 2026-08-13T20:07:17.291
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:07:17.291+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T20:07:17.291
- end: 2026-08-13T20:07:17.291
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:07:17.291+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T20:07:17.291
- request_duration_ms: 3626
- success: True
- final_source: compile_terminal

