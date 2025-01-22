
<!--
title: 关于时间序列数据的十件事
cover: https://miro.medium.com/v2/da:true/resize:fit:1200/0*BanAs9Dr-oovfWrq
-->

获取一份关于如何充分利用时间序列数据的技巧和推荐资源的综合指南。

> 译自 [10 Things You Need to Know About Time-Series Data](https://medium.com/timescale/10-things-you-need-to-know-about-time-series-data-57111f2df876)，作者 Team Timescale。

我们整理了一份全面的指南，包含提示和推荐资源，帮助您充分利用时间序列数据。✅ 现在，您的数据是时间序列吗？

您可能没有这样想过，但请查看我们的示例列表——您可能会感到惊讶。从优化数据库性能、与第三方工具集成，到评估时间序列数据库时需要考虑的因素，涵盖的主题丰富多样，无论您是时间序列新手还是经验丰富的数据库管理员，都能从中受益。

这份指南汇总了您需要了解的时间序列数据库的相关信息，内容来源于我们的内部团队和活跃的开发者社区。（其中一些内容可能是复习，而另一些可能是您未曾了解的。）

## 10. “大云”供应商不一定能提供更好的产品。

Resource: [What We Learned From Benchmarking Amazon Aurora PostgreSQL Serverless](https://www.timescale.com/blog/what-we-learned-from-benchmarking-amazon-aurora-postgresql-serverless/)

没有人希望一开始就使用一个数据库，结果发现它无法扩展或不适合其应用程序和系统的增长需求。正如这篇文章指出的那样，时间序列数据库在数据摄取速度、查询延迟、易用性、可靠性等方面差异很大。

我们有对时间序列数据库性能进行基准测试的历史，我们花费数周时间分析了 Amazon Aurora Serverless 的数据摄取性能、查询速度、成本和可靠性。我们多次仔细检查了这些数字，因为我们几乎难以置信，但 Timescale 的 PostgreSQL 云平台：

- 数据摄取速度快 35%
- 在除两个查询类别外的所有查询类别中，查询速度快 1.15 倍到 16 倍
- 数据存储效率提高 95%
- 每小时计算成本降低 52%
- 存储创建的数据每月成本降低 78%

[查看完整文章](https://www.timescale.com/blog/what-we-learned-from-benchmarking-amazon-aurora-postgresql-serverless/) 以了解详细结果、关键数据库考虑标准以及复制结果和运行您自己的基准测试的步骤。

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*EC8euXmdaKLdRkN8)

## 9. 时间序列数据非常适合金融服务，从传统股票市场到加密货币。

Resource: [Learn how to power a (successful) crypto trading bot with TimescaleDB](https://www.timescale.com/blog/blog/how-i-power-a-successful-crypto-trading-bot-with-timescaledb/)

[阅读软件开发人员和活跃的 TimescaleDB 社区成员是如何构建他的加密交易机器人的](https://www.timescale.com/blog/blog/how-i-power-a-successful-crypto-trading-bot-with-timescaledb/)——并获得了 480 倍的回报——使用 TensorFlow、Node.js、TimescaleDB 和机器学习情绪分析模型，以及他在此过程中学到的经验教训，以及他对有抱负的加密交易者的建议。

而且，如果您想尝试自己的加密分析，请查看我们的[分析加密货币市场数据](https://docs.timescale.com/latest/tutorials/analyze-cryptocurrency-data/) 教程（其中包括分步说明和 5 个以上的示例查询）。

此外，时间序列数据不仅仅是物联网、石油和天然气以及金融领域的利基市场；时间序列数据无处不在，从跟踪包裹递送车队物流到监控系统和应用程序，预测航班到达时间以及报告空气质量。（[查看我们关于时间序列数据的入门指南](https://www.timescale.com/blog/blog/what-the-heck-is-time-series-data-and-why-do-i-need-a-time-series-database-dcf3b1b18563/) 以了解使时间序列数据独一无二的更多信息。）

如果您不确定从哪里开始或时间序列数据是否适用于您的场景，我们的[开发者问答系列](https://www.timescale.com/blog/tag/dev-q-a/) 邀请社区成员分享他们使用数据解决问题、改进流程以及（在加密机器人案例中）将副项目变成赚钱机器的绝妙方法。

## 8. 持续优化数据库插入速率对于时间序列工作负载尤其重要。

Resource: [Get our 13 tips to improve PostgreSQL Insert performance](https://www.timescale.com/blog/blog/13-tips-to-improve-postgresql-insert-performance/)

对于时间序列数据，更改被视为*插入*，而不是覆盖——当您需要保留所有数据而不是覆盖过去的值时，优化数据库摄取新数据的速度变得至关重要。

为了帮助您提高数据库性能并针对时间序列场景进行优化，Timescale 首席技术官分享了[他的最佳技巧](https://www.timescale.com/blog/blog/13-tips-to-improve-postgresql-insert-performance/)。您将获得有关普通 PostgreSQL 的建议——例如如何测试 I/O 性能——以及一些 TimescaleDB 特定的建议。

## 7. 启用压缩可以显著降低存储成本，加快查询速度，并允许您保留更多数据。

Resource: [Building Columnar Compression for Large PostgreSQL Databases](https://www.timescale.com/blog/building-columnar-compression-in-a-row-oriented-database/)

压缩算法：它们并非魔法，但却能显著降低您的数据存储成本并加快查询速度。鉴于时间序列数据的持续增长特性，数据快速堆积，缩减数据存储需求就显得尤为关键。

本文将讲述我们如何为PostgreSQL构建灵活、高性能的列式压缩机制以提高其可扩展性。

✨  有趣的事实：通过结合列式存储和专门的压缩算法，我们能够实现令人印象深刻的压缩率，在任何其他关系数据库中都无法比拟（+95%）。


## 6. 有效地使用和查询您的时间序列数据，可以将其转化为预测趋势和预测未来事件的工具。

Resource: [Replacing kdb+ With PostgreSQL for Time-Series Forecasting](https://www.timescale.com/blog/how-a-data-scientist-is-building-a-time-series-forecasting-pipeline-using-timescaledb-and-helping-others-perform-time-series-engineering-directly-in-the-database/)

[时间序列预测](https://www.timescale.com/blog/what-is-time-series-forecasting/)本身就非常强大。但是，将时间序列数据与其他关系型业务数据结合起来，可以帮助您对数据（和业务）如何随时间变化做出更深入的预测。在本开发者问答中，数据科学家Andrew Engel分享了他如何使用TimescaleDB创建机器学习管道概念验证以进行时间序列预测的故事。


## 5. 如果你选择了正确的数据库，你可以将其与你最喜欢的第三方和开源工具集成。

Resource: [See our favorite PostgreSQL extensions for time-series](https://www.timescale.com/blog/blog/top-5-postgresql-extensions/)

PostgreSQL拥有2万多个扩展可供选择，我们非常喜欢它庞大的生态系统和极高的可扩展性。幸运的是，[许多扩展可以帮助您更高效地处理时间序列数据](https://www.timescale.com/learn/postgresql-extensions)，而无需切换到全新的数据库。

但是，从哪里开始呢？

为了帮助您找到可能适合您的选项，我们调查了内部团队成员和活跃的社区成员，以获取我们的“必备”扩展列表，其中包括一些鲜为人知但有用的扩展。

⭐️  奖励：安装说明和示例查询，向您展示如何获取每个扩展、它的工作原理以及它允许您做什么。


## 4. 数据库架构、灵活性和查询语言很重要——而且差异很大。

Resource: [Read how TimescaleDB and InfluxDB are purpose-built differently — and how this impacts performance](https://www.timescale.com/blog/blog/timescaledb-vs-influxdb-for-time-series-data-timescale-influx-sql-nosql-36489299877/)

虽然我们的[Amazon Aurora基准测试](https://www.timescale.com/blog/what-we-learned-from-benchmarking-amazon-aurora-postgresql-serverless/)表明，选择正确的时间序列数据库并不像从大型云提供商中选择那么简单，但我们的InfluxDB比较演示了理解您的需求的重要性，例如查询语言、开发者入门时间、生态系统和完全托管的数据库选项。

我们报告了InfluxDB在哪些方面优于TimescaleDB（低基数查询），并使用数据来展示为什么如果您拥有高基数数据集、想要灵活的托管数据库选项和/或不想学习专有的查询语言，TimescaleDB是更好的选择。

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*S_kBfdbVa4iSGr6O)

说到查询语言，我们创建了[一份备忘单，以帮助您了解InfluxQL、Flux和SQL之间的区别](https://www.timescale.com/learn/influxql-flux-sql-which-query-language-is-best-with-cheatsheet)。


## 3. Grafana非常适合时间序列，但存在学习曲线。

Resource: [Watch Guide to Grafana 101: Getting Started With (Awesome) Visualizations](https://youtu.be/oPumWaoNw5s)

Grafana是一个令人惊叹的开源可视化工具（Timescale团队非常喜欢它），非常适合常见的时间序列场景，但是有很多功能你可能不知道如何、何时或为何使用。

为了帮助您了解Grafana为什么非常适合时间序列，Avthar([@avthars](https://twitter.com/avthars)) 演示了如何构建6多种可视化——从世界地图到仪表——用于物联网、DevOps等等。您将看到真实的示例，并获得创建您自己的（很棒的）可视化所需的最佳实践、代码示例和灵感。


## 2. 您可以托管您的时间序列数据，并且只为存储的数据付费。

Resource: [Navigating a Usage-Based Model for PostgreSQL](https://www.timescale.com/blog/navigating-a-usage-based-model-for-postgresql-tips-to-reduce-your-database-size/)

对于时间序列数据，每个数据点都作为新值插入，而不是覆盖先前（即较早的）值。因此，时间序列工作负载的扩展速度**远**快于其他类型的数据，您需要一个能够与您一起发展的数据库——不会产生天文数字的成本或影响性能。

使用Timescale Cloud，[您只需为实际使用的Timescale服务存储付费，无需价格陷阱或隐藏成本](https://www.timescale.com/blog/savings-unlocked-why-we-switched-to-a-pay-for-what-you-store-database-storage-model/)。这种新的存储体验简单、透明，并且可以为您节省资金——尤其是在结合压缩和分层存储等功能时。👇


## 1. 用于时间序列的关系型数据库可以无限扩展

Resource: [Scaling PostgreSQL for Cheap: Introducing Tiered Storage in Timescale](https://www.timescale.com/blog/scaling-postgresql-for-cheap-introducing-tiered-storage-in-timescale/)

最后，我们想谈谈时间序列数据：关系数据库可以无限扩展。为了证明这一点，我们构建了分层存储，这是一种多层存储架构，旨在为Timescale平台上的时间序列和分析数据库实现无限的、低成本的可扩展性。

通过我们的分层存储架构，您现在可以将较旧的、访问频率较低的数据存储在低成本的存储层中，同时仍然能够访问它——而无需牺牲频繁访问数据的性能。最棒的是？它非常经济实惠：我们的低成本存储层的**价格为每GB/月0.021美元**——比Amazon S3更便宜。

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*ND3ntgsnm8vtTnD5)

## 总结

如果您更喜欢自行管理TimescaleDB，请[查看我们的GitHub仓库](https://github.com/timescale/timescaledb)以获取安装选项（⭐️ 欢迎和感谢！）。

最后，[加入我们的Slack社区](https://slack.timescale.com/)以提出问题、获得帮助并了解有关所有时间序列的更多信息；我们的工程师和社区成员活跃于所有频道。

