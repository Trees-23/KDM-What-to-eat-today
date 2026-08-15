# Recall Content

audit_id: 20260811_165217_029_2b04ff4e
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201004766, recipe_name=豆角焖面, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆角焖面
菜品名称: 豆角焖面
分类: 主食
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=1
source: entity_level
metadata_summary: node_id=201004769, recipe_name=豆角, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆角
食材名称: 豆角
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
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

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201004766, chunk_id=201004766_chunk_945, recipe_name=豆角焖面, category=主食, score=0.7768505811691284, search_type=vector_enhanced

```text
# 豆角焖面
难度: 3.0星

时间信息: 准备时间: 约10分钟, 烹饪时间: 约15分钟
份量: 1人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201004766, chunk_id=201004766_chunk_947, recipe_name=豆角焖面, category=主食, score=0.7160660028457642, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将豆角切成5-6 cm的小段。
方法: 切
工具: 菜刀,砧板

### 第2步
步骤: 步骤2
描述: 将葱切成1-2 cm小段；姜切成1 mm×1 mm×3 cm长条；蒜拍碎后切成1 mm粒度；五花肉切成2 mm厚片。
方法: 切
工具: 菜刀,砧板

### 第3步
步骤: 步骤3
描述: 锅烧热至手放锅上方10 cm处明显烤手，倒入10-18 ml食用油，摇晃锅使油挂满锅底三分之二。
方法: 加热,倒油
工具: 炒锅

### 第4步
步骤: 步骤4
描述: 放入全部姜和葱段，爆香5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒

### 第5步
步骤: 步骤5
描述: 放入全部肉片，静置5秒后翻炒，使肉片均匀裹油。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒+

### 第6步
步骤: 步骤6
描述: 肉片全部变色后，沿锅边淋入生抽，翻炒均匀。
方法: 炒,淋
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 依次加入盐、老抽、耗油、十三香、鸡精及全部豆角，翻炒2分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 加入150 ml热水，水开后舀出一半菜汤备用。
方法: 煮
工具: 炒锅,勺子

### 第9步
步骤: 步骤9
描述: 将面条平铺在菜上，盖盖中火焖5分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 5分钟

### 第10步
步骤: 步骤10
描述: 打开锅盖，将之前舀出的菜汤每次一勺均匀撒在面条上，再盖盖中火焖3分钟。
方法: 焖
工具: 炒锅,锅盖,勺子
时间: 3分钟

### 第11步
步骤: 步骤11
描述: 开盖后撒入全部蒜和味精，用筷子翻炒均匀即可关火。
方法: 炒
工具: 炒锅,筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201005226, chunk_id=201005226_chunk_1037, recipe_name=陕北熬豆角, category=素菜, score=0.6765478253364563, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，姜切丝，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 豆角去筋，切2-10cm小段，备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 土豆去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第4步
步骤: 步骤4
描述: 西红柿去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 辣椒去仔，切0.15cm宽条，备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱姜蒜，翻炒至闻到葱姜蒜香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 加入豆角，翻炒至变色（青绿色变为翠绿色）。
方法: 炒
工具: 锅铲
时间: 约2分钟

### 第8步
步骤: 步骤8
描述: 加入土豆块，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第9步
步骤: 步骤9
描述: 加入热水（水面刚刚漫过菜），盖上锅盖熬至土豆变软（可以用筷子确认）。
方法: 熬,煮
工具: 炒锅,锅盖,筷子
时间: 约10-12分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿块，加入盐、生抽、蚝油、五香粉、辣椒，熬至西红柿成汁（注意搅拌，防止糊锅）。
方法: 熬,搅拌
工具: 锅铲
时间: 约3-5分钟

### 第11步
步骤: 步骤11
描述: 加入香菜碎，出锅。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_998, recipe_name=素炒豆角, category=素菜, score=0.6725745797157288, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生抽、老抽、耗油、盐混合调料汁，备用。
方法: 混合
工具: 碗或盆

### 第3步
步骤: 步骤3
描述: 小米椒切圈，备用。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 豆角去筋，45°斜切4-10cm小段，备用。
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱、小米椒，翻炒至闻到香味。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 加入豆角，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入料汁，开大火翻炒2分钟。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 倒入150ml水，转中小火，盖上锅盖焖制8-10分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 8-10分钟

### 第9步
步骤: 步骤9
描述: 加入蒜切沫，出锅。
方法: 炒
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201003025, chunk_id=201003025_chunk_595, recipe_name=羊排焖面, category=荤菜, score=0.6465954780578613, search_type=vector_enhanced

```text
# 羊排焖面

菜系: 西北菜
难度: 4.0星

时间信息: 准备时间: 约20分钟（切配、焯水、和面）, 烹饪时间: 约50分钟（炖煮30分钟+焖面4分钟+其他炒制）
份量: 2人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_999, recipe_name=素炒豆角, category=素菜, score=0.6425701379776001, search_type=vector_enhanced

