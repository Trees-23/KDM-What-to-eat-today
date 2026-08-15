# RAG Process

audit_id: 20260813_201650_058_63e19a51
timestamp: 2026-08-13T20:16:50.059
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:16:50.059
- end: 2026-08-13T20:16:50.059
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 26

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:16:53.472
- end: 2026-08-13T20:16:53.472
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3413
- attempt_count: 1
- response_hash: adad04575b46f677e5e88ad7c8a5e5ba7929ec11397ef59fdb48f37de0e19dc3
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:16:53.476
- end: 2026-08-13T20:16:53.476
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:16:53.476
- end: 2026-08-13T20:16:53.476
- duration_ms: 0
- entity_id: 201000023
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:16:53.483
- end: 2026-08-13T20:16:53.483
- duration_ms: 0
- parent_id: 201000023
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1358
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

## Event / claim_policy
- stage: claim_policy
- status: blocked_and_replaced
- start: 2026-08-13T20:17:10.353
- end: 2026-08-13T20:17:10.353
- duration_ms: 0
- forbidden_claim_count: 1
- forbidden_claim_hash: 51fdcf8ee9da5f0d
- replacement_chars: 55

## Generation Non-Stream
- status: success
- duration_ms: 16869
- response_chars: 55
- response_hash: e5e6f28dd8a6314a

## Final Output
- answer_chars: 55
- answer_hash: e5e6f28dd8a6314a
- success: True

## Request Complete
- request_end: 2026-08-13T20:17:10.354
- request_duration_ms: 20295
- success: True
- final_source: generation

