# 评测配置

此目录只保存可提交的配置。当前已冻结：

- `answer-quality-judge-prompt-v1.md`：实际发送给评分 LLM 的系统提示词和输入模板；
- `answer-quality-rubric-v1.json`：评分维度、权重、公式和问题标签；
- `answer-quality-output-schema-v1.json`：LLM 输出的 JSON Schema。

运行器必须读取这些文件，记录每个文件的 SHA-256，并把原样副本放入结果包 `04-回答效果评分/评分依据/`。修改任一文件都必须创建新版本文件名，不能覆盖 V1。

`OPENAI_API_KEY` 不得出现在这里。运行时模型地址和密钥从仓库根目录 `.env` 读取；结果只记录脱敏后的地址和模型名。
