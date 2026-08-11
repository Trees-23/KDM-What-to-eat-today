#!/usr/bin/env python3
"""生成固定的 300 题真实场景检索考试题库。"""

from __future__ import annotations

import hashlib
import json
import csv
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Callable


EXAM_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = EXAM_ROOT.parents[1]
BANK_PATH = EXAM_ROOT / "试卷题库.json"
CATALOG_PATH = EXAM_ROOT / "试卷目录.md"
VALIDATION_PATH = EXAM_ROOT / "题库校验报告.md"
NODES_PATH = PROJECT_ROOT / "data/cypher/nodes.csv"
RELATIONSHIPS_PATH = PROJECT_ROOT / "data/cypher/relationships.csv"


def recipe(name: str, source_path: str) -> dict[str, str]:
    return {"name": name, "source_path": source_path}


RECIPE_FULL_TARGETS = [
    recipe("清蒸鲈鱼", "data/dishes/aquatic/清蒸鲈鱼/清蒸鲈鱼.md"),
    recipe("油焖大虾", "data/dishes/aquatic/油焖大虾/油焖大虾.md"),
    recipe("水煮鱼", "data/dishes/aquatic/水煮鱼.md"),
    recipe("糖醋鲤鱼", "data/dishes/aquatic/糖醋鲤鱼/糖醋鲤鱼.md"),
    recipe("鳊鱼炖豆腐", "data/dishes/aquatic/鳊鱼炖豆腐/鳊鱼炖豆腐.md"),
    recipe("蒜蓉虾", "data/dishes/aquatic/蒜蓉虾/蒜蓉虾.md"),
    recipe("白灼虾", "data/dishes/aquatic/白灼虾/白灼虾.md"),
    recipe("葱烧海参", "data/dishes/aquatic/葱烧海参/葱烧海参.md"),
    recipe("微波葱姜黑鳕鱼", "data/dishes/aquatic/微波葱姜黑鳕鱼.md"),
    recipe("红烧鱼头", "data/dishes/aquatic/红烧鱼头.md"),
    recipe("西红柿炒鸡蛋", "data/dishes/vegetable_dish/西红柿炒鸡蛋.md"),
    recipe("地三鲜", "data/dishes/vegetable_dish/地三鲜.md"),
    recipe("蒜蓉西兰花", "data/dishes/vegetable_dish/蒜蓉西兰花.md"),
    recipe("酸辣土豆丝", "data/dishes/vegetable_dish/酸辣土豆丝.md"),
    recipe("蚝油生菜", "data/dishes/vegetable_dish/蚝油生菜.md"),
    recipe("红烧茄子", "data/dishes/vegetable_dish/红烧茄子.md"),
    recipe("干锅花菜", "data/dishes/vegetable_dish/干锅花菜/干锅花菜.md"),
    recipe("凉拌黄瓜", "data/dishes/vegetable_dish/凉拌黄瓜.md"),
    recipe("扬州炒饭", "data/dishes/staple/扬州炒饭/扬州炒饭.md"),
    recipe("日式肥牛丼饭", "data/dishes/staple/日式肥牛丼饭/日式肥牛丼饭.md"),
    recipe("手工水饺", "data/dishes/staple/手工水饺.md"),
    recipe("炸酱面", "data/dishes/staple/炸酱面.md"),
    recipe("牛奶燕麦", "data/dishes/breakfast/牛奶燕麦.md"),
    recipe("鸡蛋三明治", "data/dishes/breakfast/鸡蛋三明治.md"),
    recipe("西红柿鸡蛋汤", "data/dishes/soup/西红柿鸡蛋汤.md"),
    recipe("玉米排骨汤", "data/dishes/soup/玉米排骨汤/玉米排骨汤.md"),
    recipe("提拉米苏", "data/dishes/dessert/提拉米苏/提拉米苏.md"),
    recipe("杨枝甘露", "data/dishes/drink/杨枝甘露.md"),
    recipe("麻婆豆腐", "data/dishes/meat_dish/麻婆豆腐/麻婆豆腐.md"),
    recipe("西红柿土豆炖牛肉", "data/dishes/meat_dish/西红柿土豆炖牛肉/西红柿土豆炖牛肉.md"),
]

