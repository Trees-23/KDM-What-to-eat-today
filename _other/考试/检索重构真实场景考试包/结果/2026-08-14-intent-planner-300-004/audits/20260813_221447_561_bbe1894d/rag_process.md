# RAG Process

audit_id: 20260813_221447_561_bbe1894d
timestamp: 2026-08-13T22:14:47.562
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:14:47.562
- end: 2026-08-13T22:14:47.562
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 37

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:14:51.018
- end: 2026-08-13T22:14:51.018
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4265
- attempt_count: 1
- response_hash: fdc6e654a97740877778f4fa3e6fc7c9959a50fb56ce35f791d3fab0cc19a59e
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:14:51.025
- end: 2026-08-13T22:14:51.025
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 58cb008445dfe787889b9299f8ca816668e4b830116e873a821c8a831964b7bb
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:14:51.025
- end: 2026-08-13T22:14:51.025
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:14:51.025+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:14:51.029
- end: 2026-08-13T22:14:51.029
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:14:51.025+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:14:51.029
- end: 2026-08-13T22:14:51.029
- duration_ms: 0
- entity_id: 201005129
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:14:51.045
- end: 2026-08-13T22:14:51.045
- duration_ms: 0
- parent_id: 201005129
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1651
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
- duration_ms: 3568
- response_chars: 94
- response_hash: 70216fb22d8ccfb6

## Final Output
- answer_chars: 94
- answer_hash: 70216fb22d8ccfb6
- success: True

## Request Complete
- request_end: 2026-08-13T22:14:54.615
- request_duration_ms: 7053
- success: True
- final_source: generation

