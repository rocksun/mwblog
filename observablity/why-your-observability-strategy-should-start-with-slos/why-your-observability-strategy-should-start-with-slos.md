
<!--
title: 可观测性策略，为何应从SLO开始？
cover: https://cdn.thenewstack.io/media/2025/11/cc0913a5-observability-use-2.jpg
summary: 可观测性应简化，赋能非技术用户。SLO应为起点，聚焦业务价值。Chronosphere致力降低成本，简化日志，但实现全面普及仍存挑战。
-->

可观测性应简化，赋能非技术用户。SLO应为起点，聚焦业务价值。Chronosphere致力降低成本，简化日志，但实现全面普及仍存挑战。

> 译自：[Why Your Observability Strategy Should Start With SLOs](https://thenewstack.io/why-your-observability-strategy-should-start-with-slos/)
> 
> 作者：B. Cameron Gain

可观测性平台通常需要高度熟练的专业人员才能理解和使用这些平台。理想情况下，非技术型利益相关者将依赖监控，理解问题或优化以做出决策，然后依赖平台完成其余工作。对于调试，AI引导的问题解决器会检测、更新并修复问题，并以非技术用户能够理解的方式阐明情况。

Chronosphere 的现场CTO [Bill Hineline](https://www.linkedin.com/in/billhineline) 最近告诉我，可观测性提供商有责任提供能够用于实现业务目标并阻止业务灾难的无缝指标。这并非新闻，但简化可观测性而不降低其水准的需求，无论如何强调都不为过。

但他也表示，非技术型利益相关者有责任尽快学习如何解读这些指标。*这*是一个令人耳目一新的观点。

另一个令人耳目一新的观点是：定义[服务级别目标 (SLO)](https://thenewstack.io/sre-fundamentals-differences-between-sli-vs-slo-vs-sla/)，这通常是可观测性策略的最后一步，应该成为第一步。

如果工具过于复杂，可观测性工具就无法广泛普及，但许多供应商却忘记了这一点。可观测性提供商谈论他们为指标、日志和追踪提供的附加功能，假设实际用户或潜在采用者知道他们在说什么，但情况并非总是如此。

即使在CTO层面，用户也可能难以理解其平台如何工作以及如何解读数据——而这些人往往是批准为开发人员和运维工程师，以及他们组织中所有利益相关者购买工具的人。

可观测性提供商经常会说：“我们有一种新的聚合日志或追踪等数据的方式。”但这到底意味着什么？它如何解决[系统宕机](https://thenewstack.io/6-scary-outage-stories-from-ctos/)并导致组织蒙受巨大经济损失的问题？

## 让非技术用户也能使用可观测性

Hineline表示，任何可观测性策略的关键要求都应该是易于广泛受众使用，从经验丰富的工程师到非技术的产品经理。有效的工具必须“开箱即用”地提供洞察力，而无需用户构建数百个仪表板。它应该像智能手机一样直观：即开即用，但也能自定义。

Hineline说，这种可访问性使非专业人士能够得出有价值的结论。

例如，他说，产品经理不需要成为“技术大师”也能看出转化率突然下降、应用程序错误率飙升以及几分钟前发布的新软件之间的关联。他们可以形成一个简单的假设，因为平台呈现清晰、相关的数据点，而没有不必要指标的干扰。

Hineline说，这一原则在美联航的一次关键故障中得到了验证，当时一个导致航班停飞的应用程序被实时监测。一名刚加入该公司几天、对应用程序内部运作一无所知的销售工程师，成功找到了根本原因并解决了问题。

这次经历带来了一个关键的认识：目标是让人们成为工具的专家，而不是公司复杂系统中每个相互关联部分的专家。Hineline说，当工具足够强大和直观时，它就能使问题解决民主化，打破知识壁垒，最终为业务带来更好、更快的结果。

他说，最有效的可观测性实施，不是从“我们可以收集什么数据？”开始，而是从“对我们的业务来说，什么才是好的？”开始。可观测性的目的是确保技术按预期支持业务。这意味着将技术性能直接与业务成果联系起来。例如，他说，如果一个电子商务网站的用户体验比竞争对手慢，这是一个切实可行的业务问题。

## 从SLO开始限制数据收集

这种以业务为中心的思维方式自然而然地引向了SLO的定义，Hineline认为SLO应该成为一个组织可观测性之旅的起点。

从SLO开始提供了关于收集哪些数据的“指导方针”。团队可以从一个简单而强大的基础开始，基于对业务重要的信号，如响应时间、错误率和饱和度，而不是收集所有数据。Hineline说，这种专注的方法不仅能提供即时洞察，还能[减轻成本担忧](https://thenewstack.io/observability-can-get-expensive-heres-how-to-trim-costs/)，正是这些担忧让组织对可观测性“望而却步”。

行业的一个核心问题是“收集一切”的商业模式。Hineline说，随着公司“超大规模发展，数据量变得巨大，因此成本也成为一个因素”。他补充说，这使得焦点转向“衡量价值”和理解“遥测数据给我带来的价值，以确保我正在收集正确的东西。”

他说，Chronosphere最大的不同之处之一是“将控制权交还给客户，让他们了解他们放入平台的遥测数据和日志的价值究竟为他们带来了什么”。

Hineline说，这解决了开发人员倾向于收集“一切”的问题。该平台提供了“元数据，用以说明，‘好的，我知道您想要5000个指标。您正在使用100个。’”

## 将可观测性与切实的业务需求联系起来

Hineline的观察与高德纳（Gartner）关于可观测性现状的报告相互印证。在高德纳分析师 [Martin Caren](https://www.linkedin.com/in/mcaren)、[Gregg Siegfried](https://www.linkedin.com/in/greggsiegfried/)、[Matt Crossley](https://www.gartner.com/en/experts/matt-crossley) 和 [Mrudula Bangera](https://www.linkedin.com/in/mrudula-bangera/) 在[今年1月发布的一份报告](https://www.gartner.com/en/documents/6064663)中，绝大多数成功采用的用例将取决于满足切实的、可衡量的业务需求。

根据高德纳的报告，到2027年，80%成功应用可观测性的组织将缩短决策延迟，从而为其目标业务或IT流程带来竞争优势。

组织通常清楚地认识到适当的可观测性所能提供的必要性和好处。然而，他们对成本增加的担忧是可以理解的，特别是当同时考虑到不断上涨的云和其他成本时。

高德纳分析师写道，日志监控通常是组织了解其系统健康和性能的起点。

高德纳报告指出：“尽管日志通常是人类可读的文本格式，但这也使其对机器来说成为挑战，并且移动、处理和存储成本高昂。”“每天操作超过1TB日志的组织将需要探索遥测管道（差异化层）来管理这些问题。”

## 一个实际例子：Chronosphere Logs 的实际应用

[![](https://cdn.thenewstack.io/media/2025/09/32be332b-screenshot-2025-09-26-at-12.35.33%E2%80%AFpm-1024x581.png)](https://cdn.thenewstack.io/media/2025/09/32be332b-screenshot-2025-09-26-at-12.35.33%E2%80%AFpm-1024x581.png) Chronosphere Logs 助您查找虚拟机的问题所在。

今年6月，Chronosphere 推出了 Logs 2.0。该公司声称，通过它，组织可以缩短恢复时间，并更轻松地优化运营和调试。

尽管我的分析公司 ReveCom 尚未测试和分析此版本，但我们已经观看了 Chronosphere [Logs 的演示](https://www.youtube.com/watch?v=cMGPZ49vuS8)。在演示中，展示了使用新发布的日志功能进行故障排除的阶段。演示强调了 Chronosphere 如何解决其通过日志数据识别出的内部问题。

在演示中，Chronosphere 的软件工程师 [Jerome Froelich](https://www.linkedin.com/in/jerome-froelich-466730a0/) 描述了当指标摄取服务的 P99 延迟增加时，Chronosphere 平台是如何使用的。虽然所涉及的服务看起来很健康，但调查转向了用于路由边缘流量的代理。

Froelich 说，一个特定代理实例的指标与其他实例不同。当查看该代理的日志时，发现云提供商对该实例运行的虚拟机执行了实时迁移。

在这种情况下，虚拟机以降级状态恢复。Froelich 说，将其从集群中移除后，观察到的延迟恢复正常。“以前，调试此类问题需要从多个不同来源拼凑信息。现在，信息可以在单一视图中获取。”

## 简化可观测性面临的持续挑战

通过缩小规模和筛选指标以满足用户需求来降低成本，而不是简单地打开所有数据的闸门，这绝对不是一个好主意，而且代价高昂。而 Chronosphere 至少看来正在认真尝试做到这一点，并简化可观测性过程以实现上述目标。

当然，这也是我们最近报道的其他可观测性提供商的理念——[Chronosphere](https://thenewstack.io/taming-ai-observability-control-is-the-key-to-success/)，以及 [Grafana Labs](https://thenewstack.io/grafanas-cto-on-the-state-of-the-observability-market/)、[Kloudfuse](https://thenewstack.io/kloudfuse-3-0-an-all-in-one-observability-platform-emerges/)、[WanAware](https://thenewstack.io/wanaware-21-packets-affordable-observability-play/) 等。

目前，正确地实施和利用可观测性仍然是一个困难的过程，学习曲线陡峭——尽管供应商声称并非如此。尽管提供商显然意识到了这一挑战，并且看到他们能带来什么令人兴奋，但在短期内，不要指望解决方案能让用户以一种非常易于访问的方式获取他们需要了解的关于其应用程序和网络的一切信息。

但惊喜确实会发生。