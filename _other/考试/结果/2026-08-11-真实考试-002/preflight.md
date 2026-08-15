# 真实服务考试预检

- 运行编号：`2026-08-11-真实考试-002`
- 预检关闭时间：`2026-08-11T15:54:47+08:00`
- 实现提交：`6b13a41f7dab1b99e1e737d29ba50873e60416f0`
- 当前分支：`codex/independent-exam-002`
- 目标基线：`origin/main` 的 `a22897275c26f89398b766af754c44452f2b35f6`
- 题库 SHA-256：`688edfea11db27a5cf5796ffa886e785f73c1f2ceb6a714f879830b3d06df88d`
- `题库校验报告.md` 声明的 SHA-256：`688edfea11db27a5cf5796ffa886e785f73c1f2ceb6a714f879830b3d06df88d`
- 静态题库重生成校验：`python _other/考试/工具/生成试卷.py` 成功生成 300 题，输出 SHA-256 与预检一致；检查后工作区无题库、目录或校验报告差异。

## 只读服务状态

- `neo4j` 为 healthy；只读 Cypher 计数为节点 `5946`、关系 `20644`、`REQUIRES` 关系 `2905`。
- `milvus-standalone` 已退出（exit `255`，完成时间 `2026-08-11T07:16:39Z`）；`milvus-etcd` 与 `milvus-minio` 同样已退出（exit `255`）。
- `backend` 仍在运行但 health 为 `starting`，观察到重启次数 `192`；`GET http://localhost:8000/health` 连接被重置，状态为 `000`。
- 后端日志显示初始化时无法连接 `milvus-standalone:19530`。未改动 `.env`、应用代码、Compose 主配置、数据或服务状态；未执行 `docker compose down`、停止服务、迁移或写 Cypher。
- V2 artifact `run/retrieval/active/retrieval_artifact_manifest.json` 可读取，声明 collection `cooking_knowledge_v2_pds_f01044e5` 与 PDS build `pds_f01044e524ef43b413f76b02`；相应 SQLite PDS 可读，包含 `341` 个 parents、`1333` 个 chunks。但因实际 Milvus 服务已退出，artifact 不可作为新路径可用证据。

## 实体与图路径复核

- 对题库引用的 S01-S05、S09、S10 稳定 `nodeId` 进行只读聚合查询：静态来源共 `253` 个唯一 ID，Neo4j 中解析 `253` 个，缺失 `0`、重复 `0`。中文名称或类别不作为 Neo4j 输出 gold，gold 使用 CSV 和源 Markdown 的稳定 ID、名称、`sourcePath`。
- 静态 `nodes.csv`、`relationships.csv` 与题库生成器一致：S04 直接路径、S05 A/B 多跳路径和 S05 C 零路径契约均可按源数据冻结。
- S05 C 的运行时只读多跳查询涵盖 `11` 个稳定食材节点，最小/最大路径数均为 `0`，与其零路径反例契约一致。
- S05 A/B 的运行时只读查询在稳定实体均已解析的前提下，以 `Ingredient <- REQUIRES - Recipe - REQUIRES -> Ingredient(category="蔬菜")` 计数为 `0`；这与静态 CSV 的正向路径契约不一致。单个已解析食材可查到 `REQUIRES` 关系和带 `category` 属性的邻接食材，但没有可由该运行时条件验证的正向蔬菜路径。因此不能将静态路径冻结表述为当前真实服务图路径通过。
- S08 的 30 个虚构菜名、S09 的 30 个虚构食材在 `nodes.csv` 与 `tips_nodes.csv` 中均为 `0` 命中；S09/S10 的已知食材稳定节点均可解析。

## Gold 冻结

`gold_manifest.json` 已在任何 API 请求之前一次性写入并关闭：覆盖 300 题，含题库 SHA、冻结时间、实现提交、S01-S03 稳定节点/来源、S04/S05 静态图节点与边、S05 C 零路径证据、S06/S07 三档相关性及来源、以及 S08-S10 的存在性前置条件。S06/S07 使用当前源节点和源 Markdown 冻结；未以 PDS 缺少的历史模糊标题补造候选。

## 预检结论

**失败，停止考试。** Milvus 依赖不可用导致 `/health` 失败；此外 S05 A/B 的实际 Neo4j 多跳类别条件与静态题库契约不一致。未执行 old/new Compose 覆盖启动，未发送 `/api/chat/stream` 请求，未产生 HTTP/SSE 响应或运行时审计，未运行 S09/S10 隔离组件。为满足逐题可复核性，old/new 各写 300 条 `blocked` 结果并保留阻断原因；这些行不构成服务考试通过或安全通过。
