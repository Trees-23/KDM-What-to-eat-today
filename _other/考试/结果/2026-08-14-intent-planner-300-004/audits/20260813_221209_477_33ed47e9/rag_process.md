# RAG Process

audit_id: 20260813_221209_477_33ed47e9
timestamp: 2026-08-13T22:12:09.477
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:12:09.478
- end: 2026-08-13T22:12:09.478
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 15

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:12:12.524
- end: 2026-08-13T22:12:12.524
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3797
- attempt_count: 1
- response_hash: 025fde6b21b08c71879ff7667fe2858507b1720490c26b8941d1a5d749dbbcf3
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:12:12.532
- end: 2026-08-13T22:12:12.532
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: a7f0ebc6e455415114ea01b7167b88b25107fd706779f78fa6b832c68d5bca92
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:12:12.532
- end: 2026-08-13T22:12:12.532
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:12:12.532+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:12:12.535
- end: 2026-08-13T22:12:12.535
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:12:12.532+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:12.535
- end: 2026-08-13T22:12:12.535
- duration_ms: 0
- entity_id: 201000272
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:12.550
- end: 2026-08-13T22:12:12.550
- duration_ms: 0
- parent_id: 201000272
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1567
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
- duration_ms: 8447
- response_chars: 326
- response_hash: 4ccf87279c6ccba2

## Final Output
- answer_chars: 326
- answer_hash: 4ccf87279c6ccba2
- success: True

## Request Complete
- request_end: 2026-08-13T22:12:20.999
- request_duration_ms: 11521
- success: True
- final_source: generation

