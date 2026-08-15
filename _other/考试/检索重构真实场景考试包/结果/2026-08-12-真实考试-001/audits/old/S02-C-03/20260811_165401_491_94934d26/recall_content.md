# Recall Content

audit_id: 20260811_165401_491_94934d26
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201005669, recipe_name=西葫芦炒鸡蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西葫芦炒鸡蛋
菜品名称: 西葫芦炒鸡蛋
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### result_order=1
source: entity_level
metadata_summary: node_id=201004808, recipe_name=西葫芦, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西葫芦
食材名称: 西葫芦
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
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

## Hybrid Retrieval / Topic Branch Raw Results
_no content_

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1124, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.7426695227622986, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，切成小块，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 西葫芦洗净，切成边长约为4cm的菱形，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 打三个鸡蛋到碗里，打散搅匀，备用
方法: 打散
工具: 碗,筷子

### 第4步
步骤: 步骤4
描述: 热锅，锅内放入5-10ml食用油
方法: 热锅
工具: 炒锅

### 第5步
步骤: 步骤5
描述: 倒入鸡蛋，保持翻炒至鸡蛋成固体，用锅铲分成小块后盛到碗里，备用
方法: 炒
工具: 炒锅,锅铲,碗

### 第6步
步骤: 步骤6
描述: 锅内放入5-10ml食用油，倒入西红柿，炒至变软
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 倒入西葫芦一起翻炒均匀，放入6g食用盐，将火调小然后等待4-5分钟
方法: 炒,焖
工具: 炒锅,锅铲
时间: 4-5分钟

### 第8步
步骤: 步骤8
描述: 倒入备用的鸡蛋，中火翻炒15秒
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 盛盘
工具: 锅铲
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1122, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.7217875719070435, search_type=vector_enhanced

```text
# 西葫芦炒鸡蛋
难度: 2.0星

时间信息: 准备时间: 约5分钟, 烹饪时间: 约8-9分钟
份量: 2人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6921697854995728, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_754, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6813176274299622, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将西红柿洗净，切块。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第2步
步骤: 步骤2
描述: 葱姜蒜切碎。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 鸡蛋打到碗中，用筷子（或打蛋器）搅拌均匀。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 热锅，并放入15毫升的油，待能从油中看到冒出一丝烟时，放入葱姜蒜翻炒30秒。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第5步
步骤: 步骤5
描述: 放入西红柿翻炒1分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 倒入水，水的高度大约为锅内菜品高度的1.2倍，并放入盐。
方法: 煮
工具: 炒锅
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 待开锅后，将鸡蛋液放入，并用筷子将鸡蛋打散，放入味素和香油。
方法: 煮,搅拌
工具: 筷子
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 等待30秒，关火出锅。
方法: 煮
工具: 炒锅
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201005272, chunk_id=201005272_chunk_1045, recipe_name=鸡蛋火腿炒黄瓜, category=素菜, score=0.6779815554618835, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 黄瓜洗净，切半圆形片，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 火腿切半圆形片，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 红尖椒（可选）切碎，备用
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入碗中，搅匀，即为鸡蛋液
方法: 搅拌
工具: 碗,筷子

### 第5步
步骤: 步骤5
描述: 热锅里倒5ml食用油
方法: 加热
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 油热后转小火，倒入打散的鸡蛋液，用筷子划散，翻炒至鸡蛋结为固体且颜色微微发黄，即为半熟鸡蛋，盛出备用
方法: 炒
工具: 炒锅,筷子
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 不用洗锅，往锅内倒入5ml食用油，倒入黄瓜片大火翻炒1分钟
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 把半熟鸡蛋倒入锅中，调入2g盐、3ml生抽，立刻倒入火腿片和辣椒碎（可选）翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201005583, chunk_id=201005583_chunk_1108, recipe_name=菠菜炒鸡蛋, category=素菜, score=0.6772553324699402, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菠菜去根，洗净，放在篮子里，焯水
方法: 切,焯水
工具: 刀,篮子,锅

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，搅匀
方法: 打,搅拌
工具: 碗,筷子

### 第3步
步骤: 步骤3
描述: 热锅，加入10ml油
方法: 加热
工具: 炒锅

### 第4步
步骤: 步骤4
描述: 油热后，倒入鸡蛋液，中火翻炒15秒，先煎成蛋饼，然后再用锅铲切成小块
方法: 煎,炒
工具: 锅铲
时间: 15秒

### 第5步
步骤: 步骤5
描述: 关火，将鸡蛋块盛到盘子中，不要洗锅
方法: 盛
工具: 盘子

### 第6步
步骤: 步骤6
描述: 重新开火，倒入5ml油，油热后，放入菠菜，大火翻炒15秒后，倒入鸡蛋块，翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第7步
步骤: 步骤7
描述: 加入5g盐、100ml饮用水，大火翻炒10秒
方法: 炒
工具: 锅铲
时间: 10秒

### 第8步
步骤: 步骤8
描述: 关火，盛盘
方法: 盛
工具: 盘子
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201005342, chunk_id=201005342_chunk_1060, recipe_name=包菜炒鸡蛋粉丝, category=素菜, score=0.6764200329780579, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 胡萝卜、包菜切丝备用
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 粉丝先用冷水浸泡1小时，然后将粉丝放入锅中，加入开水烧至粉丝烫软捞出备用
方法: 浸泡,煮
工具: 锅,漏勺
时间: 1小时+2分钟

### 第3步
步骤: 步骤3
描述: 鸡蛋打入碗中，加入盐后搅拌15秒
方法: 搅拌
工具: 碗,筷子
时间: 15秒

### 第4步
步骤: 步骤4
描述: 葱、蒜、辣椒切成小粒备用
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 起锅烧油，倒入鸡蛋，打散炒熟盛出
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第6步
步骤: 步骤6
描述: 再倒入油，放入葱、蒜、干辣椒翻炒8秒
方法: 炒
工具: 炒锅,锅铲
时间: 8秒

### 第7步
步骤: 步骤7
描述: 下胡萝卜、包菜丝儿翻炒30秒
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 放入粉丝
方法: 混合
工具: 锅铲
时间: 约5秒

### 第9步
步骤: 步骤9
描述: 放调料：生抽15 ml，老抽10 ml，蚝油10 ml，盐2克
方法: 调味
工具: 锅铲
时间: 约10秒

### 第10步
步骤: 步骤10
描述: 放入之前炒好的鸡蛋，翻炒约15秒
方法: 炒
工具: 锅铲
时间: 15秒

### 第11步
步骤: 步骤11
描述: 出锅摆盘
方法: 装盘
工具: 锅铲,盘子
时间: 约5秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1029, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6628136038780212, search_type=vector_enhanced

```text
## 标签
快速做法：鸡蛋与西红柿同炒,可用生抽替代部分盐,可选加番茄酱增汤汁,可选加熟肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1123, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.6611008644104004, search_type=vector_enhanced

