# RAG Process

audit_id: 20260813_211742_043_971e6801
timestamp: 2026-08-13T21:17:42.046
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:17:42.046
- end: 2026-08-13T21:17:42.046
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 9

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:17:45.821
- end: 2026-08-13T21:17:45.821
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3774
- attempt_count: 1
- response_hash: d005d95642c029e2105af7a87a23347985a3d256166bf44371787917c3c2951a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:17:45.823
- end: 2026-08-13T21:17:45.823
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 11f888249c3807bb3a2eaeafff5f41bcbab3ac3d19c4799bcfef69694be8d1a2
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:17:45.824
- end: 2026-08-13T21:17:45.824
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:45.824+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:17:45.824
- end: 2026-08-13T21:17:45.824
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:45.824+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:17:45.824
- request_duration_ms: 3777
- success: True
- final_source: compile_terminal

