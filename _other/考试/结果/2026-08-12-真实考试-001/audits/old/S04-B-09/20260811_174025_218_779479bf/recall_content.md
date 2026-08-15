# Recall Content

audit_id: 20260811_174025_218_779479bf
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201003941, recipe_name=玉米, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 玉米
食材名称: 玉米
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=1
source: entity_level
metadata_summary: node_id=201004928, recipe_name=松仁玉米, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 松仁玉米
菜品名称: 松仁玉米
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### result_order=2
source: entity_level
metadata_summary: node_id=201003939, recipe_name=玉米排骨汤, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 玉米排骨汤
菜品名称: 玉米排骨汤
分类: 汤类
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
```

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=201004316, recipe_name=酸辣蕨根粉, category=主食,凉菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 酸辣蕨根粉
分类: 主食,凉菜
菜系: 川菜
难度: 2.0
主要食材: 油泼辣子, 盐, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 凉菜 (Category)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=1
source: topic_level
metadata_summary: node_id=201002203, recipe_name=凉拌鸡丝, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 凉拌鸡丝
分类: 荤菜
难度: 3.0
主要食材: 香醋, 盐, 鸡胸肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
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

### result_order=3
source: topic_level
metadata_summary: node_id=201002415, recipe_name=姜炒鸡, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 姜炒鸡
分类: 荤菜
菜系: 湘菜
难度: 3.0
主要食材: 生姜, 美人辣, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=4
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

### result_order=5
source: topic_level
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 咖喱炒蟹
分类: 水产
菜系: 泰国菜
难度: 4.0
主要食材: 青蟹, 咖喱块, 洋葱
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
- OUT REQUIRES 洋葱 (Ingredient): category: 蔬菜
```

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201000596, chunk_id=201000596_chunk_109, recipe_name=水煮玉米, category=早餐, score=0.6547605991363525, search_type=vector_enhanced

```text
# 水煮玉米
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 15-20分钟
份量: 1人份

## 所需食材
1. 新鲜玉米(1个)
2. 水(50毫升)
3. 盐(2克)
4. 糖

## 制作步骤

### 第1步
步骤: 步骤1
描述: 将新鲜玉米剥去外皮，剩部分玉米皮入锅
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 加入淹过玉米约半节指头的水，加盐和糖
方法: 加
工具: 锅

### 第3步
步骤: 步骤3
描述: 水煮开之后转至小火，加盖继续煮15-20分钟，玉米煮久点没事
方法: 煮
工具: 锅,锅盖
时间: 15-20分钟

### 第4步
步骤: 步骤4
描述: 煮熟后沥干水分，冷却后食用
方法: 沥水,冷却
工具: 漏勺
关联图谱:
- OUT REQUIRES 新鲜玉米 (Ingredient): category: 蔬菜
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 糖 (Ingredient): category: 调料
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201004928, chunk_id=201004928_chunk_968, recipe_name=松仁玉米, category=素菜, score=0.6378607749938965, search_type=vector_enhanced

```text
# 松仁玉米
难度: 2.0星

时间信息: 准备时间: 5分钟（切胡萝卜丁、焯水准备）, 烹饪时间: 5分钟（炒制全过程）
份量: 1人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201003275, chunk_id=201003275_chunk_644, recipe_name=贵州辣子鸡, category=荤菜, score=0.6089127659797668, search_type=vector_enhanced

```text
## 所需食材
1. 农村玉米鸡(4斤)
2. 啤酒(0.5瓶)
3. 土豆(2个)
4. 大蒜(2个)
5. 姜(2个)
6. 糍粑辣椒(500克)
7. 老抽(20毫升)
8. 花椒
9. 菜籽油(2斤)
10. 蒜苗(3根)
11. 豆瓣酱
12. 酒糟
13. 香叶(2片)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201004928, chunk_id=201004928_chunk_970, recipe_name=松仁玉米, category=素菜, score=0.6046335697174072, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒和胡萝卜丁提前焯水1分钟，捞出沥干备用
方法: 焯水
工具: 锅,漏勺
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 热锅凉油，放入胡萝卜丁略炒，再加入玉米粒翻炒
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第3步
步骤: 步骤3
描述: 加入白砂糖和盐，炒匀
方法: 炒
工具: 锅铲
时间: 20秒

### 第4步
步骤: 步骤4
描述: 混合水与淀粉成水淀粉，倒入锅中快速翻炒使汤汁略稠
方法: 炒
工具: 锅铲,小碗
时间: 20秒

### 第5步
步骤: 步骤5
描述: 加入熟松仁翻炒均匀
方法: 炒
工具: 锅铲
时间: 15秒

### 第6步
步骤: 步骤6
描述: 出锅装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201005435, chunk_id=201005435_chunk_1078, recipe_name=椒盐玉米, category=素菜, score=0.6027167439460754, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒解冻：温水泡15分钟或开水煮5分钟（带包装煮）
方法: 解冻
工具: 盆,锅
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 将解冻好的玉米粒倒入垫有吸油纸的簸箕BoxA，摇晃至吸油纸全湿
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第3步
步骤: 步骤3
描述: 将玉米粒转入第二个垫有吸油纸的簸箕BoxB，再次摇晃至吸油纸全湿，重复多次直至玉米表面无明显水滴但仍湿润
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第4步
步骤: 步骤4
描述: 倒入大量淀粉，摇晃簸箕使淀粉均匀裹住玉米粒
方法: 裹粉
工具: 塑料簸箕

### 第5步
步骤: 步骤5
描述: 锅中倒入适量油，加热至八成热
方法: 热锅,热油
工具: 锅

### 第6步
步骤: 步骤6
描述: 倒入裹好淀粉的玉米粒，中火先煎30秒不翻动
方法: 煎
工具: 锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 轻微翻炒3分钟后出锅
方法: 炒
工具: 锅铲
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 出锅后撒上椒盐3g和芝麻粒10g即可
方法: 调味

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201004588, chunk_id=201004588_chunk_913, recipe_name=火腿饭团, category=主食, score=0.5971590876579285, search_type=vector_enhanced

```text
## 所需食材
1. 冷冻玉米粒(30g)
2. 冷冻青豆(30g)
3. 水(90ml)
4. 沙拉酱(20g)
5. 海苔碎(10g)
6. 火腿(100g)
7. 米饭(125g)
8. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201002511, chunk_id=201002511_chunk_508, recipe_name=小炒黄牛肉, category=荤菜, score=0.5971286296844482, search_type=vector_enhanced

