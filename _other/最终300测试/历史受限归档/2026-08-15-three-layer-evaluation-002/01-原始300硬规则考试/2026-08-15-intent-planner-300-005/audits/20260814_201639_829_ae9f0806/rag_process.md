# RAG Process

audit_id: 20260814_201639_829_ae9f0806
timestamp: 2026-08-14T20:16:39.830
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:16:39.830
- end: 2026-08-14T20:16:39.830
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:16:44.606
- end: 2026-08-14T20:16:44.606
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': ['STEAM'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4776
- attempt_count: 1
- response_hash: 0fac7eed0787c7a7cb75a3d28656202e8e909c3a32de39b6108fec2751f5a31a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:16:44.610
- end: 2026-08-14T20:16:44.610
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 4ff9fa6a7e6eac5e0f38f3737b1c2101d7aeb475f304807ee481e861be5e8dd9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': ['STEAM'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:16:44.610
- end: 2026-08-14T20:16:44.610
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:16:44.610+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:16:44.612
- end: 2026-08-14T20:16:44.612
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:16:44.610+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:16:44.612
- end: 2026-08-14T20:16:44.612
- duration_ms: 0
- entity_id: 201002821
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T20:16:44.614
- end: 2026-08-14T20:16:44.614
- duration_ms: 0
- recipe_id: 201002821
- step_id: 201002829

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:16:44.615
- end: 2026-08-14T20:16:44.615
- duration_ms: 0
- parent_id: 201002821
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201002829
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1559
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
- duration_ms: 6908
- response_chars: 133
- response_hash: d157f46c74bdab70

## Final Output
- answer_chars: 133
- answer_hash: d157f46c74bdab70
- success: True

## Request Complete
- request_end: 2026-08-14T20:16:51.524
- request_duration_ms: 11694
- success: True
- final_source: generation

