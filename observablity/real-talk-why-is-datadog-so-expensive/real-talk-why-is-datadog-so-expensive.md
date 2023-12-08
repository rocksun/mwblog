<!--
title:  实话实说：为什么Datadog这么贵？
cover: https://cdn.thenewstack.io/media/2023/12/780ce218-expensive-observability-1024x769.jpg
-->

云原生架构产生了更多的数据，增加了可观测性的成本。然而，有更好的方法来管理这些费用。

> 译自 [Real Talk: Why Is Datadog So Expensive?](https://thenewstack.io/real-talk-why-is-datadog-so-expensive/)，作者 Rachel Dines。

我最近在 [X](https://twitter.com/kellabyte/status/1704947999414063465)（前身为 Twitter）、[Reddit](https://www.reddit.com/r/kubernetes/comments/15b1057/datadog_costs_that_high/) 和 [HackerNews](https://news.ycombinator.com/item?id=35865473) 上看到了很多讨论 Datadog 高昂成本的帖子。这是一个热门话题，工程师们纷纷发布博客，讨论他们如何采取强力手段来降低指标。

但是，我们是怎么到这个地步的呢？为什么这些成本这么高？为什么公司为他们的[可观测性](https://thenewstack.io/observability/)支付的费用比生产基础设施还要高？有很多争论和指责锁定和企业贪婪的言论，这当然在一定程度上是有道理的。

更深层次的问题是：采用容器化基础设施和[微服务应用](https://chronosphere.io/learn/what-is-microservices-architecture/)的基本架构变化。如果我们不理解并解决这个问题，历史将重演。

## 声明：我在 Datadog 的竞争对手 Chronosphere 工作

好吧，这是事实，我在 [Chronosphere](https://chronosphere.io/?utm_content=inline-mention) 工作，这是一家与 Datadog 竞争的公司。我保证这篇文章不会向您推销我们的产品。Datadog 是一位强大的竞争对手，多年来我一直看着它建立了一个令人惊叹的业务。

我的前公司在 2015 年至 2018 年是 Datadog 的密切合作伙伴，我们看到了它的迅猛增长，我们迫切希望效仿。与此同时，我看到 Datadog 的客户对不断飙升和不可预测的成本感到越来越不满，然而他们觉得自己无法离开。

这也是我在 2021 年加入 Chronosphere 的原因之一，因为我看到了这一趋势的发展。在我加入这个领域之前，我进行了一些市场规模和分析，发现可观测性对基础设施支出的影响最大：在公共云上每花费1美元，你可能会在可观测性上花费0.25至0.35美元。这让我觉得这是一个值得颠覆的市场。

## 真正的罪魁祸首：数据增长

问题的根本原因很简单：[可观测性数据](https://thenewstack.io/top-ways-to-reduce-your-observability-costs-part-1/)（指标、日志、跟踪和事件）比这些工具预测的要多得多。因此，它们的架构不适应这个数据量，定价也不相应。我们最终产生如此多数据的原因有很多。

业务驱动因素：

- **数字转型**：技术渗透到更多业务领域自然而然地带来了更多数据，以监控系统健康并确保整体系统运行顺畅。
- **客户期望提高，风险加大**：根据[2023年在线可靠性报告](https://chronosphere.io/learn/2023-online-reliability-report-gone-in-a-glitch/)，美国人平均只容忍在应用程序或网站上出现不可靠或中断不到四次，就会转投竞争对手。运营高性能和高可用性的服务，提供卓越的客户体验，需要更详细的可观测性数据。
- **数据囤积**：当你每分钟都获取大量数据时，很难知道哪些数据是有用的。如果没有正确的工具来解析它，你可能会陷入“我永远不知道何时会需要这些数据”的陷阱，并保留比必要更多的数据。

技术驱动因素：

- **由容器和微服务生成的遥测数据更多**：[云原生环境](https://thenewstack.io/cloud-native/what-is-cloud-native-and-why-does-it-matter/)（即容器和微服务）具有显著的优势，但由于需要监视每个单独组件和服务的健康状态，因此自然而然地产生更多数据。例如，现在每个容器和微服务产生的可观测性数据量相当于以前每个虚拟机（VM）和单体应用程序产生的数据量。但现在，你不再只有几十个虚拟机和少数几个应用程序，而是拥有成千上万个容器和数十个微服务。
- **一些云原生环境的规模**：按设计，云原生是分散的，工程团队可以快速启动组件，这意味着服务和容器的数量呈指数级增长，产生了大量数据。

这种数据增长导致[可观测性支出飙升](https://thenewstack.io/4-ways-quotas-protect-your-organization-from-observability-data-explosions/)。如果不改变定价模型或软件以适应数据增长，并继续基于传统的监控标准定价，云原生架构突然变得惊人昂贵。

## 为什么 Datadog 不能降低价格？

我怀疑有两个原因：

- **股东价值**：Datadog 的股票在过去几年表现异常出色。如果它降低价格，将立即影响收入，从而影响报告的收益，进而导致股价下跌。
- **销售成本**：Datadog 经历了[三代架构](https://www.datadoghq.com/blog/engineering/introducing-husky/)，其最新的 Husky 在2022年刚刚发布。这次重新架构主要侧重于效率，但并未降低价格，因此我认为它有助于降低销售成本（COGS）并使利润率保持健康水平。由于 Datadog 可能不会很快进行另一次重新架构投资，因此通过降低价格来损害其利润率的可能性较小。

## Datadog 的替代方案

如果您不想支付 Datadog 的费用，有几个选择。

### #1：DIY 开源

一个有吸引力的替代方案是使用开源工具在内部运行自己的可观测性系统。好消息是，至少对于指标和追踪来说，开源工具取得了长足的进步，并正在形成行业公认的标准。[Prometheus](https://thenewstack.io/know-the-hidden-costs-of-diy-prometheus/) 和 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry/) 与各种时间序列数据库后端（Mimir、Thanos 或 M3）是替代 Datadog 的可行选择。

但需要注意的是，这通常不会在实际美元上为您节省资金。这只是将资本支出（CapEx）与运营支出（OpEx）进行交换。运行这些系统的[人力和基础设施成本](https://chronosphere.io/learn/the-hidden-costs-of-self-managing-tsdbs/)是相当可观的，如果尝试省略某些步骤，可能会后悔不已。

最近我和一位朋友交谈，他将公司从昂贵的商业SaaS解决方案迁移到了内部开源工具上。他承认，考虑到大约有 8% 的开发人员现在致力于运行这个系统，公司实际上并没有节省任何资金。

### #2：下一代可观测性工具

这并不是我向您推销我公司产品的地方。这是我要说的工具从一开始就以数据增长为基础的地方。解决方案的成本始终掌握在客户手中，因此不会有意外超支。

就像 Datadog、New Relic 和类似的工具取代了上一代的 Solarwinds、BMC 和 CA Technologies 一样，这一新一代的可观测性工具开始引起轰动。与这些供应商交流，了解他们是如何处理观察性数据过多的问题，而不是用更好的单位经济学来处理它。

## 结论

Datadog 的高额账单和供应商锁定不知何故已成为一种必要的恶；您知道您需要可观测性，但对所有选项不太确定。尽管 Datadog 的计费方式和专有代码存在一些问题，但它已经存在了足够长的时间，看起来仍然是一个可行的选择。但事情并不一定要这样。

随着越来越多的可观测性公司进入这一领域，也出现了从一开始就致力于解决高基数数据增长问题的选项。这些选项为您提供了更灵活的基础设施、更多对数据的控制以及对每月账单更明晰的可见性，最终为可观测性团队打造了更具可持续性和成本效益的运营模型。
