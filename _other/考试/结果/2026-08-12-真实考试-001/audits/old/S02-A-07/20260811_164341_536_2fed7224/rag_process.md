# RAG Process

audit_id: 20260811_164341_536_2fed7224
timestamp: 2026-08-11T16:43:41.536
## Request
- original_query: 羊排焖面的第 1 步应该怎么做？
- original_query_hash: 8bec15e0e20e5112
- session_id: 2026-08-12-真实考试-001:old:S02-A-07
- request_mode: stream
- request_start: 2026-08-11T16:43:41.536
- evaluation_sample_id: 20260811_164341_536_2fed7224
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:43:41.537
- end: 2026-08-11T16:43:41.537
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:43:41.538
- end: 2026-08-11T16:43:41.538
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: 8bec15e0e20e5112

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:43:41.539
- end: 2026-08-11T16:43:41.539
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 16
- analysis_input_query_hash: 8bec15e0e20e5112
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:43:41.540
- end: 2026-08-11T16:43:55.702
- duration_ms: 14161
- analysis_mode: llm
- query_complexity: 0.15
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对特定菜谱“羊排焖面”的单一步骤信息查找，目标明确：定位其“第1步”的操作内容。无需多跳推理、因果分析或方案对比，仅需通过关键词匹配、菜谱标题检索及步骤字段排序/定位即可回答。明确实体包括菜品实体“羊排焖面”和流程位置实体“第1步”。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 36, 'graph_rag_count': 0, 'total_queries': 36}
- route_stats_after: {'traditional_count': 37, 'graph_rag_count': 0, 'total_queries': 37}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['羊排焖面', '羊排', '面条']
- topic_keywords: ['烹饪步骤', '烹饪技巧']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4280

## Hybrid Branch Status / topic_level
- keywords: ['烹饪步骤', '烹饪技巧']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 12

## Hybrid Branch Status / entity_level
- keywords: ['羊排焖面', '羊排', '面条']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 32

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 496

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 0
- vector_count: 10
- origin_len: 12

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 12
- after_count: 9
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
- candidate_count: 9
- duration_ms: 15636
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '半成品': 1, '汤类': 1, '主食': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20430
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:43:41.540
- end: 2026-08-11T16:44:16.133
- duration_ms: 34592
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3474
- retrieval_levels: ['']
- search_types: ['vector_enhanced']
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
- chunk_count: 32
- redacted_field: 1959
- total_duration_ms: 2933
- fallback_used: False

## Final Output
- answer_chars: 37
- answer_hash: 94900e6d1447ef88
- success: True

## Request Complete
- request_end: 2026-08-11T16:44:19.085
- request_duration_ms: 37549
- success: True
- final_source: generation

