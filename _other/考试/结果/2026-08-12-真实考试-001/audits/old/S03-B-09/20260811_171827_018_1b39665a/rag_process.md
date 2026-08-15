# RAG Process

audit_id: 20260811_171827_018_1b39665a
timestamp: 2026-08-11T17:18:27.019
## Request
- original_query: 我想学油温判断技巧及常见温度和单位换算表，它的关键要点和适用场景是什么？
- original_query_hash: bc58f684dca64303
- session_id: 2026-08-12-真实考试-001:old:S03-B-09
- request_mode: stream
- request_start: 2026-08-11T17:18:27.019
- evaluation_sample_id: 20260811_171827_018_1b39665a
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:18:27.020
- end: 2026-08-11T17:18:27.020
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:18:27.020
- end: 2026-08-11T17:18:27.020
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: bc58f684dca64303

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:18:27.020
- end: 2026-08-11T17:18:27.020
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: bc58f684dca64303
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:18:27.021
- end: 2026-08-11T17:18:42.048
- duration_ms: 15027
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.52
- reasoning_required: True
- entity_count: 4
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于中等复杂度的烹饪知识查询，核心诉求包括油温判断技巧、常见油温区间、摄氏度与华氏度单位换算，以及不同油温对应的烹饪适用场景。查询需要将“温度数值/感官现象/烹饪操作/食材类型”进行对应匹配，存在轻度的关联与对比需求，但不涉及跨领域、多实体、多跳的复杂关系推理。适合通过关键词检索、语义检索和结构化表格资料召回来获取答案，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 77, 'graph_rag_count': 1, 'total_queries': 78}
- route_stats_after: {'traditional_count': 78, 'graph_rag_count': 1, 'total_queries': 79}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['油温判断', '油温测试', '油温计', '温度计', '油温温度表', '摄氏度', '华氏度']
- topic_keywords: ['烹饪技巧', '火候', '油温控制', '温度换算', '煎', '炒', '炸', '爆炒', '滑炒']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4958

## Hybrid Branch Status / entity_level
- keywords: ['油温判断', '油温测试', '油温计', '温度计', '油温温度表', '摄氏度', '华氏度']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 10

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '火候', '油温控制', '温度换算', '煎', '炒', '炸', '爆炒', '滑炒']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 63

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 481

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 10
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 13
- duplicate_count: 7

## Hybrid Technique Expansion
- enabled: True
- seed_count: 4
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 14
- duration_ms: 14408
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'高级技巧': 1, '烹饪技巧': 2, '通用知识': 1, '半成品': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 19891
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:18:27.021
- end: 2026-08-11T17:19:01.942
- duration_ms: 34921
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3525
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
- chunk_count: 1296
- redacted_field: 1619
- total_duration_ms: 29001
- fallback_used: False

## Final Output
- answer_chars: 1765
- answer_hash: 0b4e0dd83b04f94f
- success: True

## Request Complete
- request_end: 2026-08-11T17:19:30.975
- request_duration_ms: 63956
- success: True
- final_source: generation

