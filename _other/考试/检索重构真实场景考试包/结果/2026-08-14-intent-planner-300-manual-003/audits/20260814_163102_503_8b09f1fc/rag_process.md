# RAG Process

audit_id: 20260814_163102_503_8b09f1fc
timestamp: 2026-08-14T16:31:02.503
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:31:02.504
- end: 2026-08-14T16:31:02.504
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:31:07.142
- end: 2026-08-14T16:31:07.142
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['豆角'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4638
- attempt_count: 1
- response_hash: c312f4f502875c3a68c3d8eb95fcd7a961fe4654748faf0e7863aad3a243a5db
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:31:07.160
- end: 2026-08-14T16:31:07.160
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: f71c477cc83a703d82c68977bd4642ec866991bb81d40114c6efbe8c11029e76
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:31:07.160
- end: 2026-08-14T16:31:07.160
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:31:07.160+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:31:07.160
- end: 2026-08-14T16:31:07.160
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:31:07.160+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:31:07.160
- request_duration_ms: 4656
- success: True
- final_source: compile_terminal

