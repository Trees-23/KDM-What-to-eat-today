from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

from scripts import build_recipe_graph_csv, validate_recipe_graph_csv


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def _write_source_manifest(tmp_path: Path) -> Path:
    dishes = tmp_path / "dishes"
    meat = dishes / "meat"
    vegetable = dishes / "vegetable"
    meat.mkdir(parents=True)
    vegetable.mkdir(parents=True)
    (meat / "菜A.md").write_text(
        """# 菜A的做法

带有\"引号\"、逗号的说明。

## 必备原料和工具

- 鸡肉 200g
- 大葱（可选）

## 操作

- 鸡肉切块备用
- 加入\"酱汁\"，翻炒均匀
""",
        encoding="utf-8",
    )
    (vegetable / "菜B.md").write_text(
        """# 菜B的做法

## 必备原料和工具

- 豆腐 1块

## 操作

1. 豆腐切块
2. 小火煎至两面金黄
""",
        encoding="utf-8",
    )
    manifest = tmp_path / "sources.json"
    manifest.write_text(
        json.dumps(
            {
                "schema_version": "recipe-source-manifest-v1",
                "source_root": "dishes",
                "files": [
                    {"path": "vegetable/菜B.md"},
                    {"path": "meat/菜A.md"},
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return manifest


def _rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _refresh_manifest_hash(output: Path) -> None:
    relationships_path = output / "relationships.csv"
    build_manifest_path = output / "recipe-build-manifest.json"
    build_manifest = json.loads(build_manifest_path.read_text(encoding="utf-8"))
    build_manifest["csv_sha256"]["relationships.csv"] = hashlib.sha256(relationships_path.read_bytes()).hexdigest()
    build_manifest.pop("manifest_sha256")
    build_manifest["manifest_sha256"] = hashlib.sha256(
        build_recipe_graph_csv._canonical_json(build_manifest).encode("utf-8")
    ).hexdigest()
    build_manifest_path.write_text(json.dumps(build_manifest, ensure_ascii=False), encoding="utf-8")


def test_manifest_input_builds_repeatable_csv_and_passes_strict_validation(tmp_path: Path):
    manifest = _write_source_manifest(tmp_path)
    first = tmp_path / "first"
    second = tmp_path / "second"

    assert build_recipe_graph_csv.main(["--input-manifest", str(manifest), "--output", str(first)]) == 0
    assert build_recipe_graph_csv.main(["--input-manifest", str(manifest), "--output", str(second)]) == 0
    assert validate_recipe_graph_csv.main(["--input", str(first), "--strict"]) == 0

    for name in ("nodes.csv", "relationships.csv", "recipe-build-manifest.json"):
        assert (first / name).read_bytes() == (second / name).read_bytes()

    build_manifest = json.loads((first / "recipe-build-manifest.json").read_text(encoding="utf-8"))
    assert build_manifest["schema_version"] == "recipe-build-manifest-v1"
    assert build_manifest["producer_version"] == "recipe_graph_csv_producer_v1"
    assert [item["path"] for item in build_manifest["source_files"]] == ["meat/菜A.md", "vegetable/菜B.md"]
    assert all(len(item["sha256"]) == 64 for item in build_manifest["source_files"])
    assert build_manifest["manifest_sha256"]
    assert build_manifest["csv_sha256"]["nodes.csv"] == hashlib.sha256((first / "nodes.csv").read_bytes()).hexdigest()

    nodes = _rows(first / "nodes.csv")
    relationships = _rows(first / "relationships.csv")
    labels_by_id = {row["nodeId"]: row["labels"] for row in nodes}
    assert {row["labels"] for row in nodes} == {"Recipe", "Ingredient", "CookingStep"}
    assert any('"酱汁"' in row["description"] for row in nodes)
    assert '""' in (first / "nodes.csv").read_text(encoding="utf-8")
    assert all(labels_by_id[row["startNodeId"]] == "Recipe" for row in relationships)
    assert all(
        labels_by_id[row["endNodeId"]] == ("Ingredient" if row["relationshipType"] == "801000001" else "CookingStep")
        for row in relationships
    )


def test_manifest_input_rejects_source_hash_mismatch(tmp_path: Path):
    manifest = _write_source_manifest(tmp_path)
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    payload["files"][0]["sha256"] = "0" * 64
    manifest.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

    assert build_recipe_graph_csv.main(["--input-manifest", str(manifest), "--output", str(tmp_path / "output")]) == 2
    assert not (tmp_path / "output").exists()


def test_directory_input_and_dry_run_are_explicit_and_non_writing(tmp_path: Path):
    manifest = _write_source_manifest(tmp_path)
    source_directory = tmp_path / "dishes"
    output = tmp_path / "output"
    dry_output = tmp_path / "dry-output"

    assert build_recipe_graph_csv.main(["--input-dir", str(source_directory), "--output", str(output)]) == 0
    assert build_recipe_graph_csv.main(["--input-manifest", str(manifest), "--output", str(dry_output), "--dry-run"]) == 0
    assert (output / "nodes.csv").is_file()
    assert not dry_output.exists()


def test_calculation_section_supplies_amounts_and_excludes_cooking_tools(tmp_path: Path):
    dishes = tmp_path / "dishes"
    dishes.mkdir()
    recipe = dishes / "示例.md"
    recipe.write_text(
        """# 示例的做法

## 必备原料和工具

- 鱼肉
- 蒜瓣
- 盐
- 量杯
- 厨房秤（可选）
- 大不锈钢碗

## 计算

- 鱼肉 500g
- 大蒜 2 瓣
- 盐 5g
- 豆豉 10g（可选）
- 量杯 1个

## 操作

- 准备食材
- 下锅煮熟
""",
        encoding="utf-8",
    )
    output = tmp_path / "output"
    assert build_recipe_graph_csv.main(["--input-dir", str(dishes), "--output", str(output)]) == 0

    nodes = _rows(output / "nodes.csv")
    labels_by_id = {row["nodeId"]: row["labels"] for row in nodes}
    name_by_id = {row["nodeId"]: row["name"] for row in nodes}
    ingredient_names = {row["name"] for row in nodes if row["labels"] == "Ingredient"}
    assert {"鱼肉", "大蒜", "盐", "豆豉"}.issubset(ingredient_names)
    assert not {"量杯", "厨房秤", "大不锈钢碗", "蒜瓣"} & ingredient_names
    amounts = {
        name_by_id[row["endNodeId"]]: (row["amount"], row["unit"])
        for row in _rows(output / "relationships.csv")
        if row["relationshipType"] == "801000001" and labels_by_id[row["endNodeId"]] == "Ingredient"
    }
    assert amounts["鱼肉"] == ("500", "g")
    assert amounts["大蒜"] == ("2", "瓣")
    assert amounts["盐"] == ("5", "g")


def test_ingredient_extraction_excludes_described_tools_and_formulae(tmp_path: Path):
    dishes = tmp_path / "dishes"
    dishes.mkdir()
    (dishes / "示例.md").write_text(
        """# 示例的做法

## 必备原料和工具

- 鸡肉
- 八角
- 火锅底料
- 平底煎锅
- 烤箱 大小不限
- 蒸笼
- 小碗若干
- 筛网（可选）
- 厨房用夹

## 计算

- 鸡肉 500g
- 八角 = 5g
- 冷藏时间 Tc = 生米体积 / 10 ml
- 腌制温度 = 20 摄氏度
- 配方 = 鸡肉 * 0.1 = 50g
- 鸡蛋的用量为 1 个
- 油量 = 50 克 * 份数
- 面类材料：单人一个方便面大小的量，可以在 70g

## 操作

- 准备食材
- 完成烹饪
""",
        encoding="utf-8",
    )
    output = tmp_path / "output"

    assert build_recipe_graph_csv.main(["--input-dir", str(dishes), "--output", str(output)]) == 0

    ingredient_names = {row["name"] for row in _rows(output / "nodes.csv") if row["labels"] == "Ingredient"}
    assert {"鸡肉", "八角", "火锅底料"}.issubset(ingredient_names)
    assert not {
        "平底煎锅", "烤箱 大小不限", "蒸笼", "小碗若干", "筛网", "厨房用夹",
        "冷藏时间 Tc = 生米体积 /", "腌制温度 =", "配方 = 鸡肉 * 0.1 =", "鸡蛋的用量为", "油量",
        "面类材料：单人一个方便面大小的量，可以在",
    } & ingredient_names


def test_cooking_tool_recognition_handles_descriptions_and_preserves_food_names():
    tools = {
        "1 个小碗", "32 厘米以上的炒锅一个", "不粘平底锅", "平底锅 或 微波炉",
        "筛网 网孔约为", "需要烤箱", "一次性透明塑料杯", "大号的玻璃杯",
        "油 + 锅 + 菜刀 + 铲子", "厚底煮锅+严丝合缝的锅盖", "电饭煲/电炖锅",
        "可选：空气炸锅烤架", "洗菜盆、直径 18cm 的小锅", "调酒杯", "100°C 沸水锅",
        "瓦罐或者高压锅", "砵或者有一定深度的碗", "硅油纸或模具", "能放进微波炉的容器",
        "蒸锅或电蒸炉", "锡纸盘", "调理机/果汁机", "餐刀", "高球杯",
        "放得下玉米的锅", "厨房用温度计", "一个容量在 600 毫升以上的容器",
        "[可选] 分蛋器", "冰淇淋模具", "手动压汁器", "可密封容器", "吧勺",
        "深一点的小铁盆", "漏勺", "蒸架", "量酒器", "金属蛋糕模具",
        "筷子一双", "筷子或牙签", "一次性手套", "一次性塑料手套", "刷子", "擀面杖",
        "蒸箱", "面包机", "轻食机", "搅拌机", "料理搅拌机", "榨汁机", "隔热手套", "煲汤盅，按",
        "冰箱", "打火机", "捣药罐",
        "粉碎机", "过滤豆浆渣的纱布一块", "短吸管", "消毒纱布", "小斧头", "密封袋", "港式奶茶过滤袋",
    }
    foods = {"火锅底料", "火锅牛肉卷", "麻辣香锅调料", "北京二锅头酒", "蒸锅用水"}

    assert all(build_recipe_graph_csv._is_cooking_tool(name) for name in tools)
    assert not any(build_recipe_graph_csv._is_cooking_tool(name) for name in foods)


def test_real_recipe_sources_exclude_tools_and_calculation_formulae():
    def ingredient_names(relative_path: str) -> set[str]:
        text = (REPOSITORY_ROOT / relative_path).read_text(encoding="utf-8")
        return {
            name
            for name, _amount, _unit in build_recipe_graph_csv._extract_ingredients(
                build_recipe_graph_csv._h2_sections(build_recipe_graph_csv._clean_markdown(text))
            )
        }

    shrimp = ingredient_names("data/dishes/aquatic/蒜香黄油虾/蒜香黄油虾.md")
    egg_tart = ingredient_names("data/dishes/dessert/烤蛋挞/烤蛋挞.md")
    crayfish = ingredient_names("data/dishes/aquatic/小龙虾/小龙虾.md")
    porridge = ingredient_names("data/dishes/soup/米粥.md")
    ribs = ingredient_names("data/dishes/meat_dish/土豆炖排骨/土豆炖排骨.md")

    assert {"大虾", "大蒜", "无盐黄油"}.issubset(shrimp)
    assert not {"平底煎锅", "厨房用夹"} & shrimp
    assert {"鸡蛋", "牛奶", "淡奶油", "白砂糖"}.issubset(egg_tart)
    assert not {"烤箱 大小不限", "克数称", "搅拌器 包含且不限于筷子 打蛋器等工具", "筛网 网孔约为"} & egg_tart
    assert {"小龙虾", "油", "桂皮", "八角"}.issubset(crayfish)
    assert porridge == {"米", "水", "植物油"}
    assert "八角" in ribs

    tool_only_sources = {
        "data/dishes/staple/螺蛳粉.md": "筷子一双",
        "data/dishes/breakfast/太阳蛋.md": "筷子或牙签",
        "data/dishes/aquatic/葱油桂鱼/葱油桂鱼.md": "一次性手套",
        "data/dishes/dessert/雪花酥/雪花酥.md": "擀面杖",
        "data/dishes/vegetable_dish/鸡蛋羹/蒸箱鸡蛋羹.md": "蒸箱",
        "data/dishes/breakfast/吐司果酱.md": "面包机",
        "data/dishes/breakfast/金枪鱼酱三明治.md": "轻食机",
        "data/dishes/drink/奇异果菠菜特调/奇异果菠菜特调.md": "榨汁机",
        "data/dishes/vegetable_dish/糖拌西红柿/糖拌西红柿.md": "冰箱",
        "data/dishes/aquatic/清蒸生蚝.md": "刷子",
        "data/dishes/drink/B52轰炸机.md": "打火机",
        "data/dishes/meat_dish/孜然牛肉.md": "捣药罐",
        "data/dishes/semi-finished/牛油火锅底料.md": "粉碎机",
        "data/dishes/drink/冰粉/冰粉.md": "过滤豆浆渣的纱布一块",
        "data/dishes/meat_dish/带把肘子.md": "小斧头",
        "data/dishes/aquatic/微波葱姜黑鳕鱼.md": "密封袋",
        "data/dishes/drink/泰国手标红茶/泰国手标红茶.md": "港式奶茶过滤袋",
    }
    for relative_path, tool_name in tool_only_sources.items():
        assert tool_name not in ingredient_names(relative_path)

    sunny_side_up = ingredient_names("data/dishes/breakfast/太阳蛋.md")
    cucumber_pork = ingredient_names("data/dishes/meat_dish/黄瓜炒肉.md")
    noodles = ingredient_names("data/dishes/staple/汤面.md")
    lamb_ribs = ingredient_names("data/dishes/meat_dish/萝卜炖羊排.md")
    assert not {"鸡蛋的用量为", "盐的用量为", "油的用量为"} & sunny_side_up
    assert not {"油量", "盐量"} & cucumber_pork
    assert not {"面类材料：单人一个方便面大小的量，可以在", "冷水： 加入能浸没面的量，一般在"} & noodles
    assert "水：没过食材的量，需要" not in lamb_ribs


def test_manifest_sha_is_bound_to_the_same_bytes_used_for_parsing(tmp_path: Path, monkeypatch):
    manifest = _write_source_manifest(tmp_path)
    original_manifest_bytes = manifest.read_bytes()
    original_load_source_file = build_recipe_graph_csv._load_source_file

    def mutate_manifest_after_first_source(*args, **kwargs):
        source = original_load_source_file(*args, **kwargs)
        manifest.write_text(
            json.dumps(
                {
                    "schema_version": "recipe-source-manifest-v1",
                    "source_root": "dishes",
                    "files": [{"path": "meat/菜A.md"}],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        return source

    monkeypatch.setattr(build_recipe_graph_csv, "_load_source_file", mutate_manifest_after_first_source)
    sources, manifest_sha256 = build_recipe_graph_csv.load_sources(input_manifest=str(manifest), input_dir=None)

    assert [source.logical_path for source in sources] == ["meat/菜A.md", "vegetable/菜B.md"]
    assert manifest_sha256 == hashlib.sha256(original_manifest_bytes).hexdigest()


def test_build_uses_the_bytes_that_were_hashed_when_sources_were_loaded(tmp_path: Path):
    manifest = _write_source_manifest(tmp_path)
    sources, source_manifest_sha256 = build_recipe_graph_csv.load_sources(
        input_manifest=str(manifest), input_dir=None
    )
    source = next(item for item in sources if item.logical_path == "meat/菜A.md")
    source.path.write_text("# 已被替换的做法\n", encoding="utf-8")
    output = tmp_path / "output"

    report = build_recipe_graph_csv.build_artifact(
        sources=sources,
        source_manifest_sha256=source_manifest_sha256,
        output=output,
        dry_run=False,
    )

    assert report["valid"]
    recipe_names = {row["name"] for row in _rows(output / "nodes.csv") if row["labels"] == "Recipe"}
    assert "菜A" in recipe_names
    assert "已被替换" not in recipe_names


def test_validator_rejects_bad_relationship_direction(tmp_path: Path, capsys):
    manifest = _write_source_manifest(tmp_path)
    output = tmp_path / "output"
    assert build_recipe_graph_csv.main(["--input-manifest", str(manifest), "--output", str(output)]) == 0

    relationships_path = output / "relationships.csv"
    rows = _rows(relationships_path)
    requires = next(row for row in rows if row["relationshipType"] == "801000001")
    requires["startNodeId"], requires["endNodeId"] = requires["endNodeId"], requires["startNodeId"]
    with relationships_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    _refresh_manifest_hash(output)

    assert validate_recipe_graph_csv.main(["--input", str(output), "--strict"]) == 2
    report = json.loads(capsys.readouterr().out.splitlines()[-1])
    assert any("REQUIRES 方向无效" in error for error in report["errors"])


def test_validator_rejects_missing_foreign_key_and_non_contiguous_step_order(tmp_path: Path, capsys):
    manifest = _write_source_manifest(tmp_path)
    output = tmp_path / "output"
    assert build_recipe_graph_csv.main(["--input-manifest", str(manifest), "--output", str(output)]) == 0

    relationships_path = output / "relationships.csv"
    rows = _rows(relationships_path)
    next(row for row in rows if row["relationshipType"] == "801000001")["endNodeId"] = "999999999999999999"
    step = next(row for row in rows if row["relationshipType"] == "801000003" and row["step_order"] == "2")
    step["step_order"] = "9"
    with relationships_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    _refresh_manifest_hash(output)

    assert validate_recipe_graph_csv.main(["--input", str(output), "--strict"]) == 2
    report = json.loads(capsys.readouterr().out.splitlines()[-1])
    assert any("关系外键不存在" in error for error in report["errors"])
    assert any("Recipe 步骤顺序不连续" in error for error in report["errors"])


def test_validator_enforces_every_manifest_schema_constraint(tmp_path: Path, capsys):
    manifest = _write_source_manifest(tmp_path)
    output = tmp_path / "output"
    assert build_recipe_graph_csv.main(["--input-manifest", str(manifest), "--output", str(output)]) == 0

    build_manifest_path = output / "recipe-build-manifest.json"
    build_manifest = json.loads(build_manifest_path.read_text(encoding="utf-8"))
    build_manifest["source_manifest_sha256"] = "not-a-sha256"
    build_manifest["stable_id_summary"]["algorithm"] = "unverified"
    del build_manifest["pds_milvus_mapping"]["reason"]
    build_manifest.pop("manifest_sha256")
    build_manifest["manifest_sha256"] = hashlib.sha256(
        build_recipe_graph_csv._canonical_json(build_manifest).encode("utf-8")
    ).hexdigest()
    build_manifest_path.write_text(json.dumps(build_manifest, ensure_ascii=False), encoding="utf-8")

    assert validate_recipe_graph_csv.main(["--input", str(output), "--strict"]) == 2
    report = json.loads(capsys.readouterr().out.splitlines()[-1])
    assert any("source_manifest_sha256" in error for error in report["errors"])
    assert any("stable_id_summary" in error for error in report["errors"])
    assert any("pds_milvus_mapping" in error for error in report["errors"])
