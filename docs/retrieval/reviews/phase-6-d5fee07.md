# 阶段 6 personal-local 总签收

- 审查身份：独立只读复核代理 `/root/phase6b_fixture_rereview`。
- 审查输入提交：`d5fee076b6ae08f2bbae235ee1d28abd7900587b`。
- 审查时间：`2026-08-10T19:30:08+08:00`。
- profile：`personal-local`。
- 结论：**通过，可签收阶段 6 personal-local DoD**。

## 验收结果

- 6A：对 `data/dishes` 的两次隔离构建均得到 `4368` 个节点、`5953` 条关系和 manifest SHA-256 `8046f881...`；`nodes.csv`、`relationships.csv`、manifest 逐字一致，严格 CSV 校验通过。
- 6B：old/new fixture 各 `50` 条，严格 provenance 门控均为 `valid=true`。old/new results SHA-256 分别为 `a3a257af...`、`d577cb1a...`；报告 SHA-256 分别为 `47e09e2e...`、`ef7e4b56...`。禁止断言、关系路径违规、严格营养误报与故障注入违规均为 `0`。
- 6C：默认新路径 feature flags 关闭，`RETRIEVAL_NEW_PATH_TRAFFIC_PERCENT=0`，旧路径兼容回退默认开启。请求仅可由显式 allowlist 或稳定 SHA-256 分桶比例进入新路径；本机没有启用 allowlist 或比例。
- rollout：按实施方案的相对阈值命令运行返回 `status=not_applicable`、`valid=true`、`recommended_action=offline_evaluation_only`。受保护 workflow 默认 profile 为 `protected`，不再使用 `continue-on-error` 隐藏采样或窗口失败。
- 旧路径：相对基线，`rag_modules/hybrid_retrieval.py`、`rag_modules/graph_rag_retrieval.py`、`rag_modules/milvus_index_construction.py` 没有差异。

## 验证证据

- 阶段 6 聚焦无服务套件：`55 passed`，覆盖 CSV 生产、fixture 评测、Neo4j 快照/导入守卫、rollout 监控、实体直达与回退。
- 全量无服务回归：`200 passed, 6 warnings`；6 条均为既有 `PytestCollectionWarning`。
- CLI：`neo4j_graph_import.py` 可由文档约定的直接脚本调用；CSV dry-run 与严格校验通过。
- 工作区与远端：审查结束时 `codex/retrieval-phase-0...origin/codex/retrieval-phase-0` 干净且同步。

## 边界与回退

本签收只覆盖个人本地 profile。未启动 Docker，未连接或写入 Neo4j/Milvus，未执行 `--apply`，未切换读流量。`protected` profile 仍须单独具备已授权指标源、staging 导入与恢复、7 天/100 请求 rollout-window、UI/API 场景验收和受保护环境审批。回退为保持 `RETRIEVAL_NEW_PATH_TRAFFIC_PERCENT=0` 或关闭新路径开关，并保留旧 Router、旧 collection 与 PDS build。
