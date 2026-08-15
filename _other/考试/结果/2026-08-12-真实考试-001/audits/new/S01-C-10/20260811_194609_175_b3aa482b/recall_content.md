# Recall Content

audit_id: 20260811_194609_175_b3aa482b
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201003210, recipe_name=西红柿, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西红柿
食材名称: 西红柿
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=1
source: entity_level
metadata_summary: node_id=201001901, recipe_name=土豆, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 土豆
食材名称: 土豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
source: entity_level
metadata_summary: node_id=201001631, recipe_name=牛肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 牛肉
食材名称: 牛肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=3
source: entity_level
metadata_summary: node_id=201003196, recipe_name=西红柿土豆炖牛肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西红柿土豆炖牛肉
菜品名称: 西红柿土豆炖牛肉
分类: 荤菜
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
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_627, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.7256419658660889, search_type=vector_enhanced

```text
# 西红柿土豆炖牛肉
难度: 4.0星

时间信息: 准备时间: 约20分钟, 烹饪时间: 60-90分钟
份量: 3-4人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201001852, chunk_id=201001852_chunk_394, recipe_name=番茄红酱, category=荤菜, score=0.7056230902671814, search_type=vector_enhanced

```text
## 标签
考虑各个品牌的番茄酱内含盐量不同，建议在炒牛肉时少放盐，煮的时候尝一下再调味,煮酱料期间请搅动，以免粘锅。如果酱料变粘稠就可以出锅啦！,可将碎牛肉替换成一半碎猪肉一半碎牛肉，牛奶替换成鸡汤或饮用水
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201003224, chunk_id=201003224_chunk_633, recipe_name=西红柿牛腩, category=荤菜, score=0.6962799429893494, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 牛腩切条、切块成长宽高均2cm，冷水下锅，开锅煮制2分钟去除血水，捞出冲洗干净
方法: 切,煮
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 另起锅2L水烧开，加入2cm两段葱段、两片姜片、八角、料酒5-10ml，放入焯好的牛肉，盖盖炖制（砂锅1小时，高压锅炖肉模式45分钟），筷子能轻松插透就证明炖好了
方法: 炖
工具: 砂锅/高压锅/铝锅,筷子
时间: 45-60分钟

### 第3步
步骤: 步骤3
描述: 西红柿去皮：西红柿头部滑十字至腰线，筷子/刀叉从果蒂捅入，煤气灶小火，一边转动一边烤，及时拿下来查看，起皮后撕下来，切块。越小越好
方法: 烤,切
工具: 刀,筷子/刀叉,煤气灶
时间: 5分钟

### 第4步
步骤: 步骤4
描述: 起锅烧油，油温7成热，葱、姜各10g，番茄下锅，炒透炒出番茄红色，加入煮好的牛腩和原汤，原汤刚刚没过牛肉即可
方法: 炒
工具: 炒锅,锅铲
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 根据个人口味放入盐、糖、生抽调味盖盖
方法: 调味
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 开锅后大火继续炒制3-5分钟
方法: 炒
工具: 锅铲
时间: 3-5分钟

### 第7步
步骤: 步骤7
描述: 待番茄汁呈中等粘稠程度后关火，散入葱花，盛盘
方法: 收汁,装盘
工具: 锅铲
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.681769609451294, search_type=vector_enhanced

```text
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201003224, chunk_id=201003224_chunk_634, recipe_name=西红柿牛腩, category=荤菜, score=0.6764702796936035, search_type=vector_enhanced

```text
## 标签
用火注意安全,砂锅/铝锅炖肉时水开后转中小火/小火,番茄去皮方法：十字刀+小火旋转烤,不用番茄酱，少加佐料，还原食材原味
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_629, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.6730093955993652, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 土豆去皮、切成5cm大块，备用
方法: 切
工具: 刀,案板
时间: 3-5分钟

### 第2步
步骤: 步骤2
描述: 西红柿切十字花刀，开水烫后去皮，去芯，切3cm小块备用
方法: 切,烫
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 葱切4g葱花，其余掰成5-8cm大段；洋葱切0.5-1cm小粒
方法: 切
工具: 刀,案板
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 牛肉泡凉水半小时去血水，或凉水下锅煮至表面变白捞出，期间撇去浮沫
方法: 焯水
工具: 锅,漏勺
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 凉水没过牛肉，放入高压锅，加葱段、姜片、20g料酒，上汽压20分钟
方法: 炖
工具: 高压锅
时间: 20分钟

