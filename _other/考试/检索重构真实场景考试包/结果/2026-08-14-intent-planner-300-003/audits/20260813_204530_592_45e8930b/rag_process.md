# RAG Process

audit_id: 20260813_204530_592_45e8930b
timestamp: 2026-08-13T20:45:30.594
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:45:30.594
- end: 2026-08-13T20:45:30.594
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:45:34.146
- end: 2026-08-13T20:45:34.146
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3552
- attempt_count: 1
- response_hash: 62e65bce7422581a0c4fb3ec789c3c4ab4f2edfb9b64e6d37a2057dc6d47cb70
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:45:34.153
- end: 2026-08-13T20:45:34.153
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: f71c477cc83a703d82c68977bd4642ec866991bb81d40114c6efbe8c11029e76
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:45:34.154
- end: 2026-08-13T20:45:34.154
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:45:34.154+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:45:34.157
- end: 2026-08-13T20:45:34.157
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:45:34.154+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:45:34.157
- end: 2026-08-13T20:45:34.157
- duration_ms: 0
- entity_id: 201004766
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:45:34.165
- end: 2026-08-13T20:45:34.165
- duration_ms: 0
- parent_id: 201004766
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:45:34.166
- end: 2026-08-13T20:45:34.166
- duration_ms: 0
- entity_id: 201005031
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:45:34.173
- end: 2026-08-13T20:45:34.173
- duration_ms: 0
- parent_id: 201005031
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:45:34.174
- end: 2026-08-13T20:45:34.174
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:45:34.184
- end: 2026-08-13T20:45:34.184
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4351
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 3
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
- duration_ms: 7456
- response_chars: 119
- response_hash: ecec25d7da96fdea

## Final Output
- answer_chars: 119
- answer_hash: ecec25d7da96fdea
- success: True

## Request Complete
- request_end: 2026-08-13T20:45:41.641
- request_duration_ms: 11047
- success: True
- final_source: generation

