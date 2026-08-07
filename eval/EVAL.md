# RAGAS 测评说明

本文档说明本项目的 RAGAS 测评目录、数据格式、常见指标含义，以及本地 embedding 模型的选择。

## 测评流程

本项目的测评分为两个阶段：

1. 测评前置输入：`eval/user_input/*.jsonl`
   - 存放待提问的问题和可选标准答案。
   - 用于调用本项目的 RAG 问答接口。

2. RAGAS 数据与结果：
   - `eval/ragas_data_output/*.jsonl`：模型回答、检索上下文和元数据。
   - `eval/result/*.jsonl`：RAGAS 最终打分结果。

## 数据格式

### 测评前置输入格式

`eval/user_input/*.jsonl` 中的每一行是一条待测问题：

```json
{"id":"q001","user_input":"蚝油生菜怎么做？","category":"recipe_steps","expected_strategy_hint":"hybrid_traditional","reference":"标准答案..."}
```

字段说明：

| 字段 | 含义 |
|---|---|
| `id` | 测评样本编号 |
| `user_input` | 用户问题 |
| `category` | 问题类别，便于后续分组分析 |
| `expected_strategy_hint` | 预期检索策略，仅用于分析，不直接参与 RAGAS 打分 |
| `reference` | 标准答案，部分指标会用到 |

### RAGAS 可评估数据格式

调用 RAG 系统后，脚本会生成接近 RAGAS 标准格式的数据：

```json
{
  "user_input": "蚝油生菜怎么做？",
  "response": "模型回答...",
  "retrieved_contexts": ["检索上下文1", "检索上下文2"],
  "reference": "标准答案..."
}
```

字段说明：

| 字段 | 含义 |
|---|---|
| `user_input` | 原始问题 |
| `response` | RAG 系统生成的回答 |
| `retrieved_contexts` | RAG 检索到并提供给模型的上下文 |
| `reference` | 人工标准答案 |

## 常见 RAGAS 指标

| 指标 | 中文名 | 评估内容 | 需要的数据 | 额外模型依赖 |
|---|---|---|---|---|
| `faithfulness` | 忠实度 | 回答是否被检索上下文支持，有没有编造 | `response`, `retrieved_contexts` | LLM 评审模型 |
| `answer_relevancy` / `response_relevancy` | 答案相关性 | 回答是否切题，是否围绕用户问题 | `user_input`, `response` | LLM 评审模型 + embedding 模型 |
| `context_precision` | 上下文精确率 | 检索结果是否相关、排序是否靠前 | `user_input`, `retrieved_contexts`，通常还需要 `reference` 或 `response` | 视 RAGAS 版本而定，可能需要 LLM 或 embedding |
| `context_recall` | 上下文召回率 | 检索上下文是否覆盖标准答案所需信息 | `user_input`, `retrieved_contexts`, `reference` | LLM 评审模型 |
| `answer_correctness` | 答案正确性 | 回答事实是否接近标准答案 | `user_input`, `response`, `reference` | LLM 评审模型，部分版本也会用 embedding |
| `answer_similarity` | 答案语义相似度 | 模型回答和标准答案的语义相似程度 | `response`, `reference` | embedding 模型 |

## 指标示例

### `faithfulness`（忠实度）

示例数据：

```json
{
  "user_input": "蚝油生菜怎么做？",
  "response": "生菜焯水10秒，调蚝油汁后浇在生菜上。",
  "retrieved_contexts": ["生菜洗净，沸水中加盐和油，焯水10秒。调汁：生抽、蚝油、盐、白糖、清水。"]
}
```

判断逻辑：

- 如果 `response` 里的做法都能从 `retrieved_contexts` 中找到依据，`faithfulness` 会较高。
- 如果回答编造了上下文中没有的食材、步骤或功效，`faithfulness` 会降低。

### `answer_relevancy`（答案相关性）

示例数据：

```json
{
  "user_input": "酸辣土豆丝怎么炒才能口感脆一点？",
  "response": "先洗掉土豆丝淀粉，短时间焯水，大火快炒，最后放醋和盐。"
}
```

判断逻辑：

- 该指标评估回答是否真正回应了问题。
- RAGAS 通常会用 LLM 从回答中反推问题，再用 embedding 计算反推问题与原问题的语义相似度。
- 如果没有 embedding 模型，这个指标很容易变成 `NaN`。

### `context_recall`（上下文召回率）

示例数据：

```json
{
  "user_input": "糖醋汁怎么调？",
  "retrieved_contexts": ["糖醋汁可用料酒、清水、生抽、白糖、白醋调配。"],
  "reference": "糖醋汁常见比例可按料酒、清水、生抽、白糖、白醋等调配，核心是酸甜咸平衡。"
}
```

判断逻辑：

- 如果 `retrieved_contexts` 覆盖了 `reference` 所需的关键信息，`context_recall` 会较高。
- 如果标准答案里的关键知识没有被检索出来，召回率会降低。

