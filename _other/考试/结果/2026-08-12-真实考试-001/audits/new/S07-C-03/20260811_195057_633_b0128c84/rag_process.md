# RAG Process

audit_id: 20260811_195057_633_b0128c84
timestamp: 2026-08-11T19:50:57.634
## Request
- original_query: 希望推荐不太油的川味早餐做法。可以表达偏好匹配，但没有受治理营养来源时不要断言“低脂”或其他严格营养事实。
- original_query_hash: fe24f389a7e23c7c
- session_id: 2026-08-12-真实考试-001:new:S07-C-03
- request_mode: stream
- request_start: 2026-08-11T19:50:57.634
- evaluation_sample_id: 20260811_195057_633_b0128c84
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:50:57.635
- end: 2026-08-11T19:50:57.635
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:50:57.635
- end: 2026-08-11T19:50:57.635
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 53
- enhanced_query_length: 53
- enhanced_query_hash: fe24f389a7e23c7c

## Event / nutrition_recommendation
- stage: nutrition_recommendation
- status: evidence-insufficient
- start: 2026-08-11T19:50:57.635
- end: 2026-08-11T19:50:57.635
- duration_ms: 0
- evidence_level: evidence_insufficient
- policy_version: nutrition_soft_preference_v1
- source_status: missing_governed_nutrition_source
- missing_reason: 当前没有可信营养数值或治理标签，不能验证严格低脂、脂肪克数或医疗饮食条件。
- claim_scope: 不得给出满足营养约束的候选
- text_evidence_count: 0
- limitations: ['NUTRITION_EVIDENCE_INSUFFICIENT', '当前没有可信营养数值或治理标签，不能验证严格低脂、脂肪克数或医疗饮食条件。']

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 370
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 0
- text_evidence_count: 0
- limitation_count: 2
- recommendation_evidence_level: evidence_insufficient
- recommendation_policy_version: nutrition_soft_preference_v1

## Request Complete
- request_end: 2026-08-11T19:50:57.650
- request_duration_ms: 16
- success: True
- final_source: generation

