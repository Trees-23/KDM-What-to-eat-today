# RAG Process

audit_id: 20260811_174830_033_4563f8ed
timestamp: 2026-08-11T17:48:30.036
## Request
- original_query: 茄子适合搭配什么蔬菜？
- original_query_hash: 5716758c2886a42d
- session_id: 2026-08-12-真实考试-001:old:S05-A-06
- request_mode: stream
- request_start: 2026-08-11T17:48:30.036
- evaluation_sample_id: 20260811_174830_033_4563f8ed
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:48:30.037
- end: 2026-08-11T17:48:30.037
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:48:30.038
- end: 2026-08-11T17:48:30.038
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 11
- enhanced_query_length: 11
- enhanced_query_hash: 5716758c2886a42d

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:48:30.038
- end: 2026-08-11T17:48:30.038
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 11
- analysis_input_query_hash: 5716758c2886a42d
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:48:30.039
- end: 2026-08-11T17:48:36.681
- duration_ms: 6641
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.55
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 该查询属于食材搭配类的直接信息查找，核心是识别“茄子”与“蔬菜”类别之间的适配关系。查询包含茄子这一具体食材实体，以及蔬菜这一泛化食材类别实体，关系密集度处于中等水平，但通常无需多跳推理、因果分析或复杂对比分析。可通过关键词检索、食谱知识库召回与语义排序直接获得常见搭配蔬菜，因此推荐hybrid_traditional策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 114, 'graph_rag_count': 11, 'total_queries': 125}
- route_stats_after: {'traditional_count': 115, 'graph_rag_count': 11, 'total_queries': 126}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['茄子', '青椒', '番茄', '土豆', '豆角', '洋葱', '蒜薹', '西葫芦']
- topic_keywords: ['蔬菜搭配', '素食', '家常菜', '下饭菜', '营养搭配']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3602

## Hybrid Branch Status / topic_level
- keywords: ['蔬菜搭配', '素食', '家常菜', '下饭菜', '营养搭配']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 25

## Hybrid Branch Status / entity_level
- keywords: ['茄子', '青椒', '番茄', '土豆', '豆角', '洋葱', '蒜薹', '西葫芦']
- requested_k: 10
- actual_count: 8
- fallback_count: 0
- duration_ms: 68

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 502

## Hybrid Branch Summary
- entity_count: 8
- topic_count: 2
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 17
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 17
- duration_ms: 16475
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, 'Ingredient': 2, '主食': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20595
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:48:30.039
- end: 2026-08-11T17:48:57.277
- duration_ms: 27238
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1892
- retrieval_levels: ['', 'entity']
- search_types: ['entity_level', 'vector_enhanced']
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
- chunk_count: 196
- redacted_field: 2360
- total_duration_ms: 6473
- fallback_used: False

## Final Output
- answer_chars: 245
- answer_hash: efe4ddf1e508c4b0
- success: True

## Request Complete
- request_end: 2026-08-11T17:49:03.771
- request_duration_ms: 33734
- success: True
- final_source: generation