### 第6步
步骤: 步骤6
描述: 取出牛肉切5cm大块，挑出姜片，汤盛碗备用
方法: 切
工具: 刀,案板,碗
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 锅中倒油，油4-5成热下花椒、八角、香叶，出香味后捞出不用
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 下牛肉、葱姜炒香，必要时加少量牛肉汤防糊
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第9步
步骤: 步骤9
描述: 加生抽15ml、料酒15ml、胡椒粉、5-10g番茄酱或番茄罐头，加洋葱炒至透明
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿炒至软烂，倒入剩余牛肉汤
方法: 炒,炖
工具: 炒锅,锅铲
时间: 3-5分钟

### 第11步
步骤: 步骤11
描述: 中火开锅后转小火，出锅前30-40分钟加入土豆并调味，边尝边加糖盐
方法: 炖,调味
工具: 锅,筷子
时间: 30-40分钟

### 第12步
步骤: 步骤12
描述: 筷子能轻松戳透牛肉时即可关火出锅
方法: 检查
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201002920, chunk_id=201002920_chunk_578, recipe_name=瘦肉土豆片, category=荤菜, score=0.6641399264335632, search_type=vector_enhanced

```text
## 标签
土豆片焯水不宜太久，防止变软,腌制瘦肉需搅拌均匀
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201004898, chunk_id=201004898_chunk_966, recipe_name=地三鲜, category=素菜, score=0.6529252529144287, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(150g)
2. 姜(10g)
3. 尖椒(3.5个)
4. 水(200ml)
5. 淀粉(20g)
6. 生抽(10ml)
7. 盐(8g)
8. 糖(10g)
9. 茄子(100g)
10. 葱(3g)
11. 蒜(10g)
12. 豆瓣酱(20ml)
13. 食用油(40ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6514846682548523, search_type=vector_enhanced

```text
## 所需食材
1. 洋葱(30g)
2. 火腿肠(50g)
3. 牛奶(10ml)
4. 玉米粒(30g)
5. 番茄酱(20ml)
6. 米饭(200g)
7. 胡萝卜(30g)
8. 青豆(30g)
9. 食用油(15ml)
10. 鸡胸肉(50g)
11. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6483234167098999, search_type=vector_enhanced

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
metadata_summary: node_id=201003210, recipe_name=西红柿, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西红柿
食材名称: 西红柿
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201001901, recipe_name=土豆, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 土豆
食材名称: 土豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201001631, recipe_name=牛肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 牛肉
食材名称: 牛肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201003196, recipe_name=西红柿土豆炖牛肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西红柿土豆炖牛肉
菜品名称: 西红柿土豆炖牛肉
分类: 荤菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=4
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
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_627, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.7256419658660889, search_type=vector_enhanced

```text
# 西红柿土豆炖牛肉
难度: 4.0星

时间信息: 准备时间: 约20分钟, 烹饪时间: 60-90分钟
份量: 3-4人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201001852, chunk_id=201001852_chunk_394, recipe_name=番茄红酱, category=荤菜, score=0.7056230902671814, search_type=vector_enhanced

```text
## 标签
考虑各个品牌的番茄酱内含盐量不同，建议在炒牛肉时少放盐，煮的时候尝一下再调味,煮酱料期间请搅动，以免粘锅。如果酱料变粘稠就可以出锅啦！,可将碎牛肉替换成一半碎猪肉一半碎牛肉，牛奶替换成鸡汤或饮用水
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201003224, chunk_id=201003224_chunk_633, recipe_name=西红柿牛腩, category=荤菜, score=0.6962799429893494, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 牛腩切条、切块成长宽高均2cm，冷水下锅，开锅煮制2分钟去除血水，捞出冲洗干净
方法: 切,煮
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 另起锅2L水烧开，加入2cm两段葱段、两片姜片、八角、料酒5-10ml，放入焯好的牛肉，盖盖炖制（砂锅1小时，高压锅炖肉模式45分钟），筷子能轻松插透就证明炖好了
方法: 炖
工具: 砂锅/高压锅/铝锅,筷子
时间: 45-60分钟

### 第3步
步骤: 步骤3
描述: 西红柿去皮：西红柿头部滑十字至腰线，筷子/刀叉从果蒂捅入，煤气灶小火，一边转动一边烤，及时拿下来查看，起皮后撕下来，切块。越小越好
方法: 烤,切
工具: 刀,筷子/刀叉,煤气灶
时间: 5分钟

### 第4步
步骤: 步骤4
描述: 起锅烧油，油温7成热，葱、姜各10g，番茄下锅，炒透炒出番茄红色，加入煮好的牛腩和原汤，原汤刚刚没过牛肉即可
方法: 炒
工具: 炒锅,锅铲
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 根据个人口味放入盐、糖、生抽调味盖盖
方法: 调味
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 开锅后大火继续炒制3-5分钟
方法: 炒
工具: 锅铲
时间: 3-5分钟

