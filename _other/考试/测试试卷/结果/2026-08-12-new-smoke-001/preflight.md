# New 路径十题定向测试预检

- 运行编号：`2026-08-12-new-smoke-001`
- 记录时间：`2026-08-12T13:04:12+08:00`
- 当前提交：`d782e82d67261bad6c44f7275d5be128903608c1`
- 当前分支：`test/new-path-smoke-paper`
- 题库 SHA-256：`a2f0f729e41aa861fe5ca0c42e34c687894444f5873ca6e2673491b6bf328f72`
- 预检退出码：`0`

## 启动前容器状态

```text
what-to-eat-backend|running|Up 17 minutes (healthy)
what-to-eat-frontend|exited|Exited (255) 22 hours ago
what-to-eat-milvus-etcd|running|Up 30 minutes (healthy)
what-to-eat-milvus-minio|running|Up 30 minutes (healthy)
what-to-eat-milvus-standalone|running|Up 30 minutes (healthy)
what-to-eat-neo4j|running|Up 30 minutes (healthy)
what-to-eat-neo4j-init|exited|Exited (0) 17 minutes ago
what-to-eat-nginx|exited|Exited (255) 22 hours ago
```

## 启动前 GET /health 响应

```json
{"service":"RAG System","status":"healthy","timestamp":"2026-08-12 05:03:59.478276"}
```

## 工作区状态

```text
(clean)
```

## `开考预检.py --probe-new-path` 原始 JSON

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
    "timestamp": "2026-08-12 05:04:00.186075"
  },
  "question_count": 300,
  "resolved_runtime_targets": 210,
  "status": "ready"
}
```

- 预检解析状态：`ready`

## 受控启动后服务状态

```text
what-to-eat-backend|running|Up About a minute (healthy)
what-to-eat-frontend|exited|Exited (255) 22 hours ago
what-to-eat-milvus-etcd|running|Up 32 minutes (healthy)
what-to-eat-milvus-minio|running|Up 32 minutes (healthy)
what-to-eat-milvus-standalone|running|Up 32 minutes (healthy)
what-to-eat-neo4j|running|Up 32 minutes (healthy)
what-to-eat-neo4j-init|exited|Exited (0) About a minute ago
what-to-eat-nginx|exited|Exited (255) 22 hours ago
```

```json
{"service":"RAG System","status":"healthy","timestamp":"2026-08-12 05:05:58.179201"}
```
