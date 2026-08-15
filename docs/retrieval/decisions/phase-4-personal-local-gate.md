# 阶段 4 个人本机切换门控调整

## 决策

2026-08-09，项目所有者确认当前仓库仅用于个人本机开发，不属于生产、共享 staging 或受保护发布环境。阶段 4 允许使用 `personal-local` 切换档位完成本机演练，不要求双人审批或变更单。

本决策是对实施方案受保护切换条款的本机例外，仅适用于当前个人项目。它不削弱默认 `protected` 档位，也不授权生产、共享环境或未来公开部署跳过双人审批。

## personal-local 门槛

- 必须显式传入 `--release-profile personal-local`、`--environment personal-local` 和 `--confirm-cutover`。
- 进程环境必须设置 `RETRIEVAL_RELEASE_ENVIRONMENT=personal-local`；任何其他值都会被拒绝。
- 仍校验 database、from/to collection、V2 collection 名、PDS build、联合 artifact manifest、回退绑定、旧集合快照 SHA、快照内容和所有路径白名单。
- 仍禁止覆盖或删除 `cooking_knowledge`、V2 collection 和 restore collection。
- feature flag 默认值保持 `RETRIEVAL_MILVUS_V2_ENABLED=false`；本机启用和回退必须在验收记录中明确留档。

## 受保护档位

默认 `protected` 档位保持原规则：受保护环境绑定、双人审批、变更单、过期时间和审批记录必须全部存在。`personal-local` 不可用于替代共享或生产发布审批。