```text
## 所需食材
1. 小米椒(30g)
2. 牛里脊(400g)
3. 芹菜(200g)
4. 酱油(6ml)
5. 野山椒(30g)
6. 食用油(15ml)
7. 香菜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201005074, chunk_id=201005074_chunk_1005, recipe_name=脆皮豆腐, category=素菜, score=0.5951757431030273, search_type=vector_enhanced

```text
## 所需食材
1. 清水(200ml)
2. 玉米淀粉(50g)
3. 生抽(20g)
4. 白糖(10g)
5. 老抽(5g)
6. 老豆腐(1块)
7. 蚝油(10g)
8. 食用油(18ml)
9. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201005435, chunk_id=201005435_chunk_1076, recipe_name=椒盐玉米, category=素菜, score=0.5903434157371521, search_type=vector_enhanced

```text
# 椒盐玉米

菜系: 川菜
难度: 3.0星

时间信息: 准备时间: 15-20分钟, 烹饪时间: 4-5分钟
份量: 1份（川菜馆标准分量）

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5886499881744385, search_type=vector_enhanced

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

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201003941, recipe_name=玉米, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 玉米
食材名称: 玉米
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201004928, recipe_name=松仁玉米, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 松仁玉米
菜品名称: 松仁玉米
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201003939, recipe_name=玉米排骨汤, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 玉米排骨汤
菜品名称: 玉米排骨汤
分类: 汤类
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201004316, recipe_name=酸辣蕨根粉, category=主食,凉菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 酸辣蕨根粉
分类: 主食,凉菜
菜系: 川菜
难度: 2.0
主要食材: 油泼辣子, 盐, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 凉菜 (Category)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201002203, recipe_name=凉拌鸡丝, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 凉拌鸡丝
分类: 荤菜
难度: 3.0
主要食材: 香醋, 盐, 鸡胸肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=5
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

### result_order=6
source: branch_grouped
metadata_summary: node_id=201002415, recipe_name=姜炒鸡, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 姜炒鸡
分类: 荤菜
菜系: 湘菜
难度: 3.0
主要食材: 生姜, 美人辣, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=7
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

### result_order=8
source: branch_grouped
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 咖喱炒蟹
分类: 水产
菜系: 泰国菜
难度: 4.0
主要食材: 青蟹, 咖喱块, 洋葱
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
- OUT REQUIRES 洋葱 (Ingredient): category: 蔬菜
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201000596, chunk_id=201000596_chunk_109, recipe_name=水煮玉米, category=早餐, score=0.6547605991363525, search_type=vector_enhanced

```text
# 水煮玉米
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 15-20分钟
份量: 1人份

## 所需食材
1. 新鲜玉米(1个)
2. 水(50毫升)
3. 盐(2克)
4. 糖

## 制作步骤

### 第1步
步骤: 步骤1
描述: 将新鲜玉米剥去外皮，剩部分玉米皮入锅
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 加入淹过玉米约半节指头的水，加盐和糖
方法: 加
工具: 锅

### 第3步
步骤: 步骤3
描述: 水煮开之后转至小火，加盖继续煮15-20分钟，玉米煮久点没事
方法: 煮
工具: 锅,锅盖
时间: 15-20分钟

### 第4步
步骤: 步骤4
描述: 煮熟后沥干水分，冷却后食用
方法: 沥水,冷却
工具: 漏勺
关联图谱:
- OUT REQUIRES 新鲜玉米 (Ingredient): category: 蔬菜
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 糖 (Ingredient): category: 调料
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201004928, chunk_id=201004928_chunk_968, recipe_name=松仁玉米, category=素菜, score=0.6378607749938965, search_type=vector_enhanced

