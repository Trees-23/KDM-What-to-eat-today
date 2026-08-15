# RAG Process

audit_id: 20260811_163026_859_29d254f8
timestamp: 2026-08-11T16:30:26.860
## Request
- original_query: 凉拌黄瓜从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 3a5cbfd63d2f53f7
- session_id: 2026-08-12-真实考试-001:old:S01-B-08
- request_mode: stream
- request_start: 2026-08-11T16:30:26.860
- evaluation_sample_id: 20260811_163026_859_29d254f8
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:30:26.861
- end: 2026-08-11T16:30:26.861
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:30:26.861
- end: 2026-08-11T16:30:26.861
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: 3a5cbfd63d2f53f7

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:30:26.862
- end: 2026-08-11T16:30:26.862
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: 3a5cbfd63d2f53f7
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:30:26.863
- end: 2026-08-11T16:30:33.462
- duration_ms: 6599
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是针对“凉拌黄瓜”菜品做法的直接流程检索，核心需求是从知识库中定位备料、处理、调味、拌制及装盘等步骤。虽然包含“从备料到出锅”的顺序性要求，但凉拌菜通常不涉及实际烹饪出锅，知识库可通过关键词、菜名、步骤字段和语义检索直接返回标准做法。无需多跳推理、因果分析或不同方案对比。明确实体主要包括菜品实体“凉拌黄瓜”和操作流程实体“备料到出锅/制作步骤”。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 17, 'graph_rag_count': 0, 'total_queries': 17}
- route_stats_after: {'traditional_count': 18, 'graph_rag_count': 0, 'total_queries': 18}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['凉拌黄瓜', '黄瓜', '凉拌']
- topic_keywords: ['凉拌菜', '家常菜', '快手菜', '烹饪技巧', '调味', '备料']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5317

## Hybrid Branch Status / topic_level
- keywords: ['凉拌菜', '家常菜', '快手菜', '烹饪技巧', '调味', '备料']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 59

## Hybrid Branch Status / entity_level
- keywords: ['凉拌黄瓜', '黄瓜', '凉拌']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 145

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 398

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 22
- duplicate_count: 8

## Hybrid Technique Expansion
- enabled: True
- seed_count: 8
- expanded_count: 9
- doc_names: ['厨房准备']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 23
- duration_ms: 29100
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 1, '半成品': 1, 'TechniqueDoc': 2, '荤菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 黄瓜炒肉
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 34854
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:30:26.863
- end: 2026-08-11T16:31:08.318
- duration_ms: 41455
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 7600
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
- chunk_count: 336
- redacted_field: 4583
- total_duration_ms: 12738
- fallback_used: False

## Final Output
- answer_chars: 485
- answer_hash: f6b1051b25de9ea4
- success: True

## Request Complete
- request_end: 2026-08-11T16:31:21.083
- request_duration_ms: 54222
- success: True
- final_source: generation

