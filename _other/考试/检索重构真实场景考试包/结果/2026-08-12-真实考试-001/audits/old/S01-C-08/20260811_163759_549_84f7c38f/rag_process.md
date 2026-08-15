# RAG Process

audit_id: 20260811_163759_549_84f7c38f
timestamp: 2026-08-11T16:37:59.552
## Request
- original_query: 我只要知识库能证明的杨枝甘露做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 9dc9bd5f3c7a6a4b
- session_id: 2026-08-12-真实考试-001:old:S01-C-08
- request_mode: stream
- request_start: 2026-08-11T16:37:59.552
- evaluation_sample_id: 20260811_163759_549_84f7c38f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:37:59.553
- end: 2026-08-11T16:37:59.553
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:37:59.553
- end: 2026-08-11T16:37:59.553
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: 9dc9bd5f3c7a6a4b

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:37:59.554
- end: 2026-08-11T16:37:59.554
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 35
- analysis_input_query_hash: 9dc9bd5f3c7a6a4b
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:37:59.554
- end: 2026-08-11T16:38:12.681
- duration_ms: 13126
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.3
- reasoning_required: True
- entity_count: 4
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 查询核心是获取“杨枝甘露”的做法，并施加严格的证据边界：答案必须由知识库内容证明，且不得补充无引用依据的替代方案或营养结论。该任务需要对检索结果进行相关性排序、证据归属校验和生成约束控制，但不涉及多个实体之间的复杂关系网络。明确实体/概念包括“杨枝甘露”（菜品/饮品）、“知识库”（证据来源）、“替代方案”（需排除的内容类型）和“营养结论”（需排除的内容类型）。不需要多跳推理、因果分析或对比分析；适合使用 hybrid_traditional 进行关键词/语义混合检索，并基于命中文档进行带引用的受限回答。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 27, 'graph_rag_count': 0, 'total_queries': 27}
- route_stats_after: {'traditional_count': 28, 'graph_rag_count': 0, 'total_queries': 28}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['杨枝甘露']
- topic_keywords: ['做法', '知识库依据', '引用验证']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4467

## Hybrid Branch Status / entity_level
- keywords: ['杨枝甘露']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 15

## Hybrid Branch Status / topic_level
- keywords: ['做法', '知识库依据', '引用验证']
- requested_k: 10
- actual_count: 8
- fallback_count: 8
- duration_ms: 68

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 445

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 8
- vector_count: 10
- origin_len: 19

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 19
- after_count: 17
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['焯水', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 18
- duration_ms: 17869
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'饮料': 1, '烹饪技巧': 2, '主食': 2}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22817
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:37:59.554
- end: 2026-08-11T16:38:35.499
- duration_ms: 35945
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2435
- retrieval_levels: ['', 'context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 238
- redacted_field: 4151
- total_duration_ms: 10206
- fallback_used: False

## Final Output
- answer_chars: 303
- answer_hash: d8f848bd1fad9ad8
- success: True

## Request Complete
- request_end: 2026-08-11T16:38:45.734
- request_duration_ms: 46181
- success: True
- final_source: generation

