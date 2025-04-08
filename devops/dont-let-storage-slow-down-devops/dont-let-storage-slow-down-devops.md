
<!--
title: 不要让存储拖慢DevOps的速度
cover: https://cdn.thenewstack.io/media/2025/04/8e20736c-files.jpg
summary: 别让存储拖垮DevOps！虚拟化平台如OpenShift Virtualization需高性能存储，块存储提供低延迟、高可用，加速AI/ML数据管道。Kubernetes存储方案用PersistentVolumes和StorageClasses管理VM存储。CSI接口实现灵活存储管理。NVMe加速，IOPS监控，异地备份保障数据安全。
-->

别让存储拖垮DevOps！虚拟化平台如OpenShift Virtualization需高性能存储，块存储提供低延迟、高可用，加速AI/ML数据管道。Kubernetes存储方案用PersistentVolumes和StorageClasses管理VM存储。CSI接口实现灵活存储管理。NVMe加速，IOPS监控，异地备份保障数据安全。

> 译自：[Don’t Let Storage Slow Down DevOps](https://thenewstack.io/dont-let-storage-slow-down-devops/)
> 
> 作者：Carol Platz

虚拟化云平台为 DevOps 和软件开发人员提供了强大而灵活的环境，可以更快、更敏捷、更高效地构建、部署和管理基于云的应用程序。 示例包括 [OpenShift Virtualization](https://www.lightbitslabs.com/solutions/openshift-virtualization/)、[VMware vSphere](https://thenewstack.io/vmware-cloud-foundation-could-bring-price-relief/) 和 [基于内核的虚拟机 (KVM)](https://thenewstack.io/amazon-web-services-open-sources-a-kvm-based-fuzzing-framework/)。

可以快速配置资源，快速扩展应用程序，并在云环境之间移动工作负载，从而可以自由地自定义平台以满足特定的应用程序工作负载需求。 但是，这些[平台的性能和效率与它们的基础数据存储内在相关](https://thenewstack.io/open-source-redefines-data-platforms/)。 存储瓶颈可能导致应用程序性能下降，甚至超时。

为虚拟化平台选择合适的存储解决方案可确保您的组织实现无缝的可扩展性、高性能和运营效率。 适当的[存储支持持久存储卷](https://thenewstack.io/deploying-cloud-native-persistent-storage-in-the-age-of-containers/)，这对于有状态应用程序至关重要。

## 块存储的作用

[块存储](https://www.lightbitslabs.com/solutions/openshift-virtualization/?utm_source=TNS&utm_medium=article&utm_campaign=apr) 提供了释放虚拟化平台全部潜力所需的性能、可扩展性和敏捷性。 块存储可以无缝集成，为[虚拟机 (VM) 和容器](https://thenewstack.io/kubernetes-gets-back-to-scaling-with-virtual-clusters/)提供统一的存储层。 这通过确保持续的性能和关键工作负载（如事务和实时分析）以及新兴的 AI/机器学习 (ML) 数据管道的可用性来增强应用程序的可靠性。

主要优势包括低延迟访问、灵活的扩展和高可用性，这些对于性能敏感型应用程序都至关重要。 块存储解决方案可以进行定制，以满足特定的性能和可扩展性需求，从而确保即使在高峰负载期间也能平稳运行。

## 虚拟化的 Kubernetes 存储解决方案

[Kubernetes 存储解决方案](https://www.lightbitslabs.com/kubernetes-persistent-storage-management/?utm_source=TNS&utm_medium=article&utm_campaign=apr) 提供了 VM 中持久存储的机制。 这些解决方案利用 Kubernetes 的功能，如 PersistentVolumes (PV)，它为有状态应用程序提供持久存储，以及 StorageClasses，它定义了具有不同性能和可用性特征的不同存储类型。 虚拟化平台可以集成这些功能来管理和配置 VM 的存储资源，从而确保在这些 VM 中运行的应用程序可以访问持久且可靠的存储。 这种集成使开发人员可以在统一的环境中管理容器化和虚拟化工作负载的存储。

### 容器存储接口和平台集成

[容器存储接口](https://www.lightbitslabs.com/blog/scaling-red-hat-openshift-v-with-lightbits-part-1/?utm_source=TNS&utm_medium=article&utm_campaign=apr) (CSI) 是一种 API 标准，有助于将第三方存储解决方案与基于 Kubernetes 的平台集成。 这确保了灵活的存储管理和与供应商无关的存储解决方案，从而为组织提供了更大的选择和对其基础设施的控制。

使用 CSI 可以支持动态 [OpenShift 虚拟化存储](https://www.lightbitslabs.com/solutions/openshift-virtualization/?utm_source=TNS&utm_medium=article&utm_campaign=apr) 配置，从而提高工作负载的性能、可扩展性和易管理性。 这种集成简化了存储操作并确保了高效的资源分配。

## 虚拟化环境的存储最佳实践

为了最大限度地提高存储性能，请考虑实施分层存储策略。 这涉及根据访问频率对数据进行分类，并将其放置在适当的存储层上 - 用于频繁访问数据的高性能非易失性内存 Express (NVMe) 驱动器和用于不太关键数据的经济高效的选项。 主动管理 IOPS，以确保您的存储可以处理应用程序需求。 持续监控存储资源可以主动识别和解决潜在的瓶颈。 实施自动扩展机制可确保存储资源能够适应波动的工作负载，从而保持一致的性能。

数据保护和业务连续性需要强大的数据保护计划。定期备份对于数据恢复至关重要。跨区域复制提供了额外的保护层，以防止区域性中断。自动故障转移系统可以自动切换到备份系统，从而最大限度地减少停机时间。现代虚拟化平台提供了一些工具来创建弹性架构，从而最大限度地减少数据丢失和停机时间。通过整合这些策略，您可以确保应用程序和数据的安全性和可用性，即使在中断期间也是如此。

## 加速 DevOps 周期

现代虚拟化平台（如 OpenShift-V）使组织能够构建弹性、可扩展的云环境，从而使 DevOps 能够推动创新并实现卓越运营。实施正确的存储解决方案可通过增强性能、降低成本和提高灵活性来优化 DevOps 运营。

此外，支持混合云部署的能力使这些平台对需要桥接本地和云基础设施以实现数据移动性的组织具有吸引力。包括加密、访问控制和监控在内的安全功能进一步增强了它们的吸引力，确保了数据保护和高可用性。灵活性、性能和安全性的结合使优化的存储成为现代开发工作流程的基石。

如果您想了解更多关于在 OpenShift-V 环境中为 DevOps 构建可靠、可扩展且高性能的存储平台的信息，请[观看此视频](https://youtu.be/SRwGYmTp0Jo?si=VhUCqpaixcp-BKvG)。
]