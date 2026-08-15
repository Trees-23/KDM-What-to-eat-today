# RAG Process

audit_id: 20260814_173445_057_ded74b7b
timestamp: 2026-08-14T17:34:45.058
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T17:34:45.058
- end: 2026-08-14T17:34:45.058
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T17:34:52.459
- end: 2026-08-14T17:34:52.459
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['鳜鱼'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 7398
- attempt_count: 1
- response_hash: 938552e4ad637dbde12eb2cd07b861ab4717eff23a15d9f57fc54792af4921fc
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T17:34:52.473
- end: 2026-08-14T17:34:52.473
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 45e97a845eca82470999f7a950d563d21d600438c454ecaaba62d8b2e5f3d813
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T17:34:52.473
- end: 2026-08-14T17:34:52.473
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T17:34:52.473+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T17:34:52.476
- end: 2026-08-14T17:34:52.476
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T17:34:52.473+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:34:52.477
- end: 2026-08-14T17:34:52.477
- duration_ms: 0
- entity_id: 201002821
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:34:52.484
- end: 2026-08-14T17:34:52.484
- duration_ms: 0
- parent_id: 201002821
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1566
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
- duration_ms: 7815
- response_chars: 253
- response_hash: 9a54f94e8c79505a

## Final Output
- answer_chars: 253
- answer_hash: 9a54f94e8c79505a
- success: True

## Request Complete
- request_end: 2026-08-14T17:35:00.301
- request_duration_ms: 15242
- success: True
- final_source: generation

