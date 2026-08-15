# RAG Process

audit_id: 20260813_201958_063_98b20fd6
timestamp: 2026-08-13T20:19:58.063
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:19:58.063
- end: 2026-08-13T20:19:58.063
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 26

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:20:02.844
- end: 2026-08-13T20:20:02.844
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4780
- attempt_count: 1
- response_hash: f1ff37f008b0ea91e1954fbfd9e7f2876cdbc67da73cc7c42528b376f730a10f
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:20:02.849
- end: 2026-08-13T20:20:02.849
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:20:02.850
- end: 2026-08-13T20:20:02.850
- duration_ms: 0
- entity_id: 201004478
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:20:02.865
- end: 2026-08-13T20:20:02.865
- duration_ms: 0
- parent_id: 201004478
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1979
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
- duration_ms: 16416
- response_chars: 875
- response_hash: 0c6daffa36e4f8a4

## Final Output
- answer_chars: 875
- answer_hash: 0c6daffa36e4f8a4
- success: True

## Request Complete
- request_end: 2026-08-13T20:20:19.284
- request_duration_ms: 21220
- success: True
- final_source: generation

