
<!--
title: 开源重新定义数据平台
cover: https://cdn.thenewstack.io/media/2025/02/e24d865a-data.jpg
-->

开源解决方案提供了更灵活的基础设施，从而可以更好地控制技术堆栈的部署和管理方式。

> 译自 [Open Source Redefines Data Platforms](https://thenewstack.io/open-source-redefines-data-platforms/)，作者 Carol Platz。

支持现代工作负载（如人工智能、实时分析和云原生应用程序）对技术领导者提出了挑战，他们必须优化基础设施以实现性能、成本和可扩展性。

对于传统存储系统而言，这种平衡更加困难，因为为了满足一项要求而牺牲另一项要求的情况很常见。因此，许多领先的组织正在探索[开源](https://thenewstack.io/open-source/)和软件定义架构。

[福布斯洞察调查](https://www.vertiv.com/491ce1/contentassets/eeb0117585944a2d900d3fc46005fdc0/vertiv-forbes-modern-data-center-report.pdf)显示，只有不到三分之一 (29%) 的技术领导者和工程师表示他们的数据中心能够满足当前的业务和技术要求。这意味着，随着各组织寻求突破其传统基础设施的限制，显然需要拥抱现代化。

然而，最紧迫的问题是如何以经济高效的方式[存储](https://thenewstack.io/storage/)、管理和访问海量数据，同时又不牺牲大规模的性能和灵活性。

[OpenShift Virtualization](https://www.lightbitslabs.com/solutions/openshift-virtualization/?utm_source=TNS&utm_medium=article&utm_campaign=mar)等开源技术在数据中心越来越受欢迎，这反映了在处理当今复杂工作负载时，人们对更高的灵活性、创新性和成本节约的需求。

随着[云原生应用程序开发](https://thenewstack.io/cloud-native/)的加速，对本地云架构和混合云战略的需求也在增加，其中开源软件在管理不同环境和提供跨不同平台互操作性方面至关重要。

OpenShift-V 等开源解决方案使技术领导者能够构建更灵活的基础设施，从而更好地控制其技术堆栈的部署和管理方式，而不会被锁定在单一供应商的生态系统中。

## 开源革命

OpenShift 等开源项目彻底改变了应用程序的部署和编排。OpenShift Virtualization 在云计算中发挥着重要作用，它允许您采用云原生策略，而无需放弃现有的虚拟化基础设施。它弥合了传统虚拟机 (VM) 和现代容器化应用程序之间的差距。这种灵活性提高了运营效率，加速了数字化转型，并实现了跨不同环境的混合工作负载的无缝管理。

OpenShift Virtualization 是[Red Hat](https://www.openshift.com/try?utm_content=inline+mention)基于 Kubernetes 的 OpenShift 平台的一项功能，用于容器编排和管理。OpenShift-V 将 VM 引入 Kubernetes 环境，使您能够在同一平台上与容器化工作负载一起运行 VM。它利用了 KubeVirt 项目，这是一个旨在将虚拟化引入 Kubernetes 的开源计划。

OpenShift-V 是开源技术如何解决现代数据中心的可扩展性、性能和弹性问题的一个例子。通过采用针对 Kubernetes 优化的软件，企业可以确保其基础设施随着其快速增长的需求而发展，同时显着减少停机时间。

## 广泛的行业吸引力

OpenShift Virtualization 对于正在从传统的基于 VM 的基础设施过渡到现代的、容器化的和云原生架构的技术领导者和工程师特别有用。它提供了灵活性、渐进式现代化、高效的资源利用和统一的管理，使其成为混合云、DevOps 和多云战略的宝贵工具。

在低延迟和大规模的成本效益可以提供竞争优势的行业中，例如需要能够处理实时数据分析和事务性工作负载的金融服务和[电子商务](https://thenewstack.io/a-cloud-architects-guide-to-e-commerce-data-storage/)组织，OpenShift-V 比传统系统更受欢迎。

同样，支持机器学习 (ML) 和 AI 工作负载的组织需要灵活性、性能和效率。在这些情况下，开源和基于容器的系统成为必需品。对于云服务提供商而言，他们可以在多租户环境中安全地管理客户数据，同时保持性能并降低运营成本。

OpenShift-V 的用例：

- **优化基础设施资源和成本**：通过在同一基础设施上运行虚拟机和容器，您可以优化资源利用率并降低基础设施成本。
- **容器化单体应用**：OpenShift-V 允许单体应用继续在虚拟机中运行，同时可以使用容器围绕它们构建新的服务和[微服务](https://thenewstack.io/introduction-to-containers/)。这种并排部署允许在不中断的情况下进行现代化改造，并在您准备好时提供完全容器化单体应用的未来路径。
- **将基础设施即代码用于虚拟机**：您可以将虚拟机定义为 Kubernetes 资源，这会将基础设施即代码的优势带到虚拟机管理中。这允许您自动化虚拟机的部署、配置和扩展，使管理更具动态性，并实现与现代云原生实践的更好集成。
- **测试/开发**：在 DevOps 和 CI/CD 流程中，开发人员通常需要访问多个环境，这些环境包括用于测试和开发的虚拟机和容器。OpenShift-V 提供了灵活性，可以启动基于虚拟机的测试环境，同时为容器和虚拟机维护一致的基于 Kubernetes 的基础设施。当需要在虚拟机中运行的旧应用程序与新的容器化服务集成或测试时，这尤其有用。
- **传统应用程序的逐步现代化**：OpenShift-V 可以在单个平台上共存虚拟机和容器，从而使您可以逐步将传统应用程序迁移到云原生、容器化的架构。这有助于降低与大规模迁移项目相关的风险和成本，让您可以逐步地实现应用程序的现代化。
- **混合云和多云灵活性**：您可以在混合云或多云环境中运行虚拟机和容器的组合，从而提供灵活性并确保不同的工作负载可以共存。通过使用 Kubernetes 跨不同的云（公共云或私有云）管理基于虚拟机和容器化的应用程序，您可以根据业务需求部署工作负载，而不会受到基础设施的限制。
- **整合虚拟机和容器工作负载**：通过将虚拟机和容器化应用程序整合到单个平台上，从而降低基础设施的复杂性并优化您的资源。这种整合简化了基础设施管理，减少了运营开销并提高了资源利用率。

## 软件定义存储为 OpenShift-V 提供强大动力

虚拟化环境中的主要挑战之一是随着规模的扩大保持一致的性能。这意味着随着工作负载的增长，您可能会遇到性能瓶颈或用户体验下降。

当使用 OpenShift-V 对您的技术堆栈进行现代化改造时，不要忽视您的存储平台。软件定义存储可以为 OpenShift-V 提供强大动力，从而增强应用程序的性能、可扩展性和成本效益。

[Lightbits block storage](https://www.lightbitslabs.com/blog/4-reasons-why-block-storage-is-gaining-momentum-in-the-enterprise/?utm_source=TNS&utm_medium=article&utm_campaign=mar) 是一种选择，它提供了一个开源容器存储接口 (CSI) 插件，该插件与 OpenShift-V 无缝集成。此插件允许您轻松地为虚拟机配置和管理高性能持久存储，从而使部署和扩展变得轻而易举。它提供超过 7500 万 IOPS 的可扩展性，并具有一致的亚毫秒级延迟。

如果您想了解更多关于使用软件定义存储为 OpenShift Cloud 提供强大动力，请下载我们的白皮书，该白皮书比较了 [open source storage Ceph to Lightbits](https://www.lightbitslabs.com/software-defined-storage-private-clouds-lightbits-vs-ceph-storage/?utm_source=TNS&utm_medium=article&utm_campaign=mar)。
