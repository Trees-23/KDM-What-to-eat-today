# RAG Process

audit_id: 20260811_173120_671_a7483d35
timestamp: 2026-08-11T17:31:20.672
## Request
- original_query: 家里有茄子，知识库里能做哪些菜？
- original_query_hash: 98e365eedacb2c89
- session_id: 2026-08-12-真实考试-001:old:S04-A-07
- request_mode: stream
- request_start: 2026-08-11T17:31:20.672
- evaluation_sample_id: 20260811_173120_671_a7483d35
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:31:20.673
- end: 2026-08-11T17:31:20.673
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:31:20.674
- end: 2026-08-11T17:31:20.674
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: 98e365eedacb2c89

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:31:20.675
- end: 2026-08-11T17:31:20.674
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 16
- analysis_input_query_hash: 98e365eedacb2c89
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:31:20.675
- end: 2026-08-11T17:31:28.177
- duration_ms: 7502
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.45
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 查询的核心目标是基于明确食材“茄子”检索知识库中的相关菜谱，属于直接的食材到菜品匹配任务。虽然隐含“茄子—可制作菜品”的实体关系，但通常可通过关键词检索、菜谱标签过滤和语义召回完成，无需多跳推理、因果分析或复杂对比分析。明确实体为“茄子”，类型为食材；“家里有”是场景约束，不构成独立实体。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 95, 'graph_rag_count': 1, 'total_queries': 96}
- route_stats_after: {'traditional_count': 96, 'graph_rag_count': 1, 'total_queries': 97}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['茄子', '鱼香茄子', '红烧茄子', '地三鲜', '蒜蓉茄子', '凉拌茄子', '肉末茄子', '茄子煲']
- topic_keywords: ['家常菜', '素菜', '下饭菜', '茄子菜谱']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4278

## Hybrid Branch Status / entity_level
- keywords: ['茄子', '鱼香茄子', '红烧茄子', '地三鲜', '蒜蓉茄子', '凉拌茄子', '肉末茄子', '茄子煲']
- requested_k: 10
- actual_count: 4
- fallback_count: 0
- duration_ms: 59

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '素菜', '下饭菜', '茄子菜谱']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 80

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 403

## Hybrid Branch Summary
- entity_count: 4
- topic_count: 10
- vector_count: 10
- origin_len: 24

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 24
- after_count: 19
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
- candidate_count: 19
- duration_ms: 17571
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '荤菜': 1, '主食': 1, 'Ingredient': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22283
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:31:20.675
- end: 2026-08-11T17:31:50.461
- duration_ms: 29786
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3368
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
- chunk_count: 336
- redacted_field: 3006
- total_duration_ms: 9925
- fallback_used: False

## Final Output
- answer_chars: 422
- answer_hash: 52df0c248feff65e
- success: True

## Request Complete
- request_end: 2026-08-11T17:32:00.415
- request_duration_ms: 39742
- success: True
- final_source: generation

