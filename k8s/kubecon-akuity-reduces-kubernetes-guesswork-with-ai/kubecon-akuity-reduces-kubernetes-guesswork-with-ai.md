
<!--
title: KubeCon：Akuity AI赋能，终结Kubernetes盲猜
cover: https://cdn.thenewstack.io/media/2025/11/36f9288f-akuity.png
summary: Akuity 为其 Kubernetes 部署平台新增生成式AI辅助功能，旨在帮助系统运维人员更好地管理事故和错误配置，包括事件检测、报告和自动化修复，提高效率。
-->

Akuity 为其 Kubernetes 部署平台新增生成式AI辅助功能，旨在帮助系统运维人员更好地管理事故和错误配置，包括事件检测、报告和自动化修复，提高效率。

> 译自：[KubeCon: Akuity Reduces Kubernetes Guesswork With AI](https://thenewstack.io/kubecon-akuity-reduces-kubernetes-guesswork-with-ai/)
> 
> 作者：Joab Jackson

亚特兰大 — 云原生 GitOps 服务提供商 [Akuity](https://akuity.io) 已在其 Kubernetes 部署平台中加入了生成式 AI 辅助功能，旨在帮助系统运维人员更好地管理事故和错误配置。本周在亚特兰大参加 [KubeCon+CloudNativeCon 2025](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/?utm_source=the+new+stack&utm_medium=referral&utm_campaign=event) 的参会者可以前往 #830 展位，亲身体验 Akuity 平台及其 AI 增强功能。

与 Argo CD 不同，Akuity 商业版采用分布式、基于代理的架构。凭证本地保存，并用于本地访问集群 API 和仓库。

![architecture diagram](https://cdn.thenewstack.io/media/2025/11/8013fd8a-acuity-01.png)

## Argo CD 的崛起

过去几年，随着企业对 Kubernetes 的使用不断增长，企业发现他们需要简化 Kubernetes 以及运行在 Kubernetes 集群上的应用程序的部署。

自 2021 年推出以来，Akuity 的客户群持续稳健增长，其中包括 CoreWeave 等知名 GPU 云提供商以及 Thinking Machines Lab。其用户遍布各大垂直行业，包括《财富》100 强企业。

Akuity 联合创始人兼首席执行官

[Hong Wang](https://www.linkedin.com/in/hwang8/)

在接受 TNS 采访时表示，典型用户可能会在 Akuity 上运行 50 到 100 个应用程序，但该公司最近发现了一个在平台上运行 20,000 个应用程序的案例。

Wang 也是 Argo CD 的联合创始人之一。

Wang 说：“我们创建 Argo 是为了解决我们在日常使用 Kubernetes 时遇到的一个非常实际的问题。”“我们有许多集群需要管理。我们希望有一个部署解决方案来部署多个集群。”

Wang 当时在一家初创公司工作，该公司后来被出售给 Intuit，Argo 也随之而来。

在 Intuit，Argo 核心团队为不熟悉 Kubernetes 的开发人员开发了一个开发者友好的界面。

[theCube](https://www.thecube.net/) 研究应用程序开发和现代化实践的研究表明，70% 使用 Kubernetes 的组织发现可扩展性和可靠性是他们的首要挑战，60% 的组织则面临工具链碎片化的问题。

theCube 负责人

[Paul Nashawaty](https://www.linkedin.com/in/paulnashawaty/)

在一份声明中表示：“Akuity 的‘GitOps 驱动方法’使组织能够超越 DIY 脚本和脆弱的操作，转向更可靠、安全和自动化的 Kubernetes 运营模式。”

它既可以作为托管服务提供，也可以作为在客户数据中心运行的软件提供。

## AI 助力部署

新的 AI 功能将有助于检测应用程序的降级状态、分类事件并自动化修复。

Akuity Intelligence 功能提供多项特性，包括

*   **事件检测**，当工作负载偏离健康状态时发送警报并进行修复
*   **集中式事件报告**，包含日志、事件、指标和部署历史。
*   **运行手册自主性**，允许事件自动解决。
*   **实时 Slack 更新**，提供事件状态和所采取的行动。
*   **访问控制**，包括审批关卡、范围权限和完整的审计跟踪。

美国职业棒球大联盟首席 DevOps 工程师

[Michael Goodness](https://github.com/mgoodness)

在一份声明中表示：“借助 Akuity 新的 AI 功能，我们能够立即发现数十个问题，所有问题都附带即时分析和摘要，减少了工程师的猜测工作。它还允许工程师快速解决持续的基础设施问题，而无需成为如何部署更改的专家。”

Akuity Intelligence 已普遍可用，并可下载免费试用版。