<!--
# 平台工程的支柱之三：Provisioning
https://cdn.thenewstack.io/media/2023/09/66573c34-pillar-capitals-2135682_1280-1024x492.jpg
-->

为平台团队提供在其平台中建立 Provisioning 的工作流程和清单。

译自 [The Pillars of Platform Engineering: Part 3 — Provisioning](https://thenewstack.io/the-pillars-of-platform-engineering-part-3-provisioning/)。

*本指南概述了平台工程中开发者体验的六大主要技术领域的工作流程和步骤。该指南分为六个部分发布，第一部分介绍了该系列并关注了安全性。第二部分将介绍应用程序部署管道。指南的其他部分如下所列，您也可以下载[完整的 PDF 版本](https://www.hashicorp.com/on-demand/the-six-pillars-of-platform-engineering?utm_source=partner&utm_medium=email&utm_campaign=24Q3_WW_SIXPILLARSOFPLATFORMENGINEERING_WP&utm_content=&utm_offer=whitepaper)以获取完整的指导、大纲和清单。*

1. [安全性(包括简介)](https://yylives.cc/2023/09/24/the-6-pillars-of-platform-engineering-part-1-security/)
2. [流水线(VCS、CI/CD)](https://yylives.cc/2023/09/24/the-6-pillars-of-platform-engineering-part-2-ci-cd-vcs-pipeline/)
3. Provisioning
4. 连接性
5. 编排
6. 可观测性(包括总结和下一步)

在前两个支柱中，平台团队提供自助服务 VCS 和 CI/CD 流水线工作流程，其中内置了安全工作流程，以从一开始就充当护栏。这些是软件交付的第一步。现在您有要运行的应用程序代码，您将在哪里运行它？

每个 IT 组织都需要一个基础设施计划作为其应用程序的基础，平台团队需要将该计划视为其计划的基础。他们的首要目标是消除基础设施 Provisioning 的工单驱动工作流程，这在现代 IT 环境中不可扩展。平台团队通常通过为开发人员提供标准化的共享基础设施 Provisioning服务以及精心策划的自助服务工作流程、工具和模板来实现此目标。然后，他们将这些工作流程与前两个支柱的工作流程连接起来。

建立一个有效的现代基础设施平台取决于[基础设施即代码](https://www.hashicorp.com/resources/what-is-infrastructure-as-code)的采用。当基础设施配置和自动化编码化时，即使是最复杂的 Provisioning 场景也可以自动化。然后可以对基础设施代码进行版本控制，以便于审核、迭代和协作。采用基础设施即代码有几种解决方案，但最常见的是 [Terraform](https://www.terraform.io/)：一种 Provisioning 解决方案，其使用比竞争工具[更广泛](https://survey.stackoverflow.co/2023/#section-most-popular-technologies-other-tools)。

Terraform 是采用基础设施即代码的组织首选，因为它有一个大的集成生态系统。这个生态系统帮助平台工程师满足 Provisioning 平台的最后一个主要需求：可扩展性。广泛的插件生态系统允许平台工程师快速采用开发人员希望部署的新技术和服务，而无需编写自定义代码。

## Provisioning：模块和镜像

构建标准化的基础设施工作流程需要平台团队将其基础设施分解为可重用的、理想情况下是不变的组件。[不变的基础设施](https://www.hashicorp.com/resources/what-is-mutable-vs-immutable-infrastructure)是现代 IT 中的一个常见标准，它减少了复杂性，简化了故障排除，同时也提高了可靠性和安全性。

不变性意味着删除和重新 Provisioning 所有更改的基础设施，这将最小化服务器修补和配置更改，有助于确保每次服务迭代都会启动一个经过测试和最新实例。它还强制运行手册验证并促进故障转移和[金丝雀](https://martinfowler.com/bliki/CanaryRelease.html)部署练习的定期测试。许多组织通过使用 Terraform 或其他 Provisioning 工具来构建和重建大量基础设施，方法是修改配置代码。一些还构建[黄金镜像流水线](https://developer.hashicorp.com/packer/tutorials/cloud-production/golden-image-with-hcp-packer)，专注于构建和持续部署可重复的机器镜像，这些镜像经过测试和确认符合安全和策略合规性(黄金镜像)。

除了机器镜像之外，现代 IT 组织还将其基础设施代码模块化，将常用组件组合成可重用的模块。这很重要，因为软件开发的一个核心原则是“不重造轮子”的概念，它也适用于基础设施代码。模块创建轻量级抽象来描述基础设施的术语，而不是离散对象。它们通常通过版本控制进行管理，并与第三方系统(如服务目录或测试框架)进行交互。

高性能 IT 团队汇集黄金图像管道和自己的模块注册表，供开发人员在为其应用程序构建基础设施时使用。在对此基础设施及其设置的内部工作原理几乎不了解的情况下，开发人员可以在可重复、可扩展和可预测的工作流程中使用基础设施模块和黄金镜像管道，该工作流程在第一次部署时内置了安全性和公司最佳实践。

### 工作流程：Provisioning 模块和图像

典型的 Provisioning 工作流程将遵循以下六个步骤:

1. **代码**：开发人员提交代码并向流水线提交任务。
2. **验证**：CI/CD平台向您的IdP提交验证请求(AuthN和AuthZ)。
3. **IdP 响应**：如果成功，流水线会触发任务(例如测试、构建、部署)。
4. **请求**：CI/CD自动化工作流程用于构建模块、工件、图像和/或其他基础设施组件。
5. **响应**：将响应(成功/失败和元数据)传递给CI/CD平台。
6. **输出**：部署或存储基础设施组件，如模块、工件和图像配置。

![](https://cdn.thenewstack.io/media/2023/09/cb510842-hashicorp-3-01.jpg)

*模块和图像 Provisioning 流程*

## Provisioning：策略即代码

敏捷开发实践已经将基础设施 Provisioning 的重点从运营问题转移到应用交付预期。基础设施 Provisioning 现在是业务成功的制约因素。其价值与推动组织战略和客户任务保持一致，而不仅仅是基于控制运营支出。

在转向应用程序交付预期时，我们需要转变工作流程和流程。从历史上看，运营人员通过利用工单对 Provisioning 过程应用工作流程和投诉。这些工单通常涉及验证访问权限、审批、安全性、成本等。整个过程也为合规性和控制实践进行审计。

现在必须改变这个过程，以使开发人员和其他平台最终用户能够通过自助服务工作流进行 Provisioning 。这意味着必须实施一组新的编码安全控制和护栏，以满足合规性和控制实践。

在云原生系统中，这些控制通过策略即代码来实现。[策略即代码](https://docs.hashicorp.com/sentinel/concepts/policy-as-code)是一种使用可编程规则和条件来部署软件和基础设施的做法，它将最佳实践、合规性要求、安全规则和成本控制编码化。

一些工具和系统包括自己的策略系统，但也有与多个系统集成的更高级别的策略引擎。基本要求是这些策略系统可以以代码的形式进行管理，并将对工作流程中的人员和系统提供评估、控制、自动化和反馈循环。

实施策略即代码有助于通过在 Provisioning 过程的更早阶段向用户提供反馈并使他们能够更快地做出更好的决定，从而将工作流程“左移”。但是在可以使用它们之前，需要编写这些策略。平台团队应该拥有策略即代码的做法，与安全、合规、审计和基础设施团队合作，确保策略与风险和控制措施正确匹配。

## 工作流：策略即代码

在基础设施 Provisioning 工作流中实施策略即代码检查通常涉及五个步骤：

- **代码**：开发人员提交代码并向流水线提交任务。
- **验证**：CI/CD 平台向您的 IdP 提交验证请求(AuthN 和 AuthZ)。
- **IdP 响应**：如果成功，流水线将触发任务(例如测试、构建、部署)。
- **请求**： Provisioning 商通过策略引擎运行计划的更改，如果代码没有通过策略测试，则请求将被允许通过(有时会发出警告)或被拒绝。
- **响应**：元数据响应数据包发送到 CI/CD，然后发送到外部系统，例如安全扫描或集成测试。

![](https://cdn.thenewstack.io/media/2023/09/dda8fd00-hashicorp-3-02.jpg)
*具有策略即代码的 Provisioning 流程*

## Provisioning 需求清单

自助服务基础设施 Provisioning 成功所需的:

- 端到端自动化的统一控制和数据平面
- 自动化配置(基础设施即代码、运行手册)
- 预定义和完全可配置的工作流程
- 与 VCS 和 CI/CD 工具的本地集成
- 业务所需的各种容器和虚拟机镜像
- 针对不同人员和工作流程的多种接口(GUI、API、CLI、SDK)
- 使用广泛采用的基础设施即代码语言 - 强烈建议使用声明式语言
- 与行业标准测试和安全框架、数据管理(加密)和机密管理工具的兼容性
- 与通用工作流组件(如通知工具和 Webhook)的集成
- 支持编码化护栏，包括：
  - 策略即代码：内置的策略即代码引擎，具有可扩展的集成
  - RBAC：精细范围的权限来实现最小特权原则
  - 基于令牌的访问凭证来认证自动化工作流程
- 规定使用组织批准的模式和模块
- 与可靠的身份提供程序集成，具有单点登录和RBAC
- 维护资源 Provisioning 元数据(状态、图像、资源等):
  - 通过默认拒绝 RBAC进行控制
  - 加密
  - 人类和/或机器可以通过可编程接口访问
  - 通过可跟踪的配置保持逻辑隔离存储
- 可扩展到大型分布式团队
- 支持公共和私有模块
- 完整的审计日志记录和日志流功能
- 财务运营(FinOps)工作流程来执行基于成本的策略和优化
- 明确定义的文档和开发者启用功能
- 基于 SLA 的企业支持(例如 24/7/365)

敬请关注我们对平台工程第四个支柱的文章：连接性。或者下载《[平台工程的六大支柱](https://www.hashicorp.com/on-demand/the-six-pillars-of-platform-engineering?utm_source=partner&utm_medium=email&utm_campaign=24Q3_WW_SIXPILLARSOFPLATFORMENGINEERING_WP&utm_content=&utm_offer=whitepaper)》的完整 PDF 版本，以获取完整的指导、大纲和清单。