```text
## 标签
切豆角需要一定刀工，不会的可用剪刀
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201004746, chunk_id=201004746_chunk_943, recipe_name=西红柿鸡蛋挂面, category=主食, score=0.6414397358894348, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 小葱洗净并切成葱花；西红柿切块；青椒切成菱形块；鸡蛋打入碗中打散，如腥味重可加2g白醋去腥。
方法: 切
工具: 刀,案板,碗
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 起锅烧热，倒入15-20g食用油，油温七成热时倒入蛋液快速划散，炒至凝固后盛出备用，留底油。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 锅中留底油，下葱白、蒜末炒香，加入西红柿块和青椒翻炒出汁，加入酱油5g、白砂糖2g，翻炒十几秒后加一碗清水，煮沸后加入炒好的鸡蛋、蚝油5g（或鸡精2g）提鲜，中小火收汁，期间搅拌防粘，收汁完成后撒葱花、淋香油，制成西红柿鸡蛋臊子。
方法: 炒,煮,收汁
工具: 炒锅,锅铲
时间: 7分钟

### 第4步
步骤: 步骤4
描述: 锅中加清水500ml煮沸，下挂面，煮软后加入100ml清水，再次煮沸后再加100ml清水，重复2-3次，面条两侧呈透明状即熟，捞出放入臊子碗中拌匀即可。
方法: 煮
工具: 锅,筷子
时间: 6分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_818, recipe_name=炸酱面, category=主食, score=0.6380012631416321, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菜码切丝备用。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 葱切碎。油锅烧热，下葱和肉，炒至肉完全熟透（无红色）。
方法: 切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 下豆瓣酱和甜面酱，继续炒至微微粘稠。盛出，得到炸酱。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 取大碗，加凉水备用。
工具: 大碗
时间: 30秒

### 第5步
步骤: 步骤5
描述: 煮面条至断生（无白芯），盛入第4步装有凉水的碗中。
方法: 煮
工具: 锅,筷子
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 立即控水捞出，盛入干净的碗中。
方法: 捞
工具: 筷子,漏勺
时间: 30秒

### 第7步
步骤: 步骤7
描述: 取第3步炸酱，倒入碗中，拌匀。然后取第1步菜码，倒入碗中，拌匀。
方法: 拌
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_996, recipe_name=素炒豆角, category=素菜, score=0.6344062685966492, search_type=vector_enhanced

```text
# 素炒豆角
难度: 2.0星

时间信息: 准备时间: 约10分钟, 烹饪时间: 约11-12分钟
份量: 2人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201004466, chunk_id=201004466_chunk_890, recipe_name=意式肉酱面, category=主食, score=0.6314668655395508, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅中加水，烧开后放入意面，按包装时间煮 6-12 分钟
方法: 煮
工具: 锅
时间: 6-12分钟

### 第2步
步骤: 步骤2
描述: 洋葱切成小丁
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 空锅中倒油，中火下入洋葱碎，持续搅拌至洋葱半透明
方法: 炒,搅拌
工具: 锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 下入肉沫，继续搅拌搅散，炒至肉末变棕色
方法: 炒,搅拌
工具: 锅,锅铲
时间: 约3分钟

### 第5步
步骤: 步骤5
描述: 加入意大利面酱，稍微搅拌均匀
方法: 搅拌
工具: 锅,锅铲
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 将煮好的意面沥干水分，倒入肉酱中搅拌均匀即可
方法: 搅拌
工具: 漏勺,锅,锅铲
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201004766, recipe_name=豆角焖面, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆角焖面
菜品名称: 豆角焖面
分类: 主食
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201004769, recipe_name=豆角, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆角
食材名称: 豆角
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
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
source: branch_grouped
metadata_summary: node_id=201004766, chunk_id=201004766_chunk_945, recipe_name=豆角焖面, category=主食, score=0.7768505811691284, search_type=vector_enhanced

```text
# 豆角焖面
难度: 3.0星

时间信息: 准备时间: 约10分钟, 烹饪时间: 约15分钟
份量: 1人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201004766, chunk_id=201004766_chunk_947, recipe_name=豆角焖面, category=主食, score=0.7160660028457642, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将豆角切成5-6 cm的小段。
方法: 切
工具: 菜刀,砧板

### 第2步
步骤: 步骤2
描述: 将葱切成1-2 cm小段；姜切成1 mm×1 mm×3 cm长条；蒜拍碎后切成1 mm粒度；五花肉切成2 mm厚片。
方法: 切
工具: 菜刀,砧板

### 第3步
步骤: 步骤3
描述: 锅烧热至手放锅上方10 cm处明显烤手，倒入10-18 ml食用油，摇晃锅使油挂满锅底三分之二。
方法: 加热,倒油
工具: 炒锅

### 第4步
步骤: 步骤4
描述: 放入全部姜和葱段，爆香5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒

### 第5步
步骤: 步骤5
描述: 放入全部肉片，静置5秒后翻炒，使肉片均匀裹油。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒+

### 第6步
步骤: 步骤6
描述: 肉片全部变色后，沿锅边淋入生抽，翻炒均匀。
方法: 炒,淋
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 依次加入盐、老抽、耗油、十三香、鸡精及全部豆角，翻炒2分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 加入150 ml热水，水开后舀出一半菜汤备用。
方法: 煮
工具: 炒锅,勺子

### 第9步
步骤: 步骤9
描述: 将面条平铺在菜上，盖盖中火焖5分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 5分钟

### 第10步
步骤: 步骤10
描述: 打开锅盖，将之前舀出的菜汤每次一勺均匀撒在面条上，再盖盖中火焖3分钟。
方法: 焖
工具: 炒锅,锅盖,勺子
时间: 3分钟

### 第11步
步骤: 步骤11
描述: 开盖后撒入全部蒜和味精，用筷子翻炒均匀即可关火。
方法: 炒
工具: 炒锅,筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201005226, chunk_id=201005226_chunk_1037, recipe_name=陕北熬豆角, category=素菜, score=0.6765478253364563, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，姜切丝，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 豆角去筋，切2-10cm小段，备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 土豆去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第4步
步骤: 步骤4
描述: 西红柿去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 辣椒去仔，切0.15cm宽条，备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱姜蒜，翻炒至闻到葱姜蒜香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 加入豆角，翻炒至变色（青绿色变为翠绿色）。
方法: 炒
工具: 锅铲
时间: 约2分钟

### 第8步
步骤: 步骤8
描述: 加入土豆块，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第9步
步骤: 步骤9
描述: 加入热水（水面刚刚漫过菜），盖上锅盖熬至土豆变软（可以用筷子确认）。
方法: 熬,煮
工具: 炒锅,锅盖,筷子
时间: 约10-12分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿块，加入盐、生抽、蚝油、五香粉、辣椒，熬至西红柿成汁（注意搅拌，防止糊锅）。
方法: 熬,搅拌
工具: 锅铲
时间: 约3-5分钟

### 第11步
步骤: 步骤11
描述: 加入香菜碎，出锅。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_998, recipe_name=素炒豆角, category=素菜, score=0.6725745797157288, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生抽、老抽、耗油、盐混合调料汁，备用。
方法: 混合
工具: 碗或盆

### 第3步
步骤: 步骤3
描述: 小米椒切圈，备用。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 豆角去筋，45°斜切4-10cm小段，备用。
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱、小米椒，翻炒至闻到香味。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 加入豆角，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入料汁，开大火翻炒2分钟。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 倒入150ml水，转中小火，盖上锅盖焖制8-10分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 8-10分钟

### 第9步
步骤: 步骤9
描述: 加入蒜切沫，出锅。
方法: 炒
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201003025, chunk_id=201003025_chunk_595, recipe_name=羊排焖面, category=荤菜, score=0.6465954780578613, search_type=vector_enhanced

```text
# 羊排焖面

