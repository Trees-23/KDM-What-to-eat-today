# RAG Process

audit_id: 20260811_184428_800_25e17dc0
timestamp: 2026-08-11T18:44:28.802
## Request
- original_query: 云岚10号幻味砂锅怎么做？
- original_query_hash: 3be26386e615ed40
- session_id: 2026-08-12-真实考试-001:old:S08-A-10
- request_mode: stream
- request_start: 2026-08-11T18:44:28.804
- evaluation_sample_id: 20260811_184428_800_25e17dc0
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:44:28.805
- end: 2026-08-11T18:44:28.805
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:44:28.805
- end: 2026-08-11T18:44:28.805
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 13
- enhanced_query_length: 13
- enhanced_query_hash: 3be26386e615ed40

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:44:28.806
- end: 2026-08-11T18:44:28.806
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 13
- analysis_input_query_hash: 3be26386e615ed40
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:44:28.806
- end: 2026-08-11T18:44:35.769
- duration_ms: 6963
- analysis_mode: llm
- query_complexity: 0.2
- relationship_intensity: 0.15
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询的核心意图是获取“云岚10号幻味砂锅”的制作方法，属于针对特定菜品或商品名称的直接信息查找。可识别实体包括“云岚10号”（可能为品牌、门店、产品系列或菜品编号）和“幻味砂锅”（菜品名称）。查询不要求分析实体间的复杂关联，也不涉及多跳推理、因果分析或方案对比；适合通过关键词检索、菜谱文档召回及语义匹配的hybrid_traditional策略处理。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 174, 'graph_rag_count': 33, 'total_queries': 207}
- route_stats_after: {'traditional_count': 175, 'graph_rag_count': 33, 'total_queries': 208}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚10号幻味砂锅', '砂锅']
- topic_keywords: ['砂锅菜', '烹饪方法', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4940

## Hybrid Branch Status / entity_level
- keywords: ['云岚10号幻味砂锅', '砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 3

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '烹饪方法', '家常菜']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 15

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 374

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 2
- vector_count: 10
- origin_len: 12

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 12
- after_count: 12
- duplicate_count: 0

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 8
- doc_names: ['炒/煎']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 13
- duration_ms: 15710
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 1, '半成品': 1, '荤菜': 2, '水产': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 蛏抱蛋
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21041
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:44:28.806
- end: 2026-08-11T18:44:56.812
- duration_ms: 28006
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2668
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
- chunk_count: 480
- redacted_field: 4792
- total_duration_ms: 13310
- fallback_used: False

## Final Output
- answer_chars: 626
- answer_hash: 957863d4311151e1
- success: True

## Request Complete
- request_end: 2026-08-11T18:45:10.141
- request_duration_ms: 41336
- success: True
- final_source: generation

