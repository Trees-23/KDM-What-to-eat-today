# RAG Process

audit_id: 20260814_152735_989_57f47887
timestamp: 2026-08-14T15:27:35.990
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:27:35.991
- end: 2026-08-14T15:27:35.991
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 25

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:27:39.831
- end: 2026-08-14T15:27:39.831
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5191
- attempt_count: 1
- response_hash: 6f7c20e5327761bcecec3995c7ab0df7598d0c0b46639e80a2f9df10f50b5a5a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:27:39.836
- end: 2026-08-14T15:27:39.836
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 94bb6d0be45913225921856cb56f256a724fa4a0a615ad99d88e15cb77721a4c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:27:39.837
- end: 2026-08-14T15:27:39.837
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:27:39.836+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:27:39.840
- end: 2026-08-14T15:27:39.840
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:27:39.836+00:00
- result_count: 9

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:27:39.841
- end: 2026-08-14T15:27:39.841
- duration_ms: 0
- entity_id: tipdoc_0899584efc31
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:27:39.856
- end: 2026-08-14T15:27:39.856
- duration_ms: 0
- parent_id: tipdoc_0899584efc31
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 15

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 6126
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
- duration_ms: 32883
- response_chars: 1292
- response_hash: d2a3494ca067f3cd

## Final Output
- answer_chars: 1292
- answer_hash: d2a3494ca067f3cd
- success: True

## Request Complete
- request_end: 2026-08-14T15:28:12.743
- request_duration_ms: 36752
- success: True
- final_source: generation

