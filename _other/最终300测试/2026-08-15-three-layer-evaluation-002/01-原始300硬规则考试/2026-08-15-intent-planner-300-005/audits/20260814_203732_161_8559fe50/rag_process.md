# RAG Process

audit_id: 20260814_203732_161_8559fe50
timestamp: 2026-08-14T20:37:32.161
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:37:32.162
- end: 2026-08-14T20:37:32.162
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:37:36.137
- end: 2026-08-14T20:37:36.137
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['西红柿'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3975
- attempt_count: 1
- response_hash: 2fc92341c016210ba4f1c5d974177e72754718ed0d8993c5e8f42295d7398112
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:37:36.153
- end: 2026-08-14T20:37:36.153
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: dc18a1b1340818bc8ba14689731d3932a55ed07d2d3f03a8f230b38a6770e0ff
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:37:36.154
- end: 2026-08-14T20:37:36.154
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:37:36.154+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:37:36.157
- end: 2026-08-14T20:37:36.157
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:37:36.154+00:00
- result_count: 12

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:36.157
- end: 2026-08-14T20:37:36.157
- duration_ms: 0
- entity_id: 201002555
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:36.169
- end: 2026-08-14T20:37:36.169
- duration_ms: 0
- parent_id: 201002555
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:36.170
- end: 2026-08-14T20:37:36.170
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:36.177
- end: 2026-08-14T20:37:36.177
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:36.177
- end: 2026-08-14T20:37:36.177
- duration_ms: 0
- entity_id: 201003224
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:36.184
- end: 2026-08-14T20:37:36.184
- duration_ms: 0
- parent_id: 201003224
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:36.184
- end: 2026-08-14T20:37:36.184
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:36.191
- end: 2026-08-14T20:37:36.190
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:36.191
- end: 2026-08-14T20:37:36.191
- duration_ms: 0
- entity_id: 201003844
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:36.198
- end: 2026-08-14T20:37:36.198
- duration_ms: 0
- parent_id: 201003844
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:36.198
- end: 2026-08-14T20:37:36.198
- duration_ms: 0
- entity_id: 201004746
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:36.205
- end: 2026-08-14T20:37:36.205
- duration_ms: 0
- parent_id: 201004746
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:36.205
- end: 2026-08-14T20:37:36.205
- duration_ms: 0
- entity_id: 201005049
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:36.211
- end: 2026-08-14T20:37:36.211
- duration_ms: 0
- parent_id: 201005049
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:36.211
- end: 2026-08-14T20:37:36.211
- duration_ms: 0
- entity_id: 201005181
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:36.218
- end: 2026-08-14T20:37:36.218
- duration_ms: 0
- parent_id: 201005181
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:36.218
- end: 2026-08-14T20:37:36.218
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:36.224
- end: 2026-08-14T20:37:36.224
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:36.224
- end: 2026-08-14T20:37:36.224
- duration_ms: 0
- entity_id: 201005528
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:36.231
- end: 2026-08-14T20:37:36.231
- duration_ms: 0
- parent_id: 201005528
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:36.231
- end: 2026-08-14T20:37:36.231
- duration_ms: 0
- entity_id: 201005653
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:36.237
- end: 2026-08-14T20:37:36.237
- duration_ms: 0
- parent_id: 201005653
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:36.237
- end: 2026-08-14T20:37:36.237
- duration_ms: 0
- entity_id: 201005669
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:36.242
- end: 2026-08-14T20:37:36.242
- duration_ms: 0
- parent_id: 201005669
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 14852
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 12
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
- duration_ms: 16523
- response_chars: 786
- response_hash: 64b451e25dc1c4b9

## Final Output
- answer_chars: 786
- answer_hash: 64b451e25dc1c4b9
- success: True

## Request Complete
- request_end: 2026-08-14T20:37:52.767
- request_duration_ms: 20605
- success: True
- final_source: generation

