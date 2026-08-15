# RAG Process

audit_id: 20260811_164957_963_d36e7e5c
timestamp: 2026-08-11T16:49:57.966
## Request
- original_query: 刚开始做牛排时，第一步具体要处理什么？
- original_query_hash: 02dfa648b6a1f1ee
- session_id: 2026-08-12-真实考试-001:old:S02-B-06
- request_mode: stream
- request_start: 2026-08-11T16:49:57.967
- evaluation_sample_id: 20260811_164957_963_d36e7e5c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:49:57.968
- end: 2026-08-11T16:49:57.968
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:49:57.968
- end: 2026-08-11T16:49:57.968
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 19
- enhanced_query_length: 19
- enhanced_query_hash: 02dfa648b6a1f1ee

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:49:57.969
- end: 2026-08-11T16:49:57.969
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 19
- analysis_input_query_hash: 02dfa648b6a1f1ee
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:49:57.969
- end: 2026-08-11T16:50:04.959
- duration_ms: 6989
- analysis_mode: llm
- query_complexity: 0.18
- relationship_intensity: 0.12
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是面向烹饪流程起始步骤的直接信息查找，核心意图是确定制作牛排前的第一项具体处理动作。查询仅涉及“牛排”和“制作/处理步骤”两个明确实体（其中后者为流程类实体），关系为单一的步骤顺序关系。通常无需多跳推理、因果分析或对比分析；通过关键词检索、菜谱步骤匹配及语义排序即可获得答案，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 45, 'graph_rag_count': 0, 'total_queries': 45}
- route_stats_after: {'traditional_count': 46, 'graph_rag_count': 0, 'total_queries': 46}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['牛排']
- topic_keywords: ['烹饪技巧', '牛排处理', '解冻', '回温', '调味', '火候']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3550

## Hybrid Branch Status / entity_level
- keywords: ['牛排']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 15

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '牛排处理', '解冻', '回温', '调味', '火候']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 46

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 398

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 10
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 19
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 19
- duration_ms: 21995
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 1, '调料': 1, '素菜': 1}
- deferred_count: 7
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25960
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:49:57.969
- end: 2026-08-11T16:50:30.920
- duration_ms: 32951
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2229
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
- chunk_count: 62
- redacted_field: 1820
- total_duration_ms: 3117
- fallback_used: False

## Final Output
- answer_chars: 78
- answer_hash: 72d1f5a8b1d85193
- success: True

## Request Complete
- request_end: 2026-08-11T16:50:34.061
- request_duration_ms: 36094
- success: True
- final_source: generation

