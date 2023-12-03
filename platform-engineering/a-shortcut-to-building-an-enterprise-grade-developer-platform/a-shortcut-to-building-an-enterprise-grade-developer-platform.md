<!--
title: 快速建立企业级开发者平台
cover: https://cdn.thenewstack.io/media/2023/11/c3ba43c6-shortcut-1024x573.jpg
-->

Humanitec推出了面向AWS和GCP平台的、专门定制的开源参考架构实现代码。

> 译自 [A Shortcut to Building an Enterprise-Grade Developer Platform](https://thenewstack.io/a-shortcut-to-building-an-enterprise-grade-developer-platform/)，作者 Luca Galante。

设计一个有效的内部开发者平台(IDP)是一个非常耗时的过程。这不仅涉及确定所需的基本组件，还包括在不断扩大和复杂的工具环境中选择最合适的技术。为了加快这个过程，Humanitec 公开了基于[亚马逊网络服务(AWS)](https://github.com/humanitec-architecture/reference-architecture-aws)和[谷歌云平台(GCP)](https://github.com/humanitec-architecture/reference-architecture-gcp)平台的[参考架构](https://thenewstack.io/build-your-idp-at-light-speed-with-a-platform-reference-architecture/)实现代码。

这一最新进展可以加快整个设计过程，并在一个小时内而不是几个月内轻松构建一个最小可行产品(MVP)。为了提供更多支持，我们推出了一个[学习路径](https://developer.humanitec.com/training/master-your-internal-developer-platform/introduction/)，介绍如何掌握 IDP 并使用 Backstage、Humanitec 平台编排器、Score 和您选择的云提供商设置引用架构。该学习路径将引导您完成[开发人员和平台工程师](https://thenewstack.io/platform-engineering-benefits-developers-and-companies-too/)的日常任务，在动手实践中运行应用程序和修改设置。

在我们深入探讨什么和如何之前，让我们看一下为什么需要[构建企业级 IDP](https://thenewstack.io/heres-one-golden-path-to-build-an-mvp-enterprise-idp/)。

## 通过内部开发者平台缩短上市时间

当实施有效时，内部开发者平台有助于显着简化软件交付过程。正如我们的 CEO Kaspar von Grünberg 所强调的那样，“[内部开发者平台(IDP)](https://humanitec.com/blog/what-is-an-internal-developer-platform)是平台工程团队绑定在一起的所有技术和工具的总和，为开发者铺平黄金路径。IDP 在整个工程组织中降低了认知负载，实现了开发者的自助服务，而没有从开发者那里抽象出上下文，也没有使基础技术变得不可访问。”

使用 IDP 的组织可以在应用程序和基础架构配置中实现标准化。这赋能开发者在整个应用生命周期中进行自助服务，消除了等待运维支持的需要，从而提高了生产力。减少运维瓶颈有助于更高效的工作流程。此外，IDP 通过允许开发者在保持基础技术可访问的同时选择抽象来[减轻开发者的认知负担](https://thenewstack.io/cyberark-decreases-cognitive-load-with-platform-engineering/)。

从业务角度来看，这些好处转化为有形的优势。当开发者可以更多地关注编码时，[组织可以将上市时间缩短 30%，实现四倍更高的部署频率，并缩短 30% 的前置时间](https://humanitec.com/why-humanitec？)。这些改进对于培育收入增长并使企业具备快速响应竞争对手、不断变化的客户需求和市场动态的敏捷性至关重要。

## 为什么需要 IDP 参考架构？

当涉及到设计和构建 IDP 时，每个平台看起来都不同。直到最近，平台团队还没有标准的、经过验证的、可扩展的或可重复的模式可供遵循。您的 IDP 最终会有什么样取决于您已经在使用的技术、您想要摆脱和保留的技术，以及您想要设计的黄金路径。您组织的规模、首选的开发人员工作流程以及法规等外部因素也会影响 IDP 的结果。因此，不同公司采用非常不同的方法来构建其 IDP 是很自然的。

在 2023 年的 [PlatformCon](https://platformcon.com/) 上，McKinsey 的 Stephan Schneider 和 Mike Gatto 展示了他们基于[亚马逊网络服务(AWS)](https://aws.amazon.com/？utm_content=inline-mention)的最新的 IDP 参考架构，结合从许多现实世界的平台设置中获得的见解和共性。他们的演讲题为“[平台即代码：使用参考架构简化开发者平台设计](https://www.youtube.com/watch？v=AimSwK8Mw-U)”，启发我们为基于 [AWS、Azure 和 GCP](https://humanitec.com/reference-architectures) 的设置开发自己的 IDP 参考架构。这些资源旨在帮助组织快速设计、构建和部署企业级 IDP。

![](https://cdn.thenewstack.io/media/2023/11/b0088e77-aws1.jpg)

![](https://cdn.thenewstack.io/media/2023/11/603ba0f0-gcp1.jpg)

## 关键的平台架构组件

参考架构中规定了五个主要的平面，组成平台的不同领域。尽管参考架构的目标是为您提供一个起点，但应考虑每个组织上下文中的现有资产，以结合已有的组件:

### 开发者控制平面

这个平面是平台用户的主要配置层和交互点。它包含以下组件:

- 一个版本控制系统。GitHub 是典型的例子，但这可以是包含两种类型存储库的任何系统:
  - 应用源代码
  - 平台源代码，例如使用 Terraform
- 工作负载规范。参考架构使用 Score。
- 供开发人员交互的门户。它可以是 [Humanitec 门户](https://humanitec.com/products/portal)，您也可以使用 [Backstage](https://humanitec.com/blog/humanitec-vs-backstage-friends-or-foes) 或市场上的任何其他门户。

### 集成和交付平面

这个平面是关于构建和存储镜像，从开发人员提供的抽象中创建应用程序和基础架构配置，以及部署最终状态。这是开发人员和平台工程师领域的交汇点。

这个平面通常包含四种不同的工具:

- CI 流水线。它可以是 GitHub Actions 或市场上的任何 CI 工具。
- 保存您的容器镜像的镜像 registry。同样，这可以是市场上的任何 registry。
- 编排器，在我们的示例中，是 Humanitec [平台编排器](https://humanitec.com/products/platform-orchestrator)。
- CD 系统，可以是平台编排器的部署流水线功能 - 由编排器使用 Webhook 触发的外部系统，或与 GitOps 操作员(如 Argo CD)配合使用的设置。

### 监控和日志记录平面

监控和日志记录系统的集成因系统而异。然而，参考架构并未关注这个平面。

### 安全平面

参考架构的安全平面专注于机密管理系统。机密管理器存储诸如数据库密码、API 密钥或 TLS 证书等配置信息，应用程序在运行时需要这些信息。它允许平台编排器引用机密并将其动态注入到工作负载中。

参考体系结构的示例实现使用 Humanitec SaaS 系统附带的机密存储。

### 资源平面

这一平面是实际基础设施所在的位置，包括集群、数据库、存储或 DNS 服务。资源的配置由平台编排器管理，它使用每个部署动态创建应用程序和基础架构配置，并根据需要创建、更新或删除依赖的资源。

当涉及到这些平面的组装时，某些层的集成更直观。例如，平台团队负责将各个平面组件彼此连接起来，以及将一个平面绑定到另一个平面上。端到端流也必须进行测试和优化，以确保无缝集成和最佳的开发人员体验。

## 工作机制

所以，我们知道企业级 IDP 可以带来的好处。 我们已经确定了组成 IDP 的组件。 并且我们已经建立了使用开源实现代码快速实现 MVP 的潜力。 但是它是如何协同工作的呢？

通过使用我们的开源工作负载规范 Score，开发人员描述他们的应用程序是如何组合在一起的，并定义它们所依赖的资源。 Humanitec 平台编排器根据平台团队建立的基线配置调整这些请求。 通过每次 git 提交，平台编排器会解释工作负载操作所需的配置和资源，根据平台团队预定义的规则生成应用程序和基础架构配置。 然后，它将按照“读取” - “匹配” - “创建” - “部署”的模式执行它们：

- 读取：解释工作负载规范和上下文。
- 匹配：确定正确的配置基线以创建应用程序配置，并根据匹配的上下文确定要解析或创建的资源。
- 创建：创建应用程序配置;如果必要，创建(基础架构)资源，获取凭据并将凭据注入为机密。
- 部署：将工作负载部署到针对其依赖项连接的目标环境。

## 迈向构建您的MVP

就是这样。 您的组织现在有了一种以最快速度构建有效的企业级 IDP 的方法。 用于 AWS 和 GCP 设置的新开源实现代码是平台工程社区的一个令人兴奋的新发展，它将为您节省设计过程中的数小时时间。

![](https://cdn.thenewstack.io/media/2023/11/243b8eaf-image2.png)

准备更进一步接近有效IDP的MVP？ 如下所示:

- [创建](https://humanitec.com/free-trial)您的 [Humanitec 帐户](https://humanitec.com/free-trial)。
- 要快速搭建 IDP，请查看我们的[参考架构](https://github.com/humanitec-architecture):
  - [AWS 的开源参考架构](https://github.com/humanitec-architecture/reference-architecture-aws)
  - [GCP 的开源参考架构](https://github.com/humanitec-architecture/reference-architecture-gcp)
- 扩展您的平台知识，探索我们的[学习路径](https://developer.humanitec.com/training/master-your-internal-developer-platform/introduction/)。

祝您搭建开发者喜爱的 IDP 的过程充满乐趣！