RECIPE_STEP_TARGETS = [
    recipe("回锅肉", "data/dishes/meat_dish/回锅肉/回锅肉.md"),
    recipe("清蒸鳜鱼", "data/dishes/meat_dish/清蒸鳜鱼/清蒸鳜鱼.md"),
    recipe("水煮牛肉", "data/dishes/meat_dish/水煮牛肉/水煮牛肉.md"),
    recipe("糖醋排骨", "data/dishes/meat_dish/糖醋排骨/糖醋排骨.md"),
    recipe("啤酒鸭", "data/dishes/meat_dish/啤酒鸭/啤酒鸭.md"),
    recipe("酱牛肉", "data/dishes/meat_dish/酱牛肉/酱牛肉.md"),
    recipe("羊排焖面", "data/dishes/meat_dish/羊排焖面/羊排焖面.md"),
    recipe("小炒黄牛肉", "data/dishes/meat_dish/小炒黄牛肉/小炒黄牛肉.md"),
    recipe("咖喱炒蟹", "data/dishes/aquatic/咖喱炒蟹.md"),
    recipe("芥末黄油罗氏虾", "data/dishes/aquatic/芥末黄油罗氏虾/芥末黄油罗氏虾.md"),
    recipe("鱼香肉丝", "data/dishes/meat_dish/鱼香肉丝.md"),
    recipe("宫保鸡丁", "data/dishes/meat_dish/宫保鸡丁/宫保鸡丁.md"),
    recipe("粉蒸肉", "data/dishes/meat_dish/粉蒸肉.md"),
    recipe("辣椒炒肉", "data/dishes/meat_dish/辣椒炒肉.md"),
    recipe("水煮肉片", "data/dishes/meat_dish/水煮肉片.md"),
    recipe("牛排", "data/dishes/meat_dish/牛排/牛排.md"),
    recipe("清蒸鲈鱼", "data/dishes/aquatic/清蒸鲈鱼/清蒸鲈鱼.md"),
    recipe("小龙虾", "data/dishes/aquatic/小龙虾/小龙虾.md"),
    recipe("红烧鲤鱼", "data/dishes/aquatic/红烧鲤鱼.md"),
    recipe("豆角焖面", "data/dishes/staple/豆角焖面/豆角焖面.md"),
    recipe("蛋包饭", "data/dishes/staple/蛋包饭.md"),
    recipe("电饭煲三文鱼炊饭", "data/dishes/staple/电饭煲三文鱼炊饭/电饭煲三文鱼炊饭.md"),
    recipe("西葫芦炒鸡蛋", "data/dishes/vegetable_dish/西葫芦炒鸡蛋/西葫芦炒鸡蛋.md"),
    recipe("清蒸南瓜", "data/dishes/vegetable_dish/清蒸南瓜.md"),
    recipe("上汤娃娃菜", "data/dishes/vegetable_dish/上汤娃娃菜/上汤娃娃菜.md"),
    recipe("凉拌金针菇", "data/dishes/vegetable_dish/凉拌金针菇.md"),
    recipe("陈皮排骨汤", "data/dishes/soup/陈皮排骨汤.md"),
    recipe("罗宋汤", "data/dishes/soup/罗宋汤.md"),
    recipe("烤蛋挞", "data/dishes/dessert/烤蛋挞/烤蛋挞.md"),
    recipe("戚风蛋糕", "data/dishes/dessert/戚风蛋糕/戚风蛋糕.md"),
]

TECHNIQUE_TARGETS = [
    recipe("如何选择现在吃什么", "data/tips/如何选择现在吃什么.md"),
    recipe("高级专业术语", "data/tips/advanced/高级专业术语.md"),
    recipe("辅料技巧", "data/tips/advanced/辅料技巧.md"),
    recipe("油温判断技巧", "data/tips/advanced/油温判断技巧.md"),
    recipe("糖色的炒制", "data/tips/advanced/糖色的炒制.md"),
    recipe("厨房准备", "data/tips/厨房准备.md"),
    recipe("高压力锅", "data/tips/learn/高压力锅.md"),
    recipe("学习炒与煎", "data/tips/learn/学习炒与煎.md"),
    recipe("微波炉", "data/tips/learn/微波炉.md"),
    recipe("学习蒸", "data/tips/learn/学习蒸.md"),
    recipe("学习凉拌", "data/tips/learn/学习凉拌.md"),
    recipe("学习焯水", "data/tips/learn/学习焯水.md"),
    recipe("去腥", "data/tips/learn/去腥.md"),
    recipe("空气炸锅", "data/tips/learn/空气炸锅.md"),
    recipe("学习煮", "data/tips/learn/学习煮.md"),
    recipe("学习腌", "data/tips/learn/学习腌.md"),
    recipe("食品安全", "data/tips/learn/食品安全.md"),
    recipe("食材相克与禁忌", "data/tips/食材相克与禁忌.md"),
    recipe("油温判断技巧", "data/tips/advanced/油温判断技巧.md"),
    recipe("糖色的炒制", "data/tips/advanced/糖色的炒制.md"),
    recipe("去腥", "data/tips/learn/去腥.md"),
    recipe("学习腌", "data/tips/learn/学习腌.md"),
    recipe("学习焯水", "data/tips/learn/学习焯水.md"),
    recipe("学习蒸", "data/tips/learn/学习蒸.md"),
    recipe("学习炒与煎", "data/tips/learn/学习炒与煎.md"),
    recipe("空气炸锅", "data/tips/learn/空气炸锅.md"),
    recipe("高压力锅", "data/tips/learn/高压力锅.md"),
    recipe("厨房准备", "data/tips/厨房准备.md"),
    recipe("辅料技巧", "data/tips/advanced/辅料技巧.md"),
    recipe("食品安全", "data/tips/learn/食品安全.md"),
]

