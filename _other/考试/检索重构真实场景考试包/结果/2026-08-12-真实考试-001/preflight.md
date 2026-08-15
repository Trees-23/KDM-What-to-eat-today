# 真实服务考试预检

- 运行编号：`2026-08-12-真实考试-001`
- 预检关闭时间：`2026-08-12T00:14:06+08:00`
- 实现提交：`8020edff2679b5e3c9e147202cdbd1f05fe44d50`
- 当前分支：`codex/exam-s03-ready`
- 目标基线：`origin/main` 的 `a22897275c26f89398b766af754c44452f2b35f6`
- 题库 SHA-256：`e5edfbced75e84002bdd5b25054bf0906a022b4073e03ab31a4c85010f494f79`
- `题库校验报告.md` 声明的 SHA-256：`e5edfbced75e84002bdd5b25054bf0906a022b4073e03ab31a4c85010f494f79`
- 静态题库重生成校验：`python _other/考试/工具/生成试卷.py` 成功生成 300 题，运行前后 SHA 一致且 Git 内容差异为空。
- `python _other/考试/工具/开考预检.py --probe-new-path`：退出码 `0`，JSON `status=ready`。

## 只读服务状态

- `GET /health`：`{"service": "RAG System", "status": "healthy", "timestamp": "2026-08-11 16:07:30.066800"}`
- 解析的运行时目标数：`210`。
- PDS：parents=`341`，chunks=`1333`；Milvus V2 行数=`1333`。
- Compose 容器状态：
```text
what-to-eat-backend|running|Up 25 minutes (healthy)
what-to-eat-frontend|exited|Exited (255) 9 hours ago
what-to-eat-milvus-etcd|running|Up 3 hours (healthy)
what-to-eat-milvus-minio|running|Up 3 hours (healthy)
what-to-eat-milvus-standalone|running|Up 3 hours (healthy)
what-to-eat-neo4j|running|Up 3 hours (healthy)
what-to-eat-neo4j-init|exited|Exited (0) 25 minutes ago
what-to-eat-nginx|exited|Exited (255) 9 hours ago
```

## 原始预检 JSON

```json
{
  "artifact": {
    "manifest": {
      "created_at": "2026-08-11T13:45:23.382509+00:00",
      "milvus_build_id": "pds_2a8c0807733eb8022a623659",
      "milvus_collection": "cooking_knowledge_v2_pds_2a8c0807",
      "milvus_database": "default",
      "milvus_schema_hash": "bb34a179dcd8c4646cc0b2c416e1c6dfbbf8746f302f2161f896160987084e04",
      "pds_build_id": "pds_2a8c0807733eb8022a623659",
      "pds_manifest_sha256": "5644bef04a88bb8a3f99f526b394d88e0fdfc5d443d079e0b9a61dfd8cfbcec4",
      "rollback_collection": "cooking_knowledge_v2_pds_f01044e5",
      "rollback_database": "default",
      "rollback_pds_build": "pds_f01044e524ef43b413f76b02"
    },
    "milvus_row_count": 1333,
    "pds": {
      "anchor_count": 2634,
      "build_id": "pds_2a8c0807733eb8022a623659",
      "chunk_count": 1333,
      "parent_count": 341,
      "status": "ok"
    }
  },
  "bank_sha256": "e5edfbced75e84002bdd5b25054bf0906a022b4073e03ab31a4c85010f494f79",
  "failures": [],
  "health": {
    "service": "RAG System",
    "status": "healthy",
    "timestamp": "2026-08-11 16:07:30.066800"
  },
  "question_count": 300,
  "resolved_runtime_targets": 210,
  "status": "ready"
}
```

## 预检结论

**通过，已在任何 API 请求前关闭 gold_manifest.json。**

## old 变体启动

- 启动时间：`2026-08-12T00:14:53+08:00`。
- 环境：`EXAM_VARIANT=old`，`EXAM_NEW_PATH_TRAFFIC_PERCENT=0`，实体直达/QueryPlan/目标图/Milvus V2/PDS 均为 `false`，legacy fallback 为 `true`。
- 健康检查：`
{"service":"RAG System","status":"healthy","timestamp":"2026-08-11 16:14:53.946354"}
`。

## new 变体启动

- 环境：`EXAM_VARIANT=new`，新路径流量 `100`，实体直达/QueryPlan/目标图/Milvus V2/PDS 均为 `true`；PDS 为 `pds_2a8c0807733eb8022a623659`，collection 为 `cooking_knowledge_v2_pds_2a8c0807`，legacy fallback 为 `true`。
- 健康检查：`{"status":"healthy"}`。
