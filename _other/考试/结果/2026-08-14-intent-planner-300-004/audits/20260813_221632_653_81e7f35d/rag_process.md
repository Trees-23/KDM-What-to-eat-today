# RAG Process

audit_id: 20260813_221632_653_81e7f35d
timestamp: 2026-08-13T22:16:32.654
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:16:32.654
- end: 2026-08-13T22:16:32.654
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:16:38.062
- end: 2026-08-13T22:16:38.062
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5408
- attempt_count: 1
- response_hash: 3a9020e509abba043f310476f71f83739bc1bd6671ee309db71bf233184a580b
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:16:38.071
- end: 2026-08-13T22:16:38.071
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 42036588ccf8b22437954129850e2631d00a620f4b34adc0c208be949870bbb2
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:16:38.071
- end: 2026-08-13T22:16:38.071
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:16:38.071+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:16:38.084
- end: 2026-08-13T22:16:38.084
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:16:38.071+00:00
- result_count: 50

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.084
- end: 2026-08-13T22:16:38.084
- duration_ms: 0
- entity_id: 201000001
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.094
- end: 2026-08-13T22:16:38.094
- duration_ms: 0
- parent_id: 201000001
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.094
- end: 2026-08-13T22:16:38.094
- duration_ms: 0
- entity_id: 201000290
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.102
- end: 2026-08-13T22:16:38.102
- duration_ms: 0
- parent_id: 201000290
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.102
- end: 2026-08-13T22:16:38.102
- duration_ms: 0
- entity_id: 201000411
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.110
- end: 2026-08-13T22:16:38.110
- duration_ms: 0
- parent_id: 201000411
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.110
- end: 2026-08-13T22:16:38.110
- duration_ms: 0
- entity_id: 201000571
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.118
- end: 2026-08-13T22:16:38.118
- duration_ms: 0
- parent_id: 201000571
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.119
- end: 2026-08-13T22:16:38.119
- duration_ms: 0
- entity_id: 201000628
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.126
- end: 2026-08-13T22:16:38.126
- duration_ms: 0
- parent_id: 201000628
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.127
- end: 2026-08-13T22:16:38.127
- duration_ms: 0
- entity_id: 201000744
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.133
- end: 2026-08-13T22:16:38.133
- duration_ms: 0
- parent_id: 201000744
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.133
- end: 2026-08-13T22:16:38.133
- duration_ms: 0
- entity_id: 201001031
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.140
- end: 2026-08-13T22:16:38.140
- duration_ms: 0
- parent_id: 201001031
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.140
- end: 2026-08-13T22:16:38.140
- duration_ms: 0
- entity_id: 201001606
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.147
- end: 2026-08-13T22:16:38.147
- duration_ms: 0
- parent_id: 201001606
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.147
- end: 2026-08-13T22:16:38.147
- duration_ms: 0
- entity_id: 201001644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.153
- end: 2026-08-13T22:16:38.153
- duration_ms: 0
- parent_id: 201001644
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.153
- end: 2026-08-13T22:16:38.153
- duration_ms: 0
- entity_id: 201002162
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.159
- end: 2026-08-13T22:16:38.159
- duration_ms: 0
- parent_id: 201002162
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.159
- end: 2026-08-13T22:16:38.159
- duration_ms: 0
- entity_id: 201002179
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.166
- end: 2026-08-13T22:16:38.166
- duration_ms: 0
- parent_id: 201002179
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.166
- end: 2026-08-13T22:16:38.166
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.173
- end: 2026-08-13T22:16:38.173
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.173
- end: 2026-08-13T22:16:38.173
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.180
- end: 2026-08-13T22:16:38.180
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.180
- end: 2026-08-13T22:16:38.180
- duration_ms: 0
- entity_id: 201003138
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.186
- end: 2026-08-13T22:16:38.186
- duration_ms: 0
- parent_id: 201003138
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.187
- end: 2026-08-13T22:16:38.187
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.193
- end: 2026-08-13T22:16:38.193
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.194
- end: 2026-08-13T22:16:38.194
- duration_ms: 0
- entity_id: 201003777
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.200
- end: 2026-08-13T22:16:38.200
- duration_ms: 0
- parent_id: 201003777
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.200
- end: 2026-08-13T22:16:38.200
- duration_ms: 0
- entity_id: 201003844
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.206
- end: 2026-08-13T22:16:38.206
- duration_ms: 0
- parent_id: 201003844
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.207
- end: 2026-08-13T22:16:38.207
- duration_ms: 0
- entity_id: 201003862
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.213
- end: 2026-08-13T22:16:38.213
- duration_ms: 0
- parent_id: 201003862
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.213
- end: 2026-08-13T22:16:38.213
- duration_ms: 0
- entity_id: 201004017
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.219
- end: 2026-08-13T22:16:38.219
- duration_ms: 0
- parent_id: 201004017
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.219
- end: 2026-08-13T22:16:38.219
- duration_ms: 0
- entity_id: 201004058
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.225
- end: 2026-08-13T22:16:38.225
- duration_ms: 0
- parent_id: 201004058
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.225
- end: 2026-08-13T22:16:38.225
- duration_ms: 0
- entity_id: 201004088
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.232
- end: 2026-08-13T22:16:38.232
- duration_ms: 0
- parent_id: 201004088
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.233
- end: 2026-08-13T22:16:38.233
- duration_ms: 0
- entity_id: 201004117
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.239
- end: 2026-08-13T22:16:38.239
- duration_ms: 0
- parent_id: 201004117
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.239
- end: 2026-08-13T22:16:38.239
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.246
- end: 2026-08-13T22:16:38.246
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.246
- end: 2026-08-13T22:16:38.246
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.253
- end: 2026-08-13T22:16:38.253
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:38.254
- end: 2026-08-13T22:16:38.254
- duration_ms: 0
- entity_id: 201004282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:38.260
- end: 2026-08-13T22:16:38.260
- duration_ms: 0
- parent_id: 201004282
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 41538
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 19387
- response_chars: 409
- response_hash: 66ce7998b5bcebf9

## Final Output
- answer_chars: 409
- answer_hash: 66ce7998b5bcebf9
- success: True

## Request Complete
- request_end: 2026-08-13T22:16:57.649
- request_duration_ms: 24994
- success: True
- final_source: generation