### 第7步
步骤: 步骤7
描述: 待番茄汁呈中等粘稠程度后关火，散入葱花，盛盘
方法: 收汁,装盘
工具: 锅铲
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.681769609451294, search_type=vector_enhanced

```text
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201003224, chunk_id=201003224_chunk_634, recipe_name=西红柿牛腩, category=荤菜, score=0.6764702796936035, search_type=vector_enhanced

```text
## 标签
用火注意安全,砂锅/铝锅炖肉时水开后转中小火/小火,番茄去皮方法：十字刀+小火旋转烤,不用番茄酱，少加佐料，还原食材原味
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_629, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.6730093955993652, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 土豆去皮、切成5cm大块，备用
方法: 切
工具: 刀,案板
时间: 3-5分钟

### 第2步
步骤: 步骤2
描述: 西红柿切十字花刀，开水烫后去皮，去芯，切3cm小块备用
方法: 切,烫
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 葱切4g葱花，其余掰成5-8cm大段；洋葱切0.5-1cm小粒
方法: 切
工具: 刀,案板
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 牛肉泡凉水半小时去血水，或凉水下锅煮至表面变白捞出，期间撇去浮沫
方法: 焯水
工具: 锅,漏勺
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 凉水没过牛肉，放入高压锅，加葱段、姜片、20g料酒，上汽压20分钟
方法: 炖
工具: 高压锅
时间: 20分钟

### 第6步
步骤: 步骤6
描述: 取出牛肉切5cm大块，挑出姜片，汤盛碗备用
方法: 切
工具: 刀,案板,碗
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 锅中倒油，油4-5成热下花椒、八角、香叶，出香味后捞出不用
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 下牛肉、葱姜炒香，必要时加少量牛肉汤防糊
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第9步
步骤: 步骤9
描述: 加生抽15ml、料酒15ml、胡椒粉、5-10g番茄酱或番茄罐头，加洋葱炒至透明
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿炒至软烂，倒入剩余牛肉汤
方法: 炒,炖
工具: 炒锅,锅铲
时间: 3-5分钟

### 第11步
步骤: 步骤11
描述: 中火开锅后转小火，出锅前30-40分钟加入土豆并调味，边尝边加糖盐
方法: 炖,调味
工具: 锅,筷子
时间: 30-40分钟

### 第12步
步骤: 步骤12
描述: 筷子能轻松戳透牛肉时即可关火出锅
方法: 检查
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201002920, chunk_id=201002920_chunk_578, recipe_name=瘦肉土豆片, category=荤菜, score=0.6641399264335632, search_type=vector_enhanced

```text
## 标签
土豆片焯水不宜太久，防止变软,腌制瘦肉需搅拌均匀
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201004898, chunk_id=201004898_chunk_966, recipe_name=地三鲜, category=素菜, score=0.6529252529144287, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(150g)
2. 姜(10g)
3. 尖椒(3.5个)
4. 水(200ml)
5. 淀粉(20g)
6. 生抽(10ml)
7. 盐(8g)
8. 糖(10g)
9. 茄子(100g)
10. 葱(3g)
11. 蒜(10g)
12. 豆瓣酱(20ml)
13. 食用油(40ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6514846682548523, search_type=vector_enhanced

```text
## 所需食材
1. 洋葱(30g)
2. 火腿肠(50g)
3. 牛奶(10ml)
4. 玉米粒(30g)
5. 番茄酱(20ml)
6. 米饭(200g)
7. 胡萝卜(30g)
8. 青豆(30g)
9. 食用油(15ml)
10. 鸡胸肉(50g)
11. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=15
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6483234167098999, search_type=vector_enhanced

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
metadata_summary: node_id=201003210, recipe_name=西红柿, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西红柿
食材名称: 西红柿
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201001901, recipe_name=土豆, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 土豆
食材名称: 土豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201001631, recipe_name=牛肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 牛肉
食材名称: 牛肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_629, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.6730093955993652, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 土豆去皮、切成5cm大块，备用
方法: 切
工具: 刀,案板
时间: 3-5分钟

### 第2步
步骤: 步骤2
描述: 西红柿切十字花刀，开水烫后去皮，去芯，切3cm小块备用
方法: 切,烫
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 葱切4g葱花，其余掰成5-8cm大段；洋葱切0.5-1cm小粒
方法: 切
工具: 刀,案板
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 牛肉泡凉水半小时去血水，或凉水下锅煮至表面变白捞出，期间撇去浮沫
方法: 焯水
工具: 锅,漏勺
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 凉水没过牛肉，放入高压锅，加葱段、姜片、20g料酒，上汽压20分钟
方法: 炖
工具: 高压锅
时间: 20分钟

### 第6步
步骤: 步骤6
描述: 取出牛肉切5cm大块，挑出姜片，汤盛碗备用
方法: 切
工具: 刀,案板,碗
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 锅中倒油，油4-5成热下花椒、八角、香叶，出香味后捞出不用
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 下牛肉、葱姜炒香，必要时加少量牛肉汤防糊
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第9步
步骤: 步骤9
描述: 加生抽15ml、料酒15ml、胡椒粉、5-10g番茄酱或番茄罐头，加洋葱炒至透明
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿炒至软烂，倒入剩余牛肉汤
方法: 炒,炖
工具: 炒锅,锅铲
时间: 3-5分钟

### 第11步
步骤: 步骤11
描述: 中火开锅后转小火，出锅前30-40分钟加入土豆并调味，边尝边加糖盐
方法: 炖,调味
工具: 锅,筷子
时间: 30-40分钟

### 第12步
步骤: 步骤12
描述: 筷子能轻松戳透牛肉时即可关火出锅
方法: 检查
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=4
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
metadata_summary: node_id=201001852, chunk_id=201001852_chunk_394, recipe_name=番茄红酱, category=荤菜, score=0.7056230902671814, search_type=vector_enhanced

```text
## 标签
考虑各个品牌的番茄酱内含盐量不同，建议在炒牛肉时少放盐，煮的时候尝一下再调味,煮酱料期间请搅动，以免粘锅。如果酱料变粘稠就可以出锅啦！,可将碎牛肉替换成一半碎猪肉一半碎牛肉，牛奶替换成鸡汤或饮用水
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201003224, chunk_id=201003224_chunk_633, recipe_name=西红柿牛腩, category=荤菜, score=0.6962799429893494, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 牛腩切条、切块成长宽高均2cm，冷水下锅，开锅煮制2分钟去除血水，捞出冲洗干净
方法: 切,煮
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 另起锅2L水烧开，加入2cm两段葱段、两片姜片、八角、料酒5-10ml，放入焯好的牛肉，盖盖炖制（砂锅1小时，高压锅炖肉模式45分钟），筷子能轻松插透就证明炖好了
方法: 炖
工具: 砂锅/高压锅/铝锅,筷子
时间: 45-60分钟

### 第3步
步骤: 步骤3
描述: 西红柿去皮：西红柿头部滑十字至腰线，筷子/刀叉从果蒂捅入，煤气灶小火，一边转动一边烤，及时拿下来查看，起皮后撕下来，切块。越小越好
方法: 烤,切
工具: 刀,筷子/刀叉,煤气灶
时间: 5分钟

### 第4步
步骤: 步骤4
描述: 起锅烧油，油温7成热，葱、姜各10g，番茄下锅，炒透炒出番茄红色，加入煮好的牛腩和原汤，原汤刚刚没过牛肉即可
方法: 炒
工具: 炒锅,锅铲
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 根据个人口味放入盐、糖、生抽调味盖盖
方法: 调味
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 开锅后大火继续炒制3-5分钟
方法: 炒
工具: 锅铲
时间: 3-5分钟

### 第7步
步骤: 步骤7
描述: 待番茄汁呈中等粘稠程度后关火，散入葱花，盛盘
方法: 收汁,装盘
工具: 锅铲
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.681769609451294, search_type=vector_enhanced

```text
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=201002920, chunk_id=201002920_chunk_578, recipe_name=瘦肉土豆片, category=荤菜, score=0.6641399264335632, search_type=vector_enhanced

```text
## 标签
土豆片焯水不宜太久，防止变软,腌制瘦肉需搅拌均匀
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201004898, chunk_id=201004898_chunk_966, recipe_name=地三鲜, category=素菜, score=0.6529252529144287, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(150g)
2. 姜(10g)
3. 尖椒(3.5个)
4. 水(200ml)
5. 淀粉(20g)
6. 生抽(10ml)
7. 盐(8g)
8. 糖(10g)
9. 茄子(100g)
10. 葱(3g)
11. 蒜(10g)
12. 豆瓣酱(20ml)
13. 食用油(40ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6514846682548523, search_type=vector_enhanced

```text
## 所需食材
1. 洋葱(30g)
2. 火腿肠(50g)
3. 牛奶(10ml)
4. 玉米粒(30g)
5. 番茄酱(20ml)
6. 米饭(200g)
7. 胡萝卜(30g)
8. 青豆(30g)
9. 食用油(15ml)
10. 鸡胸肉(50g)
11. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6483234167098999, search_type=vector_enhanced

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
命中关键词: 西红柿
食材名称: 西红柿
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=1
source: rerank_input

```text
命中关键词: 土豆
食材名称: 土豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 牛肉
食材名称: 牛肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### pair_order=3
source: rerank_input

```text
菜品: 西红柿土豆炖牛肉
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 土豆去皮、切成5cm大块，备用
方法: 切
工具: 刀,案板
时间: 3-5分钟

### 第2步
步骤: 步骤2
描述: 西红柿切十字花刀，开水烫后去皮，去芯，切3cm小块备用
方法: 切,烫
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 葱切4g葱花，其余掰成5-8cm大段；洋葱切0.5-1cm小粒
方法: 切
工具: 刀,案板
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 牛肉泡凉水半小时去血水，或凉水下锅煮至表面变白捞出，期间撇去浮沫
方法: 焯水
工具: 锅,漏勺
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 凉水没过牛肉，放入高压锅，加葱段、姜片、20g料酒，上汽压20分钟
方法: 炖
工具: 高压锅
时间: 20分钟

### 第6步
步骤: 步骤6
描述: 取出牛肉切5cm大块，挑出姜片，汤盛碗备用
方法: 切
工具: 刀,案板,碗
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 锅中倒油，油4-5成热下花椒、八角、香叶，出香味后捞出不用
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 下牛肉、葱姜炒香，必要时加少量牛肉汤防糊
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第9步
步骤: 步骤9
描述: 加生抽15ml、料酒15ml、胡椒粉、5-10g番茄酱或番茄罐头，加洋葱炒至透明
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿炒至软烂，倒入剩余牛肉汤
方法: 炒,炖
工具: 炒锅,锅铲
时间: 3-5分钟

### 第11步
步骤: 步骤11
描述: 中火开锅后转小火，出锅前30-40分钟加入土豆并调味，边尝边加糖盐
方法: 炖,调味
工具: 锅,筷子
时间: 30-40分钟

### 第12步
步骤: 步骤12
描述: 筷子能轻松戳透牛肉时即可关火出锅
方法: 检查
```

### pair_order=4
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
菜品: 番茄红酱
菜系: 未知
## 标签
考虑各个品牌的番茄酱内含盐量不同，建议在炒牛肉时少放盐，煮的时候尝一下再调味,煮酱料期间请搅动，以免粘锅。如果酱料变粘稠就可以出锅啦！,可将碎牛肉替换成一半碎猪肉一半碎牛肉，牛奶替换成鸡汤或饮用水
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=7
source: rerank_input

```text
菜品: 西红柿牛腩
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 牛腩切条、切块成长宽高均2cm，冷水下锅，开锅煮制2分钟去除血水，捞出冲洗干净
方法: 切,煮
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 另起锅2L水烧开，加入2cm两段葱段、两片姜片、八角、料酒5-10ml，放入焯好的牛肉，盖盖炖制（砂锅1小时，高压锅炖肉模式45分钟），筷子能轻松插透就证明炖好了
方法: 炖
工具: 砂锅/高压锅/铝锅,筷子
时间: 45-60分钟

### 第3步
步骤: 步骤3
描述: 西红柿去皮：西红柿头部滑十字至腰线，筷子/刀叉从果蒂捅入，煤气灶小火，一边转动一边烤，及时拿下来查看，起皮后撕下来，切块。越小越好
方法: 烤,切
工具: 刀,筷子/刀叉,煤气灶
时间: 5分钟

### 第4步
步骤: 步骤4
描述: 起锅烧油，油温7成热，葱、姜各10g，番茄下锅，炒透炒出番茄红色，加入煮好的牛腩和原汤，原汤刚刚没过牛肉即可
方法: 炒
工具: 炒锅,锅铲
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 根据个人口味放入盐、糖、生抽调味盖盖
方法: 调味
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 开锅后大火继续炒制3-5分钟
方法: 炒
工具: 锅铲
时间: 3-5分钟

### 第7步
步骤: 步骤7
描述: 待番茄汁呈中等粘稠程度后关火，散入葱花，盛盘
方法: 收汁,装盘
工具: 锅铲
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=8
source: rerank_input

```text
菜品: 番茄牛肉蛋花汤
菜系: 未知
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### pair_order=9
source: rerank_input

```text
菜品: 瘦肉土豆片
菜系: 未知
## 标签
土豆片焯水不宜太久，防止变软,腌制瘦肉需搅拌均匀
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=10
source: rerank_input

```text
菜品: 地三鲜
菜系: 东北菜
## 所需食材
1. 土豆(150g)
2. 姜(10g)
3. 尖椒(3.5个)
4. 水(200ml)
5. 淀粉(20g)
6. 生抽(10ml)
7. 盐(8g)
8. 糖(10g)
9. 茄子(100g)
10. 葱(3g)
11. 蒜(10g)
12. 豆瓣酱(20ml)
13. 食用油(40ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=11
source: rerank_input

```text
菜品: 蛋包饭
菜系: 日式
## 所需食材
1. 洋葱(30g)
2. 火腿肠(50g)
3. 牛奶(10ml)
4. 玉米粒(30g)
5. 番茄酱(20ml)
6. 米饭(200g)
7. 胡萝卜(30g)
8. 青豆(30g)
9. 食用油(15ml)
10. 鸡胸肉(50g)
11. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=12
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
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_629, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.6730093955993652, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 土豆去皮、切成5cm大块，备用
方法: 切
工具: 刀,案板
时间: 3-5分钟

