# RAG Process

audit_id: 20260811_170854_677_1acecc47
timestamp: 2026-08-11T17:08:54.681
## Request
- original_query: 请说明“蒸”这个技巧的关键要点和适用情形。
- original_query_hash: adbb3f8c1e7dd1ee
- session_id: 2026-08-12-真实考试-001:old:S03-A-10
- request_mode: stream
- request_start: 2026-08-11T17:08:54.682
- evaluation_sample_id: 20260811_170854_677_1acecc47
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:08:54.683
- end: 2026-08-11T17:08:54.683
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:08:54.684
- end: 2026-08-11T17:08:54.684
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: adbb3f8c1e7dd1ee

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:08:54.685
- end: 2026-08-11T17:08:54.685
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: adbb3f8c1e7dd1ee
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:08:54.686
- end: 2026-08-11T17:09:03.756
- duration_ms: 9069
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.3
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 查询围绕单一烹饪技法“蒸”展开，要求说明其操作关键要点及适用情形，属于定义性与实践性知识检索。虽然需要将火候、时间、水量、密封性、食材特性等要点与适用食材/菜品进行对应，但不涉及跨领域、多实体的复杂关系网络或多跳推理。适合使用关键词检索结合语义检索的 hybrid_traditional 策略，以召回烹饪技法说明、操作规范和适用场景等资料。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 69, 'graph_rag_count': 0, 'total_queries': 69}
- route_stats_after: {'traditional_count': 70, 'graph_rag_count': 0, 'total_queries': 70}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['蒸', '蒸制', '蒸锅', '蒸笼']
- topic_keywords: ['烹饪技巧', '火候', '蒸汽', '熟度', '保留营养', '清淡', '少油', '食品安全']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3265

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '火候', '蒸汽', '熟度', '保留营养', '清淡', '少油', '食品安全']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 65

## Hybrid Branch Status / entity_level
- keywords: ['蒸', '蒸制', '蒸锅', '蒸笼']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 243

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 406

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
- seed_count: 10
- expanded_count: 9
- doc_names: ['蒸（米）/炖（使用电饭煲/高压锅/电压力锅）', '使用微波炉']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 22
- duration_ms: 22516
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 2, 'TechniqueChunk': 2, '烹饪技巧': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 26231
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:08:54.686
- end: 2026-08-11T17:09:29.988
- duration_ms: 35302
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 5395
- retrieval_levels: ['context_expansion', 'entity']
- search_types: ['entity_level', 'technique_expansion']
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
- chunk_count: 707
- redacted_field: 2005
- total_duration_ms: 15339
- fallback_used: False

## Final Output
- answer_chars: 895
- answer_hash: 6839b9055db8c454
- success: True

## Request Complete
- request_end: 2026-08-11T17:09:45.347
- request_duration_ms: 50665
- success: True
- final_source: generation

