
<!--
title: Pulumi全新内部开发者平台加速云基础设施交付
cover: https://cdn.thenewstack.io/media/2024/11/75da641c-pulumi.png
summary: Pulumi 发布全新 Pulumi IDP，加速云基础设施交付！基于 IaC 平台，几分钟内实现“概念到云”。亮点：内置 AI 代理，简化云环境启动，自动维护最佳实践和安全性；支持多语言，灵活的开发者界面；提供 SaaS 和自托管选项，集成 Pulumi Copilot、CrossGuard 等。
-->

Pulumi 发布全新 Pulumi IDP，加速云基础设施交付！基于 IaC 平台，几分钟内实现“概念到云”。亮点：内置 AI 代理，简化云环境启动，自动维护最佳实践和安全性；支持多语言，灵活的开发者界面；提供 SaaS 和自托管选项，集成 Pulumi Copilot、CrossGuard 等。

> 译自：[Pulumi's New Internal Developer Platform Accelerates Cloud Infrastructure Delivery](https://thenewstack.io/pulumis-new-internal-developer-platform-accelerates-cloud-infrastructure-delivery/)
> 
> 作者：Chris J Preimesberger

在今天的[用户大会](https://www.pulumi.com/pulumi-up/)上，基础设施即服务 (IaaS) 提供商 [Pulumi](https://www.pulumi.com/) 推出了 Pulumi IDP，这是一个内部开发者平台 (IDP)，旨在加速云软件交付，同时从一开始就嵌入安全和治理。

Pulumi IDP 构建于 Pulumi 流行的开源[基础设施即代码 (IaC) 平台](https://www.pulumi.com/product/infrastructure-as-code/)之上，该公司声称 Pulumi IDP 使工程团队能够在短短几分钟内从“概念到云”，从而消除数周或数月的传统开销。

该平台面向一个快速扩张的市场领域，其中包括 Qovery、Terraform、Humanitec、OpsLevel 和 Coherence。根据 [Gartner](https://gartner.com) 的数据，预计 [80% 的大型企业](https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering) 将在未来两年内部署内部开发者平台。Pulumi IDP 通过将基础设施优先原则与企业级控制相结合来应对这一趋势，为开发者和平台工程师提供了一个灵活、可扩展的云创新基础。

Pulumi 正在推出其 [IDP](https://thenewstack.io/platform-engineering-face-off-to-idp-or-not-to-idp/)，使开发者能够轻松启动云环境，同时自动维护最佳实践和安全性，这要归功于一种新的代理 AI 功能，如果需要，可以通过口头访问。这旨在解决平台团队成为瓶颈的常见问题。

首席执行官兼联合创始人 [Joe Duffy](https://thenewstack.io/qa-pulumis-joe-duffy-on-the-renaissance-of-infrastructure-as-code/) 告诉 *The New Stack*，IDP 旨在增强开发者（以及业务线员工）的能力，同时不牺牲时间、安全或治理。

“Pulumi IDP 是现代团队一直要求的云基础设施平台——多云、基础设施优先且深度灵活，”Duffy 说。“它使组织能够快速行动，而不会破坏任何东西或在安全或治理方面妥协。这是关于将云转化为竞争优势。”

Duffy 说，这家总部位于西雅图的八年历史的公司报告称，其工具每周[下载量](https://www.pulumi.com/docs/iac/get-started/)超过 100 万次。它已经是[基础设施自动化](https://thenewstack.io/introduction-to-infrastructure-as-code/)领域的重要参与者，拥有超过 3,500 家客户和 350,000 名全球用户。

## 开发者赋能的新篇章

Pulumi 汇总了从数百个客户实施中获得的关于其 [IDP](https://thenewstack.io/idp-vs-self-service-portal-a-platform-engineering-showdown/) 的见解，将定制的内部解决方案转变为可随时部署的平台，以满足开箱即用的企业需求，Duffy 说。

Pulumi IDP 没有强迫平台团队在构建高度定制的解决方案或采用不灵活的商业产品之间做出选择，而是提供了第三条途径——在基础设施层与团队会合，并向上扩展以实现开发者自助服务。

“我们已经做到了即使业务线员工也可以使用 IDP 来节省项目部署的时间，”Duffy 说。“我们的客户之一 Moderna 希望让数据科学家能够在进行疫苗研发时实际启动实验环境。显然，数据科学家通常不是云基础设施专家。现在他们可以参与其工具的开发。Moderna 确实需要让开发者能够在开发软件时启动云环境，而无需数据科学家提交工单并等待数月。”

另一个早期采用者 CLEAR 从基于 HashiCorp Terraform 的较低级别堆栈迁移到 Pulumi，使用自定义 YAML 模式简化了基础设施部署，从而简化了其开发团队的云访问。

## 大规模实现最佳实践

Pulumi IDP 有一个内部注册表，平台团队可以在其中发布可重用的基础设施模式，例如组件、模板和策略。这些构建块——以任何支持的语言编写，例如 Python、Go、Java、C#、TypeScript 或 YAML——充当快速配置项目（例如 Web 应用程序、微服务或数据管道）的标准蓝图。

该注册表支持内置文档、语义版本控制、使用情况跟踪和可发现性。组织可以将安全性、成本、合规性和运营标准直接编入这些构建块中，从而确保新基础设施从一开始就符合内部要求。
此外，这种组织最佳实践的编纂为基础设施配置带来了严谨性，同时让开发人员能够更快地构建，而不会牺牲监督。

## 具有内置防护功能的灵活开发者界面

Pulumi IDP 为开发者和数据科学家提供了多个入口点来创建和管理基础设施。该软件包中的选项包括：无代码用户界面；基于 YAML 的低代码 CI/CD 管道；首选语言的直接 IaC 编程；以及用于完全可扩展性的 REST API。

这种灵活性使具有不同技能组合和工作流程的团队能够采用 Pulumi IDP，而无需进行重大工具更改的摩擦。项目可以分组到“服务”中——包含配置、密钥、文档和可观测性工具的逻辑容器。这些服务可以代表从微服务或 Kubernetes 集群到 Jupyter notebook 或无服务器工作流的任何内容，具体取决于用例。

## 高级运营和安全控制

Pulumi IDP 不仅限于首次配置，它还可以简化持续运营。Day-two 功能包括漂移检测和修复、策略审计和执行、组件生命周期管理以及具有审批工作流的变更控制。Duffy 说，后者已被证明可以节省大量时间。

另一个功能是新的可视化导入器，它允许团队以最小的努力将以前未管理的 инфраструктура 置于 Pulumi 的治理之下。此功能简化了入门并加速了云合理化项目。

该平台还引入了高级身份和访问管理 (IAM) 系统，具有细粒度的基于角色的访问控制 (RBAC)、自定义权限以及通过 SAML/SSO 与企业身份系统集成。这些安全增强功能进一步扩展了 Pulumi 在企业级基础设施自动化方面的声誉。

## SaaS 和自托管灵活性

Pulumi IDP 提供两种部署模型：适用于大多数用户的托管 SaaS 平台和适用于具有严格合规性或数据驻留要求的组织的自托管版本。IDP 与 Pulumi 现有的企业生态系统无缝集成，包括 [Pulumi Copilot](https://www.pulumi.com/product/copilot)（一种人工智能驱动的基础设施管理工具）；用于工作流自动化的 [Pulumi Deployments](https://www.pulumi.com/docs/pulumi-cloud/deployments)；用于合规性的代码即策略 [Pulumi CrossGuard](https://www.pulumi.com/crossguard/)；以及用于跨堆栈标准化集成的 [Unified REST API](https://www.pulumi.com/docs/pulumi-cloud/reference/cloud-rest-api/)。

## 可用性和路线图

Pulumi IDP 今天进入公开预览阶段，现有 Pulumi 客户和社区用户可以免费使用。通用版本以及企业许可和支持计划计划于今年晚些时候发布。