INGREDIENTS = [
    "牛肉", "猪肉", "鸡肉", "鸡蛋", "豆腐", "土豆", "茄子", "西红柿", "虾", "鲈鱼",
    "鳜鱼", "排骨", "羊肉", "鸭肉", "青蟹", "鲤鱼", "普通面条", "米饭", "玉米", "大白菜",
    "花菜", "西兰花", "黄瓜", "豆角", "蘑菇", "金针菇", "莲藕", "南瓜", "菠菜", "干豆腐",
]

# S05 A/B 只选择当前图中存在多跳路径的实体；S05 C 专门覆盖可解析但无路径的边界。
S05_POSITIVE_INGREDIENTS = [
    "牛肉", "猪肉", "鸡蛋", "豆腐", "土豆", "茄子", "西红柿", "虾", "鲈鱼", "鳜鱼",
    "排骨", "羊肉", "鸭肉", "青蟹", "鲤鱼", "普通面条", "米饭", "玉米", "花菜", "黄瓜",
]
S05_NOT_FOUND_INGREDIENTS = [
    "南瓜", "大白菜", "新鲜玉米", "新鲜菜心", "空心菜", "苦瓜", "菠菜", "西兰花", "酸菜", "韭菜",
]

SEMANTIC_REQUESTS = [
    "天气热，想做一道清爽不腻的晚饭", "下班很晚，想找准备步骤少的家常菜", "早餐想吃热乎又不复杂的", "周末想做一道有仪式感的海鲜菜",
    "想吃带汤的家常菜，别太难", "想做一道下饭的素菜", "想吃辣一点的川味家常菜", "只有微波炉时能做点什么",
    "招待两个人，想做一道看起来体面的鱼", "想做米饭搭配的一道菜", "天气冷想喝一碗暖和的汤", "想做不需要很多工具的早餐",
    "家里人不太能吃辣，晚餐有什么选择", "想做口感软糯的肉菜", "想做一道清蒸类菜", "想带便当，做什么相对合适",
    "今天想吃面食，想要有味道一点", "想做一道有蔬菜的快手菜", "朋友来家里，想做一道有地方特色的菜", "想吃酸甜口的菜",
    "想做一人份的简单晚餐", "想做一道适合夏天的凉菜", "想吃豆腐类菜，又不想太寡淡", "想做带番茄风味的菜",
    "冰箱食材不多，想先看看容易上手的菜", "想找一道适合电饭煲的主食", "想做一道煎制的小菜", "想做偏清淡的海鲜",
    "想做一道能配米饭的炖菜", "想吃甜品但不想步骤太复杂",
]

SOFT_PREFERENCES = [
    "想吃川菜但口感清爽", "想找少油感觉的川味晚餐", "偏好清淡一些的川菜", "不想吃太腻，想吃川味配米饭的菜",
    "想要有蔬菜的轻口味川菜", "今天想吃川味但口味温和些", "想吃辣但不希望太油重的川菜", "希望做法简单、吃起来不厚重的川味菜",
    "想吃豆腐类川菜又希望有味道", "偏好蒸制或煮制风格的川味晚餐", "想吃口感清爽的川味凉菜", "希望川菜里蔬菜多一点",
    "晚餐想少一些油腻感，想吃川菜", "想找适合夏天的轻口味川菜", "口味偏清淡，但可以有一点川味酸辣", "想吃鱼但不想做得太重口的川菜",
    "希望是一道川味素菜或蔬菜占主的菜", "想找适合午餐的轻负担川菜", "想吃清爽一点的川味蒸菜", "今天胃口一般，想吃清爽一点的川菜",
    "想做少调料也能吃的川味菜", "想喝一碗清淡些的川味汤", "希望推荐不太油的川味早餐做法", "想吃清新一点的川味番茄菜",
    "想找一道柔和、适合全家的川味菜", "偏好蔬菜和豆制品做成川菜", "不想吃油炸，推荐别的川味做法", "想吃不太刺激的川味面食",
    "今天想吃轻一点的川味海鲜", "想吃家常但不厚重的川味晚饭",
]

UNKNOWN_DISHES = [f"云岚{i:02d}号幻味砂锅" for i in range(1, 31)]
MISSING_RELATIONS = [f"星雾紫萝{i:02d}" for i in range(1, 31)]


