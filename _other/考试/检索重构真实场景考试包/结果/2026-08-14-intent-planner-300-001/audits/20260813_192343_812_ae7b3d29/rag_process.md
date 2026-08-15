# RAG Process

audit_id: 20260813_192343_812_ae7b3d29
timestamp: 2026-08-13T19:23:43.813
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:23:43.813
- end: 2026-08-13T19:23:43.813
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:23:48.145
- end: 2026-08-13T19:23:48.145
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4332
- attempt_count: 1
- response_hash: 2a87a3f331c27e00bafca74c4abfbd0d5a876005bcd997f952b5b11f2007004e
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:23:48.148
- end: 2026-08-13T19:23:48.148
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 86b6f69ee220a8bff0366753292d3ae4a6c4168590176b5d173ee480f15f1def
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:23:48.148
- end: 2026-08-13T19:23:48.148
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T19:23:48.148+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:23:48.161
- end: 2026-08-13T19:23:48.161
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T19:23:48.148+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:23:48.161
- end: 2026-08-13T19:23:48.161
- duration_ms: 0
- entity_id: tipdoc_9e62e8f43239
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:23:48.170
- end: 2026-08-13T19:23:48.170
- duration_ms: 0
- parent_id: tipdoc_9e62e8f43239
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 9

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2936
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
- duration_ms: 12460
- response_chars: 354
- response_hash: 313e451cb127ed7b

## Final Output
- answer_chars: 354
- answer_hash: 313e451cb127ed7b
- success: True

## Request Complete
- request_end: 2026-08-13T19:24:00.632
- request_duration_ms: 16819
- success: True
- final_source: generation

