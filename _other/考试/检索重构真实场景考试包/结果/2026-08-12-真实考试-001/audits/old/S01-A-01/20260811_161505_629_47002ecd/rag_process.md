# RAG Process

audit_id: 20260811_161505_629_47002ecd
timestamp: 2026-08-11T16:15:05.630
## Request
- original_query: 请给出清蒸鲈鱼的完整做法，包括主要食材和步骤。
- original_query_hash: a5dd296e5aae3d11
- session_id: 2026-08-12-真实考试-001:old:S01-A-01
- request_mode: stream
- request_start: 2026-08-11T16:15:05.630
- evaluation_sample_id: 20260811_161505_629_47002ecd
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:15:05.631
- end: 2026-08-11T16:15:05.631
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:15:05.632
- end: 2026-08-11T16:15:05.632
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: a5dd296e5aae3d11

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:15:05.633
- end: 2026-08-11T16:15:05.633
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: a5dd296e5aae3d11
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:15:05.633
- end: 2026-08-11T16:15:16.434
- duration_ms: 10800
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是面向单一道菜“清蒸鲈鱼”的直接做法查询，目标明确：获取主要食材及按顺序执行的烹饪步骤。虽然涉及“鲈鱼”和“清蒸”两个明确实体/概念，且步骤中存在食材与操作的基础关联，但不需要跨文档、多跳知识推理，也不涉及因果分析或方案对比。适合采用关键词检索结合向量检索的 hybrid_traditional 策略，召回标准菜谱、食材清单、处理方法、蒸制时间等结构化或非结构化内容。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 0, 'graph_rag_count': 0, 'total_queries': 0}
- route_stats_after: {'traditional_count': 1, 'graph_rag_count': 0, 'total_queries': 1}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['清蒸鲈鱼', '鲈鱼', '姜', '葱', '蒸鱼豉油', '食用油', '蒸锅']
- topic_keywords: ['清蒸', '蒸菜', '家常菜', '海鲜', '去腥', '火候', '烹饪步骤']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6329

## Hybrid Branch Status / entity_level
- keywords: ['清蒸鲈鱼', '鲈鱼', '姜', '葱', '蒸鱼豉油', '食用油', '蒸锅']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 423

## Hybrid Branch Status / topic_level
- keywords: ['清蒸', '蒸菜', '家常菜', '海鲜', '去腥', '火候', '烹饪步骤']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 470

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 524

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 26
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 4
- expanded_count: 5
- doc_names: ['蒸']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 27
- duration_ms: 44749
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '荤菜': 2, '汤类': 1}
- deferred_count: 4
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 奶酪培根通心粉
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 51790
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:15:05.633
- end: 2026-08-11T16:16:08.226
- duration_ms: 62593
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3353
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
- chunk_count: 433
- redacted_field: 3711
- total_duration_ms: 13581
- fallback_used: False

## Final Output
- answer_chars: 566
- answer_hash: 0be636ef1fc529e5
- success: True

## Request Complete
- request_end: 2026-08-11T16:16:21.891
- request_duration_ms: 76260
- success: True
- final_source: generation

