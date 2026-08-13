# RAG Process

audit_id: 20260813_222646_103_d97eb053
timestamp: 2026-08-13T22:26:46.103
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:26:46.104
- end: 2026-08-13T22:26:46.104
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 28

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:26:50.275
- end: 2026-08-13T22:26:50.275
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: PREFERENCE_RECOMMEND
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': ['LUNCH'], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4172
- attempt_count: 1
- response_hash: 72434f3caed2b2e5518029667636ab5e3bc90dd04e5536df71ea1846be40fe7a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:26:50.276
- end: 2026-08-13T22:26:50.276
- duration_ms: 0
- compile_action: PREFERENCE_RECOMMEND
- reason: None
- query_plan_hash: 1451dc41102f87d4ceb7e67b5d8cf5836e3ba1a3d420a4e0e1a0ed1d036ffd78
- claim_policy: {'hard_constraints': [], 'soft_preferences': ['LUNCH'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / restricted_vector
- stage: restricted_vector
- status: selected
- start: 2026-08-13T22:26:50.621
- end: 2026-08-13T22:26:50.621
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
- context_chars: 5051
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
- duration_ms: 17074
- response_chars: 875
- response_hash: de8c2c4a33392cd5

## Final Output
- answer_chars: 875
- answer_hash: de8c2c4a33392cd5
- success: True

## Request Complete
- request_end: 2026-08-13T22:27:07.696
- request_duration_ms: 21592
- success: True
- final_source: generation

