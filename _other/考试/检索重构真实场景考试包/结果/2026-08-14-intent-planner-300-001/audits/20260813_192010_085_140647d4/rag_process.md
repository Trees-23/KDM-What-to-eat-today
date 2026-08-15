# RAG Process

audit_id: 20260813_192010_085_140647d4
timestamp: 2026-08-13T19:20:10.085
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:20:10.086
- end: 2026-08-13T19:20:10.085
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:20:16.540
- end: 2026-08-13T19:20:16.540
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': ['BOIL'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6980
- attempt_count: 1
- response_hash: 2067c0f6336292bc13a48e4a964fe915a38ae0b08bafaf0670d2d9b5bc773313
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:20:16.546
- end: 2026-08-13T19:20:16.546
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 745ced9bfc2012d2501cba0fabefdfc7675e6be64c21c22ccdbd8cc5bd1570c5
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': ['BOIL'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:20:16.546
- end: 2026-08-13T19:20:16.546
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T19:20:16.546+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:20:16.550
- end: 2026-08-13T19:20:16.550
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T19:20:16.546+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:20:16.550
- end: 2026-08-13T19:20:16.550
- duration_ms: 0
- entity_id: tipdoc_beafa0e516d2
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:20:16.562
- end: 2026-08-13T19:20:16.562
- duration_ms: 0
- parent_id: tipdoc_beafa0e516d2
- build_id: pds_2a8c0807733eb8022a623659
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 12210
- response_chars: 611
- response_hash: e4bded683b2236aa

## Final Output
- answer_chars: 611
- answer_hash: e4bded683b2236aa
- success: True

## Request Complete
- request_end: 2026-08-13T19:20:28.774
- request_duration_ms: 18688
- success: True
- final_source: generation

