# RAG Process

audit_id: 20260813_193610_329_08fb5294
timestamp: 2026-08-13T19:36:10.331
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:36:10.332
- end: 2026-08-13T19:36:10.332
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:36:14.402
- end: 2026-08-13T19:36:14.402
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.93
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4070
- attempt_count: 1
- response_hash: 254e3b588568765213d0332e8ddce8adfb28d14226491e1fc507c9eeb666f7b2
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:36:14.407
- end: 2026-08-13T19:36:14.407
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 8104e2b571f8c2eefdfbeb8b79d91c061ce4378c7ef0db03fcf74b8d1da269c8
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:36:14.407
- end: 2026-08-13T19:36:14.407
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T19:36:14.407+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:36:14.412
- end: 2026-08-13T19:36:14.412
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T19:36:14.407+00:00
- result_count: 13

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:36:14.412
- end: 2026-08-13T19:36:14.412
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:36:14.421
- end: 2026-08-13T19:36:14.421
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:36:14.421
- end: 2026-08-13T19:36:14.421
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:36:14.431
- end: 2026-08-13T19:36:14.431
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:36:14.431
- end: 2026-08-13T19:36:14.431
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:36:14.441
- end: 2026-08-13T19:36:14.441
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:36:14.441
- end: 2026-08-13T19:36:14.441
- duration_ms: 0
- entity_id: 201004588
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:36:14.447
- end: 2026-08-13T19:36:14.447
- duration_ms: 0
- parent_id: 201004588
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:36:14.447
- end: 2026-08-13T19:36:14.447
- duration_ms: 0
- entity_id: 201004801
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:36:14.454
- end: 2026-08-13T19:36:14.454
- duration_ms: 0
- parent_id: 201004801
- build_id: pds_2a8c0807733eb8022a623659
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 7652
- response_chars: 313
- response_hash: 388398b235ee8192

## Final Output
- answer_chars: 313
- answer_hash: 388398b235ee8192
- success: True

## Request Complete
- request_end: 2026-08-13T19:36:22.107
- request_duration_ms: 11775
- success: True
- final_source: generation

