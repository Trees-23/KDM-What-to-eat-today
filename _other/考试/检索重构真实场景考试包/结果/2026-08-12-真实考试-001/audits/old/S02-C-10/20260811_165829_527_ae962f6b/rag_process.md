# RAG Process

audit_id: 20260811_165829_527_ae962f6b
timestamp: 2026-08-11T16:58:29.532
## Request
- original_query: 只回答戚风蛋糕的第 1 步，并说明它来自哪一条菜谱步骤；不要混入后续步骤。
- original_query_hash: d862a71f32aa862b
- session_id: 2026-08-12-真实考试-001:old:S02-C-10
- request_mode: stream
- request_start: 2026-08-11T16:58:29.533
- evaluation_sample_id: 20260811_165829_527_ae962f6b
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:58:29.534
- end: 2026-08-11T16:58:29.534
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:58:29.534
- end: 2026-08-11T16:58:29.534
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 37
- enhanced_query_length: 37
- enhanced_query_hash: d862a71f32aa862b

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:58:29.535
- end: 2026-08-11T16:58:29.535
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 37
- analysis_input_query_hash: d862a71f32aa862b
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:58:29.535
- end: 2026-08-11T16:58:44.732
- duration_ms: 15196
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.4
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 该查询是对“戚风蛋糕”菜谱中的指定序号步骤（第1步）进行精确定位与受约束抽取，并要求标注其来源步骤、排除后续步骤内容。它不需要多跳推理、因果分析或对比分析，核心是基于菜谱文本的实体匹配、步骤序号过滤和片段级返回。虽然包含“菜谱—步骤—第1步”的轻量关系，但关系网络不复杂，适合使用 hybrid_traditional 进行关键词检索、字段/序号过滤及原文片段抽取。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 59, 'graph_rag_count': 0, 'total_queries': 59}
- route_stats_after: {'traditional_count': 60, 'graph_rag_count': 0, 'total_queries': 60}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['戚风蛋糕', '菜谱步骤']
- topic_keywords: ['烘焙', '步骤定位', '菜谱溯源', '步骤边界']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4260

## Hybrid Branch Status / topic_level
- keywords: ['烘焙', '步骤定位', '菜谱溯源', '步骤边界']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 4

## Hybrid Branch Status / entity_level
- keywords: ['戚风蛋糕', '菜谱步骤']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 17

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 384

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 0
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 9
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 10
- duration_ms: 13322
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'甜品': 2, '烹饪技巧': 1, '主食': 1, '早餐': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 燕麦鸡蛋饼
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18015
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:58:29.535
- end: 2026-08-11T16:59:02.748
- duration_ms: 33213
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4706
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
- chunk_count: 97
- redacted_field: 4081
- total_duration_ms: 5985
- fallback_used: False

## Final Output
- answer_chars: 128
- answer_hash: 74bd51d90f6e66f8
- success: True

## Request Complete
- request_end: 2026-08-11T16:59:08.796
- request_duration_ms: 39263
- success: True
- final_source: generation

