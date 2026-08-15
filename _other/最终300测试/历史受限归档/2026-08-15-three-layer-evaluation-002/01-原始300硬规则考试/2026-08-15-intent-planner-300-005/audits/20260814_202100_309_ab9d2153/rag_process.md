# RAG Process

audit_id: 20260814_202100_309_ab9d2153
timestamp: 2026-08-14T20:21:00.309
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:21:00.309
- end: 2026-08-14T20:21:00.309
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 37

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:21:05.978
- end: 2026-08-14T20:21:05.978
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.96
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': ['STEAM'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5668
- attempt_count: 1
- response_hash: 43fbb0e9f00a5efeca73ebafa62028c5f7a51270eb5b9b4e166cac38ae67a612
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:21:05.981
- end: 2026-08-14T20:21:05.981
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 781dcb5947c3e0f563a9d164ac26c0772e4a403e998af192225f3e0f943c3776
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': ['STEAM'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:21:05.982
- end: 2026-08-14T20:21:05.982
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:21:05.981+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:21:05.983
- end: 2026-08-14T20:21:05.983
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:21:05.981+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:21:05.984
- end: 2026-08-14T20:21:05.984
- duration_ms: 0
- entity_id: 201004991
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T20:21:05.985
- end: 2026-08-14T20:21:05.985
- duration_ms: 0
- recipe_id: 201004991
- step_id: 201004994

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:21:05.986
- end: 2026-08-14T20:21:05.986
- duration_ms: 0
- parent_id: 201004991
- build_id: pds_51e5e228cb4a935de64e2b7a
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
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 5996
- response_chars: 138
- response_hash: 20fd51f5dd5c4fbb

## Final Output
- answer_chars: 138
- answer_hash: 20fd51f5dd5c4fbb
- success: True

## Request Complete
- request_end: 2026-08-14T20:21:11.984
- request_duration_ms: 11675
- success: True
- final_source: generation

