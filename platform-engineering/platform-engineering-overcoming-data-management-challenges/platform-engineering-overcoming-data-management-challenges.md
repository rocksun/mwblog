
<!--
title: 平台工程：克服数据管理挑战
cover: https://cdn.thenewstack.io/media/2024/10/335c14c1-platform-engineering-data-management.jpg
-->

Kubernetes 数据平台对于处理容器存储接口冲突以及跨任何云构建安全、可扩展的应用程序至关重要。

> 译自 [Platform Engineering: Overcoming Data Management Challenges](https://thenewstack.io/platform-engineering-overcoming-data-management-challenges/)，作者 Adam Swidler。

平台工程正在改变组织开发和部署应用程序的方式，使开发人员能够专注于解决业务问题，而不是管理复杂的云基础设施。

通过构建[内部开发平台 (IDP)](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/)，企业可以加速创新，增加收入并提高客户留存率，同时减少开发人员的认知负荷。

[Gartner](https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering)预测，到 2026 年，80% 的大型软件工程组织将建立平台工程团队。这比 2022 年的 45% 有所增长。

## 什么是平台工程？

[平台工程](https://thenewstack.io/whats-platform-engineering-and-how-does-it-support-devops/) 是设计和构建内部开发平台、工具链和工作流程的学科，这些平台、工具链和工作流程为软件工程组织提供自助服务功能。平台工程的关键目标是摆脱“票证操作”——开发人员通过票证请求基础设施的做法——并转向自助服务平台，开发人员可以在其中独立管理其基础设施需求。这使他们能够专注于通过应用程序开发创造价值。

黄金路径或预定义的工作流程模板在平台工程中起着至关重要的作用。这些路径通过为开发人员提供用于 CI/CD 管道或新项目设置等任务的预配置工具来加速开发。例如，[Bechtle](https://thenewstack.io/platform-engineering-reshapes-software-dev-at-bechtle/) 实施了一个标准化平台，极大地减少了其开发人员在管理基础设施上花费的时间，使他们能够专注于软件开发和客户需求。

## Kubernetes 和平台工程

[Kubernetes](https://roadmap.sh/kubernetes) (K8s) 的兴起在推动平台工程采用方面发挥了重要作用。Kubernetes 和更广泛的云原生环境为组织提供了标准化工具，以简化构建 IDP 的过程。

Portworx 最近的调查，“[Kubernetes 专家之声报告](https://portworx.com/resources/voice-of-kubernetes-expert-report/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand)” 显示，80% 的受访组织计划在未来五年内在云原生平台上构建大部分新应用程序，86% 的组织打算在混合云环境中构建其云原生平台。

借助 Kubernetes，平台工程师可以自动化许多流程，为开发团队提供自助服务功能，同时保持跨环境的一致性。

在平台工程中使用 Kubernetes 的主要优势包括：

1. **一致性**：Kubernetes 使平台团队能够采用社区支持的工具，这些工具在各种基础设施环境中提供一致的工作流程。组织可以标准化机密、CI/CD 管道和第二天的操作（如[监控和可观察性](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/)）的管理。
2. **自助服务访问**：Backstage、Crossplane 和 Helm 等工具使平台工程师能够提供自助服务功能，使开发人员能够在无需等待运营团队的情况下配置基础设施资源。这种自助服务模式已成功地由 Bechtle 等公司实施，Bechtle 使用平台工程来减少开发人员对运营团队配置基础设施的依赖。
3. **避免云锁定**：通过利用 Kubernetes，平台工程师可以创建跨云提供商工作的自动化工作流程，避免供应商锁定。这有助于确保应用程序可以在任何云或本地基础设施堆栈中移植。

## CSI 造成平台工程挑战

但是，虽然 Kubernetes 解决了许多挑战，但它并没有完全解决跨云环境的一致性问题。例如，Crossplane 和 Terraform 等工具有助于自动化 Kubernetes 集群配置，但特定于云的[容器存储接口 (CSI)](https://github.com/container-storage-interface/spec/blob/master/spec.md) 插件通常会造成存储和数据管理不一致，例如：

1. **存储功能不一致**：不同的云提供商通过其 CSI 插件提供不同的存储服务。例如，[AWS](https://aws.amazon.com/?utm_content=inline+mention)的 Elastic Block Storage CSI 插件需要额外的步骤才能启用 RWX（读写多）卷，而[Microsoft](https://news.microsoft.com/?utm_content=inline+mention)在 Azure Kubernetes Service 中默认提供 RWX 卷。这些差异迫使平台工程师开发自定义脚本以确保跨云环境的一致存储功能。
2. **复制和高可用性**：云提供商以不同的方式实现复制和高可用性，这使得难以在开发、测试和生产环境中保持一致性。这会导致开发人员必须解决的生产问题，通常会增加应用程序代码的复杂性。
3. **第 2 天运营**：第 2 天运营（如数据保护和灾难恢复）在不同的云平台上有所不同，要求平台团队创建额外的自定义。这与平台工程的目标相矛盾，即减少开发人员和运营团队的认知负荷。

## 使用 Kubernetes 数据平台加速开发人员

与其为每个存储阵列或云提供单独的 CSI 插件，不如使用统一的[Kubernetes 数据平台](https://thenewstack.io/managing-data-on-kubernetes-dok-solving-the-underlying-challenges/)，可以加速开发人员将功能从开发更快地迁移到生产。它还为您的 K8s 工作负载提供应用程序和数据敏捷性，以便您可以将应用程序从本地迁移到云，反之亦然。

Kubernetes 数据平台通过在 Kubernetes 环境中提供一致的云原生存储层，帮助您解决与 CSI 相关的挑战并简化您的环境。它抽象了云提供商和 CSI 插件之间的差异，使开发人员和平台工程师能够使用统一的平台工作，而不会影响功能。

1. **一致的存储体验**：K8s 数据平台允许平台团队在 Kubernetes 集群中提供统一的存储体验，无论它们是在 AWS、Azure 还是[Google](https://cloud.google.com/?utm_content=inline+mention)Cloud Platform (GCP) 上运行。开发人员可以配置存储卷（ReadWriteOnce [RWO] 或 RWX），而无需担心云特定的差异。
2. **弹性和可靠性**：K8s 数据平台在集群和区域之间提供集群内复制和灾难恢复，以实现高可用性。这使开发人员可以专注于构建应用程序，而不必担心基础设施故障。
3. **新的黄金路径**：K8s 数据平台使平台工程师和 DevOps 团队能够创建新的黄金路径，简化应用程序测试和部署。开发人员可以在灾难恢复设置中测试应用程序，并验证生产环境将按预期执行。此外，与 Flux 和 Argo CD 等 CI/CD 工具的集成可以实现完全自动化。
4. **数据库即服务 (DBaaS)**：在 K8s 数据平台上，平台工程师和 DevOps 团队可以在 Kubernetes 发行版中提供数据库即服务。这可以消除管理不同数据库的多个运营商的需要，从而实现统一的[数据库管理](https://thenewstack.io/databases-on-kubernetes-why-when-and-what-to-consider)体验。
5. **应用程序迁移**：当开发人员可以无缝地在区域和云之间迁移应用程序时，平台团队可以管理跨区域或跨云迁移，而不会给开发人员带来复杂性。

Kubernetes 数据平台是任何[内部开发平台](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/)的关键组成部分。这使平台团队能够打包和自动化[存储和数据库](https://thenewstack.io/bring-storage-and-databases-under-kubernetes-control)配置，以便开发人员可以自助访问这些功能。

**案例研究**

福特汽车公司是竞争激烈的汽车制造行业的领导者。随着来自全球各地的竞争以及新的电动汽车 (EV) 制造商的出现，福特需要加快其创新周期，同时保持严格的质量标准。

容器和 Kubernetes 是其数字化转型战略的关键部分。但是，管理持久存储成为开发人员的负担，降低了他们的生产力，并使他们更难满足对更快创新的日益增长的需求。此外，福特对 Kubernetes 的投资使其必须找到一种存储解决方案，以确保业务连续性和提供强大的灾难恢复。
福特通过实施 Kubernetes 数据平台，在不增加 IT 团队运营复杂性的情况下，克服了这些挑战，并获得了以下关键优势：

- 为 Kubernetes 应用程序提供高性能持久存储。
- 为关键应用程序提供无缝灾难恢复和业务连续性。
- 简化的自助服务方法，使开发人员摆脱了复杂的存储管理。
- 更快的服务交付和更高的运营效率。

凭借 Portworx 作为其应用程序开发堆栈的关键组成部分，福特在其 IT 基础设施和开发人员生产力方面看到了变革性的成果。主要改进包括：

- 现代化的基础设施，通过自动化的自助服务存储赋能开发人员。
- 降低复杂性，使开发人员能够专注于价值创造和创新。
- 提高开发人员生产力，加快新服务和应用程序的上市时间。
- 简化多云数据迁移，确保跨不同环境的无缝操作。

福特云技术主管兼经理 Satish Puranam 表示：“归根结底，我们谈论的是在特定价格点和特定质量下，赋能开发人员并加快服务交付速度……在没有持久存储的情况下，我们几乎无法在 Kubernetes 中做任何事情。”

通过解决存储管理负担，福特能够保持其高标准的质量，同时赋能其开发人员以更快、更高效地进行创新。

## 摘要

平台工程通过启用自助服务功能和简化基础设施管理，正在改变应用程序开发。但是，持久数据管理挑战仍然阻碍着创建完全一致、可扩展和安全的平台。传统的存储供应商 CSI 插件通常面临性能和可扩展性限制，将数据和应用程序绑定到特定的存储基础设施。云提供商通过专有 CSI 和昂贵的数据出站费用进一步加剧了这种情况，导致数据锁定。

Portworx 通过提供一致的 Kubernetes 存储、高可用性和跨环境的无缝应用程序迁移来克服这些障碍，使开发人员能够专注于创新，并在任何云中构建安全、可扩展的应用程序。

正如福特和 Bechtle 等组织所证明的那样，拥抱平台工程对于提高开发人员生产力和减少管理基础设施所花费的时间至关重要。这确保了开发人员可以“一次构建，随处移植，随处运行”，而不会影响跨云的性能或可扩展性。

加入我们下一场 [动手实验室](https://portworx.com/hands-on-labs/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand)，了解 Portworx 如何增强您的内部开发平台，并加速您的软件开发和生成式 AI 项目。
