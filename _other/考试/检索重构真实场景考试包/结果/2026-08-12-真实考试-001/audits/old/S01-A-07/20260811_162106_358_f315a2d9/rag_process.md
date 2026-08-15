# RAG Process

audit_id: 20260811_162106_358_f315a2d9
timestamp: 2026-08-11T16:21:06.360
## Request
- original_query: 请给出白灼虾的完整做法，包括主要食材和步骤。
- original_query_hash: 79bd1e787af1b833
- session_id: 2026-08-12-真实考试-001:old:S01-A-07
- request_mode: stream
- request_start: 2026-08-11T16:21:06.360
- evaluation_sample_id: 20260811_162106_358_f315a2d9
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:21:06.361
- end: 2026-08-11T16:21:06.361
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:21:06.361
- end: 2026-08-11T16:21:06.361
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 22
- enhanced_query_length: 22
- enhanced_query_hash: 79bd1e787af1b833

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:21:06.362
- end: 2026-08-11T16:21:06.362
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 22
- analysis_input_query_hash: 79bd1e787af1b833
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:21:06.362
- end: 2026-08-11T16:21:13.674
- duration_ms: 7311
- analysis_mode: llm
- query_complexity: 0.2
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是针对“白灼虾”这一明确菜品的直接做法查询，目标是获取主要食材和标准烹饪步骤，属于结构化、单主题的信息检索任务。查询中主要实体为“白灼虾”和“虾（主要食材）”；“主要食材”“步骤”属于信息字段或属性要求，而非需要跨实体推理的独立实体。无需多跳推理、因果分析或多方案对比，只需检索权威菜谱、烹饪教程或结构化食谱内容并抽取整合即可，因此推荐使用 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 6, 'graph_rag_count': 0, 'total_queries': 6}
- route_stats_after: {'traditional_count': 7, 'graph_rag_count': 0, 'total_queries': 7}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['白灼虾', '鲜虾', '姜', '葱', '料酒', '生抽', '香醋', '香油']
- topic_keywords: ['粤菜', '海鲜', '白灼', '蘸料', '去腥', '火候', '烹饪技巧']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3443

## Hybrid Branch Status / topic_level
- keywords: ['粤菜', '海鲜', '白灼', '蘸料', '去腥', '火候', '烹饪技巧']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 41

## Hybrid Branch Status / entity_level
- keywords: ['白灼虾', '鲜虾', '姜', '葱', '料酒', '生抽', '香醋', '香油']
- requested_k: 10
- actual_count: 10
- fallback_count: 2
- duration_ms: 92

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 701

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
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 23
- duration_ms: 18616
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '荤菜': 1, '素菜': 2}
- deferred_count: 5
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22777
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:21:06.362
- end: 2026-08-11T16:21:36.452
- duration_ms: 30089
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2362
- retrieval_levels: ['', 'topic']
- search_types: ['topic_level', 'vector_enhanced']
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
- chunk_count: 281
- redacted_field: 2311
- total_duration_ms: 8443
- fallback_used: False

## Final Output
- answer_chars: 397
- answer_hash: f64b284324e2e024
- success: True

## Request Complete
- request_end: 2026-08-11T16:21:44.911
- request_duration_ms: 38550
- success: True
- final_source: generation

