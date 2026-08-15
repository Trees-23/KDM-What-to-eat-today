# RAG Process

audit_id: 20260811_162652_040_66945bf5
timestamp: 2026-08-11T16:26:52.040
## Request
- original_query: 酸辣土豆丝从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: ac38e5e62aba18df
- session_id: 2026-08-12-真实考试-001:old:S01-B-04
- request_mode: stream
- request_start: 2026-08-11T16:26:52.040
- evaluation_sample_id: 20260811_162652_040_66945bf5
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:26:52.041
- end: 2026-08-11T16:26:52.041
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:26:52.041
- end: 2026-08-11T16:26:52.041
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: ac38e5e62aba18df

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:26:52.042
- end: 2026-08-11T16:26:52.042
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: ac38e5e62aba18df
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:26:52.042
- end: 2026-08-11T16:26:59.198
- duration_ms: 7156
- analysis_mode: llm
- query_complexity: 0.3
- relationship_intensity: 0.25
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是针对“酸辣土豆丝”这一明确菜品的制作流程查询，核心目标是从知识库中检索备料、处理、烹炒到出锅的标准步骤。虽然包含“备料到出锅”的时序要求，但不涉及跨菜品、跨食材或跨领域的复杂关系推理。无需多跳推理、因果分析或对比分析；重点应通过关键词、菜品别名和步骤类字段进行精确检索，并按知识库原有做法组织答案。明确实体主要包括菜品“酸辣土豆丝”和主食材“土豆丝”。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 13, 'graph_rag_count': 0, 'total_queries': 13}
- route_stats_after: {'traditional_count': 14, 'graph_rag_count': 0, 'total_queries': 14}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['酸辣土豆丝', '土豆', '青椒', '干辣椒', '蒜', '白醋', '米醋', '花椒', '炒锅']
- topic_keywords: ['家常菜', '快手菜', '酸辣', '炒菜', '烹饪技巧', '火候', '口感爽脆', '备料']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8504

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '快手菜', '酸辣', '炒菜', '烹饪技巧', '火候', '口感爽脆', '备料']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 47

## Hybrid Branch Status / entity_level
- keywords: ['酸辣土豆丝', '土豆', '青椒', '干辣椒', '蒜', '白醋', '米醋', '花椒', '炒锅']
- requested_k: 10
- actual_count: 10
- fallback_count: 2
- duration_ms: 66

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 635

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 25
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 25
- duration_ms: 18431
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '荤菜': 2, '主食,凉菜': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 27590
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:26:52.042
- end: 2026-08-11T16:27:26.790
- duration_ms: 34747
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3145
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
- chunk_count: 329
- redacted_field: 1723
- total_duration_ms: 8348
- fallback_used: False

## Final Output
- answer_chars: 434
- answer_hash: 11e2cd8d1bc38f4a
- success: True

## Request Complete
- request_end: 2026-08-11T16:27:35.151
- request_duration_ms: 43110
- success: True
- final_source: generation

