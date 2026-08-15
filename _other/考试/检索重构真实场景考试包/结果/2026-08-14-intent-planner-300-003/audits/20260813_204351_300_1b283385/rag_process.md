# RAG Process

audit_id: 20260813_204351_300_1b283385
timestamp: 2026-08-13T20:43:51.301
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:43:51.301
- end: 2026-08-13T20:43:51.301
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:43:59.046
- end: 2026-08-13T20:43:59.046
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 7744
- attempt_count: 1
- response_hash: 796d921a2fd37d44c1ca25f0145547249f5907d1c582d5ad574e03617b4c122e
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:43:59.052
- end: 2026-08-13T20:43:59.052
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 370144f87365ea87eb0e31aac0ddee6c40cf6a652df6dd418e5c3a8c3a2dbf20
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:43:59.053
- end: 2026-08-13T20:43:59.053
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:43:59.053+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:43:59.057
- end: 2026-08-13T20:43:59.057
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:43:59.053+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:43:59.057
- end: 2026-08-13T20:43:59.057
- duration_ms: 0
- entity_id: 201000127
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:43:59.074
- end: 2026-08-13T20:43:59.074
- duration_ms: 0
- parent_id: 201000127
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:43:59.075
- end: 2026-08-13T20:43:59.075
- duration_ms: 0
- entity_id: 201000290
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:43:59.086
- end: 2026-08-13T20:43:59.086
- duration_ms: 0
- parent_id: 201000290
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:43:59.086
- end: 2026-08-13T20:43:59.086
- duration_ms: 0
- entity_id: 201000453
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:43:59.093
- end: 2026-08-13T20:43:59.093
- duration_ms: 0
- parent_id: 201000453
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4850
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
- duration_ms: 15340
- response_chars: 451
- response_hash: 918a619ff4c26e63

## Final Output
- answer_chars: 451
- answer_hash: 918a619ff4c26e63
- success: True

## Request Complete
- request_end: 2026-08-13T20:44:14.435
- request_duration_ms: 23133
- success: True
- final_source: generation

