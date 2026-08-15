# RAG Process

audit_id: 20260811_180427_649_d90018b9
timestamp: 2026-08-11T18:04:27.651
## Request
- original_query: 只有微波炉时能做点什么。请推荐知识库中最合适的菜，并说明依据。
- original_query_hash: d60f5a81faca42fb
- session_id: 2026-08-12-真实考试-001:old:S06-A-08
- request_mode: stream
- request_start: 2026-08-11T18:04:27.652
- evaluation_sample_id: 20260811_180427_649_d90018b9
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:04:27.652
- end: 2026-08-11T18:04:27.652
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:04:27.652
- end: 2026-08-11T18:04:27.652
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 31
- enhanced_query_length: 31
- enhanced_query_hash: d60f5a81faca42fb

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:04:27.653
- end: 2026-08-11T18:04:27.653
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 31
- analysis_input_query_hash: d60f5a81faca42fb
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:04:27.653
- end: 2026-08-11T18:04:36.626
- duration_ms: 8972
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.52
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 该查询的核心目标是在“仅有微波炉”这一设备约束下，从知识库菜谱中筛选并推荐最适合制作的菜品。需要识别微波炉可完成的烹饪方式、排除依赖炒锅、烤箱、明火或复杂预处理的菜谱，并对候选菜品的操作步骤、食材适配性、制作时长和成功率进行对比排序。查询包含“微波炉”和“菜品”两个明确实体/概念，二者之间存在设备—烹饪方法—菜品可行性的关系，但通常不需要复杂知识图谱中的多跳关系发现或深层因果推理。适合采用关键词检索、向量语义召回与菜谱字段过滤相结合的 hybrid_traditional 策略，以召回含有“微波炉”“加热”“蒸制”“焖制”等步骤标签的菜谱，再依据设备限制进行排序推荐。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 125, 'graph_rag_count': 32, 'total_queries': 157}
- route_stats_after: {'traditional_count': 126, 'graph_rag_count': 32, 'total_queries': 158}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['微波炉', '微波炉蒸蛋', '微波炉焖饭', '微波炉土豆', '微波炉鸡翅']
- topic_keywords: ['微波烹饪', '快手菜', '简单易做', '一人食', '免明火']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6082

## Hybrid Branch Status / topic_level
- keywords: ['微波烹饪', '快手菜', '简单易做', '一人食', '免明火']
- requested_k: 10
- actual_count: 7
- fallback_count: 7
- duration_ms: 25

## Hybrid Branch Status / entity_level
- keywords: ['微波炉', '微波炉蒸蛋', '微波炉焖饭', '微波炉土豆', '微波炉鸡翅']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 69

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 565

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 7
- vector_count: 10
- origin_len: 27

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 27
- after_count: 21
- duplicate_count: 6

## Hybrid Technique Expansion
- enabled: True
- seed_count: 10
- expanded_count: 9
- doc_names: ['使用微波炉', '厨房准备']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 22
- duration_ms: 22231
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 1, 'TechniqueDoc': 2, 'TechniqueChunk': 1, '主食': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 28951
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:04:27.653
- end: 2026-08-11T18:05:05.578
- duration_ms: 37924
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 5471
- retrieval_levels: ['context_expansion', 'entity', 'topic']
- search_types: ['entity_level', 'technique_expansion', 'topic_level']
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
- chunk_count: 381
- redacted_field: 4756
- total_duration_ms: 12232
- fallback_used: False

## Final Output
- answer_chars: 486
- answer_hash: 930d1d071a93340d
- success: True

## Request Complete
- request_end: 2026-08-11T18:05:17.826
- request_duration_ms: 50174
- success: True
- final_source: generation

