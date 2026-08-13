# RAG Process

audit_id: 20260813_215929_997_9e623e2f
timestamp: 2026-08-13T21:59:29.998
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:59:29.998
- end: 2026-08-13T21:59:29.998
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 24

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:59:38.064
- end: 2026-08-13T21:59:38.064
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 8066
- attempt_count: 1
- response_hash: 4e9b5af6ccc12a8457d0dfde6d4e4c5488c2122f8eade07626c33edc801b4abf
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:59:38.069
- end: 2026-08-13T21:59:38.069
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: a7b8763e355e86933f9b8c976f6603cc3b34187db7dfe9036c3a0654d6bc8546
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:59:38.070
- end: 2026-08-13T21:59:38.070
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T21:59:38.070+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T21:59:38.074
- end: 2026-08-13T21:59:38.074
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T21:59:38.070+00:00
- result_count: 2

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T21:59:38.074
- end: 2026-08-13T21:59:38.074
- duration_ms: 0
- entity_id: tipdoc_42a8d9f8ff95
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T21:59:38.088
- end: 2026-08-13T21:59:38.088
- duration_ms: 0
- parent_id: tipdoc_42a8d9f8ff95
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2453
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
- duration_ms: 26378
- response_chars: 1006
- response_hash: 584431c027368424

## Final Output
- answer_chars: 1006
- answer_hash: 584431c027368424
- success: True

## Request Complete
- request_end: 2026-08-13T22:00:04.469
- request_duration_ms: 34470
- success: True
- final_source: generation

