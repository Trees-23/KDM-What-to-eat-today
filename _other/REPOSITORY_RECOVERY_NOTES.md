# 仓库恢复说明

## 当前基线

`codex/recovery-clean-baseline` 从本地快照重新建立根提交，不继承原先无法推送的 Git LFS 历史。原快照仍由 `backup/pre-recovery-clean-20260808` 和既有分支保留，不应删除。

## 未纳入新基线的本地制品

- `bge-reranker-v2-m3/model.safetensors`：约 2.3 GB，超过 GitHub LFS 单对象 2 GB 上限。
- `bge-reranker-v2-m3/tokenizer.json`、`bge-small-zh-v1.5/model.safetensors`、`bge-small-zh-v1.5/pytorch_model.bin`：本地模型缓存，不属于源代码。
- `data/dishes/**` 下的 326 个图片对象：上游 Git LFS 返回 404，只有指针、没有可下载实体，不能把失效指针推入新的主线。
- `run/`：运行生成物，不属于源代码。

默认配置使用 Hugging Face 模型标识，不要求这些本地权重被 Git 管理。需要离线模型时，应从受控模型制品仓库下载到本地缓存目录。

## 后续媒体恢复规则

只有取得可校验的图片备份后，才可重新导入媒体。导入前需要先确认来源、许可证、总容量和 GitHub LFS 配额；然后为明确的媒体路径启用 LFS、完整上传对象并在新克隆中验证下载。不得重新提交只有 LFS 指针而没有实体的文件。
