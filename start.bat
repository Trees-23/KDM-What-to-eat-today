@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo.
echo ===============================================
echo       今天吃什么 - Docker 部署
echo ===============================================
echo.

docker info >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker Desktop 未运行
    pause
    exit /b 1
)

docker compose version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] 未找到 Docker Compose 插件
    pause
    exit /b 1
)

if not exist ".env" (
    copy ".env.example" ".env" >nul
    echo [INFO] 已创建 .env。请替换其中所有 CHANGE_ME 值后重新运行。
    pause
    exit /b 1
)

findstr /R /C:"=CHANGE_ME" .env >nul 2>&1
if not errorlevel 1 (
    echo [ERROR] .env 仍包含示例值。请设置数据库密码、MinIO 凭据和 OPENAI_API_KEY。
    pause
    exit /b 1
)

for %%K in (NEO4J_PASSWORD MINIO_ACCESS_KEY MINIO_SECRET_KEY OPENAI_API_KEY) do (
    findstr /R /C:"^%%K=.+" .env >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] .env 缺少 %%K
        pause
        exit /b 1
    )
)

findstr /R /C:"^EMBEDDING_MODEL=/" /C:"^RERANK_MODEL=/" .env >nul 2>&1
if not errorlevel 1 (
    echo [ERROR] .env 使用了开发机模型路径。请改为 Hugging Face 模型名。
    pause
    exit /b 1
)

echo [INFO] 拉取镜像并启动服务。首次启动会下载模型和构建检索工件，请耐心等待。
docker compose pull
if errorlevel 1 exit /b 1
docker compose up -d --build --force-recreate
if errorlevel 1 exit /b 1

set max_retries=450
set retry_count=0
:check_backend
curl -f http://localhost:8000/health >nul 2>&1
if not errorlevel 1 goto ready
set /a retry_count+=1
if !retry_count! geq !max_retries! (
    echo.
    echo [ERROR] 启动超时。请查看：docker compose logs retrieval-bootstrap backend
    pause
    exit /b 1
)
echo|set /p="."
timeout /t 2 /nobreak >nul
goto check_backend

:ready
echo.
echo [SUCCESS] 部署完成：http://localhost
echo [INFO] 初始化日志：docker compose logs -f neo4j-bootstrap retrieval-bootstrap
start http://localhost
pause