### 第2步
步骤: 步骤2
描述: 西红柿切十字花刀，开水烫后去皮，去芯，切3cm小块备用
方法: 切,烫
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 葱切4g葱花，其余掰成5-8cm大段；洋葱切0.5-1cm小粒
方法: 切
工具: 刀,案板
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 牛肉泡凉水半小时去血水，或凉水下锅煮至表面变白捞出，期间撇去浮沫
方法: 焯水
工具: 锅,漏勺
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 凉水没过牛肉，放入高压锅，加葱段、姜片、20g料酒，上汽压20分钟
方法: 炖
工具: 高压锅
时间: 20分钟

### 第6步
步骤: 步骤6
描述: 取出牛肉切5cm大块，挑出姜片，汤盛碗备用
方法: 切
工具: 刀,案板,碗
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 锅中倒油，油4-5成热下花椒、八角、香叶，出香味后捞出不用
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 下牛肉、葱姜炒香，必要时加少量牛肉汤防糊
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第9步
步骤: 步骤9
描述: 加生抽15ml、料酒15ml、胡椒粉、5-10g番茄酱或番茄罐头，加洋葱炒至透明
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿炒至软烂，倒入剩余牛肉汤
方法: 炒,炖
工具: 炒锅,锅铲
时间: 3-5分钟

### 第11步
步骤: 步骤11
描述: 中火开锅后转小火，出锅前30-40分钟加入土豆并调味，边尝边加糖盐
方法: 炖,调味
工具: 锅,筷子
时间: 30-40分钟

### 第12步
步骤: 步骤12
描述: 筷子能轻松戳透牛肉时即可关火出锅
方法: 检查
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201003224, chunk_id=201003224_chunk_633, recipe_name=西红柿牛腩, category=荤菜, score=0.6962799429893494, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 牛腩切条、切块成长宽高均2cm，冷水下锅，开锅煮制2分钟去除血水，捞出冲洗干净
方法: 切,煮
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 另起锅2L水烧开，加入2cm两段葱段、两片姜片、八角、料酒5-10ml，放入焯好的牛肉，盖盖炖制（砂锅1小时，高压锅炖肉模式45分钟），筷子能轻松插透就证明炖好了
方法: 炖
工具: 砂锅/高压锅/铝锅,筷子
时间: 45-60分钟

### 第3步
步骤: 步骤3
描述: 西红柿去皮：西红柿头部滑十字至腰线，筷子/刀叉从果蒂捅入，煤气灶小火，一边转动一边烤，及时拿下来查看，起皮后撕下来，切块。越小越好
方法: 烤,切
工具: 刀,筷子/刀叉,煤气灶
时间: 5分钟

### 第4步
步骤: 步骤4
描述: 起锅烧油，油温7成热，葱、姜各10g，番茄下锅，炒透炒出番茄红色，加入煮好的牛腩和原汤，原汤刚刚没过牛肉即可
方法: 炒
工具: 炒锅,锅铲
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 根据个人口味放入盐、糖、生抽调味盖盖
方法: 调味
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 开锅后大火继续炒制3-5分钟
方法: 炒
工具: 锅铲
时间: 3-5分钟

### 第7步
步骤: 步骤7
描述: 待番茄汁呈中等粘稠程度后关火，散入葱花，盛盘
方法: 收汁,装盘
工具: 锅铲
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.681769609451294, search_type=vector_enhanced

```text
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201004898, chunk_id=201004898_chunk_966, recipe_name=地三鲜, category=素菜, score=0.6529252529144287, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(150g)
2. 姜(10g)
3. 尖椒(3.5个)
4. 水(200ml)
5. 淀粉(20g)
6. 生抽(10ml)
7. 盐(8g)
8. 糖(10g)
9. 茄子(100g)
10. 葱(3g)
11. 蒜(10g)
12. 豆瓣酱(20ml)
13. 食用油(40ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201001852, chunk_id=201001852_chunk_394, recipe_name=番茄红酱, category=荤菜, score=0.7056230902671814, search_type=vector_enhanced

```text
## 标签
考虑各个品牌的番茄酱内含盐量不同，建议在炒牛肉时少放盐，煮的时候尝一下再调味,煮酱料期间请搅动，以免粘锅。如果酱料变粘稠就可以出锅啦！,可将碎牛肉替换成一半碎猪肉一半碎牛肉，牛奶替换成鸡汤或饮用水
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6483234167098999, search_type=vector_enhanced

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

