# RAG Process

audit_id: 20260811_184732_618_991b7368
timestamp: 2026-08-11T18:47:32.620
## Request
- original_query: 知识库里有云岚15号幻味砂锅这道菜吗？如果有请给做法。
- original_query_hash: 85dacf1a18455f34
- session_id: 2026-08-12-真实考试-001:old:S08-B-05
- request_mode: stream
- request_start: 2026-08-11T18:47:32.621
- evaluation_sample_id: 20260811_184732_618_991b7368
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:47:32.622
- end: 2026-08-11T18:47:32.622
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:47:32.623
- end: 2026-08-11T18:47:32.623
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: 85dacf1a18455f34

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:47:32.624
- end: 2026-08-11T18:47:32.624
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: 85dacf1a18455f34
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:47:32.625
- end: 2026-08-11T18:47:42.149
- duration_ms: 9524
- analysis_mode: llm
- query_complexity: 0.3
- relationship_intensity: 0.15
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询的核心是定位单一道菜品实体“云岚15号幻味砂锅”，先判断知识库中是否存在对应条目，再在存在时提取其做法。查询仅包含条件式的信息检索与字段获取，不涉及多跳推理、因果分析、实体关系网络或对比分析。建议采用 hybrid_traditional，通过关键词、别名匹配及语义检索召回菜品文档，再抽取做法内容。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 179, 'graph_rag_count': 33, 'total_queries': 212}
- route_stats_after: {'traditional_count': 180, 'graph_rag_count': 33, 'total_queries': 213}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚15号幻味砂锅']
- topic_keywords: ['砂锅菜', '做法']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3071

## Hybrid Branch Status / entity_level
- keywords: ['云岚15号幻味砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 5

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '做法']
- requested_k: 10
- actual_count: 8
- fallback_count: 8
- duration_ms: 34

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 396

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 8
- vector_count: 10
- origin_len: 18

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 18
- after_count: 17
- duplicate_count: 1

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
- candidate_count: 18
- duration_ms: 18243
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
- hybrid_total_duration_ms: 21732
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:47:32.625
- end: 2026-08-11T18:48:03.883
- duration_ms: 31258
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1772
- retrieval_levels: ['', 'context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 162
- redacted_field: 2988
- total_duration_ms: 6284
- fallback_used: False

## Final Output
- answer_chars: 211
- answer_hash: 55e1d8aab455aac9
- success: True

## Request Complete
- request_end: 2026-08-11T18:48:10.202
- request_duration_ms: 37581
- success: True
- final_source: generation

