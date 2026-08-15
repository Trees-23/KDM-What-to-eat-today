# RAG Process

audit_id: 20260811_195057_766_aa3f99f7
timestamp: 2026-08-11T19:50:57.767
## Request
- original_query: 想吃不太刺激的川味面食。可以表达偏好匹配，但没有受治理营养来源时不要断言“低脂”或其他严格营养事实。
- original_query_hash: e099bb463a233972
- session_id: 2026-08-12-真实考试-001:new:S07-C-08
- request_mode: stream
- request_start: 2026-08-11T19:50:57.767
- evaluation_sample_id: 20260811_195057_766_aa3f99f7
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:50:57.767
- end: 2026-08-11T19:50:57.767
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:50:57.768
- end: 2026-08-11T19:50:57.768
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 50
- enhanced_query_length: 50
- enhanced_query_hash: e099bb463a233972

## Event / nutrition_recommendation
- stage: nutrition_recommendation
- status: evidence-insufficient
- start: 2026-08-11T19:50:57.768
- end: 2026-08-11T19:50:57.768
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
- request_end: 2026-08-11T19:50:57.784
- request_duration_ms: 16
- success: True
- final_source: generation

