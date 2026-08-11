# RAG Process

audit_id: 20260811_195057_567_82ebc41b
timestamp: 2026-08-11T19:50:57.568
## Request
- original_query: 今天胃口一般，想吃清爽一点的川菜，有哪些做法比较贴近这种偏好？
- original_query_hash: 6716844045ad84fb
- session_id: 2026-08-12-真实考试-001:new:S07-B-10
- request_mode: stream
- request_start: 2026-08-11T19:50:57.569
- evaluation_sample_id: 20260811_195057_567_82ebc41b
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:50:57.569
- end: 2026-08-11T19:50:57.569
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:50:57.569
- end: 2026-08-11T19:50:57.569
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 31
- enhanced_query_length: 31
- enhanced_query_hash: 6716844045ad84fb

## Errors
- stage: stream_request
- status: error
- error_type: ProgrammingError
- error_message: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 123672818324224 and this is thread id 123666372220608.

## Request Complete
- request_end: 2026-08-11T19:50:57.570
- request_duration_ms: 1
- success: False
- final_source: error

