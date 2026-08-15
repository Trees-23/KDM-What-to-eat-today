#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "$0")/../../../../.." && pwd)
OUT=$(cd "$(dirname "$0")/.." && pwd)
RUN_ID=$(basename "$OUT")
RUNNER="$OUT/components/exam_runner.py"
OLD_PID=$1

while kill -0 "$OLD_PID" 2>/dev/null; do
  sleep 20
done

python "$RUNNER" components --variant old > "$OUT/components/old-isolated.stdout"

EXAM_RUN_ID="$RUN_ID" EXAM_VARIANT=new EXAM_NEW_PATH_TRAFFIC_PERCENT=100 \
EXAM_ENTITY_DIRECT_ENABLED=true EXAM_QUERY_PLAN_ENABLED=true \
EXAM_TARGETED_GRAPH_ENABLED=true EXAM_MILVUS_V2_ENABLED=true \
EXAM_PARENT_STORE_ENABLED=true \
EXAM_PARENT_STORE_PATH=/app/run/retrieval/parent_store.pds_2a8c0807733eb8022a623659.sqlite \
EXAM_MILVUS_DATABASE=default \
EXAM_MILVUS_COLLECTION=cooking_knowledge_v2_pds_2a8c0807 \
EXAM_LEGACY_FALLBACK_ENABLED=true \
docker compose -f "$ROOT/docker-compose.yml" -f "$ROOT/_other/考试/监考/docker-compose.exam.yml" up -d backend

for _ in $(seq 1 30); do
  if curl -fsS --max-time 5 http://localhost:8000/health > "$OUT/components/new-health.json"; then
    break
  fi
  sleep 2
done
test -s "$OUT/components/new-health.json"
{
  printf '\n## new 变体启动\n\n'
  printf '%s\n' "- 启动时间：\`$(date -Iseconds)\`。"
  printf '%s\n' '- 环境：`EXAM_VARIANT=new`，新路径流量 `100`，实体直达/QueryPlan/目标图/Milvus V2/PDS 均为 `true`，PDS 与 collection 使用预检冻结 artifact，legacy fallback 为 `true`。'
  printf '%s' '- 健康检查：`'
  cat "$OUT/components/new-health.json"
  printf '%s\n' '`。'
} >> "$OUT/preflight.md"

python "$RUNNER" api --variant new
python "$RUNNER" components --variant new > "$OUT/components/new-isolated.stdout"
python "$ROOT/_other/考试/工具/汇总结果.py" \
  --bank "$ROOT/_other/考试/试卷题库.json" \
  --results "$OUT/old.jsonl" "$OUT/new.jsonl" \
  --output-dir "$OUT" > "$OUT/components/汇总结果.stdout"
python "$OUT/components/finalize_exam.py" "$OUT" > "$OUT/components/finalize_exam.stdout"
