# Recall Content

audit_id: 20260811_180123_311_250c21bc
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201000006, recipe_name=鸡蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

### result_order=1
source: entity_level
metadata_summary: node_id=201005725, recipe_name=鸡蛋羹, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋羹
菜品名称: 鸡蛋羹
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### result_order=2
source: entity_level
metadata_summary: node_id=201004534, recipe_name=煎蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 煎蛋
食材名称: 煎蛋
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=3
source: entity_level
metadata_summary: node_id=201004118, recipe_name=馒头, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 馒头
食材名称: 馒头
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=201000511, recipe_name=吐司果酱, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 吐司果酱
分类: 早餐
难度: 1.0
主要食材: 吐司, 果酱
关联图谱:
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
- OUT REQUIRES 果酱 (Ingredient): category: 调料
- OUT CONTAINS_STEP 步骤5 (CookingStep): description: 用餐巾纸包一下可以边走边吃也可以吃完再出门
```

### result_order=1
source: topic_level
metadata_summary: node_id=201000539, recipe_name=微波炉荷包蛋, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 微波炉荷包蛋
分类: 早餐
难度: 1.0
主要食材: 芝麻油, 饮用水, 鸡蛋
关联图谱:
- OUT REQUIRES 芝麻油 (Ingredient): category: 调料
- OUT REQUIRES 饮用水 (Ingredient): category: 其他
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
```

### result_order=2
source: topic_level
metadata_summary: node_id=201000550, recipe_name=微波炉蛋糕, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 微波炉蛋糕
分类: 早餐
难度: 1.0
主要食材: 麦片, 香蕉, 牛奶
关联图谱:
- OUT REQUIRES 麦片 (Ingredient): category: 淀粉类
- OUT REQUIRES 香蕉 (Ingredient): category: 其他
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=3
source: topic_level
metadata_summary: node_id=201000644, recipe_name=牛奶燕麦, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 牛奶燕麦
分类: 早餐
难度: 1.0
主要食材: 鸡蛋, 燕麦, 牛奶
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=4
source: topic_level
metadata_summary: node_id=201000655, recipe_name=空气炸锅面包片, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 空气炸锅面包片
分类: 早餐
难度: 1.0
主要食材: 面包片
关联图谱:
- OUT SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
- IN SIMILAR 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
- IN SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
```

### result_order=5
source: topic_level
metadata_summary: node_id=201000718, recipe_name=金枪鱼酱三明治, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 金枪鱼酱三明治
分类: 早餐
难度: 1.0
主要食材: 俄式酸黄瓜汁, 芝士片, 火腿片
关联图谱:
- OUT REQUIRES 俄式酸黄瓜汁 (Ingredient): category: 调料
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 火腿片 (Ingredient): category: 蛋白质
```

### result_order=6
source: topic_level
metadata_summary: node_id=201000519, recipe_name=太阳蛋, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 太阳蛋
分类: 早餐
难度: 2.0
主要食材: 盐, 鸡蛋, 油
关联图谱:
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=7
source: topic_level
metadata_summary: node_id=201000571, recipe_name=手抓饼, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 手抓饼
分类: 早餐
难度: 2.0
主要食材: 芝士片, 鸡蛋, 食用油
关联图谱:
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=8
source: topic_level
metadata_summary: node_id=201001206, recipe_name=杨枝甘露, category=饮料, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 省时
菜品: 杨枝甘露
分类: 饮料
难度: 2.0
主要食材: 奇亚籽, 切丝芒果干, 切丝柳橙干
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 饮料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=9
source: topic_level
metadata_summary: node_id=201000587, recipe_name=桂圆红枣粥, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 桂圆红枣粥
分类: 早餐
难度: 2.0
主要食材: 糯米, 红枣, 桂圆
关联图谱:
- OUT REQUIRES 糯米 (Ingredient): category: 淀粉类
- OUT REQUIRES 红枣 (Ingredient): category: 蔬菜
- OUT REQUIRES 桂圆 (Ingredient): category: 其他
```

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.7216987013816833, search_type=vector_enhanced

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

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6705695986747742, search_type=vector_enhanced

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

### result_order=2
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.6632564067840576, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6552770137786865, search_type=vector_enhanced

```text
## 所需食材
1. 冷饭(500ml)
2. 油(12ml)
3. 火腿(2个)
4. 灯影牛肉丝/午餐肉/腊肠/卤肉
5. 生抽(10ml)
6. 盐(4g)
7. 胡椒粉(8g)
8. 胡萝卜(30g)
9. 香葱(1颗)
10. 鸡蛋(1.5个)
11. 黄瓜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201002309, chunk_id=201002309_chunk_472, recipe_name=咖喱肥牛, category=荤菜, score=0.6480962038040161, search_type=vector_enhanced

```text
## 所需食材
1. 冷水(适量ml)
2. 咖喱块(100g)
3. 土豆(200g)
4. 洋葱(100g)
5. 纯牛奶(50ml)
6. 肥牛卷(300g)
7. 胡萝卜(150g)
8. 食用油(10-15ml)
9. 香叶(1片)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201003793, chunk_id=201003793_chunk_745, recipe_name=罗宋汤, category=汤类, score=0.6480680108070374, search_type=vector_enhanced

```text
## 所需食材
1. 包菜(200g)
2. 植物油(5mL)
3. 橄榄油(5mL)
4. 欧芹(100g)
5. 洋葱(100g)
6. 牛肉(250g)
7. 牛肉高汤(500mL)
8. 番茄罐头(2罐)
9. 番茄膏(5g)
10. 盐(18g)
11. 红肠(150g)
12. 胡萝卜(100g)
13. 马铃薯(400g)
14. 黑胡椒(3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.6423543691635132, search_type=vector_enhanced

```text
## 所需食材
1. 牛奶(50毫升)
2. 盐(适量克)
3. 纯干燕麦片(50克)
4. 胡椒(适量克)
5. 蔬菜（菠菜等）(50克)
6. 鸡蛋(2个)
7. 黄油(适量克)

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6380630731582642, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.6363043785095215, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.6345013380050659, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(750g)
2. 大葱(100g)
3. 大蒜(4瓣)
4. 干线椒(5个)
5. 料酒(100g)
6. 油(50g)
7. 清水(1000ml)
8. 甜椒(50g)
9. 生抽(7ml)
10. 白砂糖(20g)
11. 盐(5g)
12. 花椒
13. 菜椒(50g)
14. 蚝油(10g)
15. 香叶(适量片)
16. 香果
17. 鸡腿肉(1000g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201000006, recipe_name=鸡蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201005725, recipe_name=鸡蛋羹, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋羹
菜品名称: 鸡蛋羹
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201004534, recipe_name=煎蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 煎蛋
食材名称: 煎蛋
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201004118, recipe_name=馒头, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 馒头
食材名称: 馒头
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201000511, recipe_name=吐司果酱, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 吐司果酱
分类: 早餐
难度: 1.0
主要食材: 吐司, 果酱
关联图谱:
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
- OUT REQUIRES 果酱 (Ingredient): category: 调料
- OUT CONTAINS_STEP 步骤5 (CookingStep): description: 用餐巾纸包一下可以边走边吃也可以吃完再出门
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201000539, recipe_name=微波炉荷包蛋, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 微波炉荷包蛋
分类: 早餐
难度: 1.0
主要食材: 芝麻油, 饮用水, 鸡蛋
关联图谱:
- OUT REQUIRES 芝麻油 (Ingredient): category: 调料
- OUT REQUIRES 饮用水 (Ingredient): category: 其他
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201000550, recipe_name=微波炉蛋糕, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 微波炉蛋糕
分类: 早餐
难度: 1.0
主要食材: 麦片, 香蕉, 牛奶
关联图谱:
- OUT REQUIRES 麦片 (Ingredient): category: 淀粉类
- OUT REQUIRES 香蕉 (Ingredient): category: 其他
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201000644, recipe_name=牛奶燕麦, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 牛奶燕麦
分类: 早餐
难度: 1.0
主要食材: 鸡蛋, 燕麦, 牛奶
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201000655, recipe_name=空气炸锅面包片, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 空气炸锅面包片
分类: 早餐
难度: 1.0
主要食材: 面包片
关联图谱:
- OUT SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
- IN SIMILAR 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
- IN SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201000718, recipe_name=金枪鱼酱三明治, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 金枪鱼酱三明治
分类: 早餐
难度: 1.0
主要食材: 俄式酸黄瓜汁, 芝士片, 火腿片
关联图谱:
- OUT REQUIRES 俄式酸黄瓜汁 (Ingredient): category: 调料
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 火腿片 (Ingredient): category: 蛋白质
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201000519, recipe_name=太阳蛋, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 太阳蛋
分类: 早餐
难度: 2.0
主要食材: 盐, 鸡蛋, 油
关联图谱:
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201000571, recipe_name=手抓饼, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 手抓饼
分类: 早餐
难度: 2.0
主要食材: 芝士片, 鸡蛋, 食用油
关联图谱:
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201001206, recipe_name=杨枝甘露, category=饮料, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 省时
菜品: 杨枝甘露
分类: 饮料
难度: 2.0
主要食材: 奇亚籽, 切丝芒果干, 切丝柳橙干
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 饮料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201000587, recipe_name=桂圆红枣粥, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 桂圆红枣粥
分类: 早餐
难度: 2.0
主要食材: 糯米, 红枣, 桂圆
关联图谱:
- OUT REQUIRES 糯米 (Ingredient): category: 淀粉类
- OUT REQUIRES 红枣 (Ingredient): category: 蔬菜
- OUT REQUIRES 桂圆 (Ingredient): category: 其他
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.7216987013816833, search_type=vector_enhanced

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

### result_order=15
source: branch_grouped
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6705695986747742, search_type=vector_enhanced

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

### result_order=16
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.6632564067840576, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=17
source: branch_grouped
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6552770137786865, search_type=vector_enhanced

```text
## 所需食材
1. 冷饭(500ml)
2. 油(12ml)
3. 火腿(2个)
4. 灯影牛肉丝/午餐肉/腊肠/卤肉
5. 生抽(10ml)
6. 盐(4g)
7. 胡椒粉(8g)
8. 胡萝卜(30g)
9. 香葱(1颗)
10. 鸡蛋(1.5个)
11. 黄瓜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=18
source: branch_grouped
metadata_summary: node_id=201002309, chunk_id=201002309_chunk_472, recipe_name=咖喱肥牛, category=荤菜, score=0.6480962038040161, search_type=vector_enhanced

```text
## 所需食材
1. 冷水(适量ml)
2. 咖喱块(100g)
3. 土豆(200g)
4. 洋葱(100g)
5. 纯牛奶(50ml)
6. 肥牛卷(300g)
7. 胡萝卜(150g)
8. 食用油(10-15ml)
9. 香叶(1片)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=19
source: branch_grouped
metadata_summary: node_id=201003793, chunk_id=201003793_chunk_745, recipe_name=罗宋汤, category=汤类, score=0.6480680108070374, search_type=vector_enhanced

```text
## 所需食材
1. 包菜(200g)
2. 植物油(5mL)
3. 橄榄油(5mL)
4. 欧芹(100g)
5. 洋葱(100g)
6. 牛肉(250g)
7. 牛肉高汤(500mL)
8. 番茄罐头(2罐)
9. 番茄膏(5g)
10. 盐(18g)
11. 红肠(150g)
12. 胡萝卜(100g)
13. 马铃薯(400g)
14. 黑胡椒(3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=20
source: branch_grouped
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.6423543691635132, search_type=vector_enhanced

```text
## 所需食材
1. 牛奶(50毫升)
2. 盐(适量克)
3. 纯干燕麦片(50克)
4. 胡椒(适量克)
5. 蔬菜（菠菜等）(50克)
6. 鸡蛋(2个)
7. 黄油(适量克)

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=21
source: branch_grouped
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6380630731582642, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=22
source: branch_grouped
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.6363043785095215, search_type=vector_enhanced

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

### result_order=23
source: branch_grouped
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.6345013380050659, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(750g)
2. 大葱(100g)
3. 大蒜(4瓣)
4. 干线椒(5个)
5. 料酒(100g)
6. 油(50g)
7. 清水(1000ml)
8. 甜椒(50g)
9. 生抽(7ml)
10. 白砂糖(20g)
11. 盐(5g)
12. 花椒
13. 菜椒(50g)
14. 蚝油(10g)
15. 香叶(适量片)
16. 香果
17. 鸡腿肉(1000g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201000006, recipe_name=鸡蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201005725, recipe_name=鸡蛋羹, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋羹
菜品名称: 鸡蛋羹
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201004534, recipe_name=煎蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 煎蛋
食材名称: 煎蛋
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201004118, recipe_name=馒头, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 馒头
食材名称: 馒头
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201000511, recipe_name=吐司果酱, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 吐司果酱
分类: 早餐
难度: 1.0
主要食材: 吐司, 果酱
关联图谱:
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
- OUT REQUIRES 果酱 (Ingredient): category: 调料
- OUT CONTAINS_STEP 步骤5 (CookingStep): description: 用餐巾纸包一下可以边走边吃也可以吃完再出门
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201000539, recipe_name=微波炉荷包蛋, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 微波炉荷包蛋
分类: 早餐
难度: 1.0
主要食材: 芝麻油, 饮用水, 鸡蛋
关联图谱:
- OUT REQUIRES 芝麻油 (Ingredient): category: 调料
- OUT REQUIRES 饮用水 (Ingredient): category: 其他
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=201000550, recipe_name=微波炉蛋糕, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 微波炉蛋糕
分类: 早餐
难度: 1.0
主要食材: 麦片, 香蕉, 牛奶
关联图谱:
- OUT REQUIRES 麦片 (Ingredient): category: 淀粉类
- OUT REQUIRES 香蕉 (Ingredient): category: 其他
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201000644, recipe_name=牛奶燕麦, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 牛奶燕麦
分类: 早餐
难度: 1.0
主要食材: 鸡蛋, 燕麦, 牛奶
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201000655, recipe_name=空气炸锅面包片, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 空气炸锅面包片
分类: 早餐
难度: 1.0
主要食材: 面包片
关联图谱:
- OUT SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
- IN SIMILAR 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
- IN SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=201000718, recipe_name=金枪鱼酱三明治, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 金枪鱼酱三明治
分类: 早餐
难度: 1.0
主要食材: 俄式酸黄瓜汁, 芝士片, 火腿片
关联图谱:
- OUT REQUIRES 俄式酸黄瓜汁 (Ingredient): category: 调料
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 火腿片 (Ingredient): category: 蛋白质
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201000519, recipe_name=太阳蛋, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 太阳蛋
分类: 早餐
难度: 2.0
主要食材: 盐, 鸡蛋, 油
关联图谱:
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=201000571, recipe_name=手抓饼, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 手抓饼
分类: 早餐
难度: 2.0
主要食材: 芝士片, 鸡蛋, 食用油
关联图谱:
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=201001206, recipe_name=杨枝甘露, category=饮料, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 省时
菜品: 杨枝甘露
分类: 饮料
难度: 2.0
主要食材: 奇亚籽, 切丝芒果干, 切丝柳橙干
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 饮料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=13
source: merged_candidates
metadata_summary: node_id=201000587, recipe_name=桂圆红枣粥, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 桂圆红枣粥
分类: 早餐
难度: 2.0
主要食材: 糯米, 红枣, 桂圆
关联图谱:
- OUT REQUIRES 糯米 (Ingredient): category: 淀粉类
- OUT REQUIRES 红枣 (Ingredient): category: 蔬菜
- OUT REQUIRES 桂圆 (Ingredient): category: 其他
```

### result_order=14
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.7216987013816833, search_type=vector_enhanced

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

### result_order=15
source: merged_candidates
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6705695986747742, search_type=vector_enhanced

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

### result_order=16
source: merged_candidates
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.6632564067840576, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=17
source: merged_candidates
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6552770137786865, search_type=vector_enhanced

```text
## 所需食材
1. 冷饭(500ml)
2. 油(12ml)
3. 火腿(2个)
4. 灯影牛肉丝/午餐肉/腊肠/卤肉
5. 生抽(10ml)
6. 盐(4g)
7. 胡椒粉(8g)
8. 胡萝卜(30g)
9. 香葱(1颗)
10. 鸡蛋(1.5个)
11. 黄瓜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=18
source: merged_candidates
metadata_summary: node_id=201002309, chunk_id=201002309_chunk_472, recipe_name=咖喱肥牛, category=荤菜, score=0.6480962038040161, search_type=vector_enhanced

```text
## 所需食材
1. 冷水(适量ml)
2. 咖喱块(100g)
3. 土豆(200g)
4. 洋葱(100g)
5. 纯牛奶(50ml)
6. 肥牛卷(300g)
7. 胡萝卜(150g)
8. 食用油(10-15ml)
9. 香叶(1片)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=19
source: merged_candidates
metadata_summary: node_id=201003793, chunk_id=201003793_chunk_745, recipe_name=罗宋汤, category=汤类, score=0.6480680108070374, search_type=vector_enhanced

```text
## 所需食材
1. 包菜(200g)
2. 植物油(5mL)
3. 橄榄油(5mL)
4. 欧芹(100g)
5. 洋葱(100g)
6. 牛肉(250g)
7. 牛肉高汤(500mL)
8. 番茄罐头(2罐)
9. 番茄膏(5g)
10. 盐(18g)
11. 红肠(150g)
12. 胡萝卜(100g)
13. 马铃薯(400g)
14. 黑胡椒(3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=20
source: merged_candidates
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.6423543691635132, search_type=vector_enhanced

```text
## 所需食材
1. 牛奶(50毫升)
2. 盐(适量克)
3. 纯干燕麦片(50克)
4. 胡椒(适量克)
5. 蔬菜（菠菜等）(50克)
6. 鸡蛋(2个)
7. 黄油(适量克)

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=21
source: merged_candidates
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6380630731582642, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=22
source: merged_candidates
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.6363043785095215, search_type=vector_enhanced

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

### result_order=23
source: merged_candidates
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.6345013380050659, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(750g)
2. 大葱(100g)
3. 大蒜(4瓣)
4. 干线椒(5个)
5. 料酒(100g)
6. 油(50g)
7. 清水(1000ml)
8. 甜椒(50g)
9. 生抽(7ml)
10. 白砂糖(20g)
11. 盐(5g)
12. 花椒
13. 菜椒(50g)
14. 蚝油(10g)
15. 香叶(适量片)
16. 香果
17. 鸡腿肉(1000g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e, recipe_name=如何决策吃什么, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 如何决策吃什么
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
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

### pair_order=1
source: rerank_input

```text
命中关键词: 鸡蛋羹
菜品名称: 鸡蛋羹
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 煎蛋
食材名称: 煎蛋
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### pair_order=3
source: rerank_input

```text
命中关键词: 馒头
食材名称: 馒头
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### pair_order=4
source: rerank_input

```text
命中关键词: 早餐
菜品: 吐司果酱
分类: 早餐
难度: 1.0
主要食材: 吐司, 果酱
关联图谱:
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
- OUT REQUIRES 果酱 (Ingredient): category: 调料
- OUT CONTAINS_STEP 步骤5 (CookingStep): description: 用餐巾纸包一下可以边走边吃也可以吃完再出门
```

### pair_order=5
source: rerank_input

```text
命中关键词: 早餐
菜品: 微波炉荷包蛋
分类: 早餐
难度: 1.0
主要食材: 芝麻油, 饮用水, 鸡蛋
关联图谱:
- OUT REQUIRES 芝麻油 (Ingredient): category: 调料
- OUT REQUIRES 饮用水 (Ingredient): category: 其他
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
```

### pair_order=6
source: rerank_input

```text
命中关键词: 早餐
菜品: 微波炉蛋糕
分类: 早餐
难度: 1.0
主要食材: 麦片, 香蕉, 牛奶
关联图谱:
- OUT REQUIRES 麦片 (Ingredient): category: 淀粉类
- OUT REQUIRES 香蕉 (Ingredient): category: 其他
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### pair_order=7
source: rerank_input

```text
命中关键词: 早餐
菜品: 牛奶燕麦
分类: 早餐
难度: 1.0
主要食材: 鸡蛋, 燕麦, 牛奶
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### pair_order=8
source: rerank_input

```text
命中关键词: 早餐
菜品: 空气炸锅面包片
分类: 早餐
难度: 1.0
主要食材: 面包片
关联图谱:
- OUT SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
- IN SIMILAR 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
- IN SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
```

### pair_order=9
source: rerank_input

```text
命中关键词: 早餐
菜品: 金枪鱼酱三明治
分类: 早餐
难度: 1.0
主要食材: 俄式酸黄瓜汁, 芝士片, 火腿片
关联图谱:
- OUT REQUIRES 俄式酸黄瓜汁 (Ingredient): category: 调料
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 火腿片 (Ingredient): category: 蛋白质
```

### pair_order=10
source: rerank_input

```text
命中关键词: 早餐
菜品: 太阳蛋
分类: 早餐
难度: 2.0
主要食材: 盐, 鸡蛋, 油
关联图谱:
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### pair_order=11
source: rerank_input

```text
命中关键词: 早餐
菜品: 手抓饼
分类: 早餐
难度: 2.0
主要食材: 芝士片, 鸡蛋, 食用油
关联图谱:
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### pair_order=12
source: rerank_input

```text
命中关键词: 省时
菜品: 杨枝甘露
分类: 饮料
难度: 2.0
主要食材: 奇亚籽, 切丝芒果干, 切丝柳橙干
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 饮料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=13
source: rerank_input

```text
命中关键词: 早餐
菜品: 桂圆红枣粥
分类: 早餐
难度: 2.0
主要食材: 糯米, 红枣, 桂圆
关联图谱:
- OUT REQUIRES 糯米 (Ingredient): category: 淀粉类
- OUT REQUIRES 红枣 (Ingredient): category: 蔬菜
- OUT REQUIRES 桂圆 (Ingredient): category: 其他
```

### pair_order=14
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

### pair_order=15
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

### pair_order=16
source: rerank_input

```text
菜系: 技巧知识
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### pair_order=17
source: rerank_input

```text
菜品: 蛋炒饭
菜系: 未知
## 所需食材
1. 冷饭(500ml)
2. 油(12ml)
3. 火腿(2个)
4. 灯影牛肉丝/午餐肉/腊肠/卤肉
5. 生抽(10ml)
6. 盐(4g)
7. 胡椒粉(8g)
8. 胡萝卜(30g)
9. 香葱(1颗)
10. 鸡蛋(1.5个)
11. 黄瓜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=18
source: rerank_input

```text
菜品: 咖喱肥牛
菜系: 未知
## 所需食材
1. 冷水(适量ml)
2. 咖喱块(100g)
3. 土豆(200g)
4. 洋葱(100g)
5. 纯牛奶(50ml)
6. 肥牛卷(300g)
7. 胡萝卜(150g)
8. 食用油(10-15ml)
9. 香叶(1片)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=19
source: rerank_input

```text
菜品: 罗宋汤
菜系: 未知
## 所需食材
1. 包菜(200g)
2. 植物油(5mL)
3. 橄榄油(5mL)
4. 欧芹(100g)
5. 洋葱(100g)
6. 牛肉(250g)
7. 牛肉高汤(500mL)
8. 番茄罐头(2罐)
9. 番茄膏(5g)
10. 盐(18g)
11. 红肠(150g)
12. 胡萝卜(100g)
13. 马铃薯(400g)
14. 黑胡椒(3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=20
source: rerank_input

```text
菜品: 燕麦鸡蛋饼
分类: 早餐
菜系: 未知
## 所需食材
1. 牛奶(50毫升)
2. 盐(适量克)
3. 纯干燕麦片(50克)
4. 胡椒(适量克)
5. 蔬菜（菠菜等）(50克)
6. 鸡蛋(2个)
7. 黄油(适量克)

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### pair_order=21
source: rerank_input

```text
菜品: 韭菜盒子
菜系: 未知
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=22
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

### pair_order=23
source: rerank_input

```text
菜品: 新疆大盘鸡
菜系: 西北菜
## 所需食材
1. 土豆(750g)
2. 大葱(100g)
3. 大蒜(4瓣)
4. 干线椒(5个)
5. 料酒(100g)
6. 油(50g)
7. 清水(1000ml)
8. 甜椒(50g)
9. 生抽(7ml)
10. 白砂糖(20g)
11. 盐(5g)
12. 花椒
13. 菜椒(50g)
14. 蚝油(10g)
15. 香叶(适量片)
16. 香果
17. 鸡腿肉(1000g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=24
source: rerank_input

```text
分类: 烹饪技巧
技巧文档扩展上下文: 如何决策吃什么
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
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201000655, recipe_name=空气炸锅面包片, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 空气炸锅面包片
分类: 早餐
难度: 1.0
主要食材: 面包片
关联图谱:
- OUT SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
- IN SIMILAR 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
- IN SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201000006, recipe_name=鸡蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201000718, recipe_name=金枪鱼酱三明治, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 金枪鱼酱三明治
分类: 早餐
难度: 1.0
主要食材: 俄式酸黄瓜汁, 芝士片, 火腿片
关联图谱:
- OUT REQUIRES 俄式酸黄瓜汁 (Ingredient): category: 调料
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 火腿片 (Ingredient): category: 蛋白质
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.7216987013816833, search_type=vector_enhanced

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

### result_order=4
source: reranked_results
metadata_summary: node_id=201000587, recipe_name=桂圆红枣粥, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 桂圆红枣粥
分类: 早餐
难度: 2.0
主要食材: 糯米, 红枣, 桂圆
关联图谱:
- OUT REQUIRES 糯米 (Ingredient): category: 淀粉类
- OUT REQUIRES 红枣 (Ingredient): category: 蔬菜
- OUT REQUIRES 桂圆 (Ingredient): category: 其他
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201000511, recipe_name=吐司果酱, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 吐司果酱
分类: 早餐
难度: 1.0
主要食材: 吐司, 果酱
关联图谱:
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
- OUT REQUIRES 果酱 (Ingredient): category: 调料
- OUT CONTAINS_STEP 步骤5 (CookingStep): description: 用餐巾纸包一下可以边走边吃也可以吃完再出门
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201000571, recipe_name=手抓饼, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 手抓饼
分类: 早餐
难度: 2.0
主要食材: 芝士片, 鸡蛋, 食用油
关联图谱:
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=7
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e, recipe_name=如何决策吃什么, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 如何决策吃什么
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
```

### result_order=8
source: reranked_results
metadata_summary: node_id=201000539, recipe_name=微波炉荷包蛋, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 微波炉荷包蛋
分类: 早餐
难度: 1.0
主要食材: 芝麻油, 饮用水, 鸡蛋
关联图谱:
- OUT REQUIRES 芝麻油 (Ingredient): category: 调料
- OUT REQUIRES 饮用水 (Ingredient): category: 其他
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
```

### result_order=9
source: reranked_results
metadata_summary: node_id=201000550, recipe_name=微波炉蛋糕, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 微波炉蛋糕
分类: 早餐
难度: 1.0
主要食材: 麦片, 香蕉, 牛奶
关联图谱:
- OUT REQUIRES 麦片 (Ingredient): category: 淀粉类
- OUT REQUIRES 香蕉 (Ingredient): category: 其他
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=10
source: reranked_results
metadata_summary: node_id=201000519, recipe_name=太阳蛋, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 太阳蛋
分类: 早餐
难度: 2.0
主要食材: 盐, 鸡蛋, 油
关联图谱:
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=11
source: reranked_results
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.6423543691635132, search_type=vector_enhanced

```text
## 所需食材
1. 牛奶(50毫升)
2. 盐(适量克)
3. 纯干燕麦片(50克)
4. 胡椒(适量克)
5. 蔬菜（菠菜等）(50克)
6. 鸡蛋(2个)
7. 黄油(适量克)

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=12
source: reranked_results
metadata_summary: node_id=201000644, recipe_name=牛奶燕麦, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 牛奶燕麦
分类: 早餐
难度: 1.0
主要食材: 鸡蛋, 燕麦, 牛奶
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=13
source: reranked_results
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6552770137786865, search_type=vector_enhanced

```text
## 所需食材
1. 冷饭(500ml)
2. 油(12ml)
3. 火腿(2个)
4. 灯影牛肉丝/午餐肉/腊肠/卤肉
5. 生抽(10ml)
6. 盐(4g)
7. 胡椒粉(8g)
8. 胡萝卜(30g)
9. 香葱(1颗)
10. 鸡蛋(1.5个)
11. 黄瓜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=14
source: reranked_results
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6705695986747742, search_type=vector_enhanced

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
source: reranked_results
metadata_summary: node_id=201002309, chunk_id=201002309_chunk_472, recipe_name=咖喱肥牛, category=荤菜, score=0.6480962038040161, search_type=vector_enhanced

```text
## 所需食材
1. 冷水(适量ml)
2. 咖喱块(100g)
3. 土豆(200g)
4. 洋葱(100g)
5. 纯牛奶(50ml)
6. 肥牛卷(300g)
7. 胡萝卜(150g)
8. 食用油(10-15ml)
9. 香叶(1片)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=16
source: reranked_results
metadata_summary: node_id=201001206, recipe_name=杨枝甘露, category=饮料, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 省时
菜品: 杨枝甘露
分类: 饮料
难度: 2.0
主要食材: 奇亚籽, 切丝芒果干, 切丝柳橙干
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 饮料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=17
source: reranked_results
metadata_summary: node_id=201003793, chunk_id=201003793_chunk_745, recipe_name=罗宋汤, category=汤类, score=0.6480680108070374, search_type=vector_enhanced

```text
## 所需食材
1. 包菜(200g)
2. 植物油(5mL)
3. 橄榄油(5mL)
4. 欧芹(100g)
5. 洋葱(100g)
6. 牛肉(250g)
7. 牛肉高汤(500mL)
8. 番茄罐头(2罐)
9. 番茄膏(5g)
10. 盐(18g)
11. 红肠(150g)
12. 胡萝卜(100g)
13. 马铃薯(400g)
14. 黑胡椒(3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=18
source: reranked_results
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.6345013380050659, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(750g)
2. 大葱(100g)
3. 大蒜(4瓣)
4. 干线椒(5个)
5. 料酒(100g)
6. 油(50g)
7. 清水(1000ml)
8. 甜椒(50g)
9. 生抽(7ml)
10. 白砂糖(20g)
11. 盐(5g)
12. 花椒
13. 菜椒(50g)
14. 蚝油(10g)
15. 香叶(适量片)
16. 香果
17. 鸡腿肉(1000g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=19
source: reranked_results
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6380630731582642, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=20
source: reranked_results
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.6363043785095215, search_type=vector_enhanced

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

### result_order=21
source: reranked_results
metadata_summary: node_id=201005725, recipe_name=鸡蛋羹, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋羹
菜品名称: 鸡蛋羹
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### result_order=22
source: reranked_results
metadata_summary: node_id=201004118, recipe_name=馒头, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 馒头
食材名称: 馒头
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=23
source: reranked_results
metadata_summary: node_id=201004534, recipe_name=煎蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 煎蛋
食材名称: 煎蛋
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=24
source: reranked_results
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.6632564067840576, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201000655, recipe_name=空气炸锅面包片, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 空气炸锅面包片
分类: 早餐
难度: 1.0
主要食材: 面包片
关联图谱:
- OUT SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
- IN SIMILAR 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
- IN SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201000006, recipe_name=鸡蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201000718, recipe_name=金枪鱼酱三明治, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 早餐
菜品: 金枪鱼酱三明治
分类: 早餐
难度: 1.0
主要食材: 俄式酸黄瓜汁, 芝士片, 火腿片
关联图谱:
- OUT REQUIRES 俄式酸黄瓜汁 (Ingredient): category: 调料
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 火腿片 (Ingredient): category: 蛋白质
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.7216987013816833, search_type=vector_enhanced

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

### result_order=4
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e, recipe_name=如何决策吃什么, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 如何决策吃什么
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
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201000655, recipe_name=空气炸锅面包片, category=早餐, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

```text
命中关键词: 早餐
菜品: 空气炸锅面包片
分类: 早餐
难度: 1.0
主要食材: 面包片
关联图谱:
- OUT SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
- IN SIMILAR 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
- IN SIMILAR 牛奶燕麦 (Recipe): category: 早餐；difficulty: 1.0
```

### result_order=1
source: generation_context
metadata_summary: node_id=201000006, recipe_name=鸡蛋, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

### result_order=2
source: generation_context
metadata_summary: node_id=201000718, recipe_name=金枪鱼酱三明治, category=早餐, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

```text
命中关键词: 早餐
菜品: 金枪鱼酱三明治
分类: 早餐
难度: 1.0
主要食材: 俄式酸黄瓜汁, 芝士片, 火腿片
关联图谱:
- OUT REQUIRES 俄式酸黄瓜汁 (Ingredient): category: 调料
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 火腿片 (Ingredient): category: 蛋白质
```

### result_order=3
source: generation_context
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.7216987013816833, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

### result_order=4
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e, recipe_name=如何决策吃什么, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

```text
技巧文档扩展上下文: 如何决策吃什么
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
```