```text
# 松仁玉米
难度: 2.0星

时间信息: 准备时间: 5分钟（切胡萝卜丁、焯水准备）, 烹饪时间: 5分钟（炒制全过程）
份量: 1人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201003275, chunk_id=201003275_chunk_644, recipe_name=贵州辣子鸡, category=荤菜, score=0.6089127659797668, search_type=vector_enhanced

```text
## 所需食材
1. 农村玉米鸡(4斤)
2. 啤酒(0.5瓶)
3. 土豆(2个)
4. 大蒜(2个)
5. 姜(2个)
6. 糍粑辣椒(500克)
7. 老抽(20毫升)
8. 花椒
9. 菜籽油(2斤)
10. 蒜苗(3根)
11. 豆瓣酱
12. 酒糟
13. 香叶(2片)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201004928, chunk_id=201004928_chunk_970, recipe_name=松仁玉米, category=素菜, score=0.6046335697174072, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒和胡萝卜丁提前焯水1分钟，捞出沥干备用
方法: 焯水
工具: 锅,漏勺
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 热锅凉油，放入胡萝卜丁略炒，再加入玉米粒翻炒
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第3步
步骤: 步骤3
描述: 加入白砂糖和盐，炒匀
方法: 炒
工具: 锅铲
时间: 20秒

### 第4步
步骤: 步骤4
描述: 混合水与淀粉成水淀粉，倒入锅中快速翻炒使汤汁略稠
方法: 炒
工具: 锅铲,小碗
时间: 20秒

### 第5步
步骤: 步骤5
描述: 加入熟松仁翻炒均匀
方法: 炒
工具: 锅铲
时间: 15秒

### 第6步
步骤: 步骤6
描述: 出锅装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201005435, chunk_id=201005435_chunk_1078, recipe_name=椒盐玉米, category=素菜, score=0.6027167439460754, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒解冻：温水泡15分钟或开水煮5分钟（带包装煮）
方法: 解冻
工具: 盆,锅
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 将解冻好的玉米粒倒入垫有吸油纸的簸箕BoxA，摇晃至吸油纸全湿
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第3步
步骤: 步骤3
描述: 将玉米粒转入第二个垫有吸油纸的簸箕BoxB，再次摇晃至吸油纸全湿，重复多次直至玉米表面无明显水滴但仍湿润
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第4步
步骤: 步骤4
描述: 倒入大量淀粉，摇晃簸箕使淀粉均匀裹住玉米粒
方法: 裹粉
工具: 塑料簸箕

### 第5步
步骤: 步骤5
描述: 锅中倒入适量油，加热至八成热
方法: 热锅,热油
工具: 锅

### 第6步
步骤: 步骤6
描述: 倒入裹好淀粉的玉米粒，中火先煎30秒不翻动
方法: 煎
工具: 锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 轻微翻炒3分钟后出锅
方法: 炒
工具: 锅铲
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 出锅后撒上椒盐3g和芝麻粒10g即可
方法: 调味

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201004588, chunk_id=201004588_chunk_913, recipe_name=火腿饭团, category=主食, score=0.5971590876579285, search_type=vector_enhanced

```text
## 所需食材
1. 冷冻玉米粒(30g)
2. 冷冻青豆(30g)
3. 水(90ml)
4. 沙拉酱(20g)
5. 海苔碎(10g)
6. 火腿(100g)
7. 米饭(125g)
8. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=15
source: branch_grouped
metadata_summary: node_id=201002511, chunk_id=201002511_chunk_508, recipe_name=小炒黄牛肉, category=荤菜, score=0.5971286296844482, search_type=vector_enhanced

```text
## 所需食材
1. 小米椒(30g)
2. 牛里脊(400g)
3. 芹菜(200g)
4. 酱油(6ml)
5. 野山椒(30g)
6. 食用油(15ml)
7. 香菜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=16
source: branch_grouped
metadata_summary: node_id=201005074, chunk_id=201005074_chunk_1005, recipe_name=脆皮豆腐, category=素菜, score=0.5951757431030273, search_type=vector_enhanced

```text
## 所需食材
1. 清水(200ml)
2. 玉米淀粉(50g)
3. 生抽(20g)
4. 白糖(10g)
5. 老抽(5g)
6. 老豆腐(1块)
7. 蚝油(10g)
8. 食用油(18ml)
9. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=17
source: branch_grouped
metadata_summary: node_id=201005435, chunk_id=201005435_chunk_1076, recipe_name=椒盐玉米, category=素菜, score=0.5903434157371521, search_type=vector_enhanced

```text
# 椒盐玉米

菜系: 川菜
难度: 3.0星

时间信息: 准备时间: 15-20分钟, 烹饪时间: 4-5分钟
份量: 1份（川菜馆标准分量）

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=18
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5886499881744385, search_type=vector_enhanced

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

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201003941, recipe_name=玉米, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 玉米
食材名称: 玉米
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201004928, chunk_id=201004928_chunk_970, recipe_name=松仁玉米, category=素菜, score=0.6046335697174072, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒和胡萝卜丁提前焯水1分钟，捞出沥干备用
方法: 焯水
工具: 锅,漏勺
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 热锅凉油，放入胡萝卜丁略炒，再加入玉米粒翻炒
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第3步
步骤: 步骤3
描述: 加入白砂糖和盐，炒匀
方法: 炒
工具: 锅铲
时间: 20秒

### 第4步
步骤: 步骤4
描述: 混合水与淀粉成水淀粉，倒入锅中快速翻炒使汤汁略稠
方法: 炒
工具: 锅铲,小碗
时间: 20秒

