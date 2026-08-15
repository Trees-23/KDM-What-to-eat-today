# RAG Process

audit_id: 20260814_173846_144_189cde51
timestamp: 2026-08-14T17:38:46.145
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T17:38:46.146
- end: 2026-08-14T17:38:46.146
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T17:38:50.963
- end: 2026-08-14T17:38:50.963
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['豆角'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4817
- attempt_count: 1
- response_hash: c312f4f502875c3a68c3d8eb95fcd7a961fe4654748faf0e7863aad3a243a5db
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T17:38:50.976
- end: 2026-08-14T17:38:50.976
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: f71c477cc83a703d82c68977bd4642ec866991bb81d40114c6efbe8c11029e76
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T17:38:50.977
- end: 2026-08-14T17:38:50.977
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T17:38:50.977+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T17:38:50.979
- end: 2026-08-14T17:38:50.979
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T17:38:50.977+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:38:50.979
- end: 2026-08-14T17:38:50.979
- duration_ms: 0
- entity_id: 201004766
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:38:50.986
- end: 2026-08-14T17:38:50.986
- duration_ms: 0
- parent_id: 201004766
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:38:50.986
- end: 2026-08-14T17:38:50.986
- duration_ms: 0
- entity_id: 201005031
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:38:50.993
- end: 2026-08-14T17:38:50.993
- duration_ms: 0
- parent_id: 201005031
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:38:50.993
- end: 2026-08-14T17:38:50.993
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:38:50.999
- end: 2026-08-14T17:38:50.999
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4351
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 3
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
- duration_ms: 6684
- response_chars: 103
- response_hash: 3b4c889d19e0d0ed

## Final Output
- answer_chars: 103
- answer_hash: 3b4c889d19e0d0ed
- success: True

## Request Complete
- request_end: 2026-08-14T17:38:57.685
- request_duration_ms: 11539
- success: True
- final_source: generation

