# Recall Content

audit_id: 20260811_164535_674_65fa913f
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201000319, recipe_name=芥末黄油罗氏虾, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 芥末黄油罗氏虾
菜品名称: 芥末黄油罗氏虾
分类: 水产
难度: 3.0
关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
```

### result_order=1
source: entity_level
metadata_summary: node_id=201000320, recipe_name=罗氏虾, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 罗氏虾
食材名称: 罗氏虾
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=2
source: entity_level
metadata_summary: node_id=201000322, recipe_name=芥末, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 芥末
食材名称: 芥末
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### result_order=3
source: entity_level
metadata_summary: node_id=201000321, recipe_name=黄油, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 黄油
食材名称: 黄油
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=200000000, recipe_name=菜谱, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 菜谱
菜品名称: 菜谱
分类: 未知
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
```

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_56, recipe_name=芥末黄油罗氏虾, category=水产, score=0.8190106749534607, search_type=vector_enhanced

```text
# 芥末黄油罗氏虾
难度: 3.0星

时间信息: 准备时间: 约10分钟, 烹饪时间: 约15分钟
份量: 1盘

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_58, recipe_name=芥末黄油罗氏虾, category=水产, score=0.7429306507110596, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将罗氏虾剪掉头尾尖刺、触须和脚，剪刀把虾身开背，去除虾线。
方法: 切
工具: 剪刀
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 提前搅拌好芥末酱汁：酱油、蚝油、芥末、盐、糖，搅拌均匀！
方法: 搅拌
工具: 碗,筷子
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 洗好香菜，切段备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 罗氏虾沥掉水，锅中加入油，直接放入罗氏虾，中火，外表煎至金黄，捞出。
方法: 煎
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第5步
步骤: 步骤5
描述: 下入蒜蓉，大火，利用煎虾剩下的油继续煎炒蒜蓉，等到锅中白雾冒出，蒜蓉已经煎出香味，下虾和黄油，让虾充分吸收黄油香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第6步
步骤: 步骤6
描述: 下入调好的酱汁，继续大火煮沸，翻炒虾，至酱汁收汁，加入酒（料酒、啤酒可以放30g，朗姆酒味道浓郁放15g即可）。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第7步
步骤: 步骤7
描述: 在等酱汁稍微收汁，加入香菜翻炒两下，即可出锅。
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_607, recipe_name=芥末罗氏虾, category=荤菜, score=0.7369852066040039, search_type=vector_enhanced

```text
# 芥末罗氏虾
难度: 3.0星

时间信息: 准备时间: 约10分钟, 烹饪时间: 约10分钟
份量: 2人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_609, recipe_name=芥末罗氏虾, category=荤菜, score=0.7222800254821777, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201000496, chunk_id=201000496_chunk_89, recipe_name=黄油煎虾, category=水产, score=0.6865054368972778, search_type=vector_enhanced

```text
# 黄油煎虾
难度: 3.0星

时间信息: 准备时间: 约20分钟（处理活虾、开背、调汁）, 烹饪时间: 约5分钟（热锅、煎炒、收汁）
份量: 1

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 米酒 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_69, recipe_name=蒜香黄油虾, category=水产, score=0.6707053184509277, search_type=vector_enhanced

```text
# 蒜香黄油虾
难度: 2.0星

时间信息: 准备时间: 约5分钟, 烹饪时间: 约4-5分钟
份量: 1-2人

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_71, recipe_name=蒜香黄油虾, category=水产, score=0.6706508994102478, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201000184, chunk_id=201000184_chunk_34, recipe_name=干煎阿根廷红虾, category=水产, score=0.663160502910614, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 阿根廷红虾提前1天从速冻取出放到冷藏里自然解冻，可买已开背去虾线的成品
方法: 解冻
工具: 冰箱
时间: 24小时

