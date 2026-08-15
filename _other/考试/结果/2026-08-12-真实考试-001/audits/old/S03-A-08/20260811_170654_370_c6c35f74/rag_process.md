# RAG Process

audit_id: 20260811_170654_370_c6c35f74
timestamp: 2026-08-11T17:06:54.371
## Request
- original_query: 请说明“炒/煎”这个技巧的关键要点和适用情形。
- original_query_hash: 3dbc73b5e1408d96
- session_id: 2026-08-12-真实考试-001:old:S03-A-08
- request_mode: stream
- request_start: 2026-08-11T17:06:54.372
- evaluation_sample_id: 20260811_170654_370_c6c35f74
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:06:54.374
- end: 2026-08-11T17:06:54.374
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:06:54.374
- end: 2026-08-11T17:06:54.374
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: 3dbc73b5e1408d96

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:06:54.375
- end: 2026-08-11T17:06:54.375
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: 3dbc73b5e1408d96
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:06:54.375
- end: 2026-08-11T17:07:00.726
- duration_ms: 6350
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.38
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询聚焦于“炒/煎”这一烹饪技巧，要求说明其关键要点与适用情形，属于对单一技能主题的定义、操作要领及条件匹配的中等复杂度信息检索。查询隐含“技巧—关键要点”和“技巧—适用食材/场景”两类关系，但不涉及多个实体构成的复杂关系网络。通常不需要多跳推理或复杂因果分析；可进行轻量对比以区分炒与煎的火候、用油量和适用食材，但不是核心推理要求。适合通过关键词检索、向量语义检索及结果重排序获取烹饪技法资料，因此推荐hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 67, 'graph_rag_count': 0, 'total_queries': 67}
- route_stats_after: {'traditional_count': 68, 'graph_rag_count': 0, 'total_queries': 68}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['炒', '煎', '炒制', '煎制']
- topic_keywords: ['烹饪技巧', '火候', '油温', '受热均匀', '调味', '快手菜', '食材适用性']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7816

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '火候', '油温', '受热均匀', '调味', '快手菜', '食材适用性']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 68

## Hybrid Branch Status / entity_level
- keywords: ['炒', '煎', '炒制', '煎制']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 295

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 601

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 24
- duplicate_count: 6

## Hybrid Technique Expansion
- enabled: True
- seed_count: 10
- expanded_count: 9
- doc_names: ['糖色的炒制', '炒/煎']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 25
- duration_ms: 28643
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 1, 'TechniqueDoc': 2, '高级技巧': 1, 'TechniqueChunk': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 37104
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:06:54.375
- end: 2026-08-11T17:07:37.831
- duration_ms: 43456
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 8858
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
- chunk_count: 1121
- redacted_field: 4408
- total_duration_ms: 25416
- fallback_used: False

## Final Output
- answer_chars: 1421
- answer_hash: 6f48dde74ec6a5aa
- success: True

## Request Complete
- request_end: 2026-08-11T17:08:03.277
- request_duration_ms: 68905
- success: True
- final_source: generation