### 第5步
步骤: 步骤5
描述: 加入熟松仁翻炒均匀
方法: 炒
工具: 锅铲
时间: 15秒

### 第6步
步骤: 步骤6
描述: 出锅装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201003939, recipe_name=玉米排骨汤, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 玉米排骨汤
菜品名称: 玉米排骨汤
分类: 汤类
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201004316, recipe_name=酸辣蕨根粉, category=主食,凉菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 酸辣蕨根粉
分类: 主食,凉菜
菜系: 川菜
难度: 2.0
主要食材: 油泼辣子, 盐, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 凉菜 (Category)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201002203, recipe_name=凉拌鸡丝, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 凉拌鸡丝
分类: 荤菜
难度: 3.0
主要食材: 香醋, 盐, 鸡胸肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=5
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

### result_order=6
source: merged_candidates
metadata_summary: node_id=201002415, recipe_name=姜炒鸡, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 姜炒鸡
分类: 荤菜
菜系: 湘菜
难度: 3.0
主要食材: 生姜, 美人辣, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=7
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

### result_order=8
source: merged_candidates
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 咖喱炒蟹
分类: 水产
菜系: 泰国菜
难度: 4.0
主要食材: 青蟹, 咖喱块, 洋葱
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
- OUT REQUIRES 洋葱 (Ingredient): category: 蔬菜
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=201000596, chunk_id=201000596_chunk_109, recipe_name=水煮玉米, category=早餐, score=0.6547605991363525, search_type=vector_enhanced

```text
# 水煮玉米
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 15-20分钟
份量: 1人份

## 所需食材
1. 新鲜玉米(1个)
2. 水(50毫升)
3. 盐(2克)
4. 糖

## 制作步骤

### 第1步
步骤: 步骤1
描述: 将新鲜玉米剥去外皮，剩部分玉米皮入锅
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 加入淹过玉米约半节指头的水，加盐和糖
方法: 加
工具: 锅

### 第3步
步骤: 步骤3
描述: 水煮开之后转至小火，加盖继续煮15-20分钟，玉米煮久点没事
方法: 煮
工具: 锅,锅盖
时间: 15-20分钟

### 第4步
步骤: 步骤4
描述: 煮熟后沥干水分，冷却后食用
方法: 沥水,冷却
工具: 漏勺
关联图谱:
- OUT REQUIRES 新鲜玉米 (Ingredient): category: 蔬菜
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 糖 (Ingredient): category: 调料
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201003275, chunk_id=201003275_chunk_644, recipe_name=贵州辣子鸡, category=荤菜, score=0.6089127659797668, search_type=vector_enhanced

```text
## 所需食材
1. 农村玉米鸡(4斤)
2. 啤酒(0.5瓶)
3. 土豆(2个)
4. 大蒜(2个)
5. 姜(2个)
6. 糍粑辣椒(500克)
7. 老抽(20毫升)
8. 花椒
9. 菜籽油(2斤)
10. 蒜苗(3根)
11. 豆瓣酱
12. 酒糟
13. 香叶(2片)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=201005435, chunk_id=201005435_chunk_1078, recipe_name=椒盐玉米, category=素菜, score=0.6027167439460754, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒解冻：温水泡15分钟或开水煮5分钟（带包装煮）
方法: 解冻
工具: 盆,锅
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 将解冻好的玉米粒倒入垫有吸油纸的簸箕BoxA，摇晃至吸油纸全湿
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第3步
步骤: 步骤3
描述: 将玉米粒转入第二个垫有吸油纸的簸箕BoxB，再次摇晃至吸油纸全湿，重复多次直至玉米表面无明显水滴但仍湿润
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第4步
步骤: 步骤4
描述: 倒入大量淀粉，摇晃簸箕使淀粉均匀裹住玉米粒
方法: 裹粉
工具: 塑料簸箕

### 第5步
步骤: 步骤5
描述: 锅中倒入适量油，加热至八成热
方法: 热锅,热油
工具: 锅

### 第6步
步骤: 步骤6
描述: 倒入裹好淀粉的玉米粒，中火先煎30秒不翻动
方法: 煎
工具: 锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 轻微翻炒3分钟后出锅
方法: 炒
工具: 锅铲
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 出锅后撒上椒盐3g和芝麻粒10g即可
方法: 调味

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=201004588, chunk_id=201004588_chunk_913, recipe_name=火腿饭团, category=主食, score=0.5971590876579285, search_type=vector_enhanced

```text
## 所需食材
1. 冷冻玉米粒(30g)
2. 冷冻青豆(30g)
3. 水(90ml)
4. 沙拉酱(20g)
5. 海苔碎(10g)
6. 火腿(100g)
7. 米饭(125g)
8. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=13
source: merged_candidates
metadata_summary: node_id=201002511, chunk_id=201002511_chunk_508, recipe_name=小炒黄牛肉, category=荤菜, score=0.5971286296844482, search_type=vector_enhanced

```text
## 所需食材
1. 小米椒(30g)
2. 牛里脊(400g)
3. 芹菜(200g)
4. 酱油(6ml)
5. 野山椒(30g)
6. 食用油(15ml)
7. 香菜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=14
source: merged_candidates
metadata_summary: node_id=201005074, chunk_id=201005074_chunk_1005, recipe_name=脆皮豆腐, category=素菜, score=0.5951757431030273, search_type=vector_enhanced