菜系: 西北菜
难度: 4.0星

时间信息: 准备时间: 约20分钟（切配、焯水、和面）, 烹饪时间: 约50分钟（炖煮30分钟+焖面4分钟+其他炒制）
份量: 2人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_999, recipe_name=素炒豆角, category=素菜, score=0.6425701379776001, search_type=vector_enhanced

```text
## 标签
切豆角需要一定刀工，不会的可用剪刀
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201004746, chunk_id=201004746_chunk_943, recipe_name=西红柿鸡蛋挂面, category=主食, score=0.6414397358894348, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 小葱洗净并切成葱花；西红柿切块；青椒切成菱形块；鸡蛋打入碗中打散，如腥味重可加2g白醋去腥。
方法: 切
工具: 刀,案板,碗
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 起锅烧热，倒入15-20g食用油，油温七成热时倒入蛋液快速划散，炒至凝固后盛出备用，留底油。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 锅中留底油，下葱白、蒜末炒香，加入西红柿块和青椒翻炒出汁，加入酱油5g、白砂糖2g，翻炒十几秒后加一碗清水，煮沸后加入炒好的鸡蛋、蚝油5g（或鸡精2g）提鲜，中小火收汁，期间搅拌防粘，收汁完成后撒葱花、淋香油，制成西红柿鸡蛋臊子。
方法: 炒,煮,收汁
工具: 炒锅,锅铲
时间: 7分钟

### 第4步
步骤: 步骤4
描述: 锅中加清水500ml煮沸，下挂面，煮软后加入100ml清水，再次煮沸后再加100ml清水，重复2-3次，面条两侧呈透明状即熟，捞出放入臊子碗中拌匀即可。
方法: 煮
工具: 锅,筷子
时间: 6分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_818, recipe_name=炸酱面, category=主食, score=0.6380012631416321, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菜码切丝备用。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 葱切碎。油锅烧热，下葱和肉，炒至肉完全熟透（无红色）。
方法: 切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 下豆瓣酱和甜面酱，继续炒至微微粘稠。盛出，得到炸酱。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 取大碗，加凉水备用。
工具: 大碗
时间: 30秒

### 第5步
步骤: 步骤5
描述: 煮面条至断生（无白芯），盛入第4步装有凉水的碗中。
方法: 煮
工具: 锅,筷子
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 立即控水捞出，盛入干净的碗中。
方法: 捞
工具: 筷子,漏勺
时间: 30秒

### 第7步
步骤: 步骤7
描述: 取第3步炸酱，倒入碗中，拌匀。然后取第1步菜码，倒入碗中，拌匀。
方法: 拌
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_996, recipe_name=素炒豆角, category=素菜, score=0.6344062685966492, search_type=vector_enhanced

```text
# 素炒豆角
难度: 2.0星

时间信息: 准备时间: 约10分钟, 烹饪时间: 约11-12分钟
份量: 2人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201004466, chunk_id=201004466_chunk_890, recipe_name=意式肉酱面, category=主食, score=0.6314668655395508, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅中加水，烧开后放入意面，按包装时间煮 6-12 分钟
方法: 煮
工具: 锅
时间: 6-12分钟

### 第2步
步骤: 步骤2
描述: 洋葱切成小丁
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 空锅中倒油，中火下入洋葱碎，持续搅拌至洋葱半透明
方法: 炒,搅拌
工具: 锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 下入肉沫，继续搅拌搅散，炒至肉末变棕色
方法: 炒,搅拌
工具: 锅,锅铲
时间: 约3分钟

### 第5步
步骤: 步骤5
描述: 加入意大利面酱，稍微搅拌均匀
方法: 搅拌
工具: 锅,锅铲
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 将煮好的意面沥干水分，倒入肉酱中搅拌均匀即可
方法: 搅拌
工具: 漏勺,锅,锅铲
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201004766, chunk_id=201004766_chunk_947, recipe_name=豆角焖面, category=主食, score=0.7160660028457642, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将豆角切成5-6 cm的小段。
方法: 切
工具: 菜刀,砧板

### 第2步
步骤: 步骤2
描述: 将葱切成1-2 cm小段；姜切成1 mm×1 mm×3 cm长条；蒜拍碎后切成1 mm粒度；五花肉切成2 mm厚片。
方法: 切
工具: 菜刀,砧板

### 第3步
步骤: 步骤3
描述: 锅烧热至手放锅上方10 cm处明显烤手，倒入10-18 ml食用油，摇晃锅使油挂满锅底三分之二。
方法: 加热,倒油
工具: 炒锅

### 第4步
步骤: 步骤4
描述: 放入全部姜和葱段，爆香5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒

### 第5步
步骤: 步骤5
描述: 放入全部肉片，静置5秒后翻炒，使肉片均匀裹油。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒+

### 第6步
步骤: 步骤6
描述: 肉片全部变色后，沿锅边淋入生抽，翻炒均匀。
方法: 炒,淋
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 依次加入盐、老抽、耗油、十三香、鸡精及全部豆角，翻炒2分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 加入150 ml热水，水开后舀出一半菜汤备用。
方法: 煮
工具: 炒锅,勺子

### 第9步
步骤: 步骤9
描述: 将面条平铺在菜上，盖盖中火焖5分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 5分钟

