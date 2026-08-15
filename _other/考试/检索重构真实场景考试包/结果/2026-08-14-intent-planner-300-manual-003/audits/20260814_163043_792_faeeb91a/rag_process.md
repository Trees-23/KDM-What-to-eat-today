# RAG Process

audit_id: 20260814_163043_792_faeeb91a
timestamp: 2026-08-14T16:30:43.793
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:30:43.793
- end: 2026-08-14T16:30:43.793
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 9

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:30:49.344
- end: 2026-08-14T16:30:49.344
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5550
- attempt_count: 1
- response_hash: 302a3171693379dc07a7c021491f06cfb6bcab42d61119f55006efdf74b4158e
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:30:49.360
- end: 2026-08-14T16:30:49.360
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 6e836f1ecb30340f4beeeb514281972a455ce329e87961eb8c69bab606b880bb
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:30:49.360
- end: 2026-08-14T16:30:49.360
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:30:49.360+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:30:49.360
- end: 2026-08-14T16:30:49.360
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:30:49.360+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:30:49.361
- request_duration_ms: 5567
- success: True
- final_source: compile_terminal

