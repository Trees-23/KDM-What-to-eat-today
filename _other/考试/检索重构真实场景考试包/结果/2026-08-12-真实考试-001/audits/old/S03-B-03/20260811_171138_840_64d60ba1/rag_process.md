# RAG Process

audit_id: 20260811_171138_840_64d60ba1
timestamp: 2026-08-11T17:11:38.845
## Request
- original_query: 我想学去腥，它的关键要点和适用场景是什么？
- original_query_hash: a7378789a52ecf37
- session_id: 2026-08-12-真实考试-001:old:S03-B-03
- request_mode: stream
- request_start: 2026-08-11T17:11:38.845
- evaluation_sample_id: 20260811_171138_840_64d60ba1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:11:38.847
- end: 2026-08-11T17:11:38.847
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:11:38.847
- end: 2026-08-11T17:11:38.847
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: a7378789a52ecf37

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:11:38.848
- end: 2026-08-11T17:11:38.848
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: a7378789a52ecf37
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:11:38.848
- end: 2026-08-11T17:11:46.110
- duration_ms: 7262
- analysis_mode: llm
- query_complexity: 0.52
- relationship_intensity: 0.42
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 查询核心实体为“去腥”，属于烹饪处理技巧。用户同时关注其关键要点与适用场景，需要将去腥方法、食材类型、操作阶段和效果进行基础关联与归纳。该问题需要轻度因果分析（不同腥味来源对应不同处理方式），但通常不需要多跳推理或复杂知识图谱关系发现；通过关键词检索、菜谱/烹饪知识库召回及结果重排序即可有效回答，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 72, 'graph_rag_count': 0, 'total_queries': 72}
- route_stats_after: {'traditional_count': 73, 'graph_rag_count': 0, 'total_queries': 73}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['去腥', '焯水', '腌制', '料酒', '姜', '葱', '花椒']
- topic_keywords: ['烹饪技巧', '去腥', '食材处理', '调味', '水产', '肉类', '内脏']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7618

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '去腥', '食材处理', '调味', '水产', '肉类', '内脏']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 69

## Hybrid Branch Status / entity_level
- keywords: ['去腥', '焯水', '腌制', '料酒', '姜', '葱', '花椒']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 378

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 477

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 21
- duplicate_count: 9

## Hybrid Technique Expansion
- enabled: True
- seed_count: 11
- expanded_count: 9
- doc_names: ['去腥', '焯水']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 22
- duration_ms: 20718
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 2, 'TechniqueDoc': 1, 'TechniqueChunk': 2}
- deferred_count: 6
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 28853
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:11:38.848
- end: 2026-08-11T17:12:14.965
- duration_ms: 36117
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 6145
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
- chunk_count: 1126
- redacted_field: 5496
- total_duration_ms: 48238
- fallback_used: False

## Final Output
- answer_chars: 1406
- answer_hash: 8455008788f134dc
- success: True

## Request Complete
- request_end: 2026-08-11T17:13:03.238
- request_duration_ms: 84392
- success: True
- final_source: generation

