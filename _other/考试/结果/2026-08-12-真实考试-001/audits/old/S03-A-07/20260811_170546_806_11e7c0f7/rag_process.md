# RAG Process

audit_id: 20260811_170546_806_11e7c0f7
timestamp: 2026-08-11T17:05:46.807
## Request
- original_query: 请说明“蒸（米）/炖（使用电饭煲/高压锅/电压力锅）”这个技巧的关键要点和适用情形。
- original_query_hash: c393fcfd7bbdc6a9
- session_id: 2026-08-12-真实考试-001:old:S03-A-07
- request_mode: stream
- request_start: 2026-08-11T17:05:46.807
- evaluation_sample_id: 20260811_170546_806_11e7c0f7
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:05:46.808
- end: 2026-08-11T17:05:46.808
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:05:46.808
- end: 2026-08-11T17:05:46.808
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 42
- enhanced_query_length: 42
- enhanced_query_hash: c393fcfd7bbdc6a9

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:05:46.808
- end: 2026-08-11T17:05:46.808
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 42
- analysis_input_query_hash: c393fcfd7bbdc6a9
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:05:46.809
- end: 2026-08-11T17:05:59.668
- duration_ms: 12859
- analysis_mode: llm
- query_complexity: 0.62
- relationship_intensity: 0.58
- reasoning_required: True
- entity_count: 5
- strategy: hybrid_traditional
- confidence: 0.87
- reasoning: 该查询要求说明“蒸米”和“炖”两类烹饪技巧的关键操作要点及适用情形，并涉及电饭煲、高压锅、电压力锅三种器具。需要将烹饪方式、器具特性、食材/菜品适用范围、时间与水量控制等信息进行关联，并隐含不同器具间的适用性对比。但查询主要面向明确的烹饪知识归纳与说明，不需要追溯复杂历史、地理或多领域因果网络，也不依赖多跳知识发现。因此适合采用hybrid_traditional，通过关键词检索、语义检索及结果重排获取权威烹饪说明、设备使用指南和食谱类资料。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 66, 'graph_rag_count': 0, 'total_queries': 66}
- route_stats_after: {'traditional_count': 67, 'graph_rag_count': 0, 'total_queries': 67}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['蒸米', '炖', '米', '电饭煲', '高压锅', '电压力锅']
- topic_keywords: ['烹饪技巧', '火候', '时间控制', '适用情形', '主食烹饪']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 10186

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '火候', '时间控制', '适用情形', '主食烹饪']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 78

## Hybrid Branch Status / entity_level
- keywords: ['蒸米', '炖', '米', '电饭煲', '高压锅', '电压力锅']
- requested_k: 10
- actual_count: 10
- fallback_count: 3
- duration_ms: 129

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 386

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 23
- duplicate_count: 7

## Hybrid Technique Expansion
- enabled: True
- seed_count: 7
- expanded_count: 9
- doc_names: ['蒸（米）/炖（使用电饭煲/高压锅/电压力锅）', '蒸']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 24
- duration_ms: 20699
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 2, 'TechniqueDoc': 1, 'TechniqueChunk': 2}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 31320
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:05:46.809
- end: 2026-08-11T17:06:30.989
- duration_ms: 44180
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
- chunk_count: 1059
- redacted_field: 2389
- total_duration_ms: 23339
- fallback_used: False

## Final Output
- answer_chars: 1390
- answer_hash: 87457521dda69937
- success: True

## Request Complete
- request_end: 2026-08-11T17:06:54.358
- request_duration_ms: 67550
- success: True
- final_source: generation

