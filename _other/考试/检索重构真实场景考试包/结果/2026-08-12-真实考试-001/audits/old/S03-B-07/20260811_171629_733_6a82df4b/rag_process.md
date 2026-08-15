# RAG Process

audit_id: 20260811_171629_733_6a82df4b
timestamp: 2026-08-11T17:16:29.735
## Request
- original_query: 我想学食品安全，它的关键要点和适用场景是什么？
- original_query_hash: 1436cac013bff921
- session_id: 2026-08-12-真实考试-001:old:S03-B-07
- request_mode: stream
- request_start: 2026-08-11T17:16:29.735
- evaluation_sample_id: 20260811_171629_733_6a82df4b
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:16:29.736
- end: 2026-08-11T17:16:29.736
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:16:29.736
- end: 2026-08-11T17:16:29.736
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: 1436cac013bff921

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:16:29.737
- end: 2026-08-11T17:16:29.737
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: 1436cac013bff921
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:16:29.737
- end: 2026-08-11T17:16:39.456
- duration_ms: 9719
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.42
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.83
- reasoning: 该查询属于面向学习的概述性信息需求，核心是获取“食品安全”的关键知识点及其在不同场景中的应用。需要对食品安全概念、风险控制要点、法规规范、生产加工、餐饮服务、家庭储存等场景进行归纳和分类，因此存在一定的组织与轻度推理需求，但不要求追踪多实体之间的复杂关系网络。明确实体主要为“食品安全”和“适用场景”；其中“关键要点”是信息属性而非独立实体。建议采用hybrid_traditional，通过关键词检索、语义检索及权威法规/科普资料排序，覆盖定义、原则、风险类别与典型应用场景。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 76, 'graph_rag_count': 0, 'total_queries': 76}
- route_stats_after: {'traditional_count': 77, 'graph_rag_count': 0, 'total_queries': 77}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['食品安全']
- topic_keywords: ['食品安全', '食品卫生', '食材储存', '交叉污染', '生熟分开', '加热熟透', '保质期', '食品安全风险']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3751

## Hybrid Branch Status / topic_level
- keywords: ['食品安全', '食品卫生', '食材储存', '交叉污染', '生熟分开', '加热熟透', '保质期', '食品安全风险']
- requested_k: 10
- actual_count: 1
- fallback_count: 1
- duration_ms: 22

## Hybrid Branch Status / entity_level
- keywords: ['食品安全']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 116

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 583

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 1
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 13
- duplicate_count: 8

## Hybrid Technique Expansion
- enabled: True
- seed_count: 12
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 14
- duration_ms: 15236
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 2, 'TechniqueChunk': 2, '烹饪技巧': 1}
- deferred_count: 5
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 19616
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:16:29.737
- end: 2026-08-11T17:16:59.074
- duration_ms: 29336
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 6649
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
- chunk_count: 1443
- redacted_field: 2127
- total_duration_ms: 30726
- fallback_used: False

## Final Output
- answer_chars: 1859
- answer_hash: 6c93d44269629937
- success: True

## Request Complete
- request_end: 2026-08-11T17:17:29.831
- request_duration_ms: 60096
- success: True
- final_source: generation

