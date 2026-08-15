# RAG Process

audit_id: 20260814_202136_799_9af7fcb4
timestamp: 2026-08-14T20:21:36.800
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:21:36.800
- end: 2026-08-14T20:21:36.800
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 38

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:21:40.861
- end: 2026-08-14T20:21:40.861
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.96
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4061
- attempt_count: 1
- response_hash: 6756658f358b155710b1b6b6dcf4f501e09fdfa38713d06751e81e4d04126093
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:21:40.866
- end: 2026-08-14T20:21:40.866
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: fbd9c9128cfdafcaf9e345ddff7a7d1f342259740444d877874ba00794ec81cf
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:21:40.866
- end: 2026-08-14T20:21:40.866
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:21:40.866+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:21:40.869
- end: 2026-08-14T20:21:40.869
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:21:40.866+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:21:40.869
- end: 2026-08-14T20:21:40.869
- duration_ms: 0
- entity_id: 201003873
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T20:21:40.872
- end: 2026-08-14T20:21:40.872
- duration_ms: 0
- recipe_id: 201003873
- step_id: 201003881

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:21:40.874
- end: 2026-08-14T20:21:40.874
- duration_ms: 0
- parent_id: 201003873
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201003881
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1378
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
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 10100
- response_chars: 137
- response_hash: 2b88f14154778da2

## Final Output
- answer_chars: 137
- answer_hash: 2b88f14154778da2
- success: True

## Request Complete
- request_end: 2026-08-14T20:21:50.976
- request_duration_ms: 14175
- success: True
- final_source: generation

