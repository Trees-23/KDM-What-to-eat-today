# RAG Process

audit_id: 20260813_204157_924_43a023e8
timestamp: 2026-08-13T20:41:57.925
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:41:57.925
- end: 2026-08-13T20:41:57.925
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:42:01.296
- end: 2026-08-13T20:42:01.296
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3371
- attempt_count: 1
- response_hash: f6bddb982769344c9fd8ebc44f4777cc726c5e88bfbc2cf100f9a02fbed6aa8b
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:42:01.304
- end: 2026-08-13T20:42:01.304
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 26f67e4276e5e3ae393e720125ec5c97e34bdb546f1c1818614d295d6f37a8ea
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:42:01.305
- end: 2026-08-13T20:42:01.305
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:42:01.305+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:42:01.308
- end: 2026-08-13T20:42:01.308
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:42:01.305+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:01.308
- end: 2026-08-13T20:42:01.308
- duration_ms: 0
- entity_id: 201003459
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:01.321
- end: 2026-08-13T20:42:01.321
- duration_ms: 0
- parent_id: 201003459
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:01.322
- end: 2026-08-13T20:42:01.322
- duration_ms: 0
- entity_id: 201004731
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:01.328
- end: 2026-08-13T20:42:01.328
- duration_ms: 0
- parent_id: 201004731
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:01.328
- end: 2026-08-13T20:42:01.328
- duration_ms: 0
- entity_id: 201004898
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:01.334
- end: 2026-08-13T20:42:01.334
- duration_ms: 0
- parent_id: 201004898
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:01.334
- end: 2026-08-13T20:42:01.334
- duration_ms: 0
- entity_id: 201005001
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:01.341
- end: 2026-08-13T20:42:01.341
- duration_ms: 0
- parent_id: 201005001
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:01.341
- end: 2026-08-13T20:42:01.341
- duration_ms: 0
- entity_id: 201005092
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:01.348
- end: 2026-08-13T20:42:01.348
- duration_ms: 0
- parent_id: 201005092
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:01.348
- end: 2026-08-13T20:42:01.348
- duration_ms: 0
- entity_id: 201005146
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:01.355
- end: 2026-08-13T20:42:01.355
- duration_ms: 0
- parent_id: 201005146
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:01.355
- end: 2026-08-13T20:42:01.355
- duration_ms: 0
- entity_id: 201005492
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:01.364
- end: 2026-08-13T20:42:01.364
- duration_ms: 0
- parent_id: 201005492
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 9036
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
- duration_ms: 6012
- response_chars: 259
- response_hash: 47d1df01cf2f0df1

## Final Output
- answer_chars: 259
- answer_hash: 47d1df01cf2f0df1
- success: True

## Request Complete
- request_end: 2026-08-13T20:42:07.378
- request_duration_ms: 9452
- success: True
- final_source: generation

