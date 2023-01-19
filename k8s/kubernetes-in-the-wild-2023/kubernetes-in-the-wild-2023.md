# Kubernetes 野外报告 2023

本文翻译自[ dynatrace 的 Blog ](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)。

Kubernetes 的快速采用受到不断增长的先进技术生态系统的推动和挑战。在此 Kubernetes 调查报告中，了解顶级组织如何在生产中使用 Kubernetes 和相关技术，包括可观测性、安全性、基础设施模型和开源软件。

## Kubernetes 采用调查执行摘要

现代云原生计算不可能与容器和 Kubernetes 的采用分开。虽然 Kubernetes 仍然是一项相对年轻的技术，但全球绝大多数企业都使用它在生产环境中运行关键业务应用程序。 Kubernetes 技术的快速采用受到不断增长的 Kubernetes 技术生态系统的推动和挑战，这些技术增加了高级平台功能，例如安全性、微服务通信、可观测性、扩展性、资源利用等。

这项 Kubernetes 调查显示了组织如何在生产中实际使用 Kubernetes。该研究分析了来自全球数千家使用 Dynatrace 软件智能平台来确保其 Kubernetes 集群安全、健康和高性能的组织的实际 Kubernetes 生产数据。

调查结果提供了对 Kubernetes 从业者的基础架构偏好以及他们如何使用高级 Kubernetes 平台技术的见解。该报告还揭示了从业者用于应用程序工作负载的主要编程语言。随着 Kubernetes 采用率的提高以及技术的不断进步，Kubernetes 已成为云的“操作系统”。

1. Kubernetes 于 2022 年迁移至云端
2. Kubernetes 基础基础模型在云和本地之间有所不同
3. Kubernetes 正在成为云的“操作系统”
4. Kubernetes 最强劲的增长领域是安全、数据库和 CI/CD 技术
5. 开源软件驱动充满活力的 Kubernetes 生态系统
6. Java、Go 和 Node.js 是 Kubernetes 应用程序工作负载的前 3 大编程语言

## 洞察1：Kubernetes 于 2022 年迁移至云端

2022 年，Kubernetes 成为将工作负载迁移到公有云的关键平台。云中托管的 Kubernetes 集群数量的年增长率为 +127%，增长速度是本地托管集群的五倍左右。同样，云托管集群的份额从 2021 年的 31% 增加到 2022 年的 45%。云托管的 Kubernetes 集群将在 2023 年超过本地部署。

云中的大多数 Kubernetes 集群 (73%) 都建立在 AWS Elastic Kubernetes Service (EKS)、Azure Kubernetes Service (AKS) 或 Google Kubernetes Engine (GKE) 等超大规模应用程序的托管分布之上。因此，其余 27% 的集群由客户在云虚拟机上自行管理。

Kubernetes 托管决策由一组参数指导，包括成本、配置和扩展的便利性、数据安全性和合规性。随着超大规模企业在所有这些领域进行投资并将其业务扩展到更多地理区域，它们对更广泛的组织更具吸引力。

