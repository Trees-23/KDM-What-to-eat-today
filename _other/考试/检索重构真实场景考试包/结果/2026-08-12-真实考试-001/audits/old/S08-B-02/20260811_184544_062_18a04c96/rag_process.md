# RAG Process

audit_id: 20260811_184544_062_18a04c96
timestamp: 2026-08-11T18:45:44.064
## Request
- original_query: 知识库里有云岚12号幻味砂锅这道菜吗？如果有请给做法。
- original_query_hash: f47e58546ea6057b
- session_id: 2026-08-12-真实考试-001:old:S08-B-02
- request_mode: stream
- request_start: 2026-08-11T18:45:44.064
- evaluation_sample_id: 20260811_184544_062_18a04c96
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:45:44.065
- end: 2026-08-11T18:45:44.065
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:45:44.065
- end: 2026-08-11T18:45:44.065
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: f47e58546ea6057b

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:45:44.065
- end: 2026-08-11T18:45:44.065
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: f47e58546ea6057b
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:45:44.065
- end: 2026-08-11T18:45:50.339
- duration_ms: 6273
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.15
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 查询核心是确认知识库中是否存在“云岚12号幻味砂锅”这一特定菜品，并在存在时提取其做法，属于单一命名实体的条件式事实检索与内容抽取。无需多跳推理、因果分析或实体关系对比；可先通过关键词、别名匹配和向量语义召回定位菜品文档，再抽取其中的做法字段或步骤。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 176, 'graph_rag_count': 33, 'total_queries': 209}
- route_stats_after: {'traditional_count': 177, 'graph_rag_count': 33, 'total_queries': 210}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚12号幻味砂锅']
- topic_keywords: ['砂锅菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3417

## Hybrid Branch Status / entity_level
- keywords: ['云岚12号幻味砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 3

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 3

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 393

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 0
- vector_count: 10
- origin_len: 10

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 10
- after_count: 10
- duplicate_count: 0

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 7
- doc_names: ['去腥']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 11
- duration_ms: 14536
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 1, '烹饪技巧': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18360
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:45:44.065
- end: 2026-08-11T18:46:08.701
- duration_ms: 24635
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1770
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
- chunk_count: 164
- redacted_field: 2814
- total_duration_ms: 6313
- fallback_used: False

## Final Output
- answer_chars: 206
- answer_hash: 577b293587f7d7ac
- success: True

## Request Complete
- request_end: 2026-08-11T18:46:15.042
- request_duration_ms: 30977
- success: True
- final_source: generation

