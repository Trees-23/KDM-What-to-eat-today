# RAG Process

audit_id: 20260811_170945_360_41ed7bd9
timestamp: 2026-08-11T17:09:45.362
## Request
- original_query: 我想学凉拌，它的关键要点和适用场景是什么？
- original_query_hash: 80b8971f769a63e1
- session_id: 2026-08-12-真实考试-001:old:S03-B-01
- request_mode: stream
- request_start: 2026-08-11T17:09:45.362
- evaluation_sample_id: 20260811_170945_360_41ed7bd9
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:09:45.363
- end: 2026-08-11T17:09:45.363
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:09:45.363
- end: 2026-08-11T17:09:45.363
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 80b8971f769a63e1

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:09:45.363
- end: 2026-08-11T17:09:45.363
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: 80b8971f769a63e1
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:09:45.364
- end: 2026-08-11T17:09:51.267
- duration_ms: 5903
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.42
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询聚焦于“凉拌”这一烹饪技法，要求获取其“关键要点”与“适用场景”。需要将凉拌技法与食材类型、食用情境等信息建立基础关联，但不涉及跨领域的复杂关系网络或多跳知识发现。可通过关键词检索、菜谱/烹饪知识库的语义召回与排序直接满足需求。无需多跳推理、因果分析或严格的方案对比分析；其中明确实体主要为“凉拌”（烹饪技法）和“适用场景”（应用/情境类概念）。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 70, 'graph_rag_count': 0, 'total_queries': 70}
- route_stats_after: {'traditional_count': 71, 'graph_rag_count': 0, 'total_queries': 71}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['凉拌', '凉拌菜', '凉菜', '焯水', '调味汁']
- topic_keywords: ['烹饪技巧', '调味', '入味', '口感', '开胃菜', '夏季菜', '快手菜', '食品安全']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3960

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '调味', '入味', '口感', '开胃菜', '夏季菜', '快手菜', '食品安全']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 37

## Hybrid Branch Status / entity_level
- keywords: ['凉拌', '凉拌菜', '凉菜', '焯水', '调味汁']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 270

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 324

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 19
- duplicate_count: 11

## Hybrid Technique Expansion
- enabled: True
- seed_count: 10
- expanded_count: 9
- doc_names: ['厨房准备']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 20
- duration_ms: 17994
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 2, 'TechniqueChunk': 2, '烹饪技巧': 1}
- deferred_count: 5
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22321
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:09:45.364
- end: 2026-08-11T17:10:13.590
- duration_ms: 28226
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 8513
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
- chunk_count: 836
- redacted_field: 3081
- total_duration_ms: 19785
- fallback_used: False

## Final Output
- answer_chars: 1072
- answer_hash: fb95c8a6274e2c41
- success: True

## Request Complete
- request_end: 2026-08-11T17:10:33.387
- request_duration_ms: 48025
- success: True
- final_source: generation

