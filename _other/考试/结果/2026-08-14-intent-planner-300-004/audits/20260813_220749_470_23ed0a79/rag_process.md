# RAG Process

audit_id: 20260813_220749_470_23ed0a79
timestamp: 2026-08-13T22:07:49.471
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:07:49.473
- end: 2026-08-13T22:07:49.473
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 18

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:07:52.848
- end: 2026-08-13T22:07:52.848
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3374
- attempt_count: 1
- response_hash: e0997f0c920d28eea0d2461583e8b1d271ff7bf377cabf8d8a9c947141be71e4
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:07:52.853
- end: 2026-08-13T22:07:52.853
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: d645ffae2eaeacec93999b701e410f2b15deff069747466a0340b8eee613d264
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:07:52.853
- end: 2026-08-13T22:07:52.853
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T22:07:52.853+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:07:52.857
- end: 2026-08-13T22:07:52.857
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T22:07:52.853+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:07:52.858
- end: 2026-08-13T22:07:52.858
- duration_ms: 0
- entity_id: tipdoc_897acc483178
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:07:52.872
- end: 2026-08-13T22:07:52.872
- duration_ms: 0
- parent_id: tipdoc_897acc483178
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 11

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4342
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
- duration_ms: 14087
- response_chars: 721
- response_hash: 383e757702fa32d0

## Final Output
- answer_chars: 721
- answer_hash: 383e757702fa32d0
- success: True

## Request Complete
- request_end: 2026-08-13T22:08:06.961
- request_duration_ms: 17488
- success: True
- final_source: generation