### `context_precision`（上下文精确率）

示例数据：

```json
{
  "user_input": "微波炉做鸡蛋羹有哪些注意事项？",
  "retrieved_contexts": [
    "微波鸡蛋羹需要可微波容器，覆盖保鲜膜但不要密封。",
    "可乐鸡翅用可乐和生抽焖煮收汁。"
  ],
  "reference": "微波炉做鸡蛋羹应使用可微波容器，覆盖时留孔，分段加热，注意防烫。"
}
```

判断逻辑：

- 第一条上下文和问题相关。
- 第二条上下文是噪声。
- 好的检索系统应该把相关上下文排在前面，并减少无关上下文。

### `answer_correctness`（答案正确性）

示例数据：

```json
{
  "user_input": "清蒸生蚝怎么做才比较安全？",
  "response": "生蚝需要刷洗干净并充分蒸熟，开壳和掀锅盖时注意防烫。",
  "reference": "清蒸生蚝要彻底清洗外壳，保证充分加热熟透，异常气味或变质生蚝不要食用。"
}
```

判断逻辑：

- 该指标比较 `response` 和 `reference` 的事实是否一致。
- 它比 `faithfulness` 更依赖标准答案。

### `answer_similarity`（答案语义相似度）

示例数据：

```json
{
  "response": "生菜快速焯水后浇蚝油汁。",
  "reference": "蚝油生菜的关键是短时间焯水，再淋上蚝油调味汁。"
}
```

判断逻辑：

- 该指标不一定判断事实细节是否完全正确，而是看回答和标准答案语义是否接近。
- 它依赖 embedding 模型。

## 本项目当前推荐指标

当前建议先使用 4 个指标：

```env
RAGAS_METRICS=faithfulness,answer_relevancy,context_recall,context_precision
```

原因：

- `faithfulness` 可以检查回答是否基于检索上下文，适合发现幻觉。
- `answer_relevancy` 可以检查回答是否切题。
- `context_recall` 可以检查检索上下文是否覆盖标准答案需要的信息。
- `context_precision` 可以检查检索上下文是否相关、排序是否合理。

等这 4 个指标稳定后，可以再尝试加入答案类参考指标：

```env
RAGAS_METRICS=faithfulness,answer_relevancy,context_recall,context_precision,answer_correctness,semantic_similarity
```

注意：`answer_correctness` 和 `semantic_similarity` 在不同 RAGAS 版本里的类名和实现差异较多。如果脚本提示该指标不可用，先确认当前运行环境安装的 RAGAS 版本。

## 本地模型说明

本项目使用中转站调用 LLM 评审模型，但中转站没有 embedding 接口。因此，embedding 相关指标需要使用本地 embedding 模型。

当前推荐使用：

```text
bge-small-zh-v1.5
```

原因：

- BGE 是 embedding 模型，可以生成 `answer_relevancy` 和语义相似度指标所需的向量。
- `bge-small-zh-v1.5` 对中文更友好，适合本项目的中文菜谱问答场景。
- 该模型已经存在于项目目录中。

`.env` 中的配置：

```env
RAGAS_EMBEDDING_MODEL=bge-small-zh-v1.5
```

如果在宿主机项目根目录运行评测，这个相对路径会指向：

```text
/home/kdm/MyWorkSpace/AgentLearnSpace/AllProjects/What-to-eat-today-main/What-to-eat-today-main/bge-small-zh-v1.5
```

如果在 Docker 容器内部运行评测，应使用容器路径：

```env
RAGAS_EMBEDDING_MODEL=/app/bge-small-zh-v1.5
```

## 为什么不用 `text-embedding-3-small`

`text-embedding-3-small` 是 OpenAI 的 embedding 模型名。它只有在当前 API 服务支持 `/embeddings` 接口时才适合使用。

你的中转站目前没有 embedding 接口，因此：

- 不能依赖中转站调用 `text-embedding-3-small`。
- 没必要先把 `text-embedding-3-small` 搞到本地。
- 当前更合理的做法是直接使用已有的本地 `bge-small-zh-v1.5`。

## 常用命令

严格 1 条快测：

```bash
python eval/run_eval.py --input eval/user_input/quick_test_1.jsonl --max-workers 1
```

当所有选中指标都不是 `NaN` 后，再跑 30 条：

```bash
python eval/run_eval.py --input eval/user_input/standard_30.jsonl --max-workers 1
```

检查结果是否有 `NaN`：

```bash
python - <<'PY'
import json, math
from pathlib import Path

rows = [json.loads(line) for line in Path("eval/result/ragas_scores.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
bad = []
for row in rows:
    for metric, value in (row.get("scores") or {}).items():
        if value is None or (isinstance(value, float) and math.isnan(value)):
            bad.append(f"{row.get('id')}:{metric}")

print("rows:", len(rows))
print("bad:", bad)
PY
```