```text
## 所需食材
1. 西红柿(100g)
2. 西葫芦(500g)
3. 食用油(10-20ml)
4. 食用盐(6g)
5. 鸡蛋(3个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201004478, chunk_id=201004478_chunk_894, recipe_name=扬州炒饭, category=主食, score=0.655517041683197, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 胡萝卜切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 午餐肉切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 葱分别取葱白和葱绿，各切成 0.25-0.5cm 的小段，分开备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 在碗中打入鸡蛋液，均匀搅拌，备用
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 将胡萝卜、青豆、玉米粒煮熟捞出，备用（水别倒）
方法: 煮
工具: 锅,漏勺
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将虾煮熟，捞出备用（水可以倒了）
方法: 煮
工具: 锅,漏勺
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 热锅热油（第二次倒油 20-30ml），油温后缓慢倒入鸡蛋液，不搅拌
方法: 炒,煎
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 鸡蛋凝固后立刻捞出，备用
方法: 炒
工具: 锅铲
时间: 10秒

### 第9步
步骤: 步骤9
描述: 将午餐肉、青豆、胡萝卜、玉米粒、虾倒入锅中翻炒 1-2 分钟，装盘备用
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第10步
步骤: 步骤10
描述: 水冲一下锅，将杂物冲干净，保证锅内干净（可以有油但无杂质）
方法: 清洗
工具: 水
时间: 30秒

### 第11步
步骤: 步骤11
描述: 热锅热油（10ml），将葱白放入爆香
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第12步
步骤: 步骤12
描述: 调至小火，放入米饭，用铲子快速砸击米饭并翻炒，使米饭粒粒分明
方法: 炒
工具: 锅铲
时间: 2分钟

### 第13步
步骤: 步骤13
描述: 倒入鸡蛋，继续砸击，使鸡蛋碎开并与米饭充分混合
方法: 炒
工具: 锅铲
时间: 1分钟

### 第14步
步骤: 步骤14
描述: 转大火，倒入所有备用配料，快速翻炒 1-2 分钟
方法: 炒
工具: 锅铲
时间: 1-2分钟

### 第15步
步骤: 步骤15
描述: 撒入盐，并翻炒至充分混合
方法: 炒
工具: 锅铲
时间: 30秒

### 第16步
步骤: 步骤16
描述: 撒入葱绿，翻炒 1 分钟
方法: 炒
工具: 锅铲
时间: 1分钟

### 第17步
步骤: 步骤17
描述: 关火，装盘
方法: 装盘
工具: 锅铲,盘子
时间: 10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201005669, recipe_name=西葫芦炒鸡蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西葫芦炒鸡蛋
菜品名称: 西葫芦炒鸡蛋
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201004808, recipe_name=西葫芦, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西葫芦
食材名称: 西葫芦
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
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

### result_order=3
source: branch_grouped
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1124, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.7426695227622986, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，切成小块，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 西葫芦洗净，切成边长约为4cm的菱形，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 打三个鸡蛋到碗里，打散搅匀，备用
方法: 打散
工具: 碗,筷子

### 第4步
步骤: 步骤4
描述: 热锅，锅内放入5-10ml食用油
方法: 热锅
工具: 炒锅

### 第5步
步骤: 步骤5
描述: 倒入鸡蛋，保持翻炒至鸡蛋成固体，用锅铲分成小块后盛到碗里，备用
方法: 炒
工具: 炒锅,锅铲,碗

### 第6步
步骤: 步骤6
描述: 锅内放入5-10ml食用油，倒入西红柿，炒至变软
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 倒入西葫芦一起翻炒均匀，放入6g食用盐，将火调小然后等待4-5分钟
方法: 炒,焖
工具: 炒锅,锅铲
时间: 4-5分钟

### 第8步
步骤: 步骤8
描述: 倒入备用的鸡蛋，中火翻炒15秒
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 盛盘
工具: 锅铲
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1122, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.7217875719070435, search_type=vector_enhanced

```text
# 西葫芦炒鸡蛋
难度: 2.0星

时间信息: 准备时间: 约5分钟, 烹饪时间: 约8-9分钟
份量: 2人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6921697854995728, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_754, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6813176274299622, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将西红柿洗净，切块。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第2步
步骤: 步骤2
描述: 葱姜蒜切碎。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 鸡蛋打到碗中，用筷子（或打蛋器）搅拌均匀。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 热锅，并放入15毫升的油，待能从油中看到冒出一丝烟时，放入葱姜蒜翻炒30秒。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第5步
步骤: 步骤5
描述: 放入西红柿翻炒1分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 倒入水，水的高度大约为锅内菜品高度的1.2倍，并放入盐。
方法: 煮
工具: 炒锅
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 待开锅后，将鸡蛋液放入，并用筷子将鸡蛋打散，放入味素和香油。
方法: 煮,搅拌
工具: 筷子
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 等待30秒，关火出锅。
方法: 煮
工具: 炒锅
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201005272, chunk_id=201005272_chunk_1045, recipe_name=鸡蛋火腿炒黄瓜, category=素菜, score=0.6779815554618835, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 黄瓜洗净，切半圆形片，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 火腿切半圆形片，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 红尖椒（可选）切碎，备用
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入碗中，搅匀，即为鸡蛋液
方法: 搅拌
工具: 碗,筷子

### 第5步
步骤: 步骤5
描述: 热锅里倒5ml食用油
方法: 加热
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 油热后转小火，倒入打散的鸡蛋液，用筷子划散，翻炒至鸡蛋结为固体且颜色微微发黄，即为半熟鸡蛋，盛出备用
方法: 炒
工具: 炒锅,筷子
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 不用洗锅，往锅内倒入5ml食用油，倒入黄瓜片大火翻炒1分钟
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 把半熟鸡蛋倒入锅中，调入2g盐、3ml生抽，立刻倒入火腿片和辣椒碎（可选）翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201005583, chunk_id=201005583_chunk_1108, recipe_name=菠菜炒鸡蛋, category=素菜, score=0.6772553324699402, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菠菜去根，洗净，放在篮子里，焯水
方法: 切,焯水
工具: 刀,篮子,锅

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，搅匀
方法: 打,搅拌
工具: 碗,筷子

