"""
Generate Neo4j import CSV files for markdown files under data/tips.

The project already imports recipe data from nodes.csv and relationships.csv.
This script creates a separate, repeatable import source for technique/tip
documents so they can be added to Neo4j and then indexed into Milvus.
"""

import csv
import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TIPS_DIR = ROOT / "tips"
OUT_DIR = ROOT / "cypher"
NODES_OUT = OUT_DIR / "tips_nodes.csv"
RELS_OUT = OUT_DIR / "tips_relationships.csv"


COMMON_KEYWORDS = [
    "腌", "腌肉", "腌制", "腌渍", "入味", "调味", "去腥", "焯水", "凉拌",
    "炒", "煎", "蒸", "煮", "炸", "烤", "微波炉", "空气炸锅", "高压锅",
    "食品安全", "厨房准备", "食材相克", "禁忌", "油温", "糖色", "辅料",
    "专业术语", "工具", "火候", "容器", "时间", "技巧",
]


def stable_id(prefix: str, path: Path, suffix: str = "") -> str:
    rel = path.relative_to(ROOT).as_posix()
    digest = hashlib.sha1(f"{rel}:{suffix}".encode("utf-8")).hexdigest()[:12]
    return f"{prefix}_{digest}"


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def csv_text(text: str) -> str:
    text = clean_text(text)
    text = re.sub(r"[ \t]+", " ", text)
    return text


def title_from_markdown(path: Path, text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return path.stem


def split_markdown_sections(text: str) -> list[tuple[str, str]]:
    lines = text.splitlines()
    sections: list[tuple[str, list[str]]] = []
    current_title = "正文"
    current_lines: list[str] = []

    for line in lines:
        heading = re.match(r"^(#{2,4})\s+(.+?)\s*$", line)
        if heading:
            if current_lines:
                sections.append((current_title, current_lines))
            current_title = heading.group(2).strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        sections.append((current_title, current_lines))

    cleaned = []
    for title, body_lines in sections:
        body = clean_text("\n".join(body_lines))
        if body:
            cleaned.append((title, body))
    return cleaned


def compact_summary(text: str, max_chars: int = 500) -> str:
    plain = re.sub(r"```.*?```", " ", text, flags=re.S)
    plain = re.sub(r"[#>*`|_\-\[\]（）()]+", " ", plain)
    plain = re.sub(r"\s+", " ", plain).strip()
    return plain[:max_chars]


def extract_tags(path: Path, title: str, text: str, sections: list[tuple[str, str]]) -> list[str]:
    tags = {title, path.stem}
    normalized_title = re.sub(r"[^\w\u4e00-\u9fff]+", "", title)
    if normalized_title:
        tags.add(normalized_title)
    if path.stem.startswith("学习"):
        tags.add(path.stem.replace("学习", "", 1))
    for section_title, _body in sections:
        tags.add(section_title)
    for keyword in COMMON_KEYWORDS:
        if keyword in text:
            tags.add(keyword)
    return sorted(tag for tag in tags if tag)


def category_from_path(path: Path) -> str:
    rel_parts = path.relative_to(TIPS_DIR).parts
    if len(rel_parts) > 1:
        if rel_parts[0] == "learn":
            return "烹饪技巧"
        if rel_parts[0] == "advanced":
            return "高级技巧"
        return rel_parts[0]
    return "通用知识"


def main() -> int:
    tip_files = sorted(TIPS_DIR.rglob("*.md"))
    node_rows = []
    rel_rows = []

    for doc_index, path in enumerate(tip_files, start=1):
        text = clean_text(path.read_text(encoding="utf-8"))
        if not text:
            continue

        doc_id = stable_id("tipdoc", path)
        title = title_from_markdown(path, text)
        sections = split_markdown_sections(text)
        tags = extract_tags(path, title, text, sections)
        category = category_from_path(path)
        rel_path = path.relative_to(ROOT).as_posix()

        node_rows.append({
            "nodeId": doc_id,
            "labels": "TechniqueDoc",
            "name": title,
            "title": title,
            "sectionTitle": "",
            "category": category,
            "sourcePath": rel_path,
            "chunkIndex": "",
            "tags": ",".join(tags),
            "summary": compact_summary(text),
            "content": csv_text(text),
        })

        for chunk_index, (section_title, body) in enumerate(sections):
            chunk_id = stable_id("tipchunk", path, str(chunk_index))
            chunk_name = f"{title} / {section_title}" if section_title != "正文" else title
            node_rows.append({
                "nodeId": chunk_id,
                "labels": "TechniqueChunk",
                "name": chunk_name,
                "title": title,
                "sectionTitle": section_title,
                "category": category,
                "sourcePath": rel_path,
                "chunkIndex": str(chunk_index),
                "tags": ",".join(tags),
                "summary": compact_summary(body),
                "content": csv_text(body),
            })
            rel_rows.append({
                "startNodeId": doc_id,
                "endNodeId": chunk_id,
                "relationshipType": "HAS_CHUNK",
                "relationshipId": f"TIP_REL_{doc_index:04d}_{chunk_index:03d}",
                "chunkOrder": str(chunk_index),
            })

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with NODES_OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "nodeId", "labels", "name", "title", "sectionTitle", "category",
                "sourcePath", "chunkIndex", "tags", "summary", "content",
            ],
        )
        writer.writeheader()
        writer.writerows(node_rows)

    with RELS_OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "startNodeId", "endNodeId", "relationshipType",
                "relationshipId", "chunkOrder",
            ],
        )
        writer.writeheader()
        writer.writerows(rel_rows)

    print(f"generated {len(node_rows)} tip nodes -> {NODES_OUT}")
    print(f"generated {len(rel_rows)} tip relationships -> {RELS_OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
