# RAG Process

audit_id: 20260814_162955_189_4a113a74
timestamp: 2026-08-14T16:29:55.201
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:29:55.202
- end: 2026-08-14T16:29:55.202
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:29:59.238
- end: 2026-08-14T16:29:59.238
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['鲈鱼'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4036
- attempt_count: 1
- response_hash: ed0b98f658c981abda229ea5b4682ccc1ff5d9e3adee4895660e30d6bc40b0cb
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:29:59.265
- end: 2026-08-14T16:29:59.265
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 17fe136647461470fc143c3f8c558a7986e47691be3fe9f9611c76f568471411
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:29:59.265
- end: 2026-08-14T16:29:59.265
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:29:59.265+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:29:59.265
- end: 2026-08-14T16:29:59.265
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:29:59.265+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:29:59.266
- request_duration_ms: 4064
- success: True
- final_source: compile_terminal

