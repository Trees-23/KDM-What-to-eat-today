# RAG Process

audit_id: 20260811_181325_712_6d36f40b
timestamp: 2026-08-11T18:13:25.720
## Request
- original_query: 朋友来家里，想做一道有地方特色的菜，帮我找几个贴近这个需求的做法。
- original_query_hash: b83d8beaa202aa69
- session_id: 2026-08-12-真实考试-001:old:S06-B-09
- request_mode: stream
- request_start: 2026-08-11T18:13:25.720
- evaluation_sample_id: 20260811_181325_712_6d36f40b
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:13:25.721
- end: 2026-08-11T18:13:25.722
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:13:25.722
- end: 2026-08-11T18:13:25.722
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 33
- enhanced_query_length: 33
- enhanced_query_hash: b83d8beaa202aa69

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:13:25.724
- end: 2026-08-11T18:13:25.724
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 33
- analysis_input_query_hash: b83d8beaa202aa69
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:13:25.724
- end: 2026-08-11T18:13:32.573
- duration_ms: 6849
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.86
- reasoning: 该查询属于带有场景约束的菜谱推荐需求：需要同时满足“朋友来家里”“适合招待”“具有地方特色”“提供多个做法”等条件。查询未指定具体地域、食材库存、烹饪水平或人数，因此核心任务是通过关键词检索与语义召回获取不同地域的代表性家常/待客菜做法，再按易操作性和宴客适配度进行排序。虽然存在场景与菜品属性之间的匹配关系，但不涉及地域历史、食材关系或菜系演化等复杂知识网络推理，因此更适合采用hybrid_traditional策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 135, 'graph_rag_count': 33, 'total_queries': 168}
- route_stats_after: {'traditional_count': 136, 'graph_rag_count': 33, 'total_queries': 169}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['麻婆豆腐', '剁椒鱼头', '小鸡炖蘑菇', '佛跳墙', '西湖醋鱼', '腊肉', '辣椒', '花椒']
- topic_keywords: ['地方特色菜', '家宴', '待客菜', '家常菜', '地域风味', '朋友聚餐']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5622

## Hybrid Branch Status / topic_level
- keywords: ['地方特色菜', '家宴', '待客菜', '家常菜', '地域风味', '朋友聚餐']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 16

## Hybrid Branch Status / entity_level
- keywords: ['麻婆豆腐', '剁椒鱼头', '小鸡炖蘑菇', '佛跳墙', '西湖醋鱼', '腊肉', '辣椒', '花椒']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 20

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 259

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 2
- vector_count: 10
- origin_len: 15

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 15
- after_count: 15
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
- candidate_count: 16
- duration_ms: 12780
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '通用知识': 1, '主食': 2}
- deferred_count: 4
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 热干面
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18682
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:13:25.724
- end: 2026-08-11T18:13:51.257
- duration_ms: 25532
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1777
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
- chunk_count: 917
- redacted_field: 23110
- total_duration_ms: 49669
- fallback_used: False

## Final Output
- answer_chars: 1171
- answer_hash: b05df87f482eeb2f
- success: True

## Request Complete
- request_end: 2026-08-11T18:14:40.953
- request_duration_ms: 75232
- success: True
- final_source: generation

