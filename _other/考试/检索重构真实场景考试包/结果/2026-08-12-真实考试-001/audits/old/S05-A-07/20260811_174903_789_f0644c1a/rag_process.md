# RAG Process

audit_id: 20260811_174903_789_f0644c1a
timestamp: 2026-08-11T17:49:03.791
## Request
- original_query: 西红柿适合搭配什么蔬菜？
- original_query_hash: b1be995741a4f695
- session_id: 2026-08-12-真实考试-001:old:S05-A-07
- request_mode: stream
- request_start: 2026-08-11T17:49:03.791
- evaluation_sample_id: 20260811_174903_789_f0644c1a
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:49:03.792
- end: 2026-08-11T17:49:03.792
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:49:03.793
- end: 2026-08-11T17:49:03.793
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 12
- enhanced_query_length: 12
- enhanced_query_hash: b1be995741a4f695

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:49:03.794
- end: 2026-08-11T17:49:03.794
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 12
- analysis_input_query_hash: b1be995741a4f695
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:49:03.794
- end: 2026-08-11T17:49:15.744
- duration_ms: 11950
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.5
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 查询核心是识别“西红柿”与“蔬菜”这一类实体之间的搭配关系，属于常见的单跳关联信息检索。无需多跳推理，也不要求因果分析；可在结果生成阶段按口感、烹饪方式或营养互补进行轻量对比。明确实体包括“西红柿”（具体蔬菜/食材）和“蔬菜”（食材类别）。适合通过关键词、菜谱语料和向量语义召回相结合的 hybrid_traditional 策略获取答案。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 115, 'graph_rag_count': 11, 'total_queries': 126}
- route_stats_after: {'traditional_count': 116, 'graph_rag_count': 11, 'total_queries': 127}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['西红柿', '鸡蛋', '土豆', '茄子', '黄瓜', '西兰花', '菜花', '菠菜', '豆腐', '洋葱', '青椒']
- topic_keywords: ['蔬菜搭配', '家常菜', '营养搭配', '素食', '清爽', '酸甜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5276

## Hybrid Branch Status / topic_level
- keywords: ['蔬菜搭配', '家常菜', '营养搭配', '素食', '清爽', '酸甜']
- requested_k: 10
- actual_count: 3
- fallback_count: 3
- duration_ms: 37

## Hybrid Branch Status / entity_level
- keywords: ['西红柿', '鸡蛋', '土豆', '茄子', '黄瓜', '西兰花', '菜花', '菠菜', '豆腐', '洋葱', '青椒']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 53

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 593

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 3
- vector_count: 10
- origin_len: 23

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 23
- after_count: 19
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 3
- doc_names: ['揭秘食材搭配的智慧：这些食物不宜同食']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 20
- duration_ms: 13739
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 1, 'Ingredient': 1, '素菜': 1, '通用知识': 1, '烹饪技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 19626
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:49:03.794
- end: 2026-08-11T17:49:35.371
- duration_ms: 31577
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4683
- retrieval_levels: ['', 'context_expansion', 'entity']
- search_types: ['entity_level', 'technique_expansion', 'vector_enhanced']
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
- chunk_count: 237
- redacted_field: 2687
- total_duration_ms: 7524
- fallback_used: False

## Final Output
- answer_chars: 299
- answer_hash: 4a5d929f3c63cf4e
- success: True

## Request Complete
- request_end: 2026-08-11T17:49:42.905
- request_duration_ms: 39114
- success: True
- final_source: generation

