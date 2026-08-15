# RAG Process

audit_id: 20260814_173911_504_6837b7c7
timestamp: 2026-08-14T17:39:11.514
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T17:39:11.514
- end: 2026-08-14T17:39:11.514
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 37

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T17:39:17.605
- end: 2026-08-14T17:39:17.605
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['金针菇'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6091
- attempt_count: 1
- response_hash: 4cff14fca098308c6bd5afbca8ef3fc1239137097d5c5ea2de38f0b611cdb09c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T17:39:17.617
- end: 2026-08-14T17:39:17.617
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 11f888249c3807bb3a2eaeafff5f41bcbab3ac3d19c4799bcfef69694be8d1a2
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T17:39:17.617
- end: 2026-08-14T17:39:17.617
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T17:39:17.617+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T17:39:17.619
- end: 2026-08-14T17:39:17.619
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T17:39:17.617+00:00
- result_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:39:17.620
- end: 2026-08-14T17:39:17.620
- duration_ms: 0
- entity_id: 201003862
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:39:17.626
- end: 2026-08-14T17:39:17.626
- duration_ms: 0
- parent_id: 201003862
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:39:17.627
- end: 2026-08-14T17:39:17.627
- duration_ms: 0
- entity_id: 201004863
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:39:17.633
- end: 2026-08-14T17:39:17.633
- duration_ms: 0
- parent_id: 201004863
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:39:17.633
- end: 2026-08-14T17:39:17.633
- duration_ms: 0
- entity_id: 201005212
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:39:17.640
- end: 2026-08-14T17:39:17.640
- duration_ms: 0
- parent_id: 201005212
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:39:17.640
- end: 2026-08-14T17:39:17.640
- duration_ms: 0
- entity_id: 201005289
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:39:17.646
- end: 2026-08-14T17:39:17.646
- duration_ms: 0
- parent_id: 201005289
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4586
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 4
- limitation_count: 0
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Generation Config
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 11734
- response_chars: 162
- response_hash: 7124cabb00669830

## Final Output
- answer_chars: 162
- answer_hash: 7124cabb00669830
- success: True

## Request Complete
- request_end: 2026-08-14T17:39:29.382
- request_duration_ms: 17867
- success: True
- final_source: generation