### 第2步
步骤: 步骤2
描述: 解冻好的红虾洗净擦干，用厨房用纸吸干水分
方法: 清洗,擦干
工具: 厨房用纸
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 生姜切片，洋葱切小方块，香菜洗净叶茎分离，香菜叶切碎，大蒜压碎切末
方法: 切,压碎
工具: 刀,案板,压蒜器
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 大火热锅，倒入橄榄油，油温升高后放入生姜片、洋葱块和香菜茎煸炒
方法: 热锅,煸炒
工具: 平底锅,锅铲
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 约1分钟后取出姜、洋葱和香菜茎，弃用
方法: 取出
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 调中大火，放入红虾单面煎2分钟，同时给每只虾刷一层油
方法: 煎
工具: 平底锅,刷子
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 待底面虾壳微焦黄时翻面，撒入大蒜碎末，轻晃锅使受热均匀
方法: 翻面,撒料,晃动
工具: 锅铲,平底锅
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 加入20ml白葡萄酒继续煎1分钟
方法: 煎
工具: 平底锅
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 调中小火，均匀撒盐和黑胡椒，每只虾滴一滴生抽
方法: 调味
工具: 手
时间: 30秒

### 第10步
步骤: 步骤10
描述: 撒上香菜叶装盘，切好柠檬片摆盘边即可
方法: 装盘
工具: 刀
时间: 30秒

关联图谱:
- OUT REQUIRES 橄榄油 (Ingredient): category: 调料
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201000496, chunk_id=201000496_chunk_91, recipe_name=黄油煎虾, category=水产, score=0.662589967250824, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜虾摘除头部，顺带扯出虾线（这步处理不好可在下一步开背时取出虾线），使用剪刀剪开或菜刀片开虾背，沥干水分备用
方法: 切
工具: 剪刀,菜刀,案板

### 第2步
步骤: 步骤2
描述: 调制酱汁：小碗放入上述量的全部生抽、米酒、白糖、盐搅匀备用
方法: 搅拌
工具: 小碗,筷子

### 第3步
步骤: 步骤3
描述: 中大火热锅，热锅内放入食用油，等待10秒让油温升高
方法: 炒
工具: 炒锅
时间: 10秒

### 第4步
步骤: 步骤4
描述: 虾全部放入锅中，开始瓶磨黑胡椒，均匀地撒在虾上翻炒
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 虾变色后加入黄油，黄油完全融化后倒入调制酱汁，继续翻炒
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 大火翻炒15秒收汁即可装盘
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 米酒 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_57, recipe_name=芥末黄油罗氏虾, category=水产, score=0.6472615599632263, search_type=vector_enhanced

```text
## 所需食材
1. 料酒、朗姆酒或啤酒(15克)
2. 生抽(30克)
3. 白糖(3克)
4. 盐(3克)
5. 罗氏虾(500克)
6. 芥末(15克)
7. 蒜(5颗)
8. 蚝油(30克)
9. 香菜(5条)
10. 黄油(20克)

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201000319, recipe_name=芥末黄油罗氏虾, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 芥末黄油罗氏虾
菜品名称: 芥末黄油罗氏虾
分类: 水产
难度: 3.0
关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201000320, recipe_name=罗氏虾, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 罗氏虾
食材名称: 罗氏虾
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201000322, recipe_name=芥末, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 芥末
食材名称: 芥末
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201000321, recipe_name=黄油, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 黄油
食材名称: 黄油
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=200000000, recipe_name=菜谱, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 菜谱
菜品名称: 菜谱
分类: 未知
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_56, recipe_name=芥末黄油罗氏虾, category=水产, score=0.8190106749534607, search_type=vector_enhanced

```text
# 芥末黄油罗氏虾
难度: 3.0星

时间信息: 准备时间: 约10分钟, 烹饪时间: 约15分钟
份量: 1盘

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_58, recipe_name=芥末黄油罗氏虾, category=水产, score=0.7429306507110596, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将罗氏虾剪掉头尾尖刺、触须和脚，剪刀把虾身开背，去除虾线。
方法: 切
工具: 剪刀
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 提前搅拌好芥末酱汁：酱油、蚝油、芥末、盐、糖，搅拌均匀！
方法: 搅拌
工具: 碗,筷子
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 洗好香菜，切段备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 罗氏虾沥掉水，锅中加入油，直接放入罗氏虾，中火，外表煎至金黄，捞出。
方法: 煎
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第5步
步骤: 步骤5
描述: 下入蒜蓉，大火，利用煎虾剩下的油继续煎炒蒜蓉，等到锅中白雾冒出，蒜蓉已经煎出香味，下虾和黄油，让虾充分吸收黄油香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第6步
步骤: 步骤6
描述: 下入调好的酱汁，继续大火煮沸，翻炒虾，至酱汁收汁，加入酒（料酒、啤酒可以放30g，朗姆酒味道浓郁放15g即可）。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第7步
步骤: 步骤7
描述: 在等酱汁稍微收汁，加入香菜翻炒两下，即可出锅。
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_607, recipe_name=芥末罗氏虾, category=荤菜, score=0.7369852066040039, search_type=vector_enhanced

