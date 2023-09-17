<!-- 
# 向量搜索如何影响客户购物习惯
https://cdn.thenewstack.io/media/2023/08/a931c841-grocery_aisle_dalle.jpg
Image created by DALL-E
 -->

利用大型零售商的客户促销来推动销售的向量搜索应用展望。

译自 [How Vector Search Can Influence Customer Shopping Habits](https://thenewstack.io/how-vector-search-can-influence-customer-shopping-habits/) 。

## 向量搜索如何影响客户购物习惯

随着[大语言模型](https://roadmap.sh/guides/free-resources-to-learn-llms)、向量和向量搜索的热议，退一步理解这些人工智能技术进步如何转化为组织结果，最终为客户带来价值尤为重要。

在[早期的一篇文章](https://thenewstack.io/an-e-tailers-journey-to-real-time-ai-recommendations/)中，我讲述了一个假想的承包商的故事，他被聘请帮助一家大型零售商实施 AI/ML 解决方案。在这里，我们继续讲述这个故事，当我们的分布式系统和 AI 专家利用[向量搜索](https://www.datastax.com/guides/what-is-vector-search?utm_source=thenewstack&utm_medium=byline&utm_campaign=vector-search&utm_term=all-plays&utm_content=etailers-journey)来推动一个大型零售商的客户促销结果。

## 问题

今天，我们与促销团队见面。他们正在寻求我们的帮助，对客户广告、优惠和优惠券做出一些更明智的决定。目前，促销活动主要基于地理市场。因此，发送给一个城市的客户的促销将与发送给另一个城市的客户的促销不同。因此，这些活动需要提前规划。

问题是，营销部门正在对他们施加压力，要求他们提供更具战略性的定位客户方法，不考虑地理区域。思路是，一些特定客户可能更有可能利用某些优惠，这取决于他们的购买历史。如果我们能够实时提供，例如按购物车提供 10% 的相关产品折扣，我们可能会推动一些额外的销售。

首先，我决定查看他们的 [Apache Cassandra](https://thenewstack.io/vector-search-is-coming-to-apache-cassandra/) 集群中的一些匿名订单数据。很明显，数据中确实存在一些模式，一些客户以一定的规律购买相同的物品(主要是杂货)。也许我们可以利用这些数据?

## 改善体验

我们具有的一件有利条件：我们的客户倾向于通过多种渠道与我们互动。一些人使用网站，一些人使用移动应用程序，还有一些人仍然会走进我们 1000 多个实体店。并且店内超过一半的客户同时使用移动应用程序。

另一个有趣的点：如果我们按家庭地址而不是仅按客户 ID 汇总商品销售数据，我们会看到更加固定的购物模式。将几个不同来源的数据汇总在一起后，我们可以开始描绘出这些数据的样子。

例如，一对夫妇养了一条狗。通常，一方会买狗食品。但有时另一方也会买。在个人客户层面，这些事件并不形成很大的模式。

但是在家庭层面汇总在一起，它们确实如此。事实上，他们每周都会购买一卷以上 6 磅装的“HealthyFresh – Chicken Raw Dog Food”。根据推荐的份量大小判断，他们要么养了 6 只小狗，要么养了一只大狗，可能是后者。图 1 显示了这些数据的可视化。

![](https://cdn.thenewstack.io/media/2023/08/39271adf-image1.png)
*图1 - 显示客户家庭数据结构的图,包括地址、客户姓名、已知设备ID、常去商店ID和常购物品。*

每位客户经常光顾的商店也会发挥作用。例如，我们的客户 Marie 可能出差旅行，可能会访问她从未去过的一家商店。如果商店与她的常去商店列表存在较大距离，我们可以假设 Marie 可能正在购买与她的旅行相关的特定物品。在这种情况下，她的正常购物习惯不适用(她可能不会买狗粮)，我们不需要向她呈现促销以鼓励她花钱。

然而，如果 Marie 在她经常光顾的商店之一，在她的移动设备上触发促销可能是有意义的。如果我们鼓励客户使用手机扫描物品，我们将知道哪些物品在他们的实体购物车中。然后，我们可以呈现类似的物品来补充购物车中已有的产品。

## 计算向量以查找类似产品

查找类似产品意味着我们需要为产品计算相似性向量。我们可以用几种方法来做到这一点。为了制定一个最小可行产品，我们可以仅关注产品名称并基于“词袋”方法构建自然语言处理(NLP)模型。

在这种方法中，我们从所有产品名称中获取每个单词，并为每个唯一的单词创建一个条目。这就是我们的词汇表。我们为每个产品创建和存储的相似性向量成为一个数组，指示当前产品名称是否具有该单词，如下表 1 所示。我们可以使用 [TensorFlow](https://www.tensorflow.org/) 等平台来构建和训练我们的机器学习(ML)模型。

![](https://cdn.thenewstack.io/media/2023/08/e08ebe91-screenshot-2023-08-01-at-12.40.05-pm.png)
*表1 - 宠物用品类别下产品名称的词袋NLP词汇表,显示每个向量的组装方式。*

“词袋”方法的一个问题是向量可能包含更多的零比一。这可能导致更长的模型训练时间和更长的预测时间。为了减少这些问题，我们将为每个主要产品类别构建一个唯一的词汇表。跨不同类别的向量将不可用，但这没关系，因为我们可以在查询时按类别过滤。

然后，我们可以在 Apache Cassandra 集群中创建一个表来支持每个特定类别的向量搜索。由于我们的词汇表包含 14 个单词，我们的向量大小也需要为 14：

```sql
CREATE TABLE pet_supply_vectors (
    product_id TEXT PRIMARY KEY，
    product_name TEXT，
    product_vector vector<float， 14>);
```

为了使向量搜索适当地发挥作用，我们需要在表上创建一个存储附加的二级索引(SASI):

```sql
CREATE CUSTOM INDEX ON pet_supply_vectors(product_vector) USING 'StorageAttachedIndex';
```

然后，我们可以将 ML 模型的输出加载到 Cassandra 中。有了这些数据，下一步是添加一个新的服务，它使用以下查询执行向量搜索：

```sql
SELECT * FROM pet_supply_vectors
    ORDER BY product_vector
    ANN OF [1， 1， 1， 1， 1， 0， 0， 0， 0， 0， 0， 0， 0， 0] LIMIT 2;
```

这运行一个近似最近邻(ANN)算法，使用当前产品存储的向量。这将返回当前产品和下一个最接近的(最近邻)产品，得益于 LIMIT 2 子句。 

在上面的查询中，我们使用“HealthyFresh – Chicken Raw Dog Food”产品的向量，假设客户刚刚将其添加到网上购物车中或使用手机扫描了它。我们处理此事件并组成以下消息:

```
customer_id: a3f5c9a3
device_id: e6f40454  
product_id: pf1843
product_name: “HealthyFresh - Chicken raw dog food”
product_vector: [1， 1， 1， 1， 1， 0， 0， 0， 0， 0， 0， 0， 0， 0]
```

然后，我们将此消息发送到 [Apache Pulsar](https://www.datastax.com/blog/2020/06/what-apache-pulsar?utm_source=thenewstack&utm_medium=byline&utm_campaign=vector-search&utm_term=all-plays&utm_content=etailers-journey) 主题。我们从主题中消费，并使用上述数据调用 Promotions 微服务上的 **getPromotionProduct** 端点。这会运行上面指示的查询，返回两个 “HealthyFresh” 口味。我们忽略与我们已经拥有的产品匹配 100% 的 product_vector 数据(我们已经拥有的产品)，并在其设备上触发“HealthyFresh – Beef”口味的促销：

![](https://cdn.thenewstack.io/media/2023/08/dbc86ee9-image2.png)

## 结论和下一步

在此逻辑生效的几周后，我们的促销团队联系我们并报告，我们的方法触发额外销售的次数约为 25%。虽然把这称为“胜利”很诱人，但我们肯定可以看看改进的地方。

我们采用“词袋” NLP 方法只是为了制作一个初始的(软件)产品。我读到不同的 NLP 算法如 “Word2Vec” 在长期内可能是一个更好的方法。我们的模型也仅关注构建包含产品名称词汇的词汇表。也许扩展我们的模型输入以包括其他产品详细信息(例如:大小、颜色、品牌)可能有助于微调一些？

在下一篇文章中，我们将展示如何使用向量搜索帮助我们的运输服务团队提高交付路线效率。

请查看 GitHub 存储库，其中包含一个 [getPromotionProduct 方法的示例，该方法在 DataStax Astra DB 中执行向量搜索](https://github.com/aar0np/CustomerPromotionVectorSearch/tree/main)。
