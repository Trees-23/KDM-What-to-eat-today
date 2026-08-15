# Recall Content

audit_id: 20260811_194055_317_3e1a4e7f
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201004017, recipe_name=手工水饺, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 手工水饺
菜品名称: 手工水饺
分类: 主食
难度: 5.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

## Hybrid Retrieval / Topic Branch Raw Results
_no content_

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201000613, chunk_id=201000613_chunk_115, recipe_name=煎饺, category=早餐, score=0.6547613739967346, search_type=vector_enhanced

```text
## 所需食材
1. 清水(没过饺子高度1/2毫升)
2. 葱花
3. 速冻水饺(10-15个)
4. 食用油(10-15毫升)
5. 黑芝麻

关联图谱:
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 黑芝麻 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201003618, chunk_id=201003618_chunk_705, recipe_name=速冻水饺, category=半成品, score=0.6478274464607239, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 中火，将水倒入锅中，静候水煮沸。
方法: 煮
工具: 锅

### 第2步
步骤: 步骤2
描述: 将饺子倒入锅中。倒入锅前可以适当用水过一下。
方法: 煮
工具: 锅

### 第3步
步骤: 步骤3
描述: 倒入饺子后，用炒菜勺子或铲子搅水，注意不要铲到饺子上，避免粘锅或互相粘连。频率为平均每30秒摇3秒，饺子浮起后停止。
方法: 煮,搅拌
工具: 炒菜勺子,铲子
时间: 30秒摇3秒

### 第4步
步骤: 步骤4
描述: 饺子浮起及水再次煮沸后，盛起一个饺子观察，若面皮夹生则舀入80ml凉水降温，继续煮至沸腾，最多加两次水即可全熟。
方法: 煮,观察
工具: 炒菜勺子

### 第5步
步骤: 步骤5
描述: 所有饺子浮起后（约8分钟），用铲子或漏勺将饺子铲入盘或碗中，装盘后即可食用。
方法: 装盘
工具: 铲子,漏勺,盘或碗
时间: 约8分钟

### 第6步
步骤: 步骤6
描述: 吃完饺子后，等锅内水温降低，将水倒掉并用洗洁精及时刷锅，防止面粉在锅壁形成黏糊物质。
方法: 清洗
工具: 洗洁精,锅

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.6312957406044006, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201004017, chunk_id=201004017_chunk_792, recipe_name=手工水饺, category=主食, score=0.6203062534332275, search_type=vector_enhanced

```text
# 手工水饺
难度: 5.0星

时间信息: 准备时间: 2小时30分钟, 烹饪时间: 30分钟
份量: 1人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201003818, chunk_id=201003818_chunk_751, recipe_name=腊八粥, category=汤类, score=0.6118852496147156, search_type=vector_enhanced

```text
## 标签
加料时需搅拌使食材均匀分布,注意水位线，低于米线立即补水,控制火候，定时搅拌防糊底,普通锅建议水开后再下原料并改小火,有条件可使用高压锅或粥锅
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201004017, chunk_id=201004017_chunk_794, recipe_name=手工水饺, category=主食, score=0.6094350814819336, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 盆中加入所有面粉，加入芝麻香油，面粉中央挖小洞，分4-5次加入水并搅和，出现碎末状稍干面团后停止加水，用手压实面团至面光盆光。
方法: 搅拌,压实
工具: 盆

### 第2步
步骤: 步骤2
描述: 将面团置于桌上，盆倒扣，环境温度25度醒发45分钟。
方法: 醒发
工具: 盆
时间: 45分钟

### 第3步
步骤: 步骤3
描述: 醒发完成后，将面团搓条、合团、再搓条，重复3次后擀条，切成20份均匀面团并搓成直径3-3.5cm球状。
方法: 搓,擀,切
工具: 擀面杖,刀

### 第4步
步骤: 步骤4
描述: 压扁面团，撒面粉防粘，用擀面杖擀成直径约8cm、厚约2mm、中间略厚1mm的饺子皮。
方法: 擀
工具: 擀面杖

### 第5步
步骤: 步骤5
描述: 猪肉去皮切块，用两把菜刀剁成肉末放入碗中；葱姜切末加入肉末搅拌均匀；韭菜洗净切3mm以下长度；韭菜与肉末混合，加入蚝油、生抽、香油各2ml及蛋清，用手搅拌均匀，静置30分钟。
方法: 剁,切,搅拌,腌制
工具: 刀,碗
时间: 30分钟

### 第6步
步骤: 步骤6
描述: 左手托皮，右手夹馅，沿饺子皮圆周合拢捏实，无需捏花，确保不漏即可。
方法: 包
工具: 筷子

### 第7步
步骤: 步骤7
描述: 锅中加水至3/4高度，大火烧开，放入饺子后转中火，水冒泡后加50ml冷水，重复两次；第三次水开后加50ml冷水，再开后小火60秒即可出锅。
方法: 煮
工具: 锅
时间: 约15分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201003618, chunk_id=201003618_chunk_704, recipe_name=速冻水饺, category=半成品, score=0.6042611002922058, search_type=vector_enhanced

```text
## 所需食材
1. 大蒜/蒜泥(3瓣)
2. 姜(50克)
3. 水(14个体积)
4. 速冻水饺(7个)
5. 香油(2滴)
6. 黑醋(10毫升)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=tipdoc_897acc483178, chunk_id=tipdoc_897acc483178_chunk_1250, recipe_name=焯水, category=烹饪技巧, score=0.6018674969673157, search_type=vector_enhanced

```text
## 额外注意事项

- 焯水有时也会使原料内的一些不稳定、可溶性营养物质溢出，特别是新鲜蔬菜中的水溶性维生素更容易受到损失
- 动物类原料与植物类原料要分别焯水；色味较重的与色味较轻的要分别焯水；块状大的要与块状小的分别焯水，以防彼此串味
- 焯制动物性原料后，汤汁可在撇沫澄清后作为鲜汤使用

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 焯水 (TechniqueChunk): category: 烹饪技巧
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1328, recipe_name=凉拌, category=烹饪技巧, score=0.5904332995414734, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 含水量高的食材直接在加入后可能析出过多水分淡化调料
* 搅拌时发现水量不足或搅拌不匀可适量加白开水，若无法确定用量每次 15mL 为佳
* 部分吸水率高的食材不建议搅拌，可能导致腌制后的食材味道过重

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201000613, chunk_id=201000613_chunk_116, recipe_name=煎饺, category=早餐, score=0.5890806317329407, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 取出平底锅（不沾平底锅最佳）
工具: 平底锅

### 第2步
步骤: 步骤2
描述: 加入10-15ml食用油
方法: 倒
工具: 平底锅

### 第3步
步骤: 步骤3
描述: 开火，放入饺子（尽量平均铺开，不宜堆叠）
方法: 放
工具: 平底锅

### 第4步
步骤: 步骤4
描述: 立刻加入清水，水线没过饺子平均高度的1/2
方法: 倒
工具: 平底锅

### 第5步
步骤: 步骤5
描述: 盖上锅盖（此时炉灶应该处于大火）
方法: 焖
工具: 平底锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 当锅中水分仅剩2mm时，转中火开始煎制
方法: 煎
工具: 平底锅

### 第7步
步骤: 步骤7
描述: 当水分全部蒸发后，摇晃平底锅使饺子受热均匀
方法: 煎
工具: 平底锅

### 第8步
步骤: 步骤8
描述: 放入黑芝麻和葱花再焖10秒
方法: 焖
工具: 平底锅,锅盖
时间: 10秒

### 第9步
步骤: 步骤9
描述: 1-2分钟夹出一个饺子观察底部，若出现金黄色脆皮立即取出
方法: 煎
工具: 平底锅,筷子
时间: 1-2分钟

关联图谱:
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 黑芝麻 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201004017, recipe_name=手工水饺, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 手工水饺
菜品名称: 手工水饺
分类: 主食
难度: 5.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201000613, chunk_id=201000613_chunk_115, recipe_name=煎饺, category=早餐, score=0.6547613739967346, search_type=vector_enhanced

```text
## 所需食材
1. 清水(没过饺子高度1/2毫升)
2. 葱花
3. 速冻水饺(10-15个)
4. 食用油(10-15毫升)
5. 黑芝麻

