# RAG Process

audit_id: 20260811_193310_184_0cfc0a96
timestamp: 2026-08-11T19:33:10.184
## Request
- original_query: 请给出微波葱姜黑鳕鱼的完整做法，包括主要食材和步骤。
- original_query_hash: fb57f45973a89b36
- session_id: 2026-08-12-真实考试-001:new:S01-A-09
- request_mode: stream
- request_start: 2026-08-11T19:33:10.184
- evaluation_sample_id: 20260811_193310_184_0cfc0a96
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:33:10.185
- end: 2026-08-11T19:33:10.185
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:33:10.185
- end: 2026-08-11T19:33:10.185
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: fb57f45973a89b36

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:33:10.195
- end: 2026-08-11T19:33:10.195
- duration_ms: 0
- entity_id: 201000023
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:33:10.195
- end: 2026-08-11T19:33:10.195
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:33:10.195
- end: 2026-08-11T19:33:10.195
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: fb57f45973a89b36
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:33:10.195
- end: 2026-08-11T19:33:24.574
- duration_ms: 14378
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.3
- reasoning_required: False
- entity_count: 4
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是针对特定菜品“微波葱姜黑鳕鱼”的直接做法检索，核心目标是获取主要食材清单与线性烹饪步骤。明确实体包括微波炉、葱、姜和黑鳕鱼（亦可将菜名视为复合菜品实体）。查询不要求多跳推理、因果解释或不同做法的对比分析，适合通过关键词、菜谱标题、食材字段及步骤文本进行混合检索。

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
- topic_keywords: ['微波烹饪', '快手菜', '蒸鱼', '去腥', '调味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3238

## Hybrid Branch Status / topic_level
- keywords: ['微波烹饪', '快手菜', '蒸鱼', '去腥', '调味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 95

## Hybrid Branch Status / entity_level
- keywords: ['微波葱姜黑鳕鱼', '黑鳕鱼', '葱', '姜', '微波炉']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 208

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 476

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
- duration_ms: 28082
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '烹饪技巧': 1, 'TechniqueChunk': 1, 'TechniqueDoc': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 31881
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:33:10.195
- end: 2026-08-11T19:33:56.456
- duration_ms: 46260
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
- chunk_count: 449
- redacted_field: 4298
- total_duration_ms: 13318
- fallback_used: False

## Final Output
- answer_chars: 591
- answer_hash: 3d3fe2cc182a6d77
- success: True

## Request Complete
- request_end: 2026-08-11T19:34:09.790
- request_duration_ms: 59605
- success: True
- final_source: generation

