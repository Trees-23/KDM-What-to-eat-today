# RAG Process

audit_id: 20260814_203542_380_93dc6169
timestamp: 2026-08-14T20:35:42.380
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:35:42.380
- end: 2026-08-14T20:35:42.380
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:35:46.057
- end: 2026-08-14T20:35:46.057
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['猪肉'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3676
- attempt_count: 1
- response_hash: ea73010b5e99dd6806bd8097a1af9c6337f122c61f63d3092770c2b2856f3789
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:35:46.072
- end: 2026-08-14T20:35:46.072
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: f6b8b036635df75a09eec0e7691b6c666fc00a1539a3ee17db1d41bb596cb45c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:35:46.073
- end: 2026-08-14T20:35:46.073
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:35:46.073+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:35:46.076
- end: 2026-08-14T20:35:46.076
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:35:46.073+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:35:46.076
- end: 2026-08-14T20:35:46.076
- duration_ms: 0
- entity_id: 201001780
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:35:46.089
- end: 2026-08-14T20:35:46.089
- duration_ms: 0
- parent_id: 201001780
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:35:46.089
- end: 2026-08-14T20:35:46.089
- duration_ms: 0
- entity_id: 201003372
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:35:46.098
- end: 2026-08-14T20:35:46.098
- duration_ms: 0
- parent_id: 201003372
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:35:46.098
- end: 2026-08-14T20:35:46.098
- duration_ms: 0
- entity_id: 201004709
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:35:46.104
- end: 2026-08-14T20:35:46.104
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
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 11875
- response_chars: 409
- response_hash: 93ff07cc15e16e86

## Final Output
- answer_chars: 409
- answer_hash: 93ff07cc15e16e86
- success: True

## Request Complete
- request_end: 2026-08-14T20:35:57.981
- request_duration_ms: 15600
- success: True
- final_source: generation

