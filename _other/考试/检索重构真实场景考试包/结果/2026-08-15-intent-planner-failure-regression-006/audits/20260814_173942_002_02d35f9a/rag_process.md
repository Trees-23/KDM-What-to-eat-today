# RAG Process

audit_id: 20260814_173942_002_02d35f9a
timestamp: 2026-08-14T17:39:42.003
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T17:39:42.003
- end: 2026-08-14T17:39:42.003
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T17:39:46.607
- end: 2026-08-14T17:39:46.607
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['南瓜'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6122
- attempt_count: 1
- response_hash: 0151bb7229460777fd360a8f187901e3b630877ee179e87c7723684c2985cad1
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T17:39:46.630
- end: 2026-08-14T17:39:46.630
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: ae4d9ca251149a902687bbebd9ef0155d50473f044ba014041daf05261f17fd9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T17:39:46.630
- end: 2026-08-14T17:39:46.630
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T17:39:46.630+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T17:39:46.634
- end: 2026-08-14T17:39:46.634
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T17:39:46.630+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:39:46.635
- end: 2026-08-14T17:39:46.635
- duration_ms: 0
- entity_id: 201004991
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:39:46.648
- end: 2026-08-14T17:39:46.648
- duration_ms: 0
- parent_id: 201004991
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1414
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
- duration_ms: 12127
- response_chars: 89
- response_hash: 67345782d9afcd69

## Final Output
- answer_chars: 89
- answer_hash: 67345782d9afcd69
- success: True

## Request Complete
- request_end: 2026-08-14T17:39:58.778
- request_duration_ms: 16774
- success: True
- final_source: generation

