# RAG Process

audit_id: 20260811_161824_408_e4c73bdf
timestamp: 2026-08-11T16:18:24.408
## Request
- original_query: 请给出糖醋鲤鱼的完整做法，包括主要食材和步骤。
- original_query_hash: 4033029c0d78d10e
- session_id: 2026-08-12-真实考试-001:old:S01-A-04
- request_mode: stream
- request_start: 2026-08-11T16:18:24.408
- evaluation_sample_id: 20260811_161824_408_e4c73bdf
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:18:24.409
- end: 2026-08-11T16:18:24.409
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:18:24.409
- end: 2026-08-11T16:18:24.409
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: 4033029c0d78d10e

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:18:24.410
- end: 2026-08-11T16:18:24.410
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: 4033029c0d78d10e
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:18:24.410
- end: 2026-08-11T16:18:29.976
- duration_ms: 5565
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是针对单一道菜“糖醋鲤鱼”的明确做法检索，目标是获取主要食材和标准烹饪步骤。虽然食材、调料与步骤之间存在顺序搭配关系，但属于线性流程信息，不需要跨实体、多跳关系推理、因果分析或方案对比。适合通过关键词检索、菜谱文档召回与语义匹配进行回答，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 3, 'graph_rag_count': 0, 'total_queries': 3}
- route_stats_after: {'traditional_count': 4, 'graph_rag_count': 0, 'total_queries': 4}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['糖醋鲤鱼', '鲤鱼', '糖', '醋', '葱', '姜', '蒜', '料酒', '淀粉', '食用油']
- topic_keywords: ['鲁菜', '糖醋味', '家常菜', '宴客菜', '烹饪步骤', '油炸', '挂汁', '火候']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3731

## Hybrid Branch Status / entity_level
- keywords: ['糖醋鲤鱼', '鲤鱼', '糖', '醋', '葱', '姜', '蒜', '料酒', '淀粉', '食用油']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 46

## Hybrid Branch Status / topic_level
- keywords: ['鲁菜', '糖醋味', '家常菜', '宴客菜', '烹饪步骤', '油炸', '挂汁', '火候']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 73

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 576

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
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 27
- duration_ms: 23433
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, 'Ingredient': 2, '汤类': 1}
- deferred_count: 6
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 27758
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:18:24.410
- end: 2026-08-11T16:18:57.736
- duration_ms: 33325
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2664
- retrieval_levels: ['', 'entity']
- search_types: ['entity_level', 'vector_enhanced']
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
- chunk_count: 718
- redacted_field: 6163
- total_duration_ms: 20238
- fallback_used: False

## Final Output
- answer_chars: 930
- answer_hash: a29e8aa38e585757
- success: True

## Request Complete
- request_end: 2026-08-11T16:19:17.999
- request_duration_ms: 53590
- success: True
- final_source: generation

