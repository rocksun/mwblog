
<!--
title: 您的微服务集成测试为何错过实际问题
cover: https://cdn.thenewstack.io/media/2024/12/5976d0c1-microserviceintegrationtestsmissproblems.jpg
-->

沙箱环境允许分支版本与主干/主版本的服务交互，从而实现比模拟更真实的集成测试。

> 译自 [Why Your Microservice Integration Tests Miss Real Problems](https://thenewstack.io/why-your-microservice-integration-tests-miss-real-problems/)，作者 Arjun Iyer。

在最近对构建微服务的工程团队进行的调查中[building microservices](https://thenewstack.io/how-to-apply-microservice-architecture-to-embedded-systems/)，出现了一个显著的模式：尽管大多数团队都理解其重要性，但大多数团队都跳过了服务级别的全面集成测试。这并不是因为工程师不重视测试——恰恰相反。真正的罪魁祸首是什么？在分布式系统中实施强大的集成测试策略的复杂性令人难以承受。

作为一名多年来一直致力于构建开发者工具并与工程团队合作的人，我亲眼目睹了这一挑战如何影响速度和可靠性。成本不仅仅在于潜在的生产问题；还在于团队花费无数小时调试本来可以更早发现的集成问题。

## 集成测试：一个复杂的网络

考虑一个典型的[微服务环境](https://thenewstack.io/microservices/)。您的团队刚刚实现了一个跨越多个服务的新的功能。在合并之前，您希望确保它能够与其依赖项（数据库、消息队列和其他服务）正确协同工作。听起来很简单，对吧？

事情就是这样变得混乱的。

传统的集成测试方法通常涉及创建复杂的模拟依赖项网络。团队通常遵循以下两种路径之一：

1. **“模拟一切”方法**：使用诸如[TestContainers](https://thenewstack.io/what-is-testcontainers-and-why-should-you-care/)或[WireMock](https://thenewstack.io/vendors-address-the-explosion-in-api-use/)之类的工具，团队为每个依赖项创建精心设计的模拟。维护模拟成为一项全职工作。最糟糕的是？您永远无法确定您的模拟是否准确地反映了生产行为。
2. **Docker Compose 路线**：团队使用 Docker Compose 或类似工具启动一部分服务。虽然这比纯模拟提供了更真实的运行环境，但它仍然远非生产现实。随着每项额外服务的增加，复杂性呈指数级增长。

![](https://cdn.thenewstack.io/media/2024/12/998ed8f4-traditional-testing-1024x640.png)

上图说明了传统集成测试方法的复杂性，其中每个依赖项都需要在 CI 环境中进行模拟。

## 隐藏成本

这些方法带来了巨大的隐藏成本：

* 维护负担：模拟服务需要不断更新以保持与实际服务行为同步。
* 虚假的信心：在高度模拟的环境中通过的测试并不能保证生产成功。
* 时间投入：设置和维护测试基础设施通常比编写实际测试花费更长时间。
* 可扩展性问题：随着服务数量的增长，维护测试环境的复杂性呈指数级增长。

## 新方法：实时环境中的沙箱

如果我们不与分布式系统的复杂性作斗争，而是接受它呢？这就是[沙箱](https://thenewstack.io/why-duplicating-environments-for-microservices-backfires/)的概念，轻量级环境能够实现“金丝雀式”的集成测试。

![](https://cdn.thenewstack.io/media/2024/12/19e2e8e5-sandbox-testing-1024x512.png)

上图显示了沙箱环境如何通过允许分支版本与服务的trunk/main版本交互来实现真实的集成测试。

以下是它的工作原理：

1. 对于每个拉取请求，都会自动创建一个轻量级沙箱环境。
2. 您服务的分支版本在此沙箱中运行，但可以与基线环境中的实际依赖项交互。
3. 集成测试针对此沙箱运行，提供有关您的更改在生产环境中的行为的真实反馈。

这种我们在 Signadot 中实现的方法解决了传统集成测试的核心挑战：

* 速度：开发人员无需复杂的设置即可立即获得其更改的反馈。
* 可扩展性：每个团队都可以管理自己的测试，无需集中协调。
* 可靠性：测试提供高质量的信号，因为它们针对实际依赖项运行。

## 通过服务比较实现高置信度集成测试

![](https://cdn.thenewstack.io/media/2024/12/538efd3a-comparison-testing-1024x512.png)

这种方法最强大的方面之一是能够执行全面的比较测试。通过针对服务的分支版本和基线版本运行测试，团队可以自动检测各种问题：

* [API](https://roadmap.sh/api-design)契约更改和兼容性中断，
* 性能回归和延迟峰值，
* 服务交互中的行为差异，
* 资源利用异常（CPU、内存等），
* 日志模式的意外更改和
* 错误率变化。

这就是 AI 和机器学习展现其真正潜力的领域。Signadot 最近推出的 [SmartTests](https://www.signadot.com/ai-smart-tests) 功能利用 AI 模型学习基线服务行为并自动识别重大偏差。

![](https://cdn.thenewstack.io/media/2024/12/da609eca-api-call-comparison-1024x786.png)

这种基于比较的系统可以：

- 分析日志模式以检测异常行为，
- 比较资源利用率配置文件以捕获潜在的内存泄漏或 CPU 尖峰，
- 识别服务交互模式的细微变化，以及
- 标记错误率或响应模式的意外变化。

这种方法的优势在于其可扩展性。团队可以在基础之上叠加额外的比较用例。无论您是感兴趣比较 API 响应、分析性能指标还是监控资源使用模式，沙箱基础设施都为此类复杂的比较测试提供了理想的基础。

记住，目标不仅仅是测试更多——而是更智能地测试。在当今的分布式系统世界中，这意味着采用[与您的架构一起扩展的方法](https://thenewstack.io/why-staging-doesnt-scale-for-microservice-testing)，并在开发人员最需要时向他们提供有意义的反馈。

了解更多关于 [SmartTests](https://www.signadot.com/ai-smart-tests) 的信息，并加入我们在 [Signadot 社区 Slack 频道](https://signadotcommunity.slack.com/join/shared_invite/zt-1estxm8pv-qfiaNfiFFCaW~eUlXsVoEQ#/shared-invite/email) 的从业者社区。
