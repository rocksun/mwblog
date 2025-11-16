<!--
title: Grafana已在可观测性AI领域取得领先？
cover: https://cdn.thenewstack.io/media/2025/11/5be23bde-observability-grafana-2.jpg
summary: Grafana将AI集成到其可观测性平台，推出AI助手，支持自然语言交互、查询生成与分析。它简化故障排除，自动化回滚，并旨在减少值班工作量，被认为比其他LLM更实用，展现了行业领先潜力。
-->

Grafana将AI集成到其可观测性平台，推出AI助手，支持自然语言交互、查询生成与分析。它简化故障排除，自动化回滚，并旨在减少值班工作量，被认为比其他LLM更实用，展现了行业领先潜力。

> 译自：[Has Grafana Taken Lead in AI for Observability?](https://thenewstack.io/has-grafana-taken-lead-in-ai-for-observability/)
> 
> 作者：B. Cameron Gain

[Grafana Labs](https://grafana.com/) 已将其人工智能支持集成到其[可观测性平台](https://thenewstack.io/traceloop-launches-an-observability-platform-for-llms-based-on-openllmetry/)和面板中，为[可观测性](https://thenewstack.io/introduction-to-observability/)体验带来了实际的改进。

Grafana 是否在可观测性供应商阵营中遥遥领先，取决于如何衡量不同供应商的产品。

目前，供应商们在如何最好地利用人工智能实现可观测性方面持有不同的理念。[DataDog 的](https://www.datadoghq.com/?utm_content=inline+mention)人工智能在很大程度上依赖并构建于[模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 代理之上。[Kloudfuse 的](https://www.kloudfuse.com/)人工智能功能主要支持数据湖可观测性。[Chronosphere](https://chronosphere.io/?utm_content=inline+mention) 目前对人工智能的价值及其在支持可观测性方面的适用性并不那么乐观。

与此同时，我可以亲身证明，在设置 Grafana 并将其与 [OpenTelemetry](https://thenewstack.io/how-opentelemetry-works-tracing-metrics-and-logs-on-kubernetes/) 集成时，Grafana 的 AI 支持非常有用，它能从 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 和 [Google](https://cloud.google.com/?utm_content=inline+mention) Cloud Platform 数据源获取指标数据，并汇集到我的 Grafana 面板中。

在 10 月伦敦举行的 [ObservabilityCon 大会](https://grafana.com/events/observabilitycon/)上的一次研讨会上，我在创建面板时遇到了困难。我只是简单地请求 AI 助手为我设置一个面板，它在短短几秒钟内就完成了。在研讨会期间，每当我遇到不同的障碍时——特别是在设置面板以将 AWS 数据集成到 GCP 中时——它都会为我提供相关的下一步操作（参见下图）。

[![](https://cdn.thenewstack.io/media/2025/11/386a1b22-screenshot-2025-10-13-at-12.12.59%E2%80%AFam-1024x615.png)](https://cdn.thenewstack.io/media/2025/11/386a1b22-screenshot-2025-10-13-at-12.12.59%E2%80%AFam-1024x615.png)

当然，我在研讨会上的经验有限，我的分析公司 ReveCom 尚未对其进行深入分析，以更深入地评估 Grafana 的 AI 工作。然而，我可以肯定它确实很有用。这说明了很多问题，而且它肯定比仅仅通过 Cursor 或 [Claude](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/) 助手提问，或者更糟糕的是，与 ChatGPT 提问更有用，ChatGPT 往往毫无价值。

## 自动化回滚

在 ObservabilityCon 大会上，Grafana 将 Grafana Assistant 描述为直接内置于 Grafana 中的 AI 驱动的聊天集成，使用户能够通过自然语言与可观测性数据进行交互。它使用[大型语言模型](https://thenewstack.io/introduction-to-llms/)来生成查询、分析结果并智能地迭代。

该助手旨在帮助非技术用户（那些可能在不构建仪表板的情况下提出问题的人）和专家级站点可靠性工程师（他们可以使用规则和基础设施上下文自定义行为）。它通过 MCP 服务器与 GitHub、AWS 和工单系统等工具连接，并具有“基础设施记忆”功能，可以映射遥测数据以理解依赖关系。

总体而言，Grafana Assistant 旨在使技术和非技术人员都能更轻松地访问可观测性。据 ObservabilityCon 大会上的多位演讲者称，它加速了调查并将 AI 无缝集成到工作流程中。

它提供了与 MCP 服务器的集成、用于指标和跟踪的语义语言规则以及输出图表的功能。

此外，在 ObservabilityCon 大会上还推出了 Grafana 的 Assistant Investigations，这是一个用于故障排除的自主代理系统。此功能使用诸如[扩展伯克利数据包过滤器 (eBPF)](https://thenewstack.io/what-is-ebpf/) 等数据源，并在后台运行以从多个角度探索问题。

Grafana Labs 首席技术官 Tom Wilkie 在会议期间这样向我描述：“AI 辅助的概念侧重于让 AI 现在就真正有用，而不仅仅是未来的承诺。目标是通过让客户更容易上手和诊断问题来立即带来真正的价值。内部理念是将 AI 应用于减少值班工程师的繁重工作。”

AI 辅助功能，例如助手和集群调查，会推荐下一步措施（例如，增加连接扩展）。Wilkie 说，在内部，公司已经在自动化这些修复措施的应用。

一个关键的自动化操作是版本回滚：工程师们被训练成立即回滚版本，而不是花 30 到 40 分钟应用有风险的修复，但 Wilkie 说，人性的弱点常常让他们试图彻底解决问题。

“自动化回滚实现了所需的行为，并为我们的工程师处理了大量的繁重工作，”他说。“我们的愿景是，在几年内，70% 到 80% 的值班工作量将通过回滚和扩展等安全操作自主处理。”

Wilkie 说，这种方法之所以可行，是因为该软件建立在服务水平目标 (SLO) 等抽象之上，这使得代理无需了解每个服务的来龙去脉就能判断版本是否是回归。Grafana 在开源方面的深厚基础也发挥了作用。

正如他所指出的那样，“公司相信其开源基础是其在人工智能方面的超能力，因为这些模型已经在其开源项目生成的内容上进行了训练。”