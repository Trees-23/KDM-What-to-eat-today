# RAG Process

audit_id: 20260814_201629_951_677554c7
timestamp: 2026-08-14T20:16:29.952
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:16:29.952
- end: 2026-08-14T20:16:29.952
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 15

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:16:33.971
- end: 2026-08-14T20:16:33.971
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.96
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4019
- attempt_count: 1
- response_hash: dcddc2352fe9632a6f55b2ae11e8e866b8fd1134c67d797977c7dddbf83449f8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:16:33.975
- end: 2026-08-14T20:16:33.975
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 4e093cb6496f758e6e39dc6ae5974ad0eca9df4f2ff95cada8cc7c8e0d3b276a
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:16:33.976
- end: 2026-08-14T20:16:33.976
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:16:33.976+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:16:33.982
- end: 2026-08-14T20:16:33.982
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:16:33.976+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:16:33.983
- end: 2026-08-14T20:16:33.983
- duration_ms: 0
- entity_id: 201002350
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T20:16:33.987
- end: 2026-08-14T20:16:33.987
- duration_ms: 0
- recipe_id: 201002350
- step_id: 201002360

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:16:33.990
- end: 2026-08-14T20:16:33.990
- duration_ms: 0
- parent_id: 201002350
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201002360
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1774
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
- duration_ms: 5837
- response_chars: 121
- response_hash: 1065790267edf75a

## Final Output
- answer_chars: 121
- answer_hash: 1065790267edf75a
- success: True

## Request Complete
- request_end: 2026-08-14T20:16:39.829
- request_duration_ms: 9876
- success: True
- final_source: generation

