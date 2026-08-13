# RAG Process

audit_id: 20260813_210802_325_c2242879
timestamp: 2026-08-13T21:08:02.325
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:08:02.326
- end: 2026-08-13T21:08:02.326
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 26

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:08:06.176
- end: 2026-08-13T21:08:06.176
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: PREFERENCE_RECOMMEND
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': ['SICHUAN_STYLE'], 'ingredients': [], 'preferences': ['LIGHT_FEEL'], 'meal_context': [], 'tools': [], 'methods': ['STEAM'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3850
- attempt_count: 1
- response_hash: 765fa9255287e31a95c0e8638293a14f3acf30927a5d2e484342d11d0fbed71d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:08:06.231
- end: 2026-08-13T21:08:06.231
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T21:08:06.231+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T21:08:06.234
- end: 2026-08-13T21:08:06.234
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T21:08:06.231+00:00
- result_count: 32

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:08:06.234
- end: 2026-08-13T21:08:06.234
- duration_ms: 0
- compile_action: PREFERENCE_RECOMMEND
- reason: None
- query_plan_hash: c2800b1f9eb483aa42c8a7d42c742c6014c2119487aaf254e6db0d80e084ba70
- claim_policy: {'hard_constraints': ['validated_recipe_scope'], 'soft_preferences': ['LIGHT_FEEL', 'STEAM'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / restricted_vector
- stage: restricted_vector
- status: selected
- start: 2026-08-13T21:08:06.339
- end: 2026-08-13T21:08:06.339
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
- context_chars: 6659
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
- duration_ms: 17579
- response_chars: 813
- response_hash: 2f78e98adbaee024

## Final Output
- answer_chars: 813
- answer_hash: 2f78e98adbaee024
- success: True

## Request Complete
- request_end: 2026-08-13T21:08:23.920
- request_duration_ms: 21594
- success: True
- final_source: generation

