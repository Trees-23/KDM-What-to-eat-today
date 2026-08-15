# RAG Process

audit_id: 20260811_193409_839_751e5608
timestamp: 2026-08-11T19:34:09.840
## Request
- original_query: 西红柿炒鸡蛋从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 2f75a61622dcdec8
- session_id: 2026-08-12-真实考试-001:new:S01-B-01
- request_mode: stream
- request_start: 2026-08-11T19:34:09.841
- evaluation_sample_id: 20260811_193409_839_751e5608
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:34:09.841
- end: 2026-08-11T19:34:09.841
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:34:09.842
- end: 2026-08-11T19:34:09.842
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 28
- enhanced_query_length: 28
- enhanced_query_hash: 2f75a61622dcdec8

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:34:09.852
- end: 2026-08-11T19:34:09.852
- duration_ms: 0
- entity_id: 201005181
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:34:09.852
- end: 2026-08-11T19:34:09.852
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:34:09.852
- end: 2026-08-11T19:34:09.852
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 28
- analysis_input_query_hash: 2f75a61622dcdec8
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:34:09.852
- end: 2026-08-11T19:34:17.808
- duration_ms: 7956
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.3
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是针对“西红柿炒鸡蛋”制作流程的直接信息查找，目标是从知识库中检索备料、烹饪步骤和出锅要点等标准做法。查询包含菜品实体“西红柿炒鸡蛋”及食材实体“西红柿”“鸡蛋”，但实体间主要是食材组成与线性烹饪步骤关系，不涉及复杂关系网络。无需多跳推理、因果分析或多方案对比，只需通过关键词/语义检索定位知识库中的对应菜谱，并按步骤组织返回，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 9, 'graph_rag_count': 0, 'total_queries': 9}
- route_stats_after: {'traditional_count': 10, 'graph_rag_count': 0, 'total_queries': 10}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['西红柿炒鸡蛋', '西红柿', '鸡蛋']
- topic_keywords: ['家常菜', '快手菜', '烹饪技巧', '备料', '火候', '炒制']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3742

## Hybrid Branch Status / entity_level
- keywords: ['西红柿炒鸡蛋', '西红柿', '鸡蛋']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 42

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '快手菜', '烹饪技巧', '备料', '火候', '炒制']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 78

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 482

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 10
- vector_count: 10
- origin_len: 23

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 23
- after_count: 19
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 19
- duration_ms: 14386
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '汤类': 1, '主食': 1, '早餐': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18626
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:34:09.852
- end: 2026-08-11T19:34:36.436
- duration_ms: 26583
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
- chunk_count: 387
- redacted_field: 1974
- total_duration_ms: 9925
- fallback_used: False

## Final Output
- answer_chars: 513
- answer_hash: 3fbbefe7f606c075
- success: True

## Request Complete
- request_end: 2026-08-11T19:34:46.385
- request_duration_ms: 36543
- success: True
- final_source: generation

