# RAG Process

audit_id: 20260811_165540_923_7bda5a69
timestamp: 2026-08-11T16:55:40.924
## Request
- original_query: 只回答凉拌金针菇的第 1 步，并说明它来自哪一条菜谱步骤；不要混入后续步骤。
- original_query_hash: 24df83a06e53700f
- session_id: 2026-08-12-真实考试-001:old:S02-C-06
- request_mode: stream
- request_start: 2026-08-11T16:55:40.924
- evaluation_sample_id: 20260811_165540_923_7bda5a69
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:55:40.924
- end: 2026-08-11T16:55:40.924
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:55:40.925
- end: 2026-08-11T16:55:40.925
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 38
- enhanced_query_length: 38
- enhanced_query_hash: 24df83a06e53700f

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:55:40.925
- end: 2026-08-11T16:55:40.925
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 38
- analysis_input_query_hash: 24df83a06e53700f
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:55:40.925
- end: 2026-08-11T16:55:54.452
- duration_ms: 13526
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.35
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 该查询是面向特定菜谱的精确步骤定位与受约束抽取任务。需要检索“凉拌金针菇”菜谱，并在匹配结果中定位编号为第1步的内容，同时识别其所属菜谱步骤来源；还需执行输出边界控制，排除第2步及之后的内容。无需多跳推理、因果分析或跨菜谱对比，核心是关键词/菜名匹配、步骤序号过滤和文本片段抽取，因此适合 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 55, 'graph_rag_count': 0, 'total_queries': 55}
- route_stats_after: {'traditional_count': 56, 'graph_rag_count': 0, 'total_queries': 56}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['凉拌金针菇', '金针菇', '凉拌']
- topic_keywords: ['菜谱步骤', '步骤定位', '第1步']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7169

## Hybrid Branch Status / topic_level
- keywords: ['菜谱步骤', '步骤定位', '第1步']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 12

## Hybrid Branch Status / entity_level
- keywords: ['凉拌金针菇', '金针菇', '凉拌']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 151

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 370

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 0
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 16
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 8
- expanded_count: 9
- doc_names: ['厨房准备']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 17
- duration_ms: 23440
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '汤类': 2, 'TechniqueDoc': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 勾芡香菇汤
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 31015
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:55:40.925
- end: 2026-08-11T16:56:25.469
- duration_ms: 44543
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 5784
- retrieval_levels: ['', 'context_expansion', 'entity']
- search_types: ['entity_level', 'technique_expansion', 'vector_enhanced']
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
- chunk_count: 47
- redacted_field: 2234
- total_duration_ms: 3302
- fallback_used: False

## Final Output
- answer_chars: 59
- answer_hash: d78123c65b18ba98
- success: True

## Request Complete
- request_end: 2026-08-11T16:56:28.800
- request_duration_ms: 47876
- success: True
- final_source: generation

