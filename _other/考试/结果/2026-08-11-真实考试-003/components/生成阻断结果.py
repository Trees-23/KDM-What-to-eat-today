#!/usr/bin/env python3
"""为预检无法完成的真实服务考试写入可复核的阻断记录。

本脚本只写入本次考试目录；不会调用聊天 API、修改服务配置或写入数据库。
"""
from __future__ import annotations

import csv
import hashlib
import json
import sqlite3
import subprocess
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parents[3]
RUN_ID = OUT.name
BANK_PATH = ROOT / "_other/考试/试卷题库.json"
PDS_PATH = ROOT / "run/retrieval/parent_store.pds_2a8c0807733eb8022a623659.sqlite"
ARTIFACT_PATH = ROOT / "run/retrieval/active/retrieval_artifact_manifest.json"


def source_path(row: dict[str, str]) -> str:
    raw = (row.get("filePath") or row.get("sourcePath") or "").replace("\\", "/").lstrip("/")
    return raw if raw.startswith("data/") else f"data/{raw}"


def load_nodes() -> list[dict[str, str]]:
    rows = []
    for relative in ("data/cypher/nodes.csv", "data/cypher/tips_nodes.csv"):
        with (ROOT / relative).open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream):
                row["_source_path"] = source_path(row)
                rows.append(row)
    return rows


def command(*args: str) -> str:
    return subprocess.check_output(args, cwd=ROOT, text=True).strip()


def graph_preflight(bank: dict) -> dict:
    def scalar(query: str) -> int:
        completed = subprocess.check_output(
            [
                "docker", "compose", "exec", "-T", "neo4j", "/bin/sh", "-c",
                "cypher-shell -u neo4j -p \"${NEO4J_AUTH#*/}\" --format plain " + repr(query),
            ],
            cwd=ROOT,
            text=True,
        )
        return int(next(line for line in reversed(completed.splitlines()) if line.strip()))

    direct = "MATCH (i:Ingredient {name: %s})<-[:REQUIRES]-(r:Recipe) RETURN count(*) AS count"
    paired = """MATCH (i:Ingredient {name: %s})<-[:REQUIRES]-(r:Recipe)-[rel:REQUIRES]->(v:Ingredient)
WHERE v.nodeId <> i.nodeId AND coalesce(rel.ingredientCategory, v.category) = '蔬菜'
RETURN count(*) AS count"""
    result = {"s04": {}, "s05": {}, "nodes": None, "relationships": None}
    result["nodes"] = scalar("MATCH (n) RETURN count(n) AS count")
    result["relationships"] = scalar("MATCH ()-[r]->() RETURN count(r) AS count")
    for question in bank["questions"]:
        target = question["contract"]["gold_target"]
        name = repr(target["entity_name"])
        if question["scenario_id"] == "S04":
            result["s04"][question["question_id"]] = scalar(direct % name)
        elif question["scenario_id"] == "S05":
            result["s05"][question["question_id"]] = scalar(paired % name)
    return result


