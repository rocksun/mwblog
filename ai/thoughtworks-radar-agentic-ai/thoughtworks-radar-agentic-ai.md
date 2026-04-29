<!--
title: 为什么 AI 工程需要回归传统工程纪律
cover: https://cdn.thenewstack.io/media/2026/04/95fce3b8-for-thumbnail-2.png
summary: Thoughtworks 专家 Nimisha Asthagiri 指出，AI 项目落地难源于缺乏工程纪律。她强调需重拾 TDD、零信任等传统规范以抵消 AI 复杂性，并提出了处理 AI 生成代码的“暗码”与临时软件概念。
-->

Thoughtworks 专家 Nimisha Asthagiri 指出，AI 项目落地难源于缺乏工程纪律。她强调需重拾 TDD、零信任等传统规范以抵消 AI 复杂性，并提出了处理 AI 生成代码的“暗码”与临时软件概念。

> 译自：[Why AI engineering needs old-school discipline](https://thenewstack.io/thoughtworks-radar-agentic-ai/)
> 
> 作者：Frederic Lardinois

在本期《The New Stack Makers》节目中，我们与 Thoughtworks 的数据与 AI 顾问 [Nimisha Asthagiri](https://www.linkedin.com/in/nasthagiri/) 坐下来聊了聊：为什么这么多公司在将 AI 项目从概念验证（PoC）转向生产环境时感到吃力，以及最新一期的《Thoughtworks 技术雷达》揭示了行业走向何方。

VIDEO

> “我们经常听到高管们问：如何才能更快？我认为正确的问题应该是：基于最新技术，我们能构建哪些以前无法实现的东西？”

在这一集中，我们讨论了智能体 AI（Agentic AI）从 PoC 到生产之间的鸿沟，为什么测试驱动开发（TDD）和变异测试等工程基础正在回归，以及一个挑衅性的观点：AI 生成的大部分代码可能根本不需要存在。

## 从 PoC 到生产的鸿沟

Gartner 预测，到 2027 年底，超过 40% 的智能体 AI 项目将被取消，Asthagiri 在 Thoughtworks 观察到的模式与这一预测相吻合。部分原因是，在 2022 年生成式 AI 爆发后，企业经历了一波概念验证项目的浪潮。现在，许多公司正困于如何将这些实验转化为生产力。

在 Asthagiri 看来，问题的根源在于高管们提出的问题。“我们经常从高管和其他人那里听到这样的问题：我们如何走得更快？我们如何保持竞争力？”她告诉 *The New Stack*。“我认为正确的问题——或者说另一个更好的替代问题——应该是：基于最新技术，我们能构建哪些以前无法实现的东西？”

与其将 AI 强行嫁接到现有的工作流程中，成功的公司正在重新思考这项技术究竟能赋能什么。Asthagiri 认为，这是一种系统思考的论点。

当被问及成功的公司有什么共同点时，她指出的不是工具，而是组织投入：“那些成功的公司都在做尽职调查。这是一项艰苦的工作，但它关乎组织内部人员的素养提升和赋能。”

## 工程基础回归

最新一期的《Thoughtworks 技术雷达》指出，行业在前进之前需要先回头看。雷达警告称，AI 产出的内容与开发者对自己代码库的实际理解之间差距正在扩大，这会导致[认知债务](https://www.thoughtworks.com/en-us/radar/techniques/codebase-cognitive-debt?utm_source=publisher-direct-TNS&utm_medium=digital-advertising&utm_campaign=sai_tsi_rp-gl-pspt_techradar_2026-04)的堆积。

Asthagiri 是编写该雷达的全球团队成员之一。Thoughtworks 的观点是：随着如此多的 AI 工具和开源项目上线，没有人能评估所有工具。在这种情况下，审慎的做法是重新审视许多成熟的技术——这并非出于怀旧，而是作为一种必要的抗衡力量，去应对 AI 工具生成复杂性的速度。

Asthagiri 指出，测试驱动开发（TDD）、变异测试、DORA 指标和零信任安全架构等实践需要重新回到前台。“很多关于工程纪律的传统、基础的思考方式，现在真的重新回到了最前沿，”她说。

随着自主编程智能体越来越多地编写生产代码，反馈回路变得比以往任何时候都重要。正如 Asthagiri 所言：“那些反馈传感器是什么？除了你为智能体提供的上下文输入（feed-forward）之外，通过传感器、测试、静态代码检查工具（linters）以及许多通用实践得到的反馈又是怎样的？”

同样的逻辑也适用于安全。随着智能体在开发者工作站中激增，身份层现在需要同时考虑机器智能体和人类。Asthagiri 表示，零信任架构对于“能够了解谁做了什么，以及对正在进行的工作进行身份验证和授权”至关重要。

如今，这些智能体通常作为更大团队的一部分工作。Asthagiri 看到组织正倾向于有意设计的多智能体设置，拥有针对后端、前端和其他领域的特定角色智能体——但由人类进行编排。

## 暗码与临时软件的必要性

当我们问及 Asthagiri 关于 AI 生成代码的庞大数量及其造成的下游瓶颈时，她指出，应对措施不应该是更好的审查工具。相反，组织应该询问这些代码是否从一开始就有必要存在。

“将会产生大量的暗码（dark code），”她借用了“暗数据”的概念——即组织收集但从未实际使用的信息。“因为代码将成为一种低成本生成的商品，你并不一定需要保留它。”

她将这一观点拆分为两个想法。首先，组织需要明确代码的生命周期。PoC 代码应记录失效日期，并在架构上进行隔离，以便在不再需要时将其删除。

其次，某些代码应该是临时生成的，仅为单次使用而创建，然后丢弃。“如果我没有相应的智能体技能，而且它不是一个必须复用的功能，那为什么不直接为那个特定的单次用途动态生成它，然后就结束了呢？”

这与雷达团队称为[编程智能体的沙箱化执行](https://www.thoughtworks.com/en-us/radar/techniques/sandboxed-execution-for-coding-agents?utm_source=publisher-direct-TNS&utm_medium=digital-advertising&utm_campaign=sai_tsi_rp-gl-pspt_techradar_2026-04)的技术有关，该技术允许“在受限的文件系统访问、受控的网络连接和有限的资源使用等隔离环境中运行智能体”。

你可以在这里探索完整的《Thoughtworks 技术雷达》：[thoughtworks.com/radar](https://www.thoughtworks.com/radar?utm_source=publisher-direct-TNS&utm_medium=digital-advertising&utm_campaign=sai_tsi_rp-gl-pspt_techradar_2026-04)。