### 第10步
步骤: 步骤10
描述: 打开锅盖，将之前舀出的菜汤每次一勺均匀撒在面条上，再盖盖中火焖3分钟。
方法: 焖
工具: 炒锅,锅盖,勺子
时间: 3分钟

### 第11步
步骤: 步骤11
描述: 开盖后撒入全部蒜和味精，用筷子翻炒均匀即可关火。
方法: 炒
工具: 炒锅,筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201004769, recipe_name=豆角, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆角
食材名称: 豆角
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
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
source: merged_candidates
metadata_summary: node_id=201005226, chunk_id=201005226_chunk_1037, recipe_name=陕北熬豆角, category=素菜, score=0.6765478253364563, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，姜切丝，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 豆角去筋，切2-10cm小段，备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 土豆去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第4步
步骤: 步骤4
描述: 西红柿去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 辣椒去仔，切0.15cm宽条，备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱姜蒜，翻炒至闻到葱姜蒜香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 加入豆角，翻炒至变色（青绿色变为翠绿色）。
方法: 炒
工具: 锅铲
时间: 约2分钟

### 第8步
步骤: 步骤8
描述: 加入土豆块，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第9步
步骤: 步骤9
描述: 加入热水（水面刚刚漫过菜），盖上锅盖熬至土豆变软（可以用筷子确认）。
方法: 熬,煮
工具: 炒锅,锅盖,筷子
时间: 约10-12分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿块，加入盐、生抽、蚝油、五香粉、辣椒，熬至西红柿成汁（注意搅拌，防止糊锅）。
方法: 熬,搅拌
工具: 锅铲
时间: 约3-5分钟

### 第11步
步骤: 步骤11
描述: 加入香菜碎，出锅。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_998, recipe_name=素炒豆角, category=素菜, score=0.6725745797157288, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生抽、老抽、耗油、盐混合调料汁，备用。
方法: 混合
工具: 碗或盆

### 第3步
步骤: 步骤3
描述: 小米椒切圈，备用。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 豆角去筋，45°斜切4-10cm小段，备用。
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱、小米椒，翻炒至闻到香味。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 加入豆角，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入料汁，开大火翻炒2分钟。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 倒入150ml水，转中小火，盖上锅盖焖制8-10分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 8-10分钟

### 第9步
步骤: 步骤9
描述: 加入蒜切沫，出锅。
方法: 炒
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=201003025, chunk_id=201003025_chunk_595, recipe_name=羊排焖面, category=荤菜, score=0.6465954780578613, search_type=vector_enhanced

```text
# 羊排焖面

菜系: 西北菜
难度: 4.0星

时间信息: 准备时间: 约20分钟（切配、焯水、和面）, 烹饪时间: 约50分钟（炖煮30分钟+焖面4分钟+其他炒制）
份量: 2人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201004746, chunk_id=201004746_chunk_943, recipe_name=西红柿鸡蛋挂面, category=主食, score=0.6414397358894348, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 小葱洗净并切成葱花；西红柿切块；青椒切成菱形块；鸡蛋打入碗中打散，如腥味重可加2g白醋去腥。
方法: 切
工具: 刀,案板,碗
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 起锅烧热，倒入15-20g食用油，油温七成热时倒入蛋液快速划散，炒至凝固后盛出备用，留底油。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 锅中留底油，下葱白、蒜末炒香，加入西红柿块和青椒翻炒出汁，加入酱油5g、白砂糖2g，翻炒十几秒后加一碗清水，煮沸后加入炒好的鸡蛋、蚝油5g（或鸡精2g）提鲜，中小火收汁，期间搅拌防粘，收汁完成后撒葱花、淋香油，制成西红柿鸡蛋臊子。
方法: 炒,煮,收汁
工具: 炒锅,锅铲
时间: 7分钟

### 第4步
步骤: 步骤4
描述: 锅中加清水500ml煮沸，下挂面，煮软后加入100ml清水，再次煮沸后再加100ml清水，重复2-3次，面条两侧呈透明状即熟，捞出放入臊子碗中拌匀即可。
方法: 煮
工具: 锅,筷子
时间: 6分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_818, recipe_name=炸酱面, category=主食, score=0.6380012631416321, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菜码切丝备用。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 葱切碎。油锅烧热，下葱和肉，炒至肉完全熟透（无红色）。
方法: 切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 下豆瓣酱和甜面酱，继续炒至微微粘稠。盛出，得到炸酱。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 取大碗，加凉水备用。
工具: 大碗
时间: 30秒

### 第5步
步骤: 步骤5
描述: 煮面条至断生（无白芯），盛入第4步装有凉水的碗中。
方法: 煮
工具: 锅,筷子
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 立即控水捞出，盛入干净的碗中。
方法: 捞
工具: 筷子,漏勺
时间: 30秒

### 第7步
步骤: 步骤7
描述: 取第3步炸酱，倒入碗中，拌匀。然后取第1步菜码，倒入碗中，拌匀。
方法: 拌
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=201004466, chunk_id=201004466_chunk_890, recipe_name=意式肉酱面, category=主食, score=0.6314668655395508, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅中加水，烧开后放入意面，按包装时间煮 6-12 分钟
方法: 煮
工具: 锅
时间: 6-12分钟

### 第2步
步骤: 步骤2
描述: 洋葱切成小丁
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 空锅中倒油，中火下入洋葱碎，持续搅拌至洋葱半透明
方法: 炒,搅拌
工具: 锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 下入肉沫，继续搅拌搅散，炒至肉末变棕色
方法: 炒,搅拌
工具: 锅,锅铲
时间: 约3分钟

### 第5步
步骤: 步骤5
描述: 加入意大利面酱，稍微搅拌均匀
方法: 搅拌
工具: 锅,锅铲
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 将煮好的意面沥干水分，倒入肉酱中搅拌均匀即可
方法: 搅拌
工具: 漏勺,锅,锅铲
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
菜品: 豆角焖面
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将豆角切成5-6 cm的小段。
方法: 切
工具: 菜刀,砧板

### 第2步
步骤: 步骤2
描述: 将葱切成1-2 cm小段；姜切成1 mm×1 mm×3 cm长条；蒜拍碎后切成1 mm粒度；五花肉切成2 mm厚片。
方法: 切
工具: 菜刀,砧板

### 第3步
步骤: 步骤3
描述: 锅烧热至手放锅上方10 cm处明显烤手，倒入10-18 ml食用油，摇晃锅使油挂满锅底三分之二。
方法: 加热,倒油
工具: 炒锅

### 第4步
步骤: 步骤4
描述: 放入全部姜和葱段，爆香5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒

### 第5步
步骤: 步骤5
描述: 放入全部肉片，静置5秒后翻炒，使肉片均匀裹油。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒+

### 第6步
步骤: 步骤6
描述: 肉片全部变色后，沿锅边淋入生抽，翻炒均匀。
方法: 炒,淋
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 依次加入盐、老抽、耗油、十三香、鸡精及全部豆角，翻炒2分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 加入150 ml热水，水开后舀出一半菜汤备用。
方法: 煮
工具: 炒锅,勺子

### 第9步
步骤: 步骤9
描述: 将面条平铺在菜上，盖盖中火焖5分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 5分钟

### 第10步
步骤: 步骤10
描述: 打开锅盖，将之前舀出的菜汤每次一勺均匀撒在面条上，再盖盖中火焖3分钟。
方法: 焖
工具: 炒锅,锅盖,勺子
时间: 3分钟

### 第11步
步骤: 步骤11
描述: 开盖后撒入全部蒜和味精，用筷子翻炒均匀即可关火。
方法: 炒
工具: 炒锅,筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BEL
```

### pair_order=1
source: rerank_input

```text
命中关键词: 豆角
食材名称: 豆角
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
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

### pair_order=4
source: rerank_input

```text
菜品: 陕北熬豆角
菜系: 西北菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，姜切丝，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 豆角去筋，切2-10cm小段，备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 土豆去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第4步
步骤: 步骤4
描述: 西红柿去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 辣椒去仔，切0.15cm宽条，备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱姜蒜，翻炒至闻到葱姜蒜香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 加入豆角，翻炒至变色（青绿色变为翠绿色）。
方法: 炒
工具: 锅铲
时间: 约2分钟

### 第8步
步骤: 步骤8
描述: 加入土豆块，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第9步
步骤: 步骤9
描述: 加入热水（水面刚刚漫过菜），盖上锅盖熬至土豆变软（可以用筷子确认）。
方法: 熬,煮
工具: 炒锅,锅盖,筷子
时间: 约10-12分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿块，加入盐、生抽、蚝油、五香粉、辣椒，熬至西红柿成汁（注意搅拌，防止糊锅）。
方法: 熬,搅拌
工具: 锅铲
时间: 约3-5分钟

### 第11步
步骤: 步骤11
描述: 加入香菜碎，出锅。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 
```

### pair_order=5
source: rerank_input

```text
菜品: 素炒豆角
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生抽、老抽、耗油、盐混合调料汁，备用。
方法: 混合
工具: 碗或盆

### 第3步
步骤: 步骤3
描述: 小米椒切圈，备用。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 豆角去筋，45°斜切4-10cm小段，备用。
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱、小米椒，翻炒至闻到香味。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 加入豆角，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入料汁，开大火翻炒2分钟。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 倒入150ml水，转中小火，盖上锅盖焖制8-10分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 8-10分钟

### 第9步
步骤: 步骤9
描述: 加入蒜切沫，出锅。
方法: 炒
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=6
source: rerank_input

```text
# 羊排焖面

菜系: 西北菜
难度: 4.0星

时间信息: 准备时间: 约20分钟（切配、焯水、和面）, 烹饪时间: 约50分钟（炖煮30分钟+焖面4分钟+其他炒制）
份量: 2人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=7
source: rerank_input

```text
菜品: 西红柿鸡蛋挂面
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 小葱洗净并切成葱花；西红柿切块；青椒切成菱形块；鸡蛋打入碗中打散，如腥味重可加2g白醋去腥。
方法: 切
工具: 刀,案板,碗
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 起锅烧热，倒入15-20g食用油，油温七成热时倒入蛋液快速划散，炒至凝固后盛出备用，留底油。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 锅中留底油，下葱白、蒜末炒香，加入西红柿块和青椒翻炒出汁，加入酱油5g、白砂糖2g，翻炒十几秒后加一碗清水，煮沸后加入炒好的鸡蛋、蚝油5g（或鸡精2g）提鲜，中小火收汁，期间搅拌防粘，收汁完成后撒葱花、淋香油，制成西红柿鸡蛋臊子。
方法: 炒,煮,收汁
工具: 炒锅,锅铲
时间: 7分钟

### 第4步
步骤: 步骤4
描述: 锅中加清水500ml煮沸，下挂面，煮软后加入100ml清水，再次煮沸后再加100ml清水，重复2-3次，面条两侧呈透明状即熟，捞出放入臊子碗中拌匀即可。
方法: 煮
工具: 锅,筷子
时间: 6分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=8
source: rerank_input

```text
菜品: 炸酱面
菜系: 鲁菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菜码切丝备用。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 葱切碎。油锅烧热，下葱和肉，炒至肉完全熟透（无红色）。
方法: 切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 下豆瓣酱和甜面酱，继续炒至微微粘稠。盛出，得到炸酱。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 取大碗，加凉水备用。
工具: 大碗
时间: 30秒

### 第5步
步骤: 步骤5
描述: 煮面条至断生（无白芯），盛入第4步装有凉水的碗中。
方法: 煮
工具: 锅,筷子
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 立即控水捞出，盛入干净的碗中。
方法: 捞
工具: 筷子,漏勺
时间: 30秒

### 第7步
步骤: 步骤7
描述: 取第3步炸酱，倒入碗中，拌匀。然后取第1步菜码，倒入碗中，拌匀。
方法: 拌
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=9
source: rerank_input

```text
菜品: 意式肉酱面
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅中加水，烧开后放入意面，按包装时间煮 6-12 分钟
方法: 煮
工具: 锅
时间: 6-12分钟

