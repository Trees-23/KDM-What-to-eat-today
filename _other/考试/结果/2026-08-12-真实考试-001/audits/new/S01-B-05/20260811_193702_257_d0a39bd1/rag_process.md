# RAG Process

audit_id: 20260811_193702_257_d0a39bd1
timestamp: 2026-08-11T19:37:02.258
## Request
- original_query: 蚝油生菜从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: dbd35521ee182f2c
- session_id: 2026-08-12-真实考试-001:new:S01-B-05
- request_mode: stream
- request_start: 2026-08-11T19:37:02.258
- evaluation_sample_id: 20260811_193702_257_d0a39bd1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:37:02.260
- end: 2026-08-11T19:37:02.260
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:37:02.260
- end: 2026-08-11T19:37:02.260
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: dbd35521ee182f2c

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:37:02.266
- end: 2026-08-11T19:37:02.265
- duration_ms: 0
- entity_id: 201005164
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:37:02.266
- end: 2026-08-11T19:37:02.266
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:37:02.266
- end: 2026-08-11T19:37:02.266
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: dbd35521ee182f2c
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:37:02.266
- end: 2026-08-11T19:37:11.921
- duration_ms: 9655
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询是针对“蚝油生菜”菜品制作流程的直接信息查找，核心需求是从知识库中检索备料、烹饪步骤和出锅要点。明确实体包括“蚝油”“生菜”和“蚝油生菜（菜品）”。查询不要求跨菜品、食材搭配或营养知识进行多跳推理，也不涉及因果或对比分析；“按知识库里的做法回答”进一步强调应优先进行关键词、菜名及步骤字段的精确/语义混合检索，因此推荐 hybrid_traditional。

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
- entity_keywords: ['蚝油生菜', '生菜', '蚝油']
- topic_keywords: ['家常菜', '快手菜', '素菜', '烹饪技巧', '火候', '调味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4326

## Hybrid Branch Status / entity_level
- keywords: ['蚝油生菜', '生菜', '蚝油']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 32

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '快手菜', '素菜', '烹饪技巧', '火候', '调味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 75

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 687

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 10
- vector_count: 10
- origin_len: 23

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 23
- after_count: 16
- duplicate_count: 7

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
- candidate_count: 17
- duration_ms: 15496
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '水产': 1, '烹饪技巧': 1, '调料': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 炸串酱料
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20531
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:37:02.266
- end: 2026-08-11T19:37:32.453
- duration_ms: 30187
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2952
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
- chunk_count: 403
- redacted_field: 4110
- total_duration_ms: 12504
- fallback_used: False

## Final Output
- answer_chars: 592
- answer_hash: 4ef3d3719608ca20
- success: True

## Request Complete
- request_end: 2026-08-11T19:37:44.980
- request_duration_ms: 42722
- success: True
- final_source: generation

