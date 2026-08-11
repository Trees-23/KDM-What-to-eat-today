# Recall Content

audit_id: 20260811_173841_781_3c863d47
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201004138, recipe_name=普通面条, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 普通面条
食材名称: 普通面条
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=1
source: entity_level
metadata_summary: node_id=201004040, recipe_name=汤面, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 汤面
菜品名称: 汤面
分类: 主食
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=2
source: entity_level
metadata_summary: node_id=201004135, recipe_name=炸酱面, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 炸酱面
菜品名称: 炸酱面
分类: 主食
菜系: 鲁菜
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=3
source: entity_level
metadata_summary: node_id=201004467, recipe_name=意大利面, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 意大利面
食材名称: 意大利面
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=201004040, recipe_name=汤面, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 面食
关系类型: REQUIRES
源实体: 汤面 (Recipe)
目标实体: 面食 (Ingredient)
相关菜品: 汤面
相关信息: 面食
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
菜品详情: 菜品名称: 汤面
```

### result_order=1
source: topic_level
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 青蟹 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 青蟹
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=2
source: topic_level
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 咖喱块 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 咖喱块
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=3
source: topic_level
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 洋葱 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 洋葱
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=4
source: topic_level
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 椰浆 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 椰浆
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=5
source: topic_level
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 鸡蛋 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 鸡蛋
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=6
source: topic_level
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 生粉 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 生粉
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=7
source: topic_level
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 大蒜 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 大蒜
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=8
source: topic_level
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 食用油 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 食用油
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=9
source: topic_level
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 开水 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 开水
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_817, recipe_name=炸酱面, category=主食, score=0.6696502566337585, search_type=vector_enhanced

```text
## 所需食材
1. 挂面(150g)
2. 普通面条(250g)
3. 甜面酱(20g)
4. 肉丁/肉末(150g)
5. 菜码（黄瓜、白菜、萝卜等）(35g)
6. 葱(15g)
7. 蒜(适量g)
8. 豆瓣酱(20g)
9. 食用油(10g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201004232, chunk_id=201004232_chunk_840, recipe_name=蒸卤面, category=主食, score=0.6381010413169861, search_type=vector_enhanced

```text
## 所需食材
1. 五香粉(5g)
2. 大葱(10cm)
3. 大蒜(5瓣)
4. 姜片(20g)
5. 干红椒(3个)
6. 料酒
7. 猪五花肉(350g)
8. 生抽(15ml)
9. 盐(10g)
10. 老抽(10ml)
11. 花椒(20粒)
12. 芹菜(2根)
13. 青椒(2个)
14. 食用油
15. 鲜面条(500g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6306929588317871, search_type=vector_enhanced

```text
## 所需食材
1. 其他蔬菜（青椒番茄胡萝卜等）(适量g)
2. 冷水(200-400ml)
3. 盐(适量g)
4. 肉类（牛羊鱼虾等）(适量g)
5. 胡椒粉(适量g)
6. 蛋类（鸡蛋鸭蛋等）(适量个)
7. 豆制品（豆腐皮等）(适量g)
8. 青菜（生菜菠菜等）(适量g)
9. 面食(70-230g)
10. 香油(适量ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201004746, chunk_id=201004746_chunk_943, recipe_name=西红柿鸡蛋挂面, category=主食, score=0.6293051242828369, search_type=vector_enhanced

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

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201004766, chunk_id=201004766_chunk_948, recipe_name=豆角焖面, category=主食, score=0.6282113790512085, search_type=vector_enhanced

```text
## 标签
懒人美食,操作简单,面条粗细可选：毛细/细/二细/三细/韭叶/大宽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6048961877822876, search_type=vector_enhanced

```text
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201004215, chunk_id=201004215_chunk_837, recipe_name=葱油拌面, category=主食, score=0.600509762763977, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将小葱洗净，切成长段（约5-7 cm），葱白和葱绿分开。
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 锅中加入100 ml食用油，中火烧热，先放入葱白段煸炒至微黄。
方法: 炒
工具: 锅,锅铲
时间: 2-3分钟

### 第3步
步骤: 步骤3
描述: 加入葱绿段，转小火继续煸炒15-20分钟，至葱段焦黄酥脆。
方法: 炒
工具: 锅,锅铲
时间: 15-20分钟

### 第4步
步骤: 步骤4
描述: 将焦黄的葱段捞出，葱油保留在锅中。
方法: 捞
工具: 锅铲
时间: 30秒

### 第5步
步骤: 步骤5
描述: 在葱油中加入生抽、老抽、白糖，小火加热并搅拌约1分钟至糖溶解，酱汁混合均匀后关火。
方法: 加热,搅拌
工具: 锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 将制作好的葱油酱汁倒入容器中，放凉后密封保存。
方法: 倒
工具: 容器
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 锅中加入1000 ml饮用水，大火烧开。
方法: 煮
工具: 锅
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 放入80 g干面条，根据包装说明煮至熟透（通常3-8分钟）。
方法: 煮
工具: 锅,筷子
时间: 3-8分钟

### 第9步
步骤: 步骤9
描述: 将煮好的面条捞出，沥干水分，放入碗中。
方法: 捞,沥
工具: 漏勺,碗
时间: 30秒

### 第10步
步骤: 步骤10
描述: 在面条中加入15 ml葱油酱汁，可选加入炸好的葱段，用筷子快速搅拌均匀即可食用。
方法: 拌
工具: 筷子,碗
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201004076, chunk_id=201004076_chunk_806, recipe_name=炒方便面, category=主食, score=0.6000434160232544, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将火腿肠撕开包装，切成宽度1cm的小块。
方法: 切
工具: 刀,案板
时间: 约30秒

### 第2步
步骤: 步骤2
描述: 向煮锅中加入300ml水，煮沸后加入方便面面饼，煮45秒并挑散面条，关火后立即将面汤与面分离，并用凉水冲一下面条。
方法: 煮,挑散,冲洗
工具: 煮锅,筷子
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 将方便面调料包（菜包、酱包全部，粉包50%-80%）挤入小碗中，加入80ml面汤搅匀，制成调料碗。
方法: 搅拌
工具: 小碗,筷子
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入小碗，每蛋加2g盐搅匀；热锅20秒后倒入8ml油，倒入蛋液炒20秒至固态，盛出备用。
方法: 打蛋,炒
工具: 小碗,炒锅,锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 热锅20秒后加油至10ml，倒入火腿肠翻炒10秒，加入面条翻炒30秒，倒入调料碗再炒30秒，最后加入煎好的鸡蛋翻炒30秒，关火盛盘。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1317, recipe_name=凉拌, category=烹饪技巧, score=0.5987525582313538, search_type=vector_enhanced

```text
## 块状蔬菜类主食材加工（此流程可选）（选项单选或多选）
### 块状蔬菜类主食材加工（此流程可选）（选项单选或多选）

用例：马铃薯，荸荠，黄瓜、土豆等

* 将食材切成 0.5cm * 0.5cm 截面长条状
* 将食材切成厚度小于 0.5cm 的 4cm * 4cm 片状
* 将食材用刀面拍碎或压碎（犹适用于黄瓜）
* 将食材直接使用（犹适用于本身为小块的食材）
* 将处理后的食材焯水

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1321, recipe_name=凉拌, category=烹饪技巧, score=0.5979249477386475, search_type=vector_enhanced

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
metadata_summary: node_id=201004138, recipe_name=普通面条, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 普通面条
食材名称: 普通面条
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201004040, recipe_name=汤面, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 汤面
菜品名称: 汤面
分类: 主食
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201004135, recipe_name=炸酱面, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 炸酱面
菜品名称: 炸酱面
分类: 主食
菜系: 鲁菜
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201004467, recipe_name=意大利面, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 意大利面
食材名称: 意大利面
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201004040, recipe_name=汤面, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 面食
关系类型: REQUIRES
源实体: 汤面 (Recipe)
目标实体: 面食 (Ingredient)
相关菜品: 汤面
相关信息: 面食
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
菜品详情: 菜品名称: 汤面
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 青蟹 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 青蟹
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 咖喱块 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 咖喱块
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 洋葱 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 洋葱
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 椰浆 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 椰浆
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 鸡蛋 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 鸡蛋
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 生粉 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 生粉
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 大蒜 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 大蒜
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 食用油 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 食用油
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 开水 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 开水
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_817, recipe_name=炸酱面, category=主食, score=0.6696502566337585, search_type=vector_enhanced

```text
## 所需食材
1. 挂面(150g)
2. 普通面条(250g)
3. 甜面酱(20g)
4. 肉丁/肉末(150g)
5. 菜码（黄瓜、白菜、萝卜等）(35g)
6. 葱(15g)
7. 蒜(适量g)
8. 豆瓣酱(20g)
9. 食用油(10g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=15
source: branch_grouped
metadata_summary: node_id=201004232, chunk_id=201004232_chunk_840, recipe_name=蒸卤面, category=主食, score=0.6381010413169861, search_type=vector_enhanced

```text
## 所需食材
1. 五香粉(5g)
2. 大葱(10cm)
3. 大蒜(5瓣)
4. 姜片(20g)
5. 干红椒(3个)
6. 料酒
7. 猪五花肉(350g)
8. 生抽(15ml)
9. 盐(10g)
10. 老抽(10ml)
11. 花椒(20粒)
12. 芹菜(2根)
13. 青椒(2个)
14. 食用油
15. 鲜面条(500g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=16
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6306929588317871, search_type=vector_enhanced

```text
## 所需食材
1. 其他蔬菜（青椒番茄胡萝卜等）(适量g)
2. 冷水(200-400ml)
3. 盐(适量g)
4. 肉类（牛羊鱼虾等）(适量g)
5. 胡椒粉(适量g)
6. 蛋类（鸡蛋鸭蛋等）(适量个)
7. 豆制品（豆腐皮等）(适量g)
8. 青菜（生菜菠菜等）(适量g)
9. 面食(70-230g)
10. 香油(适量ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=17
source: branch_grouped
metadata_summary: node_id=201004746, chunk_id=201004746_chunk_943, recipe_name=西红柿鸡蛋挂面, category=主食, score=0.6293051242828369, search_type=vector_enhanced

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

### result_order=18
source: branch_grouped
metadata_summary: node_id=201004766, chunk_id=201004766_chunk_948, recipe_name=豆角焖面, category=主食, score=0.6282113790512085, search_type=vector_enhanced

```text
## 标签
懒人美食,操作简单,面条粗细可选：毛细/细/二细/三细/韭叶/大宽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=19
source: branch_grouped
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6048961877822876, search_type=vector_enhanced

```text
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=20
source: branch_grouped
metadata_summary: node_id=201004215, chunk_id=201004215_chunk_837, recipe_name=葱油拌面, category=主食, score=0.600509762763977, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将小葱洗净，切成长段（约5-7 cm），葱白和葱绿分开。
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 锅中加入100 ml食用油，中火烧热，先放入葱白段煸炒至微黄。
方法: 炒
工具: 锅,锅铲
时间: 2-3分钟

### 第3步
步骤: 步骤3
描述: 加入葱绿段，转小火继续煸炒15-20分钟，至葱段焦黄酥脆。
方法: 炒
工具: 锅,锅铲
时间: 15-20分钟

### 第4步
步骤: 步骤4
描述: 将焦黄的葱段捞出，葱油保留在锅中。
方法: 捞
工具: 锅铲
时间: 30秒

### 第5步
步骤: 步骤5
描述: 在葱油中加入生抽、老抽、白糖，小火加热并搅拌约1分钟至糖溶解，酱汁混合均匀后关火。
方法: 加热,搅拌
工具: 锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 将制作好的葱油酱汁倒入容器中，放凉后密封保存。
方法: 倒
工具: 容器
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 锅中加入1000 ml饮用水，大火烧开。
方法: 煮
工具: 锅
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 放入80 g干面条，根据包装说明煮至熟透（通常3-8分钟）。
方法: 煮
工具: 锅,筷子
时间: 3-8分钟

### 第9步
步骤: 步骤9
描述: 将煮好的面条捞出，沥干水分，放入碗中。
方法: 捞,沥
工具: 漏勺,碗
时间: 30秒

### 第10步
步骤: 步骤10
描述: 在面条中加入15 ml葱油酱汁，可选加入炸好的葱段，用筷子快速搅拌均匀即可食用。
方法: 拌
工具: 筷子,碗
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=21
source: branch_grouped
metadata_summary: node_id=201004076, chunk_id=201004076_chunk_806, recipe_name=炒方便面, category=主食, score=0.6000434160232544, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将火腿肠撕开包装，切成宽度1cm的小块。
方法: 切
工具: 刀,案板
时间: 约30秒

### 第2步
步骤: 步骤2
描述: 向煮锅中加入300ml水，煮沸后加入方便面面饼，煮45秒并挑散面条，关火后立即将面汤与面分离，并用凉水冲一下面条。
方法: 煮,挑散,冲洗
工具: 煮锅,筷子
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 将方便面调料包（菜包、酱包全部，粉包50%-80%）挤入小碗中，加入80ml面汤搅匀，制成调料碗。
方法: 搅拌
工具: 小碗,筷子
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入小碗，每蛋加2g盐搅匀；热锅20秒后倒入8ml油，倒入蛋液炒20秒至固态，盛出备用。
方法: 打蛋,炒
工具: 小碗,炒锅,锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 热锅20秒后加油至10ml，倒入火腿肠翻炒10秒，加入面条翻炒30秒，倒入调料碗再炒30秒，最后加入煎好的鸡蛋翻炒30秒，关火盛盘。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=22
source: branch_grouped
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1317, recipe_name=凉拌, category=烹饪技巧, score=0.5987525582313538, search_type=vector_enhanced

```text
## 块状蔬菜类主食材加工（此流程可选）（选项单选或多选）
### 块状蔬菜类主食材加工（此流程可选）（选项单选或多选）

用例：马铃薯，荸荠，黄瓜、土豆等

* 将食材切成 0.5cm * 0.5cm 截面长条状
* 将食材切成厚度小于 0.5cm 的 4cm * 4cm 片状
* 将食材用刀面拍碎或压碎（犹适用于黄瓜）
* 将食材直接使用（犹适用于本身为小块的食材）
* 将处理后的食材焯水

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=23
source: branch_grouped
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1321, recipe_name=凉拌, category=烹饪技巧, score=0.5979249477386475, search_type=vector_enhanced

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
metadata_summary: node_id=201004138, recipe_name=普通面条, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 普通面条
食材名称: 普通面条
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6306929588317871, search_type=vector_enhanced

```text
## 所需食材
1. 其他蔬菜（青椒番茄胡萝卜等）(适量g)
2. 冷水(200-400ml)
3. 盐(适量g)
4. 肉类（牛羊鱼虾等）(适量g)
5. 胡椒粉(适量g)
6. 蛋类（鸡蛋鸭蛋等）(适量个)
7. 豆制品（豆腐皮等）(适量g)
8. 青菜（生菜菠菜等）(适量g)
9. 面食(70-230g)
10. 香油(适量ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_817, recipe_name=炸酱面, category=主食, score=0.6696502566337585, search_type=vector_enhanced

```text
## 所需食材
1. 挂面(150g)
2. 普通面条(250g)
3. 甜面酱(20g)
4. 肉丁/肉末(150g)
5. 菜码（黄瓜、白菜、萝卜等）(35g)
6. 葱(15g)
7. 蒜(适量g)
8. 豆瓣酱(20g)
9. 食用油(10g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201004467, recipe_name=意大利面, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 意大利面
食材名称: 意大利面
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 咖喱块 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 咖喱块
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201004232, chunk_id=201004232_chunk_840, recipe_name=蒸卤面, category=主食, score=0.6381010413169861, search_type=vector_enhanced

```text
## 所需食材
1. 五香粉(5g)
2. 大葱(10cm)
3. 大蒜(5瓣)
4. 姜片(20g)
5. 干红椒(3个)
6. 料酒
7. 猪五花肉(350g)
8. 生抽(15ml)
9. 盐(10g)
10. 老抽(10ml)
11. 花椒(20粒)
12. 芹菜(2根)
13. 青椒(2个)
14. 食用油
15. 鲜面条(500g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=201004746, chunk_id=201004746_chunk_943, recipe_name=西红柿鸡蛋挂面, category=主食, score=0.6293051242828369, search_type=vector_enhanced

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
source: merged_candidates
metadata_summary: node_id=201004766, chunk_id=201004766_chunk_948, recipe_name=豆角焖面, category=主食, score=0.6282113790512085, search_type=vector_enhanced

```text
## 标签
懒人美食,操作简单,面条粗细可选：毛细/细/二细/三细/韭叶/大宽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6048961877822876, search_type=vector_enhanced

```text
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=201004215, chunk_id=201004215_chunk_837, recipe_name=葱油拌面, category=主食, score=0.600509762763977, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将小葱洗净，切成长段（约5-7 cm），葱白和葱绿分开。
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 锅中加入100 ml食用油，中火烧热，先放入葱白段煸炒至微黄。
方法: 炒
工具: 锅,锅铲
时间: 2-3分钟

### 第3步
步骤: 步骤3
描述: 加入葱绿段，转小火继续煸炒15-20分钟，至葱段焦黄酥脆。
方法: 炒
工具: 锅,锅铲
时间: 15-20分钟

### 第4步
步骤: 步骤4
描述: 将焦黄的葱段捞出，葱油保留在锅中。
方法: 捞
工具: 锅铲
时间: 30秒

### 第5步
步骤: 步骤5
描述: 在葱油中加入生抽、老抽、白糖，小火加热并搅拌约1分钟至糖溶解，酱汁混合均匀后关火。
方法: 加热,搅拌
工具: 锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 将制作好的葱油酱汁倒入容器中，放凉后密封保存。
方法: 倒
工具: 容器
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 锅中加入1000 ml饮用水，大火烧开。
方法: 煮
工具: 锅
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 放入80 g干面条，根据包装说明煮至熟透（通常3-8分钟）。
方法: 煮
工具: 锅,筷子
时间: 3-8分钟

### 第9步
步骤: 步骤9
描述: 将煮好的面条捞出，沥干水分，放入碗中。
方法: 捞,沥
工具: 漏勺,碗
时间: 30秒

### 第10步
步骤: 步骤10
描述: 在面条中加入15 ml葱油酱汁，可选加入炸好的葱段，用筷子快速搅拌均匀即可食用。
方法: 拌
工具: 筷子,碗
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201004076, chunk_id=201004076_chunk_806, recipe_name=炒方便面, category=主食, score=0.6000434160232544, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将火腿肠撕开包装，切成宽度1cm的小块。
方法: 切
工具: 刀,案板
时间: 约30秒

### 第2步
步骤: 步骤2
描述: 向煮锅中加入300ml水，煮沸后加入方便面面饼，煮45秒并挑散面条，关火后立即将面汤与面分离，并用凉水冲一下面条。
方法: 煮,挑散,冲洗
工具: 煮锅,筷子
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 将方便面调料包（菜包、酱包全部，粉包50%-80%）挤入小碗中，加入80ml面汤搅匀，制成调料碗。
方法: 搅拌
工具: 小碗,筷子
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入小碗，每蛋加2g盐搅匀；热锅20秒后倒入8ml油，倒入蛋液炒20秒至固态，盛出备用。
方法: 打蛋,炒
工具: 小碗,炒锅,锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 热锅20秒后加油至10ml，倒入火腿肠翻炒10秒，加入面条翻炒30秒，倒入调料碗再炒30秒，最后加入煎好的鸡蛋翻炒30秒，关火盛盘。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1321, recipe_name=凉拌, category=烹饪技巧, score=0.5979249477386475, search_type=vector_enhanced

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
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7, recipe_name=凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 凉拌
关键技巧内容:
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
## 凉拌的目的
### 凉拌的目的

* 凉拌的目的在于对无味或味淡食材添加味道，例如鸡肋
## 凉拌能放什么
### 凉拌能放什么

包括但不限于：

* 主食材
* 辅料
* 腌制酱料
* 调味料
## 注意事项
### 注意事项

* 凉拌时应该注意食材安全，在不确认食材是否安全时，请勿凉拌对应食材，在确认食材不安全时不应凉拌对应食材
* 凉拌应尽可能加大主食菜的接触面积，故凉拌时推荐刀花、切片、拍碎甚至搅碎
* 凉拌菜对肠胃提出了基本要求，请在确认不会喷射或存有喷射时间时采用凉拌
* 文件撰写时处于新冠疫情状态下，建议将所有食材均在 100 摄氏度以上的环境中加热 15 秒以上以图心理安慰，若想求得安全请尽量避免凉拌
## 器具
## 器具

可以使用任何容器，从瓷缸到食品级塑料袋均可
## 注意事项
### 注意事项

* 为方便搅拌时食材不溅出，使用容积在所有食材两倍以上的硬质容器较为合适
* 为保证食品安全，在塑料袋或塑料碗中腌制后请尽快将食材移至瓷容器或金属质容器中
* 为保证食品安全，请在洁净的砧板上处理生食食材与辅料
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 普通面条
食材名称: 普通面条
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### pair_order=1
source: rerank_input

```text
菜品: 汤面
菜系: 未知
## 所需食材
1. 其他蔬菜（青椒番茄胡萝卜等）(适量g)
2. 冷水(200-400ml)
3. 盐(适量g)
4. 肉类（牛羊鱼虾等）(适量g)
5. 胡椒粉(适量g)
6. 蛋类（鸡蛋鸭蛋等）(适量个)
7. 豆制品（豆腐皮等）(适量g)
8. 青菜（生菜菠菜等）(适量g)
9. 面食(70-230g)
10. 香油(适量ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=2
source: rerank_input

```text
菜品: 炸酱面
菜系: 鲁菜
## 所需食材
1. 挂面(150g)
2. 普通面条(250g)
3. 甜面酱(20g)
4. 肉丁/肉末(150g)
5. 菜码（黄瓜、白菜、萝卜等）(35g)
6. 葱(15g)
7. 蒜(适量g)
8. 豆瓣酱(20g)
9. 食用油(10g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=3
source: rerank_input

```text
命中关键词: 意大利面
食材名称: 意大利面
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### pair_order=4
source: rerank_input

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 咖喱块 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 咖喱块
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### pair_order=5
source: rerank_input

```text
菜品: 蒸卤面
菜系: 豫菜
## 所需食材
1. 五香粉(5g)
2. 大葱(10cm)
3. 大蒜(5瓣)
4. 姜片(20g)
5. 干红椒(3个)
6. 料酒
7. 猪五花肉(350g)
8. 生抽(15ml)
9. 盐(10g)
10. 老抽(10ml)
11. 花椒(20粒)
12. 芹菜(2根)
13. 青椒(2个)
14. 食用油
15. 鲜面条(500g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=6
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

### pair_order=7
source: rerank_input

```text
菜品: 豆角焖面
菜系: 未知
## 标签
懒人美食,操作简单,面条粗细可选：毛细/细/二细/三细/韭叶/大宽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=8
source: rerank_input

```text
菜系: 川菜
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=9
source: rerank_input

```text
菜品: 葱油拌面
菜系: 沪菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将小葱洗净，切成长段（约5-7 cm），葱白和葱绿分开。
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 锅中加入100 ml食用油，中火烧热，先放入葱白段煸炒至微黄。
方法: 炒
工具: 锅,锅铲
时间: 2-3分钟

### 第3步
步骤: 步骤3
描述: 加入葱绿段，转小火继续煸炒15-20分钟，至葱段焦黄酥脆。
方法: 炒
工具: 锅,锅铲
时间: 15-20分钟

### 第4步
步骤: 步骤4
描述: 将焦黄的葱段捞出，葱油保留在锅中。
方法: 捞
工具: 锅铲
时间: 30秒

### 第5步
步骤: 步骤5
描述: 在葱油中加入生抽、老抽、白糖，小火加热并搅拌约1分钟至糖溶解，酱汁混合均匀后关火。
方法: 加热,搅拌
工具: 锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 将制作好的葱油酱汁倒入容器中，放凉后密封保存。
方法: 倒
工具: 容器
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 锅中加入1000 ml饮用水，大火烧开。
方法: 煮
工具: 锅
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 放入80 g干面条，根据包装说明煮至熟透（通常3-8分钟）。
方法: 煮
工具: 锅,筷子
时间: 3-8分钟

### 第9步
步骤: 步骤9
描述: 将煮好的面条捞出，沥干水分，放入碗中。
方法: 捞,沥
工具: 漏勺,碗
时间: 30秒

### 第10步
步骤: 步骤10
描述: 在面条中加入15 ml葱油酱汁，可选加入炸好的葱段，用筷子快速搅拌均匀即可食用。
方法: 拌
工具: 筷子,碗
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=10
source: rerank_input

```text
菜品: 炒方便面
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将火腿肠撕开包装，切成宽度1cm的小块。
方法: 切
工具: 刀,案板
时间: 约30秒

### 第2步
步骤: 步骤2
描述: 向煮锅中加入300ml水，煮沸后加入方便面面饼，煮45秒并挑散面条，关火后立即将面汤与面分离，并用凉水冲一下面条。
方法: 煮,挑散,冲洗
工具: 煮锅,筷子
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 将方便面调料包（菜包、酱包全部，粉包50%-80%）挤入小碗中，加入80ml面汤搅匀，制成调料碗。
方法: 搅拌
工具: 小碗,筷子
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入小碗，每蛋加2g盐搅匀；热锅20秒后倒入8ml油，倒入蛋液炒20秒至固态，盛出备用。
方法: 打蛋,炒
工具: 小碗,炒锅,锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 热锅20秒后加油至10ml，倒入火腿肠翻炒10秒，加入面条翻炒30秒，倒入调料碗再炒30秒，最后加入煎好的鸡蛋翻炒30秒，关火盛盘。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=11
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

### pair_order=12
source: rerank_input

```text
分类: 烹饪技巧
技巧文档扩展上下文: 凉拌
关键技巧内容:
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
## 凉拌的目的
### 凉拌的目的

* 凉拌的目的在于对无味或味淡食材添加味道，例如鸡肋
## 凉拌能放什么
### 凉拌能放什么

包括但不限于：

* 主食材
* 辅料
* 腌制酱料
* 调味料
## 注意事项
### 注意事项

* 凉拌时应该注意食材安全，在不确认食材是否安全时，请勿凉拌对应食材，在确认食材不安全时不应凉拌对应食材
* 凉拌应尽可能加大主食菜的接触面积，故凉拌时推荐刀花、切片、拍碎甚至搅碎
* 凉拌菜对肠胃提出了基本要求，请在确认不会喷射或存有喷射时间时采用凉拌
* 文件撰写时处于新冠疫情状态下，建议将所有食材均在 100 摄氏度以上的环境中加热 15 秒以上以图心理安慰，若想求得安全请尽量避免凉拌
## 器具
## 器具

可以使用任何容器，从瓷缸到食品级塑料袋均可
## 注意事项
### 注意事项

* 为方便搅拌时食材不溅出，使用容积在所有食材两倍以上的硬质容器较为合适
* 为保证食品安全，在塑料袋或塑料碗中腌制后请尽快将食材移至瓷容器或金属质容器中
* 为保证食品安全，请在洁净的砧板上处理生食食材与辅料
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201004138, recipe_name=普通面条, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 普通面条
食材名称: 普通面条
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_817, recipe_name=炸酱面, category=主食, score=0.6696502566337585, search_type=vector_enhanced

```text
## 所需食材
1. 挂面(150g)
2. 普通面条(250g)
3. 甜面酱(20g)
4. 肉丁/肉末(150g)
5. 菜码（黄瓜、白菜、萝卜等）(35g)
6. 葱(15g)
7. 蒜(适量g)
8. 豆瓣酱(20g)
9. 食用油(10g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201004232, chunk_id=201004232_chunk_840, recipe_name=蒸卤面, category=主食, score=0.6381010413169861, search_type=vector_enhanced

```text
## 所需食材
1. 五香粉(5g)
2. 大葱(10cm)
3. 大蒜(5瓣)
4. 姜片(20g)
5. 干红椒(3个)
6. 料酒
7. 猪五花肉(350g)
8. 生抽(15ml)
9. 盐(10g)
10. 老抽(10ml)
11. 花椒(20粒)
12. 芹菜(2根)
13. 青椒(2个)
14. 食用油
15. 鲜面条(500g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201004215, chunk_id=201004215_chunk_837, recipe_name=葱油拌面, category=主食, score=0.600509762763977, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将小葱洗净，切成长段（约5-7 cm），葱白和葱绿分开。
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 锅中加入100 ml食用油，中火烧热，先放入葱白段煸炒至微黄。
方法: 炒
工具: 锅,锅铲
时间: 2-3分钟

### 第3步
步骤: 步骤3
描述: 加入葱绿段，转小火继续煸炒15-20分钟，至葱段焦黄酥脆。
方法: 炒
工具: 锅,锅铲
时间: 15-20分钟

### 第4步
步骤: 步骤4
描述: 将焦黄的葱段捞出，葱油保留在锅中。
方法: 捞
工具: 锅铲
时间: 30秒

### 第5步
步骤: 步骤5
描述: 在葱油中加入生抽、老抽、白糖，小火加热并搅拌约1分钟至糖溶解，酱汁混合均匀后关火。
方法: 加热,搅拌
工具: 锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 将制作好的葱油酱汁倒入容器中，放凉后密封保存。
方法: 倒
工具: 容器
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 锅中加入1000 ml饮用水，大火烧开。
方法: 煮
工具: 锅
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 放入80 g干面条，根据包装说明煮至熟透（通常3-8分钟）。
方法: 煮
工具: 锅,筷子
时间: 3-8分钟

### 第9步
步骤: 步骤9
描述: 将煮好的面条捞出，沥干水分，放入碗中。
方法: 捞,沥
工具: 漏勺,碗
时间: 30秒

### 第10步
步骤: 步骤10
描述: 在面条中加入15 ml葱油酱汁，可选加入炸好的葱段，用筷子快速搅拌均匀即可食用。
方法: 拌
工具: 筷子,碗
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201004766, chunk_id=201004766_chunk_948, recipe_name=豆角焖面, category=主食, score=0.6282113790512085, search_type=vector_enhanced

```text
## 标签
懒人美食,操作简单,面条粗细可选：毛细/细/二细/三细/韭叶/大宽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201004746, chunk_id=201004746_chunk_943, recipe_name=西红柿鸡蛋挂面, category=主食, score=0.6293051242828369, search_type=vector_enhanced

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
metadata_summary: node_id=201004076, chunk_id=201004076_chunk_806, recipe_name=炒方便面, category=主食, score=0.6000434160232544, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将火腿肠撕开包装，切成宽度1cm的小块。
方法: 切
工具: 刀,案板
时间: 约30秒

### 第2步
步骤: 步骤2
描述: 向煮锅中加入300ml水，煮沸后加入方便面面饼，煮45秒并挑散面条，关火后立即将面汤与面分离，并用凉水冲一下面条。
方法: 煮,挑散,冲洗
工具: 煮锅,筷子
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 将方便面调料包（菜包、酱包全部，粉包50%-80%）挤入小碗中，加入80ml面汤搅匀，制成调料碗。
方法: 搅拌
工具: 小碗,筷子
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入小碗，每蛋加2g盐搅匀；热锅20秒后倒入8ml油，倒入蛋液炒20秒至固态，盛出备用。
方法: 打蛋,炒
工具: 小碗,炒锅,锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 热锅20秒后加油至10ml，倒入火腿肠翻炒10秒，加入面条翻炒30秒，倒入调料碗再炒30秒，最后加入煎好的鸡蛋翻炒30秒，关火盛盘。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6306929588317871, search_type=vector_enhanced

```text
## 所需食材
1. 其他蔬菜（青椒番茄胡萝卜等）(适量g)
2. 冷水(200-400ml)
3. 盐(适量g)
4. 肉类（牛羊鱼虾等）(适量g)
5. 胡椒粉(适量g)
6. 蛋类（鸡蛋鸭蛋等）(适量个)
7. 豆制品（豆腐皮等）(适量g)
8. 青菜（生菜菠菜等）(适量g)
9. 面食(70-230g)
10. 香油(适量ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6048961877822876, search_type=vector_enhanced

```text
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=9
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7, recipe_name=凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 凉拌
关键技巧内容:
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
## 凉拌的目的
### 凉拌的目的

* 凉拌的目的在于对无味或味淡食材添加味道，例如鸡肋
## 凉拌能放什么
### 凉拌能放什么

包括但不限于：

* 主食材
* 辅料
* 腌制酱料
* 调味料
## 注意事项
### 注意事项

* 凉拌时应该注意食材安全，在不确认食材是否安全时，请勿凉拌对应食材，在确认食材不安全时不应凉拌对应食材
* 凉拌应尽可能加大主食菜的接触面积，故凉拌时推荐刀花、切片、拍碎甚至搅碎
* 凉拌菜对肠胃提出了基本要求，请在确认不会喷射或存有喷射时间时采用凉拌
* 文件撰写时处于新冠疫情状态下，建议将所有食材均在 100 摄氏度以上的环境中加热 15 秒以上以图心理安慰，若想求得安全请尽量避免凉拌
## 器具
## 器具

可以使用任何容器，从瓷缸到食品级塑料袋均可
## 注意事项
### 注意事项

* 为方便搅拌时食材不溅出，使用容积在所有食材两倍以上的硬质容器较为合适
* 为保证食品安全，在塑料袋或塑料碗中腌制后请尽快将食材移至瓷容器或金属质容器中
* 为保证食品安全，请在洁净的砧板上处理生食食材与辅料
```

### result_order=10
source: reranked_results
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1321, recipe_name=凉拌, category=烹饪技巧, score=0.5979249477386475, search_type=vector_enhanced

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

### result_order=11
source: reranked_results
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 食材搭配
关系类型: REQUIRES
源实体: 咖喱炒蟹 (Recipe)
目标实体: 咖喱块 (Ingredient)
相关菜品: 咖喱炒蟹
相关信息: 咖喱块
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
菜品详情: 菜品名称: 咖喱炒蟹
```

### result_order=12
source: reranked_results
metadata_summary: node_id=201004467, recipe_name=意大利面, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 意大利面
食材名称: 意大利面
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201004138, recipe_name=普通面条, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 普通面条
食材名称: 普通面条
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_817, recipe_name=炸酱面, category=主食, score=0.6696502566337585, search_type=vector_enhanced

```text
## 所需食材
1. 挂面(150g)
2. 普通面条(250g)
3. 甜面酱(20g)
4. 肉丁/肉末(150g)
5. 菜码（黄瓜、白菜、萝卜等）(35g)
6. 葱(15g)
7. 蒜(适量g)
8. 豆瓣酱(20g)
9. 食用油(10g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201004232, chunk_id=201004232_chunk_840, recipe_name=蒸卤面, category=主食, score=0.6381010413169861, search_type=vector_enhanced

```text
## 所需食材
1. 五香粉(5g)
2. 大葱(10cm)
3. 大蒜(5瓣)
4. 姜片(20g)
5. 干红椒(3个)
6. 料酒
7. 猪五花肉(350g)
8. 生抽(15ml)
9. 盐(10g)
10. 老抽(10ml)
11. 花椒(20粒)
12. 芹菜(2根)
13. 青椒(2个)
14. 食用油
15. 鲜面条(500g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6048961877822876, search_type=vector_enhanced

```text
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7, recipe_name=凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 凉拌
关键技巧内容:
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
## 凉拌的目的
### 凉拌的目的

* 凉拌的目的在于对无味或味淡食材添加味道，例如鸡肋
## 凉拌能放什么
### 凉拌能放什么

包括但不限于：

* 主食材
* 辅料
* 腌制酱料
* 调味料
## 注意事项
### 注意事项

* 凉拌时应该注意食材安全，在不确认食材是否安全时，请勿凉拌对应食材，在确认食材不安全时不应凉拌对应食材
* 凉拌应尽可能加大主食菜的接触面积，故凉拌时推荐刀花、切片、拍碎甚至搅碎
* 凉拌菜对肠胃提出了基本要求，请在确认不会喷射或存有喷射时间时采用凉拌
* 文件撰写时处于新冠疫情状态下，建议将所有食材均在 100 摄氏度以上的环境中加热 15 秒以上以图心理安慰，若想求得安全请尽量避免凉拌
## 器具
## 器具

可以使用任何容器，从瓷缸到食品级塑料袋均可
## 注意事项
### 注意事项

* 为方便搅拌时食材不溅出，使用容积在所有食材两倍以上的硬质容器较为合适
* 为保证食品安全，在塑料袋或塑料碗中腌制后请尽快将食材移至瓷容器或金属质容器中
* 为保证食品安全，请在洁净的砧板上处理生食食材与辅料
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201004138, recipe_name=普通面条, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

```text
命中关键词: 普通面条
食材名称: 普通面条
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=1
source: generation_context
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_817, recipe_name=炸酱面, category=主食, score=0.6696502566337585, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 挂面(150g)
2. 普通面条(250g)
3. 甜面酱(20g)
4. 肉丁/肉末(150g)
5. 菜码（黄瓜、白菜、萝卜等）(35g)
6. 葱(15g)
7. 蒜(适量g)
8. 豆瓣酱(20g)
9. 食用油(10g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=2
source: generation_context
metadata_summary: node_id=201004232, chunk_id=201004232_chunk_840, recipe_name=蒸卤面, category=主食, score=0.6381010413169861, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 五香粉(5g)
2. 大葱(10cm)
3. 大蒜(5瓣)
4. 姜片(20g)
5. 干红椒(3个)
6. 料酒
7. 猪五花肉(350g)
8. 生抽(15ml)
9. 盐(10g)
10. 老抽(10ml)
11. 花椒(20粒)
12. 芹菜(2根)
13. 青椒(2个)
14. 食用油
15. 鲜面条(500g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=3
source: generation_context
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6048961877822876, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=4
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7, recipe_name=凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

```text
技巧文档扩展上下文: 凉拌
关键技巧内容:
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
## 凉拌的目的
### 凉拌的目的

* 凉拌的目的在于对无味或味淡食材添加味道，例如鸡肋
## 凉拌能放什么
### 凉拌能放什么

包括但不限于：

* 主食材
* 辅料
* 腌制酱料
* 调味料
## 注意事项
### 注意事项

* 凉拌时应该注意食材安全，在不确认食材是否安全时，请勿凉拌对应食材，在确认食材不安全时不应凉拌对应食材
* 凉拌应尽可能加大主食菜的接触面积，故凉拌时推荐刀花、切片、拍碎甚至搅碎
* 凉拌菜对肠胃提出了基本要求，请在确认不会喷射或存有喷射时间时采用凉拌
* 文件撰写时处于新冠疫情状态下，建议将所有食材均在 100 摄氏度以上的环境中加热 15 秒以上以图心理安慰，若想求得安全请尽量避免凉拌
## 器具
## 器具

可以使用任何容器，从瓷缸到食品级塑料袋均可
## 注意事项
### 注意事项

* 为方便搅拌时食材不溅出，使用容积在所有食材两倍以上的硬质容器较为合适
* 为保证食品安全，在塑料袋或塑料碗中腌制后请尽快将食材移至瓷容器或金属质容器中
* 为保证食品安全，请在洁净的砧板上处理生食食材与辅料
```

