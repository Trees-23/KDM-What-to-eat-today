# RAG Process

audit_id: 20260811_172440_654_82207b95
timestamp: 2026-08-11T17:24:40.654
## Request
- original_query: 只根据“蒸（米）/炖（使用电饭煲/高压锅/电压力锅）”技巧章节的关键要点回答；资料没有说明的结论请明确保留。
- original_query_hash: 8f6bdbd9f8512879
- session_id: 2026-08-12-真实考试-001:old:S03-C-07
- request_mode: stream
- request_start: 2026-08-11T17:24:40.654
- evaluation_sample_id: 20260811_172440_654_82207b95
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:24:40.655
- end: 2026-08-11T17:24:40.655
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:24:40.655
- end: 2026-08-11T17:24:40.655
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 54
- enhanced_query_length: 54
- enhanced_query_hash: 8f6bdbd9f8512879

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:24:40.656
- end: 2026-08-11T17:24:40.656
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 54
- analysis_input_query_hash: 8f6bdbd9f8512879
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:24:40.656
- end: 2026-08-11T17:24:47.443
- duration_ms: 6786
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.3
- reasoning_required: False
- entity_count: 5
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询的核心是限定证据范围：仅检索并依据“蒸（米）/炖（使用电饭煲/高压锅/电压力锅）”技巧章节作答，同时要求对资料未覆盖的内容明确保留。它不包含待解答的具体事实问题，也不要求多跳推理、因果分析或实体间对比；主要需要章节定位、关键词匹配、段落级证据抽取与缺失信息判定。明确实体包括蒸（米）、炖、电饭煲、高压锅、电压力锅，实体间主要是“炖”与不同烹饪设备的适用关系，关系网络较简单，因此适合使用hybrid_traditional进行精确章节过滤和语义检索。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 85, 'graph_rag_count': 1, 'total_queries': 86}
- route_stats_after: {'traditional_count': 86, 'graph_rag_count': 1, 'total_queries': 87}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['蒸（米）', '炖', '电饭煲', '高压锅', '电压力锅']
- topic_keywords: ['烹饪技巧', '蒸米', '炖煮', '资料依据', '信息保留']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4315

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '蒸米', '炖煮', '资料依据', '信息保留']
- requested_k: 10
- actual_count: 4
- fallback_count: 4
- duration_ms: 18

## Hybrid Branch Status / entity_level
- keywords: ['蒸（米）', '炖', '电饭煲', '高压锅', '电压力锅']
- requested_k: 10
- actual_count: 10
- fallback_count: 4
- duration_ms: 42

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 712

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 4
- vector_count: 10
- origin_len: 24

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 24
- after_count: 16
- duplicate_count: 8

## Hybrid Technique Expansion
- enabled: True
- seed_count: 8
- expanded_count: 9
- doc_names: ['蒸（米）/炖（使用电饭煲/高压锅/电压力锅）', '蒸']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 17
- duration_ms: 20281
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 2, 'TechniqueChunk': 2, 'TechniqueDoc': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25342
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:24:40.656
- end: 2026-08-11T17:25:12.786
- duration_ms: 32130
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4590
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
- chunk_count: 73
- redacted_field: 5530
- total_duration_ms: 6680
- fallback_used: False

## Final Output
- answer_chars: 93
- answer_hash: 20819f51eacd03fa
- success: True

## Request Complete
- request_end: 2026-08-11T17:25:19.520
- request_duration_ms: 38865
- success: True
- final_source: generation

