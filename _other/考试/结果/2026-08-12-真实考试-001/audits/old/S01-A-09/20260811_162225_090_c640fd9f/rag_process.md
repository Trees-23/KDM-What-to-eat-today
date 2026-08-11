# RAG Process

audit_id: 20260811_162225_090_c640fd9f
timestamp: 2026-08-11T16:22:25.092
## Request
- original_query: 请给出微波葱姜黑鳕鱼的完整做法，包括主要食材和步骤。
- original_query_hash: fb57f45973a89b36
- session_id: 2026-08-12-真实考试-001:old:S01-A-09
- request_mode: stream
- request_start: 2026-08-11T16:22:25.092
- evaluation_sample_id: 20260811_162225_090_c640fd9f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:22:25.092
- end: 2026-08-11T16:22:25.092
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:22:25.093
- end: 2026-08-11T16:22:25.093
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: fb57f45973a89b36

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:22:25.093
- end: 2026-08-11T16:22:25.093
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: fb57f45973a89b36
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:22:25.093
- end: 2026-08-11T16:22:40.163
- duration_ms: 15069
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.3
- reasoning_required: False
- entity_count: 4
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询属于针对特定菜品“微波葱姜黑鳕鱼”的直接做法检索，目标明确，需要返回主要食材及顺序化烹饪步骤。查询中可识别的实体包括微波炉（烹饪设备/方式）、葱（食材）、姜（食材）和黑鳕鱼（主食材）。虽然存在食材、烹饪方式与步骤之间的基础关联，但不需要多跳知识推理、因果分析或方案对比，因此适合使用hybrid_traditional进行关键词、菜谱标题和语义内容检索。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 8, 'graph_rag_count': 0, 'total_queries': 8}
- route_stats_after: {'traditional_count': 9, 'graph_rag_count': 0, 'total_queries': 9}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['微波葱姜黑鳕鱼', '黑鳕鱼', '葱', '姜', '微波炉']
- topic_keywords: ['快手菜', '微波烹饪', '蒸鱼', '去腥', '鲜嫩', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3552

## Hybrid Branch Status / topic_level
- keywords: ['快手菜', '微波烹饪', '蒸鱼', '去腥', '鲜嫩', '家常菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 76

## Hybrid Branch Status / entity_level
- keywords: ['微波葱姜黑鳕鱼', '黑鳕鱼', '葱', '姜', '微波炉']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 119

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 480

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 27
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 6
- expanded_count: 9
- doc_names: ['使用微波炉', '厨房准备']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 28
- duration_ms: 27144
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '烹饪技巧': 1, 'TechniqueChunk': 1, 'TechniqueDoc': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 31221
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:22:25.093
- end: 2026-08-11T16:23:11.386
- duration_ms: 46292
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 5865
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
- chunk_count: 474
- redacted_field: 6942
- total_duration_ms: 19670
- fallback_used: False

## Final Output
- answer_chars: 611
- answer_hash: eb15809a08fa6bf8
- success: True

## Request Complete
- request_end: 2026-08-11T16:23:31.075
- request_duration_ms: 65983
- success: True
- final_source: generation

