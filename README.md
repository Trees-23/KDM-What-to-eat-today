# RecipeRAG

面向中文菜谱检索与烹饪问答的 GraphRAG 应用，基于 Neo4j、Milvus 和大模型。项目的 Docker 启动链会从 Git 中追踪的菜谱 CSV 自动构建图数据库、Parent Document Store（PDS）和 Milvus V2 向量库；不依赖开发者电脑中的数据库、模型或 `run/` 目录。

![界面](./view.png)

## 快速部署

需要 Docker Desktop（或 Docker Engine，含 `docker compose` 插件）、联网下载镜像和嵌入模型，以及一个 OpenAI 兼容 API 的密钥。无需安装 Node.js 或 Python。

```bash
git clone https://github.com/Trees-23/RecipeRAG.git RecipeRAG
cd RecipeRAG
cp .env.example .env
# 编辑 .env，替换所有 CHANGE_ME 值
chmod +x start.sh stop.sh
./start.sh
```

Windows 用户运行：

```bat
copy .env.example .env
REM 编辑 .env，替换所有 CHANGE_ME 值
start.bat
```

启动完成后访问：

- 应用：<http://localhost>
- 后端健康检查：<http://localhost:8000/health>
- Neo4j：<http://localhost:7474>
- MinIO 控制台：<http://localhost:9001>

首次启动需要下载嵌入模型并生成向量，耗时取决于网络、CPU 和可用内存。后续启动复用 Docker 卷，一般不重新下载或重新向量化。

## 数据如何保持一致

项目中版本受控的 `data/cypher/` 是部署数据源。每次启动都会计算以下文件的摘要：

- `nodes.csv`、`relationships.csv`
- `tips_nodes.csv`、`tips_relationships.csv`
- `neo4j_import.cypher`

摘要未变化时保留已构建的数据；摘要变化时，只清空本 Compose 项目自己的 Neo4j 卷，并按下列顺序重建：

```text
受版本控制的 CSV
  -> Neo4j 图
  -> PDS
  -> Milvus V2 collection
  -> retrieval_artifact_manifest.json
  -> 后端和前端
```

新的 PDS build 会对应一个新的 Milvus collection，旧 collection 不会被自动删除。后端只使用活动 manifest 指向的 collection，因此不会把旧向量和新图混在一起。

该流程不会连接、清空或修改外部 Neo4j/Milvus。不要将本 Compose 的命名卷用于其他项目的数据。

## 日常操作

```bash
# 查看初始化进度，首次启动最有用
docker compose logs -f neo4j-bootstrap retrieval-bootstrap

# 查看全部服务
docker compose ps

# 正常停止并保留数据
docker compose down

# 重新启动；bootstrap 会重新检查源摘要，未变时复用已有工件
./start.sh
```

运行 `./stop.sh` 后选择选项 2，才会删除本项目全部 Docker 卷。该操作不可恢复，会删除 Neo4j、Milvus、PDS、模型缓存和本地运行数据。

## 配置说明

`.env` 必填项：

- `NEO4J_PASSWORD`
- `MINIO_ACCESS_KEY` 与 `MINIO_SECRET_KEY`
- `OPENAI_API_KEY`

`NEO4J_PASSWORD`、`MINIO_ACCESS_KEY` 和 `MINIO_SECRET_KEY` 都是本机服务账号，不需要到第三方平台申请。Linux/macOS 可以各执行一次下面的命令，把输出填入对应项：

~~~bash
openssl rand -hex 24
~~~

`OPENAI_API_KEY`、`OPENAI_BASE_URL` 和 `LLM_MODEL` 则填写你自己的 OpenAI 兼容 API 提供方配置。

可选项：

- `OPENAI_BASE_URL`：OpenAI 兼容服务地址。
- `EMBEDDING_MODEL`：默认 `BAAI/bge-small-zh-v1.5`；填写 Hugging Face 模型名，首次启动会下载并缓存在 Docker 卷中。不要填写宿主机上的 `/app/...` 本地路径。
- `HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`：下载模型或调用模型服务需要代理时使用。

`.env` 包含密码和 API Key，已被 Git 忽略，不能提交。

## 从旧版本迁移

如果本机已经运行过旧版本，旧的 Docker 卷会保留原有 Neo4j 和 MinIO 凭据。先在 `.env` 填入这些旧凭据，再执行 `./start.sh`；不要直接给已有的 MinIO 卷换密码，否则 Milvus 会无法认证。

希望改用新密码时，先停止服务，再通过 `./stop.sh` 选择选项 2 删除**本项目**旧卷，随后按新的 `.env` 冷启动。该操作会删除本机的图、向量、PDS 和模型缓存，但 Git 中的菜谱源文件不受影响。

## 架构

- 前端：Next.js
- 后端：Python + Flask
- 图数据库：Neo4j
- 向量数据库：Milvus
- 检索：Intent Planner、PDS、受限 Milvus V2 向量检索和推荐约束

## 许可证

本项目采用 [MIT License](./LICENSE)。菜谱内容来源和致谢见仓库历史与数据文件中的说明。
