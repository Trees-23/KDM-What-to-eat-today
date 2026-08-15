# RAG Process

audit_id: 20260813_203412_858_db1a60bd
timestamp: 2026-08-13T20:34:12.859
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:34:12.859
- end: 2026-08-13T20:34:12.859
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 23

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:34:18.859
- end: 2026-08-13T20:34:18.859
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6000
- attempt_count: 1
- response_hash: f5eead113048f19e435cee679240c06d16b9703c8ce3fed787455059cd4e99e8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:34:18.863
- end: 2026-08-13T20:34:18.863
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: cd75743034fe11902cbec7152aade315d2e17d52b10a169960ef236e5547b0d8
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:34:18.864
- end: 2026-08-13T20:34:18.864
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T20:34:18.863+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:34:18.877
- end: 2026-08-13T20:34:18.877
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T20:34:18.863+00:00
- result_count: 9

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:34:18.877
- end: 2026-08-13T20:34:18.877
- duration_ms: 0
- entity_id: tipdoc_e5959b9d0464
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:34:18.893
- end: 2026-08-13T20:34:18.893
- duration_ms: 0
- parent_id: tipdoc_e5959b9d0464
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 19

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 7905
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
- duration_ms: 25930
- response_chars: 1445
- response_hash: 3b19cb36b0bfed2b

## Final Output
- answer_chars: 1445
- answer_hash: 3b19cb36b0bfed2b
- success: True

## Request Complete
- request_end: 2026-08-13T20:34:44.825
- request_duration_ms: 31966
- success: True
- final_source: generation