```text
# 芥末罗氏虾
难度: 3.0星

时间信息: 准备时间: 约10分钟, 烹饪时间: 约10分钟
份量: 2人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_609, recipe_name=芥末罗氏虾, category=荤菜, score=0.7222800254821777, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201000496, chunk_id=201000496_chunk_89, recipe_name=黄油煎虾, category=水产, score=0.6865054368972778, search_type=vector_enhanced

```text
# 黄油煎虾
难度: 3.0星

时间信息: 准备时间: 约20分钟（处理活虾、开背、调汁）, 烹饪时间: 约5分钟（热锅、煎炒、收汁）
份量: 1

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 米酒 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_69, recipe_name=蒜香黄油虾, category=水产, score=0.6707053184509277, search_type=vector_enhanced

```text
# 蒜香黄油虾
难度: 2.0星

时间信息: 准备时间: 约5分钟, 烹饪时间: 约4-5分钟
份量: 1-2人

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_71, recipe_name=蒜香黄油虾, category=水产, score=0.6706508994102478, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201000184, chunk_id=201000184_chunk_34, recipe_name=干煎阿根廷红虾, category=水产, score=0.663160502910614, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 阿根廷红虾提前1天从速冻取出放到冷藏里自然解冻，可买已开背去虾线的成品
方法: 解冻
工具: 冰箱
时间: 24小时

### 第2步
步骤: 步骤2
描述: 解冻好的红虾洗净擦干，用厨房用纸吸干水分
方法: 清洗,擦干
工具: 厨房用纸
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 生姜切片，洋葱切小方块，香菜洗净叶茎分离，香菜叶切碎，大蒜压碎切末
方法: 切,压碎
工具: 刀,案板,压蒜器
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 大火热锅，倒入橄榄油，油温升高后放入生姜片、洋葱块和香菜茎煸炒
方法: 热锅,煸炒
工具: 平底锅,锅铲
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 约1分钟后取出姜、洋葱和香菜茎，弃用
方法: 取出
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 调中大火，放入红虾单面煎2分钟，同时给每只虾刷一层油
方法: 煎
工具: 平底锅,刷子
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 待底面虾壳微焦黄时翻面，撒入大蒜碎末，轻晃锅使受热均匀
方法: 翻面,撒料,晃动
工具: 锅铲,平底锅
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 加入20ml白葡萄酒继续煎1分钟
方法: 煎
工具: 平底锅
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 调中小火，均匀撒盐和黑胡椒，每只虾滴一滴生抽
方法: 调味
工具: 手
时间: 30秒

### 第10步
步骤: 步骤10
描述: 撒上香菜叶装盘，切好柠檬片摆盘边即可
方法: 装盘
工具: 刀
时间: 30秒

关联图谱:
- OUT REQUIRES 橄榄油 (Ingredient): category: 调料
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201000496, chunk_id=201000496_chunk_91, recipe_name=黄油煎虾, category=水产, score=0.662589967250824, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜虾摘除头部，顺带扯出虾线（这步处理不好可在下一步开背时取出虾线），使用剪刀剪开或菜刀片开虾背，沥干水分备用
方法: 切
工具: 剪刀,菜刀,案板

### 第2步
步骤: 步骤2
描述: 调制酱汁：小碗放入上述量的全部生抽、米酒、白糖、盐搅匀备用
方法: 搅拌
工具: 小碗,筷子

### 第3步
步骤: 步骤3
描述: 中大火热锅，热锅内放入食用油，等待10秒让油温升高
方法: 炒
工具: 炒锅
时间: 10秒

### 第4步
步骤: 步骤4
描述: 虾全部放入锅中，开始瓶磨黑胡椒，均匀地撒在虾上翻炒
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 虾变色后加入黄油，黄油完全融化后倒入调制酱汁，继续翻炒
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 大火翻炒15秒收汁即可装盘
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 米酒 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_57, recipe_name=芥末黄油罗氏虾, category=水产, score=0.6472615599632263, search_type=vector_enhanced

```text
## 所需食材
1. 料酒、朗姆酒或啤酒(15克)
2. 生抽(30克)
3. 白糖(3克)
4. 盐(3克)
5. 罗氏虾(500克)
6. 芥末(15克)
7. 蒜(5颗)
8. 蚝油(30克)
9. 香菜(5条)
10. 黄油(20克)

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_58, recipe_name=芥末黄油罗氏虾, category=水产, score=0.7429306507110596, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将罗氏虾剪掉头尾尖刺、触须和脚，剪刀把虾身开背，去除虾线。
方法: 切
工具: 剪刀
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 提前搅拌好芥末酱汁：酱油、蚝油、芥末、盐、糖，搅拌均匀！
方法: 搅拌
工具: 碗,筷子
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 洗好香菜，切段备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 罗氏虾沥掉水，锅中加入油，直接放入罗氏虾，中火，外表煎至金黄，捞出。
方法: 煎
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第5步
步骤: 步骤5
描述: 下入蒜蓉，大火，利用煎虾剩下的油继续煎炒蒜蓉，等到锅中白雾冒出，蒜蓉已经煎出香味，下虾和黄油，让虾充分吸收黄油香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第6步
步骤: 步骤6
描述: 下入调好的酱汁，继续大火煮沸，翻炒虾，至酱汁收汁，加入酒（料酒、啤酒可以放30g，朗姆酒味道浓郁放15g即可）。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第7步
步骤: 步骤7
描述: 在等酱汁稍微收汁，加入香菜翻炒两下，即可出锅。
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201000320, recipe_name=罗氏虾, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 罗氏虾
食材名称: 罗氏虾
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201000322, recipe_name=芥末, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 芥末
食材名称: 芥末
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201000321, recipe_name=黄油, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 黄油
食材名称: 黄油
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=200000000, recipe_name=菜谱, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 菜谱
菜品名称: 菜谱
分类: 未知
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_609, recipe_name=芥末罗氏虾, category=荤菜, score=0.7222800254821777, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=201000496, chunk_id=201000496_chunk_91, recipe_name=黄油煎虾, category=水产, score=0.662589967250824, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜虾摘除头部，顺带扯出虾线（这步处理不好可在下一步开背时取出虾线），使用剪刀剪开或菜刀片开虾背，沥干水分备用
方法: 切
工具: 剪刀,菜刀,案板

