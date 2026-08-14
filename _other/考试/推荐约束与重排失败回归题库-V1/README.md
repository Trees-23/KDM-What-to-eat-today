# 推荐约束与重排失败回归题库 V1

本题库冻结自 `2026-08-14-intent-planner-300-manual-003` 的 78 道未通过题，用于验证该轮修复，不替代最终 300 题全量验收。

运行器会校验每道题与当前官方 300 题库逐字一致，并核对官方题库 SHA-256；题库被改写或官方题库变更时会拒绝执行。

在仓库根目录执行：

```bash
python scripts/run_intent_planner_acceptance.py \
  --question-bank _other/考试/推荐约束与重排失败回归题库-V1/试卷题库.json \
  --output _other/考试/检索重构真实场景考试包/结果/2026-08-15-intent-planner-failure-regression-006
```

输出目录必须不存在。运行过程中终端会实时显示题号、用户输入、回答、耗时和失败原因；单题失败会继续执行其余题目。完整结果、失败汇总和审计证据会写入指定输出目录。
