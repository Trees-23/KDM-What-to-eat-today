# RAG Process

audit_id: 20260811_174107_793_a65dbbc3
timestamp: 2026-08-11T17:41:07.795
## Request
- original_query: 有大白菜可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: bb1966b4a52e5e32
- session_id: 2026-08-12-真实考试-001:old:S04-B-10
- request_mode: stream
- request_start: 2026-08-11T17:41:07.795
- evaluation_sample_id: 20260811_174107_793_a65dbbc3
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:41:07.796
- end: 2026-08-11T17:41:07.796
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:41:07.796
- end: 2026-08-11T17:41:07.796
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: bb1966b4a52e5e32

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:41:07.796
- end: 2026-08-11T17:41:07.796
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: bb1966b4a52e5e32
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:41:07.796
- end: 2026-08-11T17:41:14.952
- duration_ms: 7156
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.5
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询的核心实体是“大白菜”，目标是检索可制作的菜品及明确在配料表中包含大白菜的菜谱。虽然涉及“大白菜—菜品—菜谱配料”的包含关系和结果核验，但不需要多跳推理、因果分析或复杂关系网络建模。适合通过关键词检索、菜谱字段过滤（配料包含大白菜）、全文检索与语义召回来获取候选菜谱，再依据配料表进行精确验证，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 108, 'graph_rag_count': 1, 'total_queries': 109}
- route_stats_after: {'traditional_count': 109, 'graph_rag_count': 1, 'total_queries': 110}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['大白菜', '白菜炖豆腐', '醋溜白菜', '白菜炒肉', '白菜粉丝煲', '白菜饺子', '白菜汤']
- topic_keywords: ['家常菜', '素菜', '快手菜', '下饭菜', '菜谱']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4317

## Hybrid Branch Status / entity_level
- keywords: ['大白菜', '白菜炖豆腐', '醋溜白菜', '白菜炒肉', '白菜粉丝煲', '白菜饺子', '白菜汤']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 10

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '素菜', '快手菜', '下饭菜', '菜谱']
- requested_k: 10
- actual_count: 10
- fallback_count: 9
- duration_ms: 35

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 519

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 10
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 17
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 8
- doc_names: ['揭秘食材搭配的智慧：这些食物不宜同食', '如何决策吃什么']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 18
- duration_ms: 15131
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 1, 'Ingredient': 1, '烹饪技巧': 1, '素菜': 1, '通用知识': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 19988
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:41:07.796
- end: 2026-08-11T17:41:34.943
- duration_ms: 27146
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3674
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
- chunk_count: 323
- redacted_field: 4501
- total_duration_ms: 11858
- fallback_used: False

## Final Output
- answer_chars: 423
- answer_hash: aa46adb88729e88c
- success: True

## Request Complete
- request_end: 2026-08-11T17:41:46.815
- request_duration_ms: 39020
- success: True
- final_source: generation

