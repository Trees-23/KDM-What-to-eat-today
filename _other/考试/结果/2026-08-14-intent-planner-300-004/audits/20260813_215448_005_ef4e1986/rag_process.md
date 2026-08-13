# RAG Process

audit_id: 20260813_215448_005_ef4e1986
timestamp: 2026-08-13T21:54:48.006
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:54:48.006
- end: 2026-08-13T21:54:48.006
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 15

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:54:51.649
- end: 2026-08-13T21:54:51.649
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3643
- attempt_count: 1
- response_hash: 3d1696d05071a7999589906716dc5302c634e83268afad8b6eac6107d8e29ad8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:54:51.657
- end: 2026-08-13T21:54:51.657
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: dbb64ed666211d15ad5cfae6fd3a67f9bda147fb44cb49dd4b7d46ea24e9a8f5
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:54:51.658
- end: 2026-08-13T21:54:51.658
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:54:51.658+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T21:54:51.661
- end: 2026-08-13T21:54:51.661
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:54:51.658+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T21:54:51.662
- end: 2026-08-13T21:54:51.662
- duration_ms: 0
- entity_id: 201003314
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T21:54:51.665
- end: 2026-08-13T21:54:51.665
- duration_ms: 0
- recipe_id: 201003314
- step_id: 201003328

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T21:54:51.668
- end: 2026-08-13T21:54:51.668
- duration_ms: 0
- parent_id: 201003314
- build_id: pds_8ed95d0ee2ef5e64d703abd6
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 3401
- response_chars: 45
- response_hash: dcf63da8efbd64d1

## Final Output
- answer_chars: 45
- answer_hash: dcf63da8efbd64d1
- success: True

## Request Complete
- request_end: 2026-08-13T21:54:55.071
- request_duration_ms: 7064
- success: True
- final_source: generation

