
<!--
title: OpenTelemetry挑战：处理长时间运行的Span
cover: https://cdn.thenewstack.io/media/2024/10/8cc613c6-long-running-span-observability-challenge.jpg
-->

解决 OpenTelemetry 中长时间 Span 的方案比“不要有长时间 Span ”更具创造性。了解如何解决这个常见问题。

> 译自 [OpenTelemetry Challenges: Handling Long-Running Spans](https://thenewstack.io/opentelemetry-challenges-handling-long-running-spans/)，作者 Hazel Weakly。

OpenTelemetry (OTel) 席卷了可观察性领域，这是有充分理由的！在过去十年的某个时候，软件世界悄然开始将协议视为标准，在开源中发展它们并拥抱社区驱动的开源。在这一势头的推动下，OTel 迅速成长为 [CNCF](https://cncf.io/?utm_content=inline+mention) 生态系统中速度第二快的项目。OTel 专注于供应商中立性和语言互操作性，允许工程师专注于理解他们的系统，而不是调试他们的调试器，事后看来，OTel 的成功几乎是显而易见的。

也就是说，尽管围绕 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 的呼声很高，但它并不总是一帆风顺的。在 OpenTelemetry 的心智模型和假设中，有些事情真的很难解决。现实世界中需要解决的巨大障碍之一是长时间运行的 [span](https://thenewstack.io/spans-what-are-they-and-why-should-mobile-engineers-care)。

## 长时间……运行？什么？

长时间运行的 span！好吧，我会稍微解释一下。OTel 的概念一开始可能会让人不知所措，因为它在您开始之前有很多概念需要了解。当人们谈论 OpenTelemetry 时，他们通常指的是分布式跟踪。虽然我只会关注相关的部分，但如果您有兴趣，这里有一个 [全面的概述](https://opentelemetry.io/docs/concepts/observability-primer/)。

当您调试系统时，您的第一个问题通常是“发生了什么操作？”。但是，从最终用户的角度来看，一个操作从系统的角度来看会转换为多个操作。为了协调这一点，OTel 有一个 span 的概念，它是从最终用户的角度来看的一个操作。在该 span 中，您有更多代表系统角度来看的所有操作的 span。我们称“代表用户观点的 span”为 [跟踪](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app)……通常是这样。

但是，对我们来说，span 的相关部分是它包含一些内容：ID、跟踪 ID、开始时间和结束时间。当您将您的小宝贝发送到可观察性后端时，它会附带所有四条信息（以及实际数据）。但这意味着 span 有一个持续时间，这有一些深远的影响。

事实还证明，在实践中，很多工具*真的*不希望 span 的长度超过……嗯，不是很长。

为什么工具关心这个？有几个主要原因！一个很大的原因是 OTel API 规范说明了一些非常重要的事情：所有 span 都必须结束，这是实现者的责任。此外，它还指出，如果开发人员忘记结束 span，API 实现可能会对其进行任何处理。软件开发工具包 (SDK) 规范提供了内置的 [span 处理器](https://opentelemetry.io/docs/specs/otel/trace/sdk/#span-processor)，但它们仅对已完成的 span 进行操作。

换句话说，用户视角是一个 span，任何未完成的 span 都可能会永远丢失。如果未完成的 span 恰好是根 span，则发送的所有内部 span 都将显示为孤立的，如果后端甚至可以处理它们的存在。实际上，这意味着长度超过五秒左右的根 span 可能会导致问题。

工具关心这一点的另一个原因是采样。当您将大量数据从一个地方发送到另一个地方时，有理由询问如何更好地表示这些数据，以及如何避免发送其中的一些数据。这就是采样发挥作用的地方。采样服务获取遥测数据并决定是否将其发送到后端（以及一些使其全部起作用的精美数学调整）。整洁！但是，有一个小问题：它如何决定何时发送相关内容？采样决策必须在完整的 span 上进行，并且通常在整个跟踪的 span 上进行。如果您丢失了根 span，那将行不通！

因此，尴尬的是，不仅未完成的 span 可能会永远丢失，而且最有可能丢失的 span 通常是最有价值的 span，而且您的所有成本、网络和计算优化都将失效。哎哟。

## 您是否尝试过不使用长时间运行的 Span？

解决问题的最佳方法是修复它，但解决问题的绝妙方法是根本不让它发生！我们能不能……干脆不要有长 Span ？这是一个崇高的想法，但事实证明，无论我们的 Span 有多长，我们都会遇到这个问题。我们一直在谈论长 Span ，但这实际上更多的是关于中断和不完整 Span 。

原因是，就其数据模型而言， Span 基本上与数据库事务相同。因此，每当您遇到需要在多个系统之间通过网络发送事务的情况时，您就会遇到专家喜欢称之为“真正糟糕的时刻”的情况。

您可以尝试许多解决方案！以下是一些人们使用过的解决方案：

- 重构代码以用更小的块表示操作。
- [将长时间操作分解为多个间隔](https://www.honeycomb.io/blog/ask-miss-o11y-long-running-requests)。
- [生成更少的跟踪并在子 Span 中携带更多数据](https://opentelemetry.io/docs/specs/otel/context/api-propagators/#global-propagators)。
- 手动提前结束根 Span 。
- [对数据进行不健全且粗略的转换以重写 Span  ID、跟踪 ID 和链接](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/7ec6396c393c7456ddd03ce060a94e4a2d5b55fb/processor/transformprocessor#warnings)。（跟我重复一遍：“我郑重宣誓，在生产中可能会避免这种情况。”）
- [取消设置跟踪 ID 并改用链接](https://opentelemetry.io/docs/specs/otel/overview/#links-between-spans)。
- [确保您的跟踪上下文正确无误，并且您没有意外地创建根 Span ](https://www.iankduncan.com/articles/2023-08-28-opentelemetry-gotchas-phantom-spans)。

不幸的是，这些方法都没有解决根本问题：当我们说 Span 必须结束并给出一个持续时间时，我们就将它们变成了事务——而跨系统处理事务是*困难的*。

更糟糕的是，虽然您可能认为中断的 Span 不会经常发生，但事实证明它们发生得相当频繁：

- 在后端：每当应用程序在请求中途重新启动、崩溃或网络出现故障时，或者……
- 在前端：每当 Web 客户端四处导航、关闭或刷新选项卡、取消操作或浏览器事件循环中断时，或者……
- 在移动设备中：以上所有以及更多！

然而，幸运女神眷顾有创造力的人。既然我们知道我们真正要处理的是一个事务语义问题（它碰巧看起来像一个“不要有长时间运行的 Span ”问题），我们可以看看所有关于这方面的现有文献。当然有人已经解决了这个问题——或者，呃，至少尝试过？

## 针对块状 Span 的创造性解决方案

戴上我们的思考帽和研究眼镜，我们会发现围绕数据库、事件流和分布式事务的大量信息。然而，有一个小问题：其中很多看起来不像 OTel，而且很难看出解决方案是如何应用的。但是，如果我们稍微扩展一下 Span 的定义，并且在给定的约束条件下……稍微作弊一下呢？这是否会让我们能够利用其他具有类似约束条件的技术来重新利用一些解决方案呢？

在处理事务时，有两个经常出现的主题：快照和预写日志。事实上，[作为数据抽象的日志](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)是分布式系统的基本构建块之一。作为仅追加的有序数据结构，日志最终成为构建快照的完美之选，事实证明，OpenTelemetry SDK 中的 Span 处理器可以被认为是内存中的预写日志。好吧，你必须眯着眼睛才能这样想，但实际上，它确实是。

太棒了！我们不仅拥有以日志形式处理事务的行业采用模式，而且我们已经拥有构建快照所需的大部分组件！快照并不能解决我们所有的问题，但它是一个巨大的改进，它使部分数据可用——这对于调试来说是无价的。

> 那么，呃，我们该怎么做呢？

首先，我们必须重新构建流程：我们不是将 Span 发送到后端，而是将 Span 写入日志，然后将其一致地复制到后端。

> 那么，呃，我们该怎么做呢？

问得好！事实证明，[Embrace](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=long-running-spans) 已经实现了这个解决方案，并解释了[他们这样做的原因](https://www.cncf.io/blog/2024/06/14/why-embrace-created-span-snapshots-for-mobile-observability-with-opentelemetry/)。至于*如何*，虽然日志复制有大量的可能解决方案，但一个简单的解决方案只需要对客户端和服务器进行一些小的更改。

1. 首先，客户端必须发送正在进行的 Span 的快照（这需要自定义 Span 处理器和导出器）。
2. 其次，后端需要处理和存储这些数据，并等待它们最终完成。
3. 第三，如果这些 Span 从未完成，它们仍然需要优雅地整合成符合 OTel 规范的形状并发送到上游。（好吧，我撒谎了。这并不简单。我们在这里省略了很多细节。）

这看起来工作量很大，但 Embrace 的 SDK 和后端为你完成了所有这些工作，包括处理出现中断和 Span 未完成的情况。更好的是，这些 Span 在完成后完全符合 OTel 规范，这意味着没有什么能阻止此解决方案进入 OpenTelemetry。

## Tracer.getInstance().endSpan()

呼！我们在这里涵盖了很多内容。首先，我们讨论了什么是长时间运行的 Span，为什么我们会遇到它们，为什么它们是一个问题，以及无论你多么努力都无法避免它们。事实上，你不仅会遇到它们，而且任何涉及不完整或中断 Span 的情况都会遇到许多相同的故障模式，我们将这些模式确定为事务语义问题。

幸运的是，事实证明，事务语义是一个经过充分研究的问题，我们能够研究出一个很好的解决方案，并介绍了它如何与 OpenTelemetry 一起工作的草图。

如果你来自传统的以后端为中心的 Observability 方法，你会惊讶于移动环境是多么的不同。如果你想了解更多信息，Embrace 有一个很有帮助的点播网络研讨会：[DevOps 和 SRE 需要了解的有关移动可观察性的知识](https://get.embrace.io/mobile-devops-sre/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=long-running-spans)。还有一个有用的指南：[克服移动可观察性的关键挑战：面向现代 DevOps 和 SRE 团队的指南](https://get.embrace.io/mobile-observability-guide?utm_source=the-new-stack&utm_medium=paid&utm_campaign=long-running-spans)。

长时间运行的 Span 很困难，事务也很困难，但拥抱创造性的问题解决方法来找到有用的答案正是可观察性的意义所在。
