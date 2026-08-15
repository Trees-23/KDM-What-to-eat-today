# RAG Process

audit_id: 20260814_154714_675_89dff539
timestamp: 2026-08-14T15:47:14.676
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:47:14.676
- end: 2026-08-14T15:47:14.676
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:47:19.697
- end: 2026-08-14T15:47:19.697
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['鸭肉'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5020
- attempt_count: 1
- response_hash: f4bcfbc06d12078600f5b65eb333ec2242e0a1d12c91ede6ffc9617f460229b9
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:47:19.749
- end: 2026-08-14T15:47:19.749
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: c7f5c8ce174552bdcbaa7c555b482b92f4c96d4e52a49f61c050f084b9b50d96
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:47:19.750
- end: 2026-08-14T15:47:19.750
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:47:19.750+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:47:19.755
- end: 2026-08-14T15:47:19.755
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:47:19.750+00:00
- result_count: 6

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:47:19.756
- end: 2026-08-14T15:47:19.756
- duration_ms: 0
- entity_id: 201001428
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:47:19.767
- end: 2026-08-14T15:47:19.767
- duration_ms: 0
- parent_id: 201001428
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:47:19.768
- end: 2026-08-14T15:47:19.768
- duration_ms: 0
- entity_id: 201002327
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:47:19.777
- end: 2026-08-14T15:47:19.777
- duration_ms: 0
- parent_id: 201002327
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4273
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
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 9086
- response_chars: 222
- response_hash: 43d7e612ff243341

## Final Output
- answer_chars: 222
- answer_hash: 43d7e612ff243341
- success: True

## Request Complete
- request_end: 2026-08-14T15:47:28.866
- request_duration_ms: 14189
- success: True
- final_source: generation

