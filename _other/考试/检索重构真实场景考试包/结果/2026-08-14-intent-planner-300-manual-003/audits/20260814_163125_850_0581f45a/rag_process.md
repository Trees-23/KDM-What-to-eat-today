# RAG Process

audit_id: 20260814_163125_850_0581f45a
timestamp: 2026-08-14T16:31:25.851
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:31:25.852
- end: 2026-08-14T16:31:25.852
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:31:29.995
- end: 2026-08-14T16:31:29.995
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['菠菜'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4143
- attempt_count: 1
- response_hash: 60047d73fb2cb249f011bb55bb4d5d71aca690178aaa4feb36f042061dae2ab3
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:31:30.012
- end: 2026-08-14T16:31:30.012
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 2772892dfb4d87f8a38115265dc4bac51f60809ee2740138c36b4d5169d5c78d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:31:30.012
- end: 2026-08-14T16:31:30.012
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:31:30.012+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:31:30.012
- end: 2026-08-14T16:31:30.012
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:31:30.012+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:31:30.012
- request_duration_ms: 4160
- success: True
- final_source: compile_terminal

