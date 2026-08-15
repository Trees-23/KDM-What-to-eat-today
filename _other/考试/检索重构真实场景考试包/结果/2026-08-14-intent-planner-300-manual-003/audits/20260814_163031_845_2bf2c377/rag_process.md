# RAG Process

audit_id: 20260814_163031_845_2bf2c377
timestamp: 2026-08-14T16:30:31.854
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:30:31.855
- end: 2026-08-14T16:30:31.855
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 10

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:30:35.763
- end: 2026-08-14T16:30:35.763
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.94
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['普通面条'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3907
- attempt_count: 1
- response_hash: 944b22b60918698e6569b13d016431c142aeb57ff7d853b5caeff51616c581e4
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:30:35.777
- end: 2026-08-14T16:30:35.777
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 0c617862136ab3f567b417939974bd4dda876c21996bd87f9a6a344280fd732c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:30:35.777
- end: 2026-08-14T16:30:35.777
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:30:35.777+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:30:35.777
- end: 2026-08-14T16:30:35.777
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:30:35.777+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:30:35.777
- request_duration_ms: 3922
- success: True
- final_source: compile_terminal

