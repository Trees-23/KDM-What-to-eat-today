# Recall Content

audit_id: 20260811_173640_804_c132667c
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201001429, recipe_name=鸭肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸭肉
食材名称: 鸭肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=1
source: entity_level
metadata_summary: node_id=201002327, recipe_name=啤酒鸭, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 啤酒鸭
菜品名称: 啤酒鸭
分类: 荤菜
菜系: 川菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=201002391, recipe_name=奶酪培根通心粉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 奶酪培根通心粉
分类: 荤菜
菜系: 美式
难度: 3.0
主要食材: 洋葱, 黄油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=1
source: topic_level
metadata_summary: node_id=201005492, recipe_name=烤茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 烤茄子
分类: 素菜
难度: 3.0
主要食材: 茄子, 食用油, 孜然
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=2
source: topic_level
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: topic_level
metadata_summary: node_id=201000411, recipe_name=蛏抱蛋, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 蛏抱蛋
分类: 水产
菜系: 闽菜
难度: 3.0
主要食材: 鸡蛋, 食用油, 鸡精
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 鸡精 (Ingredient): category: 调料
```

### result_order=4
source: topic_level
metadata_summary: node_id=201002937, recipe_name=糖醋排骨, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
主要食材: 番茄酱, 排骨, 姜片
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=5
source: topic_level
metadata_summary: node_id=201000127, recipe_name=红烧鲤鱼, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 红烧鲤鱼
分类: 水产
菜系: 鲁菜
难度: 4.0
主要食材: 蒜瓣, 清水, 盐
关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### result_order=6
source: topic_level
metadata_summary: node_id=201003196, recipe_name=西红柿土豆炖牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 西红柿土豆炖牛肉
分类: 荤菜
难度: 4.0
主要食材: 油, 黑胡椒粉, 牛肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=7
source: topic_level
metadata_summary: node_id=201002282, recipe_name=台式卤肉饭, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 台式卤肉饭
分类: 荤菜
菜系: 台湾菜
难度: 5.0
主要食材: 大蒜, 白胡椒粉, 五香粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201001428, chunk_id=201001428_chunk_317, recipe_name=乡村啤酒鸭, category=荤菜, score=0.7047391533851624, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸭肉清洗一遍放进锅中，加清水淹没鸭肉，加入20 ml料酒、1根大葱、拍散的2厘米生姜，开火烧滚，捞出浮沫，鸭肉捞出用清水洗净备用。
方法: 焯水,清洗
工具: 锅,漏勺
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 锅清洗后烧热，加入60 ml花生油，油温升至60℃时加入30颗花椒爆香。
方法: 加热,爆香
工具: 炒锅,锅铲
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 倒入鸭肉翻炒4分钟：2分钟后加入所有香料（草果、桂皮、八角、香叶、干辣椒），3分钟时加入料头（生姜、大蒜、小米辣）。
方法: 炒
工具: 炒锅,锅铲
时间: 4分钟

### 第4步
步骤: 步骤4
描述: 加入1000 ml啤酒，大火烧开后转小火炖煮30分钟。
方法: 炖煮
工具: 炒锅,锅盖
时间: 30分钟

### 第5步
步骤: 步骤5
描述: 炖煮10分钟时加入盐3克、生抽10 ml、老抽5 ml；20分钟时加入青椒和红椒段；29分钟时加入蒜苗段和剩余大葱段，翻炒1分钟后出锅。
方法: 调味,炖煮,炒
工具: 锅铲
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201002327, chunk_id=201002327_chunk_477, recipe_name=啤酒鸭, category=荤菜, score=0.6986643075942993, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 把鸭子切成3 cm小块，鸭肉冷水下锅，加姜片、料酒，焯一遍水，盛出沥干水分，备用。
方法: 切,焯水
工具: 刀,案板,锅
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，鸭肉入锅翻炒至上色。
方法: 炒
工具: 炒锅,锅铲
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），将鸭肉拨到锅的一边，倒入豆瓣酱和糖，小火翻炒出香味和糖色。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 加入丁香、八角、香叶、干辣椒、生抽、老抽、蒜，翻炒出香味。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第5步
步骤: 步骤5
描述: 倒入啤酒，没过鸭肉，加入盐、鸡精，然后中火将鸭子烧30分钟（牙口不好的话可以再多烧5分钟）。
方法: 炖
工具: 炒锅
时间: 30-35分钟

### 第6步
步骤: 步骤6
描述: 出锅盛盘，上桌食用。
方法: 盛盘
工具: 锅铲,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201003174, chunk_id=201003174_chunk_625, recipe_name=血浆鸭, category=荤菜, score=0.6822845935821533, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜仔鸭肉切成约3cm小块，加料酒、姜片，去除血水。
方法: 切,腌制
工具: 刀,案板,盆
时间: 约10分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，放入腌制好的鲜鸭肉，不断翻炒。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），放入酒，再加入200ml开水，刚好淹没鸭肉即可，盖上锅盖中火煮15分钟。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第4步
步骤: 步骤4
描述: 水开之后，打开锅盖放入姜蒜，翻炒一遍，盖上锅盖持续加热10分钟。
方法: 炒,焖
工具: 炒锅,锅盖,锅铲
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 打开锅盖放入辣椒，不断翻炒，待至肉眼可见辣椒炒软，放入鲜鸭血，此时需要不断翻炒，确保每块鸭肉和每片辣椒都有鸭血的浸润。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第6步
步骤: 步骤6
描述: 翻炒至肉眼可见鸭血均为黑色，加入盐、鸡精、香葱，（喜欢食用山胡椒油的朋友也可以在此时放入3-6滴山胡椒油）再次翻炒一到二次即可。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第7步
步骤: 步骤7
描述: 出锅盛盘，上桌食用。
方法: 装盘
工具: 盘子
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201002857, chunk_id=201002857_chunk_565, recipe_name=湘祁米夫鸭, category=荤菜, score=0.6754992604255676, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将糯米粉、粘米粉、蒸肉粉、细辣椒粉、5克盐、白胡椒粉倒在一起搅匀，制成米粉混合物备用。
方法: 混合
工具: 盆
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 鸭子请摊主剁成适合蒸煮的块；姜切片，蒜剥皮；五花肉切片备用。
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第3步
步骤: 步骤3
描述: 热锅凉油，先煸炒五花肉出油，再加适量食用油烧热，放入鸭块煸炒。
方法: 炒
工具: 炒锅,锅铲
时间: 约3-5分钟

### 第4步
步骤: 步骤4
描述: 鸭肉煸炒至表皮焦黄变色，加入姜片、蒜瓣和剩余盐，继续炒出香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 关小火，倒入米粉混合物翻炒，使鸭肉均匀裹满米粉；少量多次加入开水，边加边翻炒，保持湿润。
方法: 炒
工具: 炒锅,锅铲
时间: 约3分钟

### 第6步
步骤: 步骤6
描述: 将裹好米粉的鸭肉装入碗中，放入高压锅，加水蒸20-25分钟（老鸭需60分钟以上）。
方法: 蒸
工具: 高压锅,碗
时间: 20-25分钟

### 第7步
步骤: 步骤7
描述: 出锅前撒葱花即可享用。
方法: 装饰
工具: 筷子
时间: 约10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201002857, chunk_id=201002857_chunk_566, recipe_name=湘祁米夫鸭, category=荤菜, score=0.6383567452430725, search_type=vector_enhanced

```text
## 标签
湖南两祁地区特色菜,鸭肉品种不限，水鸭即可,粘米粉为主粉，糯米粉增软糯，蒸肉粉增五香,辣椒粉和胡椒粉提供复合香味,高压锅蒸20分钟（老鸭需1小时以上）
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201002857, chunk_id=201002857_chunk_564, recipe_name=湘祁米夫鸭, category=荤菜, score=0.6240752339363098, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(50克)
2. 姜蒜(20克)
3. 开水(100克)
4. 白胡椒粉(5克)
5. 盐(10克)
6. 粘米粉(300克)
7. 糯米粉(100克)
8. 细辣椒粉(50克)
9. 蒸肉粉(50克)
10. 食用油(10克)
11. 鸭子(1000克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6196181774139404, search_type=vector_enhanced

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201003174, chunk_id=201003174_chunk_623, recipe_name=血浆鸭, category=荤菜, score=0.6044767498970032, search_type=vector_enhanced

```text
# 血浆鸭

菜系: 湘菜
难度: 5.0星

时间信息: 准备时间: 约20分钟（切鸭、处理鸭血、切配料）, 烹饪时间: 约40分钟（炒、煮、焖、收汁）
份量: 2-4人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_683, recipe_name=麻婆豆腐, category=荤菜, score=0.5910249352455139, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(20g)
2. 内脂豆腐(1盒)
3. 咸鸭蛋(1枚)
4. 大蒜(2瓣)
5. 小米椒(5根)
6. 开水(适量ml)
7. 生姜(2片)
8. 花椒(20颗)
9. 酱油(10g)
10. 食用油(10ml)
11. 食盐(3g)
12. 香辣酱(5g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1321, recipe_name=凉拌, category=烹饪技巧, score=0.5863900184631348, search_type=vector_enhanced

```text
## 块状肉类主食菜加工（此流程可选）（选项单选或多选）
### 块状肉类主食菜加工（此流程可选）（选项单选或多选）

用例：鱼肉、海蜇头、熟猪肉、熟禽类等

* 将食材通过蒸煮烤炸等方式熟制
* 将食材在凉水中泡上些许时间（犹适用于海产）
* 将食材撕成肉条
* 将食材切成薄片（犹适用于煮熟后的猪肉）
* 将食材切成 0.8cm * 0.8cm 截面长条状
* 将食材直接按部位撕碎或切大块（犹适用于整只熟禽）

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201001429, recipe_name=鸭肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸭肉
食材名称: 鸭肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201002327, recipe_name=啤酒鸭, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 啤酒鸭
菜品名称: 啤酒鸭
分类: 荤菜
菜系: 川菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201002391, recipe_name=奶酪培根通心粉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 奶酪培根通心粉
分类: 荤菜
菜系: 美式
难度: 3.0
主要食材: 洋葱, 黄油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201005492, recipe_name=烤茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 烤茄子
分类: 素菜
难度: 3.0
主要食材: 茄子, 食用油, 孜然
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201000411, recipe_name=蛏抱蛋, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 蛏抱蛋
分类: 水产
菜系: 闽菜
难度: 3.0
主要食材: 鸡蛋, 食用油, 鸡精
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 鸡精 (Ingredient): category: 调料
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201002937, recipe_name=糖醋排骨, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
主要食材: 番茄酱, 排骨, 姜片
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201000127, recipe_name=红烧鲤鱼, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 红烧鲤鱼
分类: 水产
菜系: 鲁菜
难度: 4.0
主要食材: 蒜瓣, 清水, 盐
关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201003196, recipe_name=西红柿土豆炖牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 西红柿土豆炖牛肉
分类: 荤菜
难度: 4.0
主要食材: 油, 黑胡椒粉, 牛肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201002282, recipe_name=台式卤肉饭, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 台式卤肉饭
分类: 荤菜
菜系: 台湾菜
难度: 5.0
主要食材: 大蒜, 白胡椒粉, 五香粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201001428, chunk_id=201001428_chunk_317, recipe_name=乡村啤酒鸭, category=荤菜, score=0.7047391533851624, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸭肉清洗一遍放进锅中，加清水淹没鸭肉，加入20 ml料酒、1根大葱、拍散的2厘米生姜，开火烧滚，捞出浮沫，鸭肉捞出用清水洗净备用。
方法: 焯水,清洗
工具: 锅,漏勺
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 锅清洗后烧热，加入60 ml花生油，油温升至60℃时加入30颗花椒爆香。
方法: 加热,爆香
工具: 炒锅,锅铲
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 倒入鸭肉翻炒4分钟：2分钟后加入所有香料（草果、桂皮、八角、香叶、干辣椒），3分钟时加入料头（生姜、大蒜、小米辣）。
方法: 炒
工具: 炒锅,锅铲
时间: 4分钟

### 第4步
步骤: 步骤4
描述: 加入1000 ml啤酒，大火烧开后转小火炖煮30分钟。
方法: 炖煮
工具: 炒锅,锅盖
时间: 30分钟

### 第5步
步骤: 步骤5
描述: 炖煮10分钟时加入盐3克、生抽10 ml、老抽5 ml；20分钟时加入青椒和红椒段；29分钟时加入蒜苗段和剩余大葱段，翻炒1分钟后出锅。
方法: 调味,炖煮,炒
工具: 锅铲
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201002327, chunk_id=201002327_chunk_477, recipe_name=啤酒鸭, category=荤菜, score=0.6986643075942993, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 把鸭子切成3 cm小块，鸭肉冷水下锅，加姜片、料酒，焯一遍水，盛出沥干水分，备用。
方法: 切,焯水
工具: 刀,案板,锅
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，鸭肉入锅翻炒至上色。
方法: 炒
工具: 炒锅,锅铲
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），将鸭肉拨到锅的一边，倒入豆瓣酱和糖，小火翻炒出香味和糖色。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 加入丁香、八角、香叶、干辣椒、生抽、老抽、蒜，翻炒出香味。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第5步
步骤: 步骤5
描述: 倒入啤酒，没过鸭肉，加入盐、鸡精，然后中火将鸭子烧30分钟（牙口不好的话可以再多烧5分钟）。
方法: 炖
工具: 炒锅
时间: 30-35分钟

### 第6步
步骤: 步骤6
描述: 出锅盛盘，上桌食用。
方法: 盛盘
工具: 锅铲,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201003174, chunk_id=201003174_chunk_625, recipe_name=血浆鸭, category=荤菜, score=0.6822845935821533, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜仔鸭肉切成约3cm小块，加料酒、姜片，去除血水。
方法: 切,腌制
工具: 刀,案板,盆
时间: 约10分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，放入腌制好的鲜鸭肉，不断翻炒。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），放入酒，再加入200ml开水，刚好淹没鸭肉即可，盖上锅盖中火煮15分钟。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第4步
步骤: 步骤4
描述: 水开之后，打开锅盖放入姜蒜，翻炒一遍，盖上锅盖持续加热10分钟。
方法: 炒,焖
工具: 炒锅,锅盖,锅铲
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 打开锅盖放入辣椒，不断翻炒，待至肉眼可见辣椒炒软，放入鲜鸭血，此时需要不断翻炒，确保每块鸭肉和每片辣椒都有鸭血的浸润。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第6步
步骤: 步骤6
描述: 翻炒至肉眼可见鸭血均为黑色，加入盐、鸡精、香葱，（喜欢食用山胡椒油的朋友也可以在此时放入3-6滴山胡椒油）再次翻炒一到二次即可。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第7步
步骤: 步骤7
描述: 出锅盛盘，上桌食用。
方法: 装盘
工具: 盘子
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201002857, chunk_id=201002857_chunk_565, recipe_name=湘祁米夫鸭, category=荤菜, score=0.6754992604255676, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将糯米粉、粘米粉、蒸肉粉、细辣椒粉、5克盐、白胡椒粉倒在一起搅匀，制成米粉混合物备用。
方法: 混合
工具: 盆
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 鸭子请摊主剁成适合蒸煮的块；姜切片，蒜剥皮；五花肉切片备用。
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第3步
步骤: 步骤3
描述: 热锅凉油，先煸炒五花肉出油，再加适量食用油烧热，放入鸭块煸炒。
方法: 炒
工具: 炒锅,锅铲
时间: 约3-5分钟

### 第4步
步骤: 步骤4
描述: 鸭肉煸炒至表皮焦黄变色，加入姜片、蒜瓣和剩余盐，继续炒出香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 关小火，倒入米粉混合物翻炒，使鸭肉均匀裹满米粉；少量多次加入开水，边加边翻炒，保持湿润。
方法: 炒
工具: 炒锅,锅铲
时间: 约3分钟

### 第6步
步骤: 步骤6
描述: 将裹好米粉的鸭肉装入碗中，放入高压锅，加水蒸20-25分钟（老鸭需60分钟以上）。
方法: 蒸
工具: 高压锅,碗
时间: 20-25分钟

### 第7步
步骤: 步骤7
描述: 出锅前撒葱花即可享用。
方法: 装饰
工具: 筷子
时间: 约10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201002857, chunk_id=201002857_chunk_566, recipe_name=湘祁米夫鸭, category=荤菜, score=0.6383567452430725, search_type=vector_enhanced

```text
## 标签
湖南两祁地区特色菜,鸭肉品种不限，水鸭即可,粘米粉为主粉，糯米粉增软糯，蒸肉粉增五香,辣椒粉和胡椒粉提供复合香味,高压锅蒸20分钟（老鸭需1小时以上）
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=15
source: branch_grouped
metadata_summary: node_id=201002857, chunk_id=201002857_chunk_564, recipe_name=湘祁米夫鸭, category=荤菜, score=0.6240752339363098, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(50克)
2. 姜蒜(20克)
3. 开水(100克)
4. 白胡椒粉(5克)
5. 盐(10克)
6. 粘米粉(300克)
7. 糯米粉(100克)
8. 细辣椒粉(50克)
9. 蒸肉粉(50克)
10. 食用油(10克)
11. 鸭子(1000克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=16
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6196181774139404, search_type=vector_enhanced

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=17
source: branch_grouped
metadata_summary: node_id=201003174, chunk_id=201003174_chunk_623, recipe_name=血浆鸭, category=荤菜, score=0.6044767498970032, search_type=vector_enhanced

```text
# 血浆鸭

菜系: 湘菜
难度: 5.0星

时间信息: 准备时间: 约20分钟（切鸭、处理鸭血、切配料）, 烹饪时间: 约40分钟（炒、煮、焖、收汁）
份量: 2-4人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=18
source: branch_grouped
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_683, recipe_name=麻婆豆腐, category=荤菜, score=0.5910249352455139, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(20g)
2. 内脂豆腐(1盒)
3. 咸鸭蛋(1枚)
4. 大蒜(2瓣)
5. 小米椒(5根)
6. 开水(适量ml)
7. 生姜(2片)
8. 花椒(20颗)
9. 酱油(10g)
10. 食用油(10ml)
11. 食盐(3g)
12. 香辣酱(5g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=19
source: branch_grouped
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1321, recipe_name=凉拌, category=烹饪技巧, score=0.5863900184631348, search_type=vector_enhanced

```text
## 块状肉类主食菜加工（此流程可选）（选项单选或多选）
### 块状肉类主食菜加工（此流程可选）（选项单选或多选）

用例：鱼肉、海蜇头、熟猪肉、熟禽类等

* 将食材通过蒸煮烤炸等方式熟制
* 将食材在凉水中泡上些许时间（犹适用于海产）
* 将食材撕成肉条
* 将食材切成薄片（犹适用于煮熟后的猪肉）
* 将食材切成 0.8cm * 0.8cm 截面长条状
* 将食材直接按部位撕碎或切大块（犹适用于整只熟禽）

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201001429, recipe_name=鸭肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸭肉
食材名称: 鸭肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201002327, chunk_id=201002327_chunk_477, recipe_name=啤酒鸭, category=荤菜, score=0.6986643075942993, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 把鸭子切成3 cm小块，鸭肉冷水下锅，加姜片、料酒，焯一遍水，盛出沥干水分，备用。
方法: 切,焯水
工具: 刀,案板,锅
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，鸭肉入锅翻炒至上色。
方法: 炒
工具: 炒锅,锅铲
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），将鸭肉拨到锅的一边，倒入豆瓣酱和糖，小火翻炒出香味和糖色。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 加入丁香、八角、香叶、干辣椒、生抽、老抽、蒜，翻炒出香味。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第5步
步骤: 步骤5
描述: 倒入啤酒，没过鸭肉，加入盐、鸡精，然后中火将鸭子烧30分钟（牙口不好的话可以再多烧5分钟）。
方法: 炖
工具: 炒锅
时间: 30-35分钟

### 第6步
步骤: 步骤6
描述: 出锅盛盘，上桌食用。
方法: 盛盘
工具: 锅铲,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201002391, recipe_name=奶酪培根通心粉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 奶酪培根通心粉
分类: 荤菜
菜系: 美式
难度: 3.0
主要食材: 洋葱, 黄油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201005492, recipe_name=烤茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 烤茄子
分类: 素菜
难度: 3.0
主要食材: 茄子, 食用油, 孜然
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201000411, recipe_name=蛏抱蛋, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 蛏抱蛋
分类: 水产
菜系: 闽菜
难度: 3.0
主要食材: 鸡蛋, 食用油, 鸡精
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 鸡精 (Ingredient): category: 调料
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=201002937, recipe_name=糖醋排骨, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
主要食材: 番茄酱, 排骨, 姜片
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201000127, recipe_name=红烧鲤鱼, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 红烧鲤鱼
分类: 水产
菜系: 鲁菜
难度: 4.0
主要食材: 蒜瓣, 清水, 盐
关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201003196, recipe_name=西红柿土豆炖牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 西红柿土豆炖牛肉
分类: 荤菜
难度: 4.0
主要食材: 油, 黑胡椒粉, 牛肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=201002282, recipe_name=台式卤肉饭, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 台式卤肉饭
分类: 荤菜
菜系: 台湾菜
难度: 5.0
主要食材: 大蒜, 白胡椒粉, 五香粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201001428, chunk_id=201001428_chunk_317, recipe_name=乡村啤酒鸭, category=荤菜, score=0.7047391533851624, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸭肉清洗一遍放进锅中，加清水淹没鸭肉，加入20 ml料酒、1根大葱、拍散的2厘米生姜，开火烧滚，捞出浮沫，鸭肉捞出用清水洗净备用。
方法: 焯水,清洗
工具: 锅,漏勺
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 锅清洗后烧热，加入60 ml花生油，油温升至60℃时加入30颗花椒爆香。
方法: 加热,爆香
工具: 炒锅,锅铲
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 倒入鸭肉翻炒4分钟：2分钟后加入所有香料（草果、桂皮、八角、香叶、干辣椒），3分钟时加入料头（生姜、大蒜、小米辣）。
方法: 炒
工具: 炒锅,锅铲
时间: 4分钟

### 第4步
步骤: 步骤4
描述: 加入1000 ml啤酒，大火烧开后转小火炖煮30分钟。
方法: 炖煮
工具: 炒锅,锅盖
时间: 30分钟

### 第5步
步骤: 步骤5
描述: 炖煮10分钟时加入盐3克、生抽10 ml、老抽5 ml；20分钟时加入青椒和红椒段；29分钟时加入蒜苗段和剩余大葱段，翻炒1分钟后出锅。
方法: 调味,炖煮,炒
工具: 锅铲
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=201003174, chunk_id=201003174_chunk_625, recipe_name=血浆鸭, category=荤菜, score=0.6822845935821533, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜仔鸭肉切成约3cm小块，加料酒、姜片，去除血水。
方法: 切,腌制
工具: 刀,案板,盆
时间: 约10分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，放入腌制好的鲜鸭肉，不断翻炒。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），放入酒，再加入200ml开水，刚好淹没鸭肉即可，盖上锅盖中火煮15分钟。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第4步
步骤: 步骤4
描述: 水开之后，打开锅盖放入姜蒜，翻炒一遍，盖上锅盖持续加热10分钟。
方法: 炒,焖
工具: 炒锅,锅盖,锅铲
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 打开锅盖放入辣椒，不断翻炒，待至肉眼可见辣椒炒软，放入鲜鸭血，此时需要不断翻炒，确保每块鸭肉和每片辣椒都有鸭血的浸润。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第6步
步骤: 步骤6
描述: 翻炒至肉眼可见鸭血均为黑色，加入盐、鸡精、香葱，（喜欢食用山胡椒油的朋友也可以在此时放入3-6滴山胡椒油）再次翻炒一到二次即可。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第7步
步骤: 步骤7
描述: 出锅盛盘，上桌食用。
方法: 装盘
工具: 盘子
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=201002857, chunk_id=201002857_chunk_565, recipe_name=湘祁米夫鸭, category=荤菜, score=0.6754992604255676, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将糯米粉、粘米粉、蒸肉粉、细辣椒粉、5克盐、白胡椒粉倒在一起搅匀，制成米粉混合物备用。
方法: 混合
工具: 盆
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 鸭子请摊主剁成适合蒸煮的块；姜切片，蒜剥皮；五花肉切片备用。
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第3步
步骤: 步骤3
描述: 热锅凉油，先煸炒五花肉出油，再加适量食用油烧热，放入鸭块煸炒。
方法: 炒
工具: 炒锅,锅铲
时间: 约3-5分钟

### 第4步
步骤: 步骤4
描述: 鸭肉煸炒至表皮焦黄变色，加入姜片、蒜瓣和剩余盐，继续炒出香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 关小火，倒入米粉混合物翻炒，使鸭肉均匀裹满米粉；少量多次加入开水，边加边翻炒，保持湿润。
方法: 炒
工具: 炒锅,锅铲
时间: 约3分钟

### 第6步
步骤: 步骤6
描述: 将裹好米粉的鸭肉装入碗中，放入高压锅，加水蒸20-25分钟（老鸭需60分钟以上）。
方法: 蒸
工具: 高压锅,碗
时间: 20-25分钟

### 第7步
步骤: 步骤7
描述: 出锅前撒葱花即可享用。
方法: 装饰
工具: 筷子
时间: 约10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=13
source: merged_candidates
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6196181774139404, search_type=vector_enhanced

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=14
source: merged_candidates
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_683, recipe_name=麻婆豆腐, category=荤菜, score=0.5910249352455139, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(20g)
2. 内脂豆腐(1盒)
3. 咸鸭蛋(1枚)
4. 大蒜(2瓣)
5. 小米椒(5根)
6. 开水(适量ml)
7. 生姜(2片)
8. 花椒(20颗)
9. 酱油(10g)
10. 食用油(10ml)
11. 食盐(3g)
12. 香辣酱(5g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=15
source: merged_candidates
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1321, recipe_name=凉拌, category=烹饪技巧, score=0.5863900184631348, search_type=vector_enhanced

```text
## 块状肉类主食菜加工（此流程可选）（选项单选或多选）
### 块状肉类主食菜加工（此流程可选）（选项单选或多选）

用例：鱼肉、海蜇头、熟猪肉、熟禽类等

* 将食材通过蒸煮烤炸等方式熟制
* 将食材在凉水中泡上些许时间（犹适用于海产）
* 将食材撕成肉条
* 将食材切成薄片（犹适用于煮熟后的猪肉）
* 将食材切成 0.8cm * 0.8cm 截面长条状
* 将食材直接按部位撕碎或切大块（犹适用于整只熟禽）

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipdoc_fd7f557c37a7, recipe_name=如何决策吃什么、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 如何决策吃什么、凉拌
关键技巧内容:
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
## 计算方法
## 计算方法
## 计算荤菜和素菜数量
### 计算荤菜和素菜数量

* 菜的数量 = 人数 + 1。
* 荤菜比素菜多一个，或一样多即可。

由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
## 形式语言描述
#### 形式语言描述

当 有人数 `N` 时，
设 `素菜数` 为 `a`, `荤菜数`为 `b`。
`N`, `a`, `b`均为整数。

此时有下列不等式组：

* a + b = N + 1
* a ≤ b ≤ a+1

解得

```javascript
const a = Math.floor((N+1)/2);
const b = Math.ceil((N+1)/2);
```
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
## 凉拌的形态
### 凉拌的形态

凉拌可做成食材与辅料在空间上交混的形态
凉拌可做成食材与辅料在空间上分立的形态，此时辅料被称为蘸料
## 为什么凉拌
### 为什么凉拌

* 部分凉拌成菜时不需要热源
* 部分凉拌能减少洗锅的流程（不洗或仅过水即可）
* 凉拌能保留食材状态，此点特别展现在蔬菜、生肉上
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 鸭肉
食材名称: 鸭肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### pair_order=1
source: rerank_input

```text
菜品: 啤酒鸭
菜系: 川菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 把鸭子切成3 cm小块，鸭肉冷水下锅，加姜片、料酒，焯一遍水，盛出沥干水分，备用。
方法: 切,焯水
工具: 刀,案板,锅
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，鸭肉入锅翻炒至上色。
方法: 炒
工具: 炒锅,锅铲
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），将鸭肉拨到锅的一边，倒入豆瓣酱和糖，小火翻炒出香味和糖色。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 加入丁香、八角、香叶、干辣椒、生抽、老抽、蒜，翻炒出香味。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第5步
步骤: 步骤5
描述: 倒入啤酒，没过鸭肉，加入盐、鸡精，然后中火将鸭子烧30分钟（牙口不好的话可以再多烧5分钟）。
方法: 炖
工具: 炒锅
时间: 30-35分钟

### 第6步
步骤: 步骤6
描述: 出锅盛盘，上桌食用。
方法: 盛盘
工具: 锅铲,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 家常菜
菜品: 奶酪培根通心粉
分类: 荤菜
菜系: 美式
难度: 3.0
主要食材: 洋葱, 黄油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=3
source: rerank_input

```text
命中关键词: 烤制
菜品: 烤茄子
分类: 素菜
难度: 3.0
主要食材: 茄子, 食用油, 孜然
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=4
source: rerank_input

```text
命中关键词: 烤制
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=5
source: rerank_input

```text
命中关键词: 家常菜
菜品: 蛏抱蛋
分类: 水产
菜系: 闽菜
难度: 3.0
主要食材: 鸡蛋, 食用油, 鸡精
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 鸡精 (Ingredient): category: 调料
```

### pair_order=6
source: rerank_input

```text
命中关键词: 炖煮
菜品: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
主要食材: 番茄酱, 排骨, 姜片
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=7
source: rerank_input

```text
命中关键词: 炖煮
菜品: 红烧鲤鱼
分类: 水产
菜系: 鲁菜
难度: 4.0
主要食材: 蒜瓣, 清水, 盐
关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### pair_order=8
source: rerank_input

```text
命中关键词: 炖煮
菜品: 西红柿土豆炖牛肉
分类: 荤菜
难度: 4.0
主要食材: 油, 黑胡椒粉, 牛肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=9
source: rerank_input

```text
命中关键词: 炖煮
菜品: 台式卤肉饭
分类: 荤菜
菜系: 台湾菜
难度: 5.0
主要食材: 大蒜, 白胡椒粉, 五香粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### pair_order=10
source: rerank_input

```text
菜品: 乡村啤酒鸭
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸭肉清洗一遍放进锅中，加清水淹没鸭肉，加入20 ml料酒、1根大葱、拍散的2厘米生姜，开火烧滚，捞出浮沫，鸭肉捞出用清水洗净备用。
方法: 焯水,清洗
工具: 锅,漏勺
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 锅清洗后烧热，加入60 ml花生油，油温升至60℃时加入30颗花椒爆香。
方法: 加热,爆香
工具: 炒锅,锅铲
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 倒入鸭肉翻炒4分钟：2分钟后加入所有香料（草果、桂皮、八角、香叶、干辣椒），3分钟时加入料头（生姜、大蒜、小米辣）。
方法: 炒
工具: 炒锅,锅铲
时间: 4分钟

### 第4步
步骤: 步骤4
描述: 加入1000 ml啤酒，大火烧开后转小火炖煮30分钟。
方法: 炖煮
工具: 炒锅,锅盖
时间: 30分钟

### 第5步
步骤: 步骤5
描述: 炖煮10分钟时加入盐3克、生抽10 ml、老抽5 ml；20分钟时加入青椒和红椒段；29分钟时加入蒜苗段和剩余大葱段，翻炒1分钟后出锅。
方法: 调味,炖煮,炒
工具: 锅铲
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=11
source: rerank_input

```text
菜品: 血浆鸭
菜系: 湘菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜仔鸭肉切成约3cm小块，加料酒、姜片，去除血水。
方法: 切,腌制
工具: 刀,案板,盆
时间: 约10分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，放入腌制好的鲜鸭肉，不断翻炒。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），放入酒，再加入200ml开水，刚好淹没鸭肉即可，盖上锅盖中火煮15分钟。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第4步
步骤: 步骤4
描述: 水开之后，打开锅盖放入姜蒜，翻炒一遍，盖上锅盖持续加热10分钟。
方法: 炒,焖
工具: 炒锅,锅盖,锅铲
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 打开锅盖放入辣椒，不断翻炒，待至肉眼可见辣椒炒软，放入鲜鸭血，此时需要不断翻炒，确保每块鸭肉和每片辣椒都有鸭血的浸润。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第6步
步骤: 步骤6
描述: 翻炒至肉眼可见鸭血均为黑色，加入盐、鸡精、香葱，（喜欢食用山胡椒油的朋友也可以在此时放入3-6滴山胡椒油）再次翻炒一到二次即可。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第7步
步骤: 步骤7
描述: 出锅盛盘，上桌食用。
方法: 装盘
工具: 盘子
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### pair_order=12
source: rerank_input

```text
菜品: 湘祁米夫鸭
菜系: 湘菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将糯米粉、粘米粉、蒸肉粉、细辣椒粉、5克盐、白胡椒粉倒在一起搅匀，制成米粉混合物备用。
方法: 混合
工具: 盆
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 鸭子请摊主剁成适合蒸煮的块；姜切片，蒜剥皮；五花肉切片备用。
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第3步
步骤: 步骤3
描述: 热锅凉油，先煸炒五花肉出油，再加适量食用油烧热，放入鸭块煸炒。
方法: 炒
工具: 炒锅,锅铲
时间: 约3-5分钟

### 第4步
步骤: 步骤4
描述: 鸭肉煸炒至表皮焦黄变色，加入姜片、蒜瓣和剩余盐，继续炒出香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 关小火，倒入米粉混合物翻炒，使鸭肉均匀裹满米粉；少量多次加入开水，边加边翻炒，保持湿润。
方法: 炒
工具: 炒锅,锅铲
时间: 约3分钟

### 第6步
步骤: 步骤6
描述: 将裹好米粉的鸭肉装入碗中，放入高压锅，加水蒸20-25分钟（老鸭需60分钟以上）。
方法: 蒸
工具: 高压锅,碗
时间: 20-25分钟

### 第7步
步骤: 步骤7
描述: 出锅前撒葱花即可享用。
方法: 装饰
工具: 筷子
时间: 约10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=13
source: rerank_input

```text
菜系: 技巧知识
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### pair_order=14
source: rerank_input

```text
菜品: 麻婆豆腐
菜系: 川菜
## 所需食材
1. 五花肉(20g)
2. 内脂豆腐(1盒)
3. 咸鸭蛋(1枚)
4. 大蒜(2瓣)
5. 小米椒(5根)
6. 开水(适量ml)
7. 生姜(2片)
8. 花椒(20颗)
9. 酱油(10g)
10. 食用油(10ml)
11. 食盐(3g)
12. 香辣酱(5g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=15
source: rerank_input

```text
菜系: 技巧知识
## 块状肉类主食菜加工（此流程可选）（选项单选或多选）
### 块状肉类主食菜加工（此流程可选）（选项单选或多选）

用例：鱼肉、海蜇头、熟猪肉、熟禽类等

* 将食材通过蒸煮烤炸等方式熟制
* 将食材在凉水中泡上些许时间（犹适用于海产）
* 将食材撕成肉条
* 将食材切成薄片（犹适用于煮熟后的猪肉）
* 将食材切成 0.8cm * 0.8cm 截面长条状
* 将食材直接按部位撕碎或切大块（犹适用于整只熟禽）

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### pair_order=16
source: rerank_input

```text
分类: 烹饪技巧
技巧文档扩展上下文: 如何决策吃什么、凉拌
关键技巧内容:
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
## 计算方法
## 计算方法
## 计算荤菜和素菜数量
### 计算荤菜和素菜数量

* 菜的数量 = 人数 + 1。
* 荤菜比素菜多一个，或一样多即可。

由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
## 形式语言描述
#### 形式语言描述

当 有人数 `N` 时，
设 `素菜数` 为 `a`, `荤菜数`为 `b`。
`N`, `a`, `b`均为整数。

此时有下列不等式组：

* a + b = N + 1
* a ≤ b ≤ a+1

解得

```javascript
const a = Math.floor((N+1)/2);
const b = Math.ceil((N+1)/2);
```
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
## 凉拌的形态
### 凉拌的形态

凉拌可做成食材与辅料在空间上交混的形态
凉拌可做成食材与辅料在空间上分立的形态，此时辅料被称为蘸料
## 为什么凉拌
### 为什么凉拌

* 部分凉拌成菜时不需要热源
* 部分凉拌能减少洗锅的流程（不洗或仅过水即可）
* 凉拌能保留食材状态，此点特别展现在蔬菜、生肉上
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201003174, chunk_id=201003174_chunk_625, recipe_name=血浆鸭, category=荤菜, score=0.6822845935821533, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜仔鸭肉切成约3cm小块，加料酒、姜片，去除血水。
方法: 切,腌制
工具: 刀,案板,盆
时间: 约10分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，放入腌制好的鲜鸭肉，不断翻炒。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），放入酒，再加入200ml开水，刚好淹没鸭肉即可，盖上锅盖中火煮15分钟。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第4步
步骤: 步骤4
描述: 水开之后，打开锅盖放入姜蒜，翻炒一遍，盖上锅盖持续加热10分钟。
方法: 炒,焖
工具: 炒锅,锅盖,锅铲
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 打开锅盖放入辣椒，不断翻炒，待至肉眼可见辣椒炒软，放入鲜鸭血，此时需要不断翻炒，确保每块鸭肉和每片辣椒都有鸭血的浸润。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第6步
步骤: 步骤6
描述: 翻炒至肉眼可见鸭血均为黑色，加入盐、鸡精、香葱，（喜欢食用山胡椒油的朋友也可以在此时放入3-6滴山胡椒油）再次翻炒一到二次即可。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第7步
步骤: 步骤7
描述: 出锅盛盘，上桌食用。
方法: 装盘
工具: 盘子
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201002327, chunk_id=201002327_chunk_477, recipe_name=啤酒鸭, category=荤菜, score=0.6986643075942993, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 把鸭子切成3 cm小块，鸭肉冷水下锅，加姜片、料酒，焯一遍水，盛出沥干水分，备用。
方法: 切,焯水
工具: 刀,案板,锅
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，鸭肉入锅翻炒至上色。
方法: 炒
工具: 炒锅,锅铲
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），将鸭肉拨到锅的一边，倒入豆瓣酱和糖，小火翻炒出香味和糖色。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 加入丁香、八角、香叶、干辣椒、生抽、老抽、蒜，翻炒出香味。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第5步
步骤: 步骤5
描述: 倒入啤酒，没过鸭肉，加入盐、鸡精，然后中火将鸭子烧30分钟（牙口不好的话可以再多烧5分钟）。
方法: 炖
工具: 炒锅
时间: 30-35分钟

### 第6步
步骤: 步骤6
描述: 出锅盛盘，上桌食用。
方法: 盛盘
工具: 锅铲,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201001428, chunk_id=201001428_chunk_317, recipe_name=乡村啤酒鸭, category=荤菜, score=0.7047391533851624, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸭肉清洗一遍放进锅中，加清水淹没鸭肉，加入20 ml料酒、1根大葱、拍散的2厘米生姜，开火烧滚，捞出浮沫，鸭肉捞出用清水洗净备用。
方法: 焯水,清洗
工具: 锅,漏勺
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 锅清洗后烧热，加入60 ml花生油，油温升至60℃时加入30颗花椒爆香。
方法: 加热,爆香
工具: 炒锅,锅铲
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 倒入鸭肉翻炒4分钟：2分钟后加入所有香料（草果、桂皮、八角、香叶、干辣椒），3分钟时加入料头（生姜、大蒜、小米辣）。
方法: 炒
工具: 炒锅,锅铲
时间: 4分钟

### 第4步
步骤: 步骤4
描述: 加入1000 ml啤酒，大火烧开后转小火炖煮30分钟。
方法: 炖煮
工具: 炒锅,锅盖
时间: 30分钟

### 第5步
步骤: 步骤5
描述: 炖煮10分钟时加入盐3克、生抽10 ml、老抽5 ml；20分钟时加入青椒和红椒段；29分钟时加入蒜苗段和剩余大葱段，翻炒1分钟后出锅。
方法: 调味,炖煮,炒
工具: 锅铲
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201002857, chunk_id=201002857_chunk_565, recipe_name=湘祁米夫鸭, category=荤菜, score=0.6754992604255676, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将糯米粉、粘米粉、蒸肉粉、细辣椒粉、5克盐、白胡椒粉倒在一起搅匀，制成米粉混合物备用。
方法: 混合
工具: 盆
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 鸭子请摊主剁成适合蒸煮的块；姜切片，蒜剥皮；五花肉切片备用。
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第3步
步骤: 步骤3
描述: 热锅凉油，先煸炒五花肉出油，再加适量食用油烧热，放入鸭块煸炒。
方法: 炒
工具: 炒锅,锅铲
时间: 约3-5分钟

### 第4步
步骤: 步骤4
描述: 鸭肉煸炒至表皮焦黄变色，加入姜片、蒜瓣和剩余盐，继续炒出香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 关小火，倒入米粉混合物翻炒，使鸭肉均匀裹满米粉；少量多次加入开水，边加边翻炒，保持湿润。
方法: 炒
工具: 炒锅,锅铲
时间: 约3分钟

### 第6步
步骤: 步骤6
描述: 将裹好米粉的鸭肉装入碗中，放入高压锅，加水蒸20-25分钟（老鸭需60分钟以上）。
方法: 蒸
工具: 高压锅,碗
时间: 20-25分钟

### 第7步
步骤: 步骤7
描述: 出锅前撒葱花即可享用。
方法: 装饰
工具: 筷子
时间: 约10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6196181774139404, search_type=vector_enhanced

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=5
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipdoc_fd7f557c37a7, recipe_name=如何决策吃什么、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 如何决策吃什么、凉拌
关键技巧内容:
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
## 计算方法
## 计算方法
## 计算荤菜和素菜数量
### 计算荤菜和素菜数量

* 菜的数量 = 人数 + 1。
* 荤菜比素菜多一个，或一样多即可。

由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
## 形式语言描述
#### 形式语言描述

当 有人数 `N` 时，
设 `素菜数` 为 `a`, `荤菜数`为 `b`。
`N`, `a`, `b`均为整数。

此时有下列不等式组：

* a + b = N + 1
* a ≤ b ≤ a+1

解得

```javascript
const a = Math.floor((N+1)/2);
const b = Math.ceil((N+1)/2);
```
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
## 凉拌的形态
### 凉拌的形态

凉拌可做成食材与辅料在空间上交混的形态
凉拌可做成食材与辅料在空间上分立的形态，此时辅料被称为蘸料
## 为什么凉拌
### 为什么凉拌

* 部分凉拌成菜时不需要热源
* 部分凉拌能减少洗锅的流程（不洗或仅过水即可）
* 凉拌能保留食材状态，此点特别展现在蔬菜、生肉上
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201001429, recipe_name=鸭肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸭肉
食材名称: 鸭肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_683, recipe_name=麻婆豆腐, category=荤菜, score=0.5910249352455139, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(20g)
2. 内脂豆腐(1盒)
3. 咸鸭蛋(1枚)
4. 大蒜(2瓣)
5. 小米椒(5根)
6. 开水(适量ml)
7. 生姜(2片)
8. 花椒(20颗)
9. 酱油(10g)
10. 食用油(10ml)
11. 食盐(3g)
12. 香辣酱(5g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1321, recipe_name=凉拌, category=烹饪技巧, score=0.5863900184631348, search_type=vector_enhanced

```text
## 块状肉类主食菜加工（此流程可选）（选项单选或多选）
### 块状肉类主食菜加工（此流程可选）（选项单选或多选）

用例：鱼肉、海蜇头、熟猪肉、熟禽类等

* 将食材通过蒸煮烤炸等方式熟制
* 将食材在凉水中泡上些许时间（犹适用于海产）
* 将食材撕成肉条
* 将食材切成薄片（犹适用于煮熟后的猪肉）
* 将食材切成 0.8cm * 0.8cm 截面长条状
* 将食材直接按部位撕碎或切大块（犹适用于整只熟禽）

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=9
source: reranked_results
metadata_summary: node_id=201002282, recipe_name=台式卤肉饭, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 台式卤肉饭
分类: 荤菜
菜系: 台湾菜
难度: 5.0
主要食材: 大蒜, 白胡椒粉, 五香粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=10
source: reranked_results
metadata_summary: node_id=201002391, recipe_name=奶酪培根通心粉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 奶酪培根通心粉
分类: 荤菜
菜系: 美式
难度: 3.0
主要食材: 洋葱, 黄油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=11
source: reranked_results
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=12
source: reranked_results
metadata_summary: node_id=201003196, recipe_name=西红柿土豆炖牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 西红柿土豆炖牛肉
分类: 荤菜
难度: 4.0
主要食材: 油, 黑胡椒粉, 牛肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=13
source: reranked_results
metadata_summary: node_id=201002937, recipe_name=糖醋排骨, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
主要食材: 番茄酱, 排骨, 姜片
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=14
source: reranked_results
metadata_summary: node_id=201000411, recipe_name=蛏抱蛋, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 蛏抱蛋
分类: 水产
菜系: 闽菜
难度: 3.0
主要食材: 鸡蛋, 食用油, 鸡精
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 鸡精 (Ingredient): category: 调料
```

### result_order=15
source: reranked_results
metadata_summary: node_id=201000127, recipe_name=红烧鲤鱼, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 红烧鲤鱼
分类: 水产
菜系: 鲁菜
难度: 4.0
主要食材: 蒜瓣, 清水, 盐
关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### result_order=16
source: reranked_results
metadata_summary: node_id=201005492, recipe_name=烤茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 烤茄子
分类: 素菜
难度: 3.0
主要食材: 茄子, 食用油, 孜然
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201003174, chunk_id=201003174_chunk_625, recipe_name=血浆鸭, category=荤菜, score=0.6822845935821533, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜仔鸭肉切成约3cm小块，加料酒、姜片，去除血水。
方法: 切,腌制
工具: 刀,案板,盆
时间: 约10分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，放入腌制好的鲜鸭肉，不断翻炒。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），放入酒，再加入200ml开水，刚好淹没鸭肉即可，盖上锅盖中火煮15分钟。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第4步
步骤: 步骤4
描述: 水开之后，打开锅盖放入姜蒜，翻炒一遍，盖上锅盖持续加热10分钟。
方法: 炒,焖
工具: 炒锅,锅盖,锅铲
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 打开锅盖放入辣椒，不断翻炒，待至肉眼可见辣椒炒软，放入鲜鸭血，此时需要不断翻炒，确保每块鸭肉和每片辣椒都有鸭血的浸润。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第6步
步骤: 步骤6
描述: 翻炒至肉眼可见鸭血均为黑色，加入盐、鸡精、香葱，（喜欢食用山胡椒油的朋友也可以在此时放入3-6滴山胡椒油）再次翻炒一到二次即可。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第7步
步骤: 步骤7
描述: 出锅盛盘，上桌食用。
方法: 装盘
工具: 盘子
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201002327, chunk_id=201002327_chunk_477, recipe_name=啤酒鸭, category=荤菜, score=0.6986643075942993, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 把鸭子切成3 cm小块，鸭肉冷水下锅，加姜片、料酒，焯一遍水，盛出沥干水分，备用。
方法: 切,焯水
工具: 刀,案板,锅
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，鸭肉入锅翻炒至上色。
方法: 炒
工具: 炒锅,锅铲
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），将鸭肉拨到锅的一边，倒入豆瓣酱和糖，小火翻炒出香味和糖色。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 加入丁香、八角、香叶、干辣椒、生抽、老抽、蒜，翻炒出香味。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第5步
步骤: 步骤5
描述: 倒入啤酒，没过鸭肉，加入盐、鸡精，然后中火将鸭子烧30分钟（牙口不好的话可以再多烧5分钟）。
方法: 炖
工具: 炒锅
时间: 30-35分钟

### 第6步
步骤: 步骤6
描述: 出锅盛盘，上桌食用。
方法: 盛盘
工具: 锅铲,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6196181774139404, search_type=vector_enhanced

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=3
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipdoc_fd7f557c37a7, recipe_name=如何决策吃什么、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 如何决策吃什么、凉拌
关键技巧内容:
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
## 计算方法
## 计算方法
## 计算荤菜和素菜数量
### 计算荤菜和素菜数量

* 菜的数量 = 人数 + 1。
* 荤菜比素菜多一个，或一样多即可。

由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
## 形式语言描述
#### 形式语言描述

当 有人数 `N` 时，
设 `素菜数` 为 `a`, `荤菜数`为 `b`。
`N`, `a`, `b`均为整数。

此时有下列不等式组：

* a + b = N + 1
* a ≤ b ≤ a+1

解得

```javascript
const a = Math.floor((N+1)/2);
const b = Math.ceil((N+1)/2);
```
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
## 凉拌的形态
### 凉拌的形态

凉拌可做成食材与辅料在空间上交混的形态
凉拌可做成食材与辅料在空间上分立的形态，此时辅料被称为蘸料
## 为什么凉拌
### 为什么凉拌

* 部分凉拌成菜时不需要热源
* 部分凉拌能减少洗锅的流程（不洗或仅过水即可）
* 凉拌能保留食材状态，此点特别展现在蔬菜、生肉上
```

### result_order=4
source: top_k_final
metadata_summary: node_id=201001429, recipe_name=鸭肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸭肉
食材名称: 鸭肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201003174, chunk_id=201003174_chunk_625, recipe_name=血浆鸭, category=荤菜, score=0.6822845935821533, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜仔鸭肉切成约3cm小块，加料酒、姜片，去除血水。
方法: 切,腌制
工具: 刀,案板,盆
时间: 约10分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，放入腌制好的鲜鸭肉，不断翻炒。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），放入酒，再加入200ml开水，刚好淹没鸭肉即可，盖上锅盖中火煮15分钟。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第4步
步骤: 步骤4
描述: 水开之后，打开锅盖放入姜蒜，翻炒一遍，盖上锅盖持续加热10分钟。
方法: 炒,焖
工具: 炒锅,锅盖,锅铲
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 打开锅盖放入辣椒，不断翻炒，待至肉眼可见辣椒炒软，放入鲜鸭血，此时需要不断翻炒，确保每块鸭肉和每片辣椒都有鸭血的浸润。
方法: 炒
工具: 炒锅,锅铲
时间: 约5分钟

### 第6步
步骤: 步骤6
描述: 翻炒至肉眼可见鸭血均为黑色，加入盐、鸡精、香葱，（喜欢食用山胡椒油的朋友也可以在此时放入3-6滴山胡椒油）再次翻炒一到二次即可。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第7步
步骤: 步骤7
描述: 出锅盛盘，上桌食用。
方法: 装盘
工具: 盘子
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=1
source: generation_context
metadata_summary: node_id=201002327, chunk_id=201002327_chunk_477, recipe_name=啤酒鸭, category=荤菜, score=0.6986643075942993, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 把鸭子切成3 cm小块，鸭肉冷水下锅，加姜片、料酒，焯一遍水，盛出沥干水分，备用。
方法: 切,焯水
工具: 刀,案板,锅
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 炒锅烧热，放入约100ml食用油，大火待油烧开，鸭肉入锅翻炒至上色。
方法: 炒
工具: 炒锅,锅铲
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 待鸭肉完全变色（肉眼可见泛白），将鸭肉拨到锅的一边，倒入豆瓣酱和糖，小火翻炒出香味和糖色。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 加入丁香、八角、香叶、干辣椒、生抽、老抽、蒜，翻炒出香味。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第5步
步骤: 步骤5
描述: 倒入啤酒，没过鸭肉，加入盐、鸡精，然后中火将鸭子烧30分钟（牙口不好的话可以再多烧5分钟）。
方法: 炖
工具: 炒锅
时间: 30-35分钟

### 第6步
步骤: 步骤6
描述: 出锅盛盘，上桌食用。
方法: 盛盘
工具: 锅铲,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: generation_context
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6196181774139404, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=3
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipdoc_fd7f557c37a7, recipe_name=如何决策吃什么、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

```text
技巧文档扩展上下文: 如何决策吃什么、凉拌
关键技巧内容:
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
## 计算方法
## 计算方法
## 计算荤菜和素菜数量
### 计算荤菜和素菜数量

* 菜的数量 = 人数 + 1。
* 荤菜比素菜多一个，或一样多即可。

由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
## 形式语言描述
#### 形式语言描述

当 有人数 `N` 时，
设 `素菜数` 为 `a`, `荤菜数`为 `b`。
`N`, `a`, `b`均为整数。

此时有下列不等式组：

* a + b = N + 1
* a ≤ b ≤ a+1

解得

```javascript
const a = Math.floor((N+1)/2);
const b = Math.ceil((N+1)/2);
```
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
## 凉拌的形态
### 凉拌的形态

凉拌可做成食材与辅料在空间上交混的形态
凉拌可做成食材与辅料在空间上分立的形态，此时辅料被称为蘸料
## 为什么凉拌
### 为什么凉拌

* 部分凉拌成菜时不需要热源
* 部分凉拌能减少洗锅的流程（不洗或仅过水即可）
* 凉拌能保留食材状态，此点特别展现在蔬菜、生肉上
```

### result_order=4
source: generation_context
metadata_summary: node_id=201001429, recipe_name=鸭肉, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

```text
命中关键词: 鸭肉
食材名称: 鸭肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

