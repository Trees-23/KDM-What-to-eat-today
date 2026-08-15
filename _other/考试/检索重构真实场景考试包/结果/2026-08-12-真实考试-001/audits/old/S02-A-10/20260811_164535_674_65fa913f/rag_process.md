# RAG Process

audit_id: 20260811_164535_674_65fa913f
timestamp: 2026-08-11T16:45:35.677
## Request
- original_query: 芥末黄油罗氏虾的第 1 步应该怎么做？
- original_query_hash: d3d4f66c08cba48a
- session_id: 2026-08-12-真实考试-001:old:S02-A-10
- request_mode: stream
- request_start: 2026-08-11T16:45:35.677
- evaluation_sample_id: 20260811_164535_674_65fa913f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:45:35.679
- end: 2026-08-11T16:45:35.679
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:45:35.679
- end: 2026-08-11T16:45:35.679
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 19
- enhanced_query_length: 19
- enhanced_query_hash: d3d4f66c08cba48a

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:45:35.681
- end: 2026-08-11T16:45:35.681
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 19
- analysis_input_query_hash: d3d4f66c08cba48a
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:45:35.682
- end: 2026-08-11T16:45:43.247
- duration_ms: 7565
- analysis_mode: llm
- query_complexity: 0.12
- relationship_intensity: 0.15
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对特定菜品“芥末黄油罗氏虾”制作流程中“第1步”的直接定位与信息抽取，不涉及多跳推理、因果分析或对比分析。查询核心实体为菜品名称，步骤序号属于流程定位条件而非独立实体，适合通过关键词匹配、菜谱文档检索与步骤字段排序的 hybrid_traditional 策略完成。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 39, 'graph_rag_count': 0, 'total_queries': 39}
- route_stats_after: {'traditional_count': 40, 'graph_rag_count': 0, 'total_queries': 40}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['芥末黄油罗氏虾', '罗氏虾', '芥末', '黄油']
- topic_keywords: ['烹饪步骤', '菜谱']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5774

## Hybrid Branch Status / topic_level
- keywords: ['烹饪步骤', '菜谱']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 13

## Hybrid Branch Status / entity_level
- keywords: ['芥末黄油罗氏虾', '罗氏虾', '芥末', '黄油']
- requested_k: 10
- actual_count: 4
- fallback_count: 0
- duration_ms: 29

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 682

## Hybrid Branch Summary
- entity_count: 4
- topic_count: 1
- vector_count: 10
- origin_len: 15

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 15
- after_count: 9
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
- candidate_count: 9
- duration_ms: 14698
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '荤菜': 1, 'Ingredient': 1, 'Recipe': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21173
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:45:35.682
- end: 2026-08-11T16:46:04.422
- duration_ms: 28740
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2311
- retrieval_levels: ['', 'entity', 'topic']
- search_types: ['entity_level', 'topic_level', 'vector_enhanced']
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
- chunk_count: 52
- redacted_field: 13247
- total_duration_ms: 14430
- fallback_used: False

## Final Output
- answer_chars: 56
- answer_hash: e1087a9e8ab14d69
- success: True

## Request Complete
- request_end: 2026-08-11T16:46:18.875
- request_duration_ms: 43197
- success: True
- final_source: generation

