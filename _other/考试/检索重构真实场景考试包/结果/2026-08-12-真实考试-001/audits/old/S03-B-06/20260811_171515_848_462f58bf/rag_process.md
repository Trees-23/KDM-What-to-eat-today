# RAG Process

audit_id: 20260811_171515_848_462f58bf
timestamp: 2026-08-11T17:15:15.850
## Request
- original_query: 我想学腌（肉），它的关键要点和适用场景是什么？
- original_query_hash: 9e8392a26d6d12f1
- session_id: 2026-08-12-真实考试-001:old:S03-B-06
- request_mode: stream
- request_start: 2026-08-11T17:15:15.850
- evaluation_sample_id: 20260811_171515_848_462f58bf
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:15:15.851
- end: 2026-08-11T17:15:15.851
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:15:15.851
- end: 2026-08-11T17:15:15.851
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: 9e8392a26d6d12f1

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:15:15.852
- end: 2026-08-11T17:15:15.852
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: 9e8392a26d6d12f1
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:15:15.853
- end: 2026-08-11T17:15:24.139
- duration_ms: 8286
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.48
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 查询的核心是学习“腌制肉类”这一烹饪/保存技术，并了解其关键操作要点及适用场景，属于包含步骤、条件和应用建议的中等复杂度信息需求。需要一定的因果分析，例如盐量、腌制时间、温度与肉质口感、入味程度及食品安全之间的关系；也可能涉及不同肉类或不同用途（如烧烤、煎制、炖煮、保存）下的腌制方式对比。但查询未要求跨多个领域、历史背景或复杂实体网络的多跳推理，因此更适合使用 hybrid_traditional，通过关键词检索结合语义检索获取腌制原理、操作规范、配方比例和场景建议。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 75, 'graph_rag_count': 0, 'total_queries': 75}
- route_stats_after: {'traditional_count': 76, 'graph_rag_count': 0, 'total_queries': 76}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['腌肉', '腌（肉）', '腌制', '腌渍']
- topic_keywords: ['烹饪技巧', '入味', '调味', '食品安全', '炸', '烤', '快炒']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5698

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '入味', '调味', '食品安全', '炸', '烤', '快炒']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 90

## Hybrid Branch Status / entity_level
- keywords: ['腌肉', '腌（肉）', '腌制', '腌渍']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 244

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 559

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 19
- duplicate_count: 11

## Hybrid Technique Expansion
- enabled: True
- seed_count: 9
- expanded_count: 9
- doc_names: ['腌（肉）']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 20
- duration_ms: 23388
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 2, 'TechniqueChunk': 2, '调料': 1}
- deferred_count: 6
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 29693
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:15:15.853
- end: 2026-08-11T17:15:53.833
- duration_ms: 37980
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 6279
- retrieval_levels: ['', 'context_expansion', 'entity', 'topic']
- search_types: ['entity_level', 'technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 1755
- redacted_field: 1756
- total_duration_ms: 35858
- fallback_used: False

## Final Output
- answer_chars: 2193
- answer_hash: e0f9e4d92a96ed1e
- success: True

## Request Complete
- request_end: 2026-08-11T17:16:29.718
- request_duration_ms: 73867
- success: True
- final_source: generation

