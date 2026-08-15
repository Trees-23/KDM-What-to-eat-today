# RAG Process

audit_id: 20260814_154327_325_cfb007f2
timestamp: 2026-08-14T15:43:27.326
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:43:27.326
- end: 2026-08-14T15:43:27.326
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:43:37.099
- end: 2026-08-14T15:43:37.099
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 9773
- attempt_count: 1
- response_hash: c36d438b67657260765d29b3d8098ad56407195e004311514b90fd751c53ba75
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:43:37.131
- end: 2026-08-14T15:43:37.131
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 42036588ccf8b22437954129850e2631d00a620f4b34adc0c208be949870bbb2
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:43:37.131
- end: 2026-08-14T15:43:37.131
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:43:37.131+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:43:37.147
- end: 2026-08-14T15:43:37.147
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:43:37.131+00:00
- result_count: 50

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.148
- end: 2026-08-14T15:43:37.148
- duration_ms: 0
- entity_id: 201000001
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.161
- end: 2026-08-14T15:43:37.161
- duration_ms: 0
- parent_id: 201000001
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.161
- end: 2026-08-14T15:43:37.161
- duration_ms: 0
- entity_id: 201000290
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.167
- end: 2026-08-14T15:43:37.167
- duration_ms: 0
- parent_id: 201000290
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.168
- end: 2026-08-14T15:43:37.168
- duration_ms: 0
- entity_id: 201000411
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.174
- end: 2026-08-14T15:43:37.174
- duration_ms: 0
- parent_id: 201000411
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.175
- end: 2026-08-14T15:43:37.175
- duration_ms: 0
- entity_id: 201000571
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.181
- end: 2026-08-14T15:43:37.181
- duration_ms: 0
- parent_id: 201000571
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.181
- end: 2026-08-14T15:43:37.181
- duration_ms: 0
- entity_id: 201000628
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.187
- end: 2026-08-14T15:43:37.187
- duration_ms: 0
- parent_id: 201000628
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.187
- end: 2026-08-14T15:43:37.187
- duration_ms: 0
- entity_id: 201000744
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.193
- end: 2026-08-14T15:43:37.193
- duration_ms: 0
- parent_id: 201000744
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.194
- end: 2026-08-14T15:43:37.194
- duration_ms: 0
- entity_id: 201001031
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.200
- end: 2026-08-14T15:43:37.200
- duration_ms: 0
- parent_id: 201001031
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.200
- end: 2026-08-14T15:43:37.200
- duration_ms: 0
- entity_id: 201001606
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.206
- end: 2026-08-14T15:43:37.206
- duration_ms: 0
- parent_id: 201001606
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.206
- end: 2026-08-14T15:43:37.206
- duration_ms: 0
- entity_id: 201001644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.212
- end: 2026-08-14T15:43:37.212
- duration_ms: 0
- parent_id: 201001644
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.212
- end: 2026-08-14T15:43:37.212
- duration_ms: 0
- entity_id: 201002162
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.218
- end: 2026-08-14T15:43:37.218
- duration_ms: 0
- parent_id: 201002162
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.219
- end: 2026-08-14T15:43:37.219
- duration_ms: 0
- entity_id: 201002179
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.225
- end: 2026-08-14T15:43:37.225
- duration_ms: 0
- parent_id: 201002179
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.225
- end: 2026-08-14T15:43:37.225
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.232
- end: 2026-08-14T15:43:37.232
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.232
- end: 2026-08-14T15:43:37.232
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.238
- end: 2026-08-14T15:43:37.238
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.239
- end: 2026-08-14T15:43:37.239
- duration_ms: 0
- entity_id: 201003138
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.245
- end: 2026-08-14T15:43:37.245
- duration_ms: 0
- parent_id: 201003138
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.245
- end: 2026-08-14T15:43:37.245
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.251
- end: 2026-08-14T15:43:37.251
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.252
- end: 2026-08-14T15:43:37.252
- duration_ms: 0
- entity_id: 201003777
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.259
- end: 2026-08-14T15:43:37.259
- duration_ms: 0
- parent_id: 201003777
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.260
- end: 2026-08-14T15:43:37.260
- duration_ms: 0
- entity_id: 201003844
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.268
- end: 2026-08-14T15:43:37.268
- duration_ms: 0
- parent_id: 201003844
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.269
- end: 2026-08-14T15:43:37.269
- duration_ms: 0
- entity_id: 201003862
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.282
- end: 2026-08-14T15:43:37.282
- duration_ms: 0
- parent_id: 201003862
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.283
- end: 2026-08-14T15:43:37.283
- duration_ms: 0
- entity_id: 201004017
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.295
- end: 2026-08-14T15:43:37.295
- duration_ms: 0
- parent_id: 201004017
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.295
- end: 2026-08-14T15:43:37.295
- duration_ms: 0
- entity_id: 201004058
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.303
- end: 2026-08-14T15:43:37.303
- duration_ms: 0
- parent_id: 201004058
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.303
- end: 2026-08-14T15:43:37.303
- duration_ms: 0
- entity_id: 201004088
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.310
- end: 2026-08-14T15:43:37.310
- duration_ms: 0
- parent_id: 201004088
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.310
- end: 2026-08-14T15:43:37.310
- duration_ms: 0
- entity_id: 201004117
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.316
- end: 2026-08-14T15:43:37.316
- duration_ms: 0
- parent_id: 201004117
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.316
- end: 2026-08-14T15:43:37.316
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.323
- end: 2026-08-14T15:43:37.323
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.324
- end: 2026-08-14T15:43:37.324
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.330
- end: 2026-08-14T15:43:37.330
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:43:37.330
- end: 2026-08-14T15:43:37.330
- duration_ms: 0
- entity_id: 201004282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:43:37.337
- end: 2026-08-14T15:43:37.337
- duration_ms: 0
- parent_id: 201004282
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 41541
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 25
- limitation_count: 0
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Generation Config
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 22890
- response_chars: 584
- response_hash: 797e2e0621d90eed

## Final Output
- answer_chars: 584
- answer_hash: 797e2e0621d90eed
- success: True

## Request Complete
- request_end: 2026-08-14T15:44:00.229
- request_duration_ms: 32903
- success: True
- final_source: generation

