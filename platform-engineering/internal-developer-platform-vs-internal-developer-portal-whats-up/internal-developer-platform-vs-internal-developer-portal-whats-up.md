
<!--
title: 内部开发者平台与内部开发者门户的区别
cover: https://cdn.thenewstack.io/media/2024/05/654a9421-scalable-platform-architecture-real-time-data.jpg
-->

许多人仍然对内部开发者平台和内部开发者门户感到困惑，但两者之间的差异很明显。

> 译自 [Internal Developer Platform vs. Internal Developer Portal: What's Up?](https://thenewstack.io/internal-developer-platform-vs-internal-developer-portal-whats-up/)，作者 Luca Galante。

我敢肯定，你很容易猜到最近在 KubeCon Paris 和 Google Next 24 等技术活动中大家都在谈论什么。是的，[人工智能](https://thenewstack.io/ai/) 当然。今年很难超越它。但看到如此多的会议和对话涵盖了讨论第二多的趋势（远远超过其他所有趋势），这非常有趣（且令人兴奋）：[平台工程](https://thenewstack.io/platform-engineering/)。

Humanitec 在 Next 上与 [Google](https://cloud.google.com/?utm_content=inline+mention) Cloud 和 Thoughtworks 共同协办了一场主平台工程会议，我们几乎无法容纳如此众多的人。

![Google Next 活动](https://cdn.thenewstack.io/media/2024/05/284700d1-google-next-24_idp_humanitec-1024x720.jpg)

*来源：Google*

关于平台工程的对话量逐年增加，但至关重要的是，质量和具体性也在增加。就在两年前的 KubeCon Detroit，我不得不向大多数人解释什么是平台工程。去年，每个人都在谈论它，现在仍然有一些企业级示例[内部开发者平台 (IDP)](https://humanitec.com/blog/what-is-an-internal-developer-platform) 实施被讨论。

今年，[企业级 IDP 的参考架构](https://thenewstack.io/build-your-idp-at-light-speed-with-a-platform-reference-architecture/)的数量大幅增加，并进行了介绍和讨论。我最喜欢的演讲之一是由德国领先的 IT 公司 Bechtle 的 André Alfter 发表的，他介绍了 Bechtle 的[适用于混合高安全设置的 IDP](https://youtu.be/BqH8byL5SHY?si=KyGrb4QTXbiBYnGj&t=290)，其中包括开源工作负载规范 [Score](https://score.dev/) 和 [平台编排器](https://internaldeveloperplatform.org/platform-orchestrators/)。

这一切都很棒，充分说明了平台工程领域正在迅速发展成熟。尚未开展平台计划（或至少在规划中）的企业正在严重冒着落后于竞争对手的风险——从技术上来说，从技术雇主品牌的角度来看，以及从上市时间来看。

然而，该领域仍然存在混乱。在我进行的大量对话中，人们仍然试图理解内部开发者平台和内部开发者门户之间的区别。很多困惑来自人们对两者都使用相同的缩写 IDP。但它们之间的区别现在非常明确且已确立。

## 什么是内部开发者平台（OG）？

[平台工程](https://thenewstack.io/want-to-be-a-tech-company-try-platform-engineering/) 是将工程组织中的技术和工具绑定到黄金路径中的学科，这些路径将复杂性从应用程序开发人员中抽象出来，实现自助服务并减少认知负荷。

这些黄金路径的总和，以及[平台工程团队](https://thenewstack.io/how-platform-teams-can-align-stakeholders/)构建的内容，是一个内部开发者平台，即原始 IDP。

Bechtle 的演讲展示了企业 IDP 的最新参考[架构](https://roadmap.sh/software-design-architecture)示例之一，这些示例遵循了麦肯锡团队[在 PlatformCon23 上提出该概念](https://www.youtube.com/watch?v=AimSwK8Mw-U)以来已成为标准的内容。

![AWS 上 IDP 的示例参考架构](https://cdn.thenewstack.io/media/2024/05/b105acfd-aws-idp-architecture-humanitec-1024x647.png)

*AWS 上 IDP 的示例参考架构*

真正适合企业的 IDP 由以下五个层面组成：

1. **开发者控制平面**：这是平台用户的首要配置层和交互点。组件包括工作负载规范（如 Score）和开发者[门户](https://humanitec.com/internal-developer-portal) 以进行交互。
2. **集成和交付平面**：此平面用于构建和存储映像，创建应用程序和基础设施配置，并部署最终状态。它通常包含一个持续集成 (CI) 管道、一个映像注册表、一个[平台编排器](https://humanitec.com/products/platform-orchestrator)和一个持续交付 (CD) 系统。
3. **资源平面**：这是实际基础设施存在的地方，包括集群、数据库、存储或 DNS 服务。
4. **监控和日志记录平面**：此平面为应用程序和基础设施提供实时指标和日志。
5. **安全平面**：此平面管理秘密和身份以保护敏感信息——例如，存储、管理和安全地检索 API 密钥和凭据或秘密。

企业级平台的核心是一个平台编排器，它是一个核心配置引擎，可以读取开发人员的抽象请求（例如，“我需要一个 Postgres”），并将其与平台工程团队定义的规则和[黄金路径](https://thenewstack.io/humanitec-the-golden-path-to-platform-engineering/)进行匹配。这正是实现遵循最高安全性和合规性标准的真正的开发人员自助服务的原因。平台编排器是 IDP 的后端，平台团队在其中构建了所有核心逻辑。

## 什么是内部开发者门户（前端）？

在此背景下，将门户（如 Backstage）理解为平台的前端非常简单。Gartner 将内部开发者门户定义为“访问内部开发者平台功能的界面”。

![](https://cdn.thenewstack.io/media/2024/05/28580c60-dev-control-plane-idp_humanitec-1024x254.png)

因此，门户基于用户界面 (UI)，而不是 IDP 中的 API、命令行界面 (CLI) 或基于代码的界面（例如，[Score](https://humanitec.com/products/score)）。它们允许[开发人员访问服务目录](https://thenewstack.io/getting-developer-self-service-right/)和脚手架模板，并为他们和其他利益相关者（例如，高管）提供对底层 IDP 的可见性层。

## 从哪里开始？

我希望这有助于阐明内部开发者平台和门户之间的区别。下一个自然而然的问题是您应该从哪里开始。正如在 Salesforce 构建平台的 Aaron Erickson 所[解释](https://platformengineering.org/blog/what-to-build-first-the-house-or-the-front-door)：

> “构建内部开发者平台就像建造房屋。您应该从基础、后端开始，然后稍后添加带有门窗的墙壁（前端）。通过从门户开始构建平台就像通过从前门开始建造房屋一样。”

门户可以成为您的开发人员访问平台的绝佳界面。但请确保您首先获得正确的[后端](https://humanitec.com/blog/why-every-internal-developer-platform-needs-a-backend)。从小处着手。使用[最小可行平台 (MVP) 框架](https://humanitec.com/blog/how-to-build-a-minimum-viable-platform-mvp)快速行动，并在扩展到推出完整的企业级 IDP 之前向所有主要利益相关者证明价值。
