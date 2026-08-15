# RAG Process

audit_id: 20260814_201723_219_4ca09bbd
timestamp: 2026-08-14T20:17:23.220
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:17:23.220
- end: 2026-08-14T20:17:23.220
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 15

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:17:26.795
- end: 2026-08-14T20:17:26.795
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3575
- attempt_count: 1
- response_hash: e1ff4d79fd679531b060a134c2a5d5907792f81f0cfd95c135e9942428d7f193
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:17:26.799
- end: 2026-08-14T20:17:26.799
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: dbb64ed666211d15ad5cfae6fd3a67f9bda147fb44cb49dd4b7d46ea24e9a8f5
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:17:26.800
- end: 2026-08-14T20:17:26.800
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:17:26.800+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:17:26.802
- end: 2026-08-14T20:17:26.802
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:17:26.800+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:17:26.802
- end: 2026-08-14T20:17:26.802
- duration_ms: 0
- entity_id: 201003314
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T20:17:26.804
- end: 2026-08-14T20:17:26.804
- duration_ms: 0
- recipe_id: 201003314
- step_id: 201003328

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:17:26.805
- end: 2026-08-14T20:17:26.805
- duration_ms: 0
- parent_id: 201003314
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201003328
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1655
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
- duration_ms: 5639
- response_chars: 97
- response_hash: b9ed8404633f86fd

## Final Output
- answer_chars: 97
- answer_hash: b9ed8404633f86fd
- success: True

## Request Complete
- request_end: 2026-08-14T20:17:32.446
- request_duration_ms: 9225
- success: True
- final_source: generation

