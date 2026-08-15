# RAG Process

audit_id: 20260813_221735_805_ef23552a
timestamp: 2026-08-13T22:17:35.806
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:17:35.806
- end: 2026-08-13T22:17:35.806
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 12

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:17:41.888
- end: 2026-08-13T22:17:41.888
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6081
- attempt_count: 1
- response_hash: 2636812a0df96b6d841d1b25353f9ef145b53cae7b835ff995996344549b6ce4
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:17:41.891
- end: 2026-08-13T22:17:41.891
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 03656bf57598d22620bfaadae1c85a537b0cbddc855d0c4d422df204fb809ee6
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:17:41.892
- end: 2026-08-13T22:17:41.892
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:17:41.892+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:17:41.894
- end: 2026-08-13T22:17:41.894
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:17:41.892+00:00
- result_count: 22

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:41.894
- end: 2026-08-13T22:17:41.894
- duration_ms: 0
- entity_id: 201002555
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:41.901
- end: 2026-08-13T22:17:41.901
- duration_ms: 0
- parent_id: 201002555
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:41.901
- end: 2026-08-13T22:17:41.901
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:41.908
- end: 2026-08-13T22:17:41.908
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:41.908
- end: 2026-08-13T22:17:41.908
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:41.914
- end: 2026-08-13T22:17:41.914
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:41.915
- end: 2026-08-13T22:17:41.915
- duration_ms: 0
- entity_id: 201004746
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:41.921
- end: 2026-08-13T22:17:41.921
- duration_ms: 0
- parent_id: 201004746
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:41.921
- end: 2026-08-13T22:17:41.921
- duration_ms: 0
- entity_id: 201005049
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:41.927
- end: 2026-08-13T22:17:41.927
- duration_ms: 0
- parent_id: 201005049
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:41.927
- end: 2026-08-13T22:17:41.927
- duration_ms: 0
- entity_id: 201005181
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:41.933
- end: 2026-08-13T22:17:41.933
- duration_ms: 0
- parent_id: 201005181
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:41.933
- end: 2026-08-13T22:17:41.933
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:41.939
- end: 2026-08-13T22:17:41.939
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:41.940
- end: 2026-08-13T22:17:41.940
- duration_ms: 0
- entity_id: 201005653
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:41.947
- end: 2026-08-13T22:17:41.947
- duration_ms: 0
- parent_id: 201005653
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:41.947
- end: 2026-08-13T22:17:41.947
- duration_ms: 0
- entity_id: 201005669
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:41.953
- end: 2026-08-13T22:17:41.953
- duration_ms: 0
- parent_id: 201005669
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 16590
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 9
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
- duration_ms: 14421
- response_chars: 524
- response_hash: e8a411dff0cfeb81

## Final Output
- answer_chars: 524
- answer_hash: e8a411dff0cfeb81
- success: True

## Request Complete
- request_end: 2026-08-13T22:17:56.376
- request_duration_ms: 20569
- success: True
- final_source: generation

