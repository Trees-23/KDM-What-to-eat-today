# RAG Process

audit_id: 20260814_201917_988_2e5ad6c7
timestamp: 2026-08-14T20:19:17.988
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:19:17.989
- end: 2026-08-14T20:19:17.989
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 19

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:19:22.077
- end: 2026-08-14T20:19:22.077
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.86
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4088
- attempt_count: 1
- response_hash: fc4c203cb0e9eb680e55e104f4ab6a2ca5adbdd446946f438382fddc9ac6cb3c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:19:22.081
- end: 2026-08-14T20:19:22.081
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 4d623f76970199f80fe6dc1add4b4dc45e848ac19c62e4a5c8bfdf44a6cc5624
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:19:22.082
- end: 2026-08-14T20:19:22.082
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:19:22.082+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:19:22.085
- end: 2026-08-14T20:19:22.085
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:19:22.082+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:19:22.085
- end: 2026-08-14T20:19:22.085
- duration_ms: 0
- entity_id: 201002876
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T20:19:22.087
- end: 2026-08-14T20:19:22.087
- duration_ms: 0
- recipe_id: 201002876
- step_id: 201002887

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:19:22.090
- end: 2026-08-14T20:19:22.090
- duration_ms: 0
- parent_id: 201002876
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201002887
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1970
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
- duration_ms: 9776
- response_chars: 176
- response_hash: 91251cb76b69c45e

## Final Output
- answer_chars: 176
- answer_hash: 91251cb76b69c45e
- success: True

## Request Complete
- request_end: 2026-08-14T20:19:31.868
- request_duration_ms: 13878
- success: True
- final_source: generation