关联图谱:
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 黑芝麻 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201003618, chunk_id=201003618_chunk_705, recipe_name=速冻水饺, category=半成品, score=0.6478274464607239, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 中火，将水倒入锅中，静候水煮沸。
方法: 煮
工具: 锅

### 第2步
步骤: 步骤2
描述: 将饺子倒入锅中。倒入锅前可以适当用水过一下。
方法: 煮
工具: 锅

### 第3步
步骤: 步骤3
描述: 倒入饺子后，用炒菜勺子或铲子搅水，注意不要铲到饺子上，避免粘锅或互相粘连。频率为平均每30秒摇3秒，饺子浮起后停止。
方法: 煮,搅拌
工具: 炒菜勺子,铲子
时间: 30秒摇3秒

### 第4步
步骤: 步骤4
描述: 饺子浮起及水再次煮沸后，盛起一个饺子观察，若面皮夹生则舀入80ml凉水降温，继续煮至沸腾，最多加两次水即可全熟。
方法: 煮,观察
工具: 炒菜勺子

### 第5步
步骤: 步骤5
描述: 所有饺子浮起后（约8分钟），用铲子或漏勺将饺子铲入盘或碗中，装盘后即可食用。
方法: 装盘
工具: 铲子,漏勺,盘或碗
时间: 约8分钟

### 第6步
步骤: 步骤6
描述: 吃完饺子后，等锅内水温降低，将水倒掉并用洗洁精及时刷锅，防止面粉在锅壁形成黏糊物质。
方法: 清洗
工具: 洗洁精,锅

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.6312957406044006, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201004017, chunk_id=201004017_chunk_792, recipe_name=手工水饺, category=主食, score=0.6203062534332275, search_type=vector_enhanced

```text
# 手工水饺
难度: 5.0星

时间信息: 准备时间: 2小时30分钟, 烹饪时间: 30分钟
份量: 1人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201003818, chunk_id=201003818_chunk_751, recipe_name=腊八粥, category=汤类, score=0.6118852496147156, search_type=vector_enhanced

```text
## 标签
加料时需搅拌使食材均匀分布,注意水位线，低于米线立即补水,控制火候，定时搅拌防糊底,普通锅建议水开后再下原料并改小火,有条件可使用高压锅或粥锅
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201004017, chunk_id=201004017_chunk_794, recipe_name=手工水饺, category=主食, score=0.6094350814819336, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 盆中加入所有面粉，加入芝麻香油，面粉中央挖小洞，分4-5次加入水并搅和，出现碎末状稍干面团后停止加水，用手压实面团至面光盆光。
方法: 搅拌,压实
工具: 盆

### 第2步
步骤: 步骤2
描述: 将面团置于桌上，盆倒扣，环境温度25度醒发45分钟。
方法: 醒发
工具: 盆
时间: 45分钟

### 第3步
步骤: 步骤3
描述: 醒发完成后，将面团搓条、合团、再搓条，重复3次后擀条，切成20份均匀面团并搓成直径3-3.5cm球状。
方法: 搓,擀,切
工具: 擀面杖,刀

### 第4步
步骤: 步骤4
描述: 压扁面团，撒面粉防粘，用擀面杖擀成直径约8cm、厚约2mm、中间略厚1mm的饺子皮。
方法: 擀
工具: 擀面杖

### 第5步
步骤: 步骤5
描述: 猪肉去皮切块，用两把菜刀剁成肉末放入碗中；葱姜切末加入肉末搅拌均匀；韭菜洗净切3mm以下长度；韭菜与肉末混合，加入蚝油、生抽、香油各2ml及蛋清，用手搅拌均匀，静置30分钟。
方法: 剁,切,搅拌,腌制
工具: 刀,碗
时间: 30分钟

### 第6步
步骤: 步骤6
描述: 左手托皮，右手夹馅，沿饺子皮圆周合拢捏实，无需捏花，确保不漏即可。
方法: 包
工具: 筷子

### 第7步
步骤: 步骤7
描述: 锅中加水至3/4高度，大火烧开，放入饺子后转中火，水冒泡后加50ml冷水，重复两次；第三次水开后加50ml冷水，再开后小火60秒即可出锅。
方法: 煮
工具: 锅
时间: 约15分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201003618, chunk_id=201003618_chunk_704, recipe_name=速冻水饺, category=半成品, score=0.6042611002922058, search_type=vector_enhanced

```text
## 所需食材
1. 大蒜/蒜泥(3瓣)
2. 姜(50克)
3. 水(14个体积)
4. 速冻水饺(7个)
5. 香油(2滴)
6. 黑醋(10毫升)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=tipdoc_897acc483178, chunk_id=tipdoc_897acc483178_chunk_1250, recipe_name=焯水, category=烹饪技巧, score=0.6018674969673157, search_type=vector_enhanced

```text
## 额外注意事项

- 焯水有时也会使原料内的一些不稳定、可溶性营养物质溢出，特别是新鲜蔬菜中的水溶性维生素更容易受到损失
- 动物类原料与植物类原料要分别焯水；色味较重的与色味较轻的要分别焯水；块状大的要与块状小的分别焯水，以防彼此串味
- 焯制动物性原料后，汤汁可在撇沫澄清后作为鲜汤使用

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 焯水 (TechniqueChunk): category: 烹饪技巧
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1328, recipe_name=凉拌, category=烹饪技巧, score=0.5904332995414734, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 含水量高的食材直接在加入后可能析出过多水分淡化调料
* 搅拌时发现水量不足或搅拌不匀可适量加白开水，若无法确定用量每次 15mL 为佳
* 部分吸水率高的食材不建议搅拌，可能导致腌制后的食材味道过重

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201000613, chunk_id=201000613_chunk_116, recipe_name=煎饺, category=早餐, score=0.5890806317329407, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 取出平底锅（不沾平底锅最佳）
工具: 平底锅

### 第2步
步骤: 步骤2
描述: 加入10-15ml食用油
方法: 倒
工具: 平底锅

### 第3步
步骤: 步骤3
描述: 开火，放入饺子（尽量平均铺开，不宜堆叠）
方法: 放
工具: 平底锅

### 第4步
步骤: 步骤4
描述: 立刻加入清水，水线没过饺子平均高度的1/2
方法: 倒
工具: 平底锅

### 第5步
步骤: 步骤5
描述: 盖上锅盖（此时炉灶应该处于大火）
方法: 焖
工具: 平底锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 当锅中水分仅剩2mm时，转中火开始煎制
方法: 煎
工具: 平底锅

### 第7步
步骤: 步骤7
描述: 当水分全部蒸发后，摇晃平底锅使饺子受热均匀
方法: 煎
工具: 平底锅

### 第8步
步骤: 步骤8
描述: 放入黑芝麻和葱花再焖10秒
方法: 焖
工具: 平底锅,锅盖
时间: 10秒

