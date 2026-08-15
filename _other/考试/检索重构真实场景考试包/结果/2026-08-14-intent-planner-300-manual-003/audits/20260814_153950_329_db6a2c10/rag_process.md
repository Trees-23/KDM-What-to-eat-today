# RAG Process

audit_id: 20260814_153950_329_db6a2c10
timestamp: 2026-08-14T15:39:50.329
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:39:50.329
- end: 2026-08-14T15:39:50.329
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:40:06.816
- end: 2026-08-14T15:40:06.816
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['鲈鱼'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 16487
- attempt_count: 1
- response_hash: ed0b98f658c981abda229ea5b4682ccc1ff5d9e3adee4895660e30d6bc40b0cb
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:40:06.833
- end: 2026-08-14T15:40:06.833
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 17fe136647461470fc143c3f8c558a7986e47691be3fe9f9611c76f568471411
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:40:06.834
- end: 2026-08-14T15:40:06.834
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T15:40:06.834+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:40:06.836
- end: 2026-08-14T15:40:06.836
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T15:40:06.834+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:40:06.836
- end: 2026-08-14T15:40:06.836
- duration_ms: 0
- entity_id: 201000257
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:40:06.843
- end: 2026-08-14T15:40:06.843
- duration_ms: 0
- parent_id: 201000257
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1654
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
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 11711
- response_chars: 371
- response_hash: 01e8ce721b1f1f2e

## Final Output
- answer_chars: 371
- answer_hash: 01e8ce721b1f1f2e
- success: True

## Request Complete
- request_end: 2026-08-14T15:40:18.556
- request_duration_ms: 28226
- success: True
- final_source: generation

