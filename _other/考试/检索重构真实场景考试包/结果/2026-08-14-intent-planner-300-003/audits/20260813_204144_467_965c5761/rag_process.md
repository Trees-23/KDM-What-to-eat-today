# RAG Process

audit_id: 20260813_204144_467_965c5761
timestamp: 2026-08-13T20:41:44.467
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:41:44.467
- end: 2026-08-13T20:41:44.467
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:41:48.063
- end: 2026-08-13T20:41:48.063
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3596
- attempt_count: 1
- response_hash: 48acd9bfa389518bb6650d59adba69d5384c9a95a49670657526d467a6117824
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:41:48.069
- end: 2026-08-13T20:41:48.069
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 0c4d511ef3bb366ebc11daa4919872543eb40da4eda5a78aa74eb53b4f1aefba
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:41:48.070
- end: 2026-08-13T20:41:48.070
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:41:48.070+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:41:48.075
- end: 2026-08-13T20:41:48.075
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:41:48.070+00:00
- result_count: 16

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.075
- end: 2026-08-13T20:41:48.075
- duration_ms: 0
- entity_id: 201001891
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.090
- end: 2026-08-13T20:41:48.090
- duration_ms: 0
- parent_id: 201001891
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.091
- end: 2026-08-13T20:41:48.091
- duration_ms: 0
- entity_id: 201002122
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.104
- end: 2026-08-13T20:41:48.104
- duration_ms: 0
- parent_id: 201002122
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.105
- end: 2026-08-13T20:41:48.105
- duration_ms: 0
- entity_id: 201002309
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.115
- end: 2026-08-13T20:41:48.115
- duration_ms: 0
- parent_id: 201002309
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.115
- end: 2026-08-13T20:41:48.115
- duration_ms: 0
- entity_id: 201002369
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.125
- end: 2026-08-13T20:41:48.125
- duration_ms: 0
- parent_id: 201002369
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.126
- end: 2026-08-13T20:41:48.126
- duration_ms: 0
- entity_id: 201002575
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.134
- end: 2026-08-13T20:41:48.134
- duration_ms: 0
- parent_id: 201002575
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.135
- end: 2026-08-13T20:41:48.135
- duration_ms: 0
- entity_id: 201002647
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.141
- end: 2026-08-13T20:41:48.141
- duration_ms: 0
- parent_id: 201002647
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.141
- end: 2026-08-13T20:41:48.141
- duration_ms: 0
- entity_id: 201002920
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.148
- end: 2026-08-13T20:41:48.148
- duration_ms: 0
- parent_id: 201002920
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.148
- end: 2026-08-13T20:41:48.148
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.155
- end: 2026-08-13T20:41:48.155
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.155
- end: 2026-08-13T20:41:48.155
- duration_ms: 0
- entity_id: 201003275
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.163
- end: 2026-08-13T20:41:48.163
- duration_ms: 0
- parent_id: 201003275
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.163
- end: 2026-08-13T20:41:48.163
- duration_ms: 0
- entity_id: 201003355
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.171
- end: 2026-08-13T20:41:48.171
- duration_ms: 0
- parent_id: 201003355
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.171
- end: 2026-08-13T20:41:48.171
- duration_ms: 0
- entity_id: 201004525
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.180
- end: 2026-08-13T20:41:48.180
- duration_ms: 0
- parent_id: 201004525
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.180
- end: 2026-08-13T20:41:48.180
- duration_ms: 0
- entity_id: 201004898
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.186
- end: 2026-08-13T20:41:48.186
- duration_ms: 0
- parent_id: 201004898
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.186
- end: 2026-08-13T20:41:48.186
- duration_ms: 0
- entity_id: 201005092
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.193
- end: 2026-08-13T20:41:48.193
- duration_ms: 0
- parent_id: 201005092
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.193
- end: 2026-08-13T20:41:48.193
- duration_ms: 0
- entity_id: 201005195
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.200
- end: 2026-08-13T20:41:48.200
- duration_ms: 0
- parent_id: 201005195
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.200
- end: 2026-08-13T20:41:48.200
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.209
- end: 2026-08-13T20:41:48.209
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:41:48.209
- end: 2026-08-13T20:41:48.209
- duration_ms: 0
- entity_id: 201005422
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:41:48.216
- end: 2026-08-13T20:41:48.216
- duration_ms: 0
- parent_id: 201005422
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 20976
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 16
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
- duration_ms: 9706
- response_chars: 382
- response_hash: a410bbb5b3f8c30f

## Final Output
- answer_chars: 382
- answer_hash: a410bbb5b3f8c30f
- success: True

## Request Complete
- request_end: 2026-08-13T20:41:57.923
- request_duration_ms: 13456
- success: True
- final_source: generation

