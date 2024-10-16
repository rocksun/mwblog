
<!--
title: 塑造可观测性市场的关键趋势
cover: https://cdn.thenewstack.io/media/2024/10/49bbadcd-observability.jpg
-->

随着人工智能导致数据复杂性和体积的增加，像 OpenTelemetry 这样的开源解决方案以及新的成本管理方法正在推动变革。

> 译自 [Key Trends Shaping the Observability Market](https://thenewstack.io/key-trends-shaping-the-observability-market/)，作者 Krishna Yadappanavar。

[可观测性](https://thenewstack.io/observability/) 市场正在经历重大转型，这得益于新技术的出现和不断变化的需求。以下四个关键趋势将对该市场产生重大影响：

## 1. AI 革命：大语言模型和可观测性

人工智能和[大语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms) 正在改变我们监控系统的方式。云原生系统会生成大量数据，而 AI 有助于发现隐藏的洞察力并自动解决问题。它可以检测异常并调整 CPU 使用率等设置以避免停机。此外，LLM 通过用通俗易懂的语言解释技术问题，使其更容易理解。

反过来，LLM 和[生成式 AI](https://thenewstack.io/ai/) 也需要强大的可观测性才能良好运行。LLM 从可观测性工具中受益的三个关键领域是：

* **资源管理**: LLM 可能非常消耗资源，需要大量的计算能力和内存。可观测性工具跟踪这些资源以优化部署并控制成本。例如，跟踪 LLM 的 CPU 和内存使用率的波动可以及时调整，从而防止意外的成本激增。
* **性能监控**: LLM 可能生成不准确的结果，这种现象被称为幻觉。实施端到端跟踪可以让你跟踪请求从提交到响应的生命周期，帮助你识别不准确发生的位置。可观测性还可以监控需要重新生成响应的频率，或评估用户对输出的满意度，作为性能问题的指标。
* **模型漂移检测**: 可观测性工具可以通过监控关键性能指标 (KPI) 来发现 LLM 的性能何时偏离预期规范。与历史数据的重大偏差可以触发警报，提示工程师重新校准模型并保持其有效性。

## 2. 统一的数据湖

传统上，可观测性一直是关于监控指标和分析日志。指标提供了系统性能的高级视图，例如响应时间和错误率。日志提供了有关事件和错误的详细信息，这对于解决特定问题至关重要。

然而，如今的组织需要更全面的洞察力，这导致了可观测性数据湖的激增。以下因素推动了这种转变：

* **分布式跟踪是必不可少的**: 随着微服务的普及，跟踪对于跟踪事务如何在系统中移动至关重要。[跟踪有助于查明请求流和分布式系统中的瓶颈](https://thenewstack.io/demystifying-distributed-traces-in-opentelemetry/)，这需要更高级的数据分析，包括依赖关系图和跨时间、位置和服务 ID 等各种因素的性能指标。可观测性数据湖提供集成的數據圖，以清晰地了解系统性能及其性能瓶颈。
* **简化根本原因分析**: 与手动分析单独的数据流以查找问题的根本原因相比，数据湖将指标、日志和跟踪组合到一个视图中。这使得不仅更容易看到出了什么问题，而且更容易看到为什么，从而可以更快、更有效地进行调查和故障排除。
* **新兴数据流**: 随着实时用户监控、持续分析和安全可观测性等新的可观测性数据流的出现，数据湖变得更加重要。它们整合了这些洞察力，提供了应用程序性能的完整视图。
* **统一运营**: 此外，数据湖在不同的运营领域（如 DevOps、ITOps、DataOps、FinOps、AIOps 和 LLM Ops）统一了可观测性。通过将数据集中在一个地方，组织可以减少资源、计算成本并提高所有系统的可靠性。

## 3. OpenTelemetry (Otel) 的兴起

[OpenTelemetry (Otel) 正在获得越来越多的关注](https://thenewstack.io/opentelemetry-gaining-traction-from-companies-and-vendors/)，这是对供应商锁定、孤立的可观测性方法以及对标准化的需求的回应。根据[最新的云原生计算基金会报告](https://www.cncf.io/reports/opentelemetry-project-journey-report/)，有 1,106 家公司和 9,168 个人参与了其开发。作为由社区创新驱动的开源项目，[Otel 提供了一个统一的框架](https://www.kloudfuse.com/blog/understanding-opentelemetry) 用于[监控各种系统和应用程序](https://thenewstack.io/why-upgrade-to-observability-from-application-monitoring/)，使其更容易在不同平台之间集成可观测性。

Otel 的广泛采用得益于其与各种技术的兼容性，特别是那些受益于其自动仪器化的技术，例如 [Java](https://thenewstack.io/oracle-unveils-java-23-simplicity-meets-enterprise-power/) 和 [Python](https://thenewstack.io/what-is-python/) 应用程序。这种灵活性帮助组织避免绑定到单个供应商，并允许他们根据自己的特定需求定制可观察性解决方案。随着可观察性需求的不断发展，Otel 可能会在推动创新和确保互操作性方面发挥更大的作用。

## 4. 通过私有部署控制成本

随着可观察性数据量的增加，成本正在急剧上升，一些公司面临着 [数百万美元的账单](https://thenewstack.io/datadogs-65m-bill-and-why-developers-should-care/)。除了支付超额费用外，公司还为将数据传输到 SaaS 可观察性产品付费。传统的 SaaS 定价模式无法跟上，导致许多组织寻求替代解决方案。

越来越多的趋势是将可观察性解决方案迁移到私有云。这种转变使公司能够更好地控制其数据和支出。私有云解决方案可以根据特定需求和预算进行定制，从而降低整体可观察性成本。

## 结论

可观察性市场正处于一个关键时刻，受到人工智能进步以及数据复杂性和数据量不断增加的影响，并由 OpenTelemetry 等开源解决方案以及管理可观察性成本的新方法主导。随着这些趋势的不断发展，它们将重新定义组织监控、管理和优化其数字环境的方式。在这个充满活力的环境中保持领先地位需要适应这些变化，并利用新的工具和策略来保持可观察性的效率和有效性。

*要了解更多关于 Kubernetes 和云原生生态系统的信息，请加入我们参加 **KubeCon + CloudNativeCon 北美**，于 2024 年 11 月 12 日至 15 日在犹他州盐湖城举行。*
