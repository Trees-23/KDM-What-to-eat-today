# RAG Process

audit_id: 20260811_162504_754_0a1dfcba
timestamp: 2026-08-11T16:25:04.755
## Request
- original_query: 地三鲜从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: b68065d12930e3fa
- session_id: 2026-08-12-真实考试-001:old:S01-B-02
- request_mode: stream
- request_start: 2026-08-11T16:25:04.756
- evaluation_sample_id: 20260811_162504_754_0a1dfcba
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:25:04.757
- end: 2026-08-11T16:25:04.757
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:25:04.757
- end: 2026-08-11T16:25:04.757
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 25
- enhanced_query_length: 25
- enhanced_query_hash: b68065d12930e3fa

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:25:04.758
- end: 2026-08-11T16:25:04.758
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 25
- analysis_input_query_hash: b68065d12930e3fa
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:25:04.758
- end: 2026-08-11T16:25:11.134
- duration_ms: 6375
- analysis_mode: llm
- query_complexity: 0.28
- relationship_intensity: 0.22
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询是针对单一道菜“地三鲜”的流程型做法检索，核心需求是从知识库中定位与整合备料、预处理、烹饪和出锅步骤。虽包含“备料到出锅”的顺序约束，但不涉及跨主题、多实体关系网络、因果归因或方案对比，因此无需多跳推理、因果分析或对比分析。明确实体主要为“地三鲜”和“知识库中的做法（菜谱/烹饪流程）”。建议使用 hybrid_traditional，通过关键词匹配、菜名别名召回及语义检索定位权威菜谱内容，再按步骤顺序输出。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 11, 'graph_rag_count': 0, 'total_queries': 11}
- route_stats_after: {'traditional_count': 12, 'graph_rag_count': 0, 'total_queries': 12}

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
- duration_ms: 4531

## Hybrid Branch Status / entity_level
- keywords: ['地三鲜', '茄子', '土豆', '青椒', '炒锅']
- requested_k: 10
- actual_count: 4
- fallback_count: 0
- duration_ms: 64

## Hybrid Branch Status / topic_level
- keywords: ['东北菜', '家常菜', '下饭菜', '烹饪技巧', '火候', '调味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 80

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 644

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
- duration_ms: 19621
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
- hybrid_total_duration_ms: 24836
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:25:04.758
- end: 2026-08-11T16:25:35.971
- duration_ms: 31212
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
- chunk_count: 530
- redacted_field: 5575
- total_duration_ms: 15445
- fallback_used: False

## Final Output
- answer_chars: 698
- answer_hash: 61bbdf113a6ce76e
- success: True

## Request Complete
- request_end: 2026-08-11T16:25:51.443
- request_duration_ms: 46686
- success: True
- final_source: generation

