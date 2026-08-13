# RAG Process

audit_id: 20260813_224018_460_fb3b19a5
timestamp: 2026-08-13T22:40:18.460
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:40:18.460
- end: 2026-08-13T22:40:18.460
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 12

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:40:22.154
- end: 2026-08-13T22:40:22.154
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: PREFERENCE_RECOMMEND
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': ['SICHUAN_STYLE'], 'ingredients': [], 'preferences': ['MILD_FLAVOR'], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3694
- attempt_count: 1
- response_hash: 3cd994cb080814a382e0584cfa68eabd209b55725af0687c7b305bfccba0e27f
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:40:22.196
- end: 2026-08-13T22:40:22.196
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T22:40:22.196+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:40:22.199
- end: 2026-08-13T22:40:22.199
- duration_ms: 0
- template_id: recipe_cuisine_filter_v1
- intent: RECIPE_CUISINE_FILTER
- database_timestamp: 2026-08-13T22:40:22.196+00:00
- result_count: 32

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:40:22.199
- end: 2026-08-13T22:40:22.199
- duration_ms: 0
- compile_action: PREFERENCE_RECOMMEND
- reason: None
- query_plan_hash: c2800b1f9eb483aa42c8a7d42c742c6014c2119487aaf254e6db0d80e084ba70
- claim_policy: {'hard_constraints': ['validated_recipe_scope'], 'soft_preferences': ['MILD_FLAVOR'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / restricted_vector
- stage: restricted_vector
- status: selected
- start: 2026-08-13T22:40:22.826
- end: 2026-08-13T22:40:22.826
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
- context_chars: 4576
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
- duration_ms: 11572
- response_chars: 418
- response_hash: a7ee135f254a35a8

## Final Output
- answer_chars: 418
- answer_hash: a7ee135f254a35a8
- success: True

## Request Complete
- request_end: 2026-08-13T22:40:34.401
- request_duration_ms: 15940
- success: True
- final_source: generation

