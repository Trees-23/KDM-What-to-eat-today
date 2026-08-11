# RAG Process

audit_id: 20260811_180713_002_f3ce36b8
timestamp: 2026-08-11T18:07:13.003
## Request
- original_query: 想做不需要很多工具的早餐，帮我找几个贴近这个需求的做法。
- original_query_hash: 1437e76e058be470
- session_id: 2026-08-12-真实考试-001:old:S06-B-02
- request_mode: stream
- request_start: 2026-08-11T18:07:13.003
- evaluation_sample_id: 20260811_180713_002_f3ce36b8
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:07:13.006
- end: 2026-08-11T18:07:13.006
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:07:13.006
- end: 2026-08-11T18:07:13.006
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 28
- enhanced_query_length: 28
- enhanced_query_hash: 1437e76e058be470

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:07:13.007
- end: 2026-08-11T18:07:13.007
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 28
- analysis_input_query_hash: 1437e76e058be470
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:07:13.007
- end: 2026-08-11T18:07:21.464
- duration_ms: 8456
- analysis_mode: llm
- query_complexity: 0.48
- relationship_intensity: 0.42
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询的核心目标是检索并筛选符合“早餐”和“所需工具少”两个条件的做法。它需要对候选食谱进行轻量级约束匹配与横向比较，例如比较不同做法所需的厨具数量、操作步骤和早餐适用性，但不涉及复杂的多实体关系网络或知识发现。无需多跳推理和因果分析，存在基础的对比分析需求。明确实体主要为“早餐”和“工具”，其中“工具少”属于对食谱制作条件的约束。因此更适合使用 hybrid_traditional，通过关键词检索、语义召回和基于工具数量等字段的过滤/排序来返回结果。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 128, 'graph_rag_count': 33, 'total_queries': 161}
- route_stats_after: {'traditional_count': 129, 'graph_rag_count': 33, 'total_queries': 162}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鸡蛋', '吐司', '燕麦', '牛奶', '酸奶', '香蕉', '平底锅', '微波炉', '电饭煲']
- topic_keywords: ['早餐', '简单早餐', '快手菜', '少工具烹饪', '便捷烹饪']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8731

## Hybrid Branch Status / topic_level
- keywords: ['早餐', '简单早餐', '快手菜', '少工具烹饪', '便捷烹饪']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 73

## Hybrid Branch Status / entity_level
- keywords: ['鸡蛋', '吐司', '燕麦', '牛奶', '酸奶', '香蕉', '平底锅', '微波炉', '电饭煲']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 139

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 405

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 28
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 6
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 29
- duration_ms: 23971
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'早餐': 2, 'TechniqueDoc': 1, '主食': 2}
- deferred_count: 5
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 蛋包饭
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 33178
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:07:13.007
- end: 2026-08-11T18:07:54.643
- duration_ms: 41636
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 5553
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
- chunk_count: 624
- redacted_field: 6660
- total_duration_ms: 18979
- fallback_used: False

## Final Output
- answer_chars: 851
- answer_hash: 16598724d16cacfc
- success: True

## Request Complete
- request_end: 2026-08-11T18:08:13.647
- request_duration_ms: 60643
- success: True
- final_source: generation

