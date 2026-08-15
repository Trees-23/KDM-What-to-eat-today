# RAG Process

audit_id: 20260814_203454_785_cadc08a7
timestamp: 2026-08-14T20:34:54.786
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:34:54.787
- end: 2026-08-14T20:34:54.787
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:34:58.358
- end: 2026-08-14T20:34:58.358
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3571
- attempt_count: 1
- response_hash: 76ea794b09aec72b1ccf14a648cda2436ffd380da9562aee1b44b04689ec2c38
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:34:58.362
- end: 2026-08-14T20:34:58.362
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 1247acfdd5c21718a3bb3abfef8cb6e3482e5292b93e7e1e376700ad22c6ec3c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:34:58.362
- end: 2026-08-14T20:34:58.362
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:34:58.362+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:34:58.366
- end: 2026-08-14T20:34:58.366
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:34:58.362+00:00
- result_count: 8

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:34:58.366
- end: 2026-08-14T20:34:58.366
- duration_ms: 0
- entity_id: tipdoc_7ce59b628288
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:34:58.380
- end: 2026-08-14T20:34:58.380
- duration_ms: 0
- parent_id: tipdoc_7ce59b628288
- build_id: pds_51e5e228cb4a935de64e2b7a
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
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 25204
- response_chars: 959
- response_hash: 91b3063124f78efb

## Final Output
- answer_chars: 959
- answer_hash: 91b3063124f78efb
- success: True

## Request Complete
- request_end: 2026-08-14T20:35:23.586
- request_duration_ms: 28799
- success: True
- final_source: generation

