<!--
title: 选择合适的红帽人工智能解决方案：RHEL AI vs. OpenShift AI
cover: https://cdn.thenewstack.io/media/2025/03/319862bd-red-hat-rhel-ai-openshift-ai.jpg
summary: 红帽AI方案选哪个？RHEL AI轻量易部署，适合小规模GenAI项目，集成Granite LLMs、InstructLab。OpenShift AI为企业级而生，支持Kubernetes跨混合云，擅长大规模MLOps自动化，集成KubeFlow等。初期选RHEL AI，扩展选OpenShift AI！
-->

红帽AI方案选哪个？**RHEL AI**轻量易部署，适合小规模**GenAI**项目，集成**Granite LLMs**、**InstructLab**。**OpenShift AI**为企业级而生，支持**Kubernetes**跨混合云，擅长大规模**MLOps**自动化，集成**KubeFlow**等。初期选**RHEL AI**，扩展选**OpenShift AI**！

> 译自：[Choosing the Right Red Hat AI Solution: RHEL AI vs. OpenShift AI](https://thenewstack.io/choosing-the-right-red-hat-ai-solution-rhel-ai-vs-openshift-ai/)
> 
> 作者：Oyedele Tioluwani

有些项目需要最小的开销和快速的结果。另一些项目需要大规模的编排和深度集成。对于您的项目来说，理想的 [AI 设置](https://thenewstack.io/as-ai-reshapes-tech-microsoft-others-refocus-dev-structure/#redhat) 将满足您眼前的需求，而不会妨碍您未来的雄心。

[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 通过两条路径来应对这些挑战：[Red Hat Enterprise Linux (RHEL) AI](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux/ai) 用于更简单的部署，而 [OpenShift AI](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_cloud_service/1/html-single/release_notes/index#overview-of-openshift-ai_relnotes) 用于扩展复杂的环境。RHEL AI 与现有的工作流程集成，并针对较小的工作负载，而 OpenShift AI 为更大的项目实现了高级管道和集群级别的协调。这两种解决方案都与 AI 之旅的不同阶段相一致。
本指南将介绍每种解决方案的优势，并帮助您决定哪种方案最适合您的项目以及何时部署它。

## 比较 RHEL AI 和 OpenShift AI

对于评估红帽 AI 解决方案的组织，此列表重点介绍了 RHEL AI 和 OpenShift AI 在部署、可扩展性和自动化方面的核心差异。

**部署模型**

- RHEL AI：单个生产服务器
- OpenShift AI：分布式 [Kubernetes](https://roadmap.sh/kubernetes) 跨混合云

**复杂性和设置**

- RHEL AI：简单直接
- OpenShift AI：高级功能，更强大的特性

**可扩展性**

- RHEL AI：适用于较小的 AI 项目
- OpenShift AI：专为中到大规模 AI 设计

**机器学习运营（[MLOps](https://thenewstack.io/what-is-mlops/)）自动化**

- RHEL AI：集成但更简单
- OpenShift AI：全面的管道自动化

**开源工具**

- RHEL AI：Granite LLMs, InstructLab, vLLM, Docling
- OpenShift AI：Granite LLMs, InstructLab, Open Data Hub, vLLM, KubeFlow, partner integrations

**理想的用例**

- RHEL AI：本地部署，较小规模
- OpenShift AI：混合云，大规模企业 AI

**云和合作伙伴集成**

- RHEL AI：来自合作伙伴的有限支持
- OpenShift AI：广泛的云和合作伙伴生态系统集成

考虑到这种比较，让我们更仔细地看看每种解决方案，从 RHEL AI 开始。

## RHEL AI：单个服务器的基础

RHEL AI 是一个易于部署的、以服务器为中心的 AI 平台，它可以在独立服务器（本地或云端）上高效运行，适用于寻求简单生成式 AI (GenAI) 解决方案的组织。它消除了大规模编排开销的负担，这对于希望专注于开发 AI 而无需管理分布式基础设施的团队来说是理想的。它也最适合专注于 AI 开发同时保持数据隐私和安全的团队。

它的一些主要优点包括：

- IBM Granite LLM，允许使用预训练的 AI 模型进行快速原型设计。
- [InstructLab](https://thenewstack.io/why-red-hat-thinks-ais-future-is-small-language-models/)，它简化了模型对齐和微调，且设置最少。
- 能够在本地运行预训练的 AI 模型，而无需动态扩展。
- 更简单的架构，减少了维护并降低了 IT 资源的消耗。

较小的团队、研究机构和具有严格数据治理政策的企业可以从 RHEL AI 中受益。对于许多组织，尤其是那些处于 AI 采用早期阶段的组织来说，这个轻量级但功能强大的平台足以入门。

## 为什么从 RHEL AI 开始有意义

最好的方法通常是从小处着手，RHEL AI 凭借其简单的设置、较低的费用和 AI 的增量采用，实现了这一点。它非常适合在不致力于复杂平台的情况下探索 AI 的团队。虽然 Kubernetes 编排功能强大，但早期可能会增加不必要的复杂性。这使得 RHEL AI 在扩大规模之前成为一个实际的选择。

除了易于使用之外，RHEL AI 还提供了灵活性。它适应开源 AI 框架，允许您测试 AI 模型，而不会被供应商挟持。这使其非常适合必须在扩展之前证明 AI 用例的研究团队和初创公司。

但是，虽然 RHEL AI 对于较小的项目有效，但它缺乏大规模 AI 运营的功能。它的一些限制是：

- 没有分布式、多集群 AI 训练——它不适合处理复杂、高容量工作负载的组织。
- 有限的自动化——它缺乏 OpenShift AI 中提供的高级 MLOps 工具。
具有长期 AI 雄心的组织可以从 RHEL AI 开始，但应计划随着工作负载的扩展过渡到更具可扩展性的解决方案。

## OpenShift AI：专为可扩展的企业级 AI 而构建

OpenShift AI 提供了一个用于构建、训练、部署和监控预测和生成式 AI 模型的平台。它为[多个混合云环境](https://www.redhat.com/zh/resources/red-hat-openshift-ai-hybrid-cloud-datasheet)上的大规模 AI 工作负载提供编排、自动化和可扩展性。它还包括 Kubernetes 原生的可扩展性，使其能够有效地调度和执行对要求严苛的 AI 应用程序的资源分配。

OpenShift AI 具有许多优势，包括：

- 在分布式基础设施上动态扩展 AI 工作负载。
- 通过数据科学管道自动执行 AI 模型训练、部署和监控，从而更轻松地运行操作。
- 支持从本地到云的 AI 模型统一管理平台，最大限度地减少手动开销。
- 符合安全和合规实践，包括基于角色的访问控制 (RBAC)、用于偏差检测的可信 AI 以及保护组织免受损害的保护措施。
- 添加自定义集群镜像以增强笔记本电脑上的协作，并添加模型注册表以跟踪和共享数据科学项目。

拥有多个模型或中型到大型 AI 工作负载的组织需要一个提供可扩展性、安全性和合规性的平台。OpenShift AI 非常适合希望构建 ML 管道的企业以及具有严格监管要求的企业，例如：

- 在混合云平台上运行多个 AI 应用程序的大型公共部门组织。
- AI 安全、合规性和风险管理至关重要的金融机构。
- 依赖 AI 进行药物开发和医疗诊断的健康和生物技术公司。

对于更关注高可用性和弹性 AI 运营的公司，OpenShift AI 是更适合可扩展的生产级 AI 部署的平台。

## 并非每个 AI 项目都需要这么多开销

虽然 OpenShift AI 提供了相当多的优势，包括可扩展性和编排，但它需要陡峭的学习曲线和并非每个组织都准备承担的基础设施要求。以下是与 OpenShift AI 相关的一些权衡：

- 管理基于 Kubernetes 的 AI 工作负载需要熟练的专业知识。
- 更高的运营复杂性意味着高级功能需要更多的设置、维护和监控。
- 强大的自动化和多云功能通常需要对基础设施和资源进行更大的投资。

对于较小的团队或刚开始使用 AI 的团队来说，开销可能超过收益。但是，对于专注于可扩展性、自动化和弹性的公司而言，OpenShift AI 仍然是一个具有战略意义的长期选择。

例如，一家跨多云基础设施管理 AI 驱动的推荐的零售公司将受益于 OpenShift AI 的模型监控和性能优化，从而为大规模的 AI 工作负载实现经济高效的解决方案。同时，一家具有严格数据隐私要求的研究所可能会选择 RHEL AI，因为它具有轻量级的本地部署，从而避免了云的复杂性。

## 哪种 AI 解决方案适合您？

在 RHEL AI 和 OpenShift AI 之间进行选择取决于您的 AI 开发策略和可扩展性需求。

- RHEL AI 非常适合以服务器为中心的 AI 工作负载、单独的部署和更简单的 AI 用例。
- OpenShift AI 在多云环境中蓬勃发展，提供企业级 AI 编排、MLOps 自动化和大规模 AI 模型训练和推理。

对于 Red Hat 商店，一个平衡的策略包括从 RHEL AI 开始进行实验性或小规模 AI 模型。当 AI 工作负载需要混合云基础设施、可扩展的 AI 和企业支持时，组织可以过渡到 OpenShift AI。

选择正确的 AI 平台可以随着您需求的演变而提高采用率和可扩展性。成功的关键是提前规划 AI 扩展。