### 第2步
步骤: 步骤2
描述: 洋葱切成小丁
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 空锅中倒油，中火下入洋葱碎，持续搅拌至洋葱半透明
方法: 炒,搅拌
工具: 锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 下入肉沫，继续搅拌搅散，炒至肉末变棕色
方法: 炒,搅拌
工具: 锅,锅铲
时间: 约3分钟

### 第5步
步骤: 步骤5
描述: 加入意大利面酱，稍微搅拌均匀
方法: 搅拌
工具: 锅,锅铲
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 将煮好的意面沥干水分，倒入肉酱中搅拌均匀即可
方法: 搅拌
工具: 漏勺,锅,锅铲
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201004766, chunk_id=201004766_chunk_947, recipe_name=豆角焖面, category=主食, score=0.7160660028457642, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将豆角切成5-6 cm的小段。
方法: 切
工具: 菜刀,砧板

### 第2步
步骤: 步骤2
描述: 将葱切成1-2 cm小段；姜切成1 mm×1 mm×3 cm长条；蒜拍碎后切成1 mm粒度；五花肉切成2 mm厚片。
方法: 切
工具: 菜刀,砧板

### 第3步
步骤: 步骤3
描述: 锅烧热至手放锅上方10 cm处明显烤手，倒入10-18 ml食用油，摇晃锅使油挂满锅底三分之二。
方法: 加热,倒油
工具: 炒锅

### 第4步
步骤: 步骤4
描述: 放入全部姜和葱段，爆香5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒

### 第5步
步骤: 步骤5
描述: 放入全部肉片，静置5秒后翻炒，使肉片均匀裹油。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒+

### 第6步
步骤: 步骤6
描述: 肉片全部变色后，沿锅边淋入生抽，翻炒均匀。
方法: 炒,淋
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 依次加入盐、老抽、耗油、十三香、鸡精及全部豆角，翻炒2分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 加入150 ml热水，水开后舀出一半菜汤备用。
方法: 煮
工具: 炒锅,勺子

### 第9步
步骤: 步骤9
描述: 将面条平铺在菜上，盖盖中火焖5分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 5分钟

### 第10步
步骤: 步骤10
描述: 打开锅盖，将之前舀出的菜汤每次一勺均匀撒在面条上，再盖盖中火焖3分钟。
方法: 焖
工具: 炒锅,锅盖,勺子
时间: 3分钟

### 第11步
步骤: 步骤11
描述: 开盖后撒入全部蒜和味精，用筷子翻炒均匀即可关火。
方法: 炒
工具: 炒锅,筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_998, recipe_name=素炒豆角, category=素菜, score=0.6725745797157288, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生抽、老抽、耗油、盐混合调料汁，备用。
方法: 混合
工具: 碗或盆

### 第3步
步骤: 步骤3
描述: 小米椒切圈，备用。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 豆角去筋，45°斜切4-10cm小段，备用。
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱、小米椒，翻炒至闻到香味。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 加入豆角，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入料汁，开大火翻炒2分钟。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 倒入150ml水，转中小火，盖上锅盖焖制8-10分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 8-10分钟

### 第9步
步骤: 步骤9
描述: 加入蒜切沫，出锅。
方法: 炒
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201005226, chunk_id=201005226_chunk_1037, recipe_name=陕北熬豆角, category=素菜, score=0.6765478253364563, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，姜切丝，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 豆角去筋，切2-10cm小段，备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 土豆去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第4步
步骤: 步骤4
描述: 西红柿去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 辣椒去仔，切0.15cm宽条，备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱姜蒜，翻炒至闻到葱姜蒜香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 加入豆角，翻炒至变色（青绿色变为翠绿色）。
方法: 炒
工具: 锅铲
时间: 约2分钟

### 第8步
步骤: 步骤8
描述: 加入土豆块，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第9步
步骤: 步骤9
描述: 加入热水（水面刚刚漫过菜），盖上锅盖熬至土豆变软（可以用筷子确认）。
方法: 熬,煮
工具: 炒锅,锅盖,筷子
时间: 约10-12分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿块，加入盐、生抽、蚝油、五香粉、辣椒，熬至西红柿成汁（注意搅拌，防止糊锅）。
方法: 熬,搅拌
工具: 锅铲
时间: 约3-5分钟

### 第11步
步骤: 步骤11
描述: 加入香菜碎，出锅。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_818, recipe_name=炸酱面, category=主食, score=0.6380012631416321, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菜码切丝备用。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 葱切碎。油锅烧热，下葱和肉，炒至肉完全熟透（无红色）。
方法: 切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 下豆瓣酱和甜面酱，继续炒至微微粘稠。盛出，得到炸酱。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 取大碗，加凉水备用。
工具: 大碗
时间: 30秒

### 第5步
步骤: 步骤5
描述: 煮面条至断生（无白芯），盛入第4步装有凉水的碗中。
方法: 煮
工具: 锅,筷子
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 立即控水捞出，盛入干净的碗中。
方法: 捞
工具: 筷子,漏勺
时间: 30秒

### 第7步
步骤: 步骤7
描述: 取第3步炸酱，倒入碗中，拌匀。然后取第1步菜码，倒入碗中，拌匀。
方法: 拌
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201004466, chunk_id=201004466_chunk_890, recipe_name=意式肉酱面, category=主食, score=0.6314668655395508, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅中加水，烧开后放入意面，按包装时间煮 6-12 分钟
方法: 煮
工具: 锅
时间: 6-12分钟

### 第2步
步骤: 步骤2
描述: 洋葱切成小丁
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 空锅中倒油，中火下入洋葱碎，持续搅拌至洋葱半透明
方法: 炒,搅拌
工具: 锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 下入肉沫，继续搅拌搅散，炒至肉末变棕色
方法: 炒,搅拌
工具: 锅,锅铲
时间: 约3分钟

