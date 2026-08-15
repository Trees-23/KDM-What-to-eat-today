# RAG Process

audit_id: 20260814_153557_759_1df9f847
timestamp: 2026-08-14T15:35:57.760
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:35:57.760
- end: 2026-08-14T15:35:57.760
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:36:02.360
- end: 2026-08-14T15:36:02.360
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['猪肉'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4599
- attempt_count: 1
- response_hash: 2647f0bbc14098295769d6f3e54488ad4493d7901199d413399a98c518f48597
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:36:02.391
- end: 2026-08-14T15:36:02.391
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: f6b8b036635df75a09eec0e7691b6c666fc00a1539a3ee17db1d41bb596cb45c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:36:02.392
- end: 2026-08-14T15:36:02.392
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T15:36:02.392+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:36:02.395
- end: 2026-08-14T15:36:02.395
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T15:36:02.392+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:36:02.395
- end: 2026-08-14T15:36:02.395
- duration_ms: 0
- entity_id: 201001780
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:36:02.403
- end: 2026-08-14T15:36:02.403
- duration_ms: 0
- parent_id: 201001780
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:36:02.404
- end: 2026-08-14T15:36:02.404
- duration_ms: 0
- entity_id: 201003372
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:36:02.414
- end: 2026-08-14T15:36:02.414
- duration_ms: 0
- parent_id: 201003372
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:36:02.415
- end: 2026-08-14T15:36:02.415
- duration_ms: 0
- entity_id: 201004709
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:36:02.422
- end: 2026-08-14T15:36:02.422
- duration_ms: 0
- parent_id: 201004709
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 3910
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
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 13919
- response_chars: 491
- response_hash: d43268d381c8e46b

## Final Output
- answer_chars: 491
- answer_hash: d43268d381c8e46b
- success: True

## Request Complete
- request_end: 2026-08-14T15:36:16.343
- request_duration_ms: 18582
- success: True
- final_source: generation

