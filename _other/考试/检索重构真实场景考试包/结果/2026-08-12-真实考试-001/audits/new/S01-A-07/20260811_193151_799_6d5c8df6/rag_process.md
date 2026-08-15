# RAG Process

audit_id: 20260811_193151_799_6d5c8df6
timestamp: 2026-08-11T19:31:51.800
## Request
- original_query: 请给出白灼虾的完整做法，包括主要食材和步骤。
- original_query_hash: 79bd1e787af1b833
- session_id: 2026-08-12-真实考试-001:new:S01-A-07
- request_mode: stream
- request_start: 2026-08-11T19:31:51.800
- evaluation_sample_id: 20260811_193151_799_6d5c8df6
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:31:51.801
- end: 2026-08-11T19:31:51.801
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:31:51.801
- end: 2026-08-11T19:31:51.801
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 22
- enhanced_query_length: 22
- enhanced_query_hash: 79bd1e787af1b833

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:31:51.810
- end: 2026-08-11T19:31:51.810
- duration_ms: 0
- entity_id: 201000272
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:31:51.810
- end: 2026-08-11T19:31:51.810
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:31:51.810
- end: 2026-08-11T19:31:51.810
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 22
- analysis_input_query_hash: 79bd1e787af1b833
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:31:51.811
- end: 2026-08-11T19:31:59.027
- duration_ms: 7216
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对单一菜品“白灼虾”的直接做法检索，需求明确限定为主要食材和制作步骤。虽涉及“虾”与调味料、烹饪步骤等基本关联，但不需要跨文档多跳推理、因果解释或方案对比。适合通过关键词、菜谱标题、食材字段和步骤字段进行混合检索后直接生成结构化答案。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 6, 'graph_rag_count': 0, 'total_queries': 6}
- route_stats_after: {'traditional_count': 7, 'graph_rag_count': 0, 'total_queries': 7}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['白灼虾', '鲜虾', '姜', '葱', '料酒', '生抽', '香醋', '蒜', '小米椒']
- topic_keywords: ['粤菜', '海鲜', '白灼', '蘸料', '去腥', '火候', '烹饪步骤']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4830

## Hybrid Branch Status / entity_level
- keywords: ['白灼虾', '鲜虾', '姜', '葱', '料酒', '生抽', '香醋', '蒜', '小米椒']
- requested_k: 10
- actual_count: 10
- fallback_count: 1
- duration_ms: 79

## Hybrid Branch Status / topic_level
- keywords: ['粤菜', '海鲜', '白灼', '蘸料', '去腥', '火候', '烹饪步骤']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 88

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 458

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 24
- duplicate_count: 6

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 24
- duration_ms: 16340
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '荤菜': 1, '素菜': 2}
- deferred_count: 5
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21652
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:31:51.811
- end: 2026-08-11T19:32:20.680
- duration_ms: 28869
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2362
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
- chunk_count: 302
- redacted_field: 2642
- total_duration_ms: 10435
- fallback_used: False

## Final Output
- answer_chars: 424
- answer_hash: e597f2cfcd8e0c44
- success: True

## Request Complete
- request_end: 2026-08-11T19:32:31.127
- request_duration_ms: 39326
- success: True
- final_source: generation

