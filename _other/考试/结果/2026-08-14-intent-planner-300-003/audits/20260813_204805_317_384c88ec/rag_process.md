# RAG Process

audit_id: 20260813_204805_317_384c88ec
timestamp: 2026-08-13T20:48:05.318
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:48:05.318
- end: 2026-08-13T20:48:05.318
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 12

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:48:09.192
- end: 2026-08-13T20:48:09.192
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3873
- attempt_count: 1
- response_hash: da1237de66310cc8301fe37a803de538759e9c7db909e2ee50187b59298ab4bf
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:48:09.196
- end: 2026-08-13T20:48:09.196
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 03656bf57598d22620bfaadae1c85a537b0cbddc855d0c4d422df204fb809ee6
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:48:09.197
- end: 2026-08-13T20:48:09.197
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:48:09.197+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:48:09.201
- end: 2026-08-13T20:48:09.201
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:48:09.197+00:00
- result_count: 18

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:48:09.202
- end: 2026-08-13T20:48:09.202
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:48:09.217
- end: 2026-08-13T20:48:09.217
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:48:09.217
- end: 2026-08-13T20:48:09.217
- duration_ms: 0
- entity_id: 201004746
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:48:09.230
- end: 2026-08-13T20:48:09.230
- duration_ms: 0
- parent_id: 201004746
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:48:09.230
- end: 2026-08-13T20:48:09.230
- duration_ms: 0
- entity_id: 201005049
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:48:09.238
- end: 2026-08-13T20:48:09.238
- duration_ms: 0
- parent_id: 201005049
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:48:09.238
- end: 2026-08-13T20:48:09.238
- duration_ms: 0
- entity_id: 201005181
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:48:09.244
- end: 2026-08-13T20:48:09.244
- duration_ms: 0
- parent_id: 201005181
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:48:09.244
- end: 2026-08-13T20:48:09.244
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:48:09.253
- end: 2026-08-13T20:48:09.253
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:48:09.253
- end: 2026-08-13T20:48:09.253
- duration_ms: 0
- entity_id: 201005653
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:48:09.260
- end: 2026-08-13T20:48:09.260
- duration_ms: 0
- parent_id: 201005653
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:48:09.260
- end: 2026-08-13T20:48:09.260
- duration_ms: 0
- entity_id: 201005669
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:48:09.270
- end: 2026-08-13T20:48:09.270
- duration_ms: 0
- parent_id: 201005669
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 13261
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 7
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
- duration_ms: 15070
- response_chars: 364
- response_hash: beb441589d098f64

## Final Output
- answer_chars: 364
- answer_hash: beb441589d098f64
- success: True

## Request Complete
- request_end: 2026-08-13T20:48:24.342
- request_duration_ms: 19023
- success: True
- final_source: generation

