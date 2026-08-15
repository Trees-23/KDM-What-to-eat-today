# RAG Process

audit_id: 20260811_164706_322_4c2dc961
timestamp: 2026-08-11T16:47:06.325
## Request
- original_query: 刚开始做宫保鸡丁时，第一步具体要处理什么？
- original_query_hash: 386a5921ae4811b1
- session_id: 2026-08-12-真实考试-001:old:S02-B-02
- request_mode: stream
- request_start: 2026-08-11T16:47:06.325
- evaluation_sample_id: 20260811_164706_322_4c2dc961
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:47:06.325
- end: 2026-08-11T16:47:06.325
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:47:06.326
- end: 2026-08-11T16:47:06.326
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 386a5921ae4811b1

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:47:06.326
- end: 2026-08-11T16:47:06.326
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: 386a5921ae4811b1
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:47:06.326
- end: 2026-08-11T16:47:12.489
- duration_ms: 6162
- analysis_mode: llm
- query_complexity: 0.18
- relationship_intensity: 0.12
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对“宫保鸡丁”制作流程中起始步骤的直接、单点信息查找，核心目标是定位菜谱或烹饪步骤中的第一步具体操作。明确实体主要包括“宫保鸡丁”（菜品）和“第一步/刚开始”（流程阶段或步骤位置）。不需要多跳推理、因果分析或对比分析；使用关键词检索结合语义检索即可高效召回包含制作步骤的菜谱内容。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 41, 'graph_rag_count': 0, 'total_queries': 41}
- route_stats_after: {'traditional_count': 42, 'graph_rag_count': 0, 'total_queries': 42}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['宫保鸡丁', '鸡肉', '花生', '干辣椒', '花椒', '腌制']
- topic_keywords: ['川菜', '烹饪步骤', '前期处理', '腌肉', '去腥', '入味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3322

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '烹饪步骤', '前期处理', '腌肉', '去腥', '入味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 74

## Hybrid Branch Status / entity_level
- keywords: ['宫保鸡丁', '鸡肉', '花生', '干辣椒', '花椒', '腌制']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 203

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 744

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 25
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 5
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 26
- duration_ms: 29522
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, 'TechniqueDoc': 2, 'TechniqueChunk': 1}
- deferred_count: 4
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 小炒鸡肝
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 33636
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:47:06.326
- end: 2026-08-11T16:47:46.126
- duration_ms: 39800
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 7154
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
- chunk_count: 83
- redacted_field: 2404
- total_duration_ms: 4128
- fallback_used: False

## Final Output
- answer_chars: 118
- answer_hash: 10b952860898970f
- success: True

## Request Complete
- request_end: 2026-08-11T16:47:50.288
- request_duration_ms: 43962
- success: True
- final_source: generation