![显示云托管集群与本地集群的饼图](https://marvel-b1-cdn.bc0a.com/f00000000236551/dt-cdn.net/wp-content/uploads/2023/01/BAE3410_ILL_StateK8s_Blog_Hosting_1920x1080_FINAL2-1000x563.png)
2022 年，更多集群从本地迁移到云端，因此在 2023 年将赶超本地部署。

## 洞察2：Kubernetes 基础架构模型在云和本地之间有所不同

在公共云中运行的典型集群由 5 个相对较小的节点组成，每个节点只有 16 到 32 GB 的内存。相比之下，本地集群的节点更多更大：平均有 9 个节点，内存为 32 到 64 GB。

不同的基础设施设置反映了经济和技术方面的考虑。 Hyperscalers 为中小型主机提供具有竞争力的价格点。通过毫不费力的配置，大量的小型主机提供了一个经济高效且可扩展的平台。本地数据中心投资于更高容量的服务器，因为它们从长远来看提供了更大的灵活性，而硬件的采购价格只是众多成本因素之一。

![Kubernetes 调查结果条形图显示托管在云端和本地的节点的内存大小。](https://marvel-b1-cdn.bc0a.com/f00000000236551/dt-cdn.net/wp-content/uploads/2023/01/BAE3410_ILL_StateK8s_Blog_Node-Memory_1920x1080_FINAL3.png)

![显示每个集群的节点和 Pod 的 Kubernetes 调查条形图](https://marvel-b1-cdn.bc0a.com/f00000000236551/dt-cdn.net/wp-content/uploads/2023/01/BAE3410_ILL_StateK8s_Blog_Node-Cluster_1920x1080_FINAL3-1000x563.png)

典型的云托管集群在 5 个相对较小的节点上运行。相反，本地托管的集群使用 9 个节点，内存几乎翻倍。

## 洞察3：Kubernetes 正在成为云的“操作系统”

作为运行云原生微服务应用程序的理想编排平台，Kubernetes 具有内置部署、扩展和弹性功能的优势。 2021 年，在典型的 Kubernetes 集群中，应用程序工作负载占了大部分的 Pod（59%）。相比之下，所有非应用程序工作负载（例如系统和辅助工作负载）所起的作用相对较小。

但在 2022 年，情况发生了逆转。随着 Kubernetes 采用率的增长，辅助工作负载现在超过了应用程序工作负载（63% 对 37%）。这一转变反映出组织正在实施更先进的 Kubernetes 平台技术，例如安全控制、服务网格、消息传递系统和可观测性工具。与此同时，组织正在将 Kubernetes 用于更广泛的情况，包括构建流水线和计划的实用程序工作负载等。 Kubernetes 成为运行几乎任何东西的平台。因此，Kubernetes 正在成为云的“操作系统”。

![显示应用程序工作负载与辅助工作负载的饼图](https://marvel-b1-cdn.bc0a.com/f00000000236551/dt-cdn.net/wp-content/uploads/2023/01/BAE3410_ILL_StateK8s_Pod-Type_1920x1080_FINAL-1000x563.png)
2021 年，应用程序工作负载占主导地位，而 2022 年，辅助工作负载占主导地位，显示出更广泛的用例。

> 在 Dynatrace，我们将 Kubernetes 用于所有新的软件项目，从构建流水线到 SaaS 产品。我们的客户也看到了同样的趋势。 Kubernetes 实际上已经成为云的操作系统。
>
>Anita Schreiner，Dynatrace 交付副总裁

## 洞察4：Kubernetes 增长最快的领域是安全、数据库和 CI/CD 技术

2022 年，组织将 Kubernetes 安全性确定为重中之重。从低基线开始，使用 Kubernetes 安全工具的组织的百分比从 2021 年的 22% 增加到 2022 年的 34%。这相当于 +55% 的年增长率。随着 Kubernetes 安全意识的进一步提高和新型安全解决方案的出现，这种趋势可能会持续下去。

在接受 Kubernetes 调查的组织中，71% 在 Kubernetes 中运行数据库和缓存，同比增长 48%。连同消息系统（+36% 的增长），组织越来越多地使用数据库和缓存来保存应用程序工作负载状态。

持续集成和交付 (CI/CD) 技术同比增长 43%。这一趋势表明，组织正在将更多的 Kubernetes 集群用于运​​行软件构建、测试和部署管道。

![显示 Kubernetes 采用率最高的技术的条形图](https://marvel-b1-cdn.bc0a.com/f00000000236551/dt-cdn.net/wp-content/uploads/2023/01/BAE3410_ILL_StateK8s_Blog_Workload-Type_1920x1080_FINAL3-1000x563.png)

> Kubernetes 的巨大增长在运行时带来了新的安全挑战，并增加了在开发中强化 CI/CD 管道的复杂性。从好的方面来看，新的应用程序安全方法可以应对这些挑战，减少遭受攻击的风险并降低风险。
>
> Andreas Berger，Dynatrace 高级首席应用程序安全

## 洞察5：开源软件驱动充满活力的 Kubernetes 生态系统

专注于非应用程序工作负载，组织使用越来越多的技术。这些结果反映出需要通过更好的可观测性、安全性和服务到服务通信来增强 Kubernetes。同样，其他技术支持特定用例，如 CI/CD 工具或数据库。在 Kubernetes 调查的所有类别中，开源项目位列最常用的解决方案之列。

![Kubernetes 调查条形图显示了 Kubernetes 环境中使用的技术](https://marvel-b1-cdn.bc0a.com/f00000000236551/dt-cdn.net/wp-content/uploads/2023/01/BAE3410_ILL_StateK8s_Blog_Workload-Category_1920x1080_FINAL3-1000x563.png)

* **开源可观察性**：Prometheus 是开源可观察性方面的明显领导者，65% 的组织都在使用它。一* 般来说，指标收集器和提供者是最常见的，其次是日志和跟踪项目。注意：该调查排除了所有* 商业可观察性产品，包括 Dynatrace。
* **数据库**：在数据库中，Redis 使用最多，达到 60%。 Redis 是一种内存中的键值存储和缓* 存，可简化 Kubernetes 环境中数据的处理、存储和交互。因此，对于经典数据库用例，组织* 使用各种关系数据库和文档存储。
* **消息传递**：RabbitMQ 和 Kafka 是使用的两个主要消息传递和事件流系统。具体来说，它们* 在微服务架构和高吞吐量分布式系统中提供异步通信。
* **持续集成和交付**：ArgoCD、Flux、Gitlab 和 Jenkins 是使用最广泛的 CI/CD 工具。组织* 越来越多地使用 Kubernetes 的灵活性和弹性来运行 CI 和 CD 作业及其控制平面。
* **大数据**：为了存储、搜索和分析大型数据集，32% 的组织使用 Elasticsearch。
* **安全性**：为了安全，组织主要使用策略检查器和执行器，例如网守。对运行时安全可观察性的* 需求正在增长，以自动化漏洞影响分析。
* **服务网格**：Istio 是最常用的服务网格。组织越来越多地在大型 Kubernetes 集群中使用服* 务网格来自动化安全的服务到服务通信并公开遥测数据以实现更好的可观察性。

> Dynatrace 相信强大的开源生态系统，并支持采用云原生技术和实践。这就是为什么我们积极贡献和引导项目，并以各种角色参与开源社区。 Dynatrace 对开源技术的投资不断增长。
>
> Alois Reitbauer，Dynatrace 首席技术策略师

## 洞察6：Java、Go 和 Node.js 是顶级的 Kubernetes 编程语言

Dynatrace OneAgent 自动检测在 Kubernetes 上运行的每个应用程序工作负载的特定编程语言。这提供了对组织使用的 Kubernetes 编程语言的独特见解。

基于 Java 虚拟机 (JVM) 的语言占主导地位。因此，65% 的应用程序工作负载在 JVM 中运行，包括相关的应用程序服务器，如 Tomcat 或 Spring。大多数组织（72%）在某种程度上使用 Java。

Go 在组织中以 58% 的采用率排名第二，其中 14% 的应用程序工作负载是用 Go 编写的。不包括 Kubernetes 系统工作负载、sidecar 或非应用程序工作负载的任何标准组件。此外，Node.js 在工作负载数量和组织采用方面排名第三。

![显示 Kubernetes 采用率最高的编程语言的条形图](https://marvel-b1-cdn.bc0a.com/f00000000236551/dt-cdn.net/wp-content/uploads/2023/01/BAE3410_ILL_StateK8s_Language_1920x1080_FINAL-1000x563.png)

> 有了 Kubernetes，多语言编程终于成为现实。因此，无论使用何种编程语言和框架，Kubernetes 都可以增强现有团队的能力并使新团队的入职变得容易。
>
> Florian Ortner，Dynatrace 首席产品官

## Kubernetes 调查方法

本报告反映了 Kubernetes 采用统计数据，该统计数据基于对来自全球所有地区数千家 Dynatrace 客户的 41 亿个 Kubernetes pod 的分析。数据涵盖 2021 年 1 月至 2022 年 9 月期间。这些客户来自所有主要行业的全球最大 15,000 家组织，包括金融服务、零售和电子商务、技术、运输、制造、医疗保健和公共部门组织。

该报告仅包括来自 Dynatrace 客户的生产数据，不包括 Dynatrace 在内部使用或用于托管 SaaS 产品的所有 Kubernetes 集群。