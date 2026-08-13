# RAG Process

audit_id: 20260813_202129_935_c4f9e9cb
timestamp: 2026-08-13T20:21:29.936
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:21:29.936
- end: 2026-08-13T20:21:29.936
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:21:34.327
- end: 2026-08-13T20:21:34.327
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4391
- attempt_count: 1
- response_hash: db29708324f21dd618031a8de107e1e5c8c93f2408cb2cbb6b8e0ff4cba336f8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:21:34.330
- end: 2026-08-13T20:21:34.330
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:21:34.331
- end: 2026-08-13T20:21:34.331
- duration_ms: 0
- entity_id: 201000730
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:21:34.338
- end: 2026-08-13T20:21:34.338
- duration_ms: 0
- parent_id: 201000730
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1075
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
- duration_ms: 13292
- response_chars: 502
- response_hash: b1e89cde7faf8b5b

## Final Output
- answer_chars: 502
- answer_hash: b1e89cde7faf8b5b
- success: True

## Request Complete
- request_end: 2026-08-13T20:21:47.632
- request_duration_ms: 17695
- success: True
- final_source: generation

