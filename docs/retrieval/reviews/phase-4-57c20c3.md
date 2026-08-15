# 阶段 4 独立复审与运行证据

- 审查身份：Codex 独立只读审查代理（`/root/phase0_independent_review`）。
- 审查输入提交：`57c20c3962a40b1ba96f48d63e50a505fd829855`。
- 审查时间：2026-08-09T15:30:19+08:00。
- 代码审查结论：**通过**，未发现 P0/P1；此前的初始化 `ArtifactMismatchError` 审计和 V2 专用 QueryPlan 越界问题均已修复。
- 后续状态：项目所有者已确认仅作个人本机开发，并通过 `phase-4-personal-local-gate.md` 建立受限本机例外。个人本机切换演练的后续证据见 `phase-4-6f47b44.md`；受保护/共享/生产环境仍适用原双人审批门槛。

## 本轮修复签收

- 初始化期间的 `ArtifactMismatchError` 被单独分类为 `artifact-mismatch`。后续偏好请求记录 `restricted_vector/artifact-mismatch` 和 `vector_scope=rejected`，随后回退旧 Router；正文 hydration 不会执行。
- `PREFERENCE_RECOMMEND` 是 V2 专用 QueryPlan。目标化图检索器会在打开 Neo4j session 前以 `QueryPlanValidationError` 显式拒绝它，不再出现 `KeyError`。
- 本轮 diff 仅涉及入口降级、目标图模板边界与对应测试；未修改旧 Hybrid/Graph RAG、旧 Milvus 构建、V2 构建、快照或切换脚本。

## 自动化验证

- 阶段 4 契约与受影响回归：`70 passed`。
- 全量：`145 passed, 6 warnings`。6 条为既有 pytest 测试替身收集警告。
- `git diff --check a4b3c33..57c20c3`：通过。

## 实例与恢复证据

2026-08-09T15:19:55+08:00 至 15:22:22+08:00，在既有本地 Milvus 实例 `what-to-eat-milvus-standalone` 的 `default` database 执行了阶段 4 允许的验证和恢复演练。

- V2 collection `cooking_knowledge_v2_pds_f01044e5`：schema hash 为 `bb34a179dcd8c4646cc0b2c416e1c6dfbbf8746f302f2161f896160987084e04`，行数为 `1333`，样本向量检索为 `verified`。
- PDS build `pds_f01044e524ef43b413f76b02` 的 preinsert 和 postinsert linkage 均为 `1333/1333`，无缺失、重复、失配或意外行。
- 从 active PDS metadata 得到 `32` 个川菜 parent ID；受限检索返回的 5 个 parent 均在该范围内，且所有正文证据均由 PDS hydration 提供。无候选范围的 child-chunk 检索同样完成 parent 聚合和 PDS hydration。
- 新建不可变旧集合快照的 payload SHA-256 为 `dd1f98a895f714ab6b323acb7a841e7dacdaad4c2f374c29acb85ad5445c9105`。源 `cooking_knowledge` 的 schema、1333 行和检索验证通过。
- 快照仅恢复至此前不存在的 `cooking_knowledge_restore_verify_20260809_r2`；该集合的 schema、1333 行、抽样 hash 和检索验证通过。旧集合与 V2 集合均仍存在，未执行 drop、重建或 cutover。

## 开关、回退与阻塞

- `RETRIEVAL_MILVUS_V2_ENABLED` 默认保持 `false`，未变更运行时流量或联合 artifact 指针。
- 回退步骤：保持或设置 `RETRIEVAL_MILVUS_V2_ENABLED=false`，并使用旧 `cooking_knowledge`；必要时只读切向已验证 restore collection。不得删除 V2 或旧集合。
- 2026-08-09 的只读检查未发现受保护发布环境、`RETRIEVAL_RELEASE_ENVIRONMENT`、双人审批、变更单、未过期 approval record 或人工 `--confirm-cutover` 确认。因此不运行 `retrieval_cutover.py`，也不把代码审查通过表述为阶段 4 完成。
- GitHub 仓库只读复查显示 Environment 数量为 `0`，Actions variable 数量为 `0`，唯一 workflow 为 Dependency Graph；仓库中也没有发布或切换 workflow。未枚举或猜测 secret，且上述配置缺失不能替代受保护审批记录。
