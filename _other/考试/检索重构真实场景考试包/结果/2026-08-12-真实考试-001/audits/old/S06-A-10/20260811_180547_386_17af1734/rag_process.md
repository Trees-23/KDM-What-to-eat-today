# RAG Process

audit_id: 20260811_180547_386_17af1734
timestamp: 2026-08-11T18:05:47.386
## Request
- original_query: 想做米饭搭配的一道菜。请推荐知识库中最合适的菜，并说明依据。
- original_query_hash: c33e994b379ac90e
- session_id: 2026-08-12-真实考试-001:old:S06-A-10
- request_mode: stream
- request_start: 2026-08-11T18:05:47.386
- evaluation_sample_id: 20260811_180547_386_17af1734
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:05:47.387
- end: 2026-08-11T18:05:47.387
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:05:47.387
- end: 2026-08-11T18:05:47.387
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 30
- enhanced_query_length: 30
- enhanced_query_hash: c33e994b379ac90e

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:05:47.388
- end: 2026-08-11T18:05:47.388
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 30
- analysis_input_query_hash: c33e994b379ac90e
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:05:47.388
- end: 2026-08-11T18:05:59.872
- duration_ms: 12484
- analysis_mode: llm
- query_complexity: 0.52
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.84
- reasoning: 该查询属于带有偏好的菜品推荐任务，核心是从知识库菜品中检索并排序出与“米饭”搭配最合适的一道菜。需要识别“米饭”和“菜”两个明确实体，并利用菜品的口味特征、汤汁/酱汁丰富度、下饭属性、主食搭配描述等文本字段进行相关性匹配与候选对比。虽然存在轻量级的比较推理，但没有要求分析复杂的多实体关系网络、历史地理关联或多跳因果链，因此更适合采用 hybrid_traditional，通过关键词检索、语义检索及排序模型筛选最符合“下饭搭配”意图的菜品。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 126, 'graph_rag_count': 33, 'total_queries': 159}
- route_stats_after: {'traditional_count': 127, 'graph_rag_count': 33, 'total_queries': 160}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['米饭', '红烧肉', '麻婆豆腐', '鱼香肉丝', '宫保鸡丁', '番茄炒蛋']
- topic_keywords: ['下饭菜', '米饭搭配', '家常菜', '咸香', '浓郁口味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5453

## Hybrid Branch Status / topic_level
- keywords: ['下饭菜', '米饭搭配', '家常菜', '咸香', '浓郁口味']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 15

## Hybrid Branch Status / entity_level
- keywords: ['米饭', '红烧肉', '麻婆豆腐', '鱼香肉丝', '宫保鸡丁', '番茄炒蛋']
- requested_k: 10
- actual_count: 4
- fallback_count: 0
- duration_ms: 25

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 348

## Hybrid Branch Summary
- entity_count: 4
- topic_count: 2
- vector_count: 10
- origin_len: 16

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 16
- after_count: 16
- duplicate_count: 0

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 5
- doc_names: ['如何决策吃什么']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 17
- duration_ms: 20273
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, 'Ingredient': 1, 'Recipe': 1, '荤菜': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 黄焖鸡
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 26105
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:05:47.388
- end: 2026-08-11T18:06:25.979
- duration_ms: 38591
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2152
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
- chunk_count: 149
- redacted_field: 2641
- total_duration_ms: 5747
- fallback_used: False

## Final Output
- answer_chars: 188
- answer_hash: 4f8653a5bfe7a6f3
- success: True

## Request Complete
- request_end: 2026-08-11T18:06:31.756
- request_duration_ms: 44369
- success: True
- final_source: generation

