# 可观测性可能会很昂贵，以下是如何削减成本

![Featued image for: Observability Can Get Expensive. Here’s How to Trim Costs](https://cdn.thenewstack.io/media/2025/02/6a790864-observability-expensive-2-1024x576.jpg)

遥测数据流对开发人员和运维团队非常有益。然而，[可观测性](https://thenewstack.io/observability/)数据流是有成本的。一些大型客户每年在可观测性解决方案上花费数千万美元。根据可观测性提供商的不同，这些成本可能包括安全覆盖。

由于面临[减少支出](https://thenewstack.io/a-diy-framework-for-optimizing-observability-costs/)的压力，首席财务官和其他财务决策者正在日益严格地审查这种按需付费模式。因此，DevOps 团队被要求在[他们付费的遥测数据方面更加挑剔](https://thenewstack.io/whats-driving-the-rising-cost-of-observability/)，专注于可观测性和服务分析。

随着客户和组织需要更高级的功能，他们肯定不希望支付更多费用。相反，他们会寻找可观测性提供商可以通过更好的工具或实践来帮助他们降低成本的方法。

[Gartner](https://www.gartner.com/en) 分析师 [Mrudula Bangera](https://www.linkedin.com/in/mrudula-bangera-a4989933/), [Martin Caren](https://www.linkedin.com/in/mcaren/), [Matt Crossley](https://www.linkedin.com/in/matt-crossley-dk) 和 [Gregg Siegfried](https://www.linkedin.com/in/greggsiegfried/) 在 1 月份发布的一份报告中写道，遥测管道已经成为大型组织可观测性战略的关键组成部分，尤其是在需要聚合和处理来自多个来源的数据的情况下。

分析师写道：“遥测管道能够高效地收集、处理和交付此类遥测数据，包括[日志、指标和追踪](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/)。” “组织在考虑其关键职能领域时，应考虑遥测管道的需求、成本、价值和[投资回报率]。”

“同样值得考虑的是，从与主要可观测性平台相同的供应商处购买遥测管道可能存在的‘锁定’风险。”

## 更换供应商的风险

组织面临着好与坏的选择，而这些决定可能充满困难。使选择更具挑战性的是：可观测性选项、供应商和成本考虑因素的激增。

许多这些选项——例如选择用于可观测性和遥测数据收集的工具，特别是考虑到高昂的存储成本——被视为改善运营的方式。然而，成本始终是一个关键的考虑因素。

可观测性供应商提供智能解决方案，可增强洞察力、分析能力和许多其他好处。他们提供可以同时降低成本的工具和平台，例如，通过过滤掉对可观测性无用的不必要的遥测数据。

但是，即使这些供应商承诺降低这些组织的成本，更换供应商始终存在风险。

正如 Gartner 分析师所写，可观测性市场上有数十家供应商，组织在选择要实施的可观测性平台时，经常难以区分它们。越来越多的核心功能被商品化，供应商选择通过更高级别的功能（例如生成式 AI (GenAI) 辅助和成本优化）来区分。

Gartner 团队写道：“请谨慎关注组织在第一年不太可能采用的专业化和差异化层的功能领域。” “可观测性解决方案的高成本使得实现价值的时间至关重要，并且取消订阅未使用的功能可能代价高昂或不可能。”

## “存储所有数据”的终结

[Grafana Labs](https://grafana.com/) 的产品总监 [Jen Villa](https://www.linkedin.com/in/jevilla) 告诉 The New Stack，从历史上看，可观测性行业一直秉持着“存储所有数据”的心态。

Villa 说：“无论是指标、日志、追踪还是配置文件——尤其是在企业级公司中——每日数据收集量很容易超过数百万个指标序列和 PB 级的日志。”

“其核心是，‘存储所有数据’的方法旨在确保当出现问题时，团队可以访问所有内容，以便他们可以查明基础设施中发生故障的确切位置，”她说。“然而，随着基础设施变得越来越复杂和短暂，这变得越来越不可行；现在有太多的数据需要收集，而且成本巨大。”

“现代工具变得昂贵，因为它们仍然使用消防水带来装满水瓶，但真正的机会在于可以使用更少的数据检测威胁和问题的工具，同时保持有效性。”
> — J Stephen Kowski, SlashNext Email Security+

即使资金不是问题，收集如此庞大的数据也会在事件解决过程中产生“大海捞针”的问题，Villa说。“工程师在试图解决问题时，需要筛选大量数据，他们不知道从哪里开始——他们发现自己淹没在数据中，等待着必须解析大量数据的长时间运行的查询。”

因此，针对不断上涨的可观测性成本，Villa认为真正的问题是，“你真的需要所有这些数据吗？答案是不需要。

“你可以存储更少的数据，或者存储压缩程度更高的数据，仍然可以获得相同的结果。你不需要为了能力而牺牲成本。”

相反，Villa说，一个合适的解决方案应该基于效用（通过警报、仪表板或查询）来分析和分类信号，以自动优化低价值数据，通过聚合，有时可以为用户节省高达80%的成本。

她说：“原本需要开发人员花费数周时间才能完成的事情——清点所有收集的遥测数据并消除较低价值的部分——只需点击一个按钮即可实现。”

Villa说，一个合适的可观测性平台可以持续分析遥测数据，以便拥有最新的有用信息，而不是一次性的、手动的审计，“一旦完成，它基本上就过时了”。

她说：“组织更多地考虑的是长期投资，并选择能够长期为他们节省成本的平台，而不是仅仅想为可观测性工具支付更少的费用。”“他们在数据收集上节省的越多，他们就可以越多地再投资于可观测性的其他领域，包括他们可能尚未探索的新信号，例如[性能分析](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/)。”

Villa说，从“存储所有数据”转变为“智能存储”策略不仅是成本优化的未来，而且还可以帮助缩小数据堆的大小——从而更容易找到其中潜在的有害“针”。

## 数据收集：关注精确性

当然，组织的需求和要求差异很大。数据库存储公司与在线零售杂货店的可观测性需求不同。没有一种万能的方法，[J Stephen Kowski](https://www.linkedin.com/in/jstephenkowski)，SlashNext Email Security+的现场CTO告诉The New Stack。

Kowski说：“这不是非黑即白的；这会因公司而异。”“十年前的‘收集一切’的心态已经演变，因为聪明的组织现在专注于精确性：只收集最有意义的数据，并使用先进的人工智能来提取最大价值。

“现代工具变得昂贵，因为它们仍然使用消防水带来填充水瓶，但真正的机会在于那些可以用更少的数据检测威胁和问题的工具，同时保持有效性。这个领域的未来赢家将是那些通过关注高信号数据收集和智能分析，而不是仅仅收集更多数据来帮助客户优化成本的人。”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)