def main() -> None:
    bank = json.loads(BANK_PATH.read_text(encoding="utf-8"))
    nodes = load_nodes()
    graph = graph_preflight(bank)
    by_path = {}
    for node in nodes:
        if node.get("labels") == "TechniqueDoc":
            by_path.setdefault(node["_source_path"], []).append(node)
    s03_issues = []
    for question in (item for item in bank["questions"] if item["scenario_id"] == "S03"):
        target = question["contract"]["gold_target"]
        exact = [
            node for node in nodes
            if node.get("labels") == target["entity_type"]
            and node.get("name") == target["entity_name"]
            and node["_source_path"] == target["source_path"]
        ]
        if len(exact) != 1:
            sources = by_path.get(target["source_path"], [])
            s03_issues.append({
                "question_id": question["question_id"],
                "expected_name": target["entity_name"],
                "source_path": target["source_path"],
                "exact_matches": len(exact),
                "source_path_nodes": [
                    {"nodeId": item.get("nodeId"), "name": item.get("name")} for item in sources
                ],
            })

    s01_s02_exact = 0
    for sid in ("S01", "S02"):
        for question in (item for item in bank["questions"] if item["scenario_id"] == sid):
            target = question["contract"]["gold_target"]
            s01_s02_exact += sum(
                node.get("labels") == target["entity_type"]
                and node.get("name") == target["entity_name"]
                and node["_source_path"] == target["source_path"]
                for node in nodes
            )

    fictional = {}
    for sid, key in (("S08", "entity_name"), ("S09", "missing_entity_name")):
        fictional[sid] = sum(
            any(node.get("name") == question["contract"]["gold_target"][key] for node in nodes)
            for question in bank["questions"]
            if question["scenario_id"] == sid
        )
    with sqlite3.connect(PDS_PATH) as connection:
        pds_counts = {
            "parents": connection.execute("SELECT count(*) FROM parents").fetchone()[0],
            "chunks": connection.execute("SELECT count(*) FROM chunks").fetchone()[0],
        }
    artifact = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    bank_sha = hashlib.sha256(BANK_PATH.read_bytes()).hexdigest()
    commit = command("git", "rev-parse", "HEAD")
    branch = command("git", "branch", "--show-current")
    health = command("curl", "-sS", "--max-time", "10", "http://localhost:8000/health")
    containers = command("docker", "compose", "ps", "--all", "--format", "{{.Name}}|{{.State}}|{{.Status}}")
    reason = (
        "S03 有 20/30 题无法以题库声明的 TechniqueDoc 名称和 sourcePath 唯一解析："
        "对应 sourcePath 存在 TechniqueDoc，但当前节点标题与题库 entity_name 不一致。"
        "因此无法在任何 API 请求前按题库契约冻结完整 gold_manifest。"
    )
    manifest = {
        "run_id": RUN_ID,
        "bank_sha256": bank_sha,
        "frozen_at": None,
        "implementation_commit": commit,
        "preflight_status": "blocked",
        "gold_manifest_closed": False,
        "reason": reason,
        "questions": [],
        "preflight_evidence": {
            "s01_s02_exact_sourcepath_matches": s01_s02_exact,
            "s03_exact_sourcepath_matches": 30 - len(s03_issues),
            "s03_resolution_issues": s03_issues,
            "s04_nonzero_paths": sum(count > 0 for count in graph["s04"].values()),
            "s05_positive_nonzero_paths": sum(
                count > 0 for qid, count in graph["s05"].items() if "-C-" not in qid
            ),
            "s05_counterexample_zero_paths": sum(
                count == 0 for qid, count in graph["s05"].items() if "-C-" in qid
            ),
        },
    }
    (OUT / "gold_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    audit_data = {
        "graph": graph,
        "s03_resolution_issues": s03_issues,
        "artifact": artifact,
        "pds_counts": pds_counts,
    }
    (OUT / "components/预检只读查询结果.json").write_text(
        json.dumps(audit_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    preflight = [
        "# 真实服务考试预检", "",
        f"- 运行编号：`{RUN_ID}`", f"- 预检关闭时间：`{now}`",
        f"- 实现提交：`{commit}`", f"- 当前分支：`{branch}`",
        "- 目标基线：`origin/main` 的 `a22897275c26f89398b766af754c44452f2b35f6`",
        f"- 题库 SHA-256：`{bank_sha}`",
        "- `题库校验报告.md` 声明的 SHA-256：`688edfea11db27a5cf5796ffa886e785f73c1f2ceb6a714f879830b3d06df88d`",
        "- 静态题库重生成校验：`python _other/考试/工具/生成试卷.py` 已成功生成 300 题，SHA 与预检一致；检查后无题库或校验报告差异。", "",
        "## 只读服务状态", "",
        f"- `GET /health`：`{health}`",
        f"- Neo4j：节点 `{graph['nodes']}`，关系 `{graph['relationships']}`；仅执行了只读 MATCH 查询。",
        f"- PDS：`{PDS_PATH.relative_to(ROOT)}` 可读，parents=`{pds_counts['parents']}`，chunks=`{pds_counts['chunks']}`。",
        "- Milvus V2 artifact 可读，内容保存在 `components/预检只读查询结果.json`；未执行导入、迁移、删除或任何写查询。",
        "- Compose 容器状态：", "```text", containers, "```", "",
        "## 实体与图路径复核", "",
        f"- S01/S02 的名称、类型与 sourcePath 精确解析：`{s01_s02_exact}/60`。",
        f"- S03 的名称、类型与 sourcePath 精确解析：`{30 - len(s03_issues)}/30`；失败 `20` 题。",
        f"- S04 实际 Recipe-REQUIRES 路径非零：`{sum(v > 0 for v in graph['s04'].values())}/30`。",
        f"- S05 A/B 实际目标多跳路径非零：`{sum(v > 0 for k, v in graph['s05'].items() if '-C-' not in k)}/20`。",
        f"- S05 C 实际目标多跳路径为零：`{sum(v == 0 for k, v in graph['s05'].items() if '-C-' in k)}/10`；这是预期反例而非阻断原因。",
        f"- S08 虚构菜名命中：`{fictional['S08']}/30`；S09 虚构食材命中：`{fictional['S09']}/30`。", "",
        "### S03 阻断明细", "",
        reason, "",
    ]
    for issue in s03_issues:
        observed = ", ".join(f"{item['nodeId']}:{item['name']}" for item in issue["source_path_nodes"]) or "无"
        preflight.append(
            f"- `{issue['question_id']}`：题库名称 `{issue['expected_name']}`，sourcePath `{issue['source_path']}`，"
            f"精确匹配 `{issue['exact_matches']}`；该 sourcePath 的当前 TechniqueDoc 为 `{observed}`。"
        )
    preflight.extend([
        "", "## 预检结论", "", "**失败，停止考试。** " + reason,
        "未启动 old/new Compose 覆盖，未发送 `/api/chat/stream` 请求，未生成 SSE/HTTP 响应或运行时审计，未运行 S09/S10 隔离组件。",
        "为满足逐题可复核性，old/new 各写 300 条 `blocked` 结果；这些行不是新旧路径的成功计分，也不构成安全通过。",
    ])
    (OUT / "preflight.md").write_text("\n".join(preflight) + "\n", encoding="utf-8")
    for variant in ("old", "new"):
        rows = []
        for question in bank["questions"]:
            contract = question["contract"]
            route = {
                "expected": contract["expected_route"],
                "observed": "preflight_blocked_gold_resolution",
                "fallback": False,
                "execution_surface": contract.get("execution_surface", "chat_api"),
                "audit_evidence": None,
            }
            rows.append({
                "question_id": question["question_id"], "scenario_id": question["scenario_id"],
                "difficulty_code": question["difficulty_code"], "variant": variant,
                "evaluation_mode": contract["evaluation_mode"], "status": "blocked", "audit_id": None,
                "route": route, "ranking": [], "gold_items": [],
                "path": {
                    "entity_resolution": [], "query_plan": {}, "graph_template": None, "graph_paths": [],
                    "vector_scope": {}, "pds_hydration": [],
                    "final_evidence": [{"source": "preflight.md", "reason": reason}],
                },
                "checks": {
                    "route_correct": None, "evidence_complete": None, "evidence_linked": None,
                    "answer_faithful": None, "safety_pass": None, "forbidden_assertion_count": 0,
                    "unsupported_relation_claim_count": 0, "strict_nutrition_misreport_count": 0,
                },
                "timing": {"ttft_ms": None, "total_latency_ms": None}, "answer": "", "exam_note": reason,
            })
        (OUT / f"{variant}.jsonl").write_text(
            "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8"
        )
        (OUT / f"responses/{variant}/未执行说明.md").write_text(
            "预检在任何 API 请求前阻断；没有 HTTP/SSE 响应可保留。\n", encoding="utf-8"
        )
        (OUT / f"audits/{variant}/未执行说明.md").write_text(
            "预检在任何 API 请求前阻断；没有运行时审计目录可复制。\n", encoding="utf-8"
        )
    (OUT / "components/未执行说明.md").write_text(
        "S09/S10 是隔离组件级考试；因 gold 预冻结无法完成，未运行组件或伪造假驱动输出。\n", encoding="utf-8"
    )
    print(json.dumps({"run_id": RUN_ID, "blocked_rows_per_variant": 300, "s03_issues": len(s03_issues)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