### 第9步
步骤: 步骤9
描述: 1-2分钟夹出一个饺子观察底部，若出现金黄色脆皮立即取出
方法: 煎
工具: 平底锅,筷子
时间: 1-2分钟

关联图谱:
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 黑芝麻 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201004017, chunk_id=201004017_chunk_794, recipe_name=手工水饺, category=主食, score=0.6094350814819336, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 盆中加入所有面粉，加入芝麻香油，面粉中央挖小洞，分4-5次加入水并搅和，出现碎末状稍干面团后停止加水，用手压实面团至面光盆光。
方法: 搅拌,压实
工具: 盆

### 第2步
步骤: 步骤2
描述: 将面团置于桌上，盆倒扣，环境温度25度醒发45分钟。
方法: 醒发
工具: 盆
时间: 45分钟

### 第3步
步骤: 步骤3
描述: 醒发完成后，将面团搓条、合团、再搓条，重复3次后擀条，切成20份均匀面团并搓成直径3-3.5cm球状。
方法: 搓,擀,切
工具: 擀面杖,刀

### 第4步
步骤: 步骤4
描述: 压扁面团，撒面粉防粘，用擀面杖擀成直径约8cm、厚约2mm、中间略厚1mm的饺子皮。
方法: 擀
工具: 擀面杖

### 第5步
步骤: 步骤5
描述: 猪肉去皮切块，用两把菜刀剁成肉末放入碗中；葱姜切末加入肉末搅拌均匀；韭菜洗净切3mm以下长度；韭菜与肉末混合，加入蚝油、生抽、香油各2ml及蛋清，用手搅拌均匀，静置30分钟。
方法: 剁,切,搅拌,腌制
工具: 刀,碗
时间: 30分钟

### 第6步
步骤: 步骤6
描述: 左手托皮，右手夹馅，沿饺子皮圆周合拢捏实，无需捏花，确保不漏即可。
方法: 包
工具: 筷子

### 第7步
步骤: 步骤7
描述: 锅中加水至3/4高度，大火烧开，放入饺子后转中火，水冒泡后加50ml冷水，重复两次；第三次水开后加50ml冷水，再开后小火60秒即可出锅。
方法: 煮
工具: 锅
时间: 约15分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201000613, chunk_id=201000613_chunk_116, recipe_name=煎饺, category=早餐, score=0.5890806317329407, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 取出平底锅（不沾平底锅最佳）
工具: 平底锅

### 第2步
步骤: 步骤2
描述: 加入10-15ml食用油
方法: 倒
工具: 平底锅

### 第3步
步骤: 步骤3
描述: 开火，放入饺子（尽量平均铺开，不宜堆叠）
方法: 放
工具: 平底锅

### 第4步
步骤: 步骤4
描述: 立刻加入清水，水线没过饺子平均高度的1/2
方法: 倒
工具: 平底锅

### 第5步
步骤: 步骤5
描述: 盖上锅盖（此时炉灶应该处于大火）
方法: 焖
工具: 平底锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 当锅中水分仅剩2mm时，转中火开始煎制
方法: 煎
工具: 平底锅

### 第7步
步骤: 步骤7
描述: 当水分全部蒸发后，摇晃平底锅使饺子受热均匀
方法: 煎
工具: 平底锅

### 第8步
步骤: 步骤8
描述: 放入黑芝麻和葱花再焖10秒
方法: 焖
工具: 平底锅,锅盖
时间: 10秒

### 第9步
步骤: 步骤9
描述: 1-2分钟夹出一个饺子观察底部，若出现金黄色脆皮立即取出
方法: 煎
工具: 平底锅,筷子
时间: 1-2分钟

关联图谱:
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 黑芝麻 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201003618, chunk_id=201003618_chunk_705, recipe_name=速冻水饺, category=半成品, score=0.6478274464607239, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 中火，将水倒入锅中，静候水煮沸。
方法: 煮
工具: 锅

### 第2步
步骤: 步骤2
描述: 将饺子倒入锅中。倒入锅前可以适当用水过一下。
方法: 煮
工具: 锅

### 第3步
步骤: 步骤3
描述: 倒入饺子后，用炒菜勺子或铲子搅水，注意不要铲到饺子上，避免粘锅或互相粘连。频率为平均每30秒摇3秒，饺子浮起后停止。
方法: 煮,搅拌
工具: 炒菜勺子,铲子
时间: 30秒摇3秒

### 第4步
步骤: 步骤4
描述: 饺子浮起及水再次煮沸后，盛起一个饺子观察，若面皮夹生则舀入80ml凉水降温，继续煮至沸腾，最多加两次水即可全熟。
方法: 煮,观察
工具: 炒菜勺子

### 第5步
步骤: 步骤5
描述: 所有饺子浮起后（约8分钟），用铲子或漏勺将饺子铲入盘或碗中，装盘后即可食用。
方法: 装盘
工具: 铲子,漏勺,盘或碗
时间: 约8分钟

### 第6步
步骤: 步骤6
描述: 吃完饺子后，等锅内水温降低，将水倒掉并用洗洁精及时刷锅，防止面粉在锅壁形成黏糊物质。
方法: 清洗
工具: 洗洁精,锅

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1328, recipe_name=凉拌, category=烹饪技巧, score=0.5904332995414734, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 含水量高的食材直接在加入后可能析出过多水分淡化调料
* 搅拌时发现水量不足或搅拌不匀可适量加白开水，若无法确定用量每次 15mL 为佳
* 部分吸水率高的食材不建议搅拌，可能导致腌制后的食材味道过重

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201003818, chunk_id=201003818_chunk_751, recipe_name=腊八粥, category=汤类, score=0.6118852496147156, search_type=vector_enhanced

```text
## 标签
加料时需搅拌使食材均匀分布,注意水位线，低于米线立即补水,控制火候，定时搅拌防糊底,普通锅建议水开后再下原料并改小火,有条件可使用高压锅或粥锅
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=tipdoc_897acc483178, chunk_id=tipdoc_897acc483178_chunk_1250, recipe_name=焯水, category=烹饪技巧, score=0.6018674969673157, search_type=vector_enhanced

```text
## 额外注意事项

- 焯水有时也会使原料内的一些不稳定、可溶性营养物质溢出，特别是新鲜蔬菜中的水溶性维生素更容易受到损失
- 动物类原料与植物类原料要分别焯水；色味较重的与色味较轻的要分别焯水；块状大的要与块状小的分别焯水，以防彼此串味
- 焯制动物性原料后，汤汁可在撇沫澄清后作为鲜汤使用

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 焯水 (TechniqueChunk): category: 烹饪技巧
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7,tipdoc_897acc483178, recipe_name=焯水、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 焯水、凉拌
关键技巧内容:
## 正文
# 焯水

焯水是做饭的一道工序，读作 chāo shuǐ。

焯水指将初步加工的原料放在开水锅中加热至半熟或全熟，取出以备进一步烹调或调味。

焯水是烹调中特别是冷拌菜不可缺少的一道工序。 对菜肴的色、香、味，特别是色起着关键作用。

大部分蔬菜和带有腥羶气味的肉类原料都需要焯水。
## 操作
## 操作
## 开水锅焯水
### 开水锅焯水

开水锅焯水，就是将锅内的水加热，然后将原料下锅。下锅后及时翻动，时间要短，不要过火。

这种方法多用于植物性原料，如：芹菜、菠菜、莴笋等。 焯水时要特别注意火候，时间稍长，颜色就会变淡，而且也不脆、嫩。 因此放入锅内后，水微开时即可捞出晾凉。

