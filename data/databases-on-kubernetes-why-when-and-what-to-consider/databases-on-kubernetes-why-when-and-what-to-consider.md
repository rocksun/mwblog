
<!--
title: Kubernetes上的数据库：为什么、何时以及需要考虑什么
cover: https://cdn.thenewstack.io/media/2024/09/42b3f3bd-databases-on-kubernetes-considerations.jpg
-->

在 Kubernetes 上运行数据库越来越普遍，但这必须对您的组织有意义。了解需要考虑的关键因素。

> 译自 [Databases on Kubernetes: Why, When and What To Consider](https://thenewstack.io/databases-on-kubernetes-why-when-and-what-to-consider/)，作者 Kathryn Hsu。

数据库在 Kubernetes 中越来越受欢迎；在最近 Portworx 委托进行的 [使用 Kubernetes 的组织调查](https://portworx.com/resources/voice-of-kubernetes-expert-report/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand) 中，超过 72% 的受访者表示他们的团队正在 [Kubernetes 上运行数据库](https://portworx.com/database-as-a-service/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand)。

显然，围绕 [Kubernetes 上的数据](https://thenewstack.io/managing-data-on-kubernetes-dok-solving-the-underlying-challenges) (DoK) 的讨论已经成熟，因为 Kubernetes 中的持久卷在 2019 年进入通用可用性。拥有更先进 Kubernetes 实践的团队正在超越 [无状态与有状态](https://thenewstack.io/3-reasons-to-bring-stateful-applications-to-kubernetes/) 应用程序的简单争论以及对持久存储的需求。相反，他们正在考虑容器数据管理层（包括数据库）如何与更广泛的业务目标以及其内部平台的基础设施、开发和交付解决方案相适应。

## 组织在 Kubernetes 中运行数据库的原因

对于软件、基础设施和 [平台工程](https://thenewstack.io/platform-engineering/) 领导者来说，决定在容器中运行数据库并使用 [Kubernetes](https://thenewstack.io/kubernetes/) 进行管理通常归结为以下因素的混合：

### 开发速度

如果数据是为最终用户提供差异化价值的有效载荷，那么应用程序就是交付工具。例如，社交新闻提要为每个人提供类似的功能，但它依赖于底层数据来确保与读者的相关性。

Kubernetes 的声明式特性允许数据库团队定义一致的部署指南并在开发、登台和生产环境中进行标准化。这消除了数据库配置作为瓶颈，从而更快地为最终用户提供更多价值。

### 降低成本，减少复杂性

在经济挑战中，数据库团队被要求用更少的资源做更多的事情。他们必须管理更多数据库实例，以更大的规模，来自更多数据库提供商和供应商，并与越来越复杂的基礎設施服務集整合。

Kubernetes 提供了一种降低复杂性的方法，因为它对跨环境的数据库部署的标准化方法简化了维护。虽然托管云数据库提供了部署捷径，但在实践中 [它们通常会引入更多复杂性](https://portworx.com/blog/break-the-chains-of-cloud-databases-with-data-on-kubernetes/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand)，通过管理辅助云服务，并增加了云锁定带来的弊端，这会增加成本并阻碍数据迁移。

### 降低风险，提高正常运行时间，大规模弹性

Kubernetes 专为运行弹性、可扩展、高弹性的应用程序而设计。为什么不让数据库也从在 Kubernetes 上运行中受益，以及从一个庞大、全球性的云原生社区的集体知识中受益，这些社区正在遵循这些原则进行构建？

## 何时在 Kubernetes 上运行数据库

如果您的应用程序需要可扩展的、自动化的数据管理，并且摩擦最小，并且您需要在开发、测试和生产环境中保持一致性，那么在 Kubernetes 上运行数据库是一个绝佳的选择。

Kubernetes 的优势包括生命周期管理、自助服务功能和增强的數據可移植性，特别是对于现代的云原生应用程序，其中模式和数据大小可能会快速变化。

## Kubernetes 上的数据有哪些好处？

在 Kubernetes 上运行数据库可以实现：

- **大规模自动化操作和生命周期管理**，尤其是在[操作符](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)几乎适用于市场上所有数据库解决方案的情况下。
- **开发、测试和生产环境的一致性**。这是[Docker](https://www.docker.com/?utm_content=inline+mention)容器的最初承诺，但适用于数据库。开发人员可以在[minikube](https://minikube.sigs.k8s.io/docs/)上本地部署数据库，并更有信心他们的应用程序将在其他地方按配置运行。
- **更轻松的数据可移植性**，用于近线或本地处理，从而提高性能，减少数据漂移，并提高整体抵御云原生应用程序的波动和弹性的能力。
- **面向最终用户的自助服务功能**，包括开发人员、数据科学家和机器学习运营 (MLOps) 工程师。数据库团队可以提供指南和策略，而最终用户可以对模式、位置和使用情况做出明智的决定。如果数据库与更广泛的开发平台正确集成，数据库管理员 (DBA) 和开发人员都不会承担[管理 Kubernetes](https://roadmap.sh/kubernetes)本身的负担。

其他数据库（例如具有数十年历史交易数据的 TB 级关系数据库管理系统 (RDBMS) 部署或海量非结构化数据湖）具有惯性，不太可能成为容器化的候选者。它们很大，难以移动，并且与支持现代应用程序开发的现代数据库有不同的用途。

## 在 Kubernetes 上引入数据库时要考虑的事项

假设您的组织已决定不使用托管云数据库或在虚拟机 (VM) 上运行数据库，并且认为更快开发速度、更低成本和降低风险的优势值得向 Kubernetes 上的数据库迈进。在进行此更改时，您和您的团队还应该考虑什么？

作为领导者，您可能会关注团队的优先事项、技能和时间，并相应地投资于技术解决方案。数据库团队通常是数据库专家，而不是 Kubernetes 专家。虽然许多开发人员熟悉容器和 Kubernetes，但他们的主要工作很少包括管理 Kubernetes 部署。

考虑 DBA 或开发人员是否将负责在 Kubernetes 上配置和管理数据库，或者这是否需要更广泛的、由内部开发人员或数据库平台支持的自动化即服务方法。如果是后者，您需要确定内部平台应提供多少级别的 Kubernetes 抽象来支持其他团队。此外，您需要定义如何根据持久卷、存储阵列以及备份或数据保护策略配置容器化数据库。

## 拥抱 Kubernetes 上的数据

对于刚刚开始 Kubernetes 之旅的组织来说，在 Kubernetes 上运行数据密集型工作负载可能看起来很令人生畏。（如果您的组织现在处于这种状态，您并不孤单！）但这是可以做到的；[Rivian](https://portworx.com/blog/breakthrough-award-winner-rivian-automotive-cloud-champion/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand) 等企业正在生产环境中在 Kubernetes 上运行数据库，并在几小时内而不是几天内完成配置，同时提高正常运行时间、弹性和控制成本。
