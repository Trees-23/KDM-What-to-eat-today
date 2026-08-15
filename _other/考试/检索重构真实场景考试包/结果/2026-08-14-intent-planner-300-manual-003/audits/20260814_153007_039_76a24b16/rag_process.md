# RAG Process

audit_id: 20260814_153007_039_76a24b16
timestamp: 2026-08-14T15:30:07.040
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:30:07.041
- end: 2026-08-14T15:30:07.041
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 37

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:30:11.256
- end: 2026-08-14T15:30:11.256
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4215
- attempt_count: 1
- response_hash: 5a28e95cfedcae02bd58bee977444370f1b78dc57f8435b15f4f8b70a7520b9f
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:30:11.380
- end: 2026-08-14T15:30:11.380
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: ab2f651a81dec193f0fa096a575ae486bd2762643f3c83b84c33a7e8acad9ba9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:30:11.380
- end: 2026-08-14T15:30:11.380
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:30:11.380+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:30:11.383
- end: 2026-08-14T15:30:11.383
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:30:11.380+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:30:11.383
- end: 2026-08-14T15:30:11.383
- duration_ms: 0
- entity_id: tipdoc_7e937e95d07f
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:30:11.390
- end: 2026-08-14T15:30:11.390
- duration_ms: 0
- parent_id: tipdoc_7e937e95d07f
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 7

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4662
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
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 28083
- response_chars: 1620
- response_hash: 2b72e284cd3104c3

## Final Output
- answer_chars: 1620
- answer_hash: 2b72e284cd3104c3
- success: True

## Request Complete
- request_end: 2026-08-14T15:30:39.476
- request_duration_ms: 32435
- success: True
- final_source: generation

