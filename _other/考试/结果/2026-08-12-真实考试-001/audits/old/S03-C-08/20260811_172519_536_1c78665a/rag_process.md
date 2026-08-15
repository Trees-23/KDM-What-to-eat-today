# RAG Process

audit_id: 20260811_172519_536_1c78665a
timestamp: 2026-08-11T17:25:19.537
## Request
- original_query: 只根据“厨房准备”技巧章节的关键要点回答；资料没有说明的结论请明确保留。
- original_query_hash: ba9d44a0b7cf09cf
- session_id: 2026-08-12-真实考试-001:old:S03-C-08
- request_mode: stream
- request_start: 2026-08-11T17:25:19.537
- evaluation_sample_id: 20260811_172519_536_1c78665a
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:25:19.539
- end: 2026-08-11T17:25:19.539
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:25:19.540
- end: 2026-08-11T17:25:19.540
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: ba9d44a0b7cf09cf

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:25:19.541
- end: 2026-08-11T17:25:19.541
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: ba9d44a0b7cf09cf
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:25:19.541
- end: 2026-08-11T17:25:28.241
- duration_ms: 8699
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询的核心是对指定资料范围进行受限检索与忠实回答：仅依据“厨房准备”技巧章节的关键要点，并对资料未覆盖的内容明确保留。它不要求跨实体关系挖掘、多跳推理、因果分析或对比分析，重点在于章节定位、关键要点提取和证据边界控制。明确实体包括“厨房准备”技巧章节、“关键要点”和“资料”。因此适合采用基于关键词、章节元数据过滤及语义匹配的 hybrid_traditional 检索策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 86, 'graph_rag_count': 1, 'total_queries': 87}
- route_stats_after: {'traditional_count': 87, 'graph_rag_count': 1, 'total_queries': 88}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['厨房准备', '厨房准备技巧章节']
- topic_keywords: ['烹饪技巧', '关键要点', '资料依据', '信息保留', '结论范围']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4568

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '关键要点', '资料依据', '信息保留', '结论范围']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 13

## Hybrid Branch Status / entity_level
- keywords: ['厨房准备', '厨房准备技巧章节']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 60

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 733

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 0
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 14
- duplicate_count: 6

## Hybrid Technique Expansion
- enabled: True
- seed_count: 13
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 15
- duration_ms: 17172
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 1, 'TechniqueChunk': 2, '烹饪技巧': 2}
- deferred_count: 7
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 凉拌
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22539
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:25:19.541
- end: 2026-08-11T17:25:50.782
- duration_ms: 31240
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 6503
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
- chunk_count: 33
- redacted_field: 2909
- total_duration_ms: 3540
- fallback_used: False

## Final Output
- answer_chars: 52
- answer_hash: 65236d4ec05d153a
- success: True

## Request Complete
- request_end: 2026-08-11T17:25:54.367
- request_duration_ms: 34829
- success: True
- final_source: generation

