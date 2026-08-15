# RAG Process

audit_id: 20260813_191359_687_f1a45686
timestamp: 2026-08-13T19:13:59.688
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:13:59.688
- end: 2026-08-13T19:13:59.688
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:14:03.437
- end: 2026-08-13T19:14:03.437
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3748
- attempt_count: 1
- response_hash: b22c87dc24b4c356a8cdbf96baff725c028b54bad0c814461d70e2de7637303f
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:14:03.452
- end: 2026-08-13T19:14:03.452
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 2b379ad625a260f18b1fac88d4a4ed750fdaad83b19aff20975080868618ac72
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:14:03.452
- end: 2026-08-13T19:14:03.452
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:14:03.452+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:14:03.454
- end: 2026-08-13T19:14:03.454
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:14:03.452+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:14:03.454
- end: 2026-08-13T19:14:03.454
- duration_ms: 0
- entity_id: 201003793
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T19:14:03.457
- end: 2026-08-13T19:14:03.457
- duration_ms: 0
- recipe_id: 201003793
- step_id: 201003808

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:14:03.458
- end: 2026-08-13T19:14:03.458
- duration_ms: 0
- parent_id: 201003793
- build_id: pds_2a8c0807733eb8022a623659
- anchor_id: 201003808
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1802
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
- duration_ms: 9103
- response_chars: 147
- response_hash: f7a9e0091150da4d

## Final Output
- answer_chars: 147
- answer_hash: f7a9e0091150da4d
- success: True

## Request Complete
- request_end: 2026-08-13T19:14:12.563
- request_duration_ms: 12874
- success: True
- final_source: generation