SCENARIOS = [
    {
        "id": "S01",
        "title": "菜谱完整做法",
        "route": "entity_direct_recipe_full",
        "evaluation_mode": "ranking",
        "description": "验证菜谱实体直达、PDS 全文回补和完整食材/步骤证据。",
        "forbidden": ["full_corpus_vector_search", "unhydrated_chunk"],
    },
    {
        "id": "S02",
        "title": "菜谱指定步骤",
        "route": "entity_direct_recipe_step",
        "evaluation_mode": "ranking",
        "description": "验证步骤锚定、白名单图计划和局部 PDS 正文回补。",
        "forbidden": ["arbitrary_cypher", "full_corpus_vector_search"],
    },
    {
        "id": "S03",
        "title": "烹饪技巧章节",
        "route": "entity_direct_technique_section",
        "evaluation_mode": "ranking",
        "description": "验证技巧文档定位、章节级召回和连续上下文回补。",
        "forbidden": ["full_corpus_vector_search", "unhydrated_chunk"],
    },
    {
        "id": "S04",
        "title": "食材到菜谱关系",
        "route": "targeted_graph_ingredient_recipes",
        "evaluation_mode": "ranking",
        "description": "验证已命名食材到菜谱的图关系和文本证据链接。",
        "forbidden": ["text_as_relation_proof", "arbitrary_cypher"],
    },
    {
        "id": "S05",
        "title": "食材搭配多跳关系",
        "route": "targeted_graph_ingredient_vegetable_pairs",
        "evaluation_mode": "ranking",
        "description": "验证食材-菜谱-蔬菜多跳路径；仅接受图中的已验证关系。",
        "forbidden": ["text_as_relation_proof", "invented_relation_path"],
    },
    {
        "id": "S06",
        "title": "模糊语义推荐",
        "route": "restricted_vector_or_legacy_hybrid",
        "evaluation_mode": "ranking",
        "description": "验证模糊意图下的候选召回、排序、重排和父文档回补。",
        "forbidden": ["unhydrated_chunk"],
    },
    {
        "id": "S07",
        "title": "软偏好与营养边界",
        "route": "soft_preference_restricted_vector",
        "evaluation_mode": "ranking",
        "description": "验证偏好推荐只表达偏好，不将缺乏来源的推断包装为严格营养结论。",
        "forbidden": ["strict_low_fat_claim", "strict_nutrition_without_governed_source"],
    },
    {
        "id": "S08",
        "title": "未收录实体",
        "route": "entity_not_found",
        "evaluation_mode": "safety",
        "description": "验证未命中实体时拒绝猜测，且不返回虚构菜谱或检索证据。",
        "forbidden": ["silent_entity_guess", "invented_recipe"],
    },
    {
        "id": "S09",
        "title": "不可证明关系",
        "route": "graph_not_found",
        "evaluation_mode": "safety",
        "description": "通过隔离的 TargetedGraphRetriever 合约调用验证关系不存在时明确不可证明，不能以正文相似性伪造关系。",
        "forbidden": ["text_as_relation_proof", "invented_relation_path"],
    },
    {
        "id": "S10",
        "title": "图服务异常降级",
        "route": "graph_unavailable_safe_degradation",
        "evaluation_mode": "safety",
        "description": "使用隔离故障注入验证降级行为，不能触碰真实 Neo4j 数据或伪造关系结论。",
        "forbidden": ["text_as_relation_proof", "graph_fault_hidden", "invented_relation_path"],
    },
]

DIFFICULTIES = [
    ("A", "正向命中", "明确、标准的目标问题。"),
    ("B", "释义与歧义", "同一意图的自然表达或需在相近意图间作出判断的问题。"),
    ("C", "边界与反例", "要求系统在证据不足时收敛回答、暴露限制或拒绝伪造的问题。"),
]


def _target_recipe(item: dict[str, str], entity_type: str = "Recipe") -> dict[str, Any]:
    return {
        "entity_type": entity_type,
        "entity_name": item["name"],
        "source_path": item["source_path"],
        "gold_resolution": "preflight_exact_name_and_source_path",
    }


def _ranking_contract(scenario: dict[str, Any], target: dict[str, Any], evidence_mode: str) -> dict[str, Any]:
    return {
        "evaluation_mode": scenario["evaluation_mode"],
        "expected_route": scenario["route"],
        "evidence_mode": evidence_mode,
        "required_metrics": ["recall_at_1", "recall_at_3", "recall_at_5", "precision_at_1", "precision_at_3", "precision_at_5", "mrr_at_5", "ndcg_at_5", "hit_rate_at_5", "route_accuracy", "evidence_completeness", "evidence_linkage", "answer_faithfulness", "ttft_ms", "total_latency_ms"],
        "gold_target": target,
        "forbidden_assertions": scenario["forbidden"],
    }


