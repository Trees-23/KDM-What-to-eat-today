"""从显式 Recipe Markdown 来源确定性生成 Neo4j CSV 构建工件。"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


PRODUCER_VERSION = "recipe_graph_csv_producer_v1"
BUILD_SCHEMA_VERSION = "recipe-build-manifest-v1"
SOURCE_SCHEMA_VERSION = "recipe-source-manifest-v1"
BUILD_MANIFEST_NAME = "recipe-build-manifest.json"

NODE_FIELDS = (
    "nodeId", "labels", "name", "preferredTerm", "fsn", "conceptType", "synonyms",
    "category", "difficulty", "cuisineType", "prepTime", "cookTime", "servings", "tags",
    "filePath", "amount", "unit", "isMain", "description", "stepNumber", "methods",
    "tools", "timeEstimate",
)
RELATIONSHIP_FIELDS = (
    "startNodeId", "endNodeId", "relationshipType", "relationshipId", "amount", "unit", "step_order",
)
REQUIRES_RELATIONSHIP = "801000001"
CONTAINS_STEP_RELATIONSHIP = "801000003"
ID_PREFIXES = {"Recipe": "210", "Ingredient": "310", "CookingStep": "410"}


class RecipeBuildError(ValueError):
    """显式输入不满足可复现构建契约。"""


@dataclass(frozen=True)
class SourceFile:
    path: Path
    logical_path: str
    sha256: str
    content: bytes


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _stable_id(prefix: str, key: str) -> str:
    digest = hashlib.sha256(f"{prefix}\0{key}".encode("utf-8")).digest()
    return f"{prefix}{int.from_bytes(digest[:8], 'big') % 10**15:015d}"


def _stable_relation_id(relationship_type: str, start_id: str, end_id: str) -> str:
    digest = hashlib.sha256(f"{relationship_type}\0{start_id}\0{end_id}".encode("utf-8")).hexdigest()
    return f"R_{digest[:24]}"


def _normalise_logical_path(value: str) -> str:
    path = PurePosixPath(value.replace("\\", "/"))
    if path.is_absolute() or ".." in path.parts or str(path) in {"", "."}:
        raise RecipeBuildError(f"来源路径必须是相对 source_root 的 Markdown 路径: {value}")
    return path.as_posix()


def _ensure_inside(root: Path, candidate: Path) -> Path:
    resolved = candidate.resolve()
    try:
        resolved.relative_to(root)
    except ValueError as error:
        raise RecipeBuildError(f"来源文件不能离开 source_root: {candidate}") from error
    return resolved


def _load_source_file(path: Path, logical_path: str) -> SourceFile:
    content = path.read_bytes()
    try:
        content.decode("utf-8")
    except UnicodeDecodeError as error:
        raise RecipeBuildError(f"来源不是 UTF-8 Markdown: {logical_path}") from error
    return SourceFile(path, logical_path, _sha256_bytes(content), content)


def load_sources(*, input_manifest: str | None, input_dir: str | None) -> tuple[list[SourceFile], str | None]:
    if bool(input_manifest) == bool(input_dir):
        raise RecipeBuildError("必须且只能提供 --input-manifest 或 --input-dir")

    if input_manifest:
        manifest_path = Path(input_manifest).resolve()
        if not manifest_path.is_file():
            raise RecipeBuildError(f"输入 manifest 不存在: {manifest_path}")
        try:
            manifest_content = manifest_path.read_bytes()
            payload = json.loads(manifest_content.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise RecipeBuildError(f"输入 manifest 不是有效 JSON: {error}") from error
        if not isinstance(payload, dict) or payload.get("schema_version") != SOURCE_SCHEMA_VERSION:
            raise RecipeBuildError(f"输入 manifest 必须声明 schema_version={SOURCE_SCHEMA_VERSION}")
        source_root_value = payload.get("source_root")
        if not isinstance(source_root_value, str) or not source_root_value:
            raise RecipeBuildError("输入 manifest 必须提供 source_root")
        root = (manifest_path.parent / source_root_value).resolve()
        if not root.is_dir():
            raise RecipeBuildError(f"source_root 不存在或不是目录: {root}")
        files = payload.get("files")
        if not isinstance(files, list) or not files:
            raise RecipeBuildError("输入 manifest 的 files 必须是非空数组")
        selected: list[SourceFile] = []
        seen: set[str] = set()
        for item in files:
            if not isinstance(item, dict) or not isinstance(item.get("path"), str):
                raise RecipeBuildError("输入 manifest 的 files 每项必须提供 path")
            logical_path = _normalise_logical_path(item["path"])
            if logical_path in seen:
                raise RecipeBuildError(f"输入 manifest 存在重复来源: {logical_path}")
            seen.add(logical_path)
            candidate = _ensure_inside(root, root / logical_path)
            if candidate.suffix.lower() != ".md" or not candidate.is_file():
                raise RecipeBuildError(f"来源必须是存在的 Markdown 文件: {logical_path}")
            source = _load_source_file(candidate, logical_path)
            actual_hash = source.sha256
            expected_hash = item.get("sha256")
            if expected_hash is not None:
                if not isinstance(expected_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
                    raise RecipeBuildError(f"来源 SHA-256 格式无效: {logical_path}")
                if actual_hash != expected_hash:
                    raise RecipeBuildError(f"来源 SHA-256 不匹配: {logical_path}")
            selected.append(source)
        # 解析与溯源摘要必须来自同一份字节，避免 manifest 在构建期间变更导致
        # CSV 选择的来源与记录的 SHA-256 不一致。
        return sorted(selected, key=lambda item: item.logical_path), _sha256_bytes(manifest_content)

    root = Path(str(input_dir)).resolve()
    if not root.is_dir():
        raise RecipeBuildError(f"输入目录不存在或不是目录: {root}")
    selected = []
    for candidate in sorted(root.rglob("*.md"), key=lambda item: item.as_posix()):
        resolved = _ensure_inside(root, candidate)
        if resolved.is_file():
            selected.append(_load_source_file(resolved, resolved.relative_to(root).as_posix()))
    if not selected:
        raise RecipeBuildError("输入目录没有 Markdown 文件")
    return selected, None


def _clean_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return text.strip()


def _plain_text(value: str) -> str:
    value = re.sub(r"!?(?:\[([^\]]*)\])\([^)]*\)", r"\1", value)
    value = re.sub(r"[`*_]", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip(" -:：；;，,。")


def _title_from_markdown(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", text, flags=re.M)
    title = _plain_text(match.group(1)) if match else fallback
    title = re.sub(r"(?:的)?做法$", "", title).strip()
    return title or fallback


def _h2_sections(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, flags=re.M))
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((_plain_text(match.group(1)), text[match.end():end]))
    return sections


def _list_items(section: str) -> list[str]:
    items: list[str] = []
    for line in section.splitlines():
        match = re.match(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)(.+?)\s*$", line)
        if match:
            item = _plain_text(match.group(1))
            if item:
                items.append(item)
    return items


def _recipe_description(text: str) -> str:
    first_h2 = re.search(r"^##\s+", text, flags=re.M)
    preface = text[:first_h2.start()] if first_h2 else text
    preface = re.sub(r"^#\s+.*$", "", preface, flags=re.M)
    preface = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", preface)
    return _plain_text(preface)[:500]


QUANTITY_PATTERN = re.compile(
    r"(?P<amount>\d+(?:\.\d+)?(?:\s*[-~至]\s*\d+(?:\.\d+)?)?)\s*"
    r"(?P<unit>毫升|ml|mL|ML|千克|kg|KG|克|g|G|人份|个|支|瓣|根|只|片|勺|汤匙|茶匙|杯|斤|两|块|条|颗|把|份|盘)"
)
INGREDIENT_ALIASES = {"蒜瓣": "大蒜", "大蒜瓣": "大蒜"}
COOKING_TOOL_NAMES = frozenset(
    {
        "量杯", "厨房秤", "秤", "大不锈钢碗", "不锈钢碗", "碗", "盘子", "碗与盘子",
        "炒锅", "平底锅", "蒸锅", "砂锅", "高压锅", "锅", "烤箱", "微波炉", "空气炸锅",
        "电饭煲", "燃气灶", "电磁炉", "菜刀", "剪刀", "砧板", "筷子", "炒勺", "锅铲",
        "保鲜膜", "锡纸", "烘焙纸", "打蛋器", "料理机", "破壁机", "平底煎锅", "蒸笼",
        "筛网", "小碗", "厨房用夹", "厨房夹", "食品夹", "夹子",
    }
)
COOKING_TOOL_CORES = (
    "空气炸锅烤架", "平底煎锅", "平底锅", "空气炸锅", "电压力锅", "高压锅", "压力锅",
    "电饭煲", "电饭锅", "电炖锅", "微波炉", "电磁炉", "燃气灶", "烘焙刮刀", "削皮刀",
    "水果刀", "厨房用夹", "厨房夹", "食品夹", "防烫盘夹", "保鲜膜", "烘焙油纸", "烘焙纸",
    "厨房纸", "吸油纸", "锡箔纸", "打蛋器", "搅拌器", "分蛋器", "压汁器", "料理机", "破壁机",
    "厨房秤", "克数称", "克称", "定时器", "蒸鱼盘子",
    "蒸锅", "炒锅", "煮锅", "炖煮锅", "砂锅", "煎锅", "汤锅", "奶锅", "油锅", "粥锅",
    "电蒸炉", "筛网", "滤网", "过滤网", "砧板", "锅铲", "炒勺", "蒜臼", "笊篱", "笼屉", "烤架",
    "量杯", "量酒器", "酒杯", "雪克杯", "高球杯", "模具", "容器", "菜刀", "剪刀", "筷子", "锡纸", "硅油纸",
    "锡纸盘", "调理机", "果汁机", "洗菜盆", "瓦罐", "灶台", "盘子", "锅盖", "夹子", "铲子",
    "刮刀", "餐刀", "温度计", "吧勺", "漏勺", "勺子", "蒸架", "杯子", "碗", "盘", "盆", "杯", "砵", "网", "刀", "锅",
)
TOOL_MODIFIER_PATTERN = re.compile(
    r"^(?:(?:大|中|小|特大|超大|大号|中号|小号|不锈钢|厨房用|家用|家庭|普通|深口|浅口|长柄|带盖|"
    r"带孔|玻璃|陶瓷|耐热|木制|竹制|硅胶|塑料|透明|一次性|电动|手动|可调温|多功能|圆形|方形|"
    r"不粘|厚底|严丝合缝|有点深度|有一定深度|能放进微波炉|分可控火候|不可控火候|铁|铸铁|电|煮|炖|油|"
    r"粥|利口酒|海波|雪克|调酒|餐|高球|可密封|带刻度|额外|家庭|铁))+$"
)
CALCULATION_NON_INGREDIENT_NAMES = frozenset({"时间", "冷藏时间", "加热时间", "烹饪时间", "温度", "体积", "重量", "容量", "比例"})
CALCULATION_NON_INGREDIENT_MARKERS = ("时间", "温度", "体积", "重量", "容量", "比例", "分量", "质量", "基于", "一般一个人")
NON_INGREDIENT_TEXT_MARKERS = ("注：", "如果有可能", "请尽量", "炒糖色过程")
TOOL_LIST_SEPARATOR = re.compile(r"\s*(?:[/+、，,]|或者|或|以及|及|和|与)\s*")


def _extract_amount_and_unit(item: str) -> tuple[str, str, str]:
    value = _plain_text(item)
    match = re.match(
        r"^(.+?)(?:\s*=\s*|\s+)(\d+(?:\.\d+)?(?:\s*[-~至]\s*\d+(?:\.\d+)?)?)\s*"
        r"(毫升|ml|mL|ML|千克|kg|KG|克|g|G|人份|个|支|瓣|根|只|片|勺|汤匙|茶匙|杯|斤|两|块|条|颗|把|份|盘)?(?:\s|$|[（(])",
        value,
    )
    if match:
        return _normalise_ingredient_name(match.group(1)), match.group(2).replace(" ", ""), match.group(3) or ""
    return _normalise_ingredient_name(value), "", ""


def _normalise_ingredient_name(value: str) -> str:
    value = _plain_text(value)
    value = re.split(r"[（(]", value, maxsplit=1)[0]
    value = re.sub(r"\s+", " ", value).strip(" -:：；;，,。=")
    return INGREDIENT_ALIASES.get(value, value)


def _extract_calculated_ingredient(item: str) -> tuple[str, str, str] | None:
    value = _plain_text(item)
    match = QUANTITY_PATTERN.search(value)
    if match is None:
        return None
    name_source = value[:match.start()].strip()
    suffix = value[match.end():].strip()
    if any(symbol in name_source or symbol in suffix for symbol in ("+", "-", "*", "/", "\\", "×", "÷", "^", "%", "<", ">")):
        return None
    if "=" in name_source:
        assignment = name_source.split("=")
        if len(assignment) != 2 or assignment[1].strip():
            return None
        name_source = assignment[0].strip()
    if "=" in suffix or re.search(r"[A-Za-z0-9]", name_source):
        return None
    name = _normalise_ingredient_name(name_source)
    if (
        not name
        or name in CALCULATION_NON_INGREDIENT_NAMES
        or any(marker in name for marker in CALCULATION_NON_INGREDIENT_MARKERS)
    ):
        return None
    return name, match.group("amount").replace(" ", ""), match.group("unit")


def _is_single_cooking_tool(name: str) -> bool:
    candidate = _normalise_ingredient_name(name)
    candidate = re.sub(r"^\[(?:可选|工具)\]\s*", "", candidate)
    if candidate in COOKING_TOOL_NAMES:
        return True
    candidate = re.sub(r"^(?:工具|器具|必备|可选|需要|准备|使用)\s*[：:]?\s*", "", candidate)
    candidate = re.sub(r"^(?:直径\s*)?\d+\s*(?:厘米|cm)(?:以上)?的?\s*", "", candidate, flags=re.I)
    candidate = re.sub(r"^(?:[一二三四五六七八九十\d]+\s*(?:个|只|把|口|套|张)|一口|一把|一只|一个|若干)\s*", "", candidate)
    candidate = re.sub(r"(?:\s*|[，,;；])(大小不限|若干|适量|[一二三四五六七八九十\d]+(?:个|只|把|口|套|张)|需.*|网孔.*|例如.*)$", "", candidate)
    candidate = re.sub(r"(?:一个|一只|一把|一口|若干)$", "", candidate)
    if re.fullmatch(r"\d+(?:°C|摄氏度)\s*.+锅", candidate, flags=re.I):
        return True
    if candidate in COOKING_TOOL_NAMES:
        return True
    for core in COOKING_TOOL_CORES:
        if candidate == core:
            return True
        if not candidate.endswith(core):
            continue
        modifier = candidate[: -len(core)].replace("的", "").strip()
        if modifier and TOOL_MODIFIER_PATTERN.fullmatch(modifier):
            return True
    if candidate.endswith(("容器", "模具", "盆")):
        return True
    if candidate.startswith("搅拌器") and "工具" in candidate:
        return True
    return False


def _is_cooking_tool(name: str) -> bool:
    raw = _plain_text(name)
    if "容量" in raw and "容器" in raw:
        return True
    candidate = _normalise_ingredient_name(name)
    if _is_single_cooking_tool(candidate):
        return True
    if candidate.endswith("锅") and "的" in candidate:
        return True
    parts = [part for part in TOOL_LIST_SEPARATOR.split(candidate) if part]
    if len(parts) < 2:
        return False
    tool_count = sum(_is_single_cooking_tool(part) for part in parts)
    return tool_count >= 2 and tool_count >= len(parts) - 1


def _is_non_ingredient_text(name: str) -> bool:
    candidate = _normalise_ingredient_name(name)
    return any(marker in candidate for marker in NON_INGREDIENT_TEXT_MARKERS)


def _extract_ingredients(sections: Iterable[tuple[str, str]]) -> list[tuple[str, str, str]]:
    raw_rows: list[tuple[str, str, str]] = []
    calculated_rows: list[tuple[str, str, str]] = []
    skipped = {"必须配料", "进阶配料", "可选配料", "调味料", "配料"}
    for title, body in sections:
        if "计算" in title:
            for item in _list_items(body):
                calculated = _extract_calculated_ingredient(item)
                if calculated is not None and not _is_cooking_tool(calculated[0]) and not _is_non_ingredient_text(calculated[0]):
                    calculated_rows.append(calculated)
            continue
        if not any(marker in title for marker in ("原料", "配料", "食材")):
            continue
        for item in _list_items(body):
            if item in skipped or _is_cooking_tool(item) or _is_non_ingredient_text(item):
                continue
            name, amount, unit = _extract_amount_and_unit(item)
            if name and not _is_cooking_tool(name) and not _is_non_ingredient_text(name):
                raw_rows.append((name, amount, unit))
    deduplicated: dict[str, tuple[str, str, str]] = {}
    for name, amount, unit in calculated_rows + raw_rows:
        current = deduplicated.get(name)
        if current is None or (not current[1] and amount):
            deduplicated[name] = (name, amount, unit)
    return [deduplicated[name] for name in sorted(deduplicated)]


def _extract_steps(sections: Iterable[tuple[str, str]]) -> list[str]:
    steps: list[str] = []
    for title, body in sections:
        if not any(marker in title for marker in ("操作", "做法", "步骤")):
            continue
        steps.extend(_list_items(body))
    return steps


def _difficulty(text: str) -> str:
    match = re.search(r"烹饪难度\s*[：:]\s*([★☆]+)", text)
    return str(match.group(1).count("★")) if match else ""


def _empty_node() -> dict[str, str]:
    return {field: "" for field in NODE_FIELDS}


def _build_rows(sources: Iterable[SourceFile]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    nodes: list[dict[str, str]] = []
    relationships: list[dict[str, str]] = []
    id_keys: dict[str, str] = {}
    ingredient_ids: dict[str, str] = {}

    def allocate(label: str, key: str) -> str:
        node_id = _stable_id(ID_PREFIXES[label], key)
        current = id_keys.get(node_id)
        if current is not None and current != key:
            raise RecipeBuildError(f"稳定 ID 哈希冲突: {node_id}")
        id_keys[node_id] = key
        return node_id

    for source in sources:
        text = _clean_markdown(source.content.decode("utf-8"))
        if not text:
            raise RecipeBuildError(f"菜谱 Markdown 不能为空: {source.logical_path}")
        title = _title_from_markdown(text, source.path.stem)
        sections = _h2_sections(text)
        ingredients = _extract_ingredients(sections)
        steps = _extract_steps(sections)
        if not ingredients:
            raise RecipeBuildError(f"未解析到必备原料、配料或食材: {source.logical_path}")
        if not steps:
            raise RecipeBuildError(f"未解析到操作步骤: {source.logical_path}")

        recipe_id = allocate("Recipe", f"recipe:{source.logical_path}")
        category = source.logical_path.split("/", 1)[0] if "/" in source.logical_path else ""
        recipe = _empty_node()
        recipe.update(
            {
                "nodeId": recipe_id,
                "labels": "Recipe",
                "name": title,
                "preferredTerm": title,
                "fsn": f"{title} (Recipe)",
                "conceptType": "Recipe",
                "category": category,
                "difficulty": _difficulty(text),
                "tags": ",".join(item for item in (title, category) if item),
                "filePath": source.logical_path,
                "description": _recipe_description(text),
            }
        )
        nodes.append(recipe)

        for ingredient_name, amount, unit in ingredients:
            ingredient_key = f"ingredient:{ingredient_name}"
            ingredient_id = ingredient_ids.get(ingredient_key)
            if ingredient_id is None:
                ingredient_id = allocate("Ingredient", ingredient_key)
                ingredient_ids[ingredient_key] = ingredient_id
                ingredient = _empty_node()
                ingredient.update(
                    {
                        "nodeId": ingredient_id,
                        "labels": "Ingredient",
                        "name": ingredient_name,
                        "preferredTerm": ingredient_name,
                        "fsn": f"{ingredient_name} (Ingredient)",
                        "conceptType": "Ingredient",
                    }
                )
                nodes.append(ingredient)
            relationships.append(
                {
                    "startNodeId": recipe_id,
                    "endNodeId": ingredient_id,
                    "relationshipType": REQUIRES_RELATIONSHIP,
                    "relationshipId": _stable_relation_id(REQUIRES_RELATIONSHIP, recipe_id, ingredient_id),
                    "amount": amount,
                    "unit": unit,
                    "step_order": "",
                }
            )

        for ordinal, step_text in enumerate(steps, start=1):
            step_id = allocate("CookingStep", f"step:{recipe_id}:{ordinal}")
            step = _empty_node()
            step.update(
                {
                    "nodeId": step_id,
                    "labels": "CookingStep",
                    "name": f"{title} 第{ordinal}步",
                    "preferredTerm": f"{title} 第{ordinal}步",
                    "fsn": f"{title} Step {ordinal}",
                    "conceptType": "CookingStep",
                    "description": step_text,
                    "stepNumber": str(ordinal),
                }
            )
            nodes.append(step)
            relationships.append(
                {
                    "startNodeId": recipe_id,
                    "endNodeId": step_id,
                    "relationshipType": CONTAINS_STEP_RELATIONSHIP,
                    "relationshipId": _stable_relation_id(CONTAINS_STEP_RELATIONSHIP, recipe_id, step_id),
                    "amount": "",
                    "unit": "",
                    "step_order": str(ordinal),
                }
            )

    return (
        sorted(nodes, key=lambda row: (row["labels"], row["nodeId"])),
        sorted(relationships, key=lambda row: (row["relationshipType"], row["startNodeId"], row["endNodeId"])),
    )


def _id_digest(values: Iterable[str]) -> str:
    return _sha256_bytes("\n".join(sorted(values)).encode("utf-8"))


def _write_csv(path: Path, fields: tuple[str, ...], rows: Iterable[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n", extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)


def build_artifact(
    *, sources: list[SourceFile], source_manifest_sha256: str | None, output: Path, dry_run: bool
) -> dict[str, Any]:
    nodes, relationships = _build_rows(sources)
    if len({row["nodeId"] for row in nodes}) != len(nodes):
        raise RecipeBuildError("生产器生成了重复 nodeId")
    if len({row["relationshipId"] for row in relationships}) != len(relationships):
        raise RecipeBuildError("生产器生成了重复 relationshipId")
    source_files = [{"path": item.logical_path, "sha256": item.sha256} for item in sources]
    manifest: dict[str, Any] = {
        "schema_version": BUILD_SCHEMA_VERSION,
        "producer_version": PRODUCER_VERSION,
        "source_manifest_sha256": source_manifest_sha256,
        "source_files": source_files,
        "node_count": len(nodes),
        "relationship_count": len(relationships),
        "node_counts": {label: sum(1 for row in nodes if row["labels"] == label) for label in sorted(ID_PREFIXES)},
        "relationship_counts": {
            "REQUIRES": sum(1 for row in relationships if row["relationshipType"] == REQUIRES_RELATIONSHIP),
            "CONTAINS_STEP": sum(1 for row in relationships if row["relationshipType"] == CONTAINS_STEP_RELATIONSHIP),
        },
        "stable_id_summary": {
            "algorithm": "sha256-prefix-decimal-v1",
            "node_ids_sha256": _id_digest(row["nodeId"] for row in nodes),
            "relationship_ids_sha256": _id_digest(row["relationshipId"] for row in relationships),
        },
        "pds_milvus_mapping": {"status": "unbound", "reason": "CSV build has not been imported into an isolated graph build"},
    }
    if dry_run:
        return {"valid": True, "dry_run": True, **manifest}
    if output.exists():
        raise RecipeBuildError(f"输出目录已存在，拒绝覆盖: {output}")
    if not output.parent.is_dir():
        raise RecipeBuildError(f"输出目录的父目录不存在: {output.parent}")

    staging = Path(tempfile.mkdtemp(prefix=f".{output.name}.", dir=output.parent))
    try:
        nodes_path = staging / "nodes.csv"
        relationships_path = staging / "relationships.csv"
        _write_csv(nodes_path, NODE_FIELDS, nodes)
        _write_csv(relationships_path, RELATIONSHIP_FIELDS, relationships)
        manifest["csv_sha256"] = {
            "nodes.csv": _sha256_file(nodes_path),
            "relationships.csv": _sha256_file(relationships_path),
        }
        manifest["manifest_sha256"] = _sha256_bytes(_canonical_json(manifest).encode("utf-8"))
        (staging / BUILD_MANIFEST_NAME).write_text(
            json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8"
        )
        os.replace(staging, output)
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise
    return {"valid": True, "dry_run": False, **manifest}


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="确定性生成 Recipe Markdown 图 CSV")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input-manifest")
    source.add_argument("--input-dir")
    parser.add_argument("--output", required=True)
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        sources, source_manifest_sha256 = load_sources(input_manifest=args.input_manifest, input_dir=args.input_dir)
        report = build_artifact(
            sources=sources,
            source_manifest_sha256=source_manifest_sha256,
            output=Path(args.output).resolve(),
            dry_run=args.dry_run,
        )
    except RecipeBuildError as error:
        print(json.dumps({"valid": False, "error": str(error)}, ensure_ascii=False, sort_keys=True))
        return 2
    summary = {
        "valid": report["valid"],
        "dry_run": report["dry_run"],
        "node_count": report["node_count"],
        "relationship_count": report["relationship_count"],
        "manifest_sha256": report.get("manifest_sha256"),
    }
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
