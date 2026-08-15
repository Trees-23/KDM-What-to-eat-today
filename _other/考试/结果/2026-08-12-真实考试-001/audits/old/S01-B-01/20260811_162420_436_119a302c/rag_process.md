# RAG Process

audit_id: 20260811_162420_436_119a302c
timestamp: 2026-08-11T16:24:20.437
## Request
- original_query: 西红柿炒鸡蛋从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 2f75a61622dcdec8
- session_id: 2026-08-12-真实考试-001:old:S01-B-01
- request_mode: stream
- request_start: 2026-08-11T16:24:20.437
- evaluation_sample_id: 20260811_162420_436_119a302c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:24:20.438
- end: 2026-08-11T16:24:20.438
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:24:20.438
- end: 2026-08-11T16:24:20.438
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 28
- enhanced_query_length: 28
- enhanced_query_hash: 2f75a61622dcdec8

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:24:20.439
- end: 2026-08-11T16:24:20.439
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 28
- analysis_input_query_hash: 2f75a61622dcdec8
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:24:20.439
- end: 2026-08-11T16:24:29.256
- duration_ms: 8817
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是针对“西红柿炒鸡蛋”这一明确菜品的流程型信息检索，目标是从知识库中获取从备料、处理食材、烹饪到出锅的标准做法。无需多跳推理、因果分析或跨菜品对比；仅需围绕菜品名称及其核心食材“西红柿”“鸡蛋”进行关键词、语义和步骤字段检索。实体包括菜品实体“西红柿炒鸡蛋”以及食材实体“西红柿”“鸡蛋”。因此适合使用 hybrid_traditional 策略，以关键词精确匹配结合语义检索召回知识库中的对应菜谱与步骤。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 10, 'graph_rag_count': 0, 'total_queries': 10}
- route_stats_after: {'traditional_count': 11, 'graph_rag_count': 0, 'total_queries': 11}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['西红柿', '鸡蛋', '西红柿炒鸡蛋']
- topic_keywords: ['家常菜', '快手菜', '烹饪技巧', '备料', '火候', '调味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 10780

## Hybrid Branch Status / entity_level
- keywords: ['西红柿', '鸡蛋', '西红柿炒鸡蛋']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: -957

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '快手菜', '烹饪技巧', '备料', '火候', '调味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: -884

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 460

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 10
- vector_count: 10
- origin_len: 23

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 23
- after_count: 18
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 18
- duration_ms: 15516
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '汤类': 1, '主食': 1, '早餐': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25781
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:24:20.439
- end: 2026-08-11T16:24:55.039
- duration_ms: 34599
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3352
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
- chunk_count: 369
- redacted_field: 2166
- total_duration_ms: 9678
- fallback_used: False

## Final Output
- answer_chars: 500
- answer_hash: 032d5f35452697d9
- success: True

## Request Complete
- request_end: 2026-08-11T16:25:04.739
- request_duration_ms: 44302
- success: True
- final_source: generation