- 叶类蔬菜原料应先焯水再切片，以免营养成分损失过多。
- 焯水时应水宽火旺，以使投入原料后能及时开锅；焯制绿叶蔬菜时，应略滚即捞出。
- 蔬菜类原料在焯水后应立即投凉控干，以免因余热而使之变黄、熟烂的现象发生。
- 蔬菜焯水可以放入适量色拉油如花生油、玉米油、大豆油以保持翠绿。
## 冷水锅焯水
### 冷水锅焯水

冷水锅焯水是将原料与冷水同时下锅。 水要没过原料，然后烧开，目的是使原料成熟，便于进一步加工。

土豆、胡萝卜等因体积大，不易成熟，需要煮的时间长一些。

有些动物性原料，如：白肉、牛百页、牛肚领等，也是冷水下锅加热成熟后再进一步加工的。有些用于煮汤的动物性原料也要冷水下锅，在加热过程中使营养物质逐渐溢出，使汤味鲜美，如用热水锅，则会造成蛋白质凝固。

- 锅内的加水量不宜过多，以淹没原料为度。
- 在逐渐加热过程中，必须对原料勤翻动，以使原料受热均匀，达到焯水的目的。
## 额外注意事项
## 额外注意事项

- 焯水有时也会使原料内的一些不稳定、可溶性营养物质溢出，特别是新鲜蔬菜中的水溶性维生素更容易受到损失
- 动物类原料与植物类原料要分别焯水；色味较重的与色味较轻的要分别焯水；块状大的要与块状小的分别焯水，以防彼此串味
- 焯制动物性原料后，汤汁可在撇沫澄清后作为鲜汤使用
## 肉的焯水
### 肉的焯水

- 肉类原料经过开水焯过后变色即可，捞出沥干水分后可以进行下一步的烹调。
- 肉类焯水后需要洗去沾附的血沫污渍，记得用温水清洗，否则肉热胀冷缩会吸附污渍，导致无法洗净血沫。
## 青菜的焯水
### 青菜的焯水

- 洗青菜时，在清水里撒一些盐，这样可以把青菜里的虫子清洗出来
- 焯过后的青菜应立即浸入冷水中，以保持颜色和口感。如果不用冷水浸，青菜会因为开水的余温变的不再清脆，而出现烂烂的感觉
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
菜品: 手工水饺
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 盆中加入所有面粉，加入芝麻香油，面粉中央挖小洞，分4-5次加入水并搅和，出现碎末状稍干面团后停止加水，用手压实面团至面光盆光。
方法: 搅拌,压实
工具: 盆

### 第2步
步骤: 步骤2
描述: 将面团置于桌上，盆倒扣，环境温度25度醒发45分钟。
方法: 醒发
工具: 盆
时间: 45分钟

### 第3步
步骤: 步骤3
描述: 醒发完成后，将面团搓条、合团、再搓条，重复3次后擀条，切成20份均匀面团并搓成直径3-3.5cm球状。
方法: 搓,擀,切
工具: 擀面杖,刀

### 第4步
步骤: 步骤4
描述: 压扁面团，撒面粉防粘，用擀面杖擀成直径约8cm、厚约2mm、中间略厚1mm的饺子皮。
方法: 擀
工具: 擀面杖

### 第5步
步骤: 步骤5
描述: 猪肉去皮切块，用两把菜刀剁成肉末放入碗中；葱姜切末加入肉末搅拌均匀；韭菜洗净切3mm以下长度；韭菜与肉末混合，加入蚝油、生抽、香油各2ml及蛋清，用手搅拌均匀，静置30分钟。
方法: 剁,切,搅拌,腌制
工具: 刀,碗
时间: 30分钟

### 第6步
步骤: 步骤6
描述: 左手托皮，右手夹馅，沿饺子皮圆周合拢捏实，无需捏花，确保不漏即可。
方法: 包
工具: 筷子

### 第7步
步骤: 步骤7
描述: 锅中加水至3/4高度，大火烧开，放入饺子后转中火，水冒泡后加50ml冷水，重复两次；第三次水开后加50ml冷水，再开后小火60秒即可出锅。
方法: 煮
工具: 锅
时间: 约15分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=1
source: rerank_input

```text
菜品: 煎饺
分类: 早餐
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 取出平底锅（不沾平底锅最佳）
工具: 平底锅

### 第2步
步骤: 步骤2
描述: 加入10-15ml食用油
方法: 倒
工具: 平底锅

### 第3步
步骤: 步骤3
描述: 开火，放入饺子（尽量平均铺开，不宜堆叠）
方法: 放
工具: 平底锅

### 第4步
步骤: 步骤4
描述: 立刻加入清水，水线没过饺子平均高度的1/2
方法: 倒
工具: 平底锅

### 第5步
步骤: 步骤5
描述: 盖上锅盖（此时炉灶应该处于大火）
方法: 焖
工具: 平底锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 当锅中水分仅剩2mm时，转中火开始煎制
方法: 煎
工具: 平底锅

### 第7步
步骤: 步骤7
描述: 当水分全部蒸发后，摇晃平底锅使饺子受热均匀
方法: 煎
工具: 平底锅

### 第8步
步骤: 步骤8
描述: 放入黑芝麻和葱花再焖10秒
方法: 焖
工具: 平底锅,锅盖
时间: 10秒

### 第9步
步骤: 步骤9
描述: 1-2分钟夹出一个饺子观察底部，若出现金黄色脆皮立即取出
方法: 煎
工具: 平底锅,筷子
时间: 1-2分钟

关联图谱:
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 黑芝麻 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### pair_order=2
source: rerank_input

```text
菜品: 速冻水饺
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 中火，将水倒入锅中，静候水煮沸。
方法: 煮
工具: 锅

### 第2步
步骤: 步骤2
描述: 将饺子倒入锅中。倒入锅前可以适当用水过一下。
方法: 煮
工具: 锅

### 第3步
步骤: 步骤3
描述: 倒入饺子后，用炒菜勺子或铲子搅水，注意不要铲到饺子上，避免粘锅或互相粘连。频率为平均每30秒摇3秒，饺子浮起后停止。
方法: 煮,搅拌
工具: 炒菜勺子,铲子
时间: 30秒摇3秒

### 第4步
步骤: 步骤4
描述: 饺子浮起及水再次煮沸后，盛起一个饺子观察，若面皮夹生则舀入80ml凉水降温，继续煮至沸腾，最多加两次水即可全熟。
方法: 煮,观察
工具: 炒菜勺子

### 第5步
步骤: 步骤5
描述: 所有饺子浮起后（约8分钟），用铲子或漏勺将饺子铲入盘或碗中，装盘后即可食用。
方法: 装盘
工具: 铲子,漏勺,盘或碗
时间: 约8分钟

### 第6步
步骤: 步骤6
描述: 吃完饺子后，等锅内水温降低，将水倒掉并用洗洁精及时刷锅，防止面粉在锅壁形成黏糊物质。
方法: 清洗
工具: 洗洁精,锅

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### pair_order=3
source: rerank_input

```text
菜系: 技巧知识
## 注意事项
#### 注意事项

* 含水量高的食材直接在加入后可能析出过多水分淡化调料
* 搅拌时发现水量不足或搅拌不匀可适量加白开水，若无法确定用量每次 15mL 为佳
* 部分吸水率高的食材不建议搅拌，可能导致腌制后的食材味道过重

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### pair_order=4
source: rerank_input

```text
菜品: 腊八粥
菜系: 未知
## 标签
加料时需搅拌使食材均匀分布,注意水位线，低于米线立即补水,控制火候，定时搅拌防糊底,普通锅建议水开后再下原料并改小火,有条件可使用高压锅或粥锅
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### pair_order=5
source: rerank_input

