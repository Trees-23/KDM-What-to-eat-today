# RAG Process

audit_id: 20260813_215252_202_dbc880cf
timestamp: 2026-08-13T21:52:52.203
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:52:52.203
- end: 2026-08-13T21:52:52.203
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 35

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:52:56.037
- end: 2026-08-13T21:52:56.037
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3834
- attempt_count: 1
- response_hash: b257d74c6b94df9491dd90d08adf06157db34e9aeb0c60fae924415b8d54dd3d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:52:56.045
- end: 2026-08-13T21:52:56.044
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T21:52:56.045
- end: 2026-08-13T21:52:56.045
- duration_ms: 0
- entity_id: 201000935
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T21:52:56.061
- end: 2026-08-13T21:52:56.061
- duration_ms: 0
- parent_id: 201000935
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1313
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
- duration_ms: 12413
- response_chars: 494
- response_hash: e3d99134d61f8f3b

## Final Output
- answer_chars: 494
- answer_hash: e3d99134d61f8f3b
- success: True

## Request Complete
- request_end: 2026-08-13T21:53:08.476
- request_duration_ms: 16273
- success: True
- final_source: generation

