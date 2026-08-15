# RAG Process

audit_id: 20260813_220118_632_da11da34
timestamp: 2026-08-13T22:01:18.632
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:01:18.633
- end: 2026-08-13T22:01:18.633
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 42

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:01:22.378
- end: 2026-08-13T22:01:22.378
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3745
- attempt_count: 1
- response_hash: 26f0b326d6b8f331e27e96047433e4b6aa96914258c42172673afe6b496e8315
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:01:22.383
- end: 2026-08-13T22:01:22.383
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: ecbd4ae16cfdeb2d53700df1e052aa7ef844fe68ef05da1243df6e01a43bb776
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:01:22.383
- end: 2026-08-13T22:01:22.383
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T22:01:22.383+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:01:22.387
- end: 2026-08-13T22:01:22.387
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T22:01:22.383+00:00
- result_count: 6

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:01:22.387
- end: 2026-08-13T22:01:22.387
- duration_ms: 0
- entity_id: tipdoc_4ba80da791e4
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:01:22.399
- end: 2026-08-13T22:01:22.399
- duration_ms: 0
- parent_id: tipdoc_4ba80da791e4
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 10

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4260
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
- duration_ms: 20130
- response_chars: 1074
- response_hash: 1795b8efb61f0355

## Final Output
- answer_chars: 1074
- answer_hash: 1795b8efb61f0355
- success: True

## Request Complete
- request_end: 2026-08-13T22:01:42.531
- request_duration_ms: 23898
- success: True
- final_source: generation

