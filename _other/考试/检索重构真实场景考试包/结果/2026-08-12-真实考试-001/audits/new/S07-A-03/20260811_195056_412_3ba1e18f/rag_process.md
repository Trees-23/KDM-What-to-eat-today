# RAG Process

audit_id: 20260811_195056_412_3ba1e18f
timestamp: 2026-08-11T19:50:56.413
## Request
- original_query: 偏好清淡一些的川菜。请推荐几个可考虑的菜。
- original_query_hash: 74269ebe589ddb51
- session_id: 2026-08-12-真实考试-001:new:S07-A-03
- request_mode: stream
- request_start: 2026-08-11T19:50:56.413
- evaluation_sample_id: 20260811_195056_412_3ba1e18f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:50:56.414
- end: 2026-08-11T19:50:56.414
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:50:56.414
- end: 2026-08-11T19:50:56.415
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 74269ebe589ddb51

## Errors
- stage: stream_request
- status: error
- error_type: ProgrammingError
- error_message: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 123672818324224 and this is thread id 123666372220608.

## Request Complete
- request_end: 2026-08-11T19:50:56.416
- request_duration_ms: 2
- success: False
- final_source: error

