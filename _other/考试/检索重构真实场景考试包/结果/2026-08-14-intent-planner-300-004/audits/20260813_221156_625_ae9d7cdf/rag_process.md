# RAG Process

audit_id: 20260813_221156_625_ae9d7cdf
timestamp: 2026-08-13T22:11:56.625
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:11:56.625
- end: 2026-08-13T22:11:56.625
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:11:59.985
- end: 2026-08-13T22:11:59.985
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3359
- attempt_count: 1
- response_hash: d7f9b5dc6ef1413ed2aa44a3c5cb3ece0a8b4bef15d624999c096fc7d3c9ac23
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:11:59.991
- end: 2026-08-13T22:11:59.991
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: dc18a1b1340818bc8ba14689731d3932a55ed07d2d3f03a8f230b38a6770e0ff
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:11:59.992
- end: 2026-08-13T22:11:59.992
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:11:59.992+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:11:59.998
- end: 2026-08-13T22:11:59.998
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:11:59.992+00:00
- result_count: 12

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:59.999
- end: 2026-08-13T22:11:59.999
- duration_ms: 0
- entity_id: 201002555
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:00.012
- end: 2026-08-13T22:12:00.012
- duration_ms: 0
- parent_id: 201002555
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:00.012
- end: 2026-08-13T22:12:00.012
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:00.020
- end: 2026-08-13T22:12:00.020
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:00.020
- end: 2026-08-13T22:12:00.020
- duration_ms: 0
- entity_id: 201003224
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:00.026
- end: 2026-08-13T22:12:00.026
- duration_ms: 0
- parent_id: 201003224
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:00.027
- end: 2026-08-13T22:12:00.027
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:00.033
- end: 2026-08-13T22:12:00.033
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:00.033
- end: 2026-08-13T22:12:00.033
- duration_ms: 0
- entity_id: 201003844
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:00.039
- end: 2026-08-13T22:12:00.039
- duration_ms: 0
- parent_id: 201003844
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:00.039
- end: 2026-08-13T22:12:00.039
- duration_ms: 0
- entity_id: 201004746
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:00.046
- end: 2026-08-13T22:12:00.046
- duration_ms: 0
- parent_id: 201004746
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:00.046
- end: 2026-08-13T22:12:00.046
- duration_ms: 0
- entity_id: 201005049
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:00.052
- end: 2026-08-13T22:12:00.052
- duration_ms: 0
- parent_id: 201005049
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:00.053
- end: 2026-08-13T22:12:00.053
- duration_ms: 0
- entity_id: 201005181
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:00.059
- end: 2026-08-13T22:12:00.059
- duration_ms: 0
- parent_id: 201005181
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:00.059
- end: 2026-08-13T22:12:00.059
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:00.066
- end: 2026-08-13T22:12:00.066
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:00.066
- end: 2026-08-13T22:12:00.066
- duration_ms: 0
- entity_id: 201005528
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:00.073
- end: 2026-08-13T22:12:00.073
- duration_ms: 0
- parent_id: 201005528
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:00.073
- end: 2026-08-13T22:12:00.073
- duration_ms: 0
- entity_id: 201005653
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:00.082
- end: 2026-08-13T22:12:00.082
- duration_ms: 0
- parent_id: 201005653
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:00.082
- end: 2026-08-13T22:12:00.082
- duration_ms: 0
- entity_id: 201005669
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:00.096
- end: 2026-08-13T22:12:00.096
- duration_ms: 0
- parent_id: 201005669
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 14849
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 12
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
- duration_ms: 9378
- response_chars: 325
- response_hash: 9ecfd940ded3d8cc

## Final Output
- answer_chars: 325
- answer_hash: 9ecfd940ded3d8cc
- success: True

## Request Complete
- request_end: 2026-08-13T22:12:09.477
- request_duration_ms: 12851
- success: True
- final_source: generation

