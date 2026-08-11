# RAG Process

audit_id: 20260811_163530_636_70fde5f6
timestamp: 2026-08-11T16:35:30.638
## Request
- original_query: 我只要知识库能证明的鸡蛋三明治做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 5f43ed0e16aec2a4
- session_id: 2026-08-12-真实考试-001:old:S01-C-04
- request_mode: stream
- request_start: 2026-08-11T16:35:30.638
- evaluation_sample_id: 20260811_163530_636_70fde5f6
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:35:30.639
- end: 2026-08-11T16:35:30.639
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:35:30.640
- end: 2026-08-11T16:35:30.640
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 5f43ed0e16aec2a4

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:35:30.640
- end: 2026-08-11T16:35:30.640
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 5f43ed0e16aec2a4
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:35:30.640
- end: 2026-08-11T16:35:40.363
- duration_ms: 9722
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.3
- reasoning_required: True
- entity_count: 4
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 查询核心是从知识库中检索“鸡蛋三明治做法”，属于目标明确的事实/步骤型信息查找。其额外难点不在复杂知识推理，而在证据约束：仅输出可被知识库文档直接支持的做法，并为步骤提供引用依据，同时过滤未被引用支持的替代方案和营养结论。无需多跳推理、因果分析或方案对比；适合采用关键词检索结合向量检索，并通过引用覆盖校验与答案约束生成实现。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 23, 'graph_rag_count': 0, 'total_queries': 23}
- route_stats_after: {'traditional_count': 24, 'graph_rag_count': 0, 'total_queries': 24}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鸡蛋三明治', '鸡蛋']
- topic_keywords: ['知识库依据', '引用', '可验证性']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3291

## Hybrid Branch Status / topic_level
- keywords: ['知识库依据', '引用', '可验证性']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 11

## Hybrid Branch Status / entity_level
- keywords: ['鸡蛋三明治', '鸡蛋']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 22

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 388

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 0
- vector_count: 10
- origin_len: 12

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 12
- after_count: 11
- duplicate_count: 1

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['炒/煎', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 12
- duration_ms: 15423
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'早餐': 2, '主食': 2, '烹饪技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 19128
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:35:30.640
- end: 2026-08-11T16:35:59.492
- duration_ms: 28851
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1965
- retrieval_levels: ['', 'context_expansion']
- search_types: ['technique_expansion', 'vector_enhanced']
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
- chunk_count: 160
- redacted_field: 3516
- total_duration_ms: 6454
- fallback_used: False

## Final Output
- answer_chars: 206
- answer_hash: cb59059b00d68720
- success: True

## Request Complete
- request_end: 2026-08-11T16:36:05.980
- request_duration_ms: 35342
- success: True
- final_source: generation

