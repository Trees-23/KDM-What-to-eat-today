# RAG Process

audit_id: 20260814_154813_223_aea57dc5
timestamp: 2026-08-14T15:48:13.224
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:48:13.225
- end: 2026-08-14T15:48:13.225
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:48:23.496
- end: 2026-08-14T15:48:23.496
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.86
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 10270
- attempt_count: 1
- response_hash: f2c015e7ead32c14c7f17f5e00be611904d744e91404b4cf1c97c0747d20f87b
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:48:23.521
- end: 2026-08-14T15:48:23.521
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 8104e2b571f8c2eefdfbeb8b79d91c061ce4378c7ef0db03fcf74b8d1da269c8
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:48:23.521
- end: 2026-08-14T15:48:23.521
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:48:23.521+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:48:23.524
- end: 2026-08-14T15:48:23.524
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:48:23.521+00:00
- result_count: 13

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:48:23.524
- end: 2026-08-14T15:48:23.524
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:48:23.532
- end: 2026-08-14T15:48:23.532
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:48:23.533
- end: 2026-08-14T15:48:23.533
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:48:23.541
- end: 2026-08-14T15:48:23.541
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:48:23.541
- end: 2026-08-14T15:48:23.541
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:48:23.549
- end: 2026-08-14T15:48:23.549
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:48:23.550
- end: 2026-08-14T15:48:23.550
- duration_ms: 0
- entity_id: 201004588
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:48:23.556
- end: 2026-08-14T15:48:23.556
- duration_ms: 0
- parent_id: 201004588
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:48:23.557
- end: 2026-08-14T15:48:23.557
- duration_ms: 0
- entity_id: 201004801
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:48:23.563
- end: 2026-08-14T15:48:23.563
- duration_ms: 0
- parent_id: 201004801
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 9476
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 5
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
- duration_ms: 16900
- response_chars: 351
- response_hash: 754ba4c6659054de

## Final Output
- answer_chars: 351
- answer_hash: 754ba4c6659054de
- success: True

## Request Complete
- request_end: 2026-08-14T15:48:40.467
- request_duration_ms: 27241
- success: True
- final_source: generation

