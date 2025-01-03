
<!--
title: Heroku将12 factor应用迁移到开源。下一步是什么？
cover: https://cdn.thenewstack.io/media/2025/01/b4f717e5-kccnc-na-24_gail-frederick_featured.png
-->

Salesforce 的 Gail Frederick 在《The New Stack Makers》的这一集中表示，Heroku 迁移该项目的原因是为了获得更新帮助，该项目是一种构建可移植、弹性应用程序的方法。

> 译自 [Heroku Moved Twelve-Factor Apps to Open Source. What’s Next?](https://thenewstack.io/heroku-moved-twelve-factor-apps-to-open-source-whats-next/)，作者 Heather Joslyn。

盐湖城——11月，[Heroku](https://www.heroku.com/?utm_content=inline+mention) 宣布已将开发方法论 [12 factor应用](https://github.com/twelve-factor/twelve-factor) 开源。该公司创建了这种方法来帮助开发人员在本地开发应用程序，“将其跨云提供商进行可移植打包，然后使其能够弹性运行，并使其成为令人愉悦的构建体验，”Heroku 的首席技术官在《The New Stack Makers》的这一集中说道。

Heroku 为什么会迁移这个项目？Frederick 说，是为了让社区参与更新。

Heroku 创始人于 2011 年撰写了 [12 factor](https://thenewstack.io/learn-12-factor-apps-before-kubernetes/)，13 年后，虽然这些要素启发了一代云开发人员，但也有一些方面已经过时，而这些正是我们在开源发布后希望更新的方面，”她在本集（在 [KubeCon + CloudNativeCon 北美峰会](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)录制）中告诉 TNS 创始人兼出版人主持人。

Heroku 记录的“12 factor”是基于该公司观察到的客户在构建应用程序时常犯的错误。但十多年在科技领域是一段很长的时间。Frederick 描述了该方法论中需要更新的一些领域。

例如，“[12 factor]宣言谈到了日志并将日志视为事件流，”她说。“从那时起，[云原生开发](https://thenewstack.io/cloud-native/) 中发生的变化是，开发人员需要指标，各种各样的指标来自他们的应用程序，而不仅仅是文本日志或数据格式日志。”

新的开源12 factor应用中可能的变化将是“专门更新该要素以转换为遥测，并确定应用程序应发出哪些指标的最佳实践，然后如何将它们移动到所需的任何可视化工具中。”

[OpenTelemetry](https://thenewstack.io/observability-in-2025-opentelemetry-and-ai-to-fill-in-gaps/) 的日益普及可能是现代化该方法论这一部分的一个因素。

## 参考架构示例

在 Makers 录制时，Frederick 说，12 factor团队花了大约三个月的时间与当前维护者交谈，以确定需要做什么来更新该方法论。她说，对遥测的关注是这些讨论中得出的一个结果。

她说：“我们也都认识到，云原生开发人员不再只部署一个应用程序了。”“他们一起部署一个由多个后端存储组成的应用程序系统。12 factor非常清楚地说明了一个应用程序与后端服务和数据存储，而这并不是当今云中应用程序开发人员的现实情况。”

展望未来，Frederick 说，她相信12 factor应用程序项目的维护者“将添加包含有关如何实现某个要素的详细信息的支持文档。我们将提供[参考架构](https://thenewstack.io/reference-architectures-and-experience-kits-for-cloud-native/)。我们将提供一个作为要素实际应用示例的代码。我甚至认为 Heroku 平台是所有要素的参考架构。”

如何衡量成功？“我认为，只有在我们结合了包括边缘、[物联网]、无服务器，甚至包括你不会认为是云原生的重量级分布式系统在内的应用程序开发用例时，我们的工作才足以更新12 factor。”

查看完整剧集，了解更多关于开源12 factor应用和 Heroku 的未来信息。
