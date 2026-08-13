# RAG Process

audit_id: 20260813_211708_592_09c6ef1a
timestamp: 2026-08-13T21:17:08.593
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:17:08.594
- end: 2026-08-13T21:17:08.594
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 10

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:17:12.204
- end: 2026-08-13T21:17:12.204
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3610
- attempt_count: 1
- response_hash: 741ef86d7f70c451a1b36af95f80841429920a80f14effe5afbb9319044cf70a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:17:12.207
- end: 2026-08-13T21:17:12.207
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 0c617862136ab3f567b417939974bd4dda876c21996bd87f9a6a344280fd732c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:17:12.207
- end: 2026-08-13T21:17:12.207
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:12.207+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:17:12.207
- end: 2026-08-13T21:17:12.207
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:12.207+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:17:12.207
- request_duration_ms: 3613
- success: True
- final_source: compile_terminal

