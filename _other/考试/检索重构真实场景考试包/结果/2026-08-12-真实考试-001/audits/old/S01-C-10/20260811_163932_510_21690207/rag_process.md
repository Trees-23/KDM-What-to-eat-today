# RAG Process

audit_id: 20260811_163932_510_21690207
timestamp: 2026-08-11T16:39:32.516
## Request
- original_query: 我只要知识库能证明的西红柿土豆炖牛肉做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: ab13e4503000d9e4
- session_id: 2026-08-12-真实考试-001:old:S01-C-10
- request_mode: stream
- request_start: 2026-08-11T16:39:32.516
- evaluation_sample_id: 20260811_163932_510_21690207
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:39:32.517
- end: 2026-08-11T16:39:32.517
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:39:32.517
- end: 2026-08-11T16:39:32.517
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 39
- enhanced_query_length: 39
- enhanced_query_hash: ab13e4503000d9e4

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:39:32.517
- end: 2026-08-11T16:39:32.517
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 39
- analysis_input_query_hash: ab13e4503000d9e4
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:39:32.518
- end: 2026-08-11T16:39:41.467
- duration_ms: 8949
- analysis_mode: llm
- query_complexity: 0.48
- relationship_intensity: 0.52
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 查询的核心目标是检索并整理“西红柿、土豆、牛肉”构成的炖菜做法，且所有步骤、用料和结论必须能够被知识库内容直接证明或引用。它涉及食材与烹饪步骤之间的关系，但不要求探索复杂知识网络。需要进行证据约束推理：筛选具有明确做法依据的文档、抽取可引用的配料和步骤、排除知识库未支持的替代方案及营养结论。通常不需要多跳推理、因果分析或对比分析，因此更适合采用关键词/BM25与向量检索结合，并配合引用片段校验的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 29, 'graph_rag_count': 0, 'total_queries': 29}
- route_stats_after: {'traditional_count': 30, 'graph_rag_count': 0, 'total_queries': 30}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['西红柿土豆炖牛肉', '西红柿', '土豆', '牛肉']
- topic_keywords: ['炖菜', '家常菜', '知识库依据', '引用']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8714

## Hybrid Branch Status / topic_level
- keywords: ['炖菜', '家常菜', '知识库依据', '引用']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 32

## Hybrid Branch Status / entity_level
- keywords: ['西红柿土豆炖牛肉', '西红柿', '土豆', '牛肉']
- requested_k: 10
- actual_count: 4
- fallback_count: 0
- duration_ms: 52

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 481

## Hybrid Branch Summary
- entity_count: 4
- topic_count: 2
- vector_count: 10
- origin_len: 16

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 16
- after_count: 13
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
- candidate_count: 13
- duration_ms: 17804
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '汤类': 1, '素菜': 1, '主食': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 27019
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:39:32.518
- end: 2026-08-11T16:40:08.488
- duration_ms: 35970
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2622
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
- chunk_count: 561
- redacted_field: 2342
- total_duration_ms: 13672
- fallback_used: False

## Final Output
- answer_chars: 742
- answer_hash: 0bc8b1be4c181e9c
- success: True

## Request Complete
- request_end: 2026-08-11T16:40:22.197
- request_duration_ms: 49680
- success: True
- final_source: generation

