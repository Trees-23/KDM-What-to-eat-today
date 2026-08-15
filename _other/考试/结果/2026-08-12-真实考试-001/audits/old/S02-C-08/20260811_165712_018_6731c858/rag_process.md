# RAG Process

audit_id: 20260811_165712_018_6731c858
timestamp: 2026-08-11T16:57:12.021
## Request
- original_query: 只回答罗宋汤的第 1 步，并说明它来自哪一条菜谱步骤；不要混入后续步骤。
- original_query_hash: 22b456e8e302eecf
- session_id: 2026-08-12-真实考试-001:old:S02-C-08
- request_mode: stream
- request_start: 2026-08-11T16:57:12.021
- evaluation_sample_id: 20260811_165712_018_6731c858
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:57:12.022
- end: 2026-08-11T16:57:12.022
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:57:12.022
- end: 2026-08-11T16:57:12.022
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 22b456e8e302eecf

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:57:12.023
- end: 2026-08-11T16:57:12.023
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 22b456e8e302eecf
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:57:12.023
- end: 2026-08-11T16:57:20.230
- duration_ms: 8206
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.32
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 查询核心是定位“罗宋汤”菜谱中的“第1步”，并严格按步骤边界输出，同时标注该内容来自第几条菜谱步骤。它不需要多跳推理、因果分析或对比分析，但需要执行步骤编号匹配、结果截断与后续步骤排除等约束校验。明确实体包括菜品“罗宋汤”和步骤实体“第1步”。适合使用 hybrid_traditional，通过关键词/字段检索定位对应菜谱及其首条步骤，再进行结构化过滤和精确输出。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 57, 'graph_rag_count': 0, 'total_queries': 57}
- route_stats_after: {'traditional_count': 58, 'graph_rag_count': 0, 'total_queries': 58}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['罗宋汤']
- topic_keywords: ['菜谱步骤', '步骤顺序', '步骤溯源', '烹饪指令约束']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 9738

## Hybrid Branch Status / topic_level
- keywords: ['菜谱步骤', '步骤顺序', '步骤溯源', '烹饪指令约束']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 8

## Hybrid Branch Status / entity_level
- keywords: ['罗宋汤']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 10

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 263

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 0
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 9
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['炒/煎', '做菜专业术语']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 10
- duration_ms: 17619
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'汤类': 2, '主食': 1, '荤菜': 1, '高级技巧': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 陈皮排骨汤
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 27639
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:57:12.023
- end: 2026-08-11T16:57:47.870
- duration_ms: 35847
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 9227
- retrieval_levels: ['', 'context_expansion']
- search_types: ['technique_expansion', 'vector_enhanced']
- stream: True
- max_retries: 3
- evidence_bundle: False
- verified_graph_fact_count: 0
- text_evidence_count: 0
- limitation_count: 0
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Generation Config
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: True
- timeout: 60
- max_retries: 3

## Generation Stream
- status: success
- chunk_count: 74
- redacted_field: 2498
- total_duration_ms: 4054
- fallback_used: False

## Final Output
- answer_chars: 99
- answer_hash: c748612f667d83f0
- success: True

## Request Complete
- request_end: 2026-08-11T16:57:51.968
- request_duration_ms: 39946
- success: True
- final_source: generation

