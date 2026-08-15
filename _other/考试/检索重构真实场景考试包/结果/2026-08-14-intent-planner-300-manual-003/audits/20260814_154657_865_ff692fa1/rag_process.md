# RAG Process

audit_id: 20260814_154657_865_ff692fa1
timestamp: 2026-08-14T15:46:57.866
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:46:57.866
- end: 2026-08-14T15:46:57.866
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:47:02.102
- end: 2026-08-14T15:47:02.102
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.93
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4236
- attempt_count: 1
- response_hash: 55c3570eaa5a8b2ca1f11a4a501e00f8e7729b3582946595b8a23af782d4b9e3
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:47:02.127
- end: 2026-08-14T15:47:02.127
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: b07333cb1e91b6ef17a60fe2cd31ca1faf0e86913fff012701bb015ccf98226b
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:47:02.127
- end: 2026-08-14T15:47:02.127
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:47:02.127+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:47:02.129
- end: 2026-08-14T15:47:02.129
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:47:02.127+00:00
- result_count: 2

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:47:02.129
- end: 2026-08-14T15:47:02.129
- duration_ms: 0
- entity_id: 201003959
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:47:02.136
- end: 2026-08-14T15:47:02.136
- duration_ms: 0
- parent_id: 201003959
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2038
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
- duration_ms: 12537
- response_chars: 187
- response_hash: 80464140e5030bf0

## Final Output
- answer_chars: 187
- answer_hash: 80464140e5030bf0
- success: True

## Request Complete
- request_end: 2026-08-14T15:47:14.675
- request_duration_ms: 16809
- success: True
- final_source: generation

