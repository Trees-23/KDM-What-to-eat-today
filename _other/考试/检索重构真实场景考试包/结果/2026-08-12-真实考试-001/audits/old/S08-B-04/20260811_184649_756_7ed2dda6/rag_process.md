# RAG Process

audit_id: 20260811_184649_756_7ed2dda6
timestamp: 2026-08-11T18:46:49.758
## Request
- original_query: 知识库里有云岚14号幻味砂锅这道菜吗？如果有请给做法。
- original_query_hash: 7e14ffc0a43f447d
- session_id: 2026-08-12-真实考试-001:old:S08-B-04
- request_mode: stream
- request_start: 2026-08-11T18:46:49.759
- evaluation_sample_id: 20260811_184649_756_7ed2dda6
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:46:49.760
- end: 2026-08-11T18:46:49.760
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:46:49.760
- end: 2026-08-11T18:46:49.760
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: 7e14ffc0a43f447d

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:46:49.761
- end: 2026-08-11T18:46:49.761
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: 7e14ffc0a43f447d
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:46:49.761
- end: 2026-08-11T18:46:55.693
- duration_ms: 5932
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询本质上是对知识库中指定菜品“云岚14号幻味砂锅”的存在性检索，并在命中后获取其关联的做法内容，属于条件式的直接信息查找。无需多跳推理、因果分析或跨实体对比；可先通过关键词/倒排索引进行精确菜名召回，再结合向量检索处理名称变体、别名或文本表述差异，并从命中文档中抽取做法。明确实体主要包括菜品实体“云岚14号幻味砂锅”和知识库实体。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 178, 'graph_rag_count': 33, 'total_queries': 211}
- route_stats_after: {'traditional_count': 179, 'graph_rag_count': 33, 'total_queries': 212}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚14号幻味砂锅']
- topic_keywords: ['砂锅菜', '做法']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3020

## Hybrid Branch Status / entity_level
- keywords: ['云岚14号幻味砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 11

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '做法']
- requested_k: 10
- actual_count: 8
- fallback_count: 8
- duration_ms: 60

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 499

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 8
- vector_count: 10
- origin_len: 18

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 18
- after_count: 16
- duplicate_count: 2

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
- candidate_count: 17
- duration_ms: 17200
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 1, '素菜': 1, '烹饪技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 蚝油生菜
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20750
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:46:49.761
- end: 2026-08-11T18:47:16.445
- duration_ms: 26683
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
- chunk_count: 163
- redacted_field: 12592
- total_duration_ms: 16122
- fallback_used: False

## Final Output
- answer_chars: 205
- answer_hash: cb6463d3bbe02fa6
- success: True

## Request Complete
- request_end: 2026-08-11T18:47:32.600
- request_duration_ms: 42840
- success: True
- final_source: generation

