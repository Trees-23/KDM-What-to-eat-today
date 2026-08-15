# RAG Process

audit_id: 20260811_165439_489_14168f30
timestamp: 2026-08-11T16:54:39.490
## Request
- original_query: 只回答清蒸南瓜的第 1 步，并说明它来自哪一条菜谱步骤；不要混入后续步骤。
- original_query_hash: 8bbc563333004d26
- session_id: 2026-08-12-真实考试-001:old:S02-C-04
- request_mode: stream
- request_start: 2026-08-11T16:54:39.490
- evaluation_sample_id: 20260811_165439_489_14168f30
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:54:39.491
- end: 2026-08-11T16:54:39.491
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:54:39.491
- end: 2026-08-11T16:54:39.491
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 37
- enhanced_query_length: 37
- enhanced_query_hash: 8bbc563333004d26

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:54:39.492
- end: 2026-08-11T16:54:39.492
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 37
- analysis_input_query_hash: 8bbc563333004d26
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:54:39.492
- end: 2026-08-11T16:54:46.153
- duration_ms: 6660
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.25
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询的核心是从“清蒸南瓜”菜谱中精确定位并返回“第1步”，同时满足不包含后续步骤、说明步骤来源的输出约束。需要进行菜谱匹配、步骤序号过滤和来源标注，但不涉及多跳推理、因果分析或实体间复杂关系推断。明确实体主要为“清蒸南瓜”菜谱和“第1步”步骤位置，因此适合使用 hybrid_traditional 进行关键词/语义检索与结构化步骤筛选。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 53, 'graph_rag_count': 0, 'total_queries': 53}
- route_stats_after: {'traditional_count': 54, 'graph_rag_count': 0, 'total_queries': 54}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['清蒸南瓜', '南瓜']
- topic_keywords: ['清蒸', '菜谱步骤', '步骤溯源']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4308

## Hybrid Branch Status / topic_level
- keywords: ['清蒸', '菜谱步骤', '步骤溯源']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 8

## Hybrid Branch Status / entity_level
- keywords: ['清蒸南瓜', '南瓜']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 20

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 393

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 0
- vector_count: 10
- origin_len: 12

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 12
- after_count: 9
- duplicate_count: 3

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
- duration_ms: 13282
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '荤菜': 2, 'Ingredient': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 17997
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:54:39.492
- end: 2026-08-11T16:55:04.151
- duration_ms: 24659
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2728
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
- chunk_count: 40
- redacted_field: 1732
- total_duration_ms: 2647
- fallback_used: False

## Final Output
- answer_chars: 46
- answer_hash: 4b1ce71ea54e3fac
- success: True

## Request Complete
- request_end: 2026-08-11T16:55:06.841
- request_duration_ms: 27351
- success: True
- final_source: generation

