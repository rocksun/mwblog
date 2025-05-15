
<!--
title: 协调微服务变更仍然很麻烦
cover: https://cdn.thenewstack.io/media/2025/04/8a2d173d-microservices-mess.jpg
summary: 微服务变更协调难？传统模式面临挑战！多租户共享环境是解法：利用 Kubernetes 和 Service Mesh (如 Istio/Linkerd)实现智能路由，无需克隆环境即可进行集成测试。Signadot 提供相应支持，加速反馈，提升交付信心。
-->

微服务变更协调难？传统模式面临挑战！多租户共享环境是解法：利用 Kubernetes 和 Service Mesh (如 Istio/Linkerd)实现智能路由，无需克隆环境即可进行集成测试。Signadot 提供相应支持，加速反馈，提升交付信心。

> 译自：[Why Coordinating Microservice Changes Is Still a Mess](https://thenewstack.io/why-coordinating-microservice-changes-is-still-a-mess/)
> 
> 作者：Anirudh Ramanathan

“嘿，先别合并，我还需要用我的服务进行测试。” 听起来是不是很熟悉？

在功能开发期间协调[微服务](https://thenewstack.io/microservices/)的变更总是开始得很简单。当你的整个堆栈可以放在一个代码仓库或一个EC2盒子里时，这没什么大不了的。但快进一下，你就会发现自己要协调 20 个、40 个，甚至数百个由不同团队拥有、按照不同时间线移动，并且以微妙的、未记录的方式相互依赖的服务。

突然，对内部[API](https://roadmap.sh/api-design)的一个小改动破坏了别人的暂存环境。一个前端拉取请求（PR）卡在等待后端部署。你又在 Slack 中说：“谁能用最新的 main 重新部署 user-service 吗？” 本应花费五分钟的事情却花费了一整天。

实际上，大多数功能都不是孤立的。一项新的能力通常意味着要修改前端、调整 API 并更新几个后端服务。你希望看到所有这些部分如何协同工作，而无需费尽周折。

“但我认为微服务是为了分离事物，而不是耦合它们。” 嗯，是的，你希望独立地推出服务。但这并不意味着你不应该先一起测试它们。仅仅因为服务可以单独部署并不意味着它们的功能是孤立存在的。在开发过程中测试它们的交互方式仍然至关重要。能够跨服务一起测试正在进行的更改，而无需提前合并或协调全面推出，不应该那么困难。

## 我们看到的三种痛苦的方法

在实践中，团队通常会陷入以下三种情况之一，没有一种是好的：

- **YOLO 模式。** 推送到暂存环境，希望一切都不会崩溃，当它不可避免地崩溃时，欢迎来到 Slack 分诊时间。团队不断互相踩踏，共享环境在测试过程中崩溃。团队将更改推送到共享的暂存或质量保证（QA）环境，意外地破坏了彼此，并花费数小时[解开混乱](https://thenewstack.io/the-staging-bottleneck-microservices-testing-in-fintech)。
- **通过仪式保证安全。** 一切都[被标记包裹和延迟](https://thenewstack.io/the-million-dollar-problem-of-slow-microservices-testing)。现在你需要三个开关和一个电子表格才能发布一个按钮。
- **克隆并祈祷。** 为每个分支启动一个完整的堆栈，花费数小时进行设置，并花费更多的时间来调试配置漂移。希望你记得关闭它。浪费时间，浪费预算，并调试相同的[配置漂移](https://thenewstack.io/scale-microservices-testing-without-duplicating-environments)。

![Drawbacks of common microservices testing approaches: YOLO mode, safety by ceremony, clone and pray](https://cdn.thenewstack.io/media/2025/04/e3528a4d-microservices-testing-drawbacks-1024x515.png)

*来源：Signadot。*

这些都不是理想的。但是现在有更多的团队正在采用第四种选择：使共享环境成为多租户的。

## 轻量级替代方案：多租户共享环境

这里的核心思想很简单：停止争夺单个共享集群。相反，使其成为多租户的。

这不是一个幻想的设置；这是一种经过验证的、大规模使用的模式。Lyft 的[暂存覆盖](https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-3-extending-our-envoy-mesh-with-staging-fdaafafca82f?gi=bcf1f4e80699)方法使用 Envoy 及其服务网格将共享环境中的流量路由到正在测试的服务的正确版本，具体取决于谁在发出请求。无需完整克隆，无需隔离技巧 - 只是智能路由。

这种“暂存覆盖”的概念使开发人员可以运行真实的集成测试，使用真实的依赖项，在对其他所有人保持稳定的环境中。你可以获得快速的、上下文相关的反馈，而无需模拟整个世界。

像 Istio 或 Linkerd 这样的服务网格[使这种模型得到广泛应用](https://thenewstack.io/using-istio-or-linkerd-to-unlock-ephemeral-environments/)。它们允许你启动服务的预览版本，并根据请求元数据将流量路由到它们。这可以保持你的测试隔离，同时共享底层的基础设施。

没有模拟，没有手动协调，没有专用的暂存集群。

![Multitenant shared environments use sandboxes and staging overlays](https://cdn.thenewstack.io/media/2025/04/1953a400-multitenant-shared-environment.png)

*来源：Signadot。*

## 为什么这如此有效？

这种方法的真正魔力在于它不需要重新发明你的堆栈。它构建在你现有的 [Kubernetes](https://roadmap.sh/kubernetes) 集群和[服务网格](https://thenewstack.io/service-mesh/)之上，以智能地路由流量。你可以在需要的地方获得隔离，在不需要的地方共享基础设施。

假设你有一个后端变更和一个前端变更，它们分别位于不同的 PR 中。使用这种方法，你可以将两者部署到相同的路由上下文中。服务网格将确保来自你的测试会话的请求命中正确版本的服务，而所有其他依赖项都从基线环境中提取。这意味着你正在测试真正的集成，而不会破坏或复制任何内容。

![智能路由将特定请求定向到特定服务版本](https://cdn.thenewstack.io/media/2025/04/6004cc23-service-mesh-routing.png)

*来源: Signadot.*

通过将特定请求定向到特定服务版本，你可以验证任意数量的变更，无论是一个、两个还是多个，而不会中断其他人。开发人员可以跨服务组合进行中的 PR，以重现真实的工作流程，同时保持环境对所有其他人来说都是干净且可预测的。

这种基于路由的模型显著改善了开发人员的体验。它缩短了反馈循环，减少了协调开销，并允许团队测试真正的集成，而不是伪造它们。随着你的服务数量的增长，它可以自然地扩展，因为你不是在克隆整个环境，而只是更智能地路由流量。

## 总结

现代开发团队需要更快、更安全的方式来验证跨服务的变更，尤其是在这些变更跨越多个存储库、团队或堆栈层时。传统的做法在规模和复杂性的重压下正在崩溃。

我们不仅仅是在谈论改进暂存环境。我们正在谈论一个根本性的转变：在不减慢团队速度的情况下，在开发过程中实现有意义的集成测试。由智能路由和覆盖支持的共享、多租户环境为团队提供了一条清晰的前进道路。

这不仅仅是一种更好的开发人员体验。这是一种在不偷工减料的情况下更快地行动，并测试系统实际存在的方式，而不是一些模拟的模拟。采用这种模型的团队不仅交付速度更快，而且对他们交付的产品也更有信心。

加速反馈。减少流失。充满信心地交付。

[Signadot](https://www.signadot.com/) 帮助团队采用这种模型，而无需复杂性。启动隔离的测试上下文，将其范围限定为你的变更，智能地路由流量，并在几分钟（而不是几天）内验证跨服务的功能。