
<!--
title: 平台团队凭借快速胜利赢得开发者的青睐
cover: https://cdn.thenewstack.io/media/2024/07/e8e8e388-platformteamswinoverdevsquickwins2.jpg
-->

通过专注于快速胜利、度量和反馈循环，您可以在一周或更短的时间内为您的开发人员带来积极的影响。

> 译自 [Platform Teams Win Over Devs With Quick Wins](https://thenewstack.io/platform-teams-win-over-devs-with-quick-wins/)，作者 Steve Demchuk。

作为软件即服务 (SaaS) 初创公司产品负责人已有十多年，我一直很喜欢公司黑客马拉松的最后一天，每个人都会演示他们那一周的工作成果，并描述这些成果如何帮助客户、公司或他们自己。了解哪些努力吸引了整个企业的关注和赞扬，这很有趣。

让我告诉你，我只有一次在黑客马拉松演示后看到过全体起立鼓掌（现场和虚拟）。掌声是献给新成立的平台工程团队的，该团队旨在消除为构建和部署软件而构建可销售功能的团队所面临的阻力。

在黑客马拉松期间，这个平台团队审查了周期时间和性能指标，并发现我们的软件部署过程中存在持续的延迟。他们还创建了一个开发者体验 (DevEx) 调查，以收集我们 14 个工程团队中每个团队的定性反馈。根据这些数据，该团队优先考虑了三个能够改善 DevEx 且可以在五个工作日内发布的最佳行动。

在黑客马拉松演示中，该团队展示了流程、顶级开发者挑战以及他们实施的快速胜利平台变更——观众对此表示热烈赞赏。在一个星期内，他们证明了专注于体验的快速胜利如何导致开发效率和开发者幸福度指标的显著提升。平台团队真正以一种建立信任、透明度和成果的方式为他们的客户——我们公司的工程组织——服务。

平台团队的出现是 2024 年的一个熟悉的故事，行业报告证实，建立专门的平台团队仍然是各种规模的软件组织的当前优先事项，尽管人们发现整个行业的采用和实践还很不成熟。Gartner 预测，到 2026 年，大约 [80% 的软件工程公司可能会将平台团队纳入](https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering) 作为可重用服务、组件和应用程序交付工具的内部贡献者。今年 6 月，这家分析公司发布了第一版 [平台工程炒作周期](https://www.gartner.com/en/documents/5519995)。

平台策略正在使组织受益——[HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) 的 [2024 年云策略现状调查](https://www.hashicorp.com/state-of-the-cloud) 报告称，高成熟度组织将平台团队标准化，其可能性高出 2 倍。看到最大收益的现代组织已经采用自助式开发者平台来不断改善开发者体验、效率、质量和合规性。使开发者能够专注于业务逻辑的自动化，从而能够更快地交付对客户重要的工作，值得全体起立鼓掌。

继续阅读以了解一些可操作的投资和建议，以帮助组织在实现平台团队的全部潜力方面取得进展。从黑客马拉松的掌声中汲取灵感，我将重点关注可以快速实施的努力，以激发新的胜利，从而带来持久的信任和成功。

## 寻找提高采用率的机会

平台的成功与否取决于其采用率和持续使用率。平台团队可以在整个开发生命周期中承担大量不同的责任，从创建内部开发者平台 (IDP)、配置和配置资源、集中安全和合规性、管理部署管道以及简化操作和监控。

但是，投资旨在抓住开发者思想和心灵的快速胜利，是提高采用率的一种非常有效的方法。我亲眼目睹了概念验证 (PoC)、[最小可行产品 (MVP)](https://thenewstack.io/2-ways-to-accelerate-developer-productivity/) 或黑客马拉松如何创造长期的兴趣、兴奋、认可和使用率。

以下是一些平台投资类别示例，可以分析以寻找快速胜利：

### 自助服务

赋予开发人员直接访问、配置和管理资源的[自由](https://thenewstack.io/infrastructure-from-code-gives-ops-needed-freedom)，而无需依赖平台团队。在高价值决策和活动上进行协作，而不是在没有价值的关卡上进行协作。一个常见的起点是盘点当前可作为自助服务的开发人员平台功能，并确定缺少什么。更高级的考虑是将自动化软件添加到现有工作流程中，这些工作流程可以在每次修改时提取和记录基础设施运行时需求。

### 黄金路径

围绕开发环境、服务和配置提供护栏，以及围绕标记、日志记录和身份和访问管理 (IAM) 策略的最佳实践，以[提供一致的](https://thenewstack.io/nitric-and-the-rise-of-infrastructure-automation-in-platform-engineering/)、高质量的软件。评估高度使用的基础设施配置，并考虑创建[基础设施即代码 (IaC)](https://thenewstack.io/infrastructure-as-code/) 模板库和开发者门户——或者更进一步，直接从开发人员的代码中自动执行它们。

### 自动化

自动化例行任务，例如设置环境、配置 API 网关、配置云资源和部署应用程序。分析您的 CI/CD 管道以识别自动化可以改进的常见延迟或手动步骤。这使开发人员能够更多地专注于为业务需求编写代码。自动化部署流程以创建一致且快速的部署到测试和生产环境，并消除交付高质量软件的代价高昂的延迟和障碍。

### 本地开发

在本地模拟已批准的云环境，以允许开发人员快速调试和测试业务逻辑。在云开发中，经常听到开发人员抱怨部署周期过长，这极大地阻碍了他们快速编码、调试和部署的能力。缩短反馈周期会对生产力和 DevEx 产生巨大影响。此实验的关键是简单性：开发人员必须能够毫不费力地建立其本地环境，而不会过度干扰团队的其余部分。

以上这些投资都有一个共同点：它们有助于提高生产力和令人满意的 DevEx，这是平台成功采用的关键。让我们深入了解如何通过启用更快的创新和软件交付来识别快速的 DevEx 胜利。

## 尝试基础设施 DevEx PoC

我们的黑客马拉松平台团队展示了如何专注于开发人员重视的东西。开发人员希望流程和工具能够让他们保持高效和专注。

在我 [Nitric](https://nitric.io/) 的工作中，我经常听到云和基础设施的复杂性是影响开发人员生产力的最大问题。在许多组织中，IaC 和类似方法要求开发人员了解云基础设施提供商的不断发展，或者他们严重依赖与平台团队的沟通、职责分离和协调。这种摩擦会对 DevEx 产生重大影响，因此会影响采用率。

自动化基础设施配置和配置有助于开发人员快速采用新的工具和流程。平台团队可能会倾向于专注于治理、流程和监控，这些对于平台团队的价值至关重要。但是，持续检查和改进 DevEx 是促进您正在构建的平台采用的关键。

尝试围绕常见的平台监控工具创建一个 PoC，以评估对 DevEx 和结果的可能影响。PoC 应该在一个冲刺内完成。

例如，尝试使用正常运行时间监控工具来检查网站或服务的可用性。此解决方案很小，但仍然在云中正确配置起来比较复杂。它使用资源，例如 API 网关、计算、消息事件、计划任务和键值存储。

![](https://cdn.thenewstack.io/media/2024/07/594b8b43-uptime-monitoring-architecture-nitric.png)

此 [正常运行时间监控指南](https://nitric.io/docs/guides/nodejs/uptime) 是为您的组织实现快速胜利的绝佳起点。它提供了使用 Node.js 开发此应用程序的前端和后端的逐步说明。

![](https://cdn.thenewstack.io/media/2024/07/bcf97164-uptime-monitoring-dashboard-nitric.png)

该工具使开发人员能够：

- 使用他们喜欢的语言快速构建新应用程序。
- 立即使用平台团队管理的资源进行部署。

## 提升您的 DevEx 指标

如果您没有衡量投资的影响，您如何知道是否正在改善开发人员体验？正如黑客马拉松团队所做的那样，平台团队应该定期评估定量和定性指标的组合，以了解和改进开发人员交付的努力。

您开发人员的定性反馈可能已经存在于几个地方（例如，Slack、GitHub、Jira、经理一对一、公司调查）。为了建立信任，请分析您已经掌握的信息，以查找任何可操作的项目。为了提升水平，定期进行开发人员反馈调查，以收集有关痛点、工具满意度和整体体验的定性反馈。

除了定性反馈之外，请选择最相关且可用的定量指标进行分析。以下是一些我们发现有助于团队的测量示例。

- **开发人员满意度评分**：收集开发人员 CSAT（客户满意度）、NSAT（净满意度）或 NPS（净推荐值）评分，以衡量对开发系统和工具的整体满意度。
- **专注时间**：衡量平均每天的专注时间，以评估开发人员在不受干扰的情况下专注于工作的能力。
- **部署频率**：捕获和分析代码部署到生产环境的频率，以衡量开发过程的效率。
- **交付周期**：分析从代码提交到代码在生产环境中运行所需的时间，以评估开发管道的速度。
- **变更失败率**：衡量导致失败的部署百分比，以评估代码质量和测试有效性。
- **工具和实践的采用率**：创建历史分析，显示积极使用特定产品、服务或最佳实践的目标开发人员的百分比。
- **投资回报率 (ROI)**：量化收益（节省的时间、提高的生产力、减少的停机时间、更快的上市时间等）并确定成本（平台团队薪资、培训、工具、开销等）。ROI = ((收益 - 成本) / 成本) * 100。

在上下文中分析指标，以牢记全局。您越容易测量和分析，对 DevEx 的了解就越全面。然后，您可以根据开发人员社区的实际情况和期望条件开始对话并推动改进。

保持测量和迭代的一致性将赢得保持团队参与您努力所需的信任，但即使在本周采取一项小行动也将证明透明度和同理心。

## 专注行动，指明方向

我希望这篇文章能激发您下一个黑客马拉松、PoC 或 MVP，以加快您为开发人员带来积极影响的能力。优先考虑与开发人员想要改进或避免的内容直接相关的快速胜利。实施测量，以持续根据开发人员社区的反馈循环采取行动。并查看 [Nitric 的开源框架](https://nitric.io/docs) 和 [社区](https://nitric.io/chat)，以激发或加速您团队的下一个快速胜利。
