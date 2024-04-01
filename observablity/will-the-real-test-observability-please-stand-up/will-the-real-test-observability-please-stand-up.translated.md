## 真正的测试可观测性请站出来？

![Will the Real Test Observability Please Stand up? 的特色图片](https://cdn.thenewstack.io/media/2024/03/86c39852-penguin-1024x576.jpg)

“测试可观测性”一词已开始出现在技术讨论和产品营销中。然而，它的定义差异很大，有时会被用在可疑的方式中。你可以认为它是一种好的营销，但却是糟糕的技术。让我们讨论一下营销宣传和这些词的实际技术含义。最后，我们希望阐明测试可观测性的真正含义。

### 首先，定义一下

[可观测性](https://thenewstack.io/observability/) 可能会有所帮助。这是一个在软件世界中众所周知且在过去几年中没有发生重大变化的概念。因此，让我们让 Claude AI 为我们提供一个公正的定义：

“测试”一词很容易理解，因此“测试可观测性”

[一定是将可观测性技术应用于测试](https://thenewstack.io/security-testing-must-be-part-of-software-development-life-cycle/) 和测试。

### 一个可能的候选者

BrowserStack 有一款名为“

[测试可观测性](https://www.browserstack.com/test-observability)”的产品。它的解释是：*“*实时测试报告。不稳定检测。人工智能驱动的测试失败调试。自动化运行状况指标跟踪 *”。*

扩展解释如下：

*“*基本测试报告工具会让你淹没在噪音中。测试可观测性会自动识别真正的测试失败，使用人工智能来查找失败原因，并能够主动监控套件运行状况。”

总之，BrowserStack 提供了高级工具来分析测试运行中的失败率。这些工具可以区分无关紧要的噪音和值得进一步检查的重大故障。太棒了！

但这真的是“测试可观测性”吗？从本质上讲，可观测性是关于发现未知的未知。它涉及对系统进行检测，以便在出现问题时，你可以调查并找出根本原因。这种方法不会从对错误的假设开始。相反，它承认意外事件会发生，你需要能够检查系统以了解发生了什么以及为什么发生。

测试管理系统不会将失败的测试运行归类为“内部状态”。测试被执行，并且它要么通过，要么失败。我们理解测试会失败，并且会出现不稳定的测试。我们也认识到需要故障率报告。BrowserStack 提供的服务可以更准确地称为“高级测试运行报告”。如果我们让营销部门添加一些天赋并结合一个时髦的流行语，它可能会被重新标记为“带有 AI 的测试运行报告”。但可观测性呢？

### 对测试可观测性的不同看法

在针对你的系统运行测试时，未知的主要来源是什么？你的系统！它很复杂，它跨许多服务进行交互，并且有许多团队编写的组件，可能使用不同的语言编写。当今运行的大多数测试都是黑盒测试，只返回响应，可能是状态代码和测试持续时间。测试工具可以尝试提供对其他工件的访问，例如来自 Cypress 或 Playwright 测试的记录，以增强你了解故障根本原因的能力，但这仍然很困难，而且这个黑盒子很难看到内部。

在过去十年中，尤其是在过去五年中，公司采用了可观测性技术来解决生产环境中的故障排除复杂性。这些技术也可以在测试和测试环境中采用。

质量保证自动化工程师 [Denis Peganov](https://medium.com/@dees3g) 撰写了一篇题为 [“通过可观测性提升测试质量](https://blog.stackademic.com/elevating-test-quality-through-observability-48926ca90c15)”的优秀博文。他讨论了仅依靠日志进行调试的局限性，以及使用指标和跟踪可以提供以下关键好处：

- 更快的调试
- 根本原因分析
- 主动问题识别
- 改进的测试覆盖率
- 团队协作

### 实施测试可观测性

测试产品开始使用可观测性信号来改进当前测试。他们采用基于标准的可观测性技术来做可观测性擅长的工作——查看黑盒内部。

Grafana 引入了一项功能，允许
## 从 k6 性能测试中捕获分布式跟踪

[Grafana 博客](https://grafana.com/blog/2023/09/19/troubleshoot-failed-performance-tests-faster-with-distributed-tracing-in-grafana-cloud-k6/)

使用 k6 的客户现在可以为性能测试中的每次测试运行捕获分布式跟踪，并将结果存储在 Grafana Tempo 中。以下引文有效地概述了此功能解决的问题：

> “理解性能测试结果并采取相应措施一直是一个挑战。这是因为性能测试的黑盒数据与被测系统的内部白盒数据之间存在可见性差距。”

[Artillery.io](http://artillery.io) 也看到了在运行性能测试时利用指标和跟踪的价值，并 [最近宣布了对 OpenTelemetry 的支持](https://www.artillery.io/blog/introducing-opentelemetry-support)。

[Tracetest](https://tracetest.io/) 在更广泛的背景下解决了这个问题。它适用于任何支持 OpenTelemetry 的后端，包括 Grafana Tempo、AWS X-Ray、Honeycomb 和 Dynatrace。它 [与您现有的测试集成](https://thenewstack.io/the-struggle-for-microservice-integration-testing/) 框架：

- 端到端 (E2E) 前端框架，如 Cypress 或 Playwright
- 性能测试工具，如 k6 或 Artillery
- API 测试，通过导入 Postman 或基于 cURL 的测试

Tracetest 提高了您快速分类失败的能力 [来自任何这些框架的测试](https://thenewstack.io/testkube-cloud-native-testing-framework-for-kubernetes/)。它有助于确定应将错误分配给哪个团队，并提供有关任何故障的可见性和详细信息。这使软件工程师能够快速解决问题。

通过将 Tracetest 添加到您的测试环境中，您现有的测试现在可以使用您当前的可观察性。例如，Playwright 测试结果不仅显示前端工件（如屏幕录制或 API 调用结果），还显示从后端系统捕获的完整分布式跟踪。

可观察性的使用揭示了任何“未知的未知”。通过 [使用 Playwright 测试和调试关键端到端流程](https://tracetest.io/blog/the-lord-of-playwright-the-two-traces) 和 OpenTelemetry 的能力，您可以全面了解整个过程。这使 QA 能够轻松确定问题的根本原因并将其分配给正确的团队。

Tracetest 允许您使用称为“ [基于跟踪的测试](https://thenewstack.io/trace-based-testing-for-a-distributed-world/)”的技术根据分布式跟踪中的数据创建断言。与仅验证调用响应数据的典型黑盒测试不同，基于跟踪的测试允许对任何系统活动进行断言。这种形式的白盒测试实现了真正的端到端测试。

**真正的测试可观察性请站出来！**

显然，将 [可观察性信号（如分布式跟踪）](https://thenewstack.io/observability-distributed-tracing-and-kubernetes-management/) 应用于您的测试可以帮助回答复杂的问题并探索未知的未知。它不仅仅是“高级报告”——它以一种新的但合乎逻辑的方式使用可观察性。它通过利用现有的可观察性，在您的测试环境中实现了更快的 [平均解决时间 (MTTR)](https://thenewstack.io/how-we-slashed-detection-and-resolution-time-in-half/)。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。