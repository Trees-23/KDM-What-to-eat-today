# RAG Process

audit_id: 20260813_204429_697_201f52c7
timestamp: 2026-08-13T20:44:29.697
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:44:29.697
- end: 2026-08-13T20:44:29.697
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:44:34.980
- end: 2026-08-13T20:44:34.980
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5283
- attempt_count: 1
- response_hash: 6598384c235b816d523fc12d75a904fb800a77f1b626ccd6ff5f4af94e7e9587
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:44:34.985
- end: 2026-08-13T20:44:34.985
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 9aedaa8d2d7664e5c2bd13246518a7450b6d35d3b197ac0eb2e609255f2d5578
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:44:34.986
- end: 2026-08-13T20:44:34.986
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:44:34.986+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:44:34.998
- end: 2026-08-13T20:44:34.998
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:44:34.986+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:44:34.999
- end: 2026-08-13T20:44:34.999
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:44:35.009
- end: 2026-08-13T20:44:35.009
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:44:35.009
- end: 2026-08-13T20:44:35.009
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:44:35.021
- end: 2026-08-13T20:44:35.021
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:44:35.022
- end: 2026-08-13T20:44:35.021
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:44:35.031
- end: 2026-08-13T20:44:35.031
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:44:35.031
- end: 2026-08-13T20:44:35.031
- duration_ms: 0
- entity_id: 201004588
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:44:35.041
- end: 2026-08-13T20:44:35.041
- duration_ms: 0
- parent_id: 201004588
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:44:35.041
- end: 2026-08-13T20:44:35.041
- duration_ms: 0
- entity_id: 201004801
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:44:35.051
- end: 2026-08-13T20:44:35.051
- duration_ms: 0
- parent_id: 201004801
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 6469
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
- duration_ms: 11698
- response_chars: 531
- response_hash: 779e8eaeefd99105

## Final Output
- answer_chars: 531
- answer_hash: 779e8eaeefd99105
- success: True

## Request Complete
- request_end: 2026-08-13T20:44:46.751
- request_duration_ms: 17054
- success: True
- final_source: generation

