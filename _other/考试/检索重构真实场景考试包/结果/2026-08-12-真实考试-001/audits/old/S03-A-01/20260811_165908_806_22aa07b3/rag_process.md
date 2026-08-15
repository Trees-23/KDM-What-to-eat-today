# RAG Process

audit_id: 20260811_165908_806_22aa07b3
timestamp: 2026-08-11T16:59:08.807
## Request
- original_query: 请说明“如何决策吃什么”这个技巧的关键要点和适用情形。
- original_query_hash: a20e75c819e5e1b7
- session_id: 2026-08-12-真实考试-001:old:S03-A-01
- request_mode: stream
- request_start: 2026-08-11T16:59:08.807
- evaluation_sample_id: 20260811_165908_806_22aa07b3
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:59:08.807
- end: 2026-08-11T16:59:08.807
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:59:08.808
- end: 2026-08-11T16:59:08.808
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: a20e75c819e5e1b7

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:59:08.809
- end: 2026-08-11T16:59:08.809
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: a20e75c819e5e1b7
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:59:08.809
- end: 2026-08-11T16:59:26.043
- duration_ms: 17233
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.87
- reasoning: 查询核心实体为“如何决策吃什么”这一技巧/方法，用户需要了解其关键要点及适用情形，属于对单一方法的结构化说明与场景匹配。虽然需要将方法原则与不同饮食决策场景建立关联，并进行一定的归纳判断，但通常不依赖多个实体之间的复杂网络关系、跨主题多跳推理或深层因果链。因此适合通过关键词检索、语义检索及结果重排序获取与该技巧相关的定义、步骤、原则和应用案例，推荐采用 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 60, 'graph_rag_count': 0, 'total_queries': 60}
- route_stats_after: {'traditional_count': 61, 'graph_rag_count': 0, 'total_queries': 61}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['如何决策吃什么']
- topic_keywords: ['饮食决策', '用餐选择', '决策技巧', '适用情形']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 16145

## Hybrid Branch Status / topic_level
- keywords: ['饮食决策', '用餐选择', '决策技巧', '适用情形']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 10

## Hybrid Branch Status / entity_level
- keywords: ['如何决策吃什么']
- requested_k: 10
- actual_count: 5
- fallback_count: 0
- duration_ms: 68

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 693

## Hybrid Branch Summary
- entity_count: 5
- topic_count: 0
- vector_count: 10
- origin_len: 15

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 15
- after_count: 9
- duplicate_count: 6

## Hybrid Technique Expansion
- enabled: True
- seed_count: 7
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 10
- duration_ms: 13146
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 1, 'TechniqueChunk': 2, '烹饪技巧': 2}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 30028
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:59:08.809
- end: 2026-08-11T16:59:56.072
- duration_ms: 47262
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3970
- retrieval_levels: ['', 'context_expansion', 'entity']
- search_types: ['entity_level', 'technique_expansion', 'vector_enhanced']
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
- chunk_count: 741
- redacted_field: 4254
- total_duration_ms: 21167
- fallback_used: False

## Final Output
- answer_chars: 1068
- answer_hash: 88f8c873994e0078
- success: True

## Request Complete
- request_end: 2026-08-11T17:00:17.276
- request_duration_ms: 68469
- success: True
- final_source: generation

