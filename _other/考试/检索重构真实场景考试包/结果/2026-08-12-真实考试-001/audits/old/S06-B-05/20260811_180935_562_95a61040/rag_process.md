# RAG Process

audit_id: 20260811_180935_562_95a61040
timestamp: 2026-08-11T18:09:35.564
## Request
- original_query: 想做一道清蒸类菜，帮我找几个贴近这个需求的做法。
- original_query_hash: cdacbce4d0cee940
- session_id: 2026-08-12-真实考试-001:old:S06-B-05
- request_mode: stream
- request_start: 2026-08-11T18:09:35.564
- evaluation_sample_id: 20260811_180935_562_95a61040
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:09:35.566
- end: 2026-08-11T18:09:35.566
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:09:35.566
- end: 2026-08-11T18:09:35.566
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 24
- enhanced_query_length: 24
- enhanced_query_hash: cdacbce4d0cee940

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:09:35.568
- end: 2026-08-11T18:09:35.568
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 24
- analysis_input_query_hash: cdacbce4d0cee940
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:09:35.568
- end: 2026-08-11T18:09:42.977
- duration_ms: 7408
- analysis_mode: llm
- query_complexity: 0.42
- relationship_intensity: 0.28
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询目标明确：寻找若干与“清蒸”烹饪方式贴近的菜品做法。核心实体为“清蒸类菜”，属于烹饪技法/菜品类别实体；未指定食材、地域、口味、难度或设备等额外约束。该需求主要依赖关键词匹配、语义召回和结果排序/适度多样化即可满足，不需要多跳推理、因果分析或复杂关系网络建模，因此推荐使用 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 131, 'graph_rag_count': 33, 'total_queries': 164}
- route_stats_after: {'traditional_count': 132, 'graph_rag_count': 33, 'total_queries': 165}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['清蒸鱼', '清蒸鸡', '清蒸排骨', '清蒸虾', '清蒸豆腐', '蒸锅']
- topic_keywords: ['清蒸', '蒸菜', '清淡', '健康', '少油', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7820

## Hybrid Branch Status / topic_level
- keywords: ['清蒸', '蒸菜', '清淡', '健康', '少油', '家常菜']
- requested_k: 10
- actual_count: 4
- fallback_count: 4
- duration_ms: 28

## Hybrid Branch Status / entity_level
- keywords: ['清蒸鱼', '清蒸鸡', '清蒸排骨', '清蒸虾', '清蒸豆腐', '蒸锅']
- requested_k: 10
- actual_count: 5
- fallback_count: 0
- duration_ms: 53

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 492

## Hybrid Branch Summary
- entity_count: 5
- topic_count: 4
- vector_count: 10
- origin_len: 19

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 19
- after_count: 17
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 6
- expanded_count: 9
- doc_names: ['蒸', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 18
- duration_ms: 17226
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 1, '主食': 1, 'TechniqueDoc': 1, '烹饪技巧': 1, '素菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25587
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:09:35.568
- end: 2026-08-11T18:10:08.565
- duration_ms: 32997
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2820
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
- chunk_count: 1
- redacted_field: 14417
- total_duration_ms: 14418
- fallback_used: False

## Final Output
- answer_chars: 741
- answer_hash: 6d5b99aea9501cbe
- success: True

## Request Complete
- request_end: 2026-08-11T18:10:22.998
- request_duration_ms: 47434
- success: True
- final_source: generation

