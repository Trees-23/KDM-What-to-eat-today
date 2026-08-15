# 真实服务考试预检

- 运行编号：`2026-08-11-真实考试-001`
- 预检时间：`2026-08-11T02:11:21+08:00`
- 实现提交：`68bf4c3ea5f73352ee1900978d7f20dfab4f074e`
- 当前分支：`codex/retrieval-exams`
- 题库 SHA-256：`d4bb3d8495e41b4daeed280e673cb884c59cb917b470f147bfa9a2ca8423208b`
- 题库校验报告声明的 SHA-256：`d4bb3d8495e41b4daeed280e673cb884c59cb917b470f147bfa9a2ca8423208b`
- 静态题库重生成校验：`python _other/考试/工具/生成试卷.py` 输出 300 题且 SHA 一致；未发现题库差异。

## 服务状态

- Compose 服务 `backend`、`frontend`、`milvus-etcd`、`milvus-minio`、`milvus-standalone`、`neo4j`、`nginx` 均为 running/healthy。
- `GET http://localhost:8000/health` 返回 HTTP 200，响应为 `{"service":"RAG System","status":"healthy",...}`。
- Neo4j 只读计数：节点 `5946`，关系 `20644`，`REQUIRES` 关系 `2905`。
- Milvus V2 artifact：`run/retrieval/active/retrieval_artifact_manifest.json` 指向 `cooking_knowledge_v2_pds_f01044e5`；PDS 指针指向 `pds_f01044e524ef43b413f76b02`，SQLite 文件存在且可读（`parents=341`、`chunks=1333`）。Milvus collection 列表包含该 collection。

## 实体与图路径复核

中文经 `cypher-shell` 显示为乱码，故名称/来源以 `data/cypher/nodes.csv`、`data/cypher/tips_nodes.csv`、源 Markdown 和稳定 `nodeId` 为准；Neo4j 只用 ASCII `nodeId` 参数执行只读路径计数。

- S01-S03 的静态 `sourcePath` 可由上述节点表与源 Markdown 唯一交叉解析。
- S08 的 30 个 `云岚NN号幻味砂锅` 和 S09 的 30 个 `星雾紫萝NN` 在节点表中均为 0 命中。
- S10 所需已知食材均在节点表中存在。
- S04 的 30 个食材均至少有一条 `Recipe-[:REQUIRES]->Ingredient` 路径。
- S05 无法满足“每题至少一条 Ingredient<-REQUIRES-Recipe-REQUIRES->蔬菜”的冻结条件：`S05-A-03`（鸡肉）为 0 条；同样为 0 条的还有 `S05-B-09`（玉米）、`S05-C-02`（西兰花）、`S05-C-08`（南瓜）、`S05-C-09`（菠菜）。
- 对 `S05-A-03`，稳定 ID `201004679` 在 Neo4j 中有 1 条菜谱关系，但同一菜谱的蔬菜配对查询结果为 0；这与节点/关系 CSV 的只读复核一致。

## 预检结论

**失败，停止考试。** `gold_manifest.json` 未关闭，未发送任何 `/api/chat/stream` 请求，未重启 backend，未运行 S09/S10 隔离组件。按照监考规则，已为 old/new 各写 300 条 `blocked` 结果并保留原因；没有编造 gold、审计、HTTP/SSE 响应或组件断言。
