# RAG Process

audit_id: 20260811_193035_952_921dbfc1
timestamp: 2026-08-11T19:30:35.953
## Request
- original_query: 请给出鳊鱼炖豆腐的完整做法，包括主要食材和步骤。
- original_query_hash: 747f25e2d25638f9
- session_id: 2026-08-12-真实考试-001:new:S01-A-05
- request_mode: stream
- request_start: 2026-08-11T19:30:35.953
- evaluation_sample_id: 20260811_193035_952_921dbfc1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:30:35.955
- end: 2026-08-11T19:30:35.955
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:30:35.955
- end: 2026-08-11T19:30:35.955
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 24
- enhanced_query_length: 24
- enhanced_query_hash: 747f25e2d25638f9

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:30:35.969
- end: 2026-08-11T19:30:35.969
- duration_ms: 0
- entity_id: 201000472
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:30:35.970
- end: 2026-08-11T19:30:35.970
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:30:35.970
- end: 2026-08-11T19:30:35.970
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 24
- analysis_input_query_hash: 747f25e2d25638f9
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:30:35.970
- end: 2026-08-11T19:30:41.159
- duration_ms: 5188
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.35
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是面向具体菜品“鳊鱼炖豆腐”的直接做法检索，目标明确：获取主要食材和完整烹饪步骤。涉及的核心实体为鳊鱼和豆腐，两者存在食材搭配关系，但不构成复杂关系网络。不需要多跳推理、因果分析或跨方案对比，只需从菜谱、烹饪知识库或结构化食谱文档中检索并整合相关信息，因此推荐使用hybrid_traditional策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 4, 'graph_rag_count': 0, 'total_queries': 4}
- route_stats_after: {'traditional_count': 5, 'graph_rag_count': 0, 'total_queries': 5}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鳊鱼', '豆腐', '鳊鱼炖豆腐']
- topic_keywords: ['家常菜', '炖菜', '鱼类菜肴', '烹饪步骤', '去腥', '火候']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3449

## Hybrid Branch Status / entity_level
- keywords: ['鳊鱼', '豆腐', '鳊鱼炖豆腐']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 54

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '炖菜', '鱼类菜肴', '烹饪步骤', '去腥', '火候']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 108

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 391

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 10
- vector_count: 10
- origin_len: 23

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 23
- after_count: 20
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
- candidate_count: 20
- duration_ms: 17167
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '汤类': 1, '荤菜': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21023
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:30:35.970
- end: 2026-08-11T19:31:02.183
- duration_ms: 26213
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2672
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
- chunk_count: 387
- redacted_field: 1846
- total_duration_ms: 9724
- fallback_used: False

## Final Output
- answer_chars: 533
- answer_hash: f3ec3e2a49f863f1
- success: True

## Request Complete
- request_end: 2026-08-11T19:31:11.933
- request_duration_ms: 35980
- success: True
- final_source: generation

