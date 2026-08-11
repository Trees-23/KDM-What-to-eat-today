# RAG Process

audit_id: 20260811_170234_963_d0bb92a2
timestamp: 2026-08-11T17:02:34.964
## Request
- original_query: 请说明“油温判断技巧及常见温度和单位换算表”这个技巧的关键要点和适用情形。
- original_query_hash: 48d003e715545cd7
- session_id: 2026-08-12-真实考试-001:old:S03-A-04
- request_mode: stream
- request_start: 2026-08-11T17:02:34.964
- evaluation_sample_id: 20260811_170234_963_d0bb92a2
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:02:34.965
- end: 2026-08-11T17:02:34.965
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:02:34.966
- end: 2026-08-11T17:02:34.966
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 37
- enhanced_query_length: 37
- enhanced_query_hash: 48d003e715545cd7

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:02:34.966
- end: 2026-08-11T17:02:34.966
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 37
- analysis_input_query_hash: 48d003e715545cd7
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:02:34.967
- end: 2026-08-11T17:02:41.920
- duration_ms: 6953
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.42
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询的核心是解释一项烹饪技巧“油温判断”，并关联常见温度区间、温度单位换算及其适用烹饪场景。需要将检索到的油温判断方法、摄氏度/华氏度换算表和煎炸炒等场景进行归纳匹配，因此存在轻度综合推理需求；但不涉及跨领域、多实体的复杂关系网络或深层因果链。适合采用hybrid_traditional，通过关键词检索、语义召回和结构化温度表匹配即可获得高质量答案。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 63, 'graph_rag_count': 0, 'total_queries': 63}
- route_stats_after: {'traditional_count': 64, 'graph_rag_count': 0, 'total_queries': 64}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['油温判断技巧', '常见温度和单位换算表', '温度计']
- topic_keywords: ['烹饪技巧', '油温', '火候', '油炸', '煎炒', '温度换算', '摄氏度', '华氏度']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4455

## Hybrid Branch Status / entity_level
- keywords: ['油温判断技巧', '常见温度和单位换算表', '温度计']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 40

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '油温', '火候', '油炸', '煎炒', '温度换算', '摄氏度', '华氏度']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 56

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 624

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 10
- vector_count: 10
- origin_len: 22

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 22
- after_count: 15
- duplicate_count: 7

## Hybrid Technique Expansion
- enabled: True
- seed_count: 4
- expanded_count: 9
- doc_names: ['炒/煎', '厨房准备']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 16
- duration_ms: 16914
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 1, 'TechniqueChunk': 1, '烹饪技巧': 2, '荤菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22032
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:02:34.967
- end: 2026-08-11T17:03:03.954
- duration_ms: 28987
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4670
- retrieval_levels: ['', 'context_expansion', 'entity', 'topic']
- search_types: ['entity_level', 'technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 951
- redacted_field: 2201
- total_duration_ms: 20776
- fallback_used: False

## Final Output
- answer_chars: 1362
- answer_hash: 8bd3056cd9963ca6
- success: True

## Request Complete
- request_end: 2026-08-11T17:03:24.747
- request_duration_ms: 49783
- success: True
- final_source: generation

