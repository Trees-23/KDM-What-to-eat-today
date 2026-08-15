# RAG Process

audit_id: 20260813_202642_371_0e0347a0
timestamp: 2026-08-13T20:26:42.372
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:26:42.372
- end: 2026-08-13T20:26:42.372
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 37

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:26:45.854
- end: 2026-08-13T20:26:45.854
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': ['STEAM'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4092
- attempt_count: 1
- response_hash: 7ab40abdb24d6faef4c22b72ea672ca0e03295de37717b6efcf418fae76b8309
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:26:45.857
- end: 2026-08-13T20:26:45.857
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 781dcb5947c3e0f563a9d164ac26c0772e4a403e998af192225f3e0f943c3776
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': ['STEAM'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:26:45.857
- end: 2026-08-13T20:26:45.857
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T20:26:45.857+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:26:45.859
- end: 2026-08-13T20:26:45.859
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T20:26:45.857+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:26:45.859
- end: 2026-08-13T20:26:45.859
- duration_ms: 0
- entity_id: 201004991
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T20:26:45.861
- end: 2026-08-13T20:26:45.861
- duration_ms: 0
- recipe_id: 201004991
- step_id: 201004994

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:26:45.862
- end: 2026-08-13T20:26:45.862
- duration_ms: 0
- parent_id: 201004991
- build_id: pds_2a8c0807733eb8022a623659
- anchor_id: 201004994
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1397
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
- duration_ms: 5749
- response_chars: 148
- response_hash: 53efeb1955760af8

## Final Output
- answer_chars: 148
- answer_hash: 53efeb1955760af8
- success: True

## Request Complete
- request_end: 2026-08-13T20:26:51.613
- request_duration_ms: 9241
- success: True
- final_source: generation

