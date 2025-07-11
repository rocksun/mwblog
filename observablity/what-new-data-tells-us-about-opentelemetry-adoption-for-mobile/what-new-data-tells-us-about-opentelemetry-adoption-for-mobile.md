
<!--
title: 移动端OpenTelemetry：调查称采用率将增三倍
cover: https://cdn.thenewstack.io/media/2025/07/2251e434-mobilex.png
summary: EMA调查显示，移动可观测性日益重要，OpenTelemetry(OTel)在移动领域的应用预计增长。成熟组织更倾向于关联移动和后端数据，并重视集成与互操作性。真实用户监控(RUM)成为关注焦点，OTel助力捕获完整用户旅程。
-->

EMA调查显示，移动可观测性日益重要，OpenTelemetry(OTel)在移动领域的应用预计增长。成熟组织更倾向于关联移动和后端数据，并重视集成与互操作性。真实用户监控(RUM)成为关注焦点，OTel助力捕获完整用户旅程。

> 译自：[OpenTelemetry for Mobile: Adoption Set to Triple, Says Survey](https://thenewstack.io/what-new-data-tells-us-about-opentelemetry-adoption-for-mobile/)
> 
> 作者：Virna Sekuj

当大多数开发者想到 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 时，他们会想到后端追踪、指标和日志，而不是 [移动应用性能](https://thenewstack.io/testing-mobile-apps-for-real-world-network-conditions/)。但新的数据显示，这种情况正在开始改变。

Enterprise Management Associates (EMA) 最近进行的一项 [调查](https://get.embrace.io/opentelemetry-for-mobile-whats-now-and-whats-next?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-mobile-report) 显示，移动可观测性正在成为现代可观测性实践的关键组成部分。拥有成熟可观测性文化的企业不仅在移动遥测方面进行投资，他们还将 OpenTelemetry (OTel) 视为跨后端和前端统一检测的未来。

以下是一些关于 OpenTelemetry 在移动和真实用户监控方面的发展方向，以及这对工程团队意味着什么的数据。

## **移动可观测性标志着可观测性的成熟**

近三分之二的参与者表示，他们的组织拥有成熟的可观测性实践，超过一半的人表示他们已经完全集成了移动遥测。相比之下，所有其他组织中只有 18% 的人表示相同。

这是有道理的：真正的端到端可见性需要 [了解移动客户端](https://get.embrace.io/mobile-observability-guide?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-mobile-report)。如果没有来自设备本身的遥测，[您将错过用户请求的来源](https://thenewstack.io/why-your-mobile-app-needs-client-side-network-monitoring/) 以及影响真实用户的许多性能问题。

更引人注目的是，75% 的成熟组织报告说，他们将移动和后端可观测性数据相关联，从而使他们能够统一查看整个堆栈。相比之下，不太成熟的组织只有 11% 这样做。

[![](https://cdn.thenewstack.io/media/2025/07/aeacfd4e-image3-1024x544.png)](https://cdn.thenewstack.io/media/2025/07/aeacfd4e-image3-1024x544.png)

来源：Enterprise Management Associates。

## **OpenTelemetry 采用率：有望在移动领域增长两倍**

OpenTelemetry 在 [移动数据收集](https://thenewstack.io/best-practices-for-monitoring-network-conditions-in-mobile/) 方面的采用仍处于早期阶段。只有 6% 的组织报告说目前正在使用它。但根据 EMA 的调查，预计在未来 12 到 24 个月内，这个数字将增长两倍。

推动这种采用的是对跨系统标准化检测的渴望。移动遥测通常使用特定于供应商的 SDK 或自制解决方案来收集，这些解决方案与其他堆栈的互操作性不佳。相比之下，OpenTelemetry 提供了一种开放的、与供应商无关的格式，可以一致地关联移动、Web 和后端信号。

不过，OTel 对移动的支持仍在不断发展。一些团队对 OpenTelemetry 的成熟度表示担忧，但总体而言，62% 的人仍然认为它是可观测性的“非常重要”或“至关重要”的推动因素。此外，83% 的人认为在评估新的移动监控工具时，OpenTelemetry 集成非常重要或至关重要。

[![](https://cdn.thenewstack.io/media/2025/07/f3423cb5-image2-1024x523.png)](https://cdn.thenewstack.io/media/2025/07/f3423cb5-image2-1024x523.png)

来源：Enterprise Management Associates。

## **集成和互操作性是首要任务**

在评估移动可观测性解决方案时，受访者普遍优先考虑集成。“易于与其他可观测性工具集成”是首要任务，其次是“能够将移动数据共享或转发到其他系统”和“移动问题专业化，例如 [ANR](https://embrace.io/blog/how-does-an-anr-work/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-mobile-report) [应用程序无响应] 和 [客户端网络问题](https://embrace.io/blog/best-practices-for-monitoring-network-conditions-in-mobile/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-mobile-report)”。

这突出了一个更广泛的趋势：工程师们厌倦了工具的蔓延和数据孤岛。无论他们专注于后端服务、Web 应用程序还是原生移动应用程序，团队都希望获得统一的数据和可见性，从而 [从用户的设备延伸到数据库](https://thenewstack.io/the-case-for-user-focused-observability/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-mobile-report)。反映移动体验的上下文和细微差别的适用于 iOS 和 Android 的 OTel SDK 对于实现这一目标至关重要。

OpenTelemetry 支持这种统一。该规范没有将移动视为一个不相关的边缘情况，而是可以标准化客户端信号并将其流入现有的可观测性平台，无论是供应商的仪表板还是自托管的 Grafana 实例。

## **下一个前沿：真实用户监控**

虽然追踪仍然是 OpenTelemetry 最常见的用例，但调查受访者表示对扩展到以用户为中心的遥测非常感兴趣。事实上，真实用户监控 (RUM) 是工程师希望添加到 OpenTelemetry 的顶级数据类型或来源，仅次于生成式 AI 性能数据。

此外，在表示他们将在未来 12 到 24 个月内进行更多 OpenTelemetry 实验的受访者中，监控真实用户行为与他们最有可能尝试的事情并列。

[![](https://cdn.thenewstack.io/media/2025/07/abab2122-image1-1024x498.png)](https://cdn.thenewstack.io/media/2025/07/abab2122-image1-1024x498.png)

来源：Enterprise Management Associates。

为什么这很重要？虽然传统的后端可观测性可以告诉您您的基础设施在做什么，但 RUM 可以回答用户正在体验什么：他们正在查看什么屏幕、内容加载需要多长时间以及他们在流程中的哪个位置退出。

随着移动工作流程变得越来越复杂，对客户端追踪和实时行为监控的需求变得至关重要。这与现代 DevOps 和站点可靠性工程 (SRE) 团队已经在做的事情相一致：使用追踪来连接分布式系统中的各个点，现在包括客户端。

## **OTel 在捕获完整用户旅程中的价值**

OpenTelemetry 通常被描述为一种朝着更开放、更统一的可观测性发展的趋势。完全采用 OTel 策略的组织希望打破孤岛并减少供应商锁定。[移动 RUM](https://embrace.io/product/mobile-rum/) 正在成为这一愿景中越来越重要的一部分。

本报告中的数据表明，基于 OTel 的移动检测和可观测性方法将在 OpenTelemetry 采用的下一阶段发挥重要作用。趋势线很明显：

* 成熟可观测性组织中的团队正在优先考虑将移动作为整体的一部分。
* OpenTelemetry 在移动领域的采用预计将显着增长。
* RUM 和以用户为中心的遥测是计划实验的重点领域。
* 对移动工具的购买决策越来越受到 OTel 支持的影响。

可观测性领域的供应商已经注意到了这一点。越来越多的工具正在扩展其对 OpenTelemetry 的支持，无论是通过促进更通用的数据摄取，还是通过改造其代理和 SDK 以遵循检测标准。

许多人也参与到开源社区中，为 [云原生计算基金会](https://cncf.io/?utm_content=inline+mention) 做出代码贡献并建立关系，云原生计算基金会是 OpenTelemetry 项目的孵化器。

最终用户不再是可观测性中的事后想法，并且作为关键的消费者接触点，移动性能正变得越来越重要，需要理解，而 OpenTelemetry 正在推动标准化和创新。

对于投资于长期可观测性战略的工程团队来说，现在是关注并了解 OpenTelemetry 如何在最终用户旅程中发挥关键作用的时候了。

如果您想了解更多信息，可以 [在此处下载完整的“移动领域的 OpenTelemetry”报告](https://get.embrace.io/opentelemetry-for-mobile-whats-now-and-whats-next?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-mobile-report)。