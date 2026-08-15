# RAG Process

audit_id: 20260811_162818_967_b45f73c1
timestamp: 2026-08-11T16:28:18.970
## Request
- original_query: 红烧茄子从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 65f7c47f22bf3c7a
- session_id: 2026-08-12-真实考试-001:old:S01-B-06
- request_mode: stream
- request_start: 2026-08-11T16:28:18.970
- evaluation_sample_id: 20260811_162818_967_b45f73c1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:28:18.972
- end: 2026-08-11T16:28:18.972
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:28:18.972
- end: 2026-08-11T16:28:18.972
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: 65f7c47f22bf3c7a

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:28:18.973
- end: 2026-08-11T16:28:18.973
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: 65f7c47f22bf3c7a
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:28:18.973
- end: 2026-08-11T16:28:31.666
- duration_ms: 12692
- analysis_mode: llm
- query_complexity: 0.3
- relationship_intensity: 0.25
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是针对“红烧茄子”的直接菜谱检索需求，核心目标是获取知识库中从备料、烹饪到出锅的标准步骤。虽然包含“备料”和“出锅”两个流程阶段，但它们属于同一菜谱内的线性过程，不需要多跳推理、因果分析或跨菜品对比。明确实体包括“红烧茄子”（菜品）、“备料”（烹饪流程阶段）和“出锅”（烹饪流程阶段）。适合使用hybrid_traditional，通过关键词匹配、菜品名称召回及语义检索定位知识库中的对应做法。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 15, 'graph_rag_count': 0, 'total_queries': 15}
- route_stats_after: {'traditional_count': 16, 'graph_rag_count': 0, 'total_queries': 16}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['红烧茄子', '茄子']
- topic_keywords: ['红烧', '家常菜', '下饭菜', '烹饪技巧', '备料', '火候', '调味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 9420

## Hybrid Branch Status / entity_level
- keywords: ['红烧茄子', '茄子']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 48

## Hybrid Branch Status / topic_level
- keywords: ['红烧', '家常菜', '下饭菜', '烹饪技巧', '备料', '火候', '调味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 68

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 663

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 10
- vector_count: 10
- origin_len: 22

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 22
- after_count: 20
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 8
- doc_names: ['炒/煎']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 21
- duration_ms: 28491
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '荤菜': 1, '烹饪技巧': 1, '主食': 1}
- deferred_count: 4
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 茄子肉煎饼
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 38599
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:28:18.973
- end: 2026-08-11T16:29:10.268
- duration_ms: 51294
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3823
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
- chunk_count: 786
- redacted_field: 5905
- total_duration_ms: 24189
- fallback_used: False

## Final Output
- answer_chars: 1102
- answer_hash: 74f0189ecf9fd457
- success: True

## Request Complete
- request_end: 2026-08-11T16:29:34.501
- request_duration_ms: 75530
- success: True
- final_source: generation

