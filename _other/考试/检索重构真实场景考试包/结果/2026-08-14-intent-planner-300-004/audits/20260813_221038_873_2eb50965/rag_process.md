# RAG Process

audit_id: 20260813_221038_873_2eb50965
timestamp: 2026-08-13T22:10:38.873
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:10:38.874
- end: 2026-08-13T22:10:38.874
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:10:42.532
- end: 2026-08-13T22:10:42.532
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3658
- attempt_count: 1
- response_hash: 1c3413d3f91132ec504a56577dc767bff2e8bdab676aba16c1102beeb4d910d8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:10:42.538
- end: 2026-08-13T22:10:42.538
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: d65d39911bb7e5ed6e7b5ed509d24bc21fe5ec5b581f03e378fea8f209d33b5e
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:10:42.538
- end: 2026-08-13T22:10:42.538
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:10:42.538+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:10:42.542
- end: 2026-08-13T22:10:42.542
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:10:42.538+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:10:42.543
- end: 2026-08-13T22:10:42.543
- duration_ms: 0
- entity_id: 201004678
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:10:42.558
- end: 2026-08-13T22:10:42.558
- duration_ms: 0
- parent_id: 201004678
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1295
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
- duration_ms: 8758
- response_chars: 209
- response_hash: d69c13fdf857a74a

## Final Output
- answer_chars: 209
- answer_hash: d69c13fdf857a74a
- success: True

## Request Complete
- request_end: 2026-08-13T22:10:51.318
- request_duration_ms: 12444
- success: True
- final_source: generation

