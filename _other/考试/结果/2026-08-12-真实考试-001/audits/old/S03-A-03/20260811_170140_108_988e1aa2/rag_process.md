# RAG Process

audit_id: 20260811_170140_108_988e1aa2
timestamp: 2026-08-11T17:01:40.109
## Request
- original_query: 请说明“辅料技巧”这个技巧的关键要点和适用情形。
- original_query_hash: d42d16031c6bc58b
- session_id: 2026-08-12-真实考试-001:old:S03-A-03
- request_mode: stream
- request_start: 2026-08-11T17:01:40.109
- evaluation_sample_id: 20260811_170140_108_988e1aa2
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:01:40.111
- end: 2026-08-11T17:01:40.111
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:01:40.111
- end: 2026-08-11T17:01:40.111
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 24
- enhanced_query_length: 24
- enhanced_query_hash: d42d16031c6bc58b

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:01:40.111
- end: 2026-08-11T17:01:40.111
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 24
- analysis_input_query_hash: d42d16031c6bc58b
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:01:40.112
- end: 2026-08-11T17:01:48.128
- duration_ms: 8016
- analysis_mode: llm
- query_complexity: 0.3
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询围绕“辅料技巧”这一单一技巧实体，要求说明其关键要点和适用情形，主要属于信息检索与归纳总结。无需多跳推理、因果分析或对比分析；实体关系较少，采用关键词检索结合语义检索即可有效获取相关内容。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 62, 'graph_rag_count': 0, 'total_queries': 62}
- route_stats_after: {'traditional_count': 63, 'graph_rag_count': 0, 'total_queries': 63}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['辅料技巧', '辅料']
- topic_keywords: ['烹饪技巧', '食材搭配', '调味', '增香', '提味', '口感', '配色', '菜品搭配']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4549

## Hybrid Branch Status / entity_level
- keywords: ['辅料技巧', '辅料']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 194

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 671

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '食材搭配', '调味', '增香', '提味', '口感', '配色', '菜品搭配']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 4264

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 13
- duplicate_count: 17

## Hybrid Technique Expansion
- enabled: True
- seed_count: 10
- expanded_count: 9
- doc_names: ['炒/煎', '辅料技巧']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 14
- duration_ms: 18730
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 2, 'TechniqueChunk': 2, '烹饪技巧': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 27583
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:01:40.112
- end: 2026-08-11T17:02:15.713
- duration_ms: 35600
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 5105
- retrieval_levels: ['context_expansion', 'entity']
- search_types: ['entity_level', 'technique_expansion']
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
- chunk_count: 703
- redacted_field: 3331
- total_duration_ms: 19222
- fallback_used: False

## Final Output
- answer_chars: 917
- answer_hash: 312e8b4692420b9a
- success: True

## Request Complete
- request_end: 2026-08-11T17:02:34.951
- request_duration_ms: 54841
- success: True
- final_source: generation

