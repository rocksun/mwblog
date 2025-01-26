# 智能短暂环境：共享更多，复制更少

![智能短暂环境：共享更多，复制更少 的特色图片](https://cdn.thenewstack.io/media/2025/01/f03d8ac1-testing12-1024x574.png)

就在上周，我与一家快速发展的安全公司的一位工程总监交谈。其由50名工程师组成的团队实施了一些让我停顿的东西：一个供开发人员在预发布环境中进行测试的注册系统。是的，你没看错：工程师们不得不排队轮流部署和测试他们的代码更改。到周五下午，积压工作会变得令人沮丧地漫长，开发人员不得不等待数小时才能有机会验证他们的工作。虽然有创意，但这清楚地表明了一个更深层次的问题，我在不断发展的工程组织中反复看到过这个问题。

这种情况完美地说明了[传统的微服务测试方法](https://thenewstack.io/we-need-a-new-approach-to-testing-microservices/)如何无法随着团队规模的增长而扩展。当组织将单体应用分解成微服务以实现独立开发和部署时，他们常常忽略了一个关键方面：他们的测试策略也需要发展。

**传统的测试瓶颈**

典型的方法是累积代码更改并[批量在共享环境中测试它们](https://thenewstack.io/why-environment-replication-doesnt-work-for-microservices-testing/)。虽然这最初可能有效，但随着团队规模的增长，它很快就会成为瓶颈。让我描绘一下这在实践中是什么样子：

开发人员进行更改并等待数小时才能将其放入共享环境。当测试失败时，他们被迫切换回数小时前——有时是数天前——编写的代码。如果多个团队都在推送更改，调试就会变成侦探任务。是他们的更改导致问题还是其他人的更改？在最坏的情况下，开发人员开始寻找变通方法，例如直接在生产环境中进行测试，这会导致更多的问题。

**基础设施成本陷阱**

许多组织试图通过创建多个复制的环境来解决这个问题。团队开始启动其基础设施的完整副本，认为这将解决争用问题。例如，以[Brex 的经验](https://www.signadot.com/blog/how-brex-transformed-developer-experience-and-slashed-infrastructure-costs-with-signadot)为例。拥有 1000 多个微服务的架构，它发现预览环境几乎与生产环境一样昂贵。这种方法不仅成本高昂：环境最初需要一个小时才能启动，即使经过大量优化，开发人员仍然面临 20 到 30 分钟的等待时间。

**新的范式：共享基线测试**

像[Uber](https://www.uber.com/blog/simplifying-developer-testing-through-slate/)、[Lyft](https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-3-extending-our-envoy-mesh-with-staging-fdaafafca82f) 和 [DoorDash](https://careersatdoordash.com/blog/fast-feedback-loop-for-kubernetes-product-development-in-a-production-environment/) 等领先科技公司已经开创了一种不同的方法。他们没有[复制整个环境](https://thenewstack.io/why-duplicating-environments-for-microservices-backfires/)，而是转向了一种在共享环境中隔离请求的模型。这种根本性的转变带来了几个关键优势：

首先，它非常具有成本效益。您可以使用传统方法所需基础设施的一小部分来支持数千个并发测试。其次，它速度很快。[开发人员可以在几秒钟内开始测试](https://thenewstack.io/is-the-testing-pyramid-broken/)，而无需等待环境启动。最重要的是，它可以随着团队规模的自然增长而扩展，因为您可以有效地共享基础设施，同时保持测试的完美隔离。

让我深入探讨一下这在实践中是如何运作的。

**共享基线测试的工作原理**

这种方法背后的关键见解是，对于大多数微服务测试，您不需要复制所有基础设施。您只需要控制通过系统的请求路径即可。可以把它想象成有多条平行的车道在同一条高速公路基础设施上行驶。

当开发人员想要测试更改时，他们只需将修改后的服务与现有的生产版本一起部署。特殊的路由规则确保他们的测试流量通过他们版本的服务器，而所有其他流量继续通过生产版本。这种[隔离扩展到整个请求链](https://thenewstack.io/shifting-testing-left-the-request-isolation-solution/)，从而可以安全地测试复杂的端到端场景。
这种方法尤其强大，允许开发人员自然地协作。想测试你的前端更改如何与同事的后端修改一起工作？只需组合你的路由规则，即可在几秒钟内创建一个统一的测试环境。这种灵活性在传统的基于环境的隔离中是根本不可能实现的。

**现实影响**

这种方法的影响不仅仅是节省基础设施成本。在Brex，转向这种模式不仅大大降低了其基础设施支出，而且还带来了开发人员生产力和代码质量的显著提升。工程师可以更快地迭代，从而导致更改更小、更集中，并降低更改失败率。

但开发人员行为的变化也许是最具说服力的影响。当测试变得快速且无摩擦时，团队自然会采用更好的实践。他们不再批量更改以避免环境设置时间，而是更频繁地进行测试。他们不再编写大型、高风险的更改，而是将其分解成更小、更易于管理的部分。结果是一个更可持续和可扩展的开发流程。

**Signadot 方法**

在Signadot，我们构建了一个平台，它将共享基线测试的强大功能带给任何使用Kubernetes的团队，而无需像Uber和Lyft这样的公司在内部进行大规模的工程投资。只需一个拉取请求，开发人员即可立即访问与生产环境完美镜像的隔离测试环境，消除了传统方法带来的等待时间和调试难题。

你想开始吗？查看我们的[快速入门](https://www.signadot.com/docs/tutorials/quickstart/first-sandbox)指南或加入我们的[Slack 社区](https://signadotcommunity.slack.com/join/shared_invite/zt-1estxm8pv-qfiaNfiFFCaW~eUlXsVoEQ#/shared-invite/email)向其他已完成此转换的人学习。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。