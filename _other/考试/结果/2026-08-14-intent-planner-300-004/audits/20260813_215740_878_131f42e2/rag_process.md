# RAG Process

audit_id: 20260813_215740_878_131f42e2
timestamp: 2026-08-13T21:57:40.879
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:57:40.880
- end: 2026-08-13T21:57:40.880
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 37

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:57:44.396
- end: 2026-08-13T21:57:44.396
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': ['STEAM'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3515
- attempt_count: 1
- response_hash: 37db1e3a29ceb428ddda56dd3429ebc056cb79fa814eb5fb9b7139ec557ce31c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:57:44.401
- end: 2026-08-13T21:57:44.401
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 781dcb5947c3e0f563a9d164ac26c0772e4a403e998af192225f3e0f943c3776
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': ['STEAM'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:57:44.402
- end: 2026-08-13T21:57:44.402
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:57:44.402+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T21:57:44.406
- end: 2026-08-13T21:57:44.406
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:57:44.402+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T21:57:44.406
- end: 2026-08-13T21:57:44.406
- duration_ms: 0
- entity_id: 201004991
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T21:57:44.409
- end: 2026-08-13T21:57:44.409
- duration_ms: 0
- recipe_id: 201004991
- step_id: 201004994

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T21:57:44.412
- end: 2026-08-13T21:57:44.412
- duration_ms: 0
- parent_id: 201004991
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- anchor_id: 201004994
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1397
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
- duration_ms: 5685
- response_chars: 95
- response_hash: b47e259deec641b2

## Final Output
- answer_chars: 95
- answer_hash: b47e259deec641b2
- success: True

## Request Complete
- request_end: 2026-08-13T21:57:50.099
- request_duration_ms: 9218
- success: True
- final_source: generation

