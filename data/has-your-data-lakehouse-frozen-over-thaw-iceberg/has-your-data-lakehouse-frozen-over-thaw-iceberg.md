
<!--
title: 您的数据湖是否已经冻结？解冻冰山
cover: https://cdn.thenewstack.io/media/2024/07/085f7683-frozen-data-lakehouse.jpg
-->

Apache Iceberg 的开放式表格式可以帮助解决大规模湖仓数据上运行操作工作负载时用户体验不佳的问题。

> 译自 [Has Your Data Lakehouse Frozen Over? Thaw Iceberg](https://thenewstack.io/has-your-data-lakehouse-frozen-over-thaw-iceberg/)，作者 Dave Eyler。

数据湖最初的灵感很简单：开发人员需要一个集中式位置来存储任何类型的大规模数据，即使这些数据不符合传统数据仓库所需的关联模式。

如果没有这个集中式位置，开发人员就只剩下两个选择来存储他们的数据——数据湖和仓库，两者都不是理想的选择。于是，[数据湖仓](https://thenewstack.io/5-ways-to-make-the-most-of-your-new-data-lakehouse/) 出现了，它将数据湖的 [Python](https://thenewstack.io/python/) 和机器学习功能与仓库强大的 [SQL](https://roadmap.sh/sql) 功能相结合。换句话说，对于开发人员来说，这是两全其美。

不幸的是，对于许多转向数据湖仓驱动的产品和服务的用户来说，承诺的满意度尚未到来。为什么？因为他们的湖仓已经冻住了。

## 等等，湖仓怎么了？

我所说的湖仓冻住是什么意思？这实际上是一个双重隐喻。第一个意思是字面上的——[Apache Iceberg](https://thenewstack.io/apache-iceberg-a-different-table-design-for-big-data/) 已经成为湖仓的标准存储格式，而冰是冻结的。

第二个意思是描述应用程序的糟糕用户体验以及在湖仓数据上为机器学习等运营工作负载提供动力的困难。通常，用于将数据写入 Iceberg 的数据平台不是满足这些需求的最佳平台。要做到这一点，您需要一个现代化的数据平台，具备以下功能：

1. 亚秒级点读写。
2. 生成式 AI，需要向量搜索和全文搜索。
3. 亚秒级分析查询，用于洞察过去在关系数据和 JSON 数据上发生的事情。
4. 超快摄取，为分析查询和实时用例提供动力。

更重要的是，您需要这些功能能够大规模扩展，具有高并发性和应用程序用户和运营工作负载所需的高质量性能体验。

## 永久解冻数据湖仓

牢记这些目标，我们的团队开发了与 Apache Iceberg 的全新原生集成，这为“解冻”Apache Iceberg 数据开辟了一系列可能性。

我们与 Apache Iceberg 的集成只是许多开发人员在处理复杂数据集时所面临的漫长旅程的第一步。随着企业寻找新的方法来获取和利用其数据，数据环境将继续变得更加难以驾驭——这还没有考虑到 [生成式 AI 应用程序](https://thenewstack.io/whats-next-in-building-better-generative-ai-applications/) 的兴起及其对数据管理和访问的影响。

无论数据摄取和管理变得多么复杂，强大的开源基础仍然具有价值，这就是我们对这种新集成感到兴奋的原因。

要了解 SingleStore 的实时数据平台如何推动您公司的创新并解冻您最宝贵企业数据，请立即试用 SingleStore 的 [免费试用版](https://www.singlestore.com/cloud-trial/)。
