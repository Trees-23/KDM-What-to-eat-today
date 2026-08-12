# New 路径第二套十题定向测试预检

- 运行编号：`2026-08-12-new-smoke-004`
- 实现提交：`51aba47ac4fa66d32e80321e03b11723d9e287eb`
- 当前分支：`codex/new-path-smoke-003`
- 预检时间：`2026-08-12T14:07:35+08:00`
- 题库 SHA-256：`27e6ded289325613bfeae2b4afe5c20f41c1a011d8686cea3397b125a4e2ad4f`

## 容器状态

```text
what-to-eat-backend|running|Up About a minute (healthy)
what-to-eat-milvus-etcd|running|Up 2 hours (healthy)
what-to-eat-milvus-minio|running|Up 2 hours (healthy)
what-to-eat-milvus-standalone|running|Up 2 hours (healthy)
what-to-eat-neo4j|running|Up 2 hours (healthy)
```

## /health 响应

```json
{"service":"RAG System","status":"healthy","timestamp":"2026-08-12 06:07:36.813193"}
```

## 正式开考预检原始 JSON

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
    "timestamp": "2026-08-12 06:07:29.217793"
  },
  "question_count": 300,
  "resolved_runtime_targets": 210,
  "status": "ready"
}
```

预检退出码为 `0`，`status` 为 `ready`。在首次 API 请求前已关闭 `gold_manifest.json`。