### result_order=6
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

### result_order=7
source: reranked_results
metadata_summary: node_id=201002920, chunk_id=201002920_chunk_578, recipe_name=瘦肉土豆片, category=荤菜, score=0.6641399264335632, search_type=vector_enhanced

```text
## 标签
土豆片焯水不宜太久，防止变软,腌制瘦肉需搅拌均匀
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6514846682548523, search_type=vector_enhanced

```text
## 所需食材
1. 洋葱(30g)
2. 火腿肠(50g)
3. 牛奶(10ml)
4. 玉米粒(30g)
5. 番茄酱(20ml)
6. 米饭(200g)
7. 胡萝卜(30g)
8. 青豆(30g)
9. 食用油(15ml)
10. 鸡胸肉(50g)
11. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=9
source: reranked_results
metadata_summary: node_id=201003210, recipe_name=西红柿, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西红柿
食材名称: 西红柿
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=10
source: reranked_results
metadata_summary: node_id=201001901, recipe_name=土豆, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 土豆
食材名称: 土豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=11
source: reranked_results
metadata_summary: node_id=201001631, recipe_name=牛肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 牛肉
食材名称: 牛肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=12
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
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_629, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.6730093955993652, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 土豆去皮、切成5cm大块，备用
方法: 切
工具: 刀,案板
时间: 3-5分钟

### 第2步
步骤: 步骤2
描述: 西红柿切十字花刀，开水烫后去皮，去芯，切3cm小块备用
方法: 切,烫
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 葱切4g葱花，其余掰成5-8cm大段；洋葱切0.5-1cm小粒
方法: 切
工具: 刀,案板
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 牛肉泡凉水半小时去血水，或凉水下锅煮至表面变白捞出，期间撇去浮沫
方法: 焯水
工具: 锅,漏勺
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 凉水没过牛肉，放入高压锅，加葱段、姜片、20g料酒，上汽压20分钟
方法: 炖
工具: 高压锅
时间: 20分钟

### 第6步
步骤: 步骤6
描述: 取出牛肉切5cm大块，挑出姜片，汤盛碗备用
方法: 切
工具: 刀,案板,碗
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 锅中倒油，油4-5成热下花椒、八角、香叶，出香味后捞出不用
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 下牛肉、葱姜炒香，必要时加少量牛肉汤防糊
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第9步
步骤: 步骤9
描述: 加生抽15ml、料酒15ml、胡椒粉、5-10g番茄酱或番茄罐头，加洋葱炒至透明
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿炒至软烂，倒入剩余牛肉汤
方法: 炒,炖
工具: 炒锅,锅铲
时间: 3-5分钟

### 第11步
步骤: 步骤11
描述: 中火开锅后转小火，出锅前30-40分钟加入土豆并调味，边尝边加糖盐
方法: 炖,调味
工具: 锅,筷子
时间: 30-40分钟

### 第12步
步骤: 步骤12
描述: 筷子能轻松戳透牛肉时即可关火出锅
方法: 检查
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201003224, chunk_id=201003224_chunk_633, recipe_name=西红柿牛腩, category=荤菜, score=0.6962799429893494, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 牛腩切条、切块成长宽高均2cm，冷水下锅，开锅煮制2分钟去除血水，捞出冲洗干净
方法: 切,煮
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 另起锅2L水烧开，加入2cm两段葱段、两片姜片、八角、料酒5-10ml，放入焯好的牛肉，盖盖炖制（砂锅1小时，高压锅炖肉模式45分钟），筷子能轻松插透就证明炖好了
方法: 炖
工具: 砂锅/高压锅/铝锅,筷子
时间: 45-60分钟

### 第3步
步骤: 步骤3
描述: 西红柿去皮：西红柿头部滑十字至腰线，筷子/刀叉从果蒂捅入，煤气灶小火，一边转动一边烤，及时拿下来查看，起皮后撕下来，切块。越小越好
方法: 烤,切
工具: 刀,筷子/刀叉,煤气灶
时间: 5分钟

### 第4步
步骤: 步骤4
描述: 起锅烧油，油温7成热，葱、姜各10g，番茄下锅，炒透炒出番茄红色，加入煮好的牛腩和原汤，原汤刚刚没过牛肉即可
方法: 炒
工具: 炒锅,锅铲
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 根据个人口味放入盐、糖、生抽调味盖盖
方法: 调味
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 开锅后大火继续炒制3-5分钟
方法: 炒
工具: 锅铲
时间: 3-5分钟

### 第7步
步骤: 步骤7
描述: 待番茄汁呈中等粘稠程度后关火，散入葱花，盛盘
方法: 收汁,装盘
工具: 锅铲
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.681769609451294, search_type=vector_enhanced

