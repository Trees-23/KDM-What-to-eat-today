# RAG Process

audit_id: 20260813_211749_217_b9888cfd
timestamp: 2026-08-13T21:17:49.228
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:17:49.228
- end: 2026-08-13T21:17:49.228
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:17:52.734
- end: 2026-08-13T21:17:52.734
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3506
- attempt_count: 1
- response_hash: ce291ccec8a64c0f9eb707fbaba4796e0d070e9d8fea284fb2b517cf4f7f9d89
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:17:52.738
- end: 2026-08-13T21:17:52.738
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: ae4d9ca251149a902687bbebd9ef0155d50473f044ba014041daf05261f17fd9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:17:52.739
- end: 2026-08-13T21:17:52.739
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:52.739+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:17:52.739
- end: 2026-08-13T21:17:52.739
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:52.739+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:17:52.739
- request_duration_ms: 3510
- success: True
- final_source: compile_terminal

