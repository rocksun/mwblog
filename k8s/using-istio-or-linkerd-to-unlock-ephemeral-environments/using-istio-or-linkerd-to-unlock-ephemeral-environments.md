
<!--
title: 使用Istio或Linkerd解锁短暂环境
cover: https://cdn.thenewstack.io/media/2025/02/f2cf79a2-service-mesh-ephemeral-environment.jpg
-->

> 译自：[Using Istio or Linkerd To Unlock Ephemeral Environments](https://thenewstack.io/using-istio-or-linkerd-to-unlock-ephemeral-environments/)
> 作者：Anirudh Ramanathan

Istio 和 Linkerd 不仅可以管理 Kubernetes 中的流量；它们还可以解锁轻量级、按需的开发和测试环境。

如果您正在使用Istio或Linkerd，那么您已经解决了在Kubernetes中管理流量最困难的部分之一。但您是否知道您也已经完成了90%的工作，可以解锁[短暂环境](https://thenewstack.io/smart-ephemeral-environments-share-more-copy-less)? 这些轻量级、按需环境可以改变您的团队开发和测试应用程序的方式——让您更快地迭代、更安全地部署和获得更好的软件质量。

## 为什么短暂环境很重要

短暂环境提供了巨大的好处。开发人员可以快速获得更改反馈，而无需等待漫长的CI构建。QA团队可以在隔离的、类似生产的环境中验证行为，从而显著降低回归的风险。这种方法促进了持续改进和部署，帮助团队以更高的信心更快地推进发布。

对于现代组织来说，短暂环境正变得至关重要。它们能够加快迭代速度，改进开发人员和QA之间的协作，并通过在开发过程的早期发现问题来降低风险。采用它们的团队可以避免许多与[传统的共享预发布环境相关的陷阱](https://thenewstack.io/why-staging-doesnt-scale-for-microservice-testing/)。

## 为什么服务网格改变了游戏规则

传统的短暂环境方法涉及在单独的[Kubernetes](https://roadmap.sh/kubernetes)命名空间或集群中复制整个微服务堆栈。虽然这提供了隔离性，但它[带来了巨大的挑战](https://thenewstack.io/why-duplicating-environments-for-microservices-backfires/)。生命周期管理变得复杂，基础设施的复制增加了成本，启动时间可能会阻碍彻底的测试。这些环境也可能很快过时，尤其是在快速发展的[微服务架构](https://thenewstack.io/microservices-testing-cycles-are-too-slow)中，如果没有持续更新，测试结果就会不可靠。

一种更有效的方法是利用服务网格的功能来创建基于租户的环境。这种方法不是复制整个堆栈，而是专注于针对Kubernetes集群中已有的共享依赖项测试更改。服务网格处理路由和流量控制，允许多个环境同时运行，而无需复制整个堆栈的成本和复杂性。

![](https://cdn.thenewstack.io/media/2025/02/c1bb81d6-service-mesh-tenancy-based-environments-1024x419.png)

在大规模情况下，请求级租户可以清晰地分割流量，提供隔离的环境，而无需大量复制基础设施。Istio或Linkerd之类的服务网格提供了一种轻量级、可扩展的解决方案，简化了管理并降低了运营成本。

## 现实世界的例子：扩展短暂环境

像Uber和DoorDash这样的行业领导者长期以来一直使用可扩展的、按需环境来降低部署风险并提高开发人员效率。Uber的[SLATE](https://www.notion.so/Istio-or-Linkerd-Unlock-Ephemeral-Environments-Easily-19708fc654be80a4887ce5d5daa5cf8f?pvs=21)允许大规模隔离测试，帮助开发人员尽早发现问题并加快发布速度。DoorDash采用了类似的方法，确保每个更改在进入生产环境之前都经过[隔离测试](https://careersatdoordash.com/blog/moving-e2e-testing-into-production-with-multi-tenancy-for-increased-speed-and-reliability/)。

借助服务网格可观测性和OpenTelemetry之类的工具，团队可以深入了解多个环境中的请求流和性能。这使得调试更快，并防止跨环境干扰。开发人员可以部署具有完整路由控制的隔离服务，并避免冲突，从而更容易发现共享预发布环境经常遗漏的问题。

## 基于租户的短暂环境的工作原理

那么，它是如何工作的呢？想象一下，每个拉取请求都会按需启动一个环境。使用租户，环境共享相同的Kubernetes集群，同时使用请求级租户进行流量控制来隔离资源、路由和数据。

例如：

- 开发人员打开一个拉取请求。
- 构建镜像后，只有更改的服务才会部署到沙箱中的集群中。
- 配置路由规则，以便具有特定标头的请求被定向到新版本的服务——类似于金丝雀在生产环境中的工作方式。
- 开发人员和QA团队在具有共享依赖项的类似生产环境中测试这些更改。
- 拉取请求关闭后，环境会自动清理。

![](https://cdn.thenewstack.io/media/2025/02/3320f2e0-ephemeral-environment-process.png)

**请求租户作为核心组件**

请求级租户高效地管理流量，无需完全隔离的基础设施。Istio 或 Linkerd 等服务网格可以使用唯一的标头来路由和分割每个环境的请求，允许多个环境共存，同时最大限度地减少资源消耗并保持逻辑隔离。

请求租户制的一个关键方面是上下文传播，它允许特定于环境的元数据跨服务边界传输。通过利用[OpenTelemetry (OTel)](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/)和 baggage 传播，此元数据会自动在服务之间传递。这使得一致的环境特定行为和使用服务网格规则的无缝重新路由成为可能。

**处理数据隔离和消息队列**

在共享数据库中，数据隔离至关重要。一种常见的方法是分区数据，通过组织 ID 或用户 ID 等标识符隔离测试，以最大限度地减少干扰。对于模式更改，团队可以启动临时的容器化数据库以确保完全隔离。消息队列隔离可以通过使用标头的消息级路由或通过动态创建临时队列来实现。这些策略支持并行测试，而不会中断共享资源。

## 结论

如果您已经在使用 Istio 或 Linkerd，那么短暂的环境就在您的掌握之中。通过采用基于租户的环境，您将解锁更快的开发周期、更安全的部署和更快乐的开发人员。要更深入地了解技术细节，请查看“[使用 OpenTelemetry 的 Kubernetes 沙箱](https://www.signadot.com/blog/sandboxes-in-kubernetes-using-opentelemetry)”。

像 Signadot 这样的工具超越了自动化，提供了诸如基于本地工作站的环境、对数据库和消息队列的无缝支持以及跨越单个路由上下文中的多个拉取请求的环境等功能。它们提供分析以获得更深入的见解，并帮助平台团队轻松采用和管理这些环境。通过支持本地和基于拉取请求的工作流，自动化测试变得简单明了，使推出更简单，并使团队能够高效地扩展短暂的环境。

所以，还在等什么？立即开始探索基于租户的短暂环境如何改变您的开发工作流程。
