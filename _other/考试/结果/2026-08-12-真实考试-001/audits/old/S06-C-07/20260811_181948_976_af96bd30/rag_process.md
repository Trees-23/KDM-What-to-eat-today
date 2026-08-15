# RAG Process

audit_id: 20260811_181948_976_af96bd30
timestamp: 2026-08-11T18:19:48.978
## Request
- original_query: 想做一道煎制的小菜。请展示推荐依据；如果意图无法由资料支持，不要把推测写成事实。
- original_query_hash: b5b452be00f1b9dd
- session_id: 2026-08-12-真实考试-001:old:S06-C-07
- request_mode: stream
- request_start: 2026-08-11T18:19:48.979
- evaluation_sample_id: 20260811_181948_976_af96bd30
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:19:48.980
- end: 2026-08-11T18:19:48.980
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:19:48.981
- end: 2026-08-11T18:19:48.981
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 40
- enhanced_query_length: 40
- enhanced_query_hash: b5b452be00f1b9dd

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:19:48.981
- end: 2026-08-11T18:19:48.981
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 40
- analysis_input_query_hash: b5b452be00f1b9dd
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:19:48.982
- end: 2026-08-11T18:20:03.988
- duration_ms: 15006
- analysis_mode: llm
- query_complexity: 0.52
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 查询的核心意图是检索并推荐一道符合“煎制”“小菜”约束的菜品，同时要求展示推荐依据并严格区分资料事实与未被资料支持的推测。它需要基于菜谱资料进行条件匹配、排序和证据引用，但未指定具体食材、地域菜系或多实体关系网络。可采用关键词检索结合向量检索召回煎制小菜类菜谱，再依据资料中明确出现的烹饪技法、食材、步骤、耗时或口味描述生成可追溯的推荐依据；缺少资料佐证的判断应标记为不确定或不输出。无需多跳推理、因果分析或复杂对比分析，hybrid_traditional更合适。明确实体主要为“煎制”（烹饪技法）和“小菜”（菜品类别）。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 143, 'graph_rag_count': 33, 'total_queries': 176}
- route_stats_after: {'traditional_count': 144, 'graph_rag_count': 33, 'total_queries': 177}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['煎制', '煎']
- topic_keywords: ['小菜', '烹饪技巧', '煎制菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4685

## Hybrid Branch Status / topic_level
- keywords: ['小菜', '烹饪技巧', '煎制菜']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 22

## Hybrid Branch Status / entity_level
- keywords: ['煎制', '煎']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 166

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 587

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 0
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 15
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 12
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 16
- duration_ms: 23098
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 2, '主食': 2, 'TechniqueChunk': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 汤面
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 28434
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:19:48.982
- end: 2026-08-11T18:20:32.424
- duration_ms: 43442
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 7103
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
- chunk_count: 562
- redacted_field: 4129
- total_duration_ms: 15292
- fallback_used: False

## Final Output
- answer_chars: 733
- answer_hash: 12add9f6c5e876d5
- success: True

## Request Complete
- request_end: 2026-08-11T18:20:47.767
- request_duration_ms: 58788
- success: True
- final_source: generation