### 第5步
步骤: 步骤5
描述: 加入意大利面酱，稍微搅拌均匀
方法: 搅拌
工具: 锅,锅铲
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 将煮好的意面沥干水分，倒入肉酱中搅拌均匀即可
方法: 搅拌
工具: 漏勺,锅,锅铲
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201004746, chunk_id=201004746_chunk_943, recipe_name=西红柿鸡蛋挂面, category=主食, score=0.6414397358894348, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 小葱洗净并切成葱花；西红柿切块；青椒切成菱形块；鸡蛋打入碗中打散，如腥味重可加2g白醋去腥。
方法: 切
工具: 刀,案板,碗
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 起锅烧热，倒入15-20g食用油，油温七成热时倒入蛋液快速划散，炒至凝固后盛出备用，留底油。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 锅中留底油，下葱白、蒜末炒香，加入西红柿块和青椒翻炒出汁，加入酱油5g、白砂糖2g，翻炒十几秒后加一碗清水，煮沸后加入炒好的鸡蛋、蚝油5g（或鸡精2g）提鲜，中小火收汁，期间搅拌防粘，收汁完成后撒葱花、淋香油，制成西红柿鸡蛋臊子。
方法: 炒,煮,收汁
工具: 炒锅,锅铲
时间: 7分钟

### 第4步
步骤: 步骤4
描述: 锅中加清水500ml煮沸，下挂面，煮软后加入100ml清水，再次煮沸后再加100ml清水，重复2-3次，面条两侧呈透明状即熟，捞出放入臊子碗中拌匀即可。
方法: 煮
工具: 锅,筷子
时间: 6分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201003025, chunk_id=201003025_chunk_595, recipe_name=羊排焖面, category=荤菜, score=0.6465954780578613, search_type=vector_enhanced

```text
# 羊排焖面

菜系: 西北菜
难度: 4.0星

时间信息: 准备时间: 约20分钟（切配、焯水、和面）, 烹饪时间: 约50分钟（炖煮30分钟+焖面4分钟+其他炒制）
份量: 2人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201004769, recipe_name=豆角, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆角
食材名称: 豆角
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=8
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

### result_order=9
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

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201004766, chunk_id=201004766_chunk_947, recipe_name=豆角焖面, category=主食, score=0.7160660028457642, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将豆角切成5-6 cm的小段。
方法: 切
工具: 菜刀,砧板

### 第2步
步骤: 步骤2
描述: 将葱切成1-2 cm小段；姜切成1 mm×1 mm×3 cm长条；蒜拍碎后切成1 mm粒度；五花肉切成2 mm厚片。
方法: 切
工具: 菜刀,砧板

### 第3步
步骤: 步骤3
描述: 锅烧热至手放锅上方10 cm处明显烤手，倒入10-18 ml食用油，摇晃锅使油挂满锅底三分之二。
方法: 加热,倒油
工具: 炒锅

### 第4步
步骤: 步骤4
描述: 放入全部姜和葱段，爆香5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒

### 第5步
步骤: 步骤5
描述: 放入全部肉片，静置5秒后翻炒，使肉片均匀裹油。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒+

### 第6步
步骤: 步骤6
描述: 肉片全部变色后，沿锅边淋入生抽，翻炒均匀。
方法: 炒,淋
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 依次加入盐、老抽、耗油、十三香、鸡精及全部豆角，翻炒2分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 加入150 ml热水，水开后舀出一半菜汤备用。
方法: 煮
工具: 炒锅,勺子

### 第9步
步骤: 步骤9
描述: 将面条平铺在菜上，盖盖中火焖5分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 5分钟

### 第10步
步骤: 步骤10
描述: 打开锅盖，将之前舀出的菜汤每次一勺均匀撒在面条上，再盖盖中火焖3分钟。
方法: 焖
工具: 炒锅,锅盖,勺子
时间: 3分钟

### 第11步
步骤: 步骤11
描述: 开盖后撒入全部蒜和味精，用筷子翻炒均匀即可关火。
方法: 炒
工具: 炒锅,筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_998, recipe_name=素炒豆角, category=素菜, score=0.6725745797157288, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生抽、老抽、耗油、盐混合调料汁，备用。
方法: 混合
工具: 碗或盆

### 第3步
步骤: 步骤3
描述: 小米椒切圈，备用。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 豆角去筋，45°斜切4-10cm小段，备用。
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱、小米椒，翻炒至闻到香味。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 加入豆角，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入料汁，开大火翻炒2分钟。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 倒入150ml水，转中小火，盖上锅盖焖制8-10分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 8-10分钟

### 第9步
步骤: 步骤9
描述: 加入蒜切沫，出锅。
方法: 炒
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201005226, chunk_id=201005226_chunk_1037, recipe_name=陕北熬豆角, category=素菜, score=0.6765478253364563, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，姜切丝，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 豆角去筋，切2-10cm小段，备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 土豆去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第4步
步骤: 步骤4
描述: 西红柿去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 辣椒去仔，切0.15cm宽条，备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱姜蒜，翻炒至闻到葱姜蒜香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 加入豆角，翻炒至变色（青绿色变为翠绿色）。
方法: 炒
工具: 锅铲
时间: 约2分钟

### 第8步
步骤: 步骤8
描述: 加入土豆块，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第9步
步骤: 步骤9
描述: 加入热水（水面刚刚漫过菜），盖上锅盖熬至土豆变软（可以用筷子确认）。
方法: 熬,煮
工具: 炒锅,锅盖,筷子
时间: 约10-12分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿块，加入盐、生抽、蚝油、五香粉、辣椒，熬至西红柿成汁（注意搅拌，防止糊锅）。
方法: 熬,搅拌
工具: 锅铲
时间: 约3-5分钟

### 第11步
步骤: 步骤11
描述: 加入香菜碎，出锅。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_818, recipe_name=炸酱面, category=主食, score=0.6380012631416321, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菜码切丝备用。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 葱切碎。油锅烧热，下葱和肉，炒至肉完全熟透（无红色）。
方法: 切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 下豆瓣酱和甜面酱，继续炒至微微粘稠。盛出，得到炸酱。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 取大碗，加凉水备用。
工具: 大碗
时间: 30秒

### 第5步
步骤: 步骤5
描述: 煮面条至断生（无白芯），盛入第4步装有凉水的碗中。
方法: 煮
工具: 锅,筷子
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 立即控水捞出，盛入干净的碗中。
方法: 捞
工具: 筷子,漏勺
时间: 30秒

### 第7步
步骤: 步骤7
描述: 取第3步炸酱，倒入碗中，拌匀。然后取第1步菜码，倒入碗中，拌匀。
方法: 拌
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=201003025, chunk_id=201003025_chunk_595, recipe_name=羊排焖面, category=荤菜, score=0.6465954780578613, search_type=vector_enhanced

```text
# 羊排焖面

