# RAG Process

audit_id: 20260813_222228_960_85bc38ef
timestamp: 2026-08-13T22:22:28.960
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:22:28.960
- end: 2026-08-13T22:22:28.960
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 32

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:22:52.859
- end: 2026-08-13T22:22:52.859
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: PREFERENCE_RECOMMEND
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': ['FEW_STEPS', 'HOMESTYLE'], 'meal_context': [], 'tools': [], 'methods': ['STEW'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 24666
- attempt_count: 2
- response_hash: 59b2531ff30dce04bb8f402e9dac5defa3bcf7888461d27ff92de2b4fac882c6
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:22:52.860
- end: 2026-08-13T22:22:52.860
- duration_ms: 0
- compile_action: PREFERENCE_RECOMMEND
- reason: None
- query_plan_hash: 1451dc41102f87d4ceb7e67b5d8cf5836e3ba1a3d420a4e0e1a0ed1d036ffd78
- claim_policy: {'hard_constraints': [], 'soft_preferences': ['FEW_STEPS', 'HOMESTYLE', 'STEW'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / restricted_vector
- stage: restricted_vector
- status: selected
- start: 2026-08-13T22:22:53.183
- end: 2026-08-13T22:22:53.183
- duration_ms: 0
- parent_count: 5
- vector_scope: all_child_chunks
- expected_parent_type: Recipe
- filter_batch_count: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4614
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 0
- text_evidence_count: 5
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
- duration_ms: 14687
- response_chars: 660
- response_hash: ab857a59133fbeed

## Final Output
- answer_chars: 660
- answer_hash: ab857a59133fbeed
- success: True

## Request Complete
- request_end: 2026-08-13T22:23:07.871
- request_duration_ms: 38910
- success: True
- final_source: generation

