# RAG Process

audit_id: 20260811_165217_029_2b04ff4e
timestamp: 2026-08-11T16:52:17.033
## Request
- original_query: 刚开始做豆角焖面时，第一步具体要处理什么？
- original_query_hash: ccc5fd0995e736fe
- session_id: 2026-08-12-真实考试-001:old:S02-B-10
- request_mode: stream
- request_start: 2026-08-11T16:52:17.033
- evaluation_sample_id: 20260811_165217_029_2b04ff4e
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:52:17.034
- end: 2026-08-11T16:52:17.034
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:52:17.034
- end: 2026-08-11T16:52:17.034
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: ccc5fd0995e736fe

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:52:17.035
- end: 2026-08-11T16:52:17.035
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: ccc5fd0995e736fe
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:52:17.035
- end: 2026-08-11T16:52:22.223
- duration_ms: 5187
- analysis_mode: llm
- query_complexity: 0.15
- relationship_intensity: 0.1
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.97
- reasoning: 该查询是对“豆角焖面”制作流程中起始步骤的直接事实查找，核心意图是定位菜谱中的第一步操作。无需多跳推理、因果分析或不同做法的对比分析。明确实体主要包括“豆角焖面”（菜品/烹饪任务）和“第一步”（流程阶段），适合通过关键词检索、菜谱步骤匹配与排序完成回答。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 49, 'graph_rag_count': 0, 'total_queries': 49}
- route_stats_after: {'traditional_count': 50, 'graph_rag_count': 0, 'total_queries': 50}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['豆角焖面', '豆角', '面条']
- topic_keywords: ['家常菜', '烹饪步骤', '食材处理', '烹饪技巧']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3636

## Hybrid Branch Status / entity_level
- keywords: ['豆角焖面', '豆角', '面条']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 25

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '烹饪步骤', '食材处理', '烹饪技巧']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 25

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 363

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 2
- vector_count: 10
- origin_len: 14

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 14
- after_count: 10
- duplicate_count: 4

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
- duration_ms: 13370
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '素菜': 2, '荤菜': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 17397
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:52:17.035
- end: 2026-08-11T16:52:39.621
- duration_ms: 22585
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3278
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
- chunk_count: 26
- redacted_field: 2133
- total_duration_ms: 5333
- fallback_used: False

## Final Output
- answer_chars: 32
- answer_hash: 0988230a9aa158c1
- success: True

## Request Complete
- request_end: 2026-08-11T16:52:44.976
- request_duration_ms: 27942
- success: True
- final_source: generation

