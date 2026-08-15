# RAG Process

audit_id: 20260811_173236_724_c82f3633
timestamp: 2026-08-11T17:32:36.726
## Request
- original_query: 家里有虾，知识库里能做哪些菜？
- original_query_hash: 47ab74136bee3056
- session_id: 2026-08-12-真实考试-001:old:S04-A-09
- request_mode: stream
- request_start: 2026-08-11T17:32:36.726
- evaluation_sample_id: 20260811_173236_724_c82f3633
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:32:36.727
- end: 2026-08-11T17:32:36.727
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:32:36.727
- end: 2026-08-11T17:32:36.727
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 15
- enhanced_query_length: 15
- enhanced_query_hash: 47ab74136bee3056

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:32:36.727
- end: 2026-08-11T17:32:36.727
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 15
- analysis_input_query_hash: 47ab74136bee3056
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:32:36.728
- end: 2026-08-11T17:32:46.730
- duration_ms: 10002
- analysis_mode: llm
- query_complexity: 0.3
- relationship_intensity: 0.5
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 查询核心是以“虾”这一食材为条件，从知识库中的菜谱/菜品文档中检索包含该食材的结果，属于食材与菜品之间的直接关联匹配。无需多跳推理、因果分析或对比分析；可通过关键词检索、食材字段过滤及语义召回实现，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 97, 'graph_rag_count': 1, 'total_queries': 98}
- route_stats_after: {'traditional_count': 98, 'graph_rag_count': 1, 'total_queries': 99}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['虾', '白灼虾', '油焖大虾', '蒜蓉粉丝蒸虾', '椒盐虾', '宫保虾球', '虾仁炒蛋', '虾仁炒饭', '虾仁豆腐', '清炒虾仁']
- topic_keywords: ['家常菜', '海鲜', '快手菜', '营养', '高蛋白']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 9577

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '海鲜', '快手菜', '营养', '高蛋白']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 90

## Hybrid Branch Status / entity_level
- keywords: ['虾', '白灼虾', '油焖大虾', '蒜蓉粉丝蒸虾', '椒盐虾', '宫保虾球', '虾仁炒蛋', '虾仁炒饭', '虾仁豆腐', '清炒虾仁']
- requested_k: 10
- actual_count: 10
- fallback_count: 7
- duration_ms: 94

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 401

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 20
- duplicate_count: 10

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 20
- duration_ms: 16566
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '荤菜': 1, 'Recipe': 1, '主食': 1}
- deferred_count: 5
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 26569
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:32:36.728
- end: 2026-08-11T17:33:13.301
- duration_ms: 36573
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2567
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
- chunk_count: 386
- redacted_field: 2645
- total_duration_ms: 11005
- fallback_used: False

## Final Output
- answer_chars: 466
- answer_hash: 5922c3b4c28c61ea
- success: True

## Request Complete
- request_end: 2026-08-11T17:33:24.327
- request_duration_ms: 47600
- success: True
- final_source: generation

