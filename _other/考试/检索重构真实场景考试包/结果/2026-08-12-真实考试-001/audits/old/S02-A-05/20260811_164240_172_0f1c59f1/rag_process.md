# RAG Process

audit_id: 20260811_164240_172_0f1c59f1
timestamp: 2026-08-11T16:42:40.173
## Request
- original_query: 啤酒鸭的第 1 步应该怎么做？
- original_query_hash: 1e5691221eaabf69
- session_id: 2026-08-12-真实考试-001:old:S02-A-05
- request_mode: stream
- request_start: 2026-08-11T16:42:40.173
- evaluation_sample_id: 20260811_164240_172_0f1c59f1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:42:40.174
- end: 2026-08-11T16:42:40.174
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:42:40.174
- end: 2026-08-11T16:42:40.174
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 15
- enhanced_query_length: 15
- enhanced_query_hash: 1e5691221eaabf69

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:42:40.175
- end: 2026-08-11T16:42:40.175
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 15
- analysis_input_query_hash: 1e5691221eaabf69
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:42:40.176
- end: 2026-08-11T16:42:45.253
- duration_ms: 5076
- analysis_mode: llm
- query_complexity: 0.15
- relationship_intensity: 0.1
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对“啤酒鸭”制作流程中“第1步”的直接定位，属于单一菜品实体的简单步骤检索。无需多跳推理、因果分析或对比分析；只需从食谱文本、步骤化文档或结构化菜谱数据中匹配并返回第一步操作。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 34, 'graph_rag_count': 0, 'total_queries': 34}
- route_stats_after: {'traditional_count': 35, 'graph_rag_count': 0, 'total_queries': 35}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['啤酒鸭', '鸭肉', '啤酒']
- topic_keywords: ['烹饪步骤', '烹饪技巧', '去腥', '焯水']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3229

## Hybrid Branch Status / entity_level
- keywords: ['啤酒鸭', '鸭肉', '啤酒']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 43

## Hybrid Branch Status / topic_level
- keywords: ['烹饪步骤', '烹饪技巧', '去腥', '焯水']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 93

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 638

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 10
- vector_count: 10
- origin_len: 23

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 23
- after_count: 17
- duplicate_count: 6

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 17
- duration_ms: 18096
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '素菜': 2, '主食': 1}
- deferred_count: 5
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21992
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:42:40.176
- end: 2026-08-11T16:43:07.246
- duration_ms: 27070
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1853
- retrieval_levels: ['', 'topic']
- search_types: ['topic_level', 'vector_enhanced']
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
- chunk_count: 85
- redacted_field: 2261
- total_duration_ms: 4842
- fallback_used: False

## Final Output
- answer_chars: 116
- answer_hash: 8ddf06e4f2efa987
- success: True

## Request Complete
- request_end: 2026-08-11T16:43:12.117
- request_duration_ms: 31944
- success: True
- final_source: generation

