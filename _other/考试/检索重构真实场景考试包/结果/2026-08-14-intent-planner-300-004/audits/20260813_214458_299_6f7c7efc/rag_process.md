# RAG Process

audit_id: 20260813_214458_299_6f7c7efc
timestamp: 2026-08-13T21:44:58.300
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:44:58.301
- end: 2026-08-13T21:44:58.301
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 23

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:45:01.906
- end: 2026-08-13T21:45:01.906
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': ['STEAM'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3605
- attempt_count: 1
- response_hash: 823316751aeb5e25cf28ec65bcde346c33dd7e8589716ef805a231891231142a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:45:01.910
- end: 2026-08-13T21:45:01.910
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': ['STEAM'], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T21:45:01.910
- end: 2026-08-13T21:45:01.910
- duration_ms: 0
- entity_id: 201000257
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T21:45:01.916
- end: 2026-08-13T21:45:01.916
- duration_ms: 0
- parent_id: 201000257
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1359
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
- duration_ms: 14187
- response_chars: 679
- response_hash: 6c58bc39aa38bb48

## Final Output
- answer_chars: 679
- answer_hash: 6c58bc39aa38bb48
- success: True

## Request Complete
- request_end: 2026-08-13T21:45:16.106
- request_duration_ms: 17805
- success: True
- final_source: generation

