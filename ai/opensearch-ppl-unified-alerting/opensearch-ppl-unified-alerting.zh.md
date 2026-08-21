**OpenSearch 是 Linux 基金会旗下的顶级开源项目**，由 Amazon Web Services 及其他知名厂商提供支持。OpenSearch 可观测性堆栈在一个开源、原生支持 OpenTelemetry 的平台中集成了 AI 代理追踪、APM、服务拓扑图、日志、指标和仪表板，并内置了机器学习驱动的异常检测和全新的管道处理语言（PPL）。

9 月 10 日，[AWS OpenSearch](https://aws.amazon.com/what-is/opensearch/) 的高级产品经理 [Joshua Bright](https://www.linkedin.com/in/joshua-bright-9411022/) 将为负责大规模可观测性的站点可靠性工程师（SRE）和平台工程师带来一场深度技术讲解，在这些场景中，告警通常是最先出现问题的环节。

## **立即注册**

SRE 并不缺乏遥测数据。问题在于，用于处理这些数据的工具没有跟上步伐，随着 AI 代理为团队现有的监控系统增加了大量高频信号，这一差距正在进一步扩大。Linux 基金会[报道](https://www.linuxfoundation.org/press/opensearchcon-north-america-2026-to-showcase-five-years-of-innovation-powering-enterprise-search-observability-and-analytics)称，77% 的组织已将 [OpenSearch](https://opensearch.org/) 视为其 AI 基础设施的核心或支持组件，代理追踪正是原因之一。

专为简单阈值设计的查询语言难以处理多信号关联，告警规则散落在不互通的工具中，导致值班工程师花费大量时间处理误报，而非调查实际事故。

为了缩小这一差距，OpenSearch 团队推出了两项新功能：用于告警的管道处理语言（PPL）和统一的告警管理器。

PPL 将熟悉的 Unix 管道模型引入到可观测性查询中，允许工程师使用可读的语法对日志、指标和追踪进行过滤、转换和关联。

通过像在终端中一样串联步骤，PPL 允许团队构建多步骤的告警条件，从而发现微妙的故障模式。例如，只有在日志错误率同时升高时，AI 代理工具调用的延迟激增才变得具有可操作性。由于 PPL 技能可直接应用于搜索、分析和告警工作负载，以往那些难以维护的复杂条件现在变得简单明了，且易于传达给团队成员。

## **集中式告警路由与 Apache 2.0 许可**

除了 PPL，新的告警管理器还为团队提供了一个集中式界面，用于管理告警规则、路由、抑制和升级，从而使纸面上的策略与团队实际响应事故的方式保持一致。本次网络研讨会涵盖的所有内容均在 Apache 2.0 许可下发布，且无任何功能限制。

[**加入我们：9 月 10 日，星期四 – 立即注册**](https://thenewstack.io/webinar/smarter-alerting-at-scale-live-opensearch-demo-on-ppl-unified-alerting/)

本次会议将演示在真实可观测性工作负载下如何使用这两项功能，并包含开放式问答环节，请准备好您关于告警的问题，与 Amazon 团队交流。[立即注册](https://thenewstack.io/webinar/smarter-alerting-at-scale-live-opensearch-demo-on-ppl-unified-alerting/)，锁定 9 月 10 日（星期四）美东时间中午 12 点/太平洋时间上午 9 点的席位。