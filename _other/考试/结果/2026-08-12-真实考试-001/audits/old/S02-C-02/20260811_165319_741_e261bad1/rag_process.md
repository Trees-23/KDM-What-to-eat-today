# RAG Process

audit_id: 20260811_165319_741_e261bad1
timestamp: 2026-08-11T16:53:19.742
## Request
- original_query: 只回答电饭煲三文鱼炊饭的第 1 步，并说明它来自哪一条菜谱步骤；不要混入后续步骤。
- original_query_hash: 8ba1014665c63da6
- session_id: 2026-08-12-真实考试-001:old:S02-C-02
- request_mode: stream
- request_start: 2026-08-11T16:53:19.742
- evaluation_sample_id: 20260811_165319_741_e261bad1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:53:19.743
- end: 2026-08-11T16:53:19.743
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:53:19.744
- end: 2026-08-11T16:53:19.744
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 41
- enhanced_query_length: 41
- enhanced_query_hash: 8ba1014665c63da6

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:53:19.745
- end: 2026-08-11T16:53:19.745
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 41
- analysis_input_query_hash: 8ba1014665c63da6
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:53:19.745
- end: 2026-08-11T16:53:29.201
- duration_ms: 9455
- analysis_mode: llm
- query_complexity: 0.42
- relationship_intensity: 0.38
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询的核心是对特定菜谱“电饭煲三文鱼炊饭”进行精确步骤定位：仅检索并返回第1步，同时标明该内容所属的菜谱步骤，且通过步骤序号过滤避免引入第2步及之后的信息。它不需要复杂的实体关系扩展、因果推断或跨文档多跳推理，但需要具备结构化字段过滤、步骤排序和来源追溯能力。因此适合使用 hybrid_traditional，通过关键词/语义检索定位目标菜谱，并依据步骤编号进行精确筛选与引用。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 51, 'graph_rag_count': 0, 'total_queries': 51}
- route_stats_after: {'traditional_count': 52, 'graph_rag_count': 0, 'total_queries': 52}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['电饭煲三文鱼炊饭', '电饭煲', '三文鱼', '菜谱步骤']
- topic_keywords: ['炊饭', '菜谱步骤', '步骤顺序', '烹饪流程']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4068

## Hybrid Branch Status / topic_level
- keywords: ['炊饭', '菜谱步骤', '步骤顺序', '烹饪流程']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 5

## Hybrid Branch Status / entity_level
- keywords: ['电饭煲三文鱼炊饭', '电饭煲', '三文鱼', '菜谱步骤']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 16

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 514

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 0
- vector_count: 10
- origin_len: 12

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 12
- after_count: 11
- duplicate_count: 1

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['炒/煎', '蒸（米）/炖（使用电饭煲/高压锅/电压力锅）']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 12
- duration_ms: 17417
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '水产': 2, '汤类': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 皮蛋瘦肉粥
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22030
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:53:19.745
- end: 2026-08-11T16:53:51.232
- duration_ms: 31486
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4081
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
- chunk_count: 55
- redacted_field: 8821
- total_duration_ms: 10223
- fallback_used: False

## Final Output
- answer_chars: 69
- answer_hash: cb3656a608acca4e
- success: True

## Request Complete
- request_end: 2026-08-11T16:54:01.482
- request_duration_ms: 41740
- success: True
- final_source: generation

