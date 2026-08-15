# RAG Process

audit_id: 20260813_193044_054_e345df7f
timestamp: 2026-08-13T19:30:44.055
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:30:44.055
- end: 2026-08-13T19:30:44.055
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:30:50.948
- end: 2026-08-13T19:30:50.948
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['玉米'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6893
- attempt_count: 1
- response_hash: 7b98300dde1a50b8d32de7ed31453965641fa2cc18b02c2855c8d77050b3ec39
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:30:50.952
- end: 2026-08-13T19:30:50.952
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: beeec1f7389a977fb34f293f824f0b9c7da26f25a8e09dcbd0de14472c4fee0c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:30:50.953
- end: 2026-08-13T19:30:50.953
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:30:50.953+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:30:50.955
- end: 2026-08-13T19:30:50.955
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:30:50.953+00:00
- result_count: 2

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:30:50.955
- end: 2026-08-13T19:30:50.955
- duration_ms: 0
- entity_id: 201003939
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:30:50.963
- end: 2026-08-13T19:30:50.963
- duration_ms: 0
- parent_id: 201003939
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:30:50.963
- end: 2026-08-13T19:30:50.963
- duration_ms: 0
- entity_id: 201003977
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:30:50.972
- end: 2026-08-13T19:30:50.972
- duration_ms: 0
- parent_id: 201003977
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2512
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 2
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
- duration_ms: 8074
- response_chars: 322
- response_hash: 9afe90e23918e252

## Final Output
- answer_chars: 322
- answer_hash: 9afe90e23918e252
- success: True

## Request Complete
- request_end: 2026-08-13T19:30:59.048
- request_duration_ms: 14993
- success: True
- final_source: generation