```text
菜系: 技巧知识
## 额外注意事项

- 焯水有时也会使原料内的一些不稳定、可溶性营养物质溢出，特别是新鲜蔬菜中的水溶性维生素更容易受到损失
- 动物类原料与植物类原料要分别焯水；色味较重的与色味较轻的要分别焯水；块状大的要与块状小的分别焯水，以防彼此串味
- 焯制动物性原料后，汤汁可在撇沫澄清后作为鲜汤使用

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 焯水 (TechniqueChunk): category: 烹饪技巧
```

### pair_order=6
source: rerank_input

```text
分类: 烹饪技巧
技巧文档扩展上下文: 焯水、凉拌
关键技巧内容:
## 正文
# 焯水

焯水是做饭的一道工序，读作 chāo shuǐ。

焯水指将初步加工的原料放在开水锅中加热至半熟或全熟，取出以备进一步烹调或调味。

焯水是烹调中特别是冷拌菜不可缺少的一道工序。 对菜肴的色、香、味，特别是色起着关键作用。

大部分蔬菜和带有腥羶气味的肉类原料都需要焯水。
## 操作
## 操作
## 开水锅焯水
### 开水锅焯水

开水锅焯水，就是将锅内的水加热，然后将原料下锅。下锅后及时翻动，时间要短，不要过火。

这种方法多用于植物性原料，如：芹菜、菠菜、莴笋等。 焯水时要特别注意火候，时间稍长，颜色就会变淡，而且也不脆、嫩。 因此放入锅内后，水微开时即可捞出晾凉。

- 叶类蔬菜原料应先焯水再切片，以免营养成分损失过多。
- 焯水时应水宽火旺，以使投入原料后能及时开锅；焯制绿叶蔬菜时，应略滚即捞出。
- 蔬菜类原料在焯水后应立即投凉控干，以免因余热而使之变黄、熟烂的现象发生。
- 蔬菜焯水可以放入适量色拉油如花生油、玉米油、大豆油以保持翠绿。
## 冷水锅焯水
### 冷水锅焯水

冷水锅焯水是将原料与冷水同时下锅。 水要没过原料，然后烧开，目的是使原料成熟，便于进一步加工。

土豆、胡萝卜等因体积大，不易成熟，需要煮的时间长一些。

有些动物性原料，如：白肉、牛百页、牛肚领等，也是冷水下锅加热成熟后再进一步加工的。有些用于煮汤的动物性原料也要冷水下锅，在加热过程中使营养物质逐渐溢出，使汤味鲜美，如用热水锅，则会造成蛋白质凝固。

- 锅内的加水量不宜过多，以淹没原料为度。
- 在逐渐加热过程中，必须对原料勤翻动，以使原料受热均匀，达到焯水的目的。
## 额外注意事项
## 额外注意事项

- 焯水有时也会使原料内的一些不稳定、可溶性营养物质溢出，特别是新鲜蔬菜中的水溶性维生素更容易受到损失
- 动物类原料与植物类原料要分别焯水；色味较重的与色味较轻的要分别焯水；块状大的要与块状小的分别焯水，以防彼此串味
- 焯制动物性原料后，汤汁可在撇沫澄清后作为鲜汤使用
## 肉的
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201004017, chunk_id=201004017_chunk_794, recipe_name=手工水饺, category=主食, score=0.6094350814819336, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 盆中加入所有面粉，加入芝麻香油，面粉中央挖小洞，分4-5次加入水并搅和，出现碎末状稍干面团后停止加水，用手压实面团至面光盆光。
方法: 搅拌,压实
工具: 盆

### 第2步
步骤: 步骤2
描述: 将面团置于桌上，盆倒扣，环境温度25度醒发45分钟。
方法: 醒发
工具: 盆
时间: 45分钟

### 第3步
步骤: 步骤3
描述: 醒发完成后，将面团搓条、合团、再搓条，重复3次后擀条，切成20份均匀面团并搓成直径3-3.5cm球状。
方法: 搓,擀,切
工具: 擀面杖,刀

### 第4步
步骤: 步骤4
描述: 压扁面团，撒面粉防粘，用擀面杖擀成直径约8cm、厚约2mm、中间略厚1mm的饺子皮。
方法: 擀
工具: 擀面杖

### 第5步
步骤: 步骤5
描述: 猪肉去皮切块，用两把菜刀剁成肉末放入碗中；葱姜切末加入肉末搅拌均匀；韭菜洗净切3mm以下长度；韭菜与肉末混合，加入蚝油、生抽、香油各2ml及蛋清，用手搅拌均匀，静置30分钟。
方法: 剁,切,搅拌,腌制
工具: 刀,碗
时间: 30分钟

### 第6步
步骤: 步骤6
描述: 左手托皮，右手夹馅，沿饺子皮圆周合拢捏实，无需捏花，确保不漏即可。
方法: 包
工具: 筷子

### 第7步
步骤: 步骤7
描述: 锅中加水至3/4高度，大火烧开，放入饺子后转中火，水冒泡后加50ml冷水，重复两次；第三次水开后加50ml冷水，再开后小火60秒即可出锅。
方法: 煮
工具: 锅
时间: 约15分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201003618, chunk_id=201003618_chunk_705, recipe_name=速冻水饺, category=半成品, score=0.6478274464607239, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 中火，将水倒入锅中，静候水煮沸。
方法: 煮
工具: 锅

### 第2步
步骤: 步骤2
描述: 将饺子倒入锅中。倒入锅前可以适当用水过一下。
方法: 煮
工具: 锅

### 第3步
步骤: 步骤3
描述: 倒入饺子后，用炒菜勺子或铲子搅水，注意不要铲到饺子上，避免粘锅或互相粘连。频率为平均每30秒摇3秒，饺子浮起后停止。
方法: 煮,搅拌
工具: 炒菜勺子,铲子
时间: 30秒摇3秒

### 第4步
步骤: 步骤4
描述: 饺子浮起及水再次煮沸后，盛起一个饺子观察，若面皮夹生则舀入80ml凉水降温，继续煮至沸腾，最多加两次水即可全熟。
方法: 煮,观察
工具: 炒菜勺子

### 第5步
步骤: 步骤5
描述: 所有饺子浮起后（约8分钟），用铲子或漏勺将饺子铲入盘或碗中，装盘后即可食用。
方法: 装盘
工具: 铲子,漏勺,盘或碗
时间: 约8分钟

### 第6步
步骤: 步骤6
描述: 吃完饺子后，等锅内水温降低，将水倒掉并用洗洁精及时刷锅，防止面粉在锅壁形成黏糊物质。
方法: 清洗
工具: 洗洁精,锅

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201000613, chunk_id=201000613_chunk_116, recipe_name=煎饺, category=早餐, score=0.5890806317329407, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 取出平底锅（不沾平底锅最佳）
工具: 平底锅

### 第2步
步骤: 步骤2
描述: 加入10-15ml食用油
方法: 倒
工具: 平底锅

### 第3步
步骤: 步骤3
描述: 开火，放入饺子（尽量平均铺开，不宜堆叠）
方法: 放
工具: 平底锅

### 第4步
步骤: 步骤4
描述: 立刻加入清水，水线没过饺子平均高度的1/2
方法: 倒
工具: 平底锅

### 第5步
步骤: 步骤5
描述: 盖上锅盖（此时炉灶应该处于大火）
方法: 焖
工具: 平底锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 当锅中水分仅剩2mm时，转中火开始煎制
方法: 煎
工具: 平底锅

### 第7步
步骤: 步骤7
描述: 当水分全部蒸发后，摇晃平底锅使饺子受热均匀
方法: 煎
工具: 平底锅

### 第8步
步骤: 步骤8
描述: 放入黑芝麻和葱花再焖10秒
方法: 焖
工具: 平底锅,锅盖
时间: 10秒

### 第9步
步骤: 步骤9
描述: 1-2分钟夹出一个饺子观察底部，若出现金黄色脆皮立即取出
方法: 煎
工具: 平底锅,筷子
时间: 1-2分钟

关联图谱:
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 黑芝麻 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=3
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7,tipdoc_897acc483178, recipe_name=焯水、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 焯水、凉拌
关键技巧内容:
## 正文
# 焯水

焯水是做饭的一道工序，读作 chāo shuǐ。

焯水指将初步加工的原料放在开水锅中加热至半熟或全熟，取出以备进一步烹调或调味。

焯水是烹调中特别是冷拌菜不可缺少的一道工序。 对菜肴的色、香、味，特别是色起着关键作用。

大部分蔬菜和带有腥羶气味的肉类原料都需要焯水。
## 操作
## 操作
## 开水锅焯水
### 开水锅焯水

开水锅焯水，就是将锅内的水加热，然后将原料下锅。下锅后及时翻动，时间要短，不要过火。

这种方法多用于植物性原料，如：芹菜、菠菜、莴笋等。 焯水时要特别注意火候，时间稍长，颜色就会变淡，而且也不脆、嫩。 因此放入锅内后，水微开时即可捞出晾凉。

- 叶类蔬菜原料应先焯水再切片，以免营养成分损失过多。
- 焯水时应水宽火旺，以使投入原料后能及时开锅；焯制绿叶蔬菜时，应略滚即捞出。
- 蔬菜类原料在焯水后应立即投凉控干，以免因余热而使之变黄、熟烂的现象发生。
- 蔬菜焯水可以放入适量色拉油如花生油、玉米油、大豆油以保持翠绿。
## 冷水锅焯水
### 冷水锅焯水

冷水锅焯水是将原料与冷水同时下锅。 水要没过原料，然后烧开，目的是使原料成熟，便于进一步加工。

土豆、胡萝卜等因体积大，不易成熟，需要煮的时间长一些。

有些动物性原料，如：白肉、牛百页、牛肚领等，也是冷水下锅加热成熟后再进一步加工的。有些用于煮汤的动物性原料也要冷水下锅，在加热过程中使营养物质逐渐溢出，使汤味鲜美，如用热水锅，则会造成蛋白质凝固。

- 锅内的加水量不宜过多，以淹没原料为度。
- 在逐渐加热过程中，必须对原料勤翻动，以使原料受热均匀，达到焯水的目的。
## 额外注意事项
## 额外注意事项

- 焯水有时也会使原料内的一些不稳定、可溶性营养物质溢出，特别是新鲜蔬菜中的水溶性维生素更容易受到损失
- 动物类原料与植物类原料要分别焯水；色味较重的与色味较轻的要分别焯水；块状大的要与块状小的分别焯水，以防彼此串味
- 焯制动物性原料后，汤汁可在撇沫澄清后作为鲜汤使用
## 肉的焯水
### 肉的焯水

- 肉类原料经过开水焯过后变色即可，捞出沥干水分后可以进行下一步的烹调。
- 肉类焯水后需要洗去沾附的血沫污渍，记得用温水清洗，否则肉热胀冷缩会吸附污渍，导致无法洗净血沫。
## 青菜的焯水
### 青菜的焯水

- 洗青菜时，在清水里撒一些盐，这样可以把青菜里的虫子清洗出来
- 焯过后的青菜应立即浸入冷水中，以保持颜色和口感。如果不用冷水浸，青菜会因为开水的余温变的不再清脆，而出现烂烂的感觉
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
```

