# RAG Process

audit_id: 20260811_162551_454_851619c2
timestamp: 2026-08-11T16:25:51.465
## Request
- original_query: 蒜蓉西兰花从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 0198f01ff5511d68
- session_id: 2026-08-12-真实考试-001:old:S01-B-03
- request_mode: stream
- request_start: 2026-08-11T16:25:51.466
- evaluation_sample_id: 20260811_162551_454_851619c2
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:25:51.467
- end: 2026-08-11T16:25:51.467
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:25:51.468
- end: 2026-08-11T16:25:51.468
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: 0198f01ff5511d68

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:25:51.469
- end: 2026-08-11T16:25:51.469
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: 0198f01ff5511d68
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:25:51.469
- end: 2026-08-11T16:25:58.199
- duration_ms: 6729
- analysis_mode: llm
- query_complexity: 0.28
- relationship_intensity: 0.22
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询是针对“蒜蓉西兰花”这一具体菜品的顺序化制作流程检索，用户明确要求依据知识库中的做法回答。核心需求是召回与菜品名称、备料、烹饪步骤、出锅要点相关的标准菜谱文本，并按步骤组织输出。虽然包含食材“蒜蓉”和“西兰花”及其烹饪组合关系，但不涉及跨菜品、跨实体的复杂关联挖掘，也不需要多跳推理、因果归因或方案对比。适合采用关键词匹配与语义检索结合的 hybrid_traditional 策略，以准确定位知识库内对应菜谱及步骤信息。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 12, 'graph_rag_count': 0, 'total_queries': 12}
- route_stats_after: {'traditional_count': 13, 'graph_rag_count': 0, 'total_queries': 13}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['蒜蓉西兰花', '西兰花', '大蒜', '焯水']
- topic_keywords: ['家常菜', '素菜', '快手菜', '烹饪技巧', '火候', '调味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 10470

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '素菜', '快手菜', '烹饪技巧', '火候', '调味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 75

## Hybrid Branch Status / entity_level
- keywords: ['蒜蓉西兰花', '西兰花', '大蒜', '焯水']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 182

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 350

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 25
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 7
- expanded_count: 9
- doc_names: ['去腥', '揭秘食材搭配的智慧：这些食物不宜同食']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 26
- duration_ms: 31166
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, 'TechniqueDoc': 1, 'TechniqueChunk': 1, '荤菜': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 蒜苔炒肉末
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 42025
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:25:51.469
- end: 2026-08-11T16:26:40.225
- duration_ms: 48756
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 6708
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
- chunk_count: 371
- redacted_field: 4428
- total_duration_ms: 11781
- fallback_used: False

## Final Output
- answer_chars: 552
- answer_hash: 17322be1994d98ab
- success: True

## Request Complete
- request_end: 2026-08-11T16:26:52.029
- request_duration_ms: 60563
- success: True
- final_source: generation

