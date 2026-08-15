# RAG Process

audit_id: 20260811_183809_018_192a3e7c
timestamp: 2026-08-11T18:38:09.021
## Request
- original_query: 今天胃口一般，想吃清爽一点的川菜，有哪些做法比较贴近这种偏好？
- original_query_hash: 6716844045ad84fb
- session_id: 2026-08-12-真实考试-001:old:S07-B-10
- request_mode: stream
- request_start: 2026-08-11T18:38:09.022
- evaluation_sample_id: 20260811_183809_018_192a3e7c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:38:09.023
- end: 2026-08-11T18:38:09.023
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:38:09.023
- end: 2026-08-11T18:38:09.023
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 31
- enhanced_query_length: 31
- enhanced_query_hash: 6716844045ad84fb

## Event / nutrition_recommendation
- stage: nutrition_recommendation
- status: preference-retrieval-unavailable
- start: 2026-08-11T18:38:09.024
- end: 2026-08-11T18:38:09.024
- duration_ms: 0
- evidence_level: soft_preference
- policy_version: nutrition_soft_preference_v1
- source_status: missing_governed_nutrition_source
- missing_reason: 当前资料不能验证严格低脂；仅可作为少油/清爽偏好参考。
- claim_scope: 少油/清爽偏好
- text_evidence_count: 0
- limitations: ['NUTRITION_PREFERENCE_RETRIEVAL_UNAVAILABLE', '少油/清爽偏好检索未启用；不能用旧路径补造低脂推荐。']

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 348
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 0
- text_evidence_count: 0
- limitation_count: 2
- recommendation_evidence_level: soft_preference
- recommendation_policy_version: nutrition_soft_preference_v1

## Request Complete
- request_end: 2026-08-11T18:38:09.077
- request_duration_ms: 55
- success: True
- final_source: generation