### 第2步
步骤: 步骤2
描述: 调制酱汁：小碗放入上述量的全部生抽、米酒、白糖、盐搅匀备用
方法: 搅拌
工具: 小碗,筷子

### 第3步
步骤: 步骤3
描述: 中大火热锅，热锅内放入食用油，等待10秒让油温升高
方法: 炒
工具: 炒锅
时间: 10秒

### 第4步
步骤: 步骤4
描述: 虾全部放入锅中，开始瓶磨黑胡椒，均匀地撒在虾上翻炒
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 虾变色后加入黄油，黄油完全融化后倒入调制酱汁，继续翻炒
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 大火翻炒15秒收汁即可装盘
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 米酒 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_71, recipe_name=蒜香黄油虾, category=水产, score=0.6706508994102478, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201000184, chunk_id=201000184_chunk_34, recipe_name=干煎阿根廷红虾, category=水产, score=0.663160502910614, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 阿根廷红虾提前1天从速冻取出放到冷藏里自然解冻，可买已开背去虾线的成品
方法: 解冻
工具: 冰箱
时间: 24小时

### 第2步
步骤: 步骤2
描述: 解冻好的红虾洗净擦干，用厨房用纸吸干水分
方法: 清洗,擦干
工具: 厨房用纸
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 生姜切片，洋葱切小方块，香菜洗净叶茎分离，香菜叶切碎，大蒜压碎切末
方法: 切,压碎
工具: 刀,案板,压蒜器
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 大火热锅，倒入橄榄油，油温升高后放入生姜片、洋葱块和香菜茎煸炒
方法: 热锅,煸炒
工具: 平底锅,锅铲
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 约1分钟后取出姜、洋葱和香菜茎，弃用
方法: 取出
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 调中大火，放入红虾单面煎2分钟，同时给每只虾刷一层油
方法: 煎
工具: 平底锅,刷子
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 待底面虾壳微焦黄时翻面，撒入大蒜碎末，轻晃锅使受热均匀
方法: 翻面,撒料,晃动
工具: 锅铲,平底锅
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 加入20ml白葡萄酒继续煎1分钟
方法: 煎
工具: 平底锅
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 调中小火，均匀撒盐和黑胡椒，每只虾滴一滴生抽
方法: 调味
工具: 手
时间: 30秒

