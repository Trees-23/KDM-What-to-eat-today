# RAG Process

audit_id: 20260813_191044_185_d467d626
timestamp: 2026-08-13T19:10:44.187
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:10:44.188
- end: 2026-08-13T19:10:44.188
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:10:48.917
- end: 2026-08-13T19:10:48.917
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4729
- attempt_count: 1
- response_hash: 1b42910cda924a22bb47fba2617852f0c8fd4d2e857b7ede4fa71d91c54d67ff
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:10:48.922
- end: 2026-08-13T19:10:48.922
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 82a14625e682855527ee466174adc1bae7fe11eb4df975e0f4ede502d23d17c0
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:10:48.923
- end: 2026-08-13T19:10:48.923
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:10:48.923+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:10:48.925
- end: 2026-08-13T19:10:48.925
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:10:48.923+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:10:48.925
- end: 2026-08-13T19:10:48.925
- duration_ms: 0
- entity_id: 201002937
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T19:10:48.927
- end: 2026-08-13T19:10:48.927
- duration_ms: 0
- recipe_id: 201002937
- step_id: 201002950

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:10:48.928
- end: 2026-08-13T19:10:48.928
- duration_ms: 0
- parent_id: 201002937
- build_id: pds_2a8c0807733eb8022a623659
- anchor_id: 201002950
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1905
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
- duration_ms: 4519
- response_chars: 135
- response_hash: 5f00fe9a0d15ca35

## Final Output
- answer_chars: 135
- answer_hash: 5f00fe9a0d15ca35
- success: True

## Request Complete
- request_end: 2026-08-13T19:10:53.448
- request_duration_ms: 9260
- success: True
- final_source: generation

