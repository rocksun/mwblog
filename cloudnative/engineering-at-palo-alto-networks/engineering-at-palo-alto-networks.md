# Palo Alto Networks 的平台工程

翻译自 [Ramesh Nampelly](https://medium.com/@rnampelly?source=post_page-----e48afdcfb1f8--------------------------------) 的 Platform Engineering at Palo Alto Networks 的 [Part-1](https://medium.com/engineering-at-palo-alto-networks/platform-engineering-at-palo-alto-networks-part-1-e48afdcfb1f8) 和 [Part-2](https://medium.com/engineering-at-palo-alto-networks/platform-engineering-at-palo-alto-networks-part-2-315bd7b0fbfa) 。 

我一直在考虑我在 Palo Alto Networks 的第一篇博文应该是什么？什么时候发布？我觉得现在是反思我领导云基础设施和平台工程的旅程和经验的最佳时机。

我于 2021 年 4 月加入 Palo Alto Networks，领导网络安全组织快艇内云交付安全服务组织的生产工程团队，最近承担了整个 NetSec 组织领导基础设施平台的扩展角色。在这篇博客中，我想谈谈我们如何将生产工程服务转变为平台。这是我们博客系列的开始，其中我提供了我们内部开发人员平台 (Internal Developer Platform，IDP) 的高级概述，我们将在未来几个月为我们的每个 IDP 组件发布单独的博客文章。

让我们从 PAN IDP 启动背后的背景开始。主要是以下两个因素促使我们踏上了这段旅程：

1. **Palo Alto Networks 平台化方法** 如您所知，Palo Alto Networks 被称为网络安全领导者，其成功的主要原因之一是其针对网络安全解决方案的平台化方法。我们将相同的想法内化为构建生产工程服务平台，例如基础设施配置、成本管理、可观测性和事件管理，而不是将它们作为孤立的自动化解决方案提供给工程团队。
2. **子服务的开发者工具** —— 遗留生产工程/DevOps/SRE 实践的主要问题之一是带有相关文档的独立自动化脚本；必须阅读多页文档才能理解和运行这些工具或咨询主题专家。

一旦我们决定采用平台方法，下一个挑战就是确定我们是内部构建还是购买。经过详细分析，我们决定考虑 Palo Alto Networks 的特定用例来构建它。由于我们的理念不是重新发明轮子，而是尝试利用开源项目实现飞跃，团队找到了一个很棒的开源项目 [backstage.io](https://backstage.io/) 来启动我们的旅程。我们分叉了 backstage OSS 的代码并添加了所需的抽象并将其命名为“**Palo Alto Networks DevClues**”。

我们实施的第一个用例是“服务目录”，以帮助开发人员或 SRE 轻松快速地找出给定生产服务的详细信息。现在经过 1.5 年的旅程，我们在 IDP 中有相当多的服务（如下图所示）处于不同的采用阶段。

![](https://miro.medium.com/max/828/1*U9GRzVm5QyCdy_4WscrgZg.webp)

该平台由 4 个类别组成——资源管理、基础设施管理、生产管理和开发人员门户。开发人员门户 (DevClues) 是该平台提供的所有服务的入口点（一站式服务）。例如——如果任何一个工程团队想要将他们的服务加入可观测性，那么他们只需登录开发人员门户并使用加入插件（即由可观测性团队贡献的自定义插件）来完成他们的可观测性集成。

如今，开发人员门户 (DevClues) 提供 12 个插件和数十个服务模板，可提高整体工程效率。我们将继续根据我们的工程需求构建更多模板和插件。我还想指出，其中一些是由开发团队（也就是我们的客户）贡献的。因此，我们从第一天起就采用了内部开源模型（即内部采购）。

在第 2 部分中，我将在 [2022 年 gartner 发布的报告](https://www.gartner.com/en/documents/4010078)中简要介绍 Palo Alto Networks IDP 的四个类别及其能力。根据这份报告，IDP 能力分为以下三个开发生命周期阶段：

- 发现和创造
- 集成和部署
- 运营与改进

![](https://miro.medium.com/max/828/0*GWKsXqwjBUW7J294)
*图 1：Gartner 发布的报告背景下的 Palo Alto Networks IDP 概览*

现在让我们对每个阶段和 IDP 能力进行一些扩展。

## 发现和创造（Day 0）

发现和创建阶段涵盖开发生命周期的初始部分，包括引导、培训、启动、本地开发等。如图 1 所示，所有这些能力都是 Palo Alto Networks 的“**开发人员门户**”的一部分。

### 开发人员门户（Palo Alto Networks DevClues）

正如我在上一篇文章中所述，DevClues 基于开源项目 [backstage.io](https://backstage.io/)，它是基础设施平台提供的所有内部服务的一站式商店。现在，我们将在 Gartner 发布的报告的背景下仔细研究 DevClues（即图 1 下方）的每项能力。

内部开发人员门户应使开发人员能够轻松地在软件交付生命周期 (SDLC) 的所有阶段执行 Day 0, Day 1 和 Day 2 的活动。

![](https://miro.medium.com/max/828/0*w-ZkiS2f4jMo3ylr)
*图 2：Palo Alto Networks DevClues 主页*

Palo Alto Networks DevClues 为开发人员提供随时可用的服务模板，以创建具有嵌入式最佳实践的新软件应用程序、服务和基础架构组件。

### 服务目录

此功能使开发人员能够快速轻松地搜索和查找生产服务（例如 On Boarded into DevClues）；包括：

- 可用服务及其元数据（即所有者和待命工程师）
- 他们的 API 说明
- 其他详细信息，例如文档、CICD 统计信息、代码覆盖率和如下图所示的 DORA 指标（即图片 2：服务目录服务概览）。

![](https://miro.medium.com/max/828/0*UPhajrLwEkQbQqqk)
*图 3：服务目录中服务概览*

### 服务生成模板

此功能允许开发人员基于预定义模板创建新服务、基础架构组件或应用程序。 DevClues 目前提供了一套用于“go”、“python”和“react”应用程序开发的服务模板，以及用于“GKE 集群启动”和“gitOps 引导”（使用 gitlab 和 argoCD）的基础设施组件配置模板。

### 文档和培训材料

这有助于开发人员了解如何以自助服务的方式最大限度地利用平台，并促进围绕平台的社区，来自不同服务团队的个人成为平台上的 SME，可以帮助他们的团队实现目标而无需等待为平台团队寻求信息或帮助。这包括：

- 平台使用指南
- 培训文档和视频
- 社区午餐会和办公时间

### 自动化支持和搜索

为开发人员提供一种自助服务方式，以查找有关平台及其功能的信息、获得对问题的答复以及问题的自动帮助。这包括：

- 全局搜索所有可用的文档、指南和示例
- 联系平台团队的 Slack 或电子邮件链接
- 协助引导的聊天机器人

### 最佳实践指南和工具

为开发人员提供有关架构的最佳实践：

- 模板和启动解决方案
- 生产准入指导
- SRE 最佳实践和标准

### 自定义插件

DevClues 使 Palo Alto Networks 开发人员能够为内部工具和流程构建门户。在 Palo Alto Networks ，我们有插件：

- 云成本
- 可观测性引导
- 事件分析
- 基础设施管理
- 证书管理
- 新的云区域扩建
- 自动修复创作
- 生产审计日志
- 适合“内部采购”的内部项目市场

## 集成和部署（Day 1）

集成和部署阶段涵盖应用程序部署到非生产/生产、集成分布式系统、配置资源等。提供单一仪表盘来管理跨云和本地环境的分布式基础设施。以下是当前的能力，它们分布在基础设施管理和生产管理类别之间（即如图 1 所示）

### 基础设施配置和编排

在 Palo Alto Networks，我们构建了一个 DevClues 插件 Uno（请参考下面的图 4），它可以帮助开发人员为利用 GitOps 的服务/应用程序提供和配置云资源和其他基础设施组件。这包括：

- 私有云或公共云中的按需资源供应
- 使用最佳实践将所有必需的资源定义为代码

![](https://miro.medium.com/max/828/0*uT6Pgp58UoS8t2Ce)
*图4：Uno——用于多云基础设置管理的 DevClues 插件*

### 策略管理

对资源和运行的应用程序实施商业、运维和最佳实践策略。我们已实施基于 OPA(Open policy agent) 的“控制平面”：

- 所有内部用户和底层 API 的授权 (RBAC)
- 将资源配置限制为允许的值（即 CICD）
- 强制执行特定注释/标签

### 环境管理

我们为管理基础设施资源而构建的 DevClues 插件已得到扩展，可以轻松创建、配置和管理服务/应用程序环境，例如：

- 轻松添加新环境/区域，或删除旧环境/区域
- 创建和删除用于开发和测试的临时环境

### Secrets 管理

在Palo Alto Networks，此功能可以提供一种服务，可以管理生产中的证明书、 Secrets 和配置的同步，以方便他们可以安全的：

- Secrets 管理系统与部署/交付系统的自动集成
- 在中央仓库（即 vault 或 GSM 或 ASM）中储/轮换他们的配置、Secrets 和凭证
- 当相应的 Secrets/证书/配置发生变化时，无缝地重新配置/重新加载他们的应用程序，这些应用程序在 K8S、Docker 和本地 linux 进程上运行

## 运营和改进（Day 2）

此阶段涵盖持续运营，通过 DevClues 插件提供对工具箱的访问，以实现自动化、监控、可观测性和事件管理等。

在 Palo Alto Networks，运营和改进阶段能力分布在 3 个类别中 — 生产管理、基础设施管理和资源管理（即如图 1 所示）。

### 监控和可观测性

监控和可观测性是 Palo Alto Networks 的关键生产工程服务之一。我们使用 grafana、grafana mimir、grafana loki、grafana tempo 和 [vector.dev](https://vector.dev/) 等成熟的开源技术构建了一个名为“Garuda”的内部可观测性平台。我们将发布一篇单独的博文，介绍 Garuda 并很快深入探讨其功能。

截至今天，Garuda 提供以下能力：

- 记录和事件
- 追踪
- 指标
- 警报
- 仪表板

我们为 Garuda 构建了一个 DevClues 插件（即下图 5），以帮助工程团队轻松地将他们的基础设施和服务/应用程序载入“可观测性平台”。

![](https://miro.medium.com/max/828/0*-Xla7y29S9iPFwuh)
*图 5：DevClues 中的 Garuda 引导插件*

监控和可观测性的主要挑战之一是不同资源类型（云、本地、k8s、虚拟机、无服务器和裸金属）的复杂引导流程。通过这个插件，我们使引导流程尽可能无缝和顺畅。

![](https://miro.medium.com/max/828/0*d3OoFRWxGjU0EBEC)
*图 6：Garuda Agent 引导*

### 事件管理

有效的事件管理是我们 SRE 最佳实践的一个关键方面，可以在发生影响业务的事件/中断时有效地提醒和通知工程师，并提供管理这些事件的工具。这包括：

- 事件管理仪表盘
- 事件分析
- 用于提醒和创建 slack 频道的工具

我们的 DevClues 事件分析插件提供以下见解

- 按天分类的事件
- 按小时统计的事故
- 按组件分类的事件
- 团队事件
- 事件修复与出现
- 按组件/服务重复事件

### 自动修复

根据最近的一项行业研究，30-50% 的生产事件是重复的，并且是 SRE 工作的主要内容。我们想通过自动化来解决这个问题，因此构建了一个名为“Nutrix”的系统，即我们基于开源项目 [stackstorm](https://stackstorm.com/) 的内部自动修复平台：

![](https://miro.medium.com/max/828/0*MQv8ZCyxxwFYNuZK)
*图 7：DevClues 中的 Nutrix 插件*

同样，增加这种自动化采用的主要瓶颈之一是没有一个强大的创作框架，这促使我们在 DevClues Nutrix 插件中构建创作框架（如下所示）。

![](https://miro.medium.com/max/828/0*_s1xcvr_uk2_NacK)
*图 8：DevClues 中的 Nutrix 自动修复创作*

### 洞察仪表盘

使用可观测性和监控数据来诊断问题和调试正在运行的系统以减少 MTTR（平均解决时间）的仪表盘。这包括：

- 托管360
- 证书360
- Kubernetes 360 仪表板
- 成本洞察

![](https://miro.medium.com/max/828/0*5eH4pa2QFsaaDgxS)
*图 9：Garuda 罐装 Host 360 仪表板*

![](https://miro.medium.com/max/828/0*niqePRRRpuWYmp3w)
*图 10：Garuda 罐装证书 360 仪表板*

![](https://miro.medium.com/max/828/0*wak8px5SueKlyrQ9)
*图 11：Garuda 罐装 Kubernetes 360 仪表板*

![](https://miro.medium.com/max/828/0*0xE-M62nKNu92Gxt)
*图 12：Garuda 罐装 Kubernetes 成本洞察仪表盘*

### IAM

管理用户和工具对云资源和系统的身份和访问管理。

例子包括：

- 基于角色管理K8s集群访问级别，例如服务操作员和集群操作员的不同访问权限
- 定义 RBAC 权限以执行部署、更新服务/应用程序和资源的配置
- 堡垒即生产基础设施访问服务
- 及时访问管理

### 安全与合规管理

Palo Alto Networks 信息安全团队负责安全策略的定义和执行以及自动验证和检查，但补救措施是工程团队的责任。这包括：

- 安全审查和批准（信息安全）
- 扫描并检查漏洞（信息安全）
- 漏洞修复（工程）
- 实施业务政策合规措施的框架（平台工程）
- 遵守治理规则和法规的框架（平台工程）

### 成本管理

在多云和混合云世界中，基础设施成本成为热门话题。毫无疑问，需要持续监控、报告和优化成本。

在 Palo Alto Networks，我们开始从两个维度解决这个问题，即自上而下和自下而上：

- 自上而下——这由 FinOps 和 CloudOps 驱动到执行团队，以推动组织和业务部门级别的成本优化。
- 自下而上——这是由基础设施平台和工程团队驱动的，我们在其中提供对单个云资源或用户级别的成本的精细洞察，包括异常检测和自动化以优化成本。

![](https://miro.medium.com/max/828/1*MV5g3snPgB6aRQFNb1Tdww.webp)
*图 13：DevClues 在 SKU 级别的成本洞察*

### 配置管理

在云世界中，基础设施管理有两个重要方面，即基础设施供应和配置。在 Palo Alto Networks，我们使用 terraform 标准化基础设施配置，使用 ansible 进行配置管理。

开发人员应该以可扩展且可靠的方式管理应用程序配置，类似于我们管理和版本化源代码或基础设施即代码 (IaC) 的方式。

为了更好地管理 ansible 代码，我们采用了 [awx](https://github.com/ansible/awx)，这是 ansible tower 的开源版本，可帮助开发人员/SRE 标准化配置的部署、启动、委托和审计方式。

### 资源管理

在 Palo Alto Networks，资源和基础设施管理齐头并进。 DevClue 的“Uno”插件旨在提供简单无缝的基础设施配置和端到端管理。这包括：

- 以代码形式管理 Kubernetes 集群队列和组件，采用最佳实践和持续部署
- 通过最佳实践将跨云提供商的虚拟机作为代码进行管理
- 管理云供应商资源；例如——google bigquery、cloudSQL 和 cloud run functions 等。

## 总结

根据 Gartner 的报告，到 2025 年，75% 的拥有平台团队的组织将提供自助式开发人员门户，以改善开发人员体验并加速产品创新。

IDP 的采用与组织的 DevOps、SRE 和平台工程实践的成熟度成正比。因此，成熟度指数越高，他们使用开发人员门户的可能性就越高。

Palo Alto Networks 的平台工程团队专注于并致力于通过管理其采用、路线图、从我们的工程团队收集反馈并推销其功能来不断创新 IDP 功能。

## 参考资料和其他资源
内部开发人员门户的创新洞察 — [https://www.gartner.com/en/documents/4010078](https://www.gartner.com/en/documents/4010078)