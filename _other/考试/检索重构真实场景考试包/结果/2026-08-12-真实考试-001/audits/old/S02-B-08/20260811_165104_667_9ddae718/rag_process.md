# RAG Process

audit_id: 20260811_165104_667_9ddae718
timestamp: 2026-08-11T16:51:04.668
## Request
- original_query: 刚开始做小龙虾时，第一步具体要处理什么？
- original_query_hash: cb3eb480388e6298
- session_id: 2026-08-12-真实考试-001:old:S02-B-08
- request_mode: stream
- request_start: 2026-08-11T16:51:04.668
- evaluation_sample_id: 20260811_165104_667_9ddae718
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:51:04.669
- end: 2026-08-11T16:51:04.669
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:51:04.669
- end: 2026-08-11T16:51:04.669
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: cb3eb480388e6298

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:51:04.669
- end: 2026-08-11T16:51:04.669
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 20
- analysis_input_query_hash: cb3eb480388e6298
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:51:04.670
- end: 2026-08-11T16:51:16.204
- duration_ms: 11534
- analysis_mode: llm
- query_complexity: 0.18
- relationship_intensity: 0.12
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是围绕“小龙虾”烹饪前处理步骤的直接事实性提问，核心意图是获取起始操作（通常为清洗、挑拣或去除杂质等）。不存在多实体关系网络，也不要求多跳、因果或对比推理，适合通过关键词检索、菜谱步骤文档与常规语义召回进行回答。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 47, 'graph_rag_count': 0, 'total_queries': 47}
- route_stats_after: {'traditional_count': 48, 'graph_rag_count': 0, 'total_queries': 48}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['小龙虾', '小龙虾清洗', '刷洗', '去虾线']
- topic_keywords: ['烹饪技巧', '食材处理', '清洗', '去腥', '食品安全']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2984

## Hybrid Branch Status / entity_level
- keywords: ['小龙虾', '小龙虾清洗', '刷洗', '去虾线']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 21

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '食材处理', '清洗', '去腥', '食品安全']
- requested_k: 10
- actual_count: 9
- fallback_count: 9
- duration_ms: 38

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 279

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 9
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
- duration_ms: 16317
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '荤菜': 2, '早餐': 1}
- deferred_count: 5
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 19603
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:51:04.670
- end: 2026-08-11T16:51:35.809
- duration_ms: 31139
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2231
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
- chunk_count: 60
- redacted_field: 4337
- total_duration_ms: 5656
- fallback_used: False

## Final Output
- answer_chars: 74
- answer_hash: 19b36c3378a20763
- success: True

## Request Complete
- request_end: 2026-08-11T16:51:41.482
- request_duration_ms: 36813
- success: True
- final_source: generation

