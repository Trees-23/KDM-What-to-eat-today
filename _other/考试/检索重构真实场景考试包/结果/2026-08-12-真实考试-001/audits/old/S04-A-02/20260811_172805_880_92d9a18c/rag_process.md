# RAG Process

audit_id: 20260811_172805_880_92d9a18c
timestamp: 2026-08-11T17:28:05.882
## Request
- original_query: 家里有猪肉，知识库里能做哪些菜？
- original_query_hash: bd80c36fa5adad68
- session_id: 2026-08-12-真实考试-001:old:S04-A-02
- request_mode: stream
- request_start: 2026-08-11T17:28:05.882
- evaluation_sample_id: 20260811_172805_880_92d9a18c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:28:05.883
- end: 2026-08-11T17:28:05.883
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:28:05.884
- end: 2026-08-11T17:28:05.884
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: bd80c36fa5adad68

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:28:05.885
- end: 2026-08-11T17:28:05.885
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 16
- analysis_input_query_hash: bd80c36fa5adad68
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:28:05.885
- end: 2026-08-11T17:28:11.690
- duration_ms: 5805
- analysis_mode: llm
- query_complexity: 0.42
- relationship_intensity: 0.48
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询的核心意图是以“猪肉”为食材约束，从知识库中检索可制作的菜品。明确实体主要为“猪肉”（食材）和隐含的“菜/菜品”（菜谱类别）。查询需要建立食材与菜谱之间的包含或适配关系，并可能根据知识库中的菜谱标签、主料字段或正文内容进行筛选，因此具有一定实体关系，但不涉及复杂关系网络、多跳推理、因果分析或方案对比。适合使用关键词检索、向量语义检索及元数据过滤相结合的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 90, 'graph_rag_count': 1, 'total_queries': 91}
- route_stats_after: {'traditional_count': 91, 'graph_rag_count': 1, 'total_queries': 92}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['猪肉', '红烧肉', '回锅肉', '鱼香肉丝', '糖醋里脊', '青椒肉丝', '京酱肉丝', '粉蒸肉', '梅菜扣肉', '猪肉炖粉条']
- topic_keywords: ['家常菜', '下饭菜', '猪肉菜谱', '荤菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7336

## Hybrid Branch Status / entity_level
- keywords: ['猪肉', '红烧肉', '回锅肉', '鱼香肉丝', '糖醋里脊', '青椒肉丝', '京酱肉丝', '粉蒸肉', '梅菜扣肉', '猪肉炖粉条']
- requested_k: 10
- actual_count: 6
- fallback_count: 0
- duration_ms: 37

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '下饭菜', '猪肉菜谱', '荤菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 44

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 560

## Hybrid Branch Summary
- entity_count: 6
- topic_count: 10
- vector_count: 10
- origin_len: 26

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 26
- after_count: 23
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
- candidate_count: 24
- duration_ms: 18713
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'通用知识': 1, '主食': 1, '烹饪技巧': 1, '荤菜': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 青椒土豆炒肉
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 26635
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:28:05.885
- end: 2026-08-11T17:28:38.327
- duration_ms: 32441
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3119
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
- chunk_count: 206
- redacted_field: 5197
- total_duration_ms: 9366
- fallback_used: False

## Final Output
- answer_chars: 258
- answer_hash: 96d45d62504bc761
- success: True

## Request Complete
- request_end: 2026-08-11T17:28:47.721
- request_duration_ms: 41839
- success: True
- final_source: generation

