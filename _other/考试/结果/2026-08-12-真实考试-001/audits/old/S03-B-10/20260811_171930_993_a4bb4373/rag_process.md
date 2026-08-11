# RAG Process

audit_id: 20260811_171930_993_a4bb4373
timestamp: 2026-08-11T17:19:30.998
## Request
- original_query: 我想学糖色的炒制，它的关键要点和适用场景是什么？
- original_query_hash: fcb151f066c6d027
- session_id: 2026-08-12-真实考试-001:old:S03-B-10
- request_mode: stream
- request_start: 2026-08-11T17:19:30.998
- evaluation_sample_id: 20260811_171930_993_a4bb4373
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:19:30.999
- end: 2026-08-11T17:19:30.999
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:19:31.000
- end: 2026-08-11T17:19:31.000
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 24
- enhanced_query_length: 24
- enhanced_query_hash: fcb151f066c6d027

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:19:31.001
- end: 2026-08-11T17:19:31.001
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 24
- analysis_input_query_hash: fcb151f066c6d027
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:19:31.002
- end: 2026-08-11T17:19:37.602
- duration_ms: 6600
- analysis_mode: llm
- query_complexity: 0.52
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 查询聚焦于烹饪技法“糖色炒制”，需要获取其操作关键要点，并将不同糖色状态、火候与适用菜品/烹饪场景建立对应关系。它包含一定的过程性、条件性和因果性知识，如火候与糖色阶段如何影响成品颜色、苦味风险及适用菜式，但通常可通过菜谱、烹饪教程和结构化知识片段直接检索后整合，无需跨大量实体构建复杂关系网络。明确实体主要包括：糖色（食材/烹饪产物）、炒制（烹饪技法）、适用场景（菜品与烹饪应用类别）。推理需求包括有限的步骤关联和因果分析，不需要多跳推理或多方案深度对比，因此推荐hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 78, 'graph_rag_count': 1, 'total_queries': 79}
- route_stats_after: {'traditional_count': 79, 'graph_rag_count': 1, 'total_queries': 80}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['糖色', '炒糖色', '冰糖', '白砂糖']
- topic_keywords: ['烹饪技巧', '火候', '焦糖化', '上色', '红烧', '卤味', '炖菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3575

## Hybrid Branch Status / entity_level
- keywords: ['糖色', '炒糖色', '冰糖', '白砂糖']
- requested_k: 10
- actual_count: 7
- fallback_count: 0
- duration_ms: 36

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '火候', '焦糖化', '上色', '红烧', '卤味', '炖菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 47

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 629

## Hybrid Branch Summary
- entity_count: 7
- topic_count: 10
- vector_count: 10
- origin_len: 27

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 27
- after_count: 18
- duplicate_count: 9

## Hybrid Technique Expansion
- enabled: True
- seed_count: 5
- expanded_count: 5
- doc_names: ['糖色的炒制']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 19
- duration_ms: 17761
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 1, 'TechniqueDoc': 1, 'TechniqueChunk': 2, '调料': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22026
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:19:31.001
- end: 2026-08-11T17:19:59.630
- duration_ms: 28628
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4154
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
- chunk_count: 1023
- redacted_field: 2966
- total_duration_ms: 22340
- fallback_used: False

## Final Output
- answer_chars: 1402
- answer_hash: fc4a42409c78d9d8
- success: True

## Request Complete
- request_end: 2026-08-11T17:20:21.987
- request_duration_ms: 50988
- success: True
- final_source: generation

