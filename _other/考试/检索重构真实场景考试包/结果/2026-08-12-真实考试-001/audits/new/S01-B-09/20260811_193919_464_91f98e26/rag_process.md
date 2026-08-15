# RAG Process

audit_id: 20260811_193919_464_91f98e26
timestamp: 2026-08-11T19:39:19.464
## Request
- original_query: 扬州炒饭从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 5b2e59aed9500e0e
- session_id: 2026-08-12-真实考试-001:new:S01-B-09
- request_mode: stream
- request_start: 2026-08-11T19:39:19.464
- evaluation_sample_id: 20260811_193919_464_91f98e26
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:39:19.465
- end: 2026-08-11T19:39:19.465
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:39:19.465
- end: 2026-08-11T19:39:19.465
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: 5b2e59aed9500e0e

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:39:19.469
- end: 2026-08-11T19:39:19.469
- duration_ms: 0
- entity_id: 201004478
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:39:19.469
- end: 2026-08-11T19:39:19.469
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:39:19.469
- end: 2026-08-11T19:39:19.469
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: 5b2e59aed9500e0e
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:39:19.470
- end: 2026-08-11T19:39:26.460
- duration_ms: 6990
- analysis_mode: llm
- query_complexity: 0.28
- relationship_intensity: 0.22
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询的核心目标是从知识库中检索“扬州炒饭”的标准制作流程，覆盖备料、处理、炒制和出锅等顺序步骤。虽包含“备料”和“出锅”两个流程阶段，但它们均属于同一菜品制作流程中的线性步骤，不涉及跨实体的复杂关系网络、多跳推理、因果归因或方案对比。明确实体可识别为“扬州炒饭”（菜品）、“备料”（烹饪流程阶段）和“出锅”（烹饪流程阶段）。适合通过关键词检索、菜谱标题匹配、步骤段落召回及重排序的 hybrid_traditional 策略获取知识库中的权威做法。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 16, 'graph_rag_count': 0, 'total_queries': 16}
- route_stats_after: {'traditional_count': 17, 'graph_rag_count': 0, 'total_queries': 17}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['扬州炒饭', '米饭', '鸡蛋', '火腿', '虾仁', '豌豆', '胡萝卜', '炒锅']
- topic_keywords: ['炒饭', '中式家常菜', '烹饪技巧', '备料', '火候', '调味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3380

## Hybrid Branch Status / entity_level
- keywords: ['扬州炒饭', '米饭', '鸡蛋', '火腿', '虾仁', '豌豆', '胡萝卜', '炒锅']
- requested_k: 10
- actual_count: 7
- fallback_count: 0
- duration_ms: 24

## Hybrid Branch Status / topic_level
- keywords: ['炒饭', '中式家常菜', '烹饪技巧', '备料', '火候', '调味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 36

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 659

## Hybrid Branch Summary
- entity_count: 7
- topic_count: 10
- vector_count: 10
- origin_len: 27

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 27
- after_count: 26
- duplicate_count: 1

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 8
- doc_names: ['炒/煎']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 27
- duration_ms: 22969
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '烹饪技巧': 2, '半成品': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 27030
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:39:19.470
- end: 2026-08-11T19:39:53.492
- duration_ms: 34022
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3520
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
- chunk_count: 607
- redacted_field: 1972
- total_duration_ms: 14011
- fallback_used: False

## Final Output
- answer_chars: 749
- answer_hash: dbdf5b2ac17e851d
- success: True

## Request Complete
- request_end: 2026-08-11T19:40:07.517
- request_duration_ms: 48052
- success: True
- final_source: generation

