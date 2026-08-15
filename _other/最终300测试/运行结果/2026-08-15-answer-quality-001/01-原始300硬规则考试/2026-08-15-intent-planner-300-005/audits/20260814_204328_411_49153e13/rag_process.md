# RAG Process

audit_id: 20260814_204328_411_49153e13
timestamp: 2026-08-14T20:43:28.411
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:43:28.412
- end: 2026-08-14T20:43:28.412
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:43:33.021
- end: 2026-08-14T20:43:33.021
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4609
- attempt_count: 1
- response_hash: e37529d69602795f2fbce73e8fc3cbfc02277d1a8ec2863d1f721a86ddde2d3c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:43:33.045
- end: 2026-08-14T20:43:33.045
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 42036588ccf8b22437954129850e2631d00a620f4b34adc0c208be949870bbb2
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:43:33.045
- end: 2026-08-14T20:43:33.045
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:43:33.045+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:43:33.051
- end: 2026-08-14T20:43:33.051
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:43:33.045+00:00
- result_count: 50

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.051
- end: 2026-08-14T20:43:33.051
- duration_ms: 0
- entity_id: 201000001
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.059
- end: 2026-08-14T20:43:33.059
- duration_ms: 0
- parent_id: 201000001
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.059
- end: 2026-08-14T20:43:33.059
- duration_ms: 0
- entity_id: 201000290
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.066
- end: 2026-08-14T20:43:33.066
- duration_ms: 0
- parent_id: 201000290
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.066
- end: 2026-08-14T20:43:33.066
- duration_ms: 0
- entity_id: 201000411
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.073
- end: 2026-08-14T20:43:33.073
- duration_ms: 0
- parent_id: 201000411
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.073
- end: 2026-08-14T20:43:33.073
- duration_ms: 0
- entity_id: 201000571
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.080
- end: 2026-08-14T20:43:33.080
- duration_ms: 0
- parent_id: 201000571
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.080
- end: 2026-08-14T20:43:33.080
- duration_ms: 0
- entity_id: 201000628
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.087
- end: 2026-08-14T20:43:33.087
- duration_ms: 0
- parent_id: 201000628
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.088
- end: 2026-08-14T20:43:33.088
- duration_ms: 0
- entity_id: 201000744
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.094
- end: 2026-08-14T20:43:33.094
- duration_ms: 0
- parent_id: 201000744
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.094
- end: 2026-08-14T20:43:33.094
- duration_ms: 0
- entity_id: 201001031
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.100
- end: 2026-08-14T20:43:33.100
- duration_ms: 0
- parent_id: 201001031
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.101
- end: 2026-08-14T20:43:33.101
- duration_ms: 0
- entity_id: 201001606
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.107
- end: 2026-08-14T20:43:33.107
- duration_ms: 0
- parent_id: 201001606
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.107
- end: 2026-08-14T20:43:33.107
- duration_ms: 0
- entity_id: 201001644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.114
- end: 2026-08-14T20:43:33.114
- duration_ms: 0
- parent_id: 201001644
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.114
- end: 2026-08-14T20:43:33.114
- duration_ms: 0
- entity_id: 201002162
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.120
- end: 2026-08-14T20:43:33.120
- duration_ms: 0
- parent_id: 201002162
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.120
- end: 2026-08-14T20:43:33.120
- duration_ms: 0
- entity_id: 201002179
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.125
- end: 2026-08-14T20:43:33.125
- duration_ms: 0
- parent_id: 201002179
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.126
- end: 2026-08-14T20:43:33.126
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.131
- end: 2026-08-14T20:43:33.131
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.132
- end: 2026-08-14T20:43:33.132
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.138
- end: 2026-08-14T20:43:33.138
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.138
- end: 2026-08-14T20:43:33.138
- duration_ms: 0
- entity_id: 201003138
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.144
- end: 2026-08-14T20:43:33.144
- duration_ms: 0
- parent_id: 201003138
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.144
- end: 2026-08-14T20:43:33.144
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.150
- end: 2026-08-14T20:43:33.150
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.150
- end: 2026-08-14T20:43:33.150
- duration_ms: 0
- entity_id: 201003777
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.155
- end: 2026-08-14T20:43:33.155
- duration_ms: 0
- parent_id: 201003777
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.156
- end: 2026-08-14T20:43:33.156
- duration_ms: 0
- entity_id: 201003844
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.161
- end: 2026-08-14T20:43:33.161
- duration_ms: 0
- parent_id: 201003844
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.162
- end: 2026-08-14T20:43:33.162
- duration_ms: 0
- entity_id: 201003862
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.167
- end: 2026-08-14T20:43:33.167
- duration_ms: 0
- parent_id: 201003862
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.167
- end: 2026-08-14T20:43:33.167
- duration_ms: 0
- entity_id: 201004017
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.173
- end: 2026-08-14T20:43:33.173
- duration_ms: 0
- parent_id: 201004017
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.173
- end: 2026-08-14T20:43:33.173
- duration_ms: 0
- entity_id: 201004058
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.179
- end: 2026-08-14T20:43:33.179
- duration_ms: 0
- parent_id: 201004058
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.179
- end: 2026-08-14T20:43:33.179
- duration_ms: 0
- entity_id: 201004088
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.185
- end: 2026-08-14T20:43:33.185
- duration_ms: 0
- parent_id: 201004088
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.185
- end: 2026-08-14T20:43:33.185
- duration_ms: 0
- entity_id: 201004117
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.191
- end: 2026-08-14T20:43:33.191
- duration_ms: 0
- parent_id: 201004117
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.191
- end: 2026-08-14T20:43:33.191
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.197
- end: 2026-08-14T20:43:33.197
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.197
- end: 2026-08-14T20:43:33.197
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.203
- end: 2026-08-14T20:43:33.203
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:43:33.204
- end: 2026-08-14T20:43:33.204
- duration_ms: 0
- entity_id: 201004282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:43:33.209
- end: 2026-08-14T20:43:33.209
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
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 33057
- response_chars: 747
- response_hash: f53806face4402ad

## Final Output
- answer_chars: 747
- answer_hash: f53806face4402ad
- success: True

## Request Complete
- request_end: 2026-08-14T20:44:06.268
- request_duration_ms: 37856
- success: True
- final_source: generation