### 第10步
步骤: 步骤10
描述: 撒上香菜叶装盘，切好柠檬片摆盘边即可
方法: 装盘
工具: 刀
时间: 30秒

关联图谱:
- OUT REQUIRES 橄榄油 (Ingredient): category: 调料
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
菜品: 芥末黄油罗氏虾
分类: 水产
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将罗氏虾剪掉头尾尖刺、触须和脚，剪刀把虾身开背，去除虾线。
方法: 切
工具: 剪刀
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 提前搅拌好芥末酱汁：酱油、蚝油、芥末、盐、糖，搅拌均匀！
方法: 搅拌
工具: 碗,筷子
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 洗好香菜，切段备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 罗氏虾沥掉水，锅中加入油，直接放入罗氏虾，中火，外表煎至金黄，捞出。
方法: 煎
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第5步
步骤: 步骤5
描述: 下入蒜蓉，大火，利用煎虾剩下的油继续煎炒蒜蓉，等到锅中白雾冒出，蒜蓉已经煎出香味，下虾和黄油，让虾充分吸收黄油香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第6步
步骤: 步骤6
描述: 下入调好的酱汁，继续大火煮沸，翻炒虾，至酱汁收汁，加入酒（料酒、啤酒可以放30g，朗姆酒味道浓郁放15g即可）。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第7步
步骤: 步骤7
描述: 在等酱汁稍微收汁，加入香菜翻炒两下，即可出锅。
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### pair_order=1
source: rerank_input

```text
命中关键词: 罗氏虾
食材名称: 罗氏虾
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 芥末
食材名称: 芥末
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### pair_order=3
source: rerank_input

```text
命中关键词: 黄油
食材名称: 黄油
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

### pair_order=4
source: rerank_input

```text
命中关键词: 菜谱
菜品名称: 菜谱
分类: 未知
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
```

### pair_order=5
source: rerank_input

```text
菜品: 芥末罗氏虾
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=6
source: rerank_input

```text
菜品: 黄油煎虾
分类: 水产
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜虾摘除头部，顺带扯出虾线（这步处理不好可在下一步开背时取出虾线），使用剪刀剪开或菜刀片开虾背，沥干水分备用
方法: 切
工具: 剪刀,菜刀,案板

### 第2步
步骤: 步骤2
描述: 调制酱汁：小碗放入上述量的全部生抽、米酒、白糖、盐搅匀备用
方法: 搅拌
工具: 小碗,筷子

### 第3步
步骤: 步骤3
描述: 中大火热锅，热锅内放入食用油，等待10秒让油温升高
方法: 炒
工具: 炒锅
时间: 10秒

### 第4步
步骤: 步骤4
描述: 虾全部放入锅中，开始瓶磨黑胡椒，均匀地撒在虾上翻炒
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 虾变色后加入黄油，黄油完全融化后倒入调制酱汁，继续翻炒
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 大火翻炒15秒收汁即可装盘
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 米酒 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### pair_order=7
source: rerank_input

```text
菜品: 蒜香黄油虾
分类: 水产
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### pair_order=8
source: rerank_input

```text
菜品: 干煎阿根廷红虾
分类: 水产
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 阿根廷红虾提前1天从速冻取出放到冷藏里自然解冻，可买已开背去虾线的成品
方法: 解冻
工具: 冰箱
时间: 24小时

### 第2步
步骤: 步骤2
描述: 解冻好的红虾洗净擦干，用厨房用纸吸干水分
方法: 清洗,擦干
工具: 厨房用纸
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 生姜切片，洋葱切小方块，香菜洗净叶茎分离，香菜叶切碎，大蒜压碎切末
方法: 切,压碎
工具: 刀,案板,压蒜器
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 大火热锅，倒入橄榄油，油温升高后放入生姜片、洋葱块和香菜茎煸炒
方法: 热锅,煸炒
工具: 平底锅,锅铲
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 约1分钟后取出姜、洋葱和香菜茎，弃用
方法: 取出
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 调中大火，放入红虾单面煎2分钟，同时给每只虾刷一层油
方法: 煎
工具: 平底锅,刷子
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 待底面虾壳微焦黄时翻面，撒入大蒜碎末，轻晃锅使受热均匀
方法: 翻面,撒料,晃动
工具: 锅铲,平底锅
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 加入20ml白葡萄酒继续煎1分钟
方法: 煎
工具: 平底锅
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 调中小火，均匀撒盐和黑胡椒，每只虾滴一滴生抽
方法: 调味
工具: 手
时间: 30秒