### result_order=4
source: reranked_results
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1328, recipe_name=凉拌, category=烹饪技巧, score=0.5904332995414734, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 含水量高的食材直接在加入后可能析出过多水分淡化调料
* 搅拌时发现水量不足或搅拌不匀可适量加白开水，若无法确定用量每次 15mL 为佳
* 部分吸水率高的食材不建议搅拌，可能导致腌制后的食材味道过重

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=5
source: reranked_results
metadata_summary: node_id=tipdoc_897acc483178, chunk_id=tipdoc_897acc483178_chunk_1250, recipe_name=焯水, category=烹饪技巧, score=0.6018674969673157, search_type=vector_enhanced

```text
## 额外注意事项

- 焯水有时也会使原料内的一些不稳定、可溶性营养物质溢出，特别是新鲜蔬菜中的水溶性维生素更容易受到损失
- 动物类原料与植物类原料要分别焯水；色味较重的与色味较轻的要分别焯水；块状大的要与块状小的分别焯水，以防彼此串味
- 焯制动物性原料后，汤汁可在撇沫澄清后作为鲜汤使用

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 焯水 (TechniqueChunk): category: 烹饪技巧
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201003818, chunk_id=201003818_chunk_751, recipe_name=腊八粥, category=汤类, score=0.6118852496147156, search_type=vector_enhanced

```text
## 标签
加料时需搅拌使食材均匀分布,注意水位线，低于米线立即补水,控制火候，定时搅拌防糊底,普通锅建议水开后再下原料并改小火,有条件可使用高压锅或粥锅
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201004017, chunk_id=201004017_chunk_794, recipe_name=手工水饺, category=主食, score=0.6094350814819336, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 盆中加入所有面粉，加入芝麻香油，面粉中央挖小洞，分4-5次加入水并搅和，出现碎末状稍干面团后停止加水，用手压实面团至面光盆光。
方法: 搅拌,压实
工具: 盆

### 第2步
步骤: 步骤2
描述: 将面团置于桌上，盆倒扣，环境温度25度醒发45分钟。
方法: 醒发
工具: 盆
时间: 45分钟

### 第3步
步骤: 步骤3
描述: 醒发完成后，将面团搓条、合团、再搓条，重复3次后擀条，切成20份均匀面团并搓成直径3-3.5cm球状。
方法: 搓,擀,切
工具: 擀面杖,刀

### 第4步
步骤: 步骤4
描述: 压扁面团，撒面粉防粘，用擀面杖擀成直径约8cm、厚约2mm、中间略厚1mm的饺子皮。
方法: 擀
工具: 擀面杖

### 第5步
步骤: 步骤5
描述: 猪肉去皮切块，用两把菜刀剁成肉末放入碗中；葱姜切末加入肉末搅拌均匀；韭菜洗净切3mm以下长度；韭菜与肉末混合，加入蚝油、生抽、香油各2ml及蛋清，用手搅拌均匀，静置30分钟。
方法: 剁,切,搅拌,腌制
工具: 刀,碗
时间: 30分钟

### 第6步
步骤: 步骤6
描述: 左手托皮，右手夹馅，沿饺子皮圆周合拢捏实，无需捏花，确保不漏即可。
方法: 包
工具: 筷子

### 第7步
步骤: 步骤7
描述: 锅中加水至3/4高度，大火烧开，放入饺子后转中火，水冒泡后加50ml冷水，重复两次；第三次水开后加50ml冷水，再开后小火60秒即可出锅。
方法: 煮
工具: 锅
时间: 约15分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201003618, chunk_id=201003618_chunk_705, recipe_name=速冻水饺, category=半成品, score=0.6478274464607239, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 中火，将水倒入锅中，静候水煮沸。
方法: 煮
工具: 锅

