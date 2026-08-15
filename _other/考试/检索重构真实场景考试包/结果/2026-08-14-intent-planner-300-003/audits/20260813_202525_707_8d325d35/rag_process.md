# RAG Process

audit_id: 20260813_202525_707_8d325d35
timestamp: 2026-08-13T20:25:25.708
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:25:25.708
- end: 2026-08-13T20:25:25.708
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:25:29.399
- end: 2026-08-13T20:25:29.399
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': ['STEAM'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3691
- attempt_count: 1
- response_hash: 2ee4aa34f321d2f6fc9a7be232493d6efbf5d1a65a8e9fba619f8b4de7a2bfe8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:25:29.403
- end: 2026-08-13T20:25:29.403
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: b7202ceeae6457fa30fa1a90882365e5d049fa2d84f361f54c0a0973857cd083
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': ['STEAM'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:25:29.403
- end: 2026-08-13T20:25:29.403
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T20:25:29.403+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:25:29.405
- end: 2026-08-13T20:25:29.405
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T20:25:29.403+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:25:29.405
- end: 2026-08-13T20:25:29.405
- duration_ms: 0
- entity_id: 201000257
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T20:25:29.406
- end: 2026-08-13T20:25:29.406
- duration_ms: 0
- recipe_id: 201000257
- step_id: 201000265

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:25:29.408
- end: 2026-08-13T20:25:29.408
- duration_ms: 0
- parent_id: 201000257
- build_id: pds_2a8c0807733eb8022a623659
- anchor_id: 201000265
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1613
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
- duration_ms: 5404
- response_chars: 100
- response_hash: 4d42e1121fe42833

## Final Output
- answer_chars: 100
- answer_hash: 4d42e1121fe42833
- success: True

## Request Complete
- request_end: 2026-08-13T20:25:34.813
- request_duration_ms: 9105
- success: True
- final_source: generation

