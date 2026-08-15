# RAG Process

audit_id: 20260814_202124_177_a6353c2d
timestamp: 2026-08-14T20:21:24.177
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:21:24.177
- end: 2026-08-14T20:21:24.177
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 38

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:21:29.824
- end: 2026-08-14T20:21:29.824
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5647
- attempt_count: 1
- response_hash: 8c0b8d9e5737f774324139afed941e067a31ea75e3d2fc12f253cf15d803709d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:21:29.828
- end: 2026-08-14T20:21:29.828
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 42fd219a21adb874cbb0ab804c6bd0903ed07d7a86e4593166771a87814974a9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:21:29.829
- end: 2026-08-14T20:21:29.829
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:21:29.829+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:21:29.832
- end: 2026-08-14T20:21:29.832
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:21:29.829+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:21:29.832
- end: 2026-08-14T20:21:29.832
- duration_ms: 0
- entity_id: 201004863
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T20:21:29.834
- end: 2026-08-14T20:21:29.834
- duration_ms: 0
- recipe_id: 201004863
- step_id: 201004872

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:21:29.837
- end: 2026-08-14T20:21:29.837
- duration_ms: 0
- parent_id: 201004863
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201004872
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1811
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
- duration_ms: 6960
- response_chars: 188
- response_hash: 864b67b24cf11772

## Final Output
- answer_chars: 188
- answer_hash: 864b67b24cf11772
- success: True

## Request Complete
- request_end: 2026-08-14T20:21:36.799
- request_duration_ms: 12621
- success: True
- final_source: generation

