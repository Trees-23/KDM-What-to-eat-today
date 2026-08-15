# RAG Process

audit_id: 20260813_221519_001_9445a3c9
timestamp: 2026-08-13T22:15:19.002
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:15:19.002
- end: 2026-08-13T22:15:19.002
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 37

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:15:22.872
- end: 2026-08-13T22:15:22.872
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4588
- attempt_count: 1
- response_hash: 4bac3b5d165408adbf17be1977a5af7df9d3e595db6fb92a314ff40a75e3dead
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:15:22.879
- end: 2026-08-13T22:15:22.879
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 11f888249c3807bb3a2eaeafff5f41bcbab3ac3d19c4799bcfef69694be8d1a2
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:15:22.880
- end: 2026-08-13T22:15:22.880
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:15:22.879+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:15:22.883
- end: 2026-08-13T22:15:22.883
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:15:22.879+00:00
- result_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:15:22.884
- end: 2026-08-13T22:15:22.884
- duration_ms: 0
- entity_id: 201003862
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:15:22.897
- end: 2026-08-13T22:15:22.897
- duration_ms: 0
- parent_id: 201003862
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:15:22.897
- end: 2026-08-13T22:15:22.897
- duration_ms: 0
- entity_id: 201004863
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:15:22.904
- end: 2026-08-13T22:15:22.904
- duration_ms: 0
- parent_id: 201004863
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:15:22.904
- end: 2026-08-13T22:15:22.904
- duration_ms: 0
- entity_id: 201005212
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:15:22.911
- end: 2026-08-13T22:15:22.911
- duration_ms: 0
- parent_id: 201005212
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:15:22.912
- end: 2026-08-13T22:15:22.912
- duration_ms: 0
- entity_id: 201005289
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:15:22.923
- end: 2026-08-13T22:15:22.923
- duration_ms: 0
- parent_id: 201005289
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4586
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 4
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
- duration_ms: 4066
- response_chars: 124
- response_hash: cebd0eff0f6f61e4

## Final Output
- answer_chars: 124
- answer_hash: cebd0eff0f6f61e4
- success: True

## Request Complete
- request_end: 2026-08-13T22:15:26.991
- request_duration_ms: 7989
- success: True
- final_source: generation

