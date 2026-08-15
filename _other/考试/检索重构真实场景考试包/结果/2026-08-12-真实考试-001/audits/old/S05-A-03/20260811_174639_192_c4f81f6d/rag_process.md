# RAG Process

audit_id: 20260811_174639_192_c4f81f6d
timestamp: 2026-08-11T17:46:39.193
## Request
- original_query: 鸡蛋适合搭配什么蔬菜？
- original_query_hash: 2cf6984927105a17
- session_id: 2026-08-12-真实考试-001:old:S05-A-03
- request_mode: stream
- request_start: 2026-08-11T17:46:39.194
- evaluation_sample_id: 20260811_174639_192_c4f81f6d
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:46:39.196
- end: 2026-08-11T17:46:39.196
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:46:39.196
- end: 2026-08-11T17:46:39.196
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 11
- enhanced_query_length: 11
- enhanced_query_hash: 2cf6984927105a17

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:46:39.198
- end: 2026-08-11T17:46:39.198
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 11
- analysis_input_query_hash: 2cf6984927105a17
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:46:39.198
- end: 2026-08-11T17:46:47.776
- duration_ms: 8578
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.55
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 该查询属于常见饮食搭配信息检索，核心是识别“鸡蛋”与“蔬菜”之间的适配关系，并返回适合共同烹饪或食用的蔬菜列表。查询存在二元搭配关系，但不涉及复杂的多实体关系网络、跨文档知识发现或多跳推理。可通过关键词检索、菜谱语料匹配与语义召回直接获得结果，因此适合hybrid_traditional策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 111, 'graph_rag_count': 11, 'total_queries': 122}
- route_stats_after: {'traditional_count': 112, 'graph_rag_count': 11, 'total_queries': 123}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鸡蛋', '番茄', '菠菜', '韭菜', '黄瓜', '西兰花', '洋葱', '青椒', '蘑菇', '胡萝卜']
- topic_keywords: ['食材搭配', '蔬菜搭配', '营养均衡', '家常菜', '快手菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5358

## Hybrid Branch Status / entity_level
- keywords: ['鸡蛋', '番茄', '菠菜', '韭菜', '黄瓜', '西兰花', '洋葱', '青椒', '蘑菇', '胡萝卜']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 70

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 572

## Hybrid Branch Status / topic_level
- keywords: ['食材搭配', '蔬菜搭配', '营养均衡', '家常菜', '快手菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 2965

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 21
- duplicate_count: 9

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
- candidate_count: 22
- duration_ms: 14765
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '主食': 2, '早餐': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 燕麦鸡蛋饼
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23108
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:46:39.198
- end: 2026-08-11T17:47:10.886
- duration_ms: 31688
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3006
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
- chunk_count: 251
- redacted_field: 1806
- total_duration_ms: 7975
- fallback_used: False

## Final Output
- answer_chars: 308
- answer_hash: 64206ff846683107
- success: True

## Request Complete
- request_end: 2026-08-11T17:47:18.878
- request_duration_ms: 39683
- success: True
- final_source: generation

