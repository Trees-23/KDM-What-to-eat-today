# RAG Process

audit_id: 20260811_165401_491_94934d26
timestamp: 2026-08-11T16:54:01.492
## Request
- original_query: 只回答西葫芦炒鸡蛋的第 1 步，并说明它来自哪一条菜谱步骤；不要混入后续步骤。
- original_query_hash: 8b39bab9afbbc8bf
- session_id: 2026-08-12-真实考试-001:old:S02-C-03
- request_mode: stream
- request_start: 2026-08-11T16:54:01.492
- evaluation_sample_id: 20260811_165401_491_94934d26
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:54:01.492
- end: 2026-08-11T16:54:01.492
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:54:01.493
- end: 2026-08-11T16:54:01.493
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 39
- enhanced_query_length: 39
- enhanced_query_hash: 8b39bab9afbbc8bf

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:54:01.493
- end: 2026-08-11T16:54:01.493
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 39
- analysis_input_query_hash: 8b39bab9afbbc8bf
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:54:01.493
- end: 2026-08-11T16:54:12.206
- duration_ms: 10712
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.2
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是对特定菜谱“西葫芦炒鸡蛋”中指定序号“第1步”的精确定位与片段抽取，并要求保留步骤来源、排除后续步骤内容。它不需要多跳推理、因果分析或实体关系网络推断，但需要执行步骤序号过滤、内容边界控制和来源归属校验。明确实体包括菜谱名称“西葫芦炒鸡蛋”和流程定位实体“第1步”。因此适合使用 hybrid_traditional 进行关键词、菜谱标题和步骤编号的精确检索与排序。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 52, 'graph_rag_count': 0, 'total_queries': 52}
- route_stats_after: {'traditional_count': 53, 'graph_rag_count': 0, 'total_queries': 53}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['西葫芦炒鸡蛋', '西葫芦', '鸡蛋']
- topic_keywords: ['菜谱步骤', '第1步']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8799

## Hybrid Branch Status / topic_level
- keywords: ['菜谱步骤', '第1步']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 8

## Hybrid Branch Status / entity_level
- keywords: ['西葫芦炒鸡蛋', '西葫芦', '鸡蛋']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 38

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 336

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 0
- vector_count: 10
- origin_len: 13

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 13
- after_count: 9
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
- candidate_count: 9
- duration_ms: 14608
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '汤类': 1, '主食': 1, 'Ingredient': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23764
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:54:01.493
- end: 2026-08-11T16:54:35.972
- duration_ms: 34478
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3452
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
- chunk_count: 39
- redacted_field: 2653
- total_duration_ms: 3485
- fallback_used: False

## Final Output
- answer_chars: 47
- answer_hash: bc443661a32cd750
- success: True

## Request Complete
- request_end: 2026-08-11T16:54:39.472
- request_duration_ms: 37980
- success: True
- final_source: generation

