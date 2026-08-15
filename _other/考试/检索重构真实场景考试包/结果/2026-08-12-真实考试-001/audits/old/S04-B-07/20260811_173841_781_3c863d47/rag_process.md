# RAG Process

audit_id: 20260811_173841_781_3c863d47
timestamp: 2026-08-11T17:38:41.782
## Request
- original_query: 有普通面条可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: 437375ed91326e04
- session_id: 2026-08-12-真实考试-001:old:S04-B-07
- request_mode: stream
- request_start: 2026-08-11T17:38:41.782
- evaluation_sample_id: 20260811_173841_781_3c863d47
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:38:41.784
- end: 2026-08-11T17:38:41.784
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:38:41.785
- end: 2026-08-11T17:38:41.785
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 22
- enhanced_query_length: 22
- enhanced_query_hash: 437375ed91326e04

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:38:41.786
- end: 2026-08-11T17:38:41.786
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 22
- analysis_input_query_hash: 437375ed91326e04
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:38:41.786
- end: 2026-08-11T17:38:49.924
- duration_ms: 8137
- analysis_mode: llm
- query_complexity: 0.48
- relationship_intensity: 0.52
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心是以“普通面条”为食材，检索可制作的菜品及明确在配料表或做法中包含该食材的菜谱。其主要关系为“食材—菜品/菜谱”的包含与适配关系，需要对检索结果进行食材字段核验，避免返回仅使用意面、米粉、挂面替代品或未明确包含普通面条的菜谱。该任务不涉及复杂多跳关系、因果解释或跨实体网络推理，适合采用关键词、同义词扩展（如面条、挂面、切面）结合配料字段过滤与排序的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 105, 'graph_rag_count': 1, 'total_queries': 106}
- route_stats_after: {'traditional_count': 106, 'graph_rag_count': 1, 'total_queries': 107}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['普通面条', '炒面', '汤面', '拌面', '凉面', '焖面', '炸酱面', '意大利面']
- topic_keywords: ['面食', '家常菜', '快手菜', '主食', '面条菜谱', '食材搭配']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4827

## Hybrid Branch Status / entity_level
- keywords: ['普通面条', '炒面', '汤面', '拌面', '凉面', '焖面', '炸酱面', '意大利面']
- requested_k: 10
- actual_count: 4
- fallback_count: 0
- duration_ms: 39

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 458

## Hybrid Branch Status / topic_level
- keywords: ['面食', '家常菜', '快手菜', '主食', '面条菜谱', '食材搭配']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 9701

## Hybrid Branch Summary
- entity_count: 4
- topic_count: 10
- vector_count: 10
- origin_len: 24

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 24
- after_count: 12
- duplicate_count: 12

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 9
- doc_names: ['凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 13
- duration_ms: 15290
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'Ingredient': 1, '主食': 2, '荤菜': 1, '烹饪技巧': 1}
- deferred_count: 5
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 29845
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:38:41.786
- end: 2026-08-11T17:39:19.770
- duration_ms: 37983
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1689
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
- chunk_count: 218
- redacted_field: 7470
- total_duration_ms: 11367
- fallback_used: False

## Final Output
- answer_chars: 289
- answer_hash: 8ff45b46487acf6f
- success: True

## Request Complete
- request_end: 2026-08-11T17:39:31.150
- request_duration_ms: 49368
- success: True
- final_source: generation

