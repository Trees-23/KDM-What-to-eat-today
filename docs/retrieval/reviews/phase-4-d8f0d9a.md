# 阶段 4 独立审查与修复复验记录

- 审查身份：Codex 独立只读审查代理（`/root/phase0_independent_review`）。
- 首轮输入提交：`834666952b1486319b180eebc897c0c212979110`。
- 首轮审查时间：2026-08-09T01:14:38+08:00。
- 首轮结论：**不通过**，发现 3 项 P1 与 1 项 P2。
- 修复输入提交：`d8f0d9a`。
- 当前状态：修复与自动化、真实 Milvus 复验已完成；等待该独立审查身份对修复提交进行二次签收。阶段 4 在签收前保持未完成，不进入阶段 5。

## 首轮发现与修复

| 级别 | 首轮发现 | 修复与覆盖 |
| --- | --- | --- |
| P1 | 主入口没有把 embedding 模型注入 V2 retriever，偏好查询会降为 `VECTOR_UNAVAILABLE`。 | `main.py` 显式注入 `index_module.embeddings`；`test_parent_aggregation.py` 覆盖 `embed_query()` 生成查询向量。 |
| P1 | `ArtifactMismatchError` 只返回空 bundle，没有回退既有 Router。 | 主入口记录 `restricted_vector/artifact-mismatch` 审计事件后返回 `None`；`test_entity_direct_retrieval.py` 验证旧 Router 被调用且没有 V2 正文 hydration。 |
| P1 | cutover 只校验备份文件 SHA，未校验其数据库、源集合和 artifact rollback 绑定。 | `retrieval_cutover.py` 使用 `load_manifest()` 校验完整可恢复快照、`database/from collection`、非空 payload，以及 `rollback_database`、`rollback_collection`、`rollback_pds_build` 与审批记录。测试拒绝缺少 rollback 审批字段和错误源集合快照。 |
| P2 | `verify-existing` 未验证向量可检索性。 | `MilvusV2IndexBuilder.verify_existing()` 支持样本向量检索；CLI 可使用 `--vectors-json` 输出 `sample_search=verified`。 |

## 自动化复验

- `python -m pytest -q`：`134 passed, 6 warnings`。6 条均为现有 pytest 测试替身的收集警告。
- `python -m py_compile main.py rag_modules/milvus_v2_index.py scripts/build_milvus_v2.py scripts/retrieval_cutover.py`：通过。
- `git diff --check`：通过。

## 真实 Milvus 与 PDS 复验

目标为既有本地实例 `what-to-eat-milvus-standalone`，database=`default`；所有操作只读验证，未执行 drop、重建、切换或修改旧集合。

- `cooking_knowledge_v2_pds_f01044e5`：V2 schema hash=`bb34a179dcd8c4646cc0b2c416e1c6dfbbf8746f302f2161f896160987084e04`，行数=`1333`，`sample_search=verified`。
- PDS build=`pds_f01044e524ef43b413f76b02` 的 preinsert/postinsert linkage：`1333/1333`，无缺失、重复、失配或意外行。
- 候选联合 manifest 已生成在受忽略的运行时路径 `run/retrieval/retrieval_artifact_manifest.json`，其 PDS manifest hash=`b5402762cfd0b0ba695c420c2fe3fa1c100f1e1314bd70a204e4bfb22daa59ca`；当前 feature flag 仍为默认 `false`。
- 旧 `cooking_knowledge` 和恢复验证集合 `cooking_knowledge_restore_verify_20260809_v2` 均通过 snapshot schema、1333 行、抽样 hash 与向量检索 verify；旧集合仍存在。

## 切换状态与回退

- 未发现受保护环境、双人审批、变更单和未过期审批记录，故未执行 `retrieval_cutover.py` 的真实 cutover。
- 2026-08-09T13:49:44+08:00 的只读复查：`run/` 与 `docs/` 下没有 approval/change/cutover/release 记录，`RETRIEVAL_RELEASE_ENVIRONMENT`、`RETRIEVAL_MILVUS_V2_ENABLED`、`RETRIEVAL_MILVUS_COLLECTION` 均未设置。
- 保持 `RETRIEVAL_MILVUS_V2_ENABLED=false`。回退动作是保持/设置该值为 `false` 并使用旧 `cooking_knowledge`；不删除 V2 或旧集合。
- 未修改 `rag_modules/hybrid_retrieval.py`、`rag_modules/graph_rag_retrieval.py` 或 `rag_modules/milvus_index_construction.py`。