```text
## 所需食材
1. 清水(200ml)
2. 玉米淀粉(50g)
3. 生抽(20g)
4. 白糖(10g)
5. 老抽(5g)
6. 老豆腐(1块)
7. 蚝油(10g)
8. 食用油(18ml)
9. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=15
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5886499881744385, search_type=vector_enhanced

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

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 玉米
食材名称: 玉米
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=1
source: rerank_input

```text
菜品: 松仁玉米
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒和胡萝卜丁提前焯水1分钟，捞出沥干备用
方法: 焯水
工具: 锅,漏勺
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 热锅凉油，放入胡萝卜丁略炒，再加入玉米粒翻炒
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第3步
步骤: 步骤3
描述: 加入白砂糖和盐，炒匀
方法: 炒
工具: 锅铲
时间: 20秒

### 第4步
步骤: 步骤4
描述: 混合水与淀粉成水淀粉，倒入锅中快速翻炒使汤汁略稠
方法: 炒
工具: 锅铲,小碗
时间: 20秒

### 第5步
步骤: 步骤5
描述: 加入熟松仁翻炒均匀
方法: 炒
工具: 锅铲
时间: 15秒

### 第6步
步骤: 步骤6
描述: 出锅装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 玉米排骨汤
菜品名称: 玉米排骨汤
分类: 汤类
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
```

### pair_order=3
source: rerank_input

```text
命中关键词: 快手菜
菜品: 酸辣蕨根粉
分类: 主食,凉菜
菜系: 川菜
难度: 2.0
主要食材: 油泼辣子, 盐, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 凉菜 (Category)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### pair_order=4
source: rerank_input

```text
命中关键词: 快手菜
菜品: 凉拌鸡丝
分类: 荤菜
难度: 3.0
主要食材: 香醋, 盐, 鸡胸肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=5
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

### pair_order=6
source: rerank_input

```text
命中关键词: 快手菜
菜品: 姜炒鸡
分类: 荤菜
菜系: 湘菜
难度: 3.0
主要食材: 生姜, 美人辣, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=7
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

### pair_order=8
source: rerank_input

```text
命中关键词: 快手菜
菜品: 咖喱炒蟹
分类: 水产
菜系: 泰国菜
难度: 4.0
主要食材: 青蟹, 咖喱块, 洋葱
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
- OUT REQUIRES 洋葱 (Ingredient): category: 蔬菜
```

### pair_order=9
source: rerank_input

```text
分类: 早餐
菜系: 未知
# 水煮玉米
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 15-20分钟
份量: 1人份

## 所需食材
1. 新鲜玉米(1个)
2. 水(50毫升)
3. 盐(2克)
4. 糖

## 制作步骤

### 第1步
步骤: 步骤1
描述: 将新鲜玉米剥去外皮，剩部分玉米皮入锅
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 加入淹过玉米约半节指头的水，加盐和糖
方法: 加
工具: 锅

### 第3步
步骤: 步骤3
描述: 水煮开之后转至小火，加盖继续煮15-20分钟，玉米煮久点没事
方法: 煮
工具: 锅,锅盖
时间: 15-20分钟

### 第4步
步骤: 步骤4
描述: 煮熟后沥干水分，冷却后食用
方法: 沥水,冷却
工具: 漏勺
关联图谱:
- OUT REQUIRES 新鲜玉米 (Ingredient): category: 蔬菜
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 糖 (Ingredient): category: 调料
```

### pair_order=10
source: rerank_input

```text
菜品: 贵州辣子鸡
菜系: 黔菜
## 所需食材
1. 农村玉米鸡(4斤)
2. 啤酒(0.5瓶)
3. 土豆(2个)
4. 大蒜(2个)
5. 姜(2个)
6. 糍粑辣椒(500克)
7. 老抽(20毫升)
8. 花椒
9. 菜籽油(2斤)
10. 蒜苗(3根)
11. 豆瓣酱
12. 酒糟
13. 香叶(2片)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=11
source: rerank_input

```text
菜品: 椒盐玉米
菜系: 川菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒解冻：温水泡15分钟或开水煮5分钟（带包装煮）
方法: 解冻
工具: 盆,锅
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 将解冻好的玉米粒倒入垫有吸油纸的簸箕BoxA，摇晃至吸油纸全湿
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第3步
步骤: 步骤3
描述: 将玉米粒转入第二个垫有吸油纸的簸箕BoxB，再次摇晃至吸油纸全湿，重复多次直至玉米表面无明显水滴但仍湿润
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第4步
步骤: 步骤4
描述: 倒入大量淀粉，摇晃簸箕使淀粉均匀裹住玉米粒
方法: 裹粉
工具: 塑料簸箕

### 第5步
步骤: 步骤5
描述: 锅中倒入适量油，加热至八成热
方法: 热锅,热油
工具: 锅

### 第6步
步骤: 步骤6
描述: 倒入裹好淀粉的玉米粒，中火先煎30秒不翻动
方法: 煎
工具: 锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 轻微翻炒3分钟后出锅
方法: 炒
工具: 锅铲
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 出锅后撒上椒盐3g和芝麻粒10g即可
方法: 调味

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=12
source: rerank_input

