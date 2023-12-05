<!--
title: 不再是短期热潮，平台工程将长久存在
cover: https://cdn.thenewstack.io/media/2023/11/c3e23328-hype-1024x683.jpg
-->

最新报告显示，平台工程师薪酬水平持续上升，越来越多公司采用了平台工程最佳实践，同时 AI 在平台工程中的应用潜力逐渐显现。

> 译自 [The Hype Train Is Over. Platform Engineering Is Here to Stay](https://thenewstack.io/the-hype-train-is-over-platform-engineering-is-here-to-stay/)，作者 Carrie Tang。

官方消息，平台工程的热潮已经过去，平台工程已经成为新的常态。我们怎么知道这一点的呢？

其实，Humanitec的《[平台工程报告](https://thenewstack.io/platform-engineering-is-devops-evolved-new-report-shows/)》第一卷发表已经整整一年了。这清楚表明了一件事......

与平台工程社区团结一致，我们热切地迎来了《平台工程报告》第二卷的发布。激动吗？你应该会很激动才对。这篇论文不仅透露了社区的最新见解，比如平台工程师的薪资水平，还探讨了组织在多大程度上遵循了平台工程最佳实践以及为什么你需要一个参考架构等相关话题。

这篇报告还深入探讨了一些关键问题和更宏观的思考，比如现在就是开始考虑 AI 在[平台工程](https://thenewstack.io/platform-engineering/)中的[未来作用](https://thenewstack.io/ai/)的时候了。所有这些都支持了平台工程确实已经到来并会持续发展的观点。

准备好了解它具体是如何实现的了吗？让我们深入探讨一下。

## 第一卷之后的情况

在过去的12个月里，平台工程见证了惊人的增长。距离第一次 PlatformCon 2022举办仅一年，它就吸引了超过6，000名与会者。而PlatformCon 2023则吸引了超过[22，000名与会者](https://platformengineering.org/blog/platformcon-2023-highlights)，获得了27个赞助商的支持，并举办了横跨5个新讨论轨道的169场演讲。如今，Platform Engineering YouTube 频道已经拥有近16，000的订阅者，其 Slack 频道的订阅者数量也差不多。

这种前所未有的增长伴随着业界认可度的不断提高。8月份，平台工程进入了 [Gartner 软件工程炒作周期](https://www.gartner.com/en/documents/4590099)的“夸张期待峰值”。这意味着它被视为一项创新，显示出产品使用量的增加，但仍有更多的宣传而不是实际证明了它能提供价值。

从工具的角度来看，[Thoughtworks 技术雷达第 29 卷](https://www.thoughtworks.com/radar/techniques/platform-orchestration)最近将平台编排识别为一种技术和新一代工具，它超越了传统的平台即服务(PaaS)模型。根据 Thoughtworks 的说法，像 Humanitec 平台编排器这样的工具在允许开发者通过配置实现自助服务访问变体的同时，也执行了组织的标准。

![](https://cdn.thenewstack.io/media/2023/11/6931cacb-image2a.png)

就平台工程的增长而言，这只是一个开始。平台工程社区驱动的研讨会、聚会和活动也在增加。我们很高兴看到越来越多的内部开发者平台(IDP)被用来帮助企业加速创新周期，打破上市时间等关键业务指标。

## 平台工程世界一览

Syntasso 在 2023 年 4 月制定的第一个[平台成熟度模型](https://www.syntasso.io/post/syntasso-donates-first-version-of-platform-maturity-model-to-cncf-working-group)启发了平台工程社区，以进一步了解组织遵循平台工程最佳实践的程度。因此，[2023 年平台工程调查](https://platformengineering.org/blog/results-are-in-the-2023-platform-engineering-survey)由社区创建和针对社区，收集了 296 人的反馈。结果显示，许多组织仍然难以运用平台工程最佳实践。

例如，大多数(64%)的受访者没有变更管理流程。只有 38.1% 拥有经费充足的平台团队，并在自身与开发组织之间有明确的职责划分。仅有不到三分之一(32.3%)的受访者遵循“平台即产品”的方法。

尽管展示工程组织需要改进的地方和方式很重要，但随着平台工程的发展，同样重要的是我们要了解平台工程师这个实际角色的样子。为此，平台工程社区再次求助于社区。

2023年平台工程调查主要在美国和欧洲展开，以收集尽可能多的数据。该报告为我们提供了有价值的见解，揭示了平台工程师的收入、工作生活的样子以及谁实际上是平台工程师。

## 平台工程师与 DevOps 工程师的薪资差距

调查的一个关键发现是，美国的平台工程师平均比 DevOps 工程师多赚 42.5%(65，439 美元)。在欧洲，工资差距较小但仍很常见，平台工程师的平均薪资比他们的 DevOps 同事高 18.64%(15，871 美元)。这种差异可能反映了担任平台工程师所需的更宽广或更专业的技能组合。

![](https://cdn.thenewstack.io/media/2023/11/6d6d68a2-image4a.png)

注：汇总的数据基于受访者“工作内容”的描述。平台工程是平台工程和开发者体验的汇总。DevOps 是基础设施、DevOps 设置和运维的汇总。

## 参考架构：将您与 IDP 拉近

这份报告不仅揭示了平台工程师这个角色的样子，还探讨了团队当今面临的最大和最耗时的挑战之一。在设计 IDP 时，如何从众多可用工具中选择？如何以有意义的方式将它们组合在一起，以确保它们定制适合您组织的需求？

虽然 IDP 的实现各不相同，但常见模式确实存在。受 [McKinsey 在 2023 年 PlatformCon 大会上的演讲](https://youtu.be/AimSwK8Mw-U)启发，我在 Humanitec 的团队根据[基于 AWS、Azure 和 GCP 设置创建了 IDP 参考架构](https://humanitec.com/reference-architectures)，其中汇聚了数百个真实设置中的模式。最近，参考架构(基于 AWS 和 GCP)的实现代码已经开源，这使团队能够加快 IDP 设计流程，并在短短 1 小时内而不是几个月内轻松构建最小可行产品(MVP)。 此外，还开发了新的学习路径，以帮助组织掌握其 IDP：

- [AWS 开源参考架构](https://github.com/humanitec-architecture/reference-architecture-aws)
- [GCP 开源参考架构](https://github.com/humanitec-architecture/reference-architecture-gcp)
- [IDP 学习路径](https://developer.humanitec.com/training/master-your-internal-developer-platform/introduction/)

## 为什么现在需要考虑 AI？

那么，平台工程的前景是什么？根据该报告，我们应该关注大型语言模型(LLM)如何[使平台团队能够构建](https://platformengineering.org/blog/ai-is-changing-the-future-of-platform-engineering-are-you-ready)更有效的 IDP。LLM 的用例已经很明显，展示了组织如何以标准化的方式自动化重复任务。这就是为什么现在是开始考虑 AI 和 LLM 对您意味着什么的时候了。这种技术对您有多大用处？它将如何影响您的角色？虽然该技术还有很长的路要走，但是否存在 LLM 完全接手您的工作的可能性？或者人为因素始终是必要的。无论如何，这需要您的重视。

为了抢占先机，该报告包含了下表，其中阐述了一些潜在的 LLM 平台工程用例。哪些适用于您？哪些易于实现，哪些难以实现？

![](https://cdn.thenewstack.io/media/2023/11/c7d0569e-image5a.png)

其中一些用例是低悬果实，可以独立部署或与第三方合作轻松部署。至少 95% 的情况下，它们在几周内就可靠运行。其他用例的实现更加困难，需要专业的 LLM 技能，并且需要更长的时间才能变得可靠。

LLM 即将改变我们所知的技术，AI 已经出现在每个 Gartner 炒作周期图的每个象限中。潜在的平台工程影响就是数十篇文章的主题。但它是否已经被积极使用了呢？根据最新的 [2023 年平台工程调查](https://platformengineering.org/blog/results-are-in-the-2023-platform-engineering-survey)，AI 的炒作声尚未被平台工程师在日常工作中充分实现。

![](https://cdn.thenewstack.io/media/2023/11/16390af7-image6a.png)

## 平台工程的未来一片光明

可以肯定地说，平台工程已经过了炒作阶段。作为一门学科，它有望持续下去，其目标是设计和交付有效的企业级 IDP。这门学科有望解决当今软件工程组织面临的一些最大挑战，例如阻碍开发者生产力和增加认知负载的复杂云原生环境。通过在设计中确保标准化、实现[真正的开发者自助服务和消除工单运维](https://thenewstack.io/how-static-config-management-kills-developer-productivity/)，IDP 可以改造软件交付。通过《平台工程现状》等报告，我们可以继续就关键平台工程主题提供指导和宝贵见解。点此下载完整报告以了解更多信息。

