# 阶段 0 独立审查记录

## 审查信息

- 审查身份：阶段 0 独立只读审查代理（`/root/phase0_independent_review`）
- 审查方式：未继承实现上下文；未修改工作区；未重跑可能产生文件的测试。
- 输入提交：`da67c64a373d59abbc53204b38d20723f19ddc98`
- 对比基线：`origin/main/a22897275c26f89398b766af754c44452f2b35f6`
- 审查时间：2026-08-08T04:59:50+08:00
- PR：未创建。本机 `gh` 缺少 GitHub 认证；候选地址为 `https://github.com/Trees-23/KDM-What-to-eat-today/pull/new/codex/retrieval-phase-0`。

## 结论

**有条件通过。** 提交符合阶段 0 的“诊断并如实 blocked”范围；阶段 0 DoD 本身仍未通过，严禁进入阶段 1。

审查发现 P0/P1：无。

## 审查发现与处置

| 级别 | 发现 | 处置 |
| --- | --- | --- |
| P2 | 基线记录了 A1 与 Compose 检查命令，但缺少 Neo4j/PyMilvus 缺失检查、Python/pytest 版本、锁文件发现与 SHA-256 的精确只读命令。 | 已在 `phase-0-2026-08-08.md` 补充对应命令、退出码和不记录敏感值的说明。 |
| P2 | 不存在阶段 0 独立审查记录。 | 本文件用于保存独立审查的身份、输入、结论、发现与时间。 |

## 核验要点

- `rag_modules/graph_rag_retrieval.py` 相对基线无差异；生产契约为 `extract_knowledge_subgraph(graph_query, query="")`，调用处传入原始 query。
- 测试替身已同步兼容签名，并断言获得 `川菜有什么特色`；未改变运行检索行为。
- 相对 `a228972`，运行时、Compose、数据、迁移、Milvus/Neo4j 文件均无改动；没有跨入阶段 1，也未触碰安全边界。
- 基线如实记录 A1 已通过，A2、B、C blocked；未将静态 CSV/导入脚本当成实例事实，且未暴露敏感连接信息。
- V2 的“C=Recipe 生产闭环”与实施方案 V1 的“C=稳定 ID/分类”差异已被披露；Recipe 生产器缺口保留为阶段 6 前提。

## 剩余风险

A2 的真实只读目标、B 的实际 `LOAD CSV` 可读性、C 的五类节点映射及蔬菜 predicate 均无实例证据，必须维持 `blocked`。补齐本记录后，仅继续安全只读监测，不创建阶段 1 代码。
