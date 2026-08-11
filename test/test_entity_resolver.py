from __future__ import annotations

from contextlib import contextmanager

import pytest

from rag_modules.entity_resolver import EntityResolver


class FakeSession:
    def __init__(self, responses):
        self.responses = responses
        self.calls = []

    def run(self, query, parameters):
        self.calls.append((query, parameters))
        if "entity_exact_name_v1" in query:
            return self.responses.get("exact", [])
        if "entity_alias_v1" in query:
            return self.responses.get("alias", [])
        if "entity_fulltext_v1" in query:
            return self.responses.get("fulltext", [])
        raise AssertionError("解析器执行了未知查询模板")


class FakeDriver:
    def __init__(self, responses):
        self.session_instance = FakeSession(responses)
        self.databases = []

    @contextmanager
    def session(self, database=None):
        self.databases.append(database)
        yield self.session_instance


def test_exact_name_stops_before_alias_or_fulltext_and_has_no_vector_dependency():
    driver = FakeDriver(
        {
            "exact": [
                {"node_id": "201002454", "display_name": "宫保鸡丁"},
            ],
            "alias": [{"node_id": "wrong", "display_name": "不应调用"}],
        }
    )
    resolver = EntityResolver(driver, database="neo4j")

    candidates = resolver.resolve("宫保鸡丁怎么做？", expected_types=("Recipe",))

    assert [(candidate.node_id, candidate.match_kind) for candidate in candidates] == [
        ("201002454", "exact_name"),
    ]
    assert len(driver.session_instance.calls) == 1
    assert "Recipe" in driver.session_instance.calls[0][0]
    assert driver.session_instance.calls[0][1]["query_text"] == "宫保鸡丁怎么做"


def test_governed_alias_precedes_fulltext_and_tied_candidates_are_ambiguous():
    driver = FakeDriver(
        {
            "exact": [],
            "alias": [
                {"node_id": "recipe-a", "display_name": "菜A"},
                {"node_id": "recipe-b", "display_name": "菜B"},
            ],
            "fulltext": [{"node_id": "wrong", "display_name": "不应调用", "score": 4.0}],
        }
    )
    resolver = EntityResolver(driver)

    candidates = resolver.resolve("家常别名", expected_types=("Recipe",))

    assert [candidate.match_kind for candidate in candidates] == ["governed_alias", "governed_alias"]
    assert all(candidate.ambiguity for candidate in candidates)
    assert len(driver.session_instance.calls) == 2


def test_exact_name_keeps_all_parallel_ingredient_candidates_within_the_governed_limit():
    rows = [
        {"node_id": f"ingredient-{index}", "display_name": "牛肉"}
        for index in range(8)
    ]
    resolver = EntityResolver(FakeDriver({"exact": rows}))

    candidates = resolver.resolve("牛肉适合搭配什么蔬菜", expected_types=("Ingredient",))

    assert len(candidates) == 8
    assert all(candidate.ambiguity for candidate in candidates)


def test_fulltext_is_the_last_fixed_fallback_and_score_tie_is_not_silently_selected():
    driver = FakeDriver(
        {
            "exact": [],
            "alias": [],
            "fulltext": [
                {"node_id": "tech-a", "display_name": "腌肉", "score": 8.0},
                {"node_id": "tech-b", "display_name": "腌（肉）", "score": 8.0},
            ],
        }
    )
    resolver = EntityResolver(driver)

    candidates = resolver.resolve("腌肉关键要点", expected_types=("TechniqueDoc",))

    assert len(driver.session_instance.calls) == 3
    assert [candidate.node_type for candidate in candidates] == ["TechniqueDoc", "TechniqueDoc"]
    assert all(candidate.ambiguity for candidate in candidates)


def test_fulltext_candidate_must_have_a_name_verifiably_present_in_query():
    driver = FakeDriver(
        {
            "exact": [],
            "alias": [],
            "fulltext": [{"node_id": "unrelated", "display_name": "无关菜名", "score": 99.0}],
        }
    )
    resolver = EntityResolver(driver)

    assert resolver.resolve("阶段二不存在的实体", expected_types=("Recipe",)) == []


def test_resolver_rejects_unknown_entity_type_before_querying():
    driver = FakeDriver({})
    resolver = EntityResolver(driver)

    with pytest.raises(ValueError, match="expected_types"):
        resolver.resolve("宫保鸡丁", expected_types=("Recipe", "AnyLabel"))

    assert driver.session_instance.calls == []
