# RAG Process

audit_id: 20260813_224034_401_7d70b38d
timestamp: 2026-08-13T22:40:34.402
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:40:34.402
- end: 2026-08-13T22:40:34.402
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 13

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:40:37.971
- end: 2026-08-13T22:40:37.971
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: PREFERENCE_RECOMMEND
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': ['SICHUAN_STYLE'], 'ingredients': [], 'preferences': ['LIGHT_FEEL'], 'meal_context': ['DINNER'], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3569
- attempt_count: 1
- response_hash: 2c540988d4981da0a15d1c1940881e31bf8658b59d5447250af41ac2efd23ee0
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:40:38.022
- end: 2026-08-13T22:40:38.022
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T22:40:38.022+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:40:38.026
- end: 2026-08-13T22:40:38.026
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T22:40:38.022+00:00
- result_count: 32

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:40:38.026
- end: 2026-08-13T22:40:38.026
- duration_ms: 0
- compile_action: PREFERENCE_RECOMMEND
- reason: None
- query_plan_hash: c2800b1f9eb483aa42c8a7d42c742c6014c2119487aaf254e6db0d80e084ba70
- claim_policy: {'hard_constraints': ['validated_recipe_scope'], 'soft_preferences': ['LIGHT_FEEL', 'DINNER'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / restricted_vector
- stage: restricted_vector
- status: selected
- start: 2026-08-13T22:40:38.823
- end: 2026-08-13T22:40:38.823
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
- context_chars: 6164
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
- duration_ms: 10779
- response_chars: 366
- response_hash: 4b53bbc7bf17c876

## Final Output
- answer_chars: 366
- answer_hash: 4b53bbc7bf17c876
- success: True

## Request Complete
- request_end: 2026-08-13T22:40:49.603
- request_duration_ms: 15200
- success: True
- final_source: generation