菜系: 西北菜
难度: 4.0星

时间信息: 准备时间: 约20分钟（切配、焯水、和面）, 烹饪时间: 约50分钟（炖煮30分钟+焖面4分钟+其他炒制）
份量: 2人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201004766, chunk_id=201004766_chunk_947, recipe_name=豆角焖面, category=主食, score=0.7160660028457642, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将豆角切成5-6 cm的小段。
方法: 切
工具: 菜刀,砧板

### 第2步
步骤: 步骤2
描述: 将葱切成1-2 cm小段；姜切成1 mm×1 mm×3 cm长条；蒜拍碎后切成1 mm粒度；五花肉切成2 mm厚片。
方法: 切
工具: 菜刀,砧板

### 第3步
步骤: 步骤3
描述: 锅烧热至手放锅上方10 cm处明显烤手，倒入10-18 ml食用油，摇晃锅使油挂满锅底三分之二。
方法: 加热,倒油
工具: 炒锅

### 第4步
步骤: 步骤4
描述: 放入全部姜和葱段，爆香5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒

### 第5步
步骤: 步骤5
描述: 放入全部肉片，静置5秒后翻炒，使肉片均匀裹油。
方法: 炒
工具: 炒锅,锅铲
时间: 5秒+

### 第6步
步骤: 步骤6
描述: 肉片全部变色后，沿锅边淋入生抽，翻炒均匀。
方法: 炒,淋
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 依次加入盐、老抽、耗油、十三香、鸡精及全部豆角，翻炒2分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 加入150 ml热水，水开后舀出一半菜汤备用。
方法: 煮
工具: 炒锅,勺子

### 第9步
步骤: 步骤9
描述: 将面条平铺在菜上，盖盖中火焖5分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 5分钟

### 第10步
步骤: 步骤10
描述: 打开锅盖，将之前舀出的菜汤每次一勺均匀撒在面条上，再盖盖中火焖3分钟。
方法: 焖
工具: 炒锅,锅盖,勺子
时间: 3分钟

### 第11步
步骤: 步骤11
描述: 开盖后撒入全部蒜和味精，用筷子翻炒均匀即可关火。
方法: 炒
工具: 炒锅,筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: generation_context
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_998, recipe_name=素炒豆角, category=素菜, score=0.6725745797157288, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生抽、老抽、耗油、盐混合调料汁，备用。
方法: 混合
工具: 碗或盆

### 第3步
步骤: 步骤3
描述: 小米椒切圈，备用。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 豆角去筋，45°斜切4-10cm小段，备用。
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱、小米椒，翻炒至闻到香味。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 加入豆角，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入料汁，开大火翻炒2分钟。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 倒入150ml水，转中小火，盖上锅盖焖制8-10分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 8-10分钟

### 第9步
步骤: 步骤9
描述: 加入蒜切沫，出锅。
方法: 炒
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=2
source: generation_context
metadata_summary: node_id=201005226, chunk_id=201005226_chunk_1037, recipe_name=陕北熬豆角, category=素菜, score=0.6765478253364563, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，姜切丝，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 豆角去筋，切2-10cm小段，备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 土豆去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第4步
步骤: 步骤4
描述: 西红柿去皮，切1cm³小块，备用。
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 辣椒去仔，切0.15cm宽条，备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱姜蒜，翻炒至闻到葱姜蒜香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 加入豆角，翻炒至变色（青绿色变为翠绿色）。
方法: 炒
工具: 锅铲
时间: 约2分钟

### 第8步
步骤: 步骤8
描述: 加入土豆块，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第9步
步骤: 步骤9
描述: 加入热水（水面刚刚漫过菜），盖上锅盖熬至土豆变软（可以用筷子确认）。
方法: 熬,煮
工具: 炒锅,锅盖,筷子
时间: 约10-12分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿块，加入盐、生抽、蚝油、五香粉、辣椒，熬至西红柿成汁（注意搅拌，防止糊锅）。
方法: 熬,搅拌
工具: 锅铲
时间: 约3-5分钟

### 第11步
步骤: 步骤11
描述: 加入香菜碎，出锅。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=3
source: generation_context
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_818, recipe_name=炸酱面, category=主食, score=0.6380012631416321, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菜码切丝备用。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 葱切碎。油锅烧热，下葱和肉，炒至肉完全熟透（无红色）。
方法: 切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 下豆瓣酱和甜面酱，继续炒至微微粘稠。盛出，得到炸酱。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 取大碗，加凉水备用。
工具: 大碗
时间: 30秒

### 第5步
步骤: 步骤5
描述: 煮面条至断生（无白芯），盛入第4步装有凉水的碗中。
方法: 煮
工具: 锅,筷子
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 立即控水捞出，盛入干净的碗中。
方法: 捞
工具: 筷子,漏勺
时间: 30秒

### 第7步
步骤: 步骤7
描述: 取第3步炸酱，倒入碗中，拌匀。然后取第1步菜码，倒入碗中，拌匀。
方法: 拌
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=4
source: generation_context
metadata_summary: node_id=201003025, chunk_id=201003025_chunk_595, recipe_name=羊排焖面, category=荤菜, score=0.6465954780578613, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
# 羊排焖面

菜系: 西北菜
难度: 4.0星

时间信息: 准备时间: 约20分钟（切配、焯水、和面）, 烹饪时间: 约50分钟（炖煮30分钟+焖面4分钟+其他炒制）
份量: 2人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

