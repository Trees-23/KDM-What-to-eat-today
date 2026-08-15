# RAG Process

audit_id: 20260811_182302_957_021eb2c1
timestamp: 2026-08-11T18:23:02.959
## Request
- original_query: 想吃川菜但口感清爽。请推荐几个可考虑的菜。
- original_query_hash: 821badeb7b47a5d5
- session_id: 2026-08-12-真实考试-001:old:S07-A-01
- request_mode: stream
- request_start: 2026-08-11T18:23:02.959
- evaluation_sample_id: 20260811_182302_957_021eb2c1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:23:02.960
- end: 2026-08-11T18:23:02.960
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:23:02.960
- end: 2026-08-11T18:23:02.960
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 821badeb7b47a5d5

## Event / nutrition_recommendation
- stage: nutrition_recommendation
- status: preference-retrieval-unavailable
- start: 2026-08-11T18:23:02.966
- end: 2026-08-11T18:23:02.966
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
- request_end: 2026-08-11T18:23:02.983
- request_duration_ms: 23
- success: True
- final_source: generation

