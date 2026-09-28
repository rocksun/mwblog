<!--
title: Cursor收购Firetiger一个月后，推出追踪代码至生产环境的Bot
cover: https://cdn.thenewstack.io/media/2026/09/e68a789e-public-domain-vectors-7pbb4kw8wyc-unsplash.jpg
summary: Cursor在收购Firetiger一个月后推出了全新智能体Rollouts和升级版的Security Reviewer。Rollouts能够追踪代码变更进入生产环境并监控其行为，旨在解决AI时代写代码变快但部署与验证风险依然存在的行业痛点。
-->

Cursor在收购Firetiger一个月后推出了全新智能体Rollouts和升级版的Security Reviewer。Rollouts能够追踪代码变更进入生产环境并监控其行为，旨在解决AI时代写代码变快但部署与验证风险依然存在的行业痛点。

> 译自：[Cursor acquired Firetiger. A month later, Cursor launched a bot that tracks code changes through to production.](https://thenewstack.io/cursor-rollouts-firetiger-production/)
> 
> 作者：Paul Sawers

我们都知道，由于AI编码工具和代理的普及，生成代码比以往任何时候都更容易。毫无疑问，更困难的部分出现在代码编写*之后*：确保更改安全上线、发现生产环境中的回归问题，以及弄清楚哪里出了问题。

这就是为什么Cursor推出了[Rollouts](https://cursor.com/changelog/rollouts-and-security-reviewer)，这是一个全新的智能体，能够追踪代码更改进入生产环境，并监控其行为是否符合预期。

## Firetiger效应

这一宣布距离SpaceX[完成其大笔收购](https://x.com/cursor_ai/status/2088249881718919393)以60亿美元收购Cursor过去了一个多月，这笔交易让这家AI编码公司在开发自己的模型时能够使用SpaceX庞大的GPU基础设施。

然而，就在该交易完成的前一天，Cursor悄然[宣布了它自己的收购](https://cursor.com/blog/firetiger)：它吞下了[Firetiger](https://www.firetiger.com/)背后的团队，这是一家成立三年的初创公司，致力于构建从拉取请求（PR）到部署全流程监控软件变更的AI智能体。

当时，Firetiger的联合创始人兼CEO [Rustam Lalkaka](https://www.linkedin.com/in/lalkaka/)指出，编码智能体大幅减少了创建软件变更所需的工作量，但在降低实际部署这些变更所涉及的风险方面却收效甚微。

“在过去的两年里，代理式编码极大地改变了软件，”Lalkaka在交易宣布后的LinkedIn[动态中](https://www.linkedin.com/feed/update/urn:li:activity:7493743431840673793/)写道。“创建变更的成本已经降至接近于零。而部署它们的成本和风险在很大程度上保持不变。”

> “编写代码不再是缓慢的部分。没有加速的是PR提交之后的一切：确保代码安全、观察部署、判断延迟激增是否真实存在、弄清楚11个更改中到底是哪一个破坏了结账功能。”
>
> Rustam Lalkaka, Cursor

快进到今天，已经加入Cursor的Lalkaka公布了这次收购的首批成果——包括Rollouts。Lalkaka在周三发布的一篇[博客文章](https://cursor.com/blog/rollouts-and-security-reviewer)中指出，这个新智能体（或公司所称的“Bot”）旨在帮助开发者“更快地将安全、可靠的代码投入生产”。

“编写代码不再是缓慢的部分，”Lalkaka写道。“没有加速的是PR提交之后的一切：确保代码安全、观察部署、判断延迟激增是否真实存在、弄清楚11个更改中到底是哪一个破坏了结账功能。”

Rollouts实际上是Firetiger的变更监视器（Change Monitors）在Cursor内部的重生，使用一个被称为*Bot Development Kit*的工具进行了重建。这个工具包似乎也是Cursor的新产品：一个用于构建和提供Cursor Bot及智能体的早期阶段框架，作为npm上的`@cursor/bdk`[包发布](https://www.npmjs.com/package/%40cursor/bdk)。其文档称，开发者可以使用Markdown和TypeScript定义智能体，并支持工具、技能、子智能体、网络钩子（webhooks）和定时运行。

与之前的变更监视器一样，Rollouts从拉取请求打开时开始工作。它检查拟议的代码更改，计算出哪些系统可能受到影响，并制定一个监控计划，涵盖该更改应该做什么、它看到的风险、它打算监视的信号，以及可用仪器中的任何漏洞。在代码到达生产环境之前，开发者可以审查和编辑该计划。

![Rollouts运行中 (1)](https://cdn.thenewstack.io/media/2026/09/e009ed6c-gif1.gif)

*Rollouts为变更生成监控计划*

一旦更改部署完毕，Rollouts就会对照该计划检查产生的遥测数据——包括日志、指标和追踪。暂存环境（staging）和生产环境会被独立评估，每次部署最终会收到三个判定结果之一：验证健康、检测到回归或不确定。

这意味着，例如，一个更改可以在暂存环境中通过检查，随后当同一代码到达生产环境时，Rollouts却发现了问题。

![Rollouts运行中 (2)](https://cdn.thenewstack.io/media/2026/09/d24a9950-gif2.gif)

*Rollouts随着更改上线报告部署状态*

如果Rollouts*确实*检测到了回归，它可以识别出它怀疑的更改，向负责的开发者发出警报，并且根据其配置方式，要么打开一个用于审查的回滚PR，要么将问题交给Cursor云智能体尝试修复。目前，在这一循环的关键部分仍然有人类的参与：Rollouts不会自己合并修复或回滚部署，尽管它可以暂停渐进式发布。

Lalkaka指出，Rollouts已经能够挑选出局限于特定端点或区域的问题，并在它们触发更广泛的警报之前将其拦截，同时它还可以将预期的行为变化与真正的回归区分开来。

据Cursor称，Rollouts“即将推出”的功能还包括与功能标志（feature flags）的集成，以便它可以直接调整到达更改的流量，同时对发布列车（release trains）和部署冻结（deployment freezes）的支持也在开发中。

## 引入Security Reviewer

除了Rollouts，Cursor还推出了升级版的Security Reviewer Bot，该Bot最早于[4月份](https://cursor.com/changelog/04-30-26)以测试版形式亮相。

在发布时，该Bot可以自动检查拉取请求中的安全漏洞、身份验证回归、隐私和数据处理风险、智能体工具自动批准以及提示注入攻击，并在相关代码旁留下发现的问题。

与Rollouts一样，其理念是开发者不必记得手动调用它：可以将其设置为只要打开新的拉取请求就会运行Security Reviewer。

![Security Reviewer运行中](https://cdn.thenewstack.io/media/2026/09/83b5f76d-gif3securityerviewr.gif)

*Security Reviewer在新的拉取请求上自动运行*

在其当前形式下，Security Reviewer在更广泛的代码库背景下分析拉取请求，重点关注可利用的问题，如注入缺陷和损坏的身份验证，并返回严重性评级、攻击路径和提出的修复方案。

“Security Review以安全工程师的方式阅读代码，”Lalkaka写道。“用户输入在哪里进入，最终去往何处，途中经过了什么。”

> “Security Review以安全工程师的方式阅读代码。”

他说，事情的速度也明显加快了：平均审查时间缩短了21%，从4.8分钟降至3.8分钟，而开发者对其评论的接受度从大约45-50%上升到60-70%。

Rollouts和Security Reviewer都通过Cursor的自动化（Automations）标签页提供给其团队版（Teams）和企业版（Enterprise）计划的客户。

## 起源故事

深入研究Rollouts的核心细节揭示了它如何成为Cursor构建[Origin](https://cursor.com/docs/origin)的一大助力，这是该公司在[8月份推出](https://thenewstack.io/cursor-origin-github-alternative/)的尚处于起步阶段的Git兼容代码托管平台。

Origin本质上是在为充满智能体的软件开发世界构建GitHub替代方案的努力。它仍处于早期阶段，功能有限，但Cursor已经明确表示，与自己的智能体进行更紧密的集成应该成为使用它的主要原因之一。

当Cursor上个月宣布收购Firetiger时，Cursor产品团队的[Maxime Prades](https://www.linkedin.com/in/pradesmaxime/?locale=en)在[一篇博客文章中指出](https://cursor.com/blog/firetiger)，这笔交易是“对团队长期运行、自主、上下文感知智能体更广泛投资”的一部分。

他指出了Origin和变更监视器作为该投资的两个例子。

“编写代码的智能体也应该能够判断它在生产环境中是否有效，”Prades写道。“今天，这些系统大体上是分开的。Cursor和Firetiger将它们拉得更近，以便智能体可以交付更改、观察其行为并在出错时做出响应。”

Rollouts提供了一个早期的窥探窗口。它可以连接到Origin或GitHub进行源码控制，从持续交付系统中拉取部署事件，并使用来自Datadog和其他遥测提供商的信号。如果它发现回归，它可以将问题传回Cursor云智能体进行调查或尝试修复。

Origin[潜在地为Cursor提供了](https://cursor.com/docs/origin/integrations)一个原生家园，可以容纳更多这样的循环：其云智能体已经可以创建分支、提交和推送代码，并针对Origin仓库打开拉取请求。然后Rollouts会添加关于之后发生的事情的信息。

随着越来越多的公司将目标对准GitHub在软件开发中的核心地位，这一点可能会变得越来越重要。例如，Zed在上周将其[Delta放入公共测试版](https://thenewstack.io/zed-delta-github-alternative/)，对于大量使用智能体的团队应该如何改变源码控制，它有自己的想法。

Cursor在更下游也面临竞争。Datadog的[Bits Release](https://www.datadoghq.com/product-preview/bits-release/)于[6月份预览版](https://www.datadoghq.com/blog/bits-release/)发布，同样追踪从拉取请求到生产环境的更改，并检查遥测数据的回归。Harness[长期以来一直提供](https://www.harness.io/products/continuous-delivery/ai-assisted-deployment-verification)基于日志和指标的自动化部署验证和回滚，而LaunchDarkly的[Guarded Rollouts](https://launchdarkly.com/docs/home/releases/guarded-rollouts)可以[监控功能发布的回归](https://thenewstack.io/ship-fast-break-nothing-launchdarklys-winning-formula/)并自动将其逆转。

Cursor潜在的优势在于邻近性：编码智能体、仓库、拉取请求、安全检查和生产反馈都可以靠得更近。Rollouts不需要Origin——GitHub仍然受支持——但拥有这个构建工场给了Cursor随着时间推移更好地集成这些部分的更多空间。这可能比单纯重现GitHub现有功能集更具吸引力。