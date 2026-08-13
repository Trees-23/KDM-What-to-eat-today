# RAG Process

audit_id: 20260813_202201_471_ad397a1e
timestamp: 2026-08-13T20:22:01.472
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:22:01.472
- end: 2026-08-13T20:22:01.472
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:22:04.887
- end: 2026-08-13T20:22:04.887
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3415
- attempt_count: 1
- response_hash: 971d8fcdeeb1343e2facd42e0d27ae2b4691057a588a417160baea63fe3080ca
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:22:04.890
- end: 2026-08-13T20:22:04.890
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:22:04.890
- end: 2026-08-13T20:22:04.890
- duration_ms: 0
- entity_id: 201003939
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:22:04.897
- end: 2026-08-13T20:22:04.897
- duration_ms: 0
- parent_id: 201003939
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1337
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
- duration_ms: 14026
- response_chars: 669
- response_hash: 8e75d21902dc5e2b

## Final Output
- answer_chars: 669
- answer_hash: 8e75d21902dc5e2b
- success: True

## Request Complete
- request_end: 2026-08-13T20:22:18.925
- request_duration_ms: 17452
- success: True
- final_source: generation

