# 阶段 4 个人本机切换验收

- 门控实现提交：`6f47b44f51694f2df7989f9bfd7c2cef2bac793d`。
- 门控决策：[phase-4-personal-local-gate.md](../decisions/phase-4-personal-local-gate.md)。
- 代码独立审查：通过，无 P0/P1/P2；审查代理为 Codex 独立只读审查代理（`/root/phase0_independent_review`）。
- 当前状态：**待本机运行证据独立复核**。本记录不将实施者执行的验证替代独立服务验收。

## 门控范围

- `personal-local` 仅接受 `--release-profile personal-local`、`--environment personal-local`、`RETRIEVAL_RELEASE_ENVIRONMENT=personal-local` 与 `--confirm-cutover` 的组合。
- database/collection 白名单、V2 命名、PDS build、artifact/schema/rollback 绑定、旧集合快照 SHA、可恢复 payload 和路径白名单均保持强制校验。
- 默认 `protected` 档位仍要求受保护环境、双人审批、变更单和未过期审批记录；本机例外不可用于共享或生产环境。

## 实施者本机演练

2026-08-09 在既有本机 `what-to-eat-milvus-standalone`（database=`default`）执行，未删除、重建或覆盖任何 collection。

- 从旧 `cooking_knowledge` 的不可变快照读取 manifest SHA-256 `8a389577ca0ec001ccb81e15d54dade8cc2853982ea29f666a20b08a98a27195`，并经 `personal-local` 守卫将 V2 artifact 原子写入独立 active 指针。
- 临时设置 `RETRIEVAL_MILVUS_V2_ENABLED=true`、V2 collection 和 active artifact 路径后，真实入口的 `_initialize_restricted_vector_retriever()` 成功初始化，artifact 状态为空。
- “推荐川菜清淡的菜”：从 PDS 得到 32 个川菜 parent ID；5 个结果全部在候选范围内，正文均来自 PDS hydration。
- “夏天吃什么清淡的？”：使用 `all_child_chunks` child-chunk 检索得到 5 个聚合 parent，正文均来自 PDS hydration。
- 在独立进程中临时设置 `RETRIEVAL_MILVUS_V2_ENABLED=false` 与 `RETRIEVAL_MILVUS_COLLECTION=cooking_knowledge`，确认旧 collection 存在且行数为 1333，状态为 `legacy-fallback-verified`。未改写 `.env`、默认配置或服务进程环境。
- 旧 `cooking_knowledge`、V2 `cooking_knowledge_v2_pds_f01044e5` 和 restore verify collection `cooking_knowledge_restore_verify_20260809_r2` 均存在，行数均为 1333。

## 验证与环境说明

- 门控及阶段 4 契约套件：`72 passed`。
- 全量：`147 passed, 6 warnings`；6 条为既有 pytest 测试替身收集警告。
- 为执行真实入口初始化，在本机 Python 环境安装了 `requirements.txt` 已声明但缺失的 `neo4j`、`langchain-core`、`langchain-community` 和 `langchain-huggingface`。未更改依赖声明或项目源码。
- `pip check` 仍报告工作站中无关的 `nanobot-ai` 与 `websockets` 版本冲突；本项目测试和本机检索验收未受影响。
