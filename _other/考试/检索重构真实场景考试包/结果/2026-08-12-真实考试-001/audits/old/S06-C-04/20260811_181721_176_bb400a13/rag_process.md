# RAG Process

audit_id: 20260811_181721_176_bb400a13
timestamp: 2026-08-11T18:17:21.178
## Request
- original_query: 想做带番茄风味的菜。请展示推荐依据；如果意图无法由资料支持，不要把推测写成事实。
- original_query_hash: aedc978d564d7733
- session_id: 2026-08-12-真实考试-001:old:S06-C-04
- request_mode: stream
- request_start: 2026-08-11T18:17:21.179
- evaluation_sample_id: 20260811_181721_176_bb400a13
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:17:21.180
- end: 2026-08-11T18:17:21.180
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:17:21.181
- end: 2026-08-11T18:17:21.181
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 40
- enhanced_query_length: 40
- enhanced_query_hash: aedc978d564d7733

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:17:21.182
- end: 2026-08-11T18:17:21.182
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 40
- analysis_input_query_hash: aedc978d564d7733
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:17:21.182
- end: 2026-08-11T18:17:39.775
- duration_ms: 18592
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 查询核心是围绕“番茄风味”检索并推荐可制作的菜品，同时要求展示推荐依据、区分资料明确支持的内容与未被资料支持的推测。该任务需要将番茄风味这一口味/食材属性与菜品、食谱步骤及资料证据进行匹配，但通常不需要跨越多实体关系进行复杂多跳推理。需要进行轻量证据归因与相关性排序，不需要因果分析；也不要求在多个候选方案间进行显式对比分析。适合使用 hybrid_traditional，通过关键词、同义词（如西红柿、番茄酱、番茄汁）及语义检索召回食谱资料，再依据资料中的明确证据生成推荐和依据说明。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 140, 'graph_rag_count': 33, 'total_queries': 173}
- route_stats_after: {'traditional_count': 141, 'graph_rag_count': 33, 'total_queries': 174}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['番茄']
- topic_keywords: ['番茄风味', '菜品推荐', '推荐依据']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4491

## Hybrid Branch Status / topic_level
- keywords: ['番茄风味', '菜品推荐', '推荐依据']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 7

## Hybrid Branch Status / entity_level
- keywords: ['番茄']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 10

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 416

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 0
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 8
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['如何决策吃什么', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 9
- duration_ms: 12071
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 2, '汤类': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 意式肉酱面
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 16996
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:17:21.182
- end: 2026-08-11T18:17:56.773
- duration_ms: 35591
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1795
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
- chunk_count: 483
- redacted_field: 2402
- total_duration_ms: 12172
- fallback_used: False

## Final Output
- answer_chars: 605
- answer_hash: 691e50b61ab09566
- success: True

## Request Complete
- request_end: 2026-08-11T18:18:08.985
- request_duration_ms: 47805
- success: True
- final_source: generation

