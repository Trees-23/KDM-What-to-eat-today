# RAG Process

audit_id: 20260813_205005_807_7464425f
timestamp: 2026-08-13T20:50:05.807
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:50:05.808
- end: 2026-08-13T20:50:05.808
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:50:09.544
- end: 2026-08-13T20:50:09.544
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.93
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3736
- attempt_count: 1
- response_hash: 254e3b588568765213d0332e8ddce8adfb28d14226491e1fc507c9eeb666f7b2
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:50:09.550
- end: 2026-08-13T20:50:09.550
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 8104e2b571f8c2eefdfbeb8b79d91c061ce4378c7ef0db03fcf74b8d1da269c8
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:50:09.550
- end: 2026-08-13T20:50:09.550
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:50:09.550+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:50:09.555
- end: 2026-08-13T20:50:09.555
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:50:09.550+00:00
- result_count: 13

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:50:09.556
- end: 2026-08-13T20:50:09.556
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:50:09.569
- end: 2026-08-13T20:50:09.569
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:50:09.570
- end: 2026-08-13T20:50:09.570
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:50:09.579
- end: 2026-08-13T20:50:09.579
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:50:09.579
- end: 2026-08-13T20:50:09.579
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:50:09.586
- end: 2026-08-13T20:50:09.586
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:50:09.586
- end: 2026-08-13T20:50:09.586
- duration_ms: 0
- entity_id: 201004588
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:50:09.594
- end: 2026-08-13T20:50:09.594
- duration_ms: 0
- parent_id: 201004588
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:50:09.594
- end: 2026-08-13T20:50:09.594
- duration_ms: 0
- entity_id: 201004801
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:50:09.600
- end: 2026-08-13T20:50:09.600
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
- duration_ms: 9319
- response_chars: 384
- response_hash: 740e48f7812520b0

## Final Output
- answer_chars: 384
- answer_hash: 740e48f7812520b0
- success: True

## Request Complete
- request_end: 2026-08-13T20:50:18.920
- request_duration_ms: 13112
- success: True
- final_source: generation

