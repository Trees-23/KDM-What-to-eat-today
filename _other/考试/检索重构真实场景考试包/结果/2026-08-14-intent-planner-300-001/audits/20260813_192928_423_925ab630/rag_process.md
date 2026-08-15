# RAG Process

audit_id: 20260813_192928_423_925ab630
timestamp: 2026-08-13T19:29:28.424
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:29:28.424
- end: 2026-08-13T19:29:28.424
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:29:32.553
- end: 2026-08-13T19:29:32.553
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['鸭肉'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4129
- attempt_count: 1
- response_hash: 314b4dedcf616ef53dffc7158975f8f404be99a3e18ffe79107884b649258c28
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:29:32.557
- end: 2026-08-13T19:29:32.557
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: c534066c8ceb460432a421bb0f6c15a03bf73b8ad71728b3da55d4207103b675
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:29:32.557
- end: 2026-08-13T19:29:32.557
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:29:32.557+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:29:32.559
- end: 2026-08-13T19:29:32.559
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:29:32.557+00:00
- result_count: 2

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:29:32.559
- end: 2026-08-13T19:29:32.559
- duration_ms: 0
- entity_id: 201001428
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:29:32.566
- end: 2026-08-13T19:29:32.566
- duration_ms: 0
- parent_id: 201001428
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:29:32.567
- end: 2026-08-13T19:29:32.567
- duration_ms: 0
- entity_id: 201002327
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:29:32.573
- end: 2026-08-13T19:29:32.573
- duration_ms: 0
- parent_id: 201002327
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2831
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 2
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
- duration_ms: 12464
- response_chars: 534
- response_hash: 2d21e8080b4296f2

## Final Output
- answer_chars: 534
- answer_hash: 2d21e8080b4296f2
- success: True

## Request Complete
- request_end: 2026-08-13T19:29:45.038
- request_duration_ms: 16613
- success: True
- final_source: generation

