# RAG Process

audit_id: 20260814_152701_574_407f700a
timestamp: 2026-08-14T15:27:01.575
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:27:01.575
- end: 2026-08-14T15:27:01.575
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:27:07.651
- end: 2026-08-14T15:27:07.651
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6076
- attempt_count: 1
- response_hash: f9107d38be90074532cd19860ba0f4a0c08207e41eb82f7fbb3fe91ed8dde0a6
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:27:07.654
- end: 2026-08-14T15:27:07.654
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: d9fbd99932a537828ded0562905cc6c1f18d12c934b5e096b9da48c139e9f7c2
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:27:07.655
- end: 2026-08-14T15:27:07.655
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:27:07.654+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:27:07.659
- end: 2026-08-14T15:27:07.659
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:27:07.654+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:27:07.659
- end: 2026-08-14T15:27:07.659
- duration_ms: 0
- entity_id: tipdoc_605102de4ff3
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:27:07.672
- end: 2026-08-14T15:27:07.672
- duration_ms: 0
- parent_id: tipdoc_605102de4ff3
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 10

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4127
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
- duration_ms: 28313
- response_chars: 939
- response_hash: 8b3ed37dc889890e

## Final Output
- answer_chars: 939
- answer_hash: 8b3ed37dc889890e
- success: True

## Request Complete
- request_end: 2026-08-14T15:27:35.989
- request_duration_ms: 34413
- success: True
- final_source: generation

