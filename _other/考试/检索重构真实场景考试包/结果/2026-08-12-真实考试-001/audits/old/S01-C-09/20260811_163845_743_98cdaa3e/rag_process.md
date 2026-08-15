# RAG Process

audit_id: 20260811_163845_743_98cdaa3e
timestamp: 2026-08-11T16:38:45.744
## Request
- original_query: 我只要知识库能证明的麻婆豆腐做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 919b2a12d98744e3
- session_id: 2026-08-12-真实考试-001:old:S01-C-09
- request_mode: stream
- request_start: 2026-08-11T16:38:45.745
- evaluation_sample_id: 20260811_163845_743_98cdaa3e
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:38:45.745
- end: 2026-08-11T16:38:45.745
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:38:45.746
- end: 2026-08-11T16:38:45.746
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: 919b2a12d98744e3

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:38:45.746
- end: 2026-08-11T16:38:45.746
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 35
- analysis_input_query_hash: 919b2a12d98744e3
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:38:45.746
- end: 2026-08-11T16:38:59.833
- duration_ms: 14087
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.25
- reasoning_required: True
- entity_count: 4
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 查询核心是从知识库中检索“麻婆豆腐做法”的可引用证据，并施加严格的答案生成约束：仅输出可被检索文档证明的内容，排除未引用的替代方案和营养结论。该任务不涉及复杂实体关系网络、跨领域关联或因果推理，但需要进行来源对齐、证据筛选与引用覆盖校验。明确实体/概念包括“知识库”“麻婆豆腐做法”“替代方案”“营养结论”。适合采用 hybrid_traditional，通过关键词/向量混合检索召回菜谱与做法文档，再按引用证据过滤生成结果。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 28, 'graph_rag_count': 0, 'total_queries': 28}
- route_stats_after: {'traditional_count': 29, 'graph_rag_count': 0, 'total_queries': 29}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['麻婆豆腐']
- topic_keywords: ['川菜', '烹饪做法', '知识库证据', '引用依据']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3222

## Hybrid Branch Status / entity_level
- keywords: ['麻婆豆腐']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 25

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '烹饪做法', '知识库证据', '引用依据']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 69

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 369

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 10
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 20
- duplicate_count: 1

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 9
- doc_names: ['凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 21
- duration_ms: 14910
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 1, '主食': 2, '烹饪技巧': 1, '素菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 韭菜盒子
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18555
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:38:45.746
- end: 2026-08-11T16:39:18.390
- duration_ms: 32643
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1751
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
- chunk_count: 218
- redacted_field: 8516
- total_duration_ms: 14080
- fallback_used: False

## Final Output
- answer_chars: 307
- answer_hash: 166889b68b49a073
- success: True

## Request Complete
- request_end: 2026-08-11T16:39:32.493
- request_duration_ms: 46748
- success: True
- final_source: generation