```text
菜品: 火腿饭团
菜系: 未知
## 所需食材
1. 冷冻玉米粒(30g)
2. 冷冻青豆(30g)
3. 水(90ml)
4. 沙拉酱(20g)
5. 海苔碎(10g)
6. 火腿(100g)
7. 米饭(125g)
8. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=13
source: rerank_input

```text
菜品: 小炒黄牛肉
菜系: 湘菜
## 所需食材
1. 小米椒(30g)
2. 牛里脊(400g)
3. 芹菜(200g)
4. 酱油(6ml)
5. 野山椒(30g)
6. 食用油(15ml)
7. 香菜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=14
source: rerank_input

```text
菜品: 脆皮豆腐
菜系: 未知
## 所需食材
1. 清水(200ml)
2. 玉米淀粉(50g)
3. 生抽(20g)
4. 白糖(10g)
5. 老抽(5g)
6. 老豆腐(1块)
7. 蚝油(10g)
8. 食用油(18ml)
9. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=15
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

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201004928, chunk_id=201004928_chunk_970, recipe_name=松仁玉米, category=素菜, score=0.6046335697174072, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒和胡萝卜丁提前焯水1分钟，捞出沥干备用
方法: 焯水
工具: 锅,漏勺
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 热锅凉油，放入胡萝卜丁略炒，再加入玉米粒翻炒
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第3步
步骤: 步骤3
描述: 加入白砂糖和盐，炒匀
方法: 炒
工具: 锅铲
时间: 20秒

### 第4步
步骤: 步骤4
描述: 混合水与淀粉成水淀粉，倒入锅中快速翻炒使汤汁略稠
方法: 炒
工具: 锅铲,小碗
时间: 20秒

### 第5步
步骤: 步骤5
描述: 加入熟松仁翻炒均匀
方法: 炒
工具: 锅铲
时间: 15秒

### 第6步
步骤: 步骤6
描述: 出锅装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201005435, chunk_id=201005435_chunk_1078, recipe_name=椒盐玉米, category=素菜, score=0.6027167439460754, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒解冻：温水泡15分钟或开水煮5分钟（带包装煮）
方法: 解冻
工具: 盆,锅
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 将解冻好的玉米粒倒入垫有吸油纸的簸箕BoxA，摇晃至吸油纸全湿
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第3步
步骤: 步骤3
描述: 将玉米粒转入第二个垫有吸油纸的簸箕BoxB，再次摇晃至吸油纸全湿，重复多次直至玉米表面无明显水滴但仍湿润
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第4步
步骤: 步骤4
描述: 倒入大量淀粉，摇晃簸箕使淀粉均匀裹住玉米粒
方法: 裹粉
工具: 塑料簸箕

### 第5步
步骤: 步骤5
描述: 锅中倒入适量油，加热至八成热
方法: 热锅,热油
工具: 锅

### 第6步
步骤: 步骤6
描述: 倒入裹好淀粉的玉米粒，中火先煎30秒不翻动
方法: 煎
工具: 锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 轻微翻炒3分钟后出锅
方法: 炒
工具: 锅铲
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 出锅后撒上椒盐3g和芝麻粒10g即可
方法: 调味

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201000596, chunk_id=201000596_chunk_109, recipe_name=水煮玉米, category=早餐, score=0.6547605991363525, search_type=vector_enhanced

```text
# 水煮玉米
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 15-20分钟
份量: 1人份

## 所需食材
1. 新鲜玉米(1个)
2. 水(50毫升)
3. 盐(2克)
4. 糖

## 制作步骤

### 第1步
步骤: 步骤1
描述: 将新鲜玉米剥去外皮，剩部分玉米皮入锅
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 加入淹过玉米约半节指头的水，加盐和糖
方法: 加
工具: 锅

### 第3步
步骤: 步骤3
描述: 水煮开之后转至小火，加盖继续煮15-20分钟，玉米煮久点没事
方法: 煮
工具: 锅,锅盖
时间: 15-20分钟

### 第4步
步骤: 步骤4
描述: 煮熟后沥干水分，冷却后食用
方法: 沥水,冷却
工具: 漏勺
关联图谱:
- OUT REQUIRES 新鲜玉米 (Ingredient): category: 蔬菜
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 糖 (Ingredient): category: 调料
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201003275, chunk_id=201003275_chunk_644, recipe_name=贵州辣子鸡, category=荤菜, score=0.6089127659797668, search_type=vector_enhanced

```text
## 所需食材
1. 农村玉米鸡(4斤)
2. 啤酒(0.5瓶)
3. 土豆(2个)
4. 大蒜(2个)
5. 姜(2个)
6. 糍粑辣椒(500克)
7. 老抽(20毫升)
8. 花椒
9. 菜籽油(2斤)
10. 蒜苗(3根)
11. 豆瓣酱
12. 酒糟
13. 香叶(2片)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201003939, recipe_name=玉米排骨汤, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 玉米排骨汤
菜品名称: 玉米排骨汤
分类: 汤类
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201005074, chunk_id=201005074_chunk_1005, recipe_name=脆皮豆腐, category=素菜, score=0.5951757431030273, search_type=vector_enhanced

```text
## 所需食材
1. 清水(200ml)
2. 玉米淀粉(50g)
3. 生抽(20g)
4. 白糖(10g)
5. 老抽(5g)
6. 老豆腐(1块)
7. 蚝油(10g)
8. 食用油(18ml)
9. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201003941, recipe_name=玉米, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 玉米
食材名称: 玉米
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201004588, chunk_id=201004588_chunk_913, recipe_name=火腿饭团, category=主食, score=0.5971590876579285, search_type=vector_enhanced

