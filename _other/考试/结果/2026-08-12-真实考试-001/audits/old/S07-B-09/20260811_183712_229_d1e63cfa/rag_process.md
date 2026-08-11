# RAG Process

audit_id: 20260811_183712_229_d1e63cfa
timestamp: 2026-08-11T18:37:12.231
## Request
- original_query: 想吃清爽一点的川味蒸菜，有哪些做法比较贴近这种偏好？
- original_query_hash: 9e2fac77efbfdd93
- session_id: 2026-08-12-真实考试-001:old:S07-B-09
- request_mode: stream
- request_start: 2026-08-11T18:37:12.231
- evaluation_sample_id: 20260811_183712_229_d1e63cfa
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:37:12.232
- end: 2026-08-11T18:37:12.232
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:37:12.232
- end: 2026-08-11T18:37:12.232
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: 9e2fac77efbfdd93

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:37:12.232
- end: 2026-08-11T18:37:12.232
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: 9e2fac77efbfdd93
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:37:12.233
- end: 2026-08-11T18:37:21.610
- duration_ms: 9377
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.52
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心是根据“清爽”这一口味偏好，在“川味”和“蒸菜”两个明确饮食实体的交集内筛选合适做法。需要进行轻度的语义匹配与对比，例如排除重油、重麻辣、重调味的做法，优先检索清蒸、豆豉蒸、剁椒轻调味、蒸蔬菜或蒸鱼等菜谱；但不涉及跨领域知识、多跳关联或复杂因果推理，因此适合使用hybrid_traditional进行关键词检索与语义排序。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 164, 'graph_rag_count': 33, 'total_queries': 197}
- route_stats_after: {'traditional_count': 165, 'graph_rag_count': 33, 'total_queries': 198}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['蒸菜', '清蒸鲈鱼', '豆豉蒸排骨', '粉蒸肉', '蒸茄子', '蒸南瓜', '豆豉', '泡椒', '花椒', '辣椒']
- topic_keywords: ['川菜', '川味', '清爽', '蒸制', '少油', '鲜香', '微辣', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5782

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '川味', '清爽', '蒸制', '少油', '鲜香', '微辣', '家常菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 61

## Hybrid Branch Status / entity_level
- keywords: ['蒸菜', '清蒸鲈鱼', '豆豉蒸排骨', '粉蒸肉', '蒸茄子', '蒸南瓜', '豆豉', '泡椒', '花椒', '辣椒']
- requested_k: 10
- actual_count: 6
- fallback_count: 0
- duration_ms: 69

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 322

## Hybrid Branch Summary
- entity_count: 6
- topic_count: 10
- vector_count: 10
- origin_len: 26

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 26
- after_count: 22
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['去腥', '腌（肉）']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 23
- duration_ms: 17344
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '素菜': 2, '主食,凉菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 蒜蓉空心菜
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23478
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:37:12.233
- end: 2026-08-11T18:37:45.090
- duration_ms: 32857
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1818
- retrieval_levels: ['context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level']
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
- chunk_count: 741
- redacted_field: 8737
- total_duration_ms: 23885
- fallback_used: False

## Final Output
- answer_chars: 899
- answer_hash: 2bf337de342ab90d
- success: True

## Request Complete
- request_end: 2026-08-11T18:38:08.995
- request_duration_ms: 56763
- success: True
- final_source: generation

