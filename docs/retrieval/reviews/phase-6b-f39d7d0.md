# 阶段 6b 独立只读审查记录

- 审查身份：`phase6b_signoff_review`（独立只读审查代理）
- 输入提交：`f39d7d0`（含前置 6b 提交 `3a4ca2e`、`781edcf`、`65f060a`）
- 审查时间：2026-08-10（UTC+8）
- 工作区权限：只读；未修改实现工作区

## 审查范围

- `eval/retrieval_refactor_cases.yaml`：10 个必测场景、每场景 5 条固定释义、故障注入期望和允许 parent/关系路径。
- `eval/retrieval_release_thresholds.yaml`：证据、关系、忠实率、链接、禁止断言、营养声明、old/new Recall@5、MRR@5 和 P95 门槛。
- `scripts/run_retrieval_eval.py` 与 `test/test_retrieval_refactor_eval.py`：结果 schema、故障降级、关系路径、严格营养来源、baseline 来源和 CLI 退出码。

## 验证证据

- `python -m pytest -q test/test_retrieval_refactor_eval.py`：7 passed。
- `python -m pytest -q`：189 passed，6 条既有 pytest 收集警告。
- `python -m py_compile scripts/run_retrieval_eval.py`：通过。
- `git show --check f39d7d0`：通过。

## 结论

前置审查发现的故障注入绕过、伪造证据链接、畸形断言、额外关系路径和未治理营养来源已由 `f39d7d0` 前的修复提交覆盖并有回归测试。后续复核又发现 baseline 必须从同一份 old 结果重算、未知 `strict_*` 断言和非有限延迟需要进一步收紧；本记录因此标记为“待修复重审”，不能作为最终阶段签收。

## 外部边界

本签收只覆盖离线评测契约与门控，不代表 Neo4j/Milvus staging 导入、7 天 rollout 或用户场景 API 签收已完成。
