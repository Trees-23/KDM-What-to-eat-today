"""真实考试预检工具的静态契约测试。"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PREFLIGHT_PATH = PROJECT_ROOT / "_other/考试/工具/开考预检.py"
GENERATOR_PATH = PROJECT_ROOT / "_other/考试/工具/生成试卷.py"


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
