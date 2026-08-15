# RAG Process

audit_id: 20260813_204414_435_00f7e7db
timestamp: 2026-08-13T20:44:14.436
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:44:14.436
- end: 2026-08-13T20:44:14.436
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 22

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:44:19.446
- end: 2026-08-13T20:44:19.446
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5010
- attempt_count: 1
- response_hash: 741ef86d7f70c451a1b36af95f80841429920a80f14effe5afbb9319044cf70a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:44:19.460
- end: 2026-08-13T20:44:19.460
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 0c617862136ab3f567b417939974bd4dda876c21996bd87f9a6a344280fd732c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:44:19.461
- end: 2026-08-13T20:44:19.461
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:44:19.461+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:44:19.462
- end: 2026-08-13T20:44:19.462
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:44:19.461+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:44:19.462
- end: 2026-08-13T20:44:19.462
- duration_ms: 0
- entity_id: 201004135
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:44:19.469
- end: 2026-08-13T20:44:19.469
- duration_ms: 0
- parent_id: 201004135
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1566
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 1
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
- duration_ms: 10225
- response_chars: 235
- response_hash: 7cc9c6f9313a6ccf

## Final Output
- answer_chars: 235
- answer_hash: 7cc9c6f9313a6ccf
- success: True

## Request Complete
- request_end: 2026-08-13T20:44:29.696
- request_duration_ms: 15260
- success: True
- final_source: generation

