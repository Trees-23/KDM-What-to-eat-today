# RAG Process

audit_id: 20260813_221502_674_eb3f07bd
timestamp: 2026-08-13T22:15:02.675
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:15:02.675
- end: 2026-08-13T22:15:02.675
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:15:06.572
- end: 2026-08-13T22:15:06.572
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3896
- attempt_count: 1
- response_hash: 62e65bce7422581a0c4fb3ec789c3c4ab4f2edfb9b64e6d37a2057dc6d47cb70
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:15:06.579
- end: 2026-08-13T22:15:06.579
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: f71c477cc83a703d82c68977bd4642ec866991bb81d40114c6efbe8c11029e76
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:15:06.579
- end: 2026-08-13T22:15:06.579
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:15:06.579+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:15:06.586
- end: 2026-08-13T22:15:06.586
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:15:06.579+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:15:06.586
- end: 2026-08-13T22:15:06.586
- duration_ms: 0
- entity_id: 201004766
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:15:06.602
- end: 2026-08-13T22:15:06.602
- duration_ms: 0
- parent_id: 201004766
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:15:06.602
- end: 2026-08-13T22:15:06.602
- duration_ms: 0
- entity_id: 201005031
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:15:06.613
- end: 2026-08-13T22:15:06.613
- duration_ms: 0
- parent_id: 201005031
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:15:06.613
- end: 2026-08-13T22:15:06.613
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:15:06.622
- end: 2026-08-13T22:15:06.622
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_8ed95d0ee2ef5e64d703abd6
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
- duration_ms: 3988
- response_chars: 113
- response_hash: f7bbb942d723a7c5

## Final Output
- answer_chars: 113
- answer_hash: f7bbb942d723a7c5
- success: True

## Request Complete
- request_end: 2026-08-13T22:15:10.613
- request_duration_ms: 7937
- success: True
- final_source: generation

