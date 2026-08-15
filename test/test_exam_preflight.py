"""真实考试预检工具的静态契约测试。"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PREFLIGHT_PATH = PROJECT_ROOT / "_other/考试/检索重构真实场景考试包/工具/开考预检.py"
GENERATOR_PATH = PROJECT_ROOT / "_other/考试/检索重构真实场景考试包/工具/生成试卷.py"


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_preflight_static_targets_are_uniquely_resolvable():
    generator = _load(GENERATOR_PATH, "exam_bank_generator")
    preflight = _load(PREFLIGHT_PATH, "exam_preflight")
    questions = generator._build_questions()
    indexed = preflight._index_static_nodes(preflight._read_static_nodes())

    resolved = preflight._question_targets(questions, indexed)

    assert len(resolved) == 210
    assert all(node.node_id for node in resolved.values())


def test_preflight_normalizes_recipe_and_tip_source_paths():
    preflight = _load(PREFLIGHT_PATH, "exam_preflight_paths")

    assert preflight._normalize_source_path(r"dishes\aquatic\清蒸鲈鱼\清蒸鲈鱼.md") == "data/dishes/aquatic/清蒸鲈鱼/清蒸鲈鱼.md"
    assert preflight._normalize_source_path("tips/learn/学习蒸.md") == "data/tips/learn/学习蒸.md"


def test_new_path_probe_exercises_a_request_thread():
    preflight = _load(PREFLIGHT_PATH, "exam_preflight_threads")
    source = preflight._probe_new_path.__code__.co_consts

    assert any(isinstance(item, str) and "threading.Thread" in item for item in source)


def test_new_path_probe_explicitly_uses_only_read_only_new_path_components():
    preflight = _load(PREFLIGHT_PATH, "exam_preflight_probe_env")

    assert preflight._NEW_PATH_PROBE_ENV["RETRIEVAL_INTENT_PLANNER_ENABLED"] == "false"
    assert preflight._NEW_PATH_PROBE_ENV["RETRIEVAL_NEW_PATH_TRAFFIC_PERCENT"] == "100"
    assert preflight._NEW_PATH_PROBE_ENV["RETRIEVAL_PARENT_STORE_ENABLED"] == "true"
    assert preflight._NEW_PATH_PROBE_ENV["RETRIEVAL_TARGETED_GRAPH_ENABLED"] == "true"
    assert preflight._NEW_PATH_PROBE_ENV["RETRIEVAL_MILVUS_V2_ENABLED"] == "true"


def test_new_path_probe_uses_the_active_artifact_milvus_target():
    preflight = _load(PREFLIGHT_PATH, "exam_preflight_active_artifact")

    environment = preflight._new_path_probe_environment(
        {"manifest": {"milvus_database": "fixture", "milvus_collection": "cooking_knowledge_v2_pds_12345678"}}
    )

    assert environment["RETRIEVAL_MILVUS_DATABASE"] == "fixture"
    assert environment["RETRIEVAL_MILVUS_COLLECTION"] == "cooking_knowledge_v2_pds_12345678"


def test_preflight_delegates_active_pointer_path_resolution_to_pds():
    preflight = _load(PREFLIGHT_PATH, "exam_preflight_pds_pointer")
    source = PREFLIGHT_PATH.read_text(encoding="utf-8")

    assert "ParentDocumentStore.open(active_pointer.parent, active_pointer=active_pointer)" in source
    assert 'Path(pointer["store_path"])' not in source