def _safety_contract(scenario: dict[str, Any], target: dict[str, Any], required_status: str, execution_surface: str = "chat_api") -> dict[str, Any]:
    return {
        "evaluation_mode": scenario["evaluation_mode"],
        "expected_route": scenario["route"],
        "required_status": required_status,
        "execution_surface": execution_surface,
        "required_metrics": ["safety_pass_rate", "forbidden_assertion_count", "unsupported_relation_claim_count", "entity_decline_accuracy", "fault_degradation_accuracy", "ttft_ms", "total_latency_ms"],
        "gold_target": target,
        "forbidden_assertions": scenario["forbidden"],
    }


def _graph_not_found_contract(scenario: dict[str, Any], target: dict[str, Any]) -> dict[str, Any]:
    return {
        "evaluation_mode": "safety",
        "expected_route": scenario["route"],
        "evidence_mode": "verified_graph_multi_hop_not_found",
        "required_status": "graph_not_found",
        "execution_surface": "chat_api",
        "required_metrics": [
            "safety_pass_rate", "forbidden_assertion_count", "unsupported_relation_claim_count",
            "graph_not_found_accuracy", "ttft_ms", "total_latency_ms",
        ],
        "gold_target": target,
        "forbidden_assertions": scenario["forbidden"],
    }


def _question_text(scenario_id: str, difficulty: str, value: str) -> str:
    templates: dict[str, dict[str, str]] = {
        "S01": {
            "A": "请给出{value}的完整做法，包括主要食材和步骤。",
            "B": "{value}从备料到出锅怎么做？请按知识库里的做法回答。",
            "C": "我只要知识库能证明的{value}做法；不要补充未引用的替代方案或营养结论。",
        },
        "S02": {
            "A": "{value}的第 1 步应该怎么做？",
            "B": "刚开始做{value}时，第一步具体要处理什么？",
            "C": "只回答{value}的第 1 步，并说明它来自哪一条菜谱步骤；不要混入后续步骤。",
        },
        "S03": {
            "A": "请说明“{value}”这个技巧的关键要点和适用情形。",
            "B": "我想学{value}，它的关键要点和适用场景是什么？",
            "C": "只根据“{value}”技巧章节的关键要点回答；资料没有说明的结论请明确保留。",
        },
        "S04": {
            "A": "家里有{value}，知识库里能做哪些菜？",
            "B": "有{value}可以做什么菜？哪些菜谱确实包含它？",
            "C": "{value}能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。",
        },
        "S05": {
            "A": "{value}适合搭配什么蔬菜？",
            "B": "做{value}相关菜时，知识图谱里有哪些蔬菜搭配？",
            "C": "只给出图中能验证的{value}与蔬菜搭配；没有路径时请说明无法证明。",
        },
        "S06": {
            "A": "{value}。请推荐知识库中最合适的菜，并说明依据。",
            "B": "{value}，帮我找几个贴近这个需求的做法。",
            "C": "{value}。请展示推荐依据；如果意图无法由资料支持，不要把推测写成事实。",
        },
        "S07": {
            "A": "{value}。请推荐几个可考虑的菜。",
            "B": "{value}，有哪些做法比较贴近这种偏好？",
            "C": "{value}。可以表达偏好匹配，但没有受治理营养来源时不要断言“低脂”或其他严格营养事实。",
        },
        "S08": {
            "A": "{value}怎么做？",
            "B": "知识库里有{value}这道菜吗？如果有请给做法。",
            "C": "请查{value}的做法；未收录时只说明未找到，不要根据名称猜配方。",
        },
        "S09": {
            "A": "{value}和{value}有什么搭配关系？",
            "B": "知识图谱能证明{value}与{value}适合一起做吗？",
            "C": "请验证{value}和{value}的关系；没有图路径时不得用常识或正文替代证明。",
        },
        "S10": {
            "A": "图服务暂不可用时，{value}能做哪些菜？",
            "B": "假设 Neo4j 查询失败，系统处理“{value}做什么菜”时应如何回答？",
            "C": "在图服务故障注入下查询{value}相关菜谱；不得假装关系已被图验证。",
        },
    }
    return templates[scenario_id][difficulty].format(value=value)


def _relation_question(difficulty: str, ingredient: str, missing: str) -> str:
    templates = {
        "A": "{ingredient}和{missing}有什么搭配关系？",
        "B": "知识图谱能证明{ingredient}与{missing}适合一起做吗？",
        "C": "请验证{ingredient}和{missing}的关系；没有图路径时不得用常识或正文替代证明。",
    }
    return templates[difficulty].format(ingredient=ingredient, missing=missing)


def _build_questions() -> list[dict[str, Any]]:
    scenario_by_id = {item["id"]: item for item in SCENARIOS}
    questions: list[dict[str, Any]] = []

    def add(scenario_id: str, difficulty: str, index: int, text: str, contract: dict[str, Any]) -> None:
        questions.append(
            {
                "question_id": f"{scenario_id}-{difficulty}-{index:02d}",
                "scenario_id": scenario_id,
                "difficulty_code": difficulty,
                "difficulty_name": next(name for code, name, _ in DIFFICULTIES if code == difficulty),
                "question": text,
                "contract": contract,
            }
        )

    for scenario_id, targets, evidence_mode, entity_type in (
        ("S01", RECIPE_FULL_TARGETS, "pds_full_recipe", "Recipe"),
        ("S02", RECIPE_STEP_TARGETS, "pds_recipe_step_anchor", "Recipe"),
        ("S03", TECHNIQUE_TARGETS, "pds_technique_section", "TechniqueDoc"),
    ):
        scenario = scenario_by_id[scenario_id]
        for difficulty_index, (difficulty, _, _) in enumerate(DIFFICULTIES):
            for ordinal, target in enumerate(targets[difficulty_index * 10 : difficulty_index * 10 + 10], start=1):
                add(scenario_id, difficulty, ordinal, _question_text(scenario_id, difficulty, target["name"]), _ranking_contract(scenario, _target_recipe(target, entity_type), evidence_mode))

    scenario = scenario_by_id["S04"]
    for difficulty_index, (difficulty, _, _) in enumerate(DIFFICULTIES):
        for ordinal, ingredient in enumerate(INGREDIENTS[difficulty_index * 10 : difficulty_index * 10 + 10], start=1):
            target = {
                "entity_type": "Ingredient",
                "entity_name": ingredient,
                "gold_resolution": "preflight_exact_name_then_freeze_verified_graph_paths",
                "minimum_verified_graph_paths": 1,
            }
            add("S04", difficulty, ordinal, _question_text("S04", difficulty, ingredient), _ranking_contract(scenario, target, "verified_graph_relation_with_pds"))

    scenario = scenario_by_id["S05"]
    for difficulty_index, (difficulty, _, _) in enumerate(DIFFICULTIES[:2]):
        for ordinal, ingredient in enumerate(S05_POSITIVE_INGREDIENTS[difficulty_index * 10 : difficulty_index * 10 + 10], start=1):
            target = {
                "entity_type": "Ingredient",
                "entity_name": ingredient,
                "gold_resolution": "preflight_exact_name_then_freeze_verified_graph_paths",
                "minimum_verified_graph_paths": 1,
            }
            add("S05", difficulty, ordinal, _question_text("S05", difficulty, ingredient), _ranking_contract(scenario, target, "verified_graph_multi_hop_with_pds"))
    for ordinal, ingredient in enumerate(S05_NOT_FOUND_INGREDIENTS, start=1):
        target = {
            "entity_type": "Ingredient",
            "entity_name": ingredient,
            "gold_resolution": "preflight_exact_name_then_verify_zero_graph_paths",
            "expected_verified_graph_paths": 0,
        }
        add("S05", "C", ordinal, _question_text("S05", "C", ingredient), _graph_not_found_contract(scenario, target))

    for scenario_id, targets in (("S06", SEMANTIC_REQUESTS), ("S07", SOFT_PREFERENCES)):
        scenario = scenario_by_id[scenario_id]
        for difficulty_index, (difficulty, _, _) in enumerate(DIFFICULTIES):
            for ordinal, request in enumerate(targets[difficulty_index * 10 : difficulty_index * 10 + 10], start=1):
                target = {
                    "entity_type": "semantic_intent" if scenario_id == "S06" else "soft_preference",
                    "intent_text": request,
                    "gold_resolution": "preflight_freeze_graded_relevance_labels_from_source_markdown",
                    "minimum_gold_items": 3,
                }
                evidence_mode = "candidate_recall_rerank_pds" if scenario_id == "S06" else "soft_preference_candidate_recall_pds"
                add(scenario_id, difficulty, ordinal, _question_text(scenario_id, difficulty, request), _ranking_contract(scenario, target, evidence_mode))

    scenario = scenario_by_id["S08"]
    for difficulty_index, (difficulty, _, _) in enumerate(DIFFICULTIES):
        for ordinal, dish in enumerate(UNKNOWN_DISHES[difficulty_index * 10 : difficulty_index * 10 + 10], start=1):
            target = {"entity_type": "Recipe", "entity_name": dish, "gold_resolution": "preflight_assert_absent"}
            add("S08", difficulty, ordinal, _question_text("S08", difficulty, dish), _safety_contract(scenario, target, "entity_not_found"))

    scenario = scenario_by_id["S09"]
    for difficulty_index, (difficulty, _, _) in enumerate(DIFFICULTIES):
        for ordinal, (ingredient, missing) in enumerate(zip(INGREDIENTS[difficulty_index * 10 : difficulty_index * 10 + 10], MISSING_RELATIONS[difficulty_index * 10 : difficulty_index * 10 + 10]), start=1):
            target = {
                "known_entity_type": "Ingredient",
                "known_entity_name": ingredient,
                "missing_entity_type": "Ingredient",
                "missing_entity_name": missing,
                "gold_resolution": "preflight_assert_missing_entity_and_absent_relation",
            }
            add("S09", difficulty, ordinal, _relation_question(difficulty, ingredient, missing), _safety_contract(scenario, target, "graph_not_found", "isolated_targeted_component"))

    scenario = scenario_by_id["S10"]
    for difficulty_index, (difficulty, _, _) in enumerate(DIFFICULTIES):
        for ordinal, ingredient in enumerate(INGREDIENTS[difficulty_index * 10 : difficulty_index * 10 + 10], start=1):
            target = {
                "entity_type": "Ingredient",
                "entity_name": ingredient,
                "fault_injection": "isolated_graph_driver_unavailable",
                "gold_resolution": "preflight_assert_known_entity_then_inject_isolated_graph_failure",
            }
            add("S10", difficulty, ordinal, _question_text("S10", difficulty, ingredient), _safety_contract(scenario, target, "graph_unavailable", "isolated_fault_injection_component"))

    if len(questions) != 300:
        raise RuntimeError(f"题目数应为 300，实际为 {len(questions)}")
    if len({item['question_id'] for item in questions}) != len(questions):
        raise RuntimeError("题目 ID 重复")
    if len({item['question'] for item in questions}) != len(questions):
        raise RuntimeError("题干重复")
    return sorted(questions, key=lambda item: item["question_id"])


def _render_catalog(payload: dict[str, Any]) -> str:
    lines = ["# 检索重构真实场景考试目录", "", "本目录由 `工具/生成试卷.py` 生成。每场景 3 套卷，每套 10 题，共 300 题。", ""]
    by_id = {item["id"]: item for item in payload["scenarios"]}
    questions = payload["questions"]
    for scenario in payload["scenarios"]:
        lines.extend([f"## {scenario['id']} {scenario['title']}", "", scenario["description"], ""])
        for difficulty, difficulty_name, difficulty_description in DIFFICULTIES:
            lines.extend([f"### {difficulty} 卷：{difficulty_name}", "", difficulty_description, ""])
            for question in (item for item in questions if item["scenario_id"] == scenario["id"] and item["difficulty_code"] == difficulty):
                target = question["contract"]["gold_target"]
                target_name = target.get("entity_name") or target.get("intent_text") or target.get("known_entity_name") or "隔离故障注入"
                lines.append(f"{question['question_id']}. {question['question']}")
                lines.append(f"   - 目标：{target_name}")
            lines.append("")
    return "\n".join(lines)


def _render_validation(payload: dict[str, Any], digest: str) -> str:
    questions = payload["questions"]
    scenario_counts = Counter(item["scenario_id"] for item in questions)
    difficulty_counts = Counter(item["difficulty_code"] for item in questions)
    paths = [item["contract"]["gold_target"].get("source_path") for item in questions]
    paths = [item for item in paths if item]
    top_level = Counter(Path(item).parts[2] if len(Path(item).parts) > 2 else "unknown" for item in paths)
    lines = [
        "# 题库校验报告",
        "",
        f"- 题库 SHA-256：`{digest}`",
        f"- 题目数：`{len(questions)}`",
        f"- 唯一题干数：`{len({item['question'] for item in questions})}`",
        f"- 静态 sourcePath 引用数：`{len(paths)}`，唯一引用数：`{len(set(paths))}`",
        "- 静态 sourcePath 存在性：`已在生成时验证`",
        "",
        "## 场景计数",
        "",
    ]
    lines.extend(f"- `{scenario_id}`：{scenario_counts[scenario_id]}" for scenario_id in sorted(scenario_counts))
    lines.extend(["", "## 难度计数", ""])
    lines.extend(f"- `{difficulty}`：{difficulty_counts[difficulty]}" for difficulty in sorted(difficulty_counts))
    lines.extend(["", "## 已覆盖的源目录", ""])
    lines.extend(f"- `{name}`：{count}" for name, count in sorted(top_level.items()))
    lines.extend([
        "", "## 图路径生成校验", "",
        "- S04 与 S05 A/B 的实体均在 `nodes.csv`/`relationships.csv` 中有题目要求的最少真实路径。",
        "- S05 C 的实体均可解析，且真实 `Ingredient <- REQUIRES - Recipe - REQUIRES -> 蔬菜` 路径数为 0；它们按安全拒答计分。",
        "", "## 开考前必须完成的检查", "",
        "- 静态 sourcePath 是否仍存在。",
        "- 所有已命名实体是否在当前 Neo4j 实例可解析。",
        "- S04 与 S05 A/B 的最少图路径是否真实存在；S05 C 必须复核为零路径，不得改写为正向 gold。",
        "- S06/S07 的分级相关性标签是否在第一次请求前冻结。",
        "- S08/S09 的虚构实体是否确实不存在。",
        "",
    ])
    return "\n".join(lines)


