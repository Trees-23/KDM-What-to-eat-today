@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo.
echo 1. 停止服务并保留数据（推荐）
echo 2. 删除本项目全部数据卷（不可恢复）
set /p choice="请选择 (1/2，默认 1): "

if "%choice%"=="2" (
    set /p confirm="确认删除 Neo4j、Milvus、PDS 和模型缓存？(y/N): "
    if /i "!confirm!"=="y" (
        docker compose down -v
    ) else (
        docker compose down
    )
) else (
    docker compose down
)
