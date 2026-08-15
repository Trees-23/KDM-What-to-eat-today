# RAG Process

audit_id: 20260811_164826_474_c2b23863
timestamp: 2026-08-11T16:48:26.477
## Request
- original_query: 刚开始做辣椒炒肉时，第一步具体要处理什么？
- original_query_hash: 6b4359be122d40e9
- session_id: 2026-08-12-真实考试-001:old:S02-B-04
- request_mode: stream
- request_start: 2026-08-11T16:48:26.477
- evaluation_sample_id: 20260811_164826_474_c2b23863
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:48:26.478
- end: 2026-08-11T16:48:26.478
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:48:26.478
- end: 2026-08-11T16:48:26.478
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 6b4359be122d40e9

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:48:26.479
- end: 2026-08-11T16:48:26.479
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: 6b4359be122d40e9
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:48:26.479
- end: 2026-08-11T16:48:32.032
- duration_ms: 5553
- analysis_mode: llm
- query_complexity: 0.15
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对“辣椒炒肉”烹饪流程中起始步骤的直接事实查找，目标明确且答案通常存在于单一菜谱步骤中。无需多跳推理、因果分析或不同方案对比。明确实体主要包括菜品“辣椒炒肉”和流程阶段“第一步（刚开始做）”。适合通过关键词检索、菜谱步骤排序和语义匹配完成，因此推荐hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 43, 'graph_rag_count': 0, 'total_queries': 43}
- route_stats_after: {'traditional_count': 44, 'graph_rag_count': 0, 'total_queries': 44}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['辣椒炒肉', '辣椒', '猪肉']
- topic_keywords: ['烹饪技巧', '食材预处理', '备菜', '火候', '快炒']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 10753

## Hybrid Branch Status / entity_level
- keywords: ['辣椒炒肉', '辣椒', '猪肉']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 31

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '食材预处理', '备菜', '火候', '快炒']
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
- duration_ms: 678

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 10
- vector_count: 10
- origin_len: 23

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 23
- after_count: 20
- duplicate_count: 3

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
- candidate_count: 21
- duration_ms: 21771
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '素菜': 2, '烹饪技巧': 1}
- deferred_count: 4
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 虎皮青椒
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 33229
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:48:26.479
- end: 2026-08-11T16:49:05.263
- duration_ms: 38784
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3349
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
- chunk_count: 61
- redacted_field: 2430
- total_duration_ms: 4480
- fallback_used: False

## Final Output
- answer_chars: 80
- answer_hash: f6f9aa6e69077455
- success: True

## Request Complete
- request_end: 2026-08-11T16:49:09.769
- request_duration_ms: 43291
- success: True
- final_source: generation

