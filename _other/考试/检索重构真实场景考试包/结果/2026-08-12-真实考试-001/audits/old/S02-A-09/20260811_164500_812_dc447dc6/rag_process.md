# RAG Process

audit_id: 20260811_164500_812_dc447dc6
timestamp: 2026-08-11T16:45:00.818
## Request
- original_query: 咖喱炒蟹的第 1 步应该怎么做？
- original_query_hash: a36b27054451caab
- session_id: 2026-08-12-真实考试-001:old:S02-A-09
- request_mode: stream
- request_start: 2026-08-11T16:45:00.819
- evaluation_sample_id: 20260811_164500_812_dc447dc6
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:45:00.820
- end: 2026-08-11T16:45:00.820
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:45:00.821
- end: 2026-08-11T16:45:00.821
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: a36b27054451caab

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:45:00.822
- end: 2026-08-11T16:45:00.822
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 16
- analysis_input_query_hash: a36b27054451caab
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:45:00.823
- end: 2026-08-11T16:45:09.598
- duration_ms: 8774
- analysis_mode: llm
- query_complexity: 0.2
- relationship_intensity: 0.25
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是针对“咖喱炒蟹”这一菜谱的明确步骤定位问题，目标是查找其“第1步”的具体操作。查询不要求跨实体关联、因果解释、对比判断或多跳推理，只需通过关键词匹配、菜谱文档检索及步骤排序即可得到答案。明确实体包括菜品“咖喱炒蟹”和流程节点“第1步”，实体关系为单一菜谱与其制作步骤之间的弱流程关系，适合采用hybrid_traditional进行关键词与语义混合检索。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 38, 'graph_rag_count': 0, 'total_queries': 38}
- route_stats_after: {'traditional_count': 39, 'graph_rag_count': 0, 'total_queries': 39}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['咖喱炒蟹', '咖喱', '螃蟹']
- topic_keywords: ['烹饪步骤', '炒蟹', '海鲜料理']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7529

## Hybrid Branch Status / topic_level
- keywords: ['烹饪步骤', '炒蟹', '海鲜料理']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 13

## Hybrid Branch Status / entity_level
- keywords: ['咖喱炒蟹', '咖喱', '螃蟹']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 24

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 593

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 0
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 6
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 6
- duration_ms: 11795
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 1, '主食': 1, '荤菜': 2, '素菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 19938
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:45:00.823
- end: 2026-08-11T16:45:29.537
- duration_ms: 28713
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3782
- retrieval_levels: ['']
- search_types: ['vector_enhanced']
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
- chunk_count: 75
- redacted_field: 4375
- total_duration_ms: 6092
- fallback_used: False

## Final Output
- answer_chars: 85
- answer_hash: 79c1055e6b2228ce
- success: True

## Request Complete
- request_end: 2026-08-11T16:45:35.654
- request_duration_ms: 34835
- success: True
- final_source: generation

