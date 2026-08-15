# RAG Process

audit_id: 20260811_194908_660_abb01bfe
timestamp: 2026-08-11T19:49:08.661
## Request
- original_query: 干豆腐能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: 3184b3fb222dadf9
- session_id: 2026-08-12-真实考试-001:new:S04-C-10
- request_mode: stream
- request_start: 2026-08-11T19:49:08.662
- evaluation_sample_id: 20260811_194908_660_abb01bfe
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:49:08.662
- end: 2026-08-11T19:49:08.662
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:49:08.663
- end: 2026-08-11T19:49:08.663
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 37
- enhanced_query_length: 37
- enhanced_query_hash: 3184b3fb222dadf9

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:49:08.669
- end: 2026-08-11T19:49:08.669
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:49:08.669+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:49:08.670
- end: 2026-08-11T19:49:08.670
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:49:08.669+00:00
- result_count: 1

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:49:08.671
- end: 2026-08-11T19:49:08.671
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:49:08.671+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:49:08.673
- end: 2026-08-11T19:49:08.673
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:49:08.671+00:00
- result_count: 3

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:49:08.674
- end: 2026-08-11T19:49:08.674
- duration_ms: 0
- template_id: ingredient_recipes_v1
- graph_fact_status: verified
- graph_fact_count: 2
- limitations: []
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1368
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 2
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
- chunk_count: 63
- redacted_field: 1760
- total_duration_ms: 3052
- fallback_used: False

## Final Output
- answer_chars: 88
- answer_hash: f7b585ded9239bac
- success: True

## Request Complete
- request_end: 2026-08-11T19:49:11.753
- request_duration_ms: 3091
- success: True
- final_source: generation

