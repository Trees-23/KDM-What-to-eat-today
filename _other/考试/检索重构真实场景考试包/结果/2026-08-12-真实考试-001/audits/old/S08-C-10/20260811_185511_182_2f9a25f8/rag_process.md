# RAG Process

audit_id: 20260811_185511_182_2f9a25f8
timestamp: 2026-08-11T18:55:11.186
## Request
- original_query: 请查云岚30号幻味砂锅的做法；未收录时只说明未找到，不要根据名称猜配方。
- original_query_hash: 0ce32c8966225af9
- session_id: 2026-08-12-真实考试-001:old:S08-C-10
- request_mode: stream
- request_start: 2026-08-11T18:55:11.187
- evaluation_sample_id: 20260811_185511_182_2f9a25f8
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:55:11.188
- end: 2026-08-11T18:55:11.188
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:55:11.188
- end: 2026-08-11T18:55:11.188
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 0ce32c8966225af9

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:55:11.189
- end: 2026-08-11T18:55:11.189
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 0ce32c8966225af9
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:55:11.189
- end: 2026-08-11T18:55:19.249
- duration_ms: 8059
- analysis_mode: llm
- query_complexity: 0.18
- relationship_intensity: 0.08
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是针对“云岚30号幻味砂锅”这一明确菜品名称的定向做法检索，核心任务是从已收录资料中精确匹配配方或制作步骤。查询明确要求未收录时仅返回未找到，禁止依据名称进行语义补全、配方推测或关联扩展，因此不需要多跳推理、因果分析、对比分析或复杂实体关系建模。建议采用 hybrid_traditional，通过关键词精确匹配、别名匹配及向量召回进行检索，并以收录状态校验和结果置信度阈值控制回答：无可靠证据时直接返回未找到。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 194, 'graph_rag_count': 33, 'total_queries': 227}
- route_stats_after: {'traditional_count': 195, 'graph_rag_count': 33, 'total_queries': 228}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚30号幻味砂锅']
- topic_keywords: ['砂锅菜', '菜谱查询']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6709

## Hybrid Branch Status / entity_level
- keywords: ['云岚30号幻味砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 4

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '菜谱查询']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 7

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 306

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 0
- vector_count: 10
- origin_len: 10

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 10
- after_count: 10
- duplicate_count: 0

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 10
- duration_ms: 3890
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '汤类': 1, '主食': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 10914
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:55:11.189
- end: 2026-08-11T18:55:30.163
- duration_ms: 18974
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 936
- retrieval_levels: ['']
- search_types: ['vector_enhanced']
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
- chunk_count: 17
- redacted_field: 2617
- total_duration_ms: 1930
- fallback_used: False

## Final Output
- answer_chars: 20
- answer_hash: f5f7aac4e6ad073b
- success: True

## Request Complete
- request_end: 2026-08-11T18:55:32.113
- request_duration_ms: 20926
- success: True
- final_source: generation

