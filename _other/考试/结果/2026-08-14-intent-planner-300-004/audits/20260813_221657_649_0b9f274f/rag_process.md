# RAG Process

audit_id: 20260813_221657_649_0b9f274f
timestamp: 2026-08-13T22:16:57.650
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:16:57.651
- end: 2026-08-13T22:16:57.651
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:17:01.094
- end: 2026-08-13T22:17:01.094
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4193
- attempt_count: 1
- response_hash: d8d65d97292c56d1ee1e9dce55840d9ce0a3d6b99cbd65f34f0667366f45a4ad
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:17:01.102
- end: 2026-08-13T22:17:01.102
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 5ff30386933dc3d2b5684e7f7ad09fd1622e4aa3d9feb6801dd6370d56f4fcaf
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:17:01.103
- end: 2026-08-13T22:17:01.103
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:17:01.103+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:17:01.107
- end: 2026-08-13T22:17:01.107
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:17:01.103+00:00
- result_count: 6

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:01.108
- end: 2026-08-13T22:17:01.108
- duration_ms: 0
- entity_id: 201003916
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:01.127
- end: 2026-08-13T22:17:01.127
- duration_ms: 0
- parent_id: 201003916
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:01.127
- end: 2026-08-13T22:17:01.127
- duration_ms: 0
- entity_id: 201004841
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:01.137
- end: 2026-08-13T22:17:01.137
- duration_ms: 0
- parent_id: 201004841
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:01.137
- end: 2026-08-13T22:17:01.137
- duration_ms: 0
- entity_id: 201005653
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:01.144
- end: 2026-08-13T22:17:01.144
- duration_ms: 0
- parent_id: 201005653
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 5098
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 3
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
- duration_ms: 8336
- response_chars: 272
- response_hash: 1387b1ffb91f7c1c

## Final Output
- answer_chars: 272
- answer_hash: 1387b1ffb91f7c1c
- success: True

## Request Complete
- request_end: 2026-08-13T22:17:09.482
- request_duration_ms: 11831
- success: True
- final_source: generation