```text
## 所需食材
1. 冷冻玉米粒(30g)
2. 冷冻青豆(30g)
3. 水(90ml)
4. 沙拉酱(20g)
5. 海苔碎(10g)
6. 火腿(100g)
7. 米饭(125g)
8. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5886499881744385, search_type=vector_enhanced

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

### result_order=9
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

### result_order=10
source: reranked_results
metadata_summary: node_id=201004316, recipe_name=酸辣蕨根粉, category=主食,凉菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 酸辣蕨根粉
分类: 主食,凉菜
菜系: 川菜
难度: 2.0
主要食材: 油泼辣子, 盐, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 凉菜 (Category)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=11
source: reranked_results
metadata_summary: node_id=201002415, recipe_name=姜炒鸡, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 姜炒鸡
分类: 荤菜
菜系: 湘菜
难度: 3.0
主要食材: 生姜, 美人辣, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=12
source: reranked_results
metadata_summary: node_id=201002511, chunk_id=201002511_chunk_508, recipe_name=小炒黄牛肉, category=荤菜, score=0.5971286296844482, search_type=vector_enhanced

```text
## 所需食材
1. 小米椒(30g)
2. 牛里脊(400g)
3. 芹菜(200g)
4. 酱油(6ml)
5. 野山椒(30g)
6. 食用油(15ml)
7. 香菜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=13
source: reranked_results
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 咖喱炒蟹
分类: 水产
菜系: 泰国菜
难度: 4.0
主要食材: 青蟹, 咖喱块, 洋葱
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
- OUT REQUIRES 洋葱 (Ingredient): category: 蔬菜
```

### result_order=14
source: reranked_results
metadata_summary: node_id=201002203, recipe_name=凉拌鸡丝, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 凉拌鸡丝
分类: 荤菜
难度: 3.0
主要食材: 香醋, 盐, 鸡胸肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=15
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
metadata_summary: node_id=201004928, chunk_id=201004928_chunk_970, recipe_name=松仁玉米, category=素菜, score=0.6046335697174072, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒和胡萝卜丁提前焯水1分钟，捞出沥干备用
方法: 焯水
工具: 锅,漏勺
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 热锅凉油，放入胡萝卜丁略炒，再加入玉米粒翻炒
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第3步
步骤: 步骤3
描述: 加入白砂糖和盐，炒匀
方法: 炒
工具: 锅铲
时间: 20秒

### 第4步
步骤: 步骤4
描述: 混合水与淀粉成水淀粉，倒入锅中快速翻炒使汤汁略稠
方法: 炒
工具: 锅铲,小碗
时间: 20秒

### 第5步
步骤: 步骤5
描述: 加入熟松仁翻炒均匀
方法: 炒
工具: 锅铲
时间: 15秒

### 第6步
步骤: 步骤6
描述: 出锅装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201005435, chunk_id=201005435_chunk_1078, recipe_name=椒盐玉米, category=素菜, score=0.6027167439460754, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒解冻：温水泡15分钟或开水煮5分钟（带包装煮）
方法: 解冻
工具: 盆,锅
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 将解冻好的玉米粒倒入垫有吸油纸的簸箕BoxA，摇晃至吸油纸全湿
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第3步
步骤: 步骤3
描述: 将玉米粒转入第二个垫有吸油纸的簸箕BoxB，再次摇晃至吸油纸全湿，重复多次直至玉米表面无明显水滴但仍湿润
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第4步
步骤: 步骤4
描述: 倒入大量淀粉，摇晃簸箕使淀粉均匀裹住玉米粒
方法: 裹粉
工具: 塑料簸箕

### 第5步
步骤: 步骤5
描述: 锅中倒入适量油，加热至八成热
方法: 热锅,热油
工具: 锅

### 第6步
步骤: 步骤6
描述: 倒入裹好淀粉的玉米粒，中火先煎30秒不翻动
方法: 煎
工具: 锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 轻微翻炒3分钟后出锅
方法: 炒
工具: 锅铲
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 出锅后撒上椒盐3g和芝麻粒10g即可
方法: 调味

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201000596, chunk_id=201000596_chunk_109, recipe_name=水煮玉米, category=早餐, score=0.6547605991363525, search_type=vector_enhanced

```text
# 水煮玉米
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 15-20分钟
份量: 1人份

## 所需食材
1. 新鲜玉米(1个)
2. 水(50毫升)
3. 盐(2克)
4. 糖

## 制作步骤

### 第1步
步骤: 步骤1
描述: 将新鲜玉米剥去外皮，剩部分玉米皮入锅
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 加入淹过玉米约半节指头的水，加盐和糖
方法: 加
工具: 锅

### 第3步
步骤: 步骤3
描述: 水煮开之后转至小火，加盖继续煮15-20分钟，玉米煮久点没事
方法: 煮
工具: 锅,锅盖
时间: 15-20分钟

