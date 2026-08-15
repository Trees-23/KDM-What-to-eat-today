# 阶段 2 独立审查记录

- 审查身份：Codex 独立只读审查代理（`/root/phase0_independent_review`），未修改工作区。
- 输入基线：`135100d40241bc00e3e74dc625fe11409ec137e3`。
- 签收提交：`ec9d0de731b174adae3add8a8fa9f5cc0427765b`，包含后续修复 `5b75417`、`74f0e58` 与 `ec9d0de`。
- 审查时间：2026-08-08T23:05:25+08:00。
- 结论：**通过**；P0/P1/P2 均为无。

## 核验结果

- 证据契约包含 `EntityCandidate`、`GraphFact`、`TextEvidence`、`EvidenceBundle`；生成输入物理分为“已验证图事实 / 正文证据 / 限制与不可证明项”。
- 实体解析按精确名称、受治理别名、已验证全文候选的固定顺序执行；同分候选标记为歧义，未静默选择。
- `recipe_step_anchor_v1` 为固定参数化定位器，拒绝 Cypher、label、关系等非授权参数；实体直达路径不持有 Milvus 客户端。
- 未定位实体默认返回并审计 `ENTITY_NOT_FOUND`，且向量调用数为 `0`；只有调用方显式设置 `allow_generalized_advice=True` 才可回退旧 Router。Web 非流式/流式入口均只接受 JSON 布尔 `true`。
- CLI 在未传入审计 run 时创建审计 run；`NullAuditRun` 与真实审计对象的开始时间接口兼容，关闭审计的 CLI、Web 非流式及 Web 流式路径均可运行。
- PDS 或图读取不可用时保留显式限制/审计；实体直达开关和 PDS 开关默认关闭。关闭实体直达开关可回退既有 Router/Hybrid，PDS build 保留用于诊断。
- 实际只读 PDS 核验：`201002454`（宫保鸡丁）全文与第一步从 `pds_f01044e524ef43b413f76b02` 回补；`tipdoc_e5959b9d0464`（腌（肉））技巧全文可回补；不存在实体候选数为 `0`；实体直达路径全库向量调用为 `0`。
- 相对输入基线未修改 `rag_modules/hybrid_retrieval.py`、`rag_modules/graph_rag_retrieval.py`、`rag_modules/milvus_index_construction.py`。
- `git diff --check` 通过，审查时工作区干净。

## 自动化验证

- `python -m pytest -q test/test_entity_resolver.py test/test_entity_direct_retrieval.py test/test_evidence_bundle.py test/test_generation_evidence_context.py test/test_web_audit_a3.py test/test_router_audit_a4.py test/test_graph_audit_a6.py test/test_hybrid_retrieval_fusion.py`：`46 passed`，1 条既有 pytest 收集警告。
- `python -m pytest -q`：`86 passed, 6 warnings`；警告均为现有测试替身定义构造函数导致的 pytest 收集警告。

## 阶段判定

阶段 2 DoD 已通过。阶段 3 可以开始；仍须以阶段 0 已记录的运行实例 schema、关系方向与分类 predicate 为唯一依据，且不得修改旧 Hybrid/Graph RAG/Milvus 入口。
