"""检索考试题库的图路径契约测试。"""

from __future__ import annotations

import csv
import importlib.util
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = PROJECT_ROOT / "_other/考试/工具/生成试卷.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("exam_bank_generator", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("无法加载考试题库生成器")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ExamBankGenerationTest(unittest.TestCase):
    def test_s05_contracts_match_graph_data(self) -> None:
        generator = load_generator()
        questions = generator._build_questions()
        generator._validate_static_sources(questions)
        generator._validate_graph_targets(questions)

        s05 = [question for question in questions if question["scenario_id"] == "S05"]
        positive = [question for question in s05 if question["difficulty_code"] in {"A", "B"}]
        negative = [question for question in s05 if question["difficulty_code"] == "C"]

        self.assertEqual(len(positive), 20)
        self.assertEqual(len(negative), 10)
        self.assertTrue(all(question["contract"]["evaluation_mode"] == "ranking" for question in positive))
        self.assertTrue(all(question["contract"]["gold_target"]["minimum_verified_graph_paths"] == 1 for question in positive))
        self.assertTrue(all(question["contract"]["evaluation_mode"] == "safety" for question in negative))
        self.assertTrue(all(question["contract"]["gold_target"]["expected_verified_graph_paths"] == 0 for question in negative))

    def test_s03_targets_share_the_technique_import_source(self) -> None:
        generator = load_generator()
        with generator.TIPS_NODES_PATH.open(encoding="utf-8", newline="") as stream:
            rows = [row for row in csv.DictReader(stream) if row["labels"] == "TechniqueDoc"]
        docs = {(row["name"], f"data/{row['sourcePath']}") for row in rows}

        self.assertEqual(len(generator.TECHNIQUE_TARGETS), 30)
        self.assertTrue(all((target["name"], target["source_path"]) in docs for target in generator.TECHNIQUE_TARGETS))


if __name__ == "__main__":
    unittest.main()