### 第2步
步骤: 步骤2
描述: 将饺子倒入锅中。倒入锅前可以适当用水过一下。
方法: 煮
工具: 锅

### 第3步
步骤: 步骤3
描述: 倒入饺子后，用炒菜勺子或铲子搅水，注意不要铲到饺子上，避免粘锅或互相粘连。频率为平均每30秒摇3秒，饺子浮起后停止。
方法: 煮,搅拌
工具: 炒菜勺子,铲子
时间: 30秒摇3秒

### 第4步
步骤: 步骤4
描述: 饺子浮起及水再次煮沸后，盛起一个饺子观察，若面皮夹生则舀入80ml凉水降温，继续煮至沸腾，最多加两次水即可全熟。
方法: 煮,观察
工具: 炒菜勺子

### 第5步
步骤: 步骤5
描述: 所有饺子浮起后（约8分钟），用铲子或漏勺将饺子铲入盘或碗中，装盘后即可食用。
方法: 装盘
工具: 铲子,漏勺,盘或碗
时间: 约8分钟

### 第6步
步骤: 步骤6
描述: 吃完饺子后，等锅内水温降低，将水倒掉并用洗洁精及时刷锅，防止面粉在锅壁形成黏糊物质。
方法: 清洗
工具: 洗洁精,锅

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201000613, chunk_id=201000613_chunk_116, recipe_name=煎饺, category=早餐, score=0.5890806317329407, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 取出平底锅（不沾平底锅最佳）
工具: 平底锅

### 第2步
步骤: 步骤2
描述: 加入10-15ml食用油
方法: 倒
工具: 平底锅

### 第3步
步骤: 步骤3
描述: 开火，放入饺子（尽量平均铺开，不宜堆叠）
方法: 放
工具: 平底锅

### 第4步
步骤: 步骤4
描述: 立刻加入清水，水线没过饺子平均高度的1/2
方法: 倒
工具: 平底锅

### 第5步
步骤: 步骤5
描述: 盖上锅盖（此时炉灶应该处于大火）
方法: 焖
工具: 平底锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 当锅中水分仅剩2mm时，转中火开始煎制
方法: 煎
工具: 平底锅

### 第7步
步骤: 步骤7
描述: 当水分全部蒸发后，摇晃平底锅使饺子受热均匀
方法: 煎
工具: 平底锅

### 第8步
步骤: 步骤8
描述: 放入黑芝麻和葱花再焖10秒
方法: 焖
工具: 平底锅,锅盖
时间: 10秒

### 第9步
步骤: 步骤9
描述: 1-2分钟夹出一个饺子观察底部，若出现金黄色脆皮立即取出
方法: 煎
工具: 平底锅,筷子
时间: 1-2分钟

关联图谱:
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 黑芝麻 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=3
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7,tipdoc_897acc483178, recipe_name=焯水、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 焯水、凉拌
关键技巧内容:
## 正文
# 焯水

焯水是做饭的一道工序，读作 chāo shuǐ。

焯水指将初步加工的原料放在开水锅中加热至半熟或全熟，取出以备进一步烹调或调味。

焯水是烹调中特别是冷拌菜不可缺少的一道工序。 对菜肴的色、香、味，特别是色起着关键作用。

大部分蔬菜和带有腥羶气味的肉类原料都需要焯水。
## 操作
## 操作
## 开水锅焯水
### 开水锅焯水

开水锅焯水，就是将锅内的水加热，然后将原料下锅。下锅后及时翻动，时间要短，不要过火。

这种方法多用于植物性原料，如：芹菜、菠菜、莴笋等。 焯水时要特别注意火候，时间稍长，颜色就会变淡，而且也不脆、嫩。 因此放入锅内后，水微开时即可捞出晾凉。

- 叶类蔬菜原料应先焯水再切片，以免营养成分损失过多。
- 焯水时应水宽火旺，以使投入原料后能及时开锅；焯制绿叶蔬菜时，应略滚即捞出。
- 蔬菜类原料在焯水后应立即投凉控干，以免因余热而使之变黄、熟烂的现象发生。
- 蔬菜焯水可以放入适量色拉油如花生油、玉米油、大豆油以保持翠绿。
## 冷水锅焯水
### 冷水锅焯水

冷水锅焯水是将原料与冷水同时下锅。 水要没过原料，然后烧开，目的是使原料成熟，便于进一步加工。

土豆、胡萝卜等因体积大，不易成熟，需要煮的时间长一些。

有些动物性原料，如：白肉、牛百页、牛肚领等，也是冷水下锅加热成熟后再进一步加工的。有些用于煮汤的动物性原料也要冷水下锅，在加热过程中使营养物质逐渐溢出，使汤味鲜美，如用热水锅，则会造成蛋白质凝固。

- 锅内的加水量不宜过多，以淹没原料为度。
- 在逐渐加热过程中，必须对原料勤翻动，以使原料受热均匀，达到焯水的目的。
## 额外注意事项
## 额外注意事项

- 焯水有时也会使原料内的一些不稳定、可溶性营养物质溢出，特别是新鲜蔬菜中的水溶性维生素更容易受到损失
- 动物类原料与植物类原料要分别焯水；色味较重的与色味较轻的要分别焯水；块状大的要与块状小的分别焯水，以防彼此串味
- 焯制动物性原料后，汤汁可在撇沫澄清后作为鲜汤使用
## 肉的焯水
### 肉的焯水

- 肉类原料经过开水焯过后变色即可，捞出沥干水分后可以进行下一步的烹调。
- 肉类焯水后需要洗去沾附的血沫污渍，记得用温水清洗，否则肉热胀冷缩会吸附污渍，导致无法洗净血沫。
## 青菜的焯水
### 青菜的焯水

