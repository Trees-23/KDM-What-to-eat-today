# RAG Process

audit_id: 20260814_163130_013_56e78520
timestamp: 2026-08-14T16:31:30.014
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:31:30.015
- end: 2026-08-14T16:31:30.015
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 9

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:31:35.242
- end: 2026-08-14T16:31:35.242
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['干豆腐'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6870
- attempt_count: 1
- response_hash: 438cc4dcf9aa1aa0eb552e6f1814804e3c366ee30e2153dea8aa554c9d659013
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:31:35.251
- end: 2026-08-14T16:31:35.251
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 7df3f0dc5749160777e03a4f4a37bffd31853b180dbeaf40c8e7ff02c1954e55
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:31:35.251
- end: 2026-08-14T16:31:35.251
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:31:35.251+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:31:35.252
- end: 2026-08-14T16:31:35.252
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:31:35.251+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:31:35.252
- request_duration_ms: 5237
- success: True
- final_source: compile_terminal