### 第10步
步骤: 步骤10
描述: 撒上香菜叶装盘，切好柠檬片摆盘边即可
方法: 装盘
工具: 刀
时间: 30秒

关联图谱:
- OUT REQUIRES 橄榄油 (Ingredient): category: 调料
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_58, recipe_name=芥末黄油罗氏虾, category=水产, score=0.7429306507110596, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将罗氏虾剪掉头尾尖刺、触须和脚，剪刀把虾身开背，去除虾线。
方法: 切
工具: 剪刀
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 提前搅拌好芥末酱汁：酱油、蚝油、芥末、盐、糖，搅拌均匀！
方法: 搅拌
工具: 碗,筷子
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 洗好香菜，切段备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 罗氏虾沥掉水，锅中加入油，直接放入罗氏虾，中火，外表煎至金黄，捞出。
方法: 煎
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第5步
步骤: 步骤5
描述: 下入蒜蓉，大火，利用煎虾剩下的油继续煎炒蒜蓉，等到锅中白雾冒出，蒜蓉已经煎出香味，下虾和黄油，让虾充分吸收黄油香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第6步
步骤: 步骤6
描述: 下入调好的酱汁，继续大火煮沸，翻炒虾，至酱汁收汁，加入酒（料酒、啤酒可以放30g，朗姆酒味道浓郁放15g即可）。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第7步
步骤: 步骤7
描述: 在等酱汁稍微收汁，加入香菜翻炒两下，即可出锅。
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_609, recipe_name=芥末罗氏虾, category=荤菜, score=0.7222800254821777, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_71, recipe_name=蒜香黄油虾, category=水产, score=0.6706508994102478, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201000496, chunk_id=201000496_chunk_91, recipe_name=黄油煎虾, category=水产, score=0.662589967250824, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜虾摘除头部，顺带扯出虾线（这步处理不好可在下一步开背时取出虾线），使用剪刀剪开或菜刀片开虾背，沥干水分备用
方法: 切
工具: 剪刀,菜刀,案板

### 第2步
步骤: 步骤2
描述: 调制酱汁：小碗放入上述量的全部生抽、米酒、白糖、盐搅匀备用
方法: 搅拌
工具: 小碗,筷子

### 第3步
步骤: 步骤3
描述: 中大火热锅，热锅内放入食用油，等待10秒让油温升高
方法: 炒
工具: 炒锅
时间: 10秒

### 第4步
步骤: 步骤4
描述: 虾全部放入锅中，开始瓶磨黑胡椒，均匀地撒在虾上翻炒
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 虾变色后加入黄油，黄油完全融化后倒入调制酱汁，继续翻炒
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 大火翻炒15秒收汁即可装盘
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 米酒 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201000184, chunk_id=201000184_chunk_34, recipe_name=干煎阿根廷红虾, category=水产, score=0.663160502910614, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 阿根廷红虾提前1天从速冻取出放到冷藏里自然解冻，可买已开背去虾线的成品
方法: 解冻
工具: 冰箱
时间: 24小时

### 第2步
步骤: 步骤2
描述: 解冻好的红虾洗净擦干，用厨房用纸吸干水分
方法: 清洗,擦干
工具: 厨房用纸
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 生姜切片，洋葱切小方块，香菜洗净叶茎分离，香菜叶切碎，大蒜压碎切末
方法: 切,压碎
工具: 刀,案板,压蒜器
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 大火热锅，倒入橄榄油，油温升高后放入生姜片、洋葱块和香菜茎煸炒
方法: 热锅,煸炒
工具: 平底锅,锅铲
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 约1分钟后取出姜、洋葱和香菜茎，弃用
方法: 取出
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 调中大火，放入红虾单面煎2分钟，同时给每只虾刷一层油
方法: 煎
工具: 平底锅,刷子
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 待底面虾壳微焦黄时翻面，撒入大蒜碎末，轻晃锅使受热均匀
方法: 翻面,撒料,晃动
工具: 锅铲,平底锅
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 加入20ml白葡萄酒继续煎1分钟
方法: 煎
工具: 平底锅
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 调中小火，均匀撒盐和黑胡椒，每只虾滴一滴生抽
方法: 调味
工具: 手
时间: 30秒