- 洗青菜时，在清水里撒一些盐，这样可以把青菜里的虫子清洗出来
- 焯过后的青菜应立即浸入冷水中，以保持颜色和口感。如果不用冷水浸，青菜会因为开水的余温变的不再清脆，而出现烂烂的感觉
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
```

### result_order=4
source: top_k_final
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1328, recipe_name=凉拌, category=烹饪技巧, score=0.5904332995414734, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 含水量高的食材直接在加入后可能析出过多水分淡化调料
* 搅拌时发现水量不足或搅拌不匀可适量加白开水，若无法确定用量每次 15mL 为佳
* 部分吸水率高的食材不建议搅拌，可能导致腌制后的食材味道过重

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201004017, chunk_id=201004017_chunk_794, recipe_name=手工水饺, category=主食, score=0.6094350814819336, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 盆中加入所有面粉，加入芝麻香油，面粉中央挖小洞，分4-5次加入水并搅和，出现碎末状稍干面团后停止加水，用手压实面团至面光盆光。
方法: 搅拌,压实
工具: 盆

### 第2步
步骤: 步骤2
描述: 将面团置于桌上，盆倒扣，环境温度25度醒发45分钟。
方法: 醒发
工具: 盆
时间: 45分钟

### 第3步
步骤: 步骤3
描述: 醒发完成后，将面团搓条、合团、再搓条，重复3次后擀条，切成20份均匀面团并搓成直径3-3.5cm球状。
方法: 搓,擀,切
工具: 擀面杖,刀

### 第4步
步骤: 步骤4
描述: 压扁面团，撒面粉防粘，用擀面杖擀成直径约8cm、厚约2mm、中间略厚1mm的饺子皮。
方法: 擀
工具: 擀面杖

### 第5步
步骤: 步骤5
描述: 猪肉去皮切块，用两把菜刀剁成肉末放入碗中；葱姜切末加入肉末搅拌均匀；韭菜洗净切3mm以下长度；韭菜与肉末混合，加入蚝油、生抽、香油各2ml及蛋清，用手搅拌均匀，静置30分钟。
方法: 剁,切,搅拌,腌制
工具: 刀,碗
时间: 30分钟

### 第6步
步骤: 步骤6
描述: 左手托皮，右手夹馅，沿饺子皮圆周合拢捏实，无需捏花，确保不漏即可。
方法: 包
工具: 筷子

### 第7步
步骤: 步骤7
描述: 锅中加水至3/4高度，大火烧开，放入饺子后转中火，水冒泡后加50ml冷水，重复两次；第三次水开后加50ml冷水，再开后小火60秒即可出锅。
方法: 煮
工具: 锅
时间: 约15分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: generation_context
metadata_summary: node_id=201003618, chunk_id=201003618_chunk_705, recipe_name=速冻水饺, category=半成品, score=0.6478274464607239, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 中火，将水倒入锅中，静候水煮沸。
方法: 煮
工具: 锅

### 第2步
步骤: 步骤2
描述: 将饺子倒入锅中。倒入锅前可以适当用水过一下。
方法: 煮
工具: 锅

### 第3步
步骤: 步骤3
描述: 倒入饺子后，用炒菜勺子或铲子搅水，注意不要铲到饺子上，避免粘锅或互相粘连。频率为平均每30秒摇3秒，饺子浮起后停止。
方法: 煮,搅拌
工具: 炒菜勺子,铲子
时间: 30秒摇3秒

### 第4步
步骤: 步骤4
描述: 饺子浮起及水再次煮沸后，盛起一个饺子观察，若面皮夹生则舀入80ml凉水降温，继续煮至沸腾，最多加两次水即可全熟。
方法: 煮,观察
工具: 炒菜勺子

### 第5步
步骤: 步骤5
描述: 所有饺子浮起后（约8分钟），用铲子或漏勺将饺子铲入盘或碗中，装盘后即可食用。
方法: 装盘
工具: 铲子,漏勺,盘或碗
时间: 约8分钟

### 第6步
步骤: 步骤6
描述: 吃完饺子后，等锅内水温降低，将水倒掉并用洗洁精及时刷锅，防止面粉在锅壁形成黏糊物质。
方法: 清洗
工具: 洗洁精,锅

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=2
source: generation_context
metadata_summary: node_id=201000613, chunk_id=201000613_chunk_116, recipe_name=煎饺, category=早餐, score=0.5890806317329407, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 取出平底锅（不沾平底锅最佳）
工具: 平底锅

### 第2步
步骤: 步骤2
描述: 加入10-15ml食用油
方法: 倒
工具: 平底锅

### 第3步
步骤: 步骤3
描述: 开火，放入饺子（尽量平均铺开，不宜堆叠）
方法: 放
工具: 平底锅

### 第4步
步骤: 步骤4
描述: 立刻加入清水，水线没过饺子平均高度的1/2
方法: 倒
工具: 平底锅

### 第5步
步骤: 步骤5
描述: 盖上锅盖（此时炉灶应该处于大火）
方法: 焖
工具: 平底锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 当锅中水分仅剩2mm时，转中火开始煎制
方法: 煎
工具: 平底锅

### 第7步
步骤: 步骤7
描述: 当水分全部蒸发后，摇晃平底锅使饺子受热均匀
方法: 煎
工具: 平底锅

### 第8步
步骤: 步骤8
描述: 放入黑芝麻和葱花再焖10秒
方法: 焖
工具: 平底锅,锅盖
时间: 10秒

### 第9步
步骤: 步骤9
描述: 1-2分钟夹出一个饺子观察底部，若出现金黄色脆皮立即取出
方法: 煎
工具: 平底锅,筷子
时间: 1-2分钟

关联图谱:
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 黑芝麻 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=3
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7,tipdoc_897acc483178, recipe_name=焯水、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

```text
技巧文档扩展上下文: 焯水、凉拌
关键技巧内容:
## 正文
# 焯水

焯水是做饭的一道工序，读作 chāo shuǐ。

焯水指将初步加工的原料放在开水锅中加热至半熟或全熟，取出以备进一步烹调或调味。

焯水是烹调中特别是冷拌菜不可缺少的一道工序。 对菜肴的色、香、味，特别是色起着关键作用。

大部分蔬菜和带有腥羶气味的肉类原料都需要焯水。
## 操作
## 操作
## 开水锅焯水
### 开水锅焯水

开水锅焯水，就是将锅内的水加热，然后将原料下锅。下锅后及时翻动，时间要短，不要过火。

这种方法多用于植物性原料，如：芹菜、菠菜、莴笋等。 焯水时要特别注意火候，时间稍长，颜色就会变淡，而且也不脆、嫩。 因此放入锅内后，水微开时即可捞出晾凉。

- 叶类蔬菜原料应先焯水再切片，以免营养成分损失过多。
- 焯水时应水宽火旺，以使投入原料后能及时开锅；焯制绿叶蔬菜时，应略滚即捞出。
- 蔬菜类原料在焯水后应立即投凉控干，以免因余热而使之变黄、熟烂的现象发生。
- 蔬菜焯水可以放入适量色拉油如花生油、玉米油、大豆油以保持翠绿。
## 冷水锅焯水
### 冷水锅焯水

冷水锅焯水是将原料与冷水同时下锅。 水要没过原料，然后烧开，目的是使原料成熟，便于进一步加工。

土豆、胡萝卜等因体积大，不易成熟，需要煮的时间长一些。

有些动物性原料，如：白肉、牛百页、牛肚领等，也是冷水下锅加热成熟后再进一步加工的。有些用于煮汤的动物性原料也要冷水下锅，在加热过程中使营养物质逐渐溢出，使汤味鲜美，如用热水锅，则会造成蛋白质凝固。

- 锅内的加水量不宜过多，以淹没原料为度。
- 在逐渐加热过程中，必须对原料勤翻动，以使原料受热均匀，达到焯水的目的。
## 额外注意事项
## 额外注意事项

- 焯水有时也会使原料内的一些不稳定、可溶性营养物质溢出，特别是新鲜蔬菜中的水溶性维生素更容易受到损失
- 动物类原料与植物类原料要分别焯水；色味较重的与色味较轻的要分别焯水；块状大的要与块状小的分别焯水，以防彼此串味
- 焯制动物性原料后，汤汁可在撇沫澄清后作为鲜汤使用
## 肉的焯水
### 肉的焯水

- 肉类原料经过开水焯过后变色即可，捞出沥干水分后可以进行下一步的烹调。
- 肉类焯水后需要洗去沾附的血沫污渍，记得用温水清洗，否则肉热胀冷缩会吸附污渍，导致无法洗净血沫。
## 青菜的焯水
### 青菜的焯水

- 洗青菜时，在清水里撒一些盐，这样可以把青菜里的虫子清洗出来
- 焯过后的青菜应立即浸入冷水中，以保持颜色和口感。如果不用冷水浸，青菜会因为开水的余温变的不再清脆，而出现烂烂的感觉
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
```

### result_order=4
source: generation_context
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1328, recipe_name=凉拌, category=烹饪技巧, score=0.5904332995414734, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 注意事项
#### 注意事项

* 含水量高的食材直接在加入后可能析出过多水分淡化调料
* 搅拌时发现水量不足或搅拌不匀可适量加白开水，若无法确定用量每次 15mL 为佳
* 部分吸水率高的食材不建议搅拌，可能导致腌制后的食材味道过重

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

