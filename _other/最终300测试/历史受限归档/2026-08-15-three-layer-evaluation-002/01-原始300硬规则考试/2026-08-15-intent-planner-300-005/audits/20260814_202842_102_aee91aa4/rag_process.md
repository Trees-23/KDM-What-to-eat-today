# RAG Process

audit_id: 20260814_202842_102_aee91aa4
timestamp: 2026-08-14T20:28:42.103
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:28:42.103
- end: 2026-08-14T20:28:42.103
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:28:46.371
- end: 2026-08-14T20:28:46.371
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.94
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': ['BOIL'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4267
- attempt_count: 1
- response_hash: 7101cfb1fc9a554d419fe97433328530baf047161e676dd0a21e31dfa4e1107f
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:28:46.374
- end: 2026-08-14T20:28:46.374
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 745ced9bfc2012d2501cba0fabefdfc7675e6be64c21c22ccdbd8cc5bd1570c5
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': ['BOIL'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:28:46.375
- end: 2026-08-14T20:28:46.375
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:28:46.375+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:28:46.378
- end: 2026-08-14T20:28:46.378
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:28:46.375+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:28:46.378
- end: 2026-08-14T20:28:46.378
- duration_ms: 0
- entity_id: tipdoc_beafa0e516d2
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:28:46.391
- end: 2026-08-14T20:28:46.391
- duration_ms: 0
- parent_id: tipdoc_beafa0e516d2
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1900
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
- duration_ms: 14493
- response_chars: 454
- response_hash: c7a1e71a2b7e90e2

## Final Output
- answer_chars: 454
- answer_hash: c7a1e71a2b7e90e2
- success: True

## Request Complete
- request_end: 2026-08-14T20:29:00.886
- request_duration_ms: 18782
- success: True
- final_source: generation