### 第3步
步骤: 步骤3
描述: 热锅，加入10ml油
方法: 加热
工具: 炒锅

### 第4步
步骤: 步骤4
描述: 油热后，倒入鸡蛋液，中火翻炒15秒，先煎成蛋饼，然后再用锅铲切成小块
方法: 煎,炒
工具: 锅铲
时间: 15秒

### 第5步
步骤: 步骤5
描述: 关火，将鸡蛋块盛到盘子中，不要洗锅
方法: 盛
工具: 盘子

### 第6步
步骤: 步骤6
描述: 重新开火，倒入5ml油，油热后，放入菠菜，大火翻炒15秒后，倒入鸡蛋块，翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第7步
步骤: 步骤7
描述: 加入5g盐、100ml饮用水，大火翻炒10秒
方法: 炒
工具: 锅铲
时间: 10秒

### 第8步
步骤: 步骤8
描述: 关火，盛盘
方法: 盛
工具: 盘子
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201005342, chunk_id=201005342_chunk_1060, recipe_name=包菜炒鸡蛋粉丝, category=素菜, score=0.6764200329780579, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 胡萝卜、包菜切丝备用
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 粉丝先用冷水浸泡1小时，然后将粉丝放入锅中，加入开水烧至粉丝烫软捞出备用
方法: 浸泡,煮
工具: 锅,漏勺
时间: 1小时+2分钟

### 第3步
步骤: 步骤3
描述: 鸡蛋打入碗中，加入盐后搅拌15秒
方法: 搅拌
工具: 碗,筷子
时间: 15秒

### 第4步
步骤: 步骤4
描述: 葱、蒜、辣椒切成小粒备用
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 起锅烧油，倒入鸡蛋，打散炒熟盛出
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第6步
步骤: 步骤6
描述: 再倒入油，放入葱、蒜、干辣椒翻炒8秒
方法: 炒
工具: 炒锅,锅铲
时间: 8秒

### 第7步
步骤: 步骤7
描述: 下胡萝卜、包菜丝儿翻炒30秒
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 放入粉丝
方法: 混合
工具: 锅铲
时间: 约5秒

### 第9步
步骤: 步骤9
描述: 放调料：生抽15 ml，老抽10 ml，蚝油10 ml，盐2克
方法: 调味
工具: 锅铲
时间: 约10秒

### 第10步
步骤: 步骤10
描述: 放入之前炒好的鸡蛋，翻炒约15秒
方法: 炒
工具: 锅铲
时间: 15秒

### 第11步
步骤: 步骤11
描述: 出锅摆盘
方法: 装盘
工具: 锅铲,盘子
时间: 约5秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1029, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6628136038780212, search_type=vector_enhanced

