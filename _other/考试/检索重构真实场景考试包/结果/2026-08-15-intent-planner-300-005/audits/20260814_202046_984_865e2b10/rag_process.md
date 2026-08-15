# RAG Process

audit_id: 20260814_202046_984_865e2b10
timestamp: 2026-08-14T20:20:46.985
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:20:46.986
- end: 2026-08-14T20:20:46.986
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 39

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:20:50.612
- end: 2026-08-14T20:20:50.612
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3626
- attempt_count: 1
- response_hash: b6fa07530964928f7b5b4bb9124b896d0e94fcb8f1e1bba96ce1c470c19b8746
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:20:50.615
- end: 2026-08-14T20:20:50.615
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 07380e993f672ad987a8b9c012a2cb42a8107b6790f2a4f10e751f768ef15ec9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:20:50.615
- end: 2026-08-14T20:20:50.615
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:20:50.615+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:20:50.617
- end: 2026-08-14T20:20:50.617
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:20:50.615+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:20:50.617
- end: 2026-08-14T20:20:50.617
- duration_ms: 0
- entity_id: 201005669
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T20:20:50.618
- end: 2026-08-14T20:20:50.618
- duration_ms: 0
- recipe_id: 201005669
- step_id: 201005675

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:20:50.619
- end: 2026-08-14T20:20:50.619
- duration_ms: 0
- parent_id: 201005669
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201005675
- chunk_count: 2

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1500
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
- duration_ms: 9688
- response_chars: 144
- response_hash: 01a52d199edc5b0f

## Final Output
- answer_chars: 144
- answer_hash: 01a52d199edc5b0f
- success: True

## Request Complete
- request_end: 2026-08-14T20:21:00.309
- request_duration_ms: 13323
- success: True
- final_source: generation

