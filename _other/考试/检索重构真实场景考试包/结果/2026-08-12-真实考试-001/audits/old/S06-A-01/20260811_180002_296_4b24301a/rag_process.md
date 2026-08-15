# RAG Process

audit_id: 20260811_180002_296_4b24301a
timestamp: 2026-08-11T18:00:02.297
## Request
- original_query: 天气热，想做一道清爽不腻的晚饭。请推荐知识库中最合适的菜，并说明依据。
- original_query_hash: 972c852ccbacab42
- session_id: 2026-08-12-真实考试-001:old:S06-A-01
- request_mode: stream
- request_start: 2026-08-11T18:00:02.297
- evaluation_sample_id: 20260811_180002_296_4b24301a
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:00:02.299
- end: 2026-08-11T18:00:02.299
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:00:02.300
- end: 2026-08-11T18:00:02.300
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: 972c852ccbacab42

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:00:02.300
- end: 2026-08-11T18:00:02.300
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 35
- analysis_input_query_hash: 972c852ccbacab42
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:00:02.301
- end: 2026-08-11T18:00:10.305
- duration_ms: 8004
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 该查询属于带条件的菜品推荐，而非单一菜谱查找。需要识别“天气热”“晚饭”“清爽不腻”三个核心条件，并在知识库菜品中匹配口味、烹饪方式、油脂水平、食材属性及适合作为晚餐等信息，再对候选菜品进行相关性排序和简要对比。它需要语义理解与条件匹配，但通常不依赖跨多实体、多层关系的复杂图谱推理，因此更适合采用 hybrid_traditional，通过关键词检索召回天气、清淡、凉拌、蒸煮、低油等相关菜品，并结合向量检索理解“清爽不腻”的隐含语义后进行重排序。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 31, 'total_queries': 150}
- route_stats_after: {'traditional_count': 120, 'graph_rag_count': 31, 'total_queries': 151}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['凉拌黄瓜', '凉拌鸡丝', '番茄鸡蛋面', '荞麦面', '黄瓜', '番茄', '鸡胸肉']
- topic_keywords: ['夏季饮食', '清爽', '不油腻', '晚餐', '凉拌菜', '快手菜', '低脂', '开胃']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8686

## Hybrid Branch Status / entity_level
- keywords: ['凉拌黄瓜', '凉拌鸡丝', '番茄鸡蛋面', '荞麦面', '黄瓜', '番茄', '鸡胸肉']
- requested_k: 10
- actual_count: 6
- fallback_count: 0
- duration_ms: 38

## Hybrid Branch Status / topic_level
- keywords: ['夏季饮食', '清爽', '不油腻', '晚餐', '凉拌菜', '快手菜', '低脂', '开胃']
- requested_k: 10
- actual_count: 6
- fallback_count: 6
- duration_ms: 52

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 668

## Hybrid Branch Summary
- entity_count: 6
- topic_count: 6
- vector_count: 10
- origin_len: 22

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 22
- after_count: 19
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['如何决策吃什么', '厨房准备']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 20
- duration_ms: 20217
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '通用知识': 2, '烹饪技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 29593
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:00:02.301
- end: 2026-08-11T18:00:39.900
- duration_ms: 37598
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3527
- retrieval_levels: ['', 'context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 230
- redacted_field: 3528
- total_duration_ms: 8208
- fallback_used: False

## Final Output
- answer_chars: 294
- answer_hash: c51d60d241013006
- success: True

## Request Complete
- request_end: 2026-08-11T18:00:48.135
- request_duration_ms: 45837
- success: True
- final_source: generation