### 第4步
步骤: 步骤4
描述: 煮熟后沥干水分，冷却后食用
方法: 沥水,冷却
工具: 漏勺
关联图谱:
- OUT REQUIRES 新鲜玉米 (Ingredient): category: 蔬菜
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 糖 (Ingredient): category: 调料
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201003275, chunk_id=201003275_chunk_644, recipe_name=贵州辣子鸡, category=荤菜, score=0.6089127659797668, search_type=vector_enhanced

```text
## 所需食材
1. 农村玉米鸡(4斤)
2. 啤酒(0.5瓶)
3. 土豆(2个)
4. 大蒜(2个)
5. 姜(2个)
6. 糍粑辣椒(500克)
7. 老抽(20毫升)
8. 花椒
9. 菜籽油(2斤)
10. 蒜苗(3根)
11. 豆瓣酱
12. 酒糟
13. 香叶(2片)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=201003939, recipe_name=玉米排骨汤, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 玉米排骨汤
菜品名称: 玉米排骨汤
分类: 汤类
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201004928, chunk_id=201004928_chunk_970, recipe_name=松仁玉米, category=素菜, score=0.6046335697174072, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒和胡萝卜丁提前焯水1分钟，捞出沥干备用
方法: 焯水
工具: 锅,漏勺
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 热锅凉油，放入胡萝卜丁略炒，再加入玉米粒翻炒
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第3步
步骤: 步骤3
描述: 加入白砂糖和盐，炒匀
方法: 炒
工具: 锅铲
时间: 20秒

### 第4步
步骤: 步骤4
描述: 混合水与淀粉成水淀粉，倒入锅中快速翻炒使汤汁略稠
方法: 炒
工具: 锅铲,小碗
时间: 20秒

### 第5步
步骤: 步骤5
描述: 加入熟松仁翻炒均匀
方法: 炒
工具: 锅铲
时间: 15秒

### 第6步
步骤: 步骤6
描述: 出锅装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=1
source: generation_context
metadata_summary: node_id=201005435, chunk_id=201005435_chunk_1078, recipe_name=椒盐玉米, category=素菜, score=0.6027167439460754, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 玉米粒解冻：温水泡15分钟或开水煮5分钟（带包装煮）
方法: 解冻
工具: 盆,锅
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 将解冻好的玉米粒倒入垫有吸油纸的簸箕BoxA，摇晃至吸油纸全湿
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第3步
步骤: 步骤3
描述: 将玉米粒转入第二个垫有吸油纸的簸箕BoxB，再次摇晃至吸油纸全湿，重复多次直至玉米表面无明显水滴但仍湿润
方法: 沥水
工具: 塑料簸箕,吸油纸

### 第4步
步骤: 步骤4
描述: 倒入大量淀粉，摇晃簸箕使淀粉均匀裹住玉米粒
方法: 裹粉
工具: 塑料簸箕

### 第5步
步骤: 步骤5
描述: 锅中倒入适量油，加热至八成热
方法: 热锅,热油
工具: 锅

### 第6步
步骤: 步骤6
描述: 倒入裹好淀粉的玉米粒，中火先煎30秒不翻动
方法: 煎
工具: 锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 轻微翻炒3分钟后出锅
方法: 炒
工具: 锅铲
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 出锅后撒上椒盐3g和芝麻粒10g即可
方法: 调味

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=2
source: generation_context
metadata_summary: node_id=201000596, chunk_id=201000596_chunk_109, recipe_name=水煮玉米, category=早餐, score=0.6547605991363525, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
# 水煮玉米
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 15-20分钟
份量: 1人份

## 所需食材
1. 新鲜玉米(1个)
2. 水(50毫升)
3. 盐(2克)
4. 糖

## 制作步骤

### 第1步
步骤: 步骤1
描述: 将新鲜玉米剥去外皮，剩部分玉米皮入锅
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 加入淹过玉米约半节指头的水，加盐和糖
方法: 加
工具: 锅

### 第3步
步骤: 步骤3
描述: 水煮开之后转至小火，加盖继续煮15-20分钟，玉米煮久点没事
方法: 煮
工具: 锅,锅盖
时间: 15-20分钟

### 第4步
步骤: 步骤4
描述: 煮熟后沥干水分，冷却后食用
方法: 沥水,冷却
工具: 漏勺
关联图谱:
- OUT REQUIRES 新鲜玉米 (Ingredient): category: 蔬菜
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 糖 (Ingredient): category: 调料
```

### result_order=3
source: generation_context
metadata_summary: node_id=201003275, chunk_id=201003275_chunk_644, recipe_name=贵州辣子鸡, category=荤菜, score=0.6089127659797668, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 农村玉米鸡(4斤)
2. 啤酒(0.5瓶)
3. 土豆(2个)
4. 大蒜(2个)
5. 姜(2个)
6. 糍粑辣椒(500克)
7. 老抽(20毫升)
8. 花椒
9. 菜籽油(2斤)
10. 蒜苗(3根)
11. 豆瓣酱
12. 酒糟
13. 香叶(2片)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=4
source: generation_context
metadata_summary: node_id=201003939, recipe_name=玉米排骨汤, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

```text
命中关键词: 玉米排骨汤
菜品名称: 玉米排骨汤
分类: 汤类
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
```

