# RAG Process

audit_id: 20260813_221806_624_4d0559f8
timestamp: 2026-08-13T22:18:06.625
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:18:06.625
- end: 2026-08-13T22:18:06.625
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:18:10.887
- end: 2026-08-13T22:18:10.887
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4261
- attempt_count: 1
- response_hash: 9bc156194647ab277d22837955d7989613b9f2c47715b4066c923859d8360f60
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:18:10.895
- end: 2026-08-13T22:18:10.895
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: d70ccc30fda8afdea7b0f5b0ad25e1c6ab94d52271d86952c2c31678e252f411
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:18:10.896
- end: 2026-08-13T22:18:10.896
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:18:10.895+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:18:10.902
- end: 2026-08-13T22:18:10.902
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:18:10.895+00:00
- result_count: 2

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:18:10.902
- end: 2026-08-13T22:18:10.902
- duration_ms: 0
- entity_id: 201000257
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:18:10.923
- end: 2026-08-13T22:18:10.923
- duration_ms: 0
- parent_id: 201000257
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2120
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 1
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
- duration_ms: 4298
- response_chars: 140
- response_hash: 699d43f4aa2d5033

## Final Output
- answer_chars: 140
- answer_hash: 699d43f4aa2d5033
- success: True

## Request Complete
- request_end: 2026-08-13T22:18:15.223
- request_duration_ms: 8597
- success: True
- final_source: generation

