# RAG Process

audit_id: 20260811_174755_494_2f2b1c0e
timestamp: 2026-08-11T17:47:55.496
## Request
- original_query: 土豆适合搭配什么蔬菜？
- original_query_hash: 351698b6c7e5e376
- session_id: 2026-08-12-真实考试-001:old:S05-A-05
- request_mode: stream
- request_start: 2026-08-11T17:47:55.496
- evaluation_sample_id: 20260811_174755_494_2f2b1c0e
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:47:55.497
- end: 2026-08-11T17:47:55.497
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:47:55.498
- end: 2026-08-11T17:47:55.498
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 11
- enhanced_query_length: 11
- enhanced_query_hash: 351698b6c7e5e376

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:47:55.499
- end: 2026-08-11T17:47:55.499
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 11
- analysis_input_query_hash: 351698b6c7e5e376
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:47:55.499
- end: 2026-08-11T17:48:01.606
- duration_ms: 6107
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.5
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 查询核心是“土豆”与“蔬菜”这一泛化类别之间的搭配关系，目标是获取适合共同烹饪或食用的蔬菜列表。该问题不需要多跳推理、因果分析或复杂知识图谱关系发现，仅需通过关键词检索、语义召回和结果排序即可获得高质量答案；可在结果生成阶段进行简单的搭配维度归纳，如口感、烹饪方式和营养互补。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 113, 'graph_rag_count': 11, 'total_queries': 124}
- route_stats_after: {'traditional_count': 114, 'graph_rag_count': 11, 'total_queries': 125}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['土豆', '胡萝卜', '洋葱', '青椒', '西红柿', '茄子', '西兰花', '芹菜', '四季豆', '白菜']
- topic_keywords: ['蔬菜搭配', '营养搭配', '家常菜', '素食']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4255

## Hybrid Branch Status / topic_level
- keywords: ['蔬菜搭配', '营养搭配', '家常菜', '素食']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 26

## Hybrid Branch Status / entity_level
- keywords: ['土豆', '胡萝卜', '洋葱', '青椒', '西红柿', '茄子', '西兰花', '芹菜', '四季豆', '白菜']
- requested_k: 10
- actual_count: 9
- fallback_count: 0
- duration_ms: 69

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 474

## Hybrid Branch Summary
- entity_count: 9
- topic_count: 2
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 20
- duplicate_count: 1

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
- candidate_count: 21
- duration_ms: 15019
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 1, '素菜': 2, 'Ingredient': 1, '烹饪技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 19765
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:47:55.499
- end: 2026-08-11T17:48:21.373
- duration_ms: 25873
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2623
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
- chunk_count: 244
- redacted_field: 3728
- total_duration_ms: 8624
- fallback_used: False

## Final Output
- answer_chars: 297
- answer_hash: ae3016af07c4255d
- success: True

## Request Complete
- request_end: 2026-08-11T17:48:30.015
- request_duration_ms: 34519
- success: True
- final_source: generation