### 第10步
步骤: 步骤10
描述: 撒上香菜叶装盘，切好柠檬片摆盘边即可
方法: 装盘
工具: 刀
时间: 30秒

关联图谱:
- OUT REQUIRES 橄榄油 (Ingredient): category: 调料
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201000320, recipe_name=罗氏虾, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 罗氏虾
食材名称: 罗氏虾
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=6
source: reranked_results
metadata_summary: node_id=200000000, recipe_name=菜谱, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 菜谱
菜品名称: 菜谱
分类: 未知
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201000322, recipe_name=芥末, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 芥末
食材名称: 芥末
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=201000321, recipe_name=黄油, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 黄油
食材名称: 黄油
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_58, recipe_name=芥末黄油罗氏虾, category=水产, score=0.7429306507110596, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将罗氏虾剪掉头尾尖刺、触须和脚，剪刀把虾身开背，去除虾线。
方法: 切
工具: 剪刀
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 提前搅拌好芥末酱汁：酱油、蚝油、芥末、盐、糖，搅拌均匀！
方法: 搅拌
工具: 碗,筷子
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 洗好香菜，切段备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 罗氏虾沥掉水，锅中加入油，直接放入罗氏虾，中火，外表煎至金黄，捞出。
方法: 煎
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第5步
步骤: 步骤5
描述: 下入蒜蓉，大火，利用煎虾剩下的油继续煎炒蒜蓉，等到锅中白雾冒出，蒜蓉已经煎出香味，下虾和黄油，让虾充分吸收黄油香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第6步
步骤: 步骤6
描述: 下入调好的酱汁，继续大火煮沸，翻炒虾，至酱汁收汁，加入酒（料酒、啤酒可以放30g，朗姆酒味道浓郁放15g即可）。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第7步
步骤: 步骤7
描述: 在等酱汁稍微收汁，加入香菜翻炒两下，即可出锅。
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_609, recipe_name=芥末罗氏虾, category=荤菜, score=0.7222800254821777, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_71, recipe_name=蒜香黄油虾, category=水产, score=0.6706508994102478, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201000320, recipe_name=罗氏虾, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 罗氏虾
食材名称: 罗氏虾
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=200000000, recipe_name=菜谱, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 菜谱
菜品名称: 菜谱
分类: 未知
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_58, recipe_name=芥末黄油罗氏虾, category=水产, score=0.7429306507110596, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将罗氏虾剪掉头尾尖刺、触须和脚，剪刀把虾身开背，去除虾线。
方法: 切
工具: 剪刀
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 提前搅拌好芥末酱汁：酱油、蚝油、芥末、盐、糖，搅拌均匀！
方法: 搅拌
工具: 碗,筷子
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 洗好香菜，切段备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 罗氏虾沥掉水，锅中加入油，直接放入罗氏虾，中火，外表煎至金黄，捞出。
方法: 煎
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第5步
步骤: 步骤5
描述: 下入蒜蓉，大火，利用煎虾剩下的油继续煎炒蒜蓉，等到锅中白雾冒出，蒜蓉已经煎出香味，下虾和黄油，让虾充分吸收黄油香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第6步
步骤: 步骤6
描述: 下入调好的酱汁，继续大火煮沸，翻炒虾，至酱汁收汁，加入酒（料酒、啤酒可以放30g，朗姆酒味道浓郁放15g即可）。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第7步
步骤: 步骤7
描述: 在等酱汁稍微收汁，加入香菜翻炒两下，即可出锅。
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=1
source: generation_context
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_609, recipe_name=芥末罗氏虾, category=荤菜, score=0.7222800254821777, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
source: generation_context
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_71, recipe_name=蒜香黄油虾, category=水产, score=0.6706508994102478, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=3
source: generation_context
metadata_summary: node_id=201000320, recipe_name=罗氏虾, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

```text
命中关键词: 罗氏虾
食材名称: 罗氏虾
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=4
source: generation_context
metadata_summary: node_id=200000000, recipe_name=菜谱, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

```text
命中关键词: 菜谱
菜品名称: 菜谱
分类: 未知
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
```

