# RAG Process

audit_id: 20260814_204159_973_beeebbe5
timestamp: 2026-08-14T20:41:59.974
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:41:59.974
- end: 2026-08-14T20:41:59.974
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 37

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:42:04.056
- end: 2026-08-14T20:42:04.056
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['金针菇'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4081
- attempt_count: 1
- response_hash: 77de225a5a1f9c494f35e884f998279327cbac217e167b9476f020a78d59abf2
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:42:04.065
- end: 2026-08-14T20:42:04.065
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 11f888249c3807bb3a2eaeafff5f41bcbab3ac3d19c4799bcfef69694be8d1a2
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:42:04.065
- end: 2026-08-14T20:42:04.065
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:42:04.065+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:42:04.068
- end: 2026-08-14T20:42:04.068
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:42:04.065+00:00
- result_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:42:04.068
- end: 2026-08-14T20:42:04.068
- duration_ms: 0
- entity_id: 201003862
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:42:04.081
- end: 2026-08-14T20:42:04.081
- duration_ms: 0
- parent_id: 201003862
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:42:04.081
- end: 2026-08-14T20:42:04.081
- duration_ms: 0
- entity_id: 201004863
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:42:04.094
- end: 2026-08-14T20:42:04.094
- duration_ms: 0
- parent_id: 201004863
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:42:04.094
- end: 2026-08-14T20:42:04.094
- duration_ms: 0
- entity_id: 201005212
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:42:04.105
- end: 2026-08-14T20:42:04.105
- duration_ms: 0
- parent_id: 201005212
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:42:04.105
- end: 2026-08-14T20:42:04.105
- duration_ms: 0
- entity_id: 201005289
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:42:04.111
- end: 2026-08-14T20:42:04.111
- duration_ms: 0
- parent_id: 201005289
- build_id: pds_51e5e228cb4a935de64e2b7a
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
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 6356
- response_chars: 154
- response_hash: 08a44b5334797865

## Final Output
- answer_chars: 154
- answer_hash: 08a44b5334797865
- success: True

## Request Complete
- request_end: 2026-08-14T20:42:10.468
- request_duration_ms: 10493
- success: True
- final_source: generation