```text
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201004898, chunk_id=201004898_chunk_966, recipe_name=地三鲜, category=素菜, score=0.6529252529144287, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(150g)
2. 姜(10g)
3. 尖椒(3.5个)
4. 水(200ml)
5. 淀粉(20g)
6. 生抽(10ml)
7. 盐(8g)
8. 糖(10g)
9. 茄子(100g)
10. 葱(3g)
11. 蒜(10g)
12. 豆瓣酱(20ml)
13. 食用油(40ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6483234167098999, search_type=vector_enhanced

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

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_629, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.6730093955993652, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 土豆去皮、切成5cm大块，备用
方法: 切
工具: 刀,案板
时间: 3-5分钟

### 第2步
步骤: 步骤2
描述: 西红柿切十字花刀，开水烫后去皮，去芯，切3cm小块备用
方法: 切,烫
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 葱切4g葱花，其余掰成5-8cm大段；洋葱切0.5-1cm小粒
方法: 切
工具: 刀,案板
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 牛肉泡凉水半小时去血水，或凉水下锅煮至表面变白捞出，期间撇去浮沫
方法: 焯水
工具: 锅,漏勺
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 凉水没过牛肉，放入高压锅，加葱段、姜片、20g料酒，上汽压20分钟
方法: 炖
工具: 高压锅
时间: 20分钟

### 第6步
步骤: 步骤6
描述: 取出牛肉切5cm大块，挑出姜片，汤盛碗备用
方法: 切
工具: 刀,案板,碗
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 锅中倒油，油4-5成热下花椒、八角、香叶，出香味后捞出不用
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 下牛肉、葱姜炒香，必要时加少量牛肉汤防糊
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第9步
步骤: 步骤9
描述: 加生抽15ml、料酒15ml、胡椒粉、5-10g番茄酱或番茄罐头，加洋葱炒至透明
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第10步
步骤: 步骤10
描述: 加入西红柿炒至软烂，倒入剩余牛肉汤
方法: 炒,炖
工具: 炒锅,锅铲
时间: 3-5分钟

### 第11步
步骤: 步骤11
描述: 中火开锅后转小火，出锅前30-40分钟加入土豆并调味，边尝边加糖盐
方法: 炖,调味
工具: 锅,筷子
时间: 30-40分钟

### 第12步
步骤: 步骤12
描述: 筷子能轻松戳透牛肉时即可关火出锅
方法: 检查
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=1
source: generation_context
metadata_summary: node_id=201003224, chunk_id=201003224_chunk_633, recipe_name=西红柿牛腩, category=荤菜, score=0.6962799429893494, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 牛腩切条、切块成长宽高均2cm，冷水下锅，开锅煮制2分钟去除血水，捞出冲洗干净
方法: 切,煮
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 另起锅2L水烧开，加入2cm两段葱段、两片姜片、八角、料酒5-10ml，放入焯好的牛肉，盖盖炖制（砂锅1小时，高压锅炖肉模式45分钟），筷子能轻松插透就证明炖好了
方法: 炖
工具: 砂锅/高压锅/铝锅,筷子
时间: 45-60分钟

### 第3步
步骤: 步骤3
描述: 西红柿去皮：西红柿头部滑十字至腰线，筷子/刀叉从果蒂捅入，煤气灶小火，一边转动一边烤，及时拿下来查看，起皮后撕下来，切块。越小越好
方法: 烤,切
工具: 刀,筷子/刀叉,煤气灶
时间: 5分钟

### 第4步
步骤: 步骤4
描述: 起锅烧油，油温7成热，葱、姜各10g，番茄下锅，炒透炒出番茄红色，加入煮好的牛腩和原汤，原汤刚刚没过牛肉即可
方法: 炒
工具: 炒锅,锅铲
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 根据个人口味放入盐、糖、生抽调味盖盖
方法: 调味
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 开锅后大火继续炒制3-5分钟
方法: 炒
工具: 锅铲
时间: 3-5分钟

### 第7步
步骤: 步骤7
描述: 待番茄汁呈中等粘稠程度后关火，散入葱花，盛盘
方法: 收汁,装盘
工具: 锅铲
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: generation_context
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.681769609451294, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=3
source: generation_context
metadata_summary: node_id=201004898, chunk_id=201004898_chunk_966, recipe_name=地三鲜, category=素菜, score=0.6529252529144287, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 土豆(150g)
2. 姜(10g)
3. 尖椒(3.5个)
4. 水(200ml)
5. 淀粉(20g)
6. 生抽(10ml)
7. 盐(8g)
8. 糖(10g)
9. 茄子(100g)
10. 葱(3g)
11. 蒜(10g)
12. 豆瓣酱(20ml)
13. 食用油(40ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=4
source: generation_context
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6483234167098999, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

