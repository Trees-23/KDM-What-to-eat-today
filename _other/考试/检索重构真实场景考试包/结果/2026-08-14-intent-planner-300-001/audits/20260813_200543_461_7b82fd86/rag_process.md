# RAG Process

audit_id: 20260813_200543_461_7b82fd86
timestamp: 2026-08-13T20:05:43.462
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:05:43.464
- end: 2026-08-13T20:05:43.464
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:05:50.871
- end: 2026-08-13T20:05:50.871
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 7407
- attempt_count: 1
- response_hash: a726b3d325bb7b1e619490b104e38e57eaf024986a2bfd93fc4036fb11cb8c9a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:05:50.877
- end: 2026-08-13T20:05:50.877
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: d65d39911bb7e5ed6e7b5ed509d24bc21fe5ec5b581f03e378fea8f209d33b5e
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:05:50.877
- end: 2026-08-13T20:05:50.877
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:05:50.877+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T20:05:50.877
- end: 2026-08-13T20:05:50.877
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:05:50.877+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T20:05:50.877
- request_duration_ms: 7413
- success: True
- final_source: compile_terminal

