# RAG Process

audit_id: 20260811_173552_847_0e4b33fe
timestamp: 2026-08-11T17:35:52.847
## Request
- original_query: 有羊肉可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: 42e8edcebc5ff17f
- session_id: 2026-08-12-真实考试-001:old:S04-B-03
- request_mode: stream
- request_start: 2026-08-11T17:35:52.848
- evaluation_sample_id: 20260811_173552_847_0e4b33fe
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:35:52.848
- end: 2026-08-11T17:35:52.848
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:35:52.849
- end: 2026-08-11T17:35:52.849
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: 42e8edcebc5ff17f

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:35:52.849
- end: 2026-08-11T17:35:52.849
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 20
- analysis_input_query_hash: 42e8edcebc5ff17f
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:35:52.850
- end: 2026-08-11T17:36:07.128
- duration_ms: 14277
- analysis_mode: llm
- query_complexity: 0.48
- relationship_intensity: 0.58
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询的核心实体是“羊肉”（食材实体），目标是检索与其存在“食材-菜谱包含”关系的菜品。除生成可做菜品列表外，还要求确认“哪些菜谱确实包含它”，因此需要对召回结果中的配料表、主料字段或正文进行实体匹配与证据校验。该任务主要是关键词/语义检索结合结构化食材字段过滤，关系较明确但不涉及复杂多跳、因果或跨实体网络推理，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 101, 'graph_rag_count': 1, 'total_queries': 102}
- route_stats_after: {'traditional_count': 102, 'graph_rag_count': 1, 'total_queries': 103}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['羊肉', '羊肉串', '孜然羊肉', '葱爆羊肉', '红烧羊肉', '羊肉汤', '羊肉炖萝卜', '羊肉火锅', '羊肉抓饭', '羊肉饺子']
- topic_keywords: ['羊肉菜谱', '家常菜', '炖菜', '烧烤', '火锅', '汤品', '西北菜', '清真菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5417

## Hybrid Branch Status / entity_level
- keywords: ['羊肉', '羊肉串', '孜然羊肉', '葱爆羊肉', '红烧羊肉', '羊肉汤', '羊肉炖萝卜', '羊肉火锅', '羊肉抓饭', '羊肉饺子']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 35

## Hybrid Branch Status / topic_level
- keywords: ['羊肉菜谱', '家常菜', '炖菜', '烧烤', '火锅', '汤品', '西北菜', '清真菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 62

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 446

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 10
- vector_count: 10
- origin_len: 22

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 22
- after_count: 17
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['如何决策吃什么', '腌（肉）']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 18
- duration_ms: 16737
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '烹饪技巧': 1, '汤类': 1, '通用知识': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22621
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:35:52.850
- end: 2026-08-11T17:36:29.751
- duration_ms: 36900
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3778
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
- chunk_count: 348
- redacted_field: 5189
- total_duration_ms: 11014
- fallback_used: False

## Final Output
- answer_chars: 429
- answer_hash: 0d5a02af0065a5ca
- success: True

## Request Complete
- request_end: 2026-08-11T17:36:40.789
- request_duration_ms: 47940
- success: True
- final_source: generation

