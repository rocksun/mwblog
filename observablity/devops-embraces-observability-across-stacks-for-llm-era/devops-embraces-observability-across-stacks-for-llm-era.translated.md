# DevOps 在 LLM 时代拥抱跨栈可观测性

![Featued image for: DevOps Embraces Observability Across Stacks for LLM Era](https://cdn.thenewstack.io/media/2024/07/939dc367-alex-shuper-nkbruh3ngbs-unsplash-1-683x1024-1.jpg)

纽约 - 人工智能的巨大影响、安全问题以及向云原生迁移带来的持续挑战，对 [DevOps](https://thenewstack.io/devops/) 构成了重大颠覆。所有这些都将在未来几个月或几年内，如果不是几个月的话，导致变化。

虽然 [平台工程](https://thenewstack.io/platform-engineering/) 看起来为应对与之相关的基础设施和数据爆炸以及应用程序管理提供了有希望的方法，但应对这些挑战的根本方法将涉及适当的 [可观测性](https://thenewstack.io/observability/) 和对 [OpenTelemetry](https://thenewstack.io/observability-in-2024-more-opentelemetry-less-confusion/) 的支持。这是 [DASH 2024](https://www.dashcon.io/)，[Datadog](https://thenewstack.io/datadog-brings-big-observability-directly-to-your-phone/) 最近在这里举办的年度用户大会的主要收获之一。

这个主题可能与任何用户或任何会议相关，因为社区正在寻找方法来应对数据和应用程序管理和观察的爆炸式增长，没有人确切地知道人工智能对软件开发和部署、[CI/CD](https://thenewstack.io/ci-cd/) 以及 DevOps 和 IT 的总体影响。然而，可以争论的是，随着未来尘埃落定，将取决于适当的可观测性流程、工具和实践来分析并做出关于如何最好地利用 LLM 进行应用程序开发和其他 AI 辅助流程的正确决策。

“我们从你们中许多人那里听说，你们支持 LLM 的应用程序正在迁移到生产环境。一旦进入生产环境，就必须像任何其他承重机器一样对其进行监控，”Datadog 首席技术官兼联合创始人 [Alexis Lê-Quôc](https://www.linkedin.com/in/alexislequoc/) 在 DASH 主题演讲中说。“但与它们不同的是，需要了解健康状况、性能和安全性的数据类型。”


[@datadoghq] 说你可以通过[@opentelemetry](Datadog 是前 10 大贡献者之一) 获得 Datadog 的所有监控和可观测性，工程总监 Gordon Radlein 在今天的 [#DASH] 用户大会主题演讲中说。[pic.twitter.com/nCvNJpLSBt]— BC Gain (@bcamerongain)

[2024 年 6 月 26 日]
为了标准化日志、跟踪和指标的检测，不仅针对 [大型语言模型 (LLM)](https://thenewstack.io/llm/)，而且针对任何组织的整个堆栈和环境，OpenTelemetry——一个更具活力的开源项目——将变得更加重要。“OpenTelemetry 正在通过提供基于标准的基础为我们构建，从而彻底改变可观测性，释放整个行业的创新，”Datadog 工程总监 [Gordon Radlein](https://www.linkedin.com/in/gordonradlein/) 在他的主题演讲中说。“这是一场让所有船只都受益的潮流。”

为了帮助 Datadog 用户以及那些正在考虑采用该平台的用户——OpenTelemetry 有助于更轻松地与现有解决方案混合和匹配——Datadog 在 DASH 上发布了一系列新产品和功能。这是对来自 187,000 次客户会议的一年多反馈的总结；导致大约 50 万次生产发布，涵盖 400 多种新产品和新功能，Datadog 联合创始人兼首席执行官 [Olivier Pomel](https://www.linkedin.com/in/olivierpomel/) 在他的主题演讲中说。

## LLM 和平

再说一次，LLM 安全是一个大问题，也是一个不同的动物，为此，Datadog 在 DASH 上发布了 Datadog LLM 可观测性。借助它，该平台旨在帮助组织更好地洞察和控制 LLM 数据的爆炸式增长，这些数据通常表现为单个组织中的多个 LLM。正如 Datadog 工程主管 [Mohamed Alimi](https://www.linkedin.com/in/mohamed-kamel-alimi/) 所解释的那样，对 LLM 的实验“导致了许多行业的令人难以置信的创新，其中许多实验已经从简单的应用程序发展成为在生产环境中运行的更复杂的系统，使用多个 LLM，”用于编排框架、检索系统和 [知识图谱](https://thenewstack.io/better-llm-integration-with-content-centric-knowledge-graphs/)。“但这同时也带来了新的挑战，”他说。

Alimi 说，随着应用程序参与 LLM 和更复杂的模式，它们变得更难排查。其次，由于 LLM 和人工智能组件的固有不可预测性，这些应用程序需要持续监控幻觉。最后，Alimi 说，这些应用程序可能会面临来自提示黑客和数据共享的重大风险。
在 DASH 的演示中，Alim 展示了如何使用 LLM 支持的电子商务聊天机器人，Datadog LLM 可观测性突出显示需要立即关注的问题。错误、潜在的幻觉、缓慢的响应、令牌计数和安全威胁都被标记出来。“它还突出了‘忠实度’，这是相对于给定上下文而言的正确性和准确性的衡量标准，”Alimi 说。“我们在这里使用忠实度作为幻觉的代理。”

在演示过程中，Alimi 使用该平台收集有关报告的幻觉的情報。提供的信息包括交互的持续时间、消耗的令牌计数和进行的 LLM 调用次数。“组织需要拥抱可观测性”，以便为安全性和性能正确管理 LLM，Alimi 说。

作为可观测性提供商，Datadog 对作为 OpenTelemetry 项目的主要贡献者以及使用 OpenTelemetry 提供的标准化使其工具与 OpenTelemetry 兼容有着浓厚的兴趣。

其理念是，通过此 OpenTelemetry 功能或仪器，用户组织可以立即无缝地连接并开始使用他们选择的可观测性平台。当然，可观测性提供商也会单独尽力通过 OpenTelemetry 使这种体验优于其他参与者。

OpenTelemetry 的优势之一是它有助于简化兼容性，并且随着社区的贡献，它允许开发更多可以利用此功能或允许解决方案可观测性提供商利用这种兼容性的功能。

## OpenTelemetry 强劲
作为 OpenTelemetry 项目的前 10 名贡献者之一，Datadog 继续帮助构建该项目，而其产品开发继续超过 OpenTelemetry 兼容性。“由于 Datadog 在这个领域已经发展了很长时间，OTel [OpenTelemetry] 还没有支持所有提供的产品。随着 Datadog 的创新速度，这种情况预计会继续下去，即使差距正在缩小。这带来了一个困境：要么全力投入 Datadog，放弃 OpenTelemetry 带来的某些巨大好处，要么局限于 OTel 支持的产品，”Radlein 说。“自然而然地，问题出现了，为什么不两者兼得呢？Datadog 一直在努力解决这个问题，因为 Datadog 与 OpenTelemetry 结合更好，而 OpenTelemetry 与 Datadog 结合更好。”

在 DASH 期间，Radlein 描述了 Datadog 如何通过统一 Datadog 代理和 OpenTelemetry 收集器来迈出下一步。“现在，代理和收集器协同工作，形成一个大于其各部分之和的整体，丰富 OpenTelemetry 数据并启用产品套件，”Radlein 说。

Radlein 说，使用新代理，收集器用户将立即获得对完整产品套件和平台的访问权限。提供基于应用程序的收集器集群管理，“以及来自专用产品支持的安心。新代理用户还将获得对大量不断增长的社区贡献的集成访问权限，包括对越来越多的商业和开源工具的开箱即用支持，这些工具使用 OpenTelemetry 本地进行仪器化，”Radlein 说。“实现了可观测性集群中工具的更好互操作性，无论这些工具是基于供应商的还是开源的。提供对 OTLP 数据的控制，并完全访问收集器强大的路由和处理功能。”

## 云原生方式
LLMS 和 OpenTelemetry 虽然规模巨大，但只是在会议上宣布的十多个其他公告之一。其中包括 Datadog 如何加强可观测性以帮助缓解不断上升的云成本。正如 Datadog 容器和 Kubernetes 监控产品经理 Danny Driscoll 所说，超过 65% 的 Datadog 监控的 Kubernetes 容器仍然使用不到其请求的内存和 CPU 资源的一半。

使用 Datadog Kubernetes 自动缩放，优先考虑具有最大节省潜力的工作负载和集群，以便从 Datadog 平台直接采取行动来应用并自动执行大小调整建议，并观察和衡量您的完整自动缩放程序对您的关键成本和效率指标的影响。Driscoll 说，此公告旨在帮助用户在 Kubernetes 上构建平台以提供更有效的资源使用，这可以降低基础设施成本，并降低您的企业对能源消耗的影响。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)