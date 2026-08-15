# RAG Process

audit_id: 20260811_174718_902_0579d6a2
timestamp: 2026-08-11T17:47:18.903
## Request
- original_query: 豆腐适合搭配什么蔬菜？
- original_query_hash: 5ad6ff38101f7cd8
- session_id: 2026-08-12-真实考试-001:old:S05-A-04
- request_mode: stream
- request_start: 2026-08-11T17:47:18.904
- evaluation_sample_id: 20260811_174718_902_0579d6a2
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:47:18.905
- end: 2026-08-11T17:47:18.905
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:47:18.906
- end: 2026-08-11T17:47:18.906
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 11
- enhanced_query_length: 11
- enhanced_query_hash: 5ad6ff38101f7cd8

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:47:18.906
- end: 2026-08-11T17:47:18.906
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 11
- analysis_input_query_hash: 5ad6ff38101f7cd8
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:47:18.906
- end: 2026-08-11T17:47:26.730
- duration_ms: 7823
- analysis_mode: llm
- query_complexity: 0.3
- relationship_intensity: 0.5
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 该查询围绕“豆腐”与“蔬菜”两类食材的搭配关系展开，属于明确、常见的烹饪知识检索需求。虽然需要基于口感、烹饪方式、营养搭配等因素进行轻量级匹配与对比，但通常不需要多跳推理、复杂因果分析或大规模关系网络发现。使用关键词检索结合语义检索可有效召回豆腐搭配青菜、菌菇、番茄、白菜、芹菜等相关内容，因此推荐hybrid_traditional策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 112, 'graph_rag_count': 11, 'total_queries': 123}
- route_stats_after: {'traditional_count': 113, 'graph_rag_count': 11, 'total_queries': 124}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['豆腐', '小白菜', '菠菜', '油菜', '青菜', '芹菜', '西兰花', '香菇', '番茄', '胡萝卜']
- topic_keywords: ['蔬菜搭配', '素食', '家常菜', '营养搭配', '高蛋白', '低脂']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3800

## Hybrid Branch Status / topic_level
- keywords: ['蔬菜搭配', '素食', '家常菜', '营养搭配', '高蛋白', '低脂']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 23

## Hybrid Branch Status / entity_level
- keywords: ['豆腐', '小白菜', '菠菜', '油菜', '青菜', '芹菜', '西兰花', '香菇', '番茄', '胡萝卜']
- requested_k: 10
- actual_count: 8
- fallback_count: 0
- duration_ms: 60

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 549

## Hybrid Branch Summary
- entity_count: 8
- topic_count: 2
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 17
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 3
- doc_names: ['揭秘食材搭配的智慧：这些食物不宜同食']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 18
- duration_ms: 15203
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 1, '通用知识': 1, '主食': 2, 'Ingredient': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 19569
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:47:18.906
- end: 2026-08-11T17:47:46.301
- duration_ms: 27394
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4162
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
- chunk_count: 254
- redacted_field: 3450
- total_duration_ms: 9154
- fallback_used: False

## Final Output
- answer_chars: 304
- answer_hash: 580fcc2a497277cd
- success: True

## Request Complete
- request_end: 2026-08-11T17:47:55.474
- request_duration_ms: 36570
- success: True
- final_source: generation

