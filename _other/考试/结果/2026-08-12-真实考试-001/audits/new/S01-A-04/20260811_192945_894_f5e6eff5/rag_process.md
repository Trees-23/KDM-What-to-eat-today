# RAG Process

audit_id: 20260811_192945_894_f5e6eff5
timestamp: 2026-08-11T19:29:45.895
## Request
- original_query: 请给出糖醋鲤鱼的完整做法，包括主要食材和步骤。
- original_query_hash: 4033029c0d78d10e
- session_id: 2026-08-12-真实考试-001:new:S01-A-04
- request_mode: stream
- request_start: 2026-08-11T19:29:45.895
- evaluation_sample_id: 20260811_192945_894_f5e6eff5
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:29:45.896
- end: 2026-08-11T19:29:45.896
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:29:45.896
- end: 2026-08-11T19:29:45.896
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: 4033029c0d78d10e

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:29:45.911
- end: 2026-08-11T19:29:45.911
- duration_ms: 0
- entity_id: 201000290
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:29:45.911
- end: 2026-08-11T19:29:45.911
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:29:45.911
- end: 2026-08-11T19:29:45.911
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: 4033029c0d78d10e
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:29:45.911
- end: 2026-08-11T19:29:55.265
- duration_ms: 9353
- analysis_mode: llm
- query_complexity: 0.2
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询围绕单一菜品实体“糖醋鲤鱼”获取标准化制作信息，目标明确：主要食材与烹饪步骤。无需多跳推理、因果分析或跨菜品对比，仅需从菜谱、烹饪知识库或文档中检索并整合直接信息。明确实体为“糖醋鲤鱼”，实体类型为菜品；“主要食材”和“步骤”属于所请求的信息字段，而非独立命名实体。因此适合使用hybrid_traditional进行关键词、语义及结构化字段检索。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 3, 'graph_rag_count': 0, 'total_queries': 3}
- route_stats_after: {'traditional_count': 4, 'graph_rag_count': 0, 'total_queries': 4}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['糖醋鲤鱼', '鲤鱼', '番茄酱', '白糖', '香醋', '淀粉', '葱', '姜', '蒜']
- topic_keywords: ['鲁菜', '糖醋口味', '家常菜', '宴客菜', '烹饪步骤', '油炸', '调味', '火候']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3269

## Hybrid Branch Status / entity_level
- keywords: ['糖醋鲤鱼', '鲤鱼', '番茄酱', '白糖', '香醋', '淀粉', '葱', '姜', '蒜']
- requested_k: 10
- actual_count: 10
- fallback_count: 1
- duration_ms: 97

## Hybrid Branch Status / topic_level
- keywords: ['鲁菜', '糖醋口味', '家常菜', '宴客菜', '烹饪步骤', '油炸', '调味', '火候']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 107

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 338

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 26
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 26
- duration_ms: 20505
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '汤类': 1, 'Ingredient': 1, '荤菜': 1}
- deferred_count: 5
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24142
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:29:45.911
- end: 2026-08-11T19:30:19.409
- duration_ms: 33497
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2690
- retrieval_levels: ['', 'entity', 'topic']
- search_types: ['entity_level', 'topic_level', 'vector_enhanced']
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
- chunk_count: 701
- redacted_field: 1726
- total_duration_ms: 16481
- fallback_used: False

## Final Output
- answer_chars: 913
- answer_hash: db762ad48243fd24
- success: True

## Request Complete
- request_end: 2026-08-11T19:30:35.929
- request_duration_ms: 50034
- success: True
- final_source: generation

