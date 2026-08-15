# RAG Process

audit_id: 20260811_192856_483_3bdb4c25
timestamp: 2026-08-11T19:28:56.483
## Request
- original_query: 请给出水煮鱼的完整做法，包括主要食材和步骤。
- original_query_hash: 80f6e88f9a0a6252
- session_id: 2026-08-12-真实考试-001:new:S01-A-03
- request_mode: stream
- request_start: 2026-08-11T19:28:56.483
- evaluation_sample_id: 20260811_192856_483_3bdb4c25
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:28:56.484
- end: 2026-08-11T19:28:56.484
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:28:56.484
- end: 2026-08-11T19:28:56.484
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 22
- enhanced_query_length: 22
- enhanced_query_hash: 80f6e88f9a0a6252

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:28:56.498
- end: 2026-08-11T19:28:56.498
- duration_ms: 0
- entity_id: 201000040
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:28:56.499
- end: 2026-08-11T19:28:56.499
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:28:56.499
- end: 2026-08-11T19:28:56.499
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 22
- analysis_input_query_hash: 80f6e88f9a0a6252
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:28:56.499
- end: 2026-08-11T19:29:02.392
- duration_ms: 5893
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询属于明确的菜谱型信息检索任务，核心目标是获取“水煮鱼”的主要食材与按顺序组织的制作步骤。虽然回答需要覆盖食材、调料、处理流程和烹饪顺序，但这些内容是围绕单一菜品的结构化属性展开，不涉及跨领域、多实体的复杂关系网络。无需多跳推理、因果分析或方案对比；采用关键词检索、菜谱文档召回与结构化字段抽取即可满足需求，因此推荐hybrid_traditional。明确实体包括：水煮鱼（菜品）、主要食材（食材类别/属性）、步骤（制作流程属性）。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 2, 'graph_rag_count': 0, 'total_queries': 2}
- route_stats_after: {'traditional_count': 3, 'graph_rag_count': 0, 'total_queries': 3}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['水煮鱼', '鱼片', '豆芽', '油菜', '干辣椒', '花椒', '郫县豆瓣酱', '葱', '姜', '蒜', '食用油', '炒锅']
- topic_keywords: ['川菜', '麻辣', '香辣', '下饭菜', '烹饪步骤', '火候', '调味', '去腥']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4392

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '麻辣', '香辣', '下饭菜', '烹饪步骤', '火候', '调味', '去腥']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 90

## Hybrid Branch Status / entity_level
- keywords: ['水煮鱼', '鱼片', '豆芽', '油菜', '干辣椒', '花椒', '郫县豆瓣酱', '葱', '姜', '蒜', '食用油', '炒锅']
- requested_k: 10
- actual_count: 10
- fallback_count: 1
- duration_ms: 146

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 293

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 29
- duplicate_count: 1

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 29
- duration_ms: 27513
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '汤类': 1, 'Ingredient': 1, '主食,凉菜': 1}
- deferred_count: 7
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 32216
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:28:56.499
- end: 2026-08-11T19:29:34.610
- duration_ms: 38110
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2686
- retrieval_levels: ['', 'entity', 'topic']
- search_types: ['entity_level', 'topic_level', 'vector_enhanced']
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
- chunk_count: 515
- redacted_field: 1955
- total_duration_ms: 11244
- fallback_used: False

## Final Output
- answer_chars: 664
- answer_hash: 06880ab41b1dbc94
- success: True

## Request Complete
- request_end: 2026-08-11T19:29:45.878
- request_duration_ms: 49394
- success: True
- final_source: generation

