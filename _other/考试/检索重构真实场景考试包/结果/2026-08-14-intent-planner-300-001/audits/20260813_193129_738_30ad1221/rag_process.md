# RAG Process

audit_id: 20260813_193129_738_30ad1221
timestamp: 2026-08-13T19:31:29.739
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:31:29.739
- end: 2026-08-13T19:31:29.739
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:31:33.580
- end: 2026-08-13T19:31:33.580
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3841
- attempt_count: 1
- response_hash: 0dde797f01db7ad9b2df6d2d3131bc3f06306117d7c3c0abf12d3df81a389ab9
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:31:33.585
- end: 2026-08-13T19:31:33.585
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: e71a3c5f96904496a022cbe7edbe063a605d5ae4d4fb43f5c87aad3d053b53ee
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:31:33.585
- end: 2026-08-13T19:31:33.585
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:31:33.585+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:31:33.587
- end: 2026-08-13T19:31:33.587
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:31:33.585+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:31:33.587
- end: 2026-08-13T19:31:33.587
- duration_ms: 0
- entity_id: 201002146
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:31:33.594
- end: 2026-08-13T19:31:33.594
- duration_ms: 0
- parent_id: 201002146
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:31:33.594
- end: 2026-08-13T19:31:33.594
- duration_ms: 0
- entity_id: 201003534
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:31:33.600
- end: 2026-08-13T19:31:33.600
- duration_ms: 0
- parent_id: 201003534
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:31:33.601
- end: 2026-08-13T19:31:33.601
- duration_ms: 0
- entity_id: 201004088
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:31:33.607
- end: 2026-08-13T19:31:33.607
- duration_ms: 0
- parent_id: 201004088
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:31:33.607
- end: 2026-08-13T19:31:33.607
- duration_ms: 0
- entity_id: 201004282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:31:33.613
- end: 2026-08-13T19:31:33.613
- duration_ms: 0
- parent_id: 201004282
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:31:33.613
- end: 2026-08-13T19:31:33.613
- duration_ms: 0
- entity_id: 201004793
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:31:33.620
- end: 2026-08-13T19:31:33.620
- duration_ms: 0
- parent_id: 201004793
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:31:33.620
- end: 2026-08-13T19:31:33.620
- duration_ms: 0
- entity_id: 201004885
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:31:33.626
- end: 2026-08-13T19:31:33.626
- duration_ms: 0
- parent_id: 201004885
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:31:33.626
- end: 2026-08-13T19:31:33.626
- duration_ms: 0
- entity_id: 201005272
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:31:33.633
- end: 2026-08-13T19:31:33.633
- duration_ms: 0
- parent_id: 201005272
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 8424
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
- duration_ms: 10327
- response_chars: 148
- response_hash: 8bc64dcb0b563d72

## Final Output
- answer_chars: 148
- answer_hash: 8bc64dcb0b563d72
- success: True

## Request Complete
- request_end: 2026-08-13T19:31:43.962
- request_duration_ms: 14223
- success: True
- final_source: generation

