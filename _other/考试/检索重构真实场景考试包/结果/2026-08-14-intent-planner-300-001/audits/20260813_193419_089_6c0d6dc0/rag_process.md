# RAG Process

audit_id: 20260813_193419_089_6c0d6dc0
timestamp: 2026-08-13T19:34:19.090
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:34:19.090
- end: 2026-08-13T19:34:19.090
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 12

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:34:25.475
- end: 2026-08-13T19:34:25.475
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6384
- attempt_count: 1
- response_hash: 2636812a0df96b6d841d1b25353f9ef145b53cae7b835ff995996344549b6ce4
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:34:25.480
- end: 2026-08-13T19:34:25.480
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 03656bf57598d22620bfaadae1c85a537b0cbddc855d0c4d422df204fb809ee6
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:34:25.480
- end: 2026-08-13T19:34:25.480
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T19:34:25.480+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:34:25.482
- end: 2026-08-13T19:34:25.482
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T19:34:25.480+00:00
- result_count: 18

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:34:25.482
- end: 2026-08-13T19:34:25.482
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:34:25.489
- end: 2026-08-13T19:34:25.489
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:34:25.490
- end: 2026-08-13T19:34:25.490
- duration_ms: 0
- entity_id: 201004746
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:34:25.496
- end: 2026-08-13T19:34:25.496
- duration_ms: 0
- parent_id: 201004746
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:34:25.496
- end: 2026-08-13T19:34:25.496
- duration_ms: 0
- entity_id: 201005049
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:34:25.502
- end: 2026-08-13T19:34:25.502
- duration_ms: 0
- parent_id: 201005049
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:34:25.502
- end: 2026-08-13T19:34:25.502
- duration_ms: 0
- entity_id: 201005181
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:34:25.508
- end: 2026-08-13T19:34:25.508
- duration_ms: 0
- parent_id: 201005181
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:34:25.508
- end: 2026-08-13T19:34:25.508
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:34:25.514
- end: 2026-08-13T19:34:25.514
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:34:25.514
- end: 2026-08-13T19:34:25.514
- duration_ms: 0
- entity_id: 201005653
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:34:25.520
- end: 2026-08-13T19:34:25.520
- duration_ms: 0
- parent_id: 201005653
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:34:25.520
- end: 2026-08-13T19:34:25.520
- duration_ms: 0
- entity_id: 201005669
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:34:25.526
- end: 2026-08-13T19:34:25.526
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
- duration_ms: 14165
- response_chars: 430
- response_hash: 209b568343b2c2ba

## Final Output
- answer_chars: 430
- answer_hash: 209b568343b2c2ba
- success: True

## Request Complete
- request_end: 2026-08-13T19:34:39.693
- request_duration_ms: 20602
- success: True
- final_source: generation

