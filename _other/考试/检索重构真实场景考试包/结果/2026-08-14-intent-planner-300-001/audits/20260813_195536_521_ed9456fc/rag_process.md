# RAG Process

audit_id: 20260813_195536_521_ed9456fc
timestamp: 2026-08-13T19:55:36.522
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:55:36.522
- end: 2026-08-13T19:55:36.522
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 15

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:55:40.300
- end: 2026-08-13T19:55:40.300
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: PREFERENCE_RECOMMEND
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': ['SICHUAN_STYLE'], 'ingredients': [], 'preferences': ['LOW_OIL_FEEL'], 'meal_context': ['BREAKFAST'], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3778
- attempt_count: 1
- response_hash: f3d7eeff7a2bda34f2feafea06ced5178703608456c0a4476fcdccd3ab91cbb1
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:55:40.330
- end: 2026-08-13T19:55:40.330
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T19:55:40.330+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:55:40.333
- end: 2026-08-13T19:55:40.333
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T19:55:40.330+00:00
- result_count: 32

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:55:40.333
- end: 2026-08-13T19:55:40.333
- duration_ms: 0
- compile_action: PREFERENCE_RECOMMEND
- reason: None
- query_plan_hash: c2800b1f9eb483aa42c8a7d42c742c6014c2119487aaf254e6db0d80e084ba70
- claim_policy: {'hard_constraints': ['validated_recipe_scope'], 'soft_preferences': ['LOW_OIL_FEEL', 'BREAKFAST'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / restricted_vector
- stage: restricted_vector
- status: selected
- start: 2026-08-13T19:55:40.968
- end: 2026-08-13T19:55:40.968
- duration_ms: 0
- parent_count: 5
- vector_scope: candidate_parents
- expected_parent_type: Recipe
- filter_batch_count: 2

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 6070
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 0
- text_evidence_count: 5
- limitation_count: 0
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Generation Config
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 20204
- response_chars: 769
- response_hash: d629bdccbfd3da08

## Final Output
- answer_chars: 769
- answer_hash: d629bdccbfd3da08
- success: True

## Request Complete
- request_end: 2026-08-13T19:56:01.173
- request_duration_ms: 24650
- success: True
- final_source: generation

