# RAG Process

audit_id: 20260814_163057_794_1eefbc6e
timestamp: 2026-08-14T16:30:57.795
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:30:57.796
- end: 2026-08-14T16:30:57.796
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:31:02.485
- end: 2026-08-14T16:31:02.485
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['黄瓜'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6311
- attempt_count: 1
- response_hash: 5a0d55c88b6097fe7f09b5a0c0f697bc39d65615c0bb280f8896030978f2fb58
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:31:02.502
- end: 2026-08-14T16:31:02.502
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: e71a3c5f96904496a022cbe7edbe063a605d5ae4d4fb43f5c87aad3d053b53ee
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:31:02.502
- end: 2026-08-14T16:31:02.502
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:31:02.502+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:31:02.502
- end: 2026-08-14T16:31:02.502
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:31:02.502+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:31:02.502
- request_duration_ms: 4707
- success: True
- final_source: compile_terminal

