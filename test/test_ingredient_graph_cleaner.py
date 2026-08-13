import csv
from pathlib import Path

from scripts.clean_ingredient_nodes import clean_graph


NODE_FIELDS = ("nodeId", "labels", "name", "category", "amount", "unit", "isMain")
RELATIONSHIP_FIELDS = (
    "startNodeId",
    "endNodeId",
    "relationshipType",
    "relationshipId",
    "amount",
    "unit",
    "step_order",
)


def _write_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _build_fixture(directory: Path) -> None:
    _write_csv(
        directory / "nodes.csv",
        NODE_FIELDS,
        [
            {"nodeId": "recipe-1", "labels": "Recipe", "name": "示例菜", "category": "", "amount": "", "unit": "", "isMain": ""},
            {"nodeId": "ingredient-1", "labels": "Ingredient", "name": "鸡腿", "category": "蛋白质", "amount": "4", "unit": "个", "isMain": "True"},
            {"nodeId": "ingredient-2", "labels": "Ingredient", "name": "鸡腿", "category": "蛋白质", "amount": "400", "unit": "克", "isMain": "False"},
            {"nodeId": "ingredient-3", "labels": "Ingredient", "name": "大蒜", "category": "调料", "amount": "10", "unit": "克", "isMain": "False"},
            {"nodeId": "ingredient-4", "labels": "Ingredient", "name": "大蒜", "category": "蔬菜", "amount": "20", "unit": "克", "isMain": "False"},
        ],
    )
    _write_csv(
        directory / "relationships.csv",
        RELATIONSHIP_FIELDS,
        [
            {"startNodeId": "recipe-1", "endNodeId": "ingredient-1", "relationshipType": "801000001", "relationshipId": "requires-1", "amount": "4", "unit": "个", "step_order": ""},
            {"startNodeId": "recipe-1", "endNodeId": "ingredient-2", "relationshipType": "801000001", "relationshipId": "requires-2", "amount": "400", "unit": "克", "step_order": ""},
            {"startNodeId": "recipe-1", "endNodeId": "ingredient-3", "relationshipType": "801000001", "relationshipId": "requires-3", "amount": "10", "unit": "克", "step_order": ""},
            {"startNodeId": "recipe-1", "endNodeId": "ingredient-4", "relationshipType": "801000001", "relationshipId": "requires-4", "amount": "20", "unit": "克", "step_order": ""},
        ],
    )


def test_clean_graph_merges_exact_ingredients_and_keeps_context_on_relationships(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    _build_fixture(source)

    output = tmp_path / "cleaned"
    report = clean_graph(source, output)

    assert report == {
        "input_node_count": 5,
        "output_node_count": 3,
        "input_relationship_count": 4,
        "output_relationship_count": 4,
        "ingredient_duplicate_groups": 2,
        "ingredient_nodes_removed": 2,
        "ingredient_category_conflicts": 1,
        "relationship_endpoints_rewritten": 2,
    }
    nodes = _rows(output / "nodes.csv")
    assert {row["nodeId"] for row in nodes} == {"recipe-1", "ingredient-1", "ingredient-3"}
    chicken = next(row for row in nodes if row["nodeId"] == "ingredient-1")
    assert chicken["amount"] == chicken["unit"] == chicken["isMain"] == ""

    relationships = _rows(output / "relationships.csv")
    chicken_relationships = [row for row in relationships if row["endNodeId"] == "ingredient-1"]
    assert [(row["relationshipId"], row["amount"], row["unit"], row["ingredientCategory"], row["isMain"]) for row in chicken_relationships] == [
        ("requires-1", "4", "个", "蛋白质", "True"),
        ("requires-2", "400", "克", "蛋白质", "False"),
    ]
    garlic_relationships = [row for row in relationships if row["endNodeId"] == "ingredient-3"]
    assert [row["ingredientCategory"] for row in garlic_relationships] == ["调料", "蔬菜"]


def test_clean_graph_output_is_deterministic(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    _build_fixture(source)

    first = tmp_path / "first"
    second = tmp_path / "second"
    clean_graph(source, first)
    clean_graph(source, second)

    for name in ("nodes.csv", "relationships.csv", "ingredient_canonical_map.csv", "ingredient_cleaning_report.json"):
        assert (first / name).read_bytes() == (second / name).read_bytes()


def test_clean_graph_merges_governed_tomato_alias_and_rewrites_every_recipe_edge(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    _write_csv(
        source / "nodes.csv",
        NODE_FIELDS,
        [
            {"nodeId": "recipe-a", "labels": "Recipe", "name": "番茄汤", "category": "", "amount": "", "unit": "", "isMain": ""},
            {"nodeId": "recipe-b", "labels": "Recipe", "name": "西红柿炒蛋", "category": "", "amount": "", "unit": "", "isMain": ""},
            {"nodeId": "tomato", "labels": "Ingredient", "name": "番茄", "category": "蔬菜", "amount": "1", "unit": "个", "isMain": "True"},
            {"nodeId": "tomato-cn", "labels": "Ingredient", "name": "西红柿", "category": "蔬菜", "amount": "2", "unit": "个", "isMain": "True"},
        ],
    )
    _write_csv(
        source / "relationships.csv",
        RELATIONSHIP_FIELDS,
        [
            {"startNodeId": "recipe-a", "endNodeId": "tomato", "relationshipType": "801000001", "relationshipId": "requires-a", "amount": "1", "unit": "个", "step_order": ""},
            {"startNodeId": "recipe-b", "endNodeId": "tomato-cn", "relationshipType": "801000001", "relationshipId": "requires-b", "amount": "2", "unit": "个", "step_order": ""},
        ],
    )

    output = tmp_path / "cleaned"
    report = clean_graph(source, output)

    assert report["ingredient_nodes_removed"] == 1
    assert report["relationship_endpoints_rewritten"] == 1
    ingredients = [row for row in _rows(output / "nodes.csv") if row["labels"] == "Ingredient"]
    assert [(row["nodeId"], row["name"]) for row in ingredients] == [("tomato-cn", "西红柿")]
    assert {row["endNodeId"] for row in _rows(output / "relationships.csv")} == {"tomato-cn"}
    canonical_map = _rows(output / "ingredient_canonical_map.csv")
    assert ("tomato", "tomato-cn", "西红柿", "true") in {
        (row["originalNodeId"], row["canonicalNodeId"], row["name"], row["merged"])
        for row in canonical_map
    }
