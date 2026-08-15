# RAG Process

audit_id: 20260813_192054_734_e974c8ba
timestamp: 2026-08-13T19:20:54.735
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:20:54.735
- end: 2026-08-13T19:20:54.735
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 23

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:21:00.990
- end: 2026-08-13T19:21:00.990
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6254
- attempt_count: 1
- response_hash: d1254d4fa4cb3a0499848ed32afdd00b1f9630706b6e626391fb99df6a4629f3
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:21:01.005
- end: 2026-08-13T19:21:01.005
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 1247acfdd5c21718a3bb3abfef8cb6e3482e5292b93e7e1e376700ad22c6ec3c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:21:01.005
- end: 2026-08-13T19:21:01.005
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T19:21:01.005+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:21:01.010
- end: 2026-08-13T19:21:01.010
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T19:21:01.005+00:00
- result_count: 8

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:21:01.010
- end: 2026-08-13T19:21:01.010
- duration_ms: 0
- entity_id: tipdoc_7ce59b628288
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:21:01.024
- end: 2026-08-13T19:21:01.024
- duration_ms: 0
- parent_id: tipdoc_7ce59b628288
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 17

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 5622
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
- duration_ms: 20004
- response_chars: 1191
- response_hash: ce764d28d720d29d

## Final Output
- answer_chars: 1191
- answer_hash: ce764d28d720d29d
- success: True

## Request Complete
- request_end: 2026-08-13T19:21:21.031
- request_duration_ms: 26296
- success: True
- final_source: generation

