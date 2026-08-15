# RAG Process

audit_id: 20260811_170017_293_e1a864d0
timestamp: 2026-08-11T17:00:17.298
## Request
- original_query: 请说明“做菜专业术语”这个技巧的关键要点和适用情形。
- original_query_hash: ace57f005f71a6d6
- session_id: 2026-08-12-真实考试-001:old:S03-A-02
- request_mode: stream
- request_start: 2026-08-11T17:00:17.298
- evaluation_sample_id: 20260811_170017_293_e1a864d0
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:00:17.298
- end: 2026-08-11T17:00:17.298
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:00:17.299
- end: 2026-08-11T17:00:17.299
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: ace57f005f71a6d6

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:00:17.299
- end: 2026-08-11T17:00:17.299
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: ace57f005f71a6d6
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:00:17.299
- end: 2026-08-11T17:00:24.559
- duration_ms: 7259
- analysis_mode: llm
- query_complexity: 0.48
- relationship_intensity: 0.32
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心实体为“做菜专业术语”，要求说明其关键要点和适用情形，属于对单一主题的定义、分类与场景化说明。需要进行轻量级的归纳推理，将术语按烹饪环节或技法分类，并将其映射到相应菜品、食材或操作场景；但不涉及多个实体之间的复杂关系网络、多跳知识发现或深层因果链分析。因此更适合采用 hybrid_traditional，通过关键词检索、术语词典/菜谱资料召回及语义排序获取答案。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 61, 'graph_rag_count': 0, 'total_queries': 61}
- route_stats_after: {'traditional_count': 62, 'graph_rag_count': 0, 'total_queries': 62}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['做菜专业术语']
- topic_keywords: ['烹饪技巧', '烹饪术语', '关键要点', '适用情形', '火候', '调味', '刀工', '烹饪方法']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5039

## Hybrid Branch Status / entity_level
- keywords: ['做菜专业术语']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 36

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '烹饪术语', '关键要点', '适用情形', '火候', '调味', '刀工', '烹饪方法']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 87

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 550

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 10
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 16
- duplicate_count: 5

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
- candidate_count: 17
- duration_ms: 16659
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'高级技巧': 1, '烹饪技巧': 2, '通用知识': 1, '主食': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 意式肉酱面
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22277
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:00:17.299
- end: 2026-08-11T17:00:46.838
- duration_ms: 29538
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 7816
- retrieval_levels: ['', 'context_expansion']
- search_types: ['technique_expansion', 'vector_enhanced']
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
- chunk_count: 2401
- redacted_field: 5260
- total_duration_ms: 53219
- fallback_used: False

## Final Output
- answer_chars: 3039
- answer_hash: 2bf54cdc0dd0d443
- success: True

## Request Complete
- request_end: 2026-08-11T17:01:40.086
- request_duration_ms: 82787
- success: True
- final_source: generation

