#!/bin/bash

# 今天吃什么 - 统一启动脚本
# 支持 Linux/macOS/Windows(WSL)

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_message() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

print_header() {
    echo
    print_message $CYAN "==============================================="
    print_message $WHITE "      今天吃什么 - AI美食推荐助手"
    print_message $CYAN "==============================================="
    echo
}

print_step() {
    print_message $BLUE "[STEP] $1"
}

print_success() {
    print_message $GREEN "[SUCCESS] $1"
}

print_error() {
    print_message $RED "[ERROR] $1"
}

print_warning() {
    print_message $YELLOW "[WARNING] $1"
}

print_info() {
    print_message $PURPLE "[INFO] $1"
}

# 检查命令是否存在
check_command() {
    if ! command -v $1 &> /dev/null; then
        print_error "$1 未安装或不在PATH中"
        return 1
    fi
    return 0
}

# 检查Docker环境
check_docker() {
    print_step "检查Docker环境..."
    
    if ! check_command docker; then
        print_error "Docker未安装，请先安装Docker"
        echo
        print_info "安装指南："
        print_info "  - Linux: https://docs.docker.com/engine/install/"
        print_info "  - macOS: https://docs.docker.com/desktop/mac/"
        print_info "  - Windows: https://docs.docker.com/desktop/windows/"
        exit 1
    fi
    
    if ! docker info &> /dev/null; then
        print_error "Docker未运行，请启动Docker服务"
        exit 1
    fi
    
    if ! docker compose version &> /dev/null; then
        print_error "Docker Compose未安装"
        exit 1
    fi
    
    print_success "Docker环境检查通过"
}

# 检查环境配置
check_environment() {
    print_step "检查环境配置..."

    # 检查.env文件
    if [ ! -f ".env" ]; then
        print_warning ".env文件不存在，正在创建..."
        if [ -f ".env.example" ]; then
            cp .env.example .env
            print_info "已从.env.example创建.env文件"
        else
            print_error ".env.example文件不存在，无法创建配置文件"
            print_info "请手动创建.env文件并配置必要的环境变量"
            return 1
        fi
    fi

    if grep -qE '=CHANGE_ME|=your_.*_here' .env 2>/dev/null; then
        print_error ".env 仍包含示例值，请先替换 NEO4J_PASSWORD、MinIO 凭据和 OPENAI_API_KEY"
        exit 1
    fi
    local required_key
    for required_key in NEO4J_PASSWORD MINIO_ACCESS_KEY MINIO_SECRET_KEY OPENAI_API_KEY; do
        if ! grep -qE "^${required_key}=.+" .env 2>/dev/null; then
            print_error ".env 缺少 ${required_key}"
            exit 1
        fi
    done
    if grep -qE '^(EMBEDDING_MODEL|RERANK_MODEL)=/' .env 2>/dev/null; then
        print_error ".env 使用了开发机模型路径。部署配置必须使用可下载的模型名，例如 BAAI/bge-small-zh-v1.5"
        exit 1
    fi
    print_success "环境配置检查通过"
}

# 前端依赖将在Docker容器中自动安装
check_frontend() {
    print_info "前端依赖将在Docker容器中自动安装"
}

# 创建必要目录
create_directories() {
    print_step "创建必要目录..."
    print_success "Docker 将创建并管理运行数据卷"
}

# 启动服务
start_services() {
    print_step "启动所有服务..."
    
    # 拉取镜像
    print_info "拉取Docker镜像..."
    docker compose pull
    
    # 构建自定义镜像
    print_info "构建应用镜像..."
    docker compose build
    
    # 启动服务
    print_info "启动服务容器..."
    # bootstrap 服务每次都执行；内部摘要和 build ID 负责避免无变化时重复构建。
    docker compose up -d --force-recreate
    
    print_success "服务启动命令执行完成"
}

# 等待服务就绪
wait_for_services() {
    print_step "等待服务启动..."

    # 首次下载嵌入模型和生成向量可能超过两分钟。
    local max_retries=450
    local retry_count=0

    # 等待后端服务
    print_info "等待后端服务启动..."
    while [ $retry_count -lt $max_retries ]; do
        if curl -f http://localhost:8000/health &> /dev/null; then
            print_success "后端服务启动成功"
            break
        fi

        retry_count=$((retry_count + 1))
        echo -n "."
        sleep 2
    done
    echo

    if [ $retry_count -eq $max_retries ]; then
        print_error "后端服务启动超时"
        print_info "查看日志: docker compose logs retrieval-bootstrap backend"
        print_info "常见问题："
        print_info "  - 检查端口8000是否被占用"
        print_info "  - 检查Docker内存是否充足"
        print_info "  - 检查API密钥配置是否正确"
        exit 1
    fi

    # 等待Nginx代理服务
    print_info "等待Nginx代理服务启动..."
    retry_count=0
    while [ $retry_count -lt $max_retries ]; do
        if curl -f http://localhost &> /dev/null; then
            print_success "Nginx代理服务启动成功"
            break
        fi

        retry_count=$((retry_count + 1))
        echo -n "."
        sleep 2
    done
    echo

    if [ $retry_count -eq $max_retries ]; then
        print_error "Nginx代理服务启动超时"
        print_info "查看日志: docker compose logs nginx"
        print_info "尝试直接访问前端: http://localhost:3000"
        # 不退出，因为可以直接访问前端
    fi

    # API功能将在应用启动后可用
    print_info "API功能将在应用启动后可用"
}

# 显示服务信息
show_services() {
    echo
    print_message $CYAN "==============================================="
    print_message $WHITE "           🎉 部署完成！"
    print_message $CYAN "==============================================="
    echo
    
    print_message $GREEN "📋 服务访问地址："
    echo "   🌐 应用首页:     http://localhost"
    echo "   ⚛️  前端应用:     http://localhost:3000"
    echo "   🐍 后端API:      http://localhost:8000"
    echo "   📊 Neo4j浏览器:  http://localhost:7474"
    echo "      用户名: neo4j，密码见 .env"
    echo "   🗄️  Milvus控制台: http://localhost:9001"
    echo "      凭据见 .env"
    echo
    
    print_message $YELLOW "📝 管理命令："
    echo "   查看服务状态: docker compose ps"
    echo "   查看日志:     docker compose logs -f [service_name]"
    echo "   停止服务:     docker compose down"
    echo "   清空项目数据: ./stop.sh 后选择 2"
    echo
    
    print_message $PURPLE "💡 开发提示："
    echo "   - 首次启动会下载模型并构建图、PDS、Milvus，耗时取决于网络和 CPU"
    echo "   - 菜谱 CSV 变更后再次执行 ./start.sh，会重建本项目图和检索工件"
    echo
}

# 主函数
main() {
    print_header

    check_docker
    check_environment
    create_directories
    check_frontend
    start_services
    wait_for_services
    show_services
    
    print_success "🚀 系统启动完成，正在为您打开应用..."
    
    # 尝试打开浏览器
    if command -v xdg-open &> /dev/null; then
        xdg-open http://localhost &
    elif command -v open &> /dev/null; then
        open http://localhost &
    elif command -v start &> /dev/null; then
        start http://localhost &
    fi
    
    echo
    print_info "按 Ctrl+C 退出"
}

# 信号处理
trap 'echo; print_info "正在停止服务..."; docker compose down; exit 0' INT TERM

# 执行主函数
main "$@"
