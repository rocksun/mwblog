# 将成本效率纳入平台工程以实现增长和盈利能力

翻译 [Factor Cost Efficiency into Platform Engineering for Growth, Profitability](https://thenewstack.io/factor-cost-efficiency-into-platform-engineering-for-growth-profitability/) 。

在平台工程中加入对成本效益的额外关注可以帮助企业度过困难的财务时期，并让它们飞速发展。

![](https://cdn.thenewstack.io/media/2023/03/4a0a0010-shutterstock_1748417273-1024x683.jpg)

这篇文章是 4 月 18 日至 21 日在阿姆斯特丹举行的 [KubeCon + CloudNativeCon Europe 2023](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 预览系列文章之一。加入我们，了解有关云原生应用程序和开源软件的变革性质的更多信息。

平台工程是一种战略性概念，工程师使用单个窗口来简化所有流程、工具和平台。它优化了安全性、 DevOps 、 CloudOps 等方面，使工程师能够更有效地工作，而不需要投入过多的时间和精力。

这种简化消除了在复杂的微服务和云原生环境中工作时产生的大量任务和责任。随着建立应用程序所需的认知负荷减少，更多的产品和服务可以更快地进入市场，支持 CI/CD 实践、自动化、安全和治理。

尽管平台工程如今备受关注，但当前的范式中缺少一个方面，它专注于平衡开发人员时间与应用程序稳定性和性能。这个缺失的组成部分是成本效率，而在当今的经济环境中，这应该是前沿问题。

平台工程应该实现流畅的集成，以实现成本效率的云提供和自动扩展。这样，企业就可以充分获得优化的开发人员时间、性能和成本效益的全部好处。

## 为什么选择平台工程？

DevOps 团队需要跟踪和维护大量技术、基础架构和依赖项。他们常常被无穷无尽的任务和责任压得喘不过气来，使他们忘记了关键的技术依赖性。

平台工程旨在通过创建一个统一的 SaaS 平台来解决这个问题，从而更好地帮助团队构建、部署和运行软件应用。所有工具和依赖项都统一且流程化地集成在一个地方，团队不再需要担心工具或基础架构，可以专注于构建服务，而不是打开工单或等待请求。

## 将云成本纳入其中

平台工程在工程师圈子里正在广泛推广，但将成本效益整合到这一运动中将更有助于组织，确保盈利能力，或至少在开发过程中嵌入成本意识。

平台工程的概念有许多方法可以用来控制成本，许多组织可能会开发自己个性化的系统，但有一些简单的开始方式。

### 成本阈值的自动通知

当工程师构建、编码和交付新应用时，成本通常是他们最不关心的事情。但作为一个组织，需要有人（或某个系统）来确保产品服务的成本得到控制。

这就是自动化的作用。想象一下，如果你可以将工程师已经在使用的平台嵌入自动通知和警报，预测在产生成本之前的成本。例如，如果一个工程师即将启动一个超出预算的云资源，他们将收到有关预计成本和审批提示的通知。

这将提供一个自动的屏障，防止工程师超出预算。此外，它还会让工程团队更加关注和负责他们所产生的成本，鼓励他们提出更具成本效益的发布服务方法。

类似的真实世界例子是 InfraCost，它为 Terraform 拉取请求提供自动云成本估算。当与自动化相结合时，这个工具可以作为一个成本门槛，配备一个审批链，确保成本得到管理和控制。

### 云资源的持续扩展

另一个可以将自动化成本优化解决方案整合到平台工程中的领域是持续扩展云资源以适应业务需求。

今天，云资源过度预配给公司造成了数百万的成本。但解决这个问题是复杂的。限制资源可能导致服务崩溃，而过度预配则昂贵、浪费和效率低下。解决方案是自动扩展云资源，以便以最具成本效益的价格持续满足应用程序需求。

在平台工程角度下，这是什么样子？将这种能力构建到平台中，并将其作为自动化功能提供给开发人员，使他们不再需要进一步考虑它。

一个应用案例是容器，工程师往往难以在复杂和不可预测的环境中分配所需的正确 CPU 和 RAM 。为了确保应用程序的稳定性和性能，他们通常会过度预配这些资源，这不必要地增加了成本。据 Datadog 的数据显示，高达 49% 的容器使用的 CPU 不到请求的 30% ，内存利用率也类似。

将这种自动扩展技术集成到开发人员的流程中可以有效地降低成本，无需任何人工干预。这样的自动资源分配工具将检测需求水平，然后将 CPU 和 RAM 等资源扩展到能够使应用程序在最佳稳定性和性能下运行的水平。在幕后，组织将大幅削减成本，并显著减轻 DevOps 工程师的手动工作和认知负荷。

## 总结

作为 DevOps 和软件工程领域的一种新方法，平台工程因其精简和简化开发者操作的愿景而越来越受欢迎。

将其提升到一个更高的层次，并注入更多的成本效益关注，可以帮助企业度过更困难的财务时期，并在经济形势最终好转时使它们进入增长的飞轮。

平台工程的概念中有许多未被开发的潜力，技术精湛的业务领导者应该考虑如何利用它来开发新的方法，以支持应用程序的稳定性、性能、安全性和成本效益。经济衰退从来不是容易的，但它也为领导者提供了一个很好的机会，去减少低效率，简化流程，从而使您的业务在未来多年中蓬勃发展。