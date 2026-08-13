# RAG Process

audit_id: 20260813_220838_722_a77ea1fb
timestamp: 2026-08-13T22:08:38.723
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:08:38.723
- end: 2026-08-13T22:08:38.723
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 22

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:08:42.611
- end: 2026-08-13T22:08:42.610
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3887
- attempt_count: 1
- response_hash: 6f7c20e5327761bcecec3995c7ab0df7598d0c0b46639e80a2f9df10f50b5a5a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:08:42.615
- end: 2026-08-13T22:08:42.615
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 94bb6d0be45913225921856cb56f256a724fa4a0a615ad99d88e15cb77721a4c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:08:42.615
- end: 2026-08-13T22:08:42.615
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T22:08:42.615+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:08:42.617
- end: 2026-08-13T22:08:42.617
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T22:08:42.615+00:00
- result_count: 9

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:08:42.618
- end: 2026-08-13T22:08:42.618
- duration_ms: 0
- entity_id: tipdoc_0899584efc31
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:08:42.629
- end: 2026-08-13T22:08:42.629
- duration_ms: 0
- parent_id: tipdoc_0899584efc31
- build_id: pds_8ed95d0ee2ef5e64d703abd6
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 18796
- response_chars: 864
- response_hash: 3ff1822ab4014982

## Final Output
- answer_chars: 864
- answer_hash: 3ff1822ab4014982
- success: True

## Request Complete
- request_end: 2026-08-13T22:09:01.428
- request_duration_ms: 22705
- success: True
- final_source: generation

