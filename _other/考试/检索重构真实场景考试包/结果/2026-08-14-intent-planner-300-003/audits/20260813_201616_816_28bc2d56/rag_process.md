# RAG Process

audit_id: 20260813_201616_816_28bc2d56
timestamp: 2026-08-13T20:16:16.817
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:16:16.817
- end: 2026-08-13T20:16:16.817
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 22

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:16:20.542
- end: 2026-08-13T20:16:20.542
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3724
- attempt_count: 1
- response_hash: ac760247836a7aae0996f802ead2595cad7d7e5f68caadd07f2a5f95862b1fb7
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:16:20.544
- end: 2026-08-13T20:16:20.544
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:16:20.544
- end: 2026-08-13T20:16:20.544
- duration_ms: 0
- entity_id: 201000272
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:16:20.551
- end: 2026-08-13T20:16:20.551
- duration_ms: 0
- parent_id: 201000272
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1266
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
- duration_ms: 13101
- response_chars: 622
- response_hash: 6a2a5048080d9325

## Final Output
- answer_chars: 622
- answer_hash: 6a2a5048080d9325
- success: True

## Request Complete
- request_end: 2026-08-13T20:16:33.653
- request_duration_ms: 16835
- success: True
- final_source: generation

