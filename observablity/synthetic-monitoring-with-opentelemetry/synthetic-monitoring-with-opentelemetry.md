
<!--
title: 使用 OpenTelemetry 进行合成监控
cover: https://cdn.thenewstack.io/media/2024/07/b2aa2dde-viewing.jpg
-->

基于对 OpenTelemetry 深入理解的合成监控解决方案提高了可视性和可测试性。

> 译自 [Synthetic Monitoring With OpenTelemetry](https://thenewstack.io/synthetic-monitoring-with-opentelemetry/)，作者 Ken Hamric。

合成监控用于主动测试和监控生产系统，确保性能、可用性、关键功能并评估用户体验。监控类型多种多样，从简单的 ping 到全自动的 Web 交互。

现代工程团队现在使用 [OpenTelemetry](https://opentelemetry.io/) 和分布式追踪进行生产监控和故障排除，但主要以手动、被动的方式进行。在主动的合成监控测试中使用 OpenTelemetry 有什么优势？

## 现有合成监控工具的局限性

大多数合成监控工具存在两个主要局限性，更好的可见性可以消除这些局限性：

1. 合成测试返回的结果很少。这需要工程师在可以捕获更多详细日志信息的環境中重现错误，才能开始诊断问题。
2. 大多数合成工具依赖于黑盒测试技术，无法正确检查当今复杂异步系统中存在的复杂流程。

让我们将这些问题归类为可见性和可测试性问题。我们如何做得更好？

## 使能技术 - OpenTelemetry

现代 DevOps 和站点可靠性工程 (SRE) 团队使用可观测性，特别是 OpenTelemetry，来快速诊断和解决生产故障。特别是分布式追踪，是为了解决当今现代系统的复杂性而构建的，包括：

- 异步进程，使用基于消息的架构，例如 Kafka。
- 分成多个微服务的系统，更多地依赖于第三方服务。
- 多个团队，地理位置分散，使用不同的语言编写代码。
- 各个服务分别进行测试，但在完全连接时，高度依赖于跨边界正常运行。

这些复杂性使得工程师难以完全理解系统在进程或 API 调用失败时发生的情况。然而，使用分布式追踪，工程师可以查看跨各种微服务的交易的完整详细信息。这种可见性有助于管理这些复杂的系统，提供对微服务和整个系统运行所需的洞察。

## 将 OpenTelemetry 与合成监控一起使用

OpenTelemetry 可以通过提高可见性和可测试性来增强合成监控。

### 使用 OpenTelemetry 提高合成监控的可见性

可见性相当简单。如果您在生产环境中运行合成监控器，并且它失败了，哪个工程师不想查看该失败交易的分布式追踪？

您可能会想，“没问题，我会检查我的生产可观测性解决方案并获取追踪。”不幸的是，大多数高流量生产系统依赖于采样，因此从这次特定执行中获取追踪的可能性很小。

其次，即使将采样设置为 100% 的追踪，您仍然需要将一次合成监控交易与该时间窗口内发生的数千次交易相关联。这不是一项容易、快速或可靠的任务。

要使用 OpenTelemetry 提供的可见性，您需要一个合成监控系统，该系统：

- 将父追踪 ID 设置为运行合成测试的一部分，以便您知道哪个追踪属于此运行。
- 将此父追踪 ID 或最好是完整的追踪作为每个测试结果的一部分返回。
- 通过在追踪标志中设置采样标志，将每次执行标记为“必须采样”。

合成监控解决方案需要以 OpenTelemetry 为中心构建。

### 使用 OpenTelemetry 提高合成监控的可测试性

![](https://cdn.thenewstack.io/media/2024/07/50b844b2-image1-2-1024x305.png)

使用可观测性来提高可测试性同样重要。几乎所有基于 API 的合成测试都局限于运行黑盒测试，无法根据被测系统的任何内部细节设置断言。基于浏览器的合成测试虽然可以更深入地了解浏览器的内部结构，但对后端系统也完全一无所知。

幸运的是，OpenTelemetry 通过一种称为 [基于追踪的测试](https://thenewstack.io/trace-based-testing-for-a-distributed-world/) 的技术提供了解决方案。这种方法允许您不仅对 API 调用的结果进行断言，还可以对追踪中公开的任何系统进行断言。您可以向任何合成测试添加各种其他验证，例如：

- 所有数据库查询都应该在 100 毫秒内完成。
- 第三方应用程序应该以特定格式、特定时间长度返回特定响应。
- API 调用甚至可能不会阻塞的异步进程应该成功完成。
- 关键进程必须在特定时间范围内从 Kafka 队列中提取消息。
- 跟踪中的所有 gRPC 调用应返回状态码 0，表示成功。

基于跟踪的测试通过 [使用 OpenTelemetry 公开的可观测性表面](https://thenewstack.io/testing-the-observability-surface/) 来实现。此附加的响应数据可以作为合成 API 或基于浏览器的测试的一部分进行断言。

![](https://cdn.thenewstack.io/media/2024/08/19183f8e-observability-surface-1024x596.png)

### 启用 OpenTelemetry 的合成监控解决方案的优势

使用对 OpenTelemetry 有深入了解构建的合成监控解决方案可以提高可见性和可测试性。利用这种力量的组织将获得许多好处：

- 每个测试都有一个跟踪，可以减少解决故障的时间和精力。
- 使用基于跟踪的测试来验证整个系统流程，可以实现前所未有的端到端测试能力，从而能够对前端和后端进行功能性和非功能性检查。
- 为合成监控创建的基于跟踪的测试可以在 CI/CD 中使用，以主动防止回归。
- 在合成监控中使用 OpenTelemetry 促进了“无处不在的可观测性”理念，并增加了对可观测性投资的使用和价值。

## 关于 Tracetest

[Tracetest](https://tracetest.io/) 是一种现代测试解决方案，它利用 OpenTelemetry 为每个测试提供跟踪和基于跟踪的测试功能。Tracetest 与您现有的测试（如 Playwright、Cypress、Postman 或 k6）以及您现有的生产可观测性解决方案（如 Tempo、Honeycomb、Datadog 或 Dynatrace）协同工作，以主动利用分布式跟踪数据在您的 CI/CD 流程中。现在能够 [运行由 Playwright 测试触发的合成监控](https://tracetest.io/blog/tracetest-playwright-engine-the-future-of-end-to-end-tests-is-trace-based-testing)，Tracetest 充分利用 OpenTelemetry 作为合成监控的一部分。