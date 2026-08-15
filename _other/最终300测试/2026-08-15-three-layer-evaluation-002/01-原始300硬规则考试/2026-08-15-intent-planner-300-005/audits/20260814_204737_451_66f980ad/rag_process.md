# RAG Process

audit_id: 20260814_204737_451_66f980ad
timestamp: 2026-08-14T20:47:37.451
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:47:37.451
- end: 2026-08-14T20:47:37.451
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:47:42.245
- end: 2026-08-14T20:47:42.245
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.92
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4794
- attempt_count: 1
- response_hash: 08cb8fa6054a2c2e9dc68b644ac0bca34faf2155d747cf4587f76c044890c67b
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:47:42.255
- end: 2026-08-14T20:47:42.255
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 8104e2b571f8c2eefdfbeb8b79d91c061ce4378c7ef0db03fcf74b8d1da269c8
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:47:42.255
- end: 2026-08-14T20:47:42.255
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:47:42.255+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:47:42.257
- end: 2026-08-14T20:47:42.257
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:47:42.255+00:00
- result_count: 13

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:47:42.257
- end: 2026-08-14T20:47:42.257
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:47:42.263
- end: 2026-08-14T20:47:42.263
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:47:42.263
- end: 2026-08-14T20:47:42.263
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:47:42.269
- end: 2026-08-14T20:47:42.269
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:47:42.269
- end: 2026-08-14T20:47:42.269
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:47:42.275
- end: 2026-08-14T20:47:42.275
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:47:42.275
- end: 2026-08-14T20:47:42.275
- duration_ms: 0
- entity_id: 201004588
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:47:42.281
- end: 2026-08-14T20:47:42.281
- duration_ms: 0
- parent_id: 201004588
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:47:42.281
- end: 2026-08-14T20:47:42.281
- duration_ms: 0
- entity_id: 201004801
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:47:42.287
- end: 2026-08-14T20:47:42.287
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
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 11169
- response_chars: 311
- response_hash: 49a48524e46e1fe5

## Final Output
- answer_chars: 311
- answer_hash: 49a48524e46e1fe5
- success: True

## Request Complete
- request_end: 2026-08-14T20:47:53.457
- request_duration_ms: 16006
- success: True
- final_source: generation

