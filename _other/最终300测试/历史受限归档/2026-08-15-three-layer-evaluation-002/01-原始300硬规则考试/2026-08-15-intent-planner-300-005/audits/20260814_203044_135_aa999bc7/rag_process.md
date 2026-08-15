# RAG Process

audit_id: 20260814_203044_135_aa999bc7
timestamp: 2026-08-14T20:30:44.136
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:30:44.136
- end: 2026-08-14T20:30:44.136
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:30:48.984
- end: 2026-08-14T20:30:48.984
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.93
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4847
- attempt_count: 1
- response_hash: 7b6202ba7f631917166f494cd97a5a64157fa7a281fcb2260c3e6806ca8d1efd
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:30:48.987
- end: 2026-08-14T20:30:48.987
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 28d180e6a7ec73f45d2971f031bc9222eb93b0c7d67da3eb148bc910044f4b99
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:30:48.988
- end: 2026-08-14T20:30:48.988
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:30:48.988+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:30:48.991
- end: 2026-08-14T20:30:48.991
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:30:48.988+00:00
- result_count: 2

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:30:48.992
- end: 2026-08-14T20:30:48.992
- duration_ms: 0
- entity_id: tipdoc_b43f2b437984
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:30:49.006
- end: 2026-08-14T20:30:49.006
- duration_ms: 0
- parent_id: tipdoc_b43f2b437984
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2764
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
- duration_ms: 20791
- response_chars: 1115
- response_hash: cf093c7a75161a07

## Final Output
- answer_chars: 1115
- answer_hash: cf093c7a75161a07
- success: True

## Request Complete
- request_end: 2026-08-14T20:31:09.798
- request_duration_ms: 25662
- success: True
- final_source: generation