def _validate_static_sources(questions: list[dict[str, Any]]) -> None:
    source_paths = {
        target["source_path"]
        for question in questions
        if isinstance((target := question["contract"].get("gold_target")), dict)
        and isinstance(target.get("source_path"), str)
    }
    missing = sorted(path for path in source_paths if not (PROJECT_ROOT / path).is_file())
    if missing:
        rendered = "\n".join(f"- {path}" for path in missing)
        raise RuntimeError(f"题库引用了不存在的静态 sourcePath：\n{rendered}")


def _graph_path_counts() -> tuple[Counter[str], Counter[str]]:
    with NODES_PATH.open(encoding="utf-8", newline="") as stream:
        nodes = list(csv.DictReader(stream))
    with RELATIONSHIPS_PATH.open(encoding="utf-8", newline="") as stream:
        relationships = list(csv.DictReader(stream))

    nodes_by_id = {node["nodeId"]: node for node in nodes if node.get("nodeId")}
    requires = [relation for relation in relationships if relation.get("relationshipType") == "801000001"]
    requires_by_recipe: dict[str, list[dict[str, str]]] = defaultdict(list)
    for relation in requires:
        requires_by_recipe[relation.get("startNodeId", "")].append(relation)
    direct_counts: Counter[str] = Counter()
    pair_counts: Counter[str] = Counter()
    for relation in requires:
        ingredient = nodes_by_id.get(relation.get("endNodeId", ""))
        recipe_node = nodes_by_id.get(relation.get("startNodeId", ""))
        if not ingredient or not recipe_node or ingredient.get("labels") != "Ingredient" or recipe_node.get("labels") != "Recipe":
            continue
        ingredient_name = ingredient.get("name", "")
        direct_counts[ingredient_name] += 1
        for other in requires_by_recipe[recipe_node["nodeId"]]:
            vegetable = nodes_by_id.get(other.get("endNodeId", ""))
            if (
                other.get("endNodeId") != ingredient["nodeId"]
                and vegetable
                and vegetable.get("labels") == "Ingredient"
                and vegetable.get("category") == "蔬菜"
            ):
                pair_counts[ingredient_name] += 1
    return direct_counts, pair_counts


def _validate_graph_targets(questions: list[dict[str, Any]]) -> None:
    direct_counts, pair_counts = _graph_path_counts()
    failures: list[str] = []
    for question in questions:
        scenario_id = question["scenario_id"]
        target = question["contract"]["gold_target"]
        entity_name = target.get("entity_name")
        if scenario_id == "S04":
            if not entity_name or direct_counts[entity_name] < target.get("minimum_verified_graph_paths", 1):
                failures.append(f"{question['question_id']} 缺少食材到菜谱图路径：{entity_name}")
        elif scenario_id == "S05":
            expected_paths = target.get("expected_verified_graph_paths")
            if expected_paths == 0:
                if not entity_name or direct_counts[entity_name] == 0 or pair_counts[entity_name] != 0:
                    failures.append(f"{question['question_id']} 不是可解析且零路径的 S05 边界题：{entity_name}")
            elif not entity_name or pair_counts[entity_name] < target.get("minimum_verified_graph_paths", 1):
                failures.append(f"{question['question_id']} 缺少食材-菜谱-蔬菜图路径：{entity_name}")
    if failures:
        raise RuntimeError("题库图路径契约不满足：\n" + "\n".join(f"- {failure}" for failure in failures))


def main() -> None:
    questions = _build_questions()
    _validate_static_sources(questions)
    _validate_graph_targets(questions)
    payload = {
        "schema_version": "retrieval-real-exam-v1",
        "title": "检索重构真实场景考试",
        "question_count": 300,
        "scenario_count": 10,
        "papers_per_scenario": 3,
        "questions_per_paper": 10,
        "difficulties": [{"code": code, "name": name, "description": description} for code, name, description in DIFFICULTIES],
        "scenarios": SCENARIOS,
        "questions": questions,
    }
    encoded = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    digest = hashlib.sha256(encoded.encode("utf-8")).hexdigest()
    BANK_PATH.write_text(encoded, encoding="utf-8")
    CATALOG_PATH.write_text(_render_catalog(payload), encoding="utf-8")
    VALIDATION_PATH.write_text(_render_validation(payload, digest), encoding="utf-8")
    print(f"generated {len(questions)} questions")
    print(f"bank_sha256={digest}")


if __name__ == "__main__":
    main()
