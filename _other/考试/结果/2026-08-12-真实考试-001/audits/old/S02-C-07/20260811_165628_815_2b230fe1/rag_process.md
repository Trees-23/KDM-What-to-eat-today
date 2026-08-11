# RAG Process

audit_id: 20260811_165628_815_2b230fe1
timestamp: 2026-08-11T16:56:28.818
## Request
- original_query: 只回答陈皮排骨汤的第 1 步，并说明它来自哪一条菜谱步骤；不要混入后续步骤。
- original_query_hash: c5f5ef558ae321d2
- session_id: 2026-08-12-真实考试-001:old:S02-C-07
- request_mode: stream
- request_start: 2026-08-11T16:56:28.819
- evaluation_sample_id: 20260811_165628_815_2b230fe1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:56:28.819
- end: 2026-08-11T16:56:28.819
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:56:28.820
- end: 2026-08-11T16:56:28.820
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 38
- enhanced_query_length: 38
- enhanced_query_hash: c5f5ef558ae321d2

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:56:28.820
- end: 2026-08-11T16:56:28.820
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 38
- analysis_input_query_hash: c5f5ef558ae321d2
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:56:28.820
- end: 2026-08-11T16:56:51.092
- duration_ms: 22271
- analysis_mode: llm
- query_complexity: 0.42
- relationship_intensity: 0.35
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询本质上是带有严格位置、范围和溯源约束的结构化信息抽取任务，而非复杂关系发现。需要检索“陈皮排骨汤”菜谱，并通过关键词、步骤编号或文档字段过滤精确返回第1步，同时避免召回或生成后续步骤。传统关键词检索结合向量检索及元数据/段落排序即可满足需求，无需图谱多跳推理。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 56, 'graph_rag_count': 0, 'total_queries': 56}
- route_stats_after: {'traditional_count': 57, 'graph_rag_count': 0, 'total_queries': 57}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['陈皮排骨汤', '陈皮', '排骨']
- topic_keywords: ['菜谱步骤', '第1步', '步骤溯源', '烹饪流程']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 1813

## Hybrid Branch Status / topic_level
- keywords: ['菜谱步骤', '第1步', '步骤溯源', '烹饪流程']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 6

## Hybrid Branch Status / entity_level
- keywords: ['陈皮排骨汤', '陈皮', '排骨']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 19

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 647

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 0
- vector_count: 10
- origin_len: 13

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 13
- after_count: 10
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
- candidate_count: 10
- duration_ms: 14333
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'汤类': 2, '荤菜': 2, 'Ingredient': 1}
- deferred_count: 4
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 16805
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:56:28.820
- end: 2026-08-11T16:57:07.899
- duration_ms: 39078
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2453
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
- chunk_count: 58
- redacted_field: 3279
- total_duration_ms: 4069
- fallback_used: False

## Final Output
- answer_chars: 72
- answer_hash: de11a8f08c604d7d
- success: True

## Request Complete
- request_end: 2026-08-11T16:57:12.003
- request_duration_ms: 43184
- success: True
- final_source: generation

