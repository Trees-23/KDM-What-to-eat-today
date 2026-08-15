# RAG Process

audit_id: 20260813_191029_366_f4db350d
timestamp: 2026-08-13T19:10:29.366
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:10:29.367
- end: 2026-08-13T19:10:29.367
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:10:32.908
- end: 2026-08-13T19:10:32.908
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3541
- attempt_count: 1
- response_hash: f2d21e6142482244196786b99ff31410bc3dca9ba767b01788bcaae56f8caa8a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:10:32.916
- end: 2026-08-13T19:10:32.916
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 4ff9fa6a7e6eac5e0f38f3737b1c2101d7aeb475f304807ee481e861be5e8dd9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:10:32.916
- end: 2026-08-13T19:10:32.916
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:10:32.916+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:10:32.919
- end: 2026-08-13T19:10:32.919
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:10:32.916+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:10:32.920
- end: 2026-08-13T19:10:32.920
- duration_ms: 0
- entity_id: 201002821
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T19:10:32.922
- end: 2026-08-13T19:10:32.922
- duration_ms: 0
- recipe_id: 201002821
- step_id: 201002829

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:10:32.923
- end: 2026-08-13T19:10:32.923
- duration_ms: 0
- parent_id: 201002821
- build_id: pds_2a8c0807733eb8022a623659
- anchor_id: 201002829
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1552
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
- duration_ms: 4250
- response_chars: 146
- response_hash: a213c921fe56d1c2

## Final Output
- answer_chars: 146
- answer_hash: a213c921fe56d1c2
- success: True

## Request Complete
- request_end: 2026-08-13T19:10:37.175
- request_duration_ms: 7808
- success: True
- final_source: generation

