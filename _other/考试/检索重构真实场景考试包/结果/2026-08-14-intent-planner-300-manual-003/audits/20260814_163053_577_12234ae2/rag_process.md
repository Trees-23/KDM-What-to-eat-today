# RAG Process

audit_id: 20260814_163053_577_12234ae2
timestamp: 2026-08-14T16:30:53.577
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:30:53.578
- end: 2026-08-14T16:30:53.578
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 9

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:30:57.776
- end: 2026-08-14T16:30:57.776
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['西兰花'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4198
- attempt_count: 1
- response_hash: a11f5342d3141740e652ebb59ad2ace7b68f8eb8b3cefd13e73d412870604a67
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:30:57.793
- end: 2026-08-14T16:30:57.793
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 58cb008445dfe787889b9299f8ca816668e4b830116e873a821c8a831964b7bb
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:30:57.793
- end: 2026-08-14T16:30:57.793
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:30:57.793+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:30:57.793
- end: 2026-08-14T16:30:57.793
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:30:57.793+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:30:57.793
- request_duration_ms: 4215
- success: True
- final_source: compile_terminal

