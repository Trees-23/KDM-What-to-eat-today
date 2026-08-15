# RAG Process

audit_id: 20260811_193446_401_c157f9ca
timestamp: 2026-08-11T19:34:46.402
## Request
- original_query: 地三鲜从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: b68065d12930e3fa
- session_id: 2026-08-12-真实考试-001:new:S01-B-02
- request_mode: stream
- request_start: 2026-08-11T19:34:46.402
- evaluation_sample_id: 20260811_193446_401_c157f9ca
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:34:46.402
- end: 2026-08-11T19:34:46.402
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:34:46.403
- end: 2026-08-11T19:34:46.403
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 25
- enhanced_query_length: 25
- enhanced_query_hash: b68065d12930e3fa

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:34:46.413
- end: 2026-08-11T19:34:46.413
- duration_ms: 0
- entity_id: 201004898
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:34:46.414
- end: 2026-08-11T19:34:46.414
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:34:46.414
- end: 2026-08-11T19:34:46.414
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 25
- analysis_input_query_hash: b68065d12930e3fa
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:34:46.414
- end: 2026-08-11T19:34:53.181
- duration_ms: 6766
- analysis_mode: llm
- query_complexity: 0.28
- relationship_intensity: 0.22
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询是对菜品“地三鲜”制作流程的直接信息查找，核心目标是依据知识库检索备料、预处理、烹饪顺序、调味与出锅等步骤。虽然流程本身包含食材与操作步骤的顺序关系，但不需要跨文档多跳推理、因果机制分析或不同方案对比。明确实体主要包括“地三鲜”和“知识库中的做法”；其中地三鲜为菜品实体，知识库做法为内容/来源约束。适合使用hybrid_traditional，通过关键词、菜品别名及步骤类字段进行混合检索，并优先返回知识库中权威且步骤完整的食谱文档。

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
- entity_keywords: ['地三鲜', '茄子', '土豆', '青椒', '炒锅']
- topic_keywords: ['东北菜', '家常菜', '下饭菜', '烹饪技巧', '火候', '调味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3884

## Hybrid Branch Status / entity_level
- keywords: ['地三鲜', '茄子', '土豆', '青椒', '炒锅']
- requested_k: 10
- actual_count: 4
- fallback_count: 0
- duration_ms: 82

## Hybrid Branch Status / topic_level
- keywords: ['东北菜', '家常菜', '下饭菜', '烹饪技巧', '火候', '调味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 117

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 577

## Hybrid Branch Summary
- entity_count: 4
- topic_count: 10
- vector_count: 10
- origin_len: 24

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 24
- after_count: 22
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 4
- expanded_count: 9
- doc_names: ['炒/煎', '去腥']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 23
- duration_ms: 20119
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '烹饪技巧': 2, '主食': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 汤面
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24609
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:34:46.414
- end: 2026-08-11T19:35:17.791
- duration_ms: 31377
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2615
- retrieval_levels: ['', 'context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 670
- redacted_field: 4131
- total_duration_ms: 16836
- fallback_used: False

## Final Output
- answer_chars: 905
- answer_hash: e9b3a0ed1b632677
- success: True

## Request Complete
- request_end: 2026-08-11T19:35:34.661
- request_duration_ms: 48259
- success: True
- final_source: generation

