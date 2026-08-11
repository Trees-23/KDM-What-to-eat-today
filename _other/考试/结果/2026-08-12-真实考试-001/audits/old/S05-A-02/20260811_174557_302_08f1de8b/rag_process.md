# RAG Process

audit_id: 20260811_174557_302_08f1de8b
timestamp: 2026-08-11T17:45:57.303
## Request
- original_query: 猪肉适合搭配什么蔬菜？
- original_query_hash: 03e246776c535772
- session_id: 2026-08-12-真实考试-001:old:S05-A-02
- request_mode: stream
- request_start: 2026-08-11T17:45:57.303
- evaluation_sample_id: 20260811_174557_302_08f1de8b
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:45:57.303
- end: 2026-08-11T17:45:57.303
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:45:57.304
- end: 2026-08-11T17:45:57.304
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 11
- enhanced_query_length: 11
- enhanced_query_hash: 03e246776c535772

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:45:57.304
- end: 2026-08-11T17:45:57.304
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 11
- analysis_input_query_hash: 03e246776c535772
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:45:57.304
- end: 2026-08-11T17:46:05.129
- duration_ms: 7824
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.55
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询是围绕“猪肉”与“蔬菜”之间搭配关系的直接信息查找，目标是获取适宜搭配的蔬菜列表或常见烹饪组合。虽然包含实体间关系，但通常不需要多跳推理、因果分析或复杂对比；可通过关键词检索、语义召回及菜谱/饮食知识库排序直接获得高质量答案。明确实体包括“猪肉”（肉类食材）和“蔬菜”（食材类别）。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 110, 'graph_rag_count': 11, 'total_queries': 121}
- route_stats_after: {'traditional_count': 111, 'graph_rag_count': 11, 'total_queries': 122}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['猪肉', '白菜', '土豆', '青椒', '芹菜', '萝卜', '豆角', '莲藕', '蘑菇', '西兰花']
- topic_keywords: ['荤素搭配', '营养均衡', '家常菜', '下饭菜', '猪肉搭配']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7481

## Hybrid Branch Status / topic_level
- keywords: ['荤素搭配', '营养均衡', '家常菜', '下饭菜', '猪肉搭配']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 24

## Hybrid Branch Status / entity_level
- keywords: ['猪肉', '白菜', '土豆', '青椒', '芹菜', '萝卜', '豆角', '莲藕', '蘑菇', '西兰花']
- requested_k: 10
- actual_count: 9
- fallback_count: 0
- duration_ms: 62

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 395

## Hybrid Branch Summary
- entity_count: 9
- topic_count: 2
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 19
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 3
- expanded_count: 9
- doc_names: ['揭秘食材搭配的智慧：这些食物不宜同食', '如何决策吃什么', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 20
- duration_ms: 15143
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 1, '烹饪技巧': 1, '通用知识': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23057
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:45:57.304
- end: 2026-08-11T17:46:28.188
- duration_ms: 30883
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4836
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
- chunk_count: 280
- redacted_field: 5621
- total_duration_ms: 10965
- fallback_used: False

## Final Output
- answer_chars: 338
- answer_hash: 6296265c930008ec
- success: True

## Request Complete
- request_end: 2026-08-11T17:46:39.172
- request_duration_ms: 41869
- success: True
- final_source: generation

