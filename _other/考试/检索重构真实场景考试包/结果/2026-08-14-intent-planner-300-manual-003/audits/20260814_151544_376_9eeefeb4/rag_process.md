# RAG Process

audit_id: 20260814_151544_376_9eeefeb4
timestamp: 2026-08-14T15:15:44.376
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:15:44.376
- end: 2026-08-14T15:15:44.376
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 19

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:15:53.834
- end: 2026-08-14T15:15:53.834
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 9458
- attempt_count: 1
- response_hash: 6c14e1ea462d46272b1844674f59211989919ca6b9bac90aecf263daaf4c51f6
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:15:53.837
- end: 2026-08-14T15:15:53.837
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 77043a35d5978c43c70252e2beb4dd858c42dd4202083078fdc27c3c726407d8
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:15:53.837
- end: 2026-08-14T15:15:53.837
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:15:53.837+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:15:53.839
- end: 2026-08-14T15:15:53.839
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:15:53.837+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:15:53.839
- end: 2026-08-14T15:15:53.839
- duration_ms: 0
- entity_id: 201000319
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T15:15:53.841
- end: 2026-08-14T15:15:53.841
- duration_ms: 0
- recipe_id: 201000319
- step_id: 201000330

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:15:53.842
- end: 2026-08-14T15:15:53.842
- duration_ms: 0
- parent_id: 201000319
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201000330
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1621
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
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 6682
- response_chars: 138
- response_hash: 516ec009ad5e08db

## Final Output
- answer_chars: 138
- answer_hash: 516ec009ad5e08db
- success: True

## Request Complete
- request_end: 2026-08-14T15:16:00.526
- request_duration_ms: 16149
- success: True
- final_source: generation