```text
## 标签
快速做法：鸡蛋与西红柿同炒,可用生抽替代部分盐,可选加番茄酱增汤汁,可选加熟肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1123, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.6611008644104004, search_type=vector_enhanced

```text
## 所需食材
1. 西红柿(100g)
2. 西葫芦(500g)
3. 食用油(10-20ml)
4. 食用盐(6g)
5. 鸡蛋(3个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201004478, chunk_id=201004478_chunk_894, recipe_name=扬州炒饭, category=主食, score=0.655517041683197, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 胡萝卜切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 午餐肉切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 葱分别取葱白和葱绿，各切成 0.25-0.5cm 的小段，分开备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 在碗中打入鸡蛋液，均匀搅拌，备用
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 将胡萝卜、青豆、玉米粒煮熟捞出，备用（水别倒）
方法: 煮
工具: 锅,漏勺
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将虾煮熟，捞出备用（水可以倒了）
方法: 煮
工具: 锅,漏勺
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 热锅热油（第二次倒油 20-30ml），油温后缓慢倒入鸡蛋液，不搅拌
方法: 炒,煎
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 鸡蛋凝固后立刻捞出，备用
方法: 炒
工具: 锅铲
时间: 10秒

### 第9步
步骤: 步骤9
描述: 将午餐肉、青豆、胡萝卜、玉米粒、虾倒入锅中翻炒 1-2 分钟，装盘备用
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第10步
步骤: 步骤10
描述: 水冲一下锅，将杂物冲干净，保证锅内干净（可以有油但无杂质）
方法: 清洗
工具: 水
时间: 30秒

### 第11步
步骤: 步骤11
描述: 热锅热油（10ml），将葱白放入爆香
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第12步
步骤: 步骤12
描述: 调至小火，放入米饭，用铲子快速砸击米饭并翻炒，使米饭粒粒分明
方法: 炒
工具: 锅铲
时间: 2分钟

### 第13步
步骤: 步骤13
描述: 倒入鸡蛋，继续砸击，使鸡蛋碎开并与米饭充分混合
方法: 炒
工具: 锅铲
时间: 1分钟

### 第14步
步骤: 步骤14
描述: 转大火，倒入所有备用配料，快速翻炒 1-2 分钟
方法: 炒
工具: 锅铲
时间: 1-2分钟

### 第15步
步骤: 步骤15
描述: 撒入盐，并翻炒至充分混合
方法: 炒
工具: 锅铲
时间: 30秒

### 第16步
步骤: 步骤16
描述: 撒入葱绿，翻炒 1 分钟
方法: 炒
工具: 锅铲
时间: 1分钟

### 第17步
步骤: 步骤17
描述: 关火，装盘
方法: 装盘
工具: 锅铲,盘子
时间: 10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1124, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.7426695227622986, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，切成小块，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 西葫芦洗净，切成边长约为4cm的菱形，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 打三个鸡蛋到碗里，打散搅匀，备用
方法: 打散
工具: 碗,筷子

### 第4步
步骤: 步骤4
描述: 热锅，锅内放入5-10ml食用油
方法: 热锅
工具: 炒锅

### 第5步
步骤: 步骤5
描述: 倒入鸡蛋，保持翻炒至鸡蛋成固体，用锅铲分成小块后盛到碗里，备用
方法: 炒
工具: 炒锅,锅铲,碗

### 第6步
步骤: 步骤6
描述: 锅内放入5-10ml食用油，倒入西红柿，炒至变软
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 倒入西葫芦一起翻炒均匀，放入6g食用盐，将火调小然后等待4-5分钟
方法: 炒,焖
工具: 炒锅,锅铲
时间: 4-5分钟

### 第8步
步骤: 步骤8
描述: 倒入备用的鸡蛋，中火翻炒15秒
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 盛盘
工具: 锅铲
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201004808, recipe_name=西葫芦, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西葫芦
食材名称: 西葫芦
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
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

### result_order=3
source: merged_candidates
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6921697854995728, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_754, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6813176274299622, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将西红柿洗净，切块。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第2步
步骤: 步骤2
描述: 葱姜蒜切碎。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 鸡蛋打到碗中，用筷子（或打蛋器）搅拌均匀。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 热锅，并放入15毫升的油，待能从油中看到冒出一丝烟时，放入葱姜蒜翻炒30秒。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第5步
步骤: 步骤5
描述: 放入西红柿翻炒1分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 倒入水，水的高度大约为锅内菜品高度的1.2倍，并放入盐。
方法: 煮
工具: 炒锅
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 待开锅后，将鸡蛋液放入，并用筷子将鸡蛋打散，放入味素和香油。
方法: 煮,搅拌
工具: 筷子
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 等待30秒，关火出锅。
方法: 煮
工具: 炒锅
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201005272, chunk_id=201005272_chunk_1045, recipe_name=鸡蛋火腿炒黄瓜, category=素菜, score=0.6779815554618835, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 黄瓜洗净，切半圆形片，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 火腿切半圆形片，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 红尖椒（可选）切碎，备用
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入碗中，搅匀，即为鸡蛋液
方法: 搅拌
工具: 碗,筷子

### 第5步
步骤: 步骤5
描述: 热锅里倒5ml食用油
方法: 加热
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 油热后转小火，倒入打散的鸡蛋液，用筷子划散，翻炒至鸡蛋结为固体且颜色微微发黄，即为半熟鸡蛋，盛出备用
方法: 炒
工具: 炒锅,筷子
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 不用洗锅，往锅内倒入5ml食用油，倒入黄瓜片大火翻炒1分钟
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 把半熟鸡蛋倒入锅中，调入2g盐、3ml生抽，立刻倒入火腿片和辣椒碎（可选）翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=201005583, chunk_id=201005583_chunk_1108, recipe_name=菠菜炒鸡蛋, category=素菜, score=0.6772553324699402, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菠菜去根，洗净，放在篮子里，焯水
方法: 切,焯水
工具: 刀,篮子,锅

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，搅匀
方法: 打,搅拌
工具: 碗,筷子

### 第3步
步骤: 步骤3
描述: 热锅，加入10ml油
方法: 加热
工具: 炒锅

### 第4步
步骤: 步骤4
描述: 油热后，倒入鸡蛋液，中火翻炒15秒，先煎成蛋饼，然后再用锅铲切成小块
方法: 煎,炒
工具: 锅铲
时间: 15秒

### 第5步
步骤: 步骤5
描述: 关火，将鸡蛋块盛到盘子中，不要洗锅
方法: 盛
工具: 盘子

### 第6步
步骤: 步骤6
描述: 重新开火，倒入5ml油，油热后，放入菠菜，大火翻炒15秒后，倒入鸡蛋块，翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第7步
步骤: 步骤7
描述: 加入5g盐、100ml饮用水，大火翻炒10秒
方法: 炒
工具: 锅铲
时间: 10秒

### 第8步
步骤: 步骤8
描述: 关火，盛盘
方法: 盛
工具: 盘子
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201005342, chunk_id=201005342_chunk_1060, recipe_name=包菜炒鸡蛋粉丝, category=素菜, score=0.6764200329780579, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 胡萝卜、包菜切丝备用
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 粉丝先用冷水浸泡1小时，然后将粉丝放入锅中，加入开水烧至粉丝烫软捞出备用
方法: 浸泡,煮
工具: 锅,漏勺
时间: 1小时+2分钟

### 第3步
步骤: 步骤3
描述: 鸡蛋打入碗中，加入盐后搅拌15秒
方法: 搅拌
工具: 碗,筷子
时间: 15秒

### 第4步
步骤: 步骤4
描述: 葱、蒜、辣椒切成小粒备用
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 起锅烧油，倒入鸡蛋，打散炒熟盛出
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第6步
步骤: 步骤6
描述: 再倒入油，放入葱、蒜、干辣椒翻炒8秒
方法: 炒
工具: 炒锅,锅铲
时间: 8秒

### 第7步
步骤: 步骤7
描述: 下胡萝卜、包菜丝儿翻炒30秒
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 放入粉丝
方法: 混合
工具: 锅铲
时间: 约5秒

### 第9步
步骤: 步骤9
描述: 放调料：生抽15 ml，老抽10 ml，蚝油10 ml，盐2克
方法: 调味
工具: 锅铲
时间: 约10秒

### 第10步
步骤: 步骤10
描述: 放入之前炒好的鸡蛋，翻炒约15秒
方法: 炒
工具: 锅铲
时间: 15秒

### 第11步
步骤: 步骤11
描述: 出锅摆盘
方法: 装盘
工具: 锅铲,盘子
时间: 约5秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201004478, chunk_id=201004478_chunk_894, recipe_name=扬州炒饭, category=主食, score=0.655517041683197, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 胡萝卜切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 午餐肉切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 葱分别取葱白和葱绿，各切成 0.25-0.5cm 的小段，分开备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 在碗中打入鸡蛋液，均匀搅拌，备用
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 将胡萝卜、青豆、玉米粒煮熟捞出，备用（水别倒）
方法: 煮
工具: 锅,漏勺
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将虾煮熟，捞出备用（水可以倒了）
方法: 煮
工具: 锅,漏勺
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 热锅热油（第二次倒油 20-30ml），油温后缓慢倒入鸡蛋液，不搅拌
方法: 炒,煎
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 鸡蛋凝固后立刻捞出，备用
方法: 炒
工具: 锅铲
时间: 10秒

### 第9步
步骤: 步骤9
描述: 将午餐肉、青豆、胡萝卜、玉米粒、虾倒入锅中翻炒 1-2 分钟，装盘备用
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第10步
步骤: 步骤10
描述: 水冲一下锅，将杂物冲干净，保证锅内干净（可以有油但无杂质）
方法: 清洗
工具: 水
时间: 30秒

### 第11步
步骤: 步骤11
描述: 热锅热油（10ml），将葱白放入爆香
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第12步
步骤: 步骤12
描述: 调至小火，放入米饭，用铲子快速砸击米饭并翻炒，使米饭粒粒分明
方法: 炒
工具: 锅铲
时间: 2分钟

### 第13步
步骤: 步骤13
描述: 倒入鸡蛋，继续砸击，使鸡蛋碎开并与米饭充分混合
方法: 炒
工具: 锅铲
时间: 1分钟

### 第14步
步骤: 步骤14
描述: 转大火，倒入所有备用配料，快速翻炒 1-2 分钟
方法: 炒
工具: 锅铲
时间: 1-2分钟

### 第15步
步骤: 步骤15
描述: 撒入盐，并翻炒至充分混合
方法: 炒
工具: 锅铲
时间: 30秒

### 第16步
步骤: 步骤16
描述: 撒入葱绿，翻炒 1 分钟
方法: 炒
工具: 锅铲
时间: 1分钟

### 第17步
步骤: 步骤17
描述: 关火，装盘
方法: 装盘
工具: 锅铲,盘子
时间: 10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
菜品: 西葫芦炒鸡蛋
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，切成小块，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 西葫芦洗净，切成边长约为4cm的菱形，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 打三个鸡蛋到碗里，打散搅匀，备用
方法: 打散
工具: 碗,筷子

### 第4步
步骤: 步骤4
描述: 热锅，锅内放入5-10ml食用油
方法: 热锅
工具: 炒锅

### 第5步
步骤: 步骤5
描述: 倒入鸡蛋，保持翻炒至鸡蛋成固体，用锅铲分成小块后盛到碗里，备用
方法: 炒
工具: 炒锅,锅铲,碗

### 第6步
步骤: 步骤6
描述: 锅内放入5-10ml食用油，倒入西红柿，炒至变软
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 倒入西葫芦一起翻炒均匀，放入6g食用盐，将火调小然后等待4-5分钟
方法: 炒,焖
工具: 炒锅,锅铲
时间: 4-5分钟

### 第8步
步骤: 步骤8
描述: 倒入备用的鸡蛋，中火翻炒15秒
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 盛盘
工具: 锅铲
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=1
source: rerank_input

```text
命中关键词: 西葫芦
食材名称: 西葫芦
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

### pair_order=3
source: rerank_input

```text
菜品: 西红柿炒鸡蛋
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=4
source: rerank_input

```text
菜品: 西红柿鸡蛋汤
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将西红柿洗净，切块。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第2步
步骤: 步骤2
描述: 葱姜蒜切碎。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 鸡蛋打到碗中，用筷子（或打蛋器）搅拌均匀。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 热锅，并放入15毫升的油，待能从油中看到冒出一丝烟时，放入葱姜蒜翻炒30秒。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第5步
步骤: 步骤5
描述: 放入西红柿翻炒1分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 倒入水，水的高度大约为锅内菜品高度的1.2倍，并放入盐。
方法: 煮
工具: 炒锅
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 待开锅后，将鸡蛋液放入，并用筷子将鸡蛋打散，放入味素和香油。
方法: 煮,搅拌
工具: 筷子
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 等待30秒，关火出锅。
方法: 煮
工具: 炒锅
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=5
source: rerank_input

```text
菜品: 鸡蛋火腿炒黄瓜
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 黄瓜洗净，切半圆形片，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 火腿切半圆形片，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 红尖椒（可选）切碎，备用
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入碗中，搅匀，即为鸡蛋液
方法: 搅拌
工具: 碗,筷子

### 第5步
步骤: 步骤5
描述: 热锅里倒5ml食用油
方法: 加热
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 油热后转小火，倒入打散的鸡蛋液，用筷子划散，翻炒至鸡蛋结为固体且颜色微微发黄，即为半熟鸡蛋，盛出备用
方法: 炒
工具: 炒锅,筷子
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 不用洗锅，往锅内倒入5ml食用油，倒入黄瓜片大火翻炒1分钟
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 把半熟鸡蛋倒入锅中，调入2g盐、3ml生抽，立刻倒入火腿片和辣椒碎（可选）翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=6
source: rerank_input

```text
菜品: 菠菜炒鸡蛋
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菠菜去根，洗净，放在篮子里，焯水
方法: 切,焯水
工具: 刀,篮子,锅

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，搅匀
方法: 打,搅拌
工具: 碗,筷子

### 第3步
步骤: 步骤3
描述: 热锅，加入10ml油
方法: 加热
工具: 炒锅

### 第4步
步骤: 步骤4
描述: 油热后，倒入鸡蛋液，中火翻炒15秒，先煎成蛋饼，然后再用锅铲切成小块
方法: 煎,炒
工具: 锅铲
时间: 15秒

### 第5步
步骤: 步骤5
描述: 关火，将鸡蛋块盛到盘子中，不要洗锅
方法: 盛
工具: 盘子

### 第6步
步骤: 步骤6
描述: 重新开火，倒入5ml油，油热后，放入菠菜，大火翻炒15秒后，倒入鸡蛋块，翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第7步
步骤: 步骤7
描述: 加入5g盐、100ml饮用水，大火翻炒10秒
方法: 炒
工具: 锅铲
时间: 10秒

### 第8步
步骤: 步骤8
描述: 关火，盛盘
方法: 盛
工具: 盘子
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=7
source: rerank_input

```text
菜品: 包菜炒鸡蛋粉丝
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 胡萝卜、包菜切丝备用
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 粉丝先用冷水浸泡1小时，然后将粉丝放入锅中，加入开水烧至粉丝烫软捞出备用
方法: 浸泡,煮
工具: 锅,漏勺
时间: 1小时+2分钟

### 第3步
步骤: 步骤3
描述: 鸡蛋打入碗中，加入盐后搅拌15秒
方法: 搅拌
工具: 碗,筷子
时间: 15秒

### 第4步
步骤: 步骤4
描述: 葱、蒜、辣椒切成小粒备用
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 起锅烧油，倒入鸡蛋，打散炒熟盛出
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第6步
步骤: 步骤6
描述: 再倒入油，放入葱、蒜、干辣椒翻炒8秒
方法: 炒
工具: 炒锅,锅铲
时间: 8秒

### 第7步
步骤: 步骤7
描述: 下胡萝卜、包菜丝儿翻炒30秒
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 放入粉丝
方法: 混合
工具: 锅铲
时间: 约5秒

### 第9步
步骤: 步骤9
描述: 放调料：生抽15 ml，老抽10 ml，蚝油10 ml，盐2克
方法: 调味
工具: 锅铲
时间: 约10秒

### 第10步
步骤: 步骤10
描述: 放入之前炒好的鸡蛋，翻炒约15秒
方法: 炒
工具: 锅铲
时间: 15秒

### 第11步
步骤: 步骤11
描述: 出锅摆盘
方法: 装盘
工具: 锅铲,盘子
时间: 约5秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=8
source: rerank_input

```text
菜品: 扬州炒饭
菜系: 苏菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 胡萝卜切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 午餐肉切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 葱分别取葱白和葱绿，各切成 0.25-0.5cm 的小段，分开备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 在碗中打入鸡蛋液，均匀搅拌，备用
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 将胡萝卜、青豆、玉米粒煮熟捞出，备用（水别倒）
方法: 煮
工具: 锅,漏勺
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将虾煮熟，捞出备用（水可以倒了）
方法: 煮
工具: 锅,漏勺
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 热锅热油（第二次倒油 20-30ml），油温后缓慢倒入鸡蛋液，不搅拌
方法: 炒,煎
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 鸡蛋凝固后立刻捞出，备用
方法: 炒
工具: 锅铲
时间: 10秒

### 第9步
步骤: 步骤9
描述: 将午餐肉、青豆、胡萝卜、玉米粒、虾倒入锅中翻炒 1-2 分钟，装盘备用
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第10步
步骤: 步骤10
描述: 水冲一下锅，将杂物冲干净，保证锅内干净（可以有油但无杂质）
方法: 清洗
工具: 水
时间: 30秒

### 第11步
步骤: 步骤11
描述: 热锅热油（10ml），将葱白放入爆香
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第12步
步骤: 步骤12
描述: 调至小火，放入米饭，用铲子快速砸击米饭并翻炒，使米饭粒粒分明
方法: 炒
工具: 锅铲
时间: 2分钟

### 第13步
步骤: 步骤13
描述: 倒入鸡蛋，
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1124, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.7426695227622986, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，切成小块，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 西葫芦洗净，切成边长约为4cm的菱形，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 打三个鸡蛋到碗里，打散搅匀，备用
方法: 打散
工具: 碗,筷子

### 第4步
步骤: 步骤4
描述: 热锅，锅内放入5-10ml食用油
方法: 热锅
工具: 炒锅

### 第5步
步骤: 步骤5
描述: 倒入鸡蛋，保持翻炒至鸡蛋成固体，用锅铲分成小块后盛到碗里，备用
方法: 炒
工具: 炒锅,锅铲,碗

### 第6步
步骤: 步骤6
描述: 锅内放入5-10ml食用油，倒入西红柿，炒至变软
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 倒入西葫芦一起翻炒均匀，放入6g食用盐，将火调小然后等待4-5分钟
方法: 炒,焖
工具: 炒锅,锅铲
时间: 4-5分钟

### 第8步
步骤: 步骤8
描述: 倒入备用的鸡蛋，中火翻炒15秒
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 盛盘
工具: 锅铲
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6921697854995728, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201005342, chunk_id=201005342_chunk_1060, recipe_name=包菜炒鸡蛋粉丝, category=素菜, score=0.6764200329780579, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 胡萝卜、包菜切丝备用
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 粉丝先用冷水浸泡1小时，然后将粉丝放入锅中，加入开水烧至粉丝烫软捞出备用
方法: 浸泡,煮
工具: 锅,漏勺
时间: 1小时+2分钟

### 第3步
步骤: 步骤3
描述: 鸡蛋打入碗中，加入盐后搅拌15秒
方法: 搅拌
工具: 碗,筷子
时间: 15秒

### 第4步
步骤: 步骤4
描述: 葱、蒜、辣椒切成小粒备用
方法: 切
工具: 刀,案板
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 起锅烧油，倒入鸡蛋，打散炒熟盛出
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第6步
步骤: 步骤6
描述: 再倒入油，放入葱、蒜、干辣椒翻炒8秒
方法: 炒
工具: 炒锅,锅铲
时间: 8秒

### 第7步
步骤: 步骤7
描述: 下胡萝卜、包菜丝儿翻炒30秒
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 放入粉丝
方法: 混合
工具: 锅铲
时间: 约5秒

### 第9步
步骤: 步骤9
描述: 放调料：生抽15 ml，老抽10 ml，蚝油10 ml，盐2克
方法: 调味
工具: 锅铲
时间: 约10秒

### 第10步
步骤: 步骤10
描述: 放入之前炒好的鸡蛋，翻炒约15秒
方法: 炒
工具: 锅铲
时间: 15秒

### 第11步
步骤: 步骤11
描述: 出锅摆盘
方法: 装盘
工具: 锅铲,盘子
时间: 约5秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_754, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6813176274299622, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将西红柿洗净，切块。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第2步
步骤: 步骤2
描述: 葱姜蒜切碎。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 鸡蛋打到碗中，用筷子（或打蛋器）搅拌均匀。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 热锅，并放入15毫升的油，待能从油中看到冒出一丝烟时，放入葱姜蒜翻炒30秒。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第5步
步骤: 步骤5
描述: 放入西红柿翻炒1分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 倒入水，水的高度大约为锅内菜品高度的1.2倍，并放入盐。
方法: 煮
工具: 炒锅
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 待开锅后，将鸡蛋液放入，并用筷子将鸡蛋打散，放入味素和香油。
方法: 煮,搅拌
工具: 筷子
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 等待30秒，关火出锅。
方法: 煮
工具: 炒锅
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201004478, chunk_id=201004478_chunk_894, recipe_name=扬州炒饭, category=主食, score=0.655517041683197, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 胡萝卜切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 午餐肉切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 葱分别取葱白和葱绿，各切成 0.25-0.5cm 的小段，分开备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 在碗中打入鸡蛋液，均匀搅拌，备用
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 将胡萝卜、青豆、玉米粒煮熟捞出，备用（水别倒）
方法: 煮
工具: 锅,漏勺
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将虾煮熟，捞出备用（水可以倒了）
方法: 煮
工具: 锅,漏勺
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 热锅热油（第二次倒油 20-30ml），油温后缓慢倒入鸡蛋液，不搅拌
方法: 炒,煎
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 鸡蛋凝固后立刻捞出，备用
方法: 炒
工具: 锅铲
时间: 10秒

### 第9步
步骤: 步骤9
描述: 将午餐肉、青豆、胡萝卜、玉米粒、虾倒入锅中翻炒 1-2 分钟，装盘备用
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第10步
步骤: 步骤10
描述: 水冲一下锅，将杂物冲干净，保证锅内干净（可以有油但无杂质）
方法: 清洗
工具: 水
时间: 30秒

### 第11步
步骤: 步骤11
描述: 热锅热油（10ml），将葱白放入爆香
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第12步
步骤: 步骤12
描述: 调至小火，放入米饭，用铲子快速砸击米饭并翻炒，使米饭粒粒分明
方法: 炒
工具: 锅铲
时间: 2分钟

### 第13步
步骤: 步骤13
描述: 倒入鸡蛋，继续砸击，使鸡蛋碎开并与米饭充分混合
方法: 炒
工具: 锅铲
时间: 1分钟

### 第14步
步骤: 步骤14
描述: 转大火，倒入所有备用配料，快速翻炒 1-2 分钟
方法: 炒
工具: 锅铲
时间: 1-2分钟

### 第15步
步骤: 步骤15
描述: 撒入盐，并翻炒至充分混合
方法: 炒
工具: 锅铲
时间: 30秒

### 第16步
步骤: 步骤16
描述: 撒入葱绿，翻炒 1 分钟
方法: 炒
工具: 锅铲
时间: 1分钟

### 第17步
步骤: 步骤17
描述: 关火，装盘
方法: 装盘
工具: 锅铲,盘子
时间: 10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201005583, chunk_id=201005583_chunk_1108, recipe_name=菠菜炒鸡蛋, category=素菜, score=0.6772553324699402, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菠菜去根，洗净，放在篮子里，焯水
方法: 切,焯水
工具: 刀,篮子,锅

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，搅匀
方法: 打,搅拌
工具: 碗,筷子

### 第3步
步骤: 步骤3
描述: 热锅，加入10ml油
方法: 加热
工具: 炒锅

### 第4步
步骤: 步骤4
描述: 油热后，倒入鸡蛋液，中火翻炒15秒，先煎成蛋饼，然后再用锅铲切成小块
方法: 煎,炒
工具: 锅铲
时间: 15秒

### 第5步
步骤: 步骤5
描述: 关火，将鸡蛋块盛到盘子中，不要洗锅
方法: 盛
工具: 盘子

### 第6步
步骤: 步骤6
描述: 重新开火，倒入5ml油，油热后，放入菠菜，大火翻炒15秒后，倒入鸡蛋块，翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第7步
步骤: 步骤7
描述: 加入5g盐、100ml饮用水，大火翻炒10秒
方法: 炒
工具: 锅铲
时间: 10秒

### 第8步
步骤: 步骤8
描述: 关火，盛盘
方法: 盛
工具: 盘子
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201005272, chunk_id=201005272_chunk_1045, recipe_name=鸡蛋火腿炒黄瓜, category=素菜, score=0.6779815554618835, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 黄瓜洗净，切半圆形片，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 火腿切半圆形片，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 红尖椒（可选）切碎，备用
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入碗中，搅匀，即为鸡蛋液
方法: 搅拌
工具: 碗,筷子

### 第5步
步骤: 步骤5
描述: 热锅里倒5ml食用油
方法: 加热
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 油热后转小火，倒入打散的鸡蛋液，用筷子划散，翻炒至鸡蛋结为固体且颜色微微发黄，即为半熟鸡蛋，盛出备用
方法: 炒
工具: 炒锅,筷子
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 不用洗锅，往锅内倒入5ml食用油，倒入黄瓜片大火翻炒1分钟
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 把半熟鸡蛋倒入锅中，调入2g盐、3ml生抽，立刻倒入火腿片和辣椒碎（可选）翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201004808, recipe_name=西葫芦, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西葫芦
食材名称: 西葫芦
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=8
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

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1124, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.7426695227622986, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，切成小块，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 西葫芦洗净，切成边长约为4cm的菱形，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 打三个鸡蛋到碗里，打散搅匀，备用
方法: 打散
工具: 碗,筷子

### 第4步
步骤: 步骤4
描述: 热锅，锅内放入5-10ml食用油
方法: 热锅
工具: 炒锅

### 第5步
步骤: 步骤5
描述: 倒入鸡蛋，保持翻炒至鸡蛋成固体，用锅铲分成小块后盛到碗里，备用
方法: 炒
工具: 炒锅,锅铲,碗

### 第6步
步骤: 步骤6
描述: 锅内放入5-10ml食用油，倒入西红柿，炒至变软
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 倒入西葫芦一起翻炒均匀，放入6g食用盐，将火调小然后等待4-5分钟
方法: 炒,焖
工具: 炒锅,锅铲
时间: 4-5分钟

### 第8步
步骤: 步骤8
描述: 倒入备用的鸡蛋，中火翻炒15秒
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 盛盘
工具: 锅铲
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6921697854995728, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_754, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6813176274299622, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将西红柿洗净，切块。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第2步
步骤: 步骤2
描述: 葱姜蒜切碎。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 鸡蛋打到碗中，用筷子（或打蛋器）搅拌均匀。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 热锅，并放入15毫升的油，待能从油中看到冒出一丝烟时，放入葱姜蒜翻炒30秒。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第5步
步骤: 步骤5
描述: 放入西红柿翻炒1分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 倒入水，水的高度大约为锅内菜品高度的1.2倍，并放入盐。
方法: 煮
工具: 炒锅
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 待开锅后，将鸡蛋液放入，并用筷子将鸡蛋打散，放入味素和香油。
方法: 煮,搅拌
工具: 筷子
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 等待30秒，关火出锅。
方法: 煮
工具: 炒锅
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201004478, chunk_id=201004478_chunk_894, recipe_name=扬州炒饭, category=主食, score=0.655517041683197, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 胡萝卜切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 午餐肉切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 葱分别取葱白和葱绿，各切成 0.25-0.5cm 的小段，分开备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 在碗中打入鸡蛋液，均匀搅拌，备用
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 将胡萝卜、青豆、玉米粒煮熟捞出，备用（水别倒）
方法: 煮
工具: 锅,漏勺
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将虾煮熟，捞出备用（水可以倒了）
方法: 煮
工具: 锅,漏勺
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 热锅热油（第二次倒油 20-30ml），油温后缓慢倒入鸡蛋液，不搅拌
方法: 炒,煎
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 鸡蛋凝固后立刻捞出，备用
方法: 炒
工具: 锅铲
时间: 10秒

### 第9步
步骤: 步骤9
描述: 将午餐肉、青豆、胡萝卜、玉米粒、虾倒入锅中翻炒 1-2 分钟，装盘备用
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第10步
步骤: 步骤10
描述: 水冲一下锅，将杂物冲干净，保证锅内干净（可以有油但无杂质）
方法: 清洗
工具: 水
时间: 30秒

### 第11步
步骤: 步骤11
描述: 热锅热油（10ml），将葱白放入爆香
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第12步
步骤: 步骤12
描述: 调至小火，放入米饭，用铲子快速砸击米饭并翻炒，使米饭粒粒分明
方法: 炒
工具: 锅铲
时间: 2分钟

### 第13步
步骤: 步骤13
描述: 倒入鸡蛋，继续砸击，使鸡蛋碎开并与米饭充分混合
方法: 炒
工具: 锅铲
时间: 1分钟

### 第14步
步骤: 步骤14
描述: 转大火，倒入所有备用配料，快速翻炒 1-2 分钟
方法: 炒
工具: 锅铲
时间: 1-2分钟

### 第15步
步骤: 步骤15
描述: 撒入盐，并翻炒至充分混合
方法: 炒
工具: 锅铲
时间: 30秒

### 第16步
步骤: 步骤16
描述: 撒入葱绿，翻炒 1 分钟
方法: 炒
工具: 锅铲
时间: 1分钟

### 第17步
步骤: 步骤17
描述: 关火，装盘
方法: 装盘
工具: 锅铲,盘子
时间: 10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=201004808, recipe_name=西葫芦, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西葫芦
食材名称: 西葫芦
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1124, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.7426695227622986, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，切成小块，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 西葫芦洗净，切成边长约为4cm的菱形，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 打三个鸡蛋到碗里，打散搅匀，备用
方法: 打散
工具: 碗,筷子

### 第4步
步骤: 步骤4
描述: 热锅，锅内放入5-10ml食用油
方法: 热锅
工具: 炒锅

### 第5步
步骤: 步骤5
描述: 倒入鸡蛋，保持翻炒至鸡蛋成固体，用锅铲分成小块后盛到碗里，备用
方法: 炒
工具: 炒锅,锅铲,碗

### 第6步
步骤: 步骤6
描述: 锅内放入5-10ml食用油，倒入西红柿，炒至变软
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 倒入西葫芦一起翻炒均匀，放入6g食用盐，将火调小然后等待4-5分钟
方法: 炒,焖
工具: 炒锅,锅铲
时间: 4-5分钟

### 第8步
步骤: 步骤8
描述: 倒入备用的鸡蛋，中火翻炒15秒
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 盛盘
工具: 锅铲
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=1
source: generation_context
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6921697854995728, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: generation_context
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_754, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6813176274299622, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将西红柿洗净，切块。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第2步
步骤: 步骤2
描述: 葱姜蒜切碎。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 鸡蛋打到碗中，用筷子（或打蛋器）搅拌均匀。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 热锅，并放入15毫升的油，待能从油中看到冒出一丝烟时，放入葱姜蒜翻炒30秒。
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第5步
步骤: 步骤5
描述: 放入西红柿翻炒1分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 倒入水，水的高度大约为锅内菜品高度的1.2倍，并放入盐。
方法: 煮
工具: 炒锅
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 待开锅后，将鸡蛋液放入，并用筷子将鸡蛋打散，放入味素和香油。
方法: 煮,搅拌
工具: 筷子
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 等待30秒，关火出锅。
方法: 煮
工具: 炒锅
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=3
source: generation_context
metadata_summary: node_id=201004478, chunk_id=201004478_chunk_894, recipe_name=扬州炒饭, category=主食, score=0.655517041683197, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 胡萝卜切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 午餐肉切丁 0.2cm×0.2cm×0.2cm，备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 葱分别取葱白和葱绿，各切成 0.25-0.5cm 的小段，分开备用
方法: 切
工具: 刀,案板
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 在碗中打入鸡蛋液，均匀搅拌，备用
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 将胡萝卜、青豆、玉米粒煮熟捞出，备用（水别倒）
方法: 煮
工具: 锅,漏勺
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将虾煮熟，捞出备用（水可以倒了）
方法: 煮
工具: 锅,漏勺
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 热锅热油（第二次倒油 20-30ml），油温后缓慢倒入鸡蛋液，不搅拌
方法: 炒,煎
工具: 炒锅,锅铲
时间: 30秒

### 第8步
步骤: 步骤8
描述: 鸡蛋凝固后立刻捞出，备用
方法: 炒
工具: 锅铲
时间: 10秒

### 第9步
步骤: 步骤9
描述: 将午餐肉、青豆、胡萝卜、玉米粒、虾倒入锅中翻炒 1-2 分钟，装盘备用
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第10步
步骤: 步骤10
描述: 水冲一下锅，将杂物冲干净，保证锅内干净（可以有油但无杂质）
方法: 清洗
工具: 水
时间: 30秒

### 第11步
步骤: 步骤11
描述: 热锅热油（10ml），将葱白放入爆香
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第12步
步骤: 步骤12
描述: 调至小火，放入米饭，用铲子快速砸击米饭并翻炒，使米饭粒粒分明
方法: 炒
工具: 锅铲
时间: 2分钟

### 第13步
步骤: 步骤13
描述: 倒入鸡蛋，继续砸击，使鸡蛋碎开并与米饭充分混合
方法: 炒
工具: 锅铲
时间: 1分钟

### 第14步
步骤: 步骤14
描述: 转大火，倒入所有备用配料，快速翻炒 1-2 分钟
方法: 炒
工具: 锅铲
时间: 1-2分钟

### 第15步
步骤: 步骤15
描述: 撒入盐，并翻炒至充分混合
方法: 炒
工具: 锅铲
时间: 30秒

### 第16步
步骤: 步骤16
描述: 撒入葱绿，翻炒 1 分钟
方法: 炒
工具: 锅铲
时间: 1分钟

### 第17步
步骤: 步骤17
描述: 关火，装盘
方法: 装盘
工具: 锅铲,盘子
时间: 10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=4
source: generation_context
metadata_summary: node_id=201004808, recipe_name=西葫芦, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

```text
命中关键词: 西葫芦
食材名称: 西葫芦
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

