# RAG Process

audit_id: 20260811_172228_733_890eae1d
timestamp: 2026-08-11T17:22:28.734
## Request
- original_query: 只根据“蒸”技巧章节的关键要点回答；资料没有说明的结论请明确保留。
- original_query_hash: fc9b23009dffb59f
- session_id: 2026-08-12-真实考试-001:old:S03-C-04
- request_mode: stream
- request_start: 2026-08-11T17:22:28.734
- evaluation_sample_id: 20260811_172228_733_890eae1d
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:22:28.735
- end: 2026-08-11T17:22:28.735
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:22:28.736
- end: 2026-08-11T17:22:28.736
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 33
- enhanced_query_length: 33
- enhanced_query_hash: fc9b23009dffb59f

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:22:28.737
- end: 2026-08-11T17:22:28.737
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 33
- analysis_input_query_hash: fc9b23009dffb59f
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:22:28.737
- end: 2026-08-11T17:22:36.211
- duration_ms: 7474
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.2
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询本质上是对回答范围与证据边界的约束，而非要求分析多个实体之间的关系。明确实体主要为“蒸”技巧章节和“关键要点”。系统需要完成章节级定向检索、关键点抽取，并进行基于资料覆盖范围的保守性判断：资料未明确说明的内容必须拒绝推断或明确保留。无需多跳推理、因果分析或对比分析，适合采用hybrid_traditional进行关键词/章节定位与语义检索，并结合证据校验生成答案。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 82, 'graph_rag_count': 1, 'total_queries': 83}
- route_stats_after: {'traditional_count': 83, 'graph_rag_count': 1, 'total_queries': 84}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['蒸', '“蒸”技巧章节']
- topic_keywords: ['烹饪技巧', '关键要点', '资料依据', '结论保留']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8556

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '关键要点', '资料依据', '结论保留']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 4

## Hybrid Branch Status / entity_level
- keywords: ['蒸', '“蒸”技巧章节']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 201

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 587

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 0
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 14
- duplicate_count: 6

## Hybrid Technique Expansion
- enabled: True
- seed_count: 10
- expanded_count: 9
- doc_names: ['蒸（米）/炖（使用电饭煲/高压锅/电压力锅）', '使用微波炉']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 15
- duration_ms: 21278
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueChunk': 2, 'TechniqueDoc': 2, '烹饪技巧': 1}
- deferred_count: 4
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 30484
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:22:28.737
- end: 2026-08-11T17:23:06.696
- duration_ms: 37959
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4573
- retrieval_levels: ['context_expansion', 'entity']
- search_types: ['entity_level', 'technique_expansion']
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
- chunk_count: 91
- redacted_field: 2423
- total_duration_ms: 4306
- fallback_used: False

## Final Output
- answer_chars: 132
- answer_hash: 4abd8f5e59b08c03
- success: True

## Request Complete
- request_end: 2026-08-11T17:23:11.020
- request_duration_ms: 42286
- success: True
- final_source: generation

