# RAG Process

audit_id: 20260813_205131_645_a0327ab1
timestamp: 2026-08-13T20:51:31.656
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:51:31.656
- end: 2026-08-13T20:51:31.656
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:51:35.810
- end: 2026-08-13T20:51:35.810
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4154
- attempt_count: 1
- response_hash: 5acdc052c257a23a155c477b3e03a62b4904ccf7f6c2eea9b1cace5ba6900df3
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:51:35.817
- end: 2026-08-13T20:51:35.817
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 42ad5eeeae9b6055b05113016dca0781bb1fa59e6a03efab753ee004bb960190
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:51:35.818
- end: 2026-08-13T20:51:35.818
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:51:35.818+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-13T20:51:35.822
- end: 2026-08-13T20:51:35.822
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:51:35.818+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-13T20:51:35.822
- request_duration_ms: 4165
- success: True
- final_source: compile_terminal

