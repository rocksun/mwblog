
<!--
title: Kubernetes推进云原生数据保护：分享反馈
cover: https://cdn.thenewstack.io/media/2024/10/a0d41f8b-kubernetes-cloud-native-data-protection.jpg
-->

工作组寻求对容器存储接口中新的变更块跟踪 (CBT) 功能的反馈，以将增量备份引入 Kubernetes。

> 译自 [Kubernetes Advances Cloud Native Data Protection: Share Feedback](https://thenewstack.io/kubernetes-advances-cloud-native-data-protection-share-feedback/)，作者 Mark Lavi。

当 IT、虚拟化、备份、存储和运维团队探索 [Kubernetes](https://thenewstack.io/kubernetes/) 时，他们会将存储和数据保护功能与传统的裸机和虚拟机 (VM) 设施进行比较。由于云原生架构本质上是分布式的、API驱动的和松耦合的，因此云原生操作需要新的工具和技能才能实现相同的 [灾难恢复](https://thenewstack.io/k8s-backup-and-disaster-recovery-is-more-important-than-ever/) (DR) 业务成果。虽然许多云原生存储优势令人印象深刻，但仍缺少一个关键领域：变更块跟踪 (CBT)。

在最简单的情况下，CBT 通过 [增量备份](https://en.wikipedia.org/wiki/Incremental_backup) 提高备份效率——仅查找和传输当前存储在存储中的内容与最新备份映像之间的差异。CBT 可以发现自上次备份以来几乎没有发生变化，并以最小的占用时间、CPU、内存或存储空间来创建几乎即时的全新备份。缩短备份窗口并减轻其负担也有助于组织更频繁地执行备份，从而减少恢复点目标 (RPO) 或发生的數據丢失量。

CBT 是存储系统的一项功能。大多数这些系统提供对卷进行快照的能力，这会在快照拍摄时创建卷的只读视图。启用 CBT 后，存储系统将跟踪写入的每个块，并可以提供两个快照之间发生更改的块列表。如果在快照之间多次写入块，则只需要复制一次，因为快照备份时的状态是唯一需要保留的状态。这使得卷备份非常高效，尤其是从未写入的块不需要备份。

由于几乎每个存储提供商都提供 CBT，因此令人惊讶的是，Kubernetes 的云原生存储缺乏此功能。为什么？更长的答案将在后面给出，但简短的答案是，经过两年的努力，Kubernetes CBT 即将到来！存储和备份供应商以及项目可以进行原型设计、提供反馈并改进 CBT，使其成为进入 Kubernetes alpha 阶段的行业级解决方案。

## 有状态的 Kubernetes 工作负载和存储

[十年](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/) 之后，Kubernetes 首次亮相，有状态的工作负载已变得司空见惯。但当 Kubernetes 在 2018 年发布 [StatefulSets](https://www.veeam.com/blog/stateful-vs-stateless-kubernetes.html) 时，云原生存储需要一段时间才能加速。
容器存储接口 (CSI) 版本 1.0 也在 2018 年与 [Kubernetes 1.13](https://kubernetes.io/blog/2018/12/03/kubernetes-1-13-release-announcement/) 一起被采用。CSI 为不同的存储提供商提供统一的 API，并且是一个独立的联盟，发布行业范围的规范。它已被领先的平台采用，例如 [Cloud Foundry](https://www.cloudfoundry.org/?utm_content=inline+mention)、[Apache Mesos](https://mesos.apache.org/) 和 [HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) Nomad。

存储供应商创建 CSI 驱动程序，这些驱动程序安装在 [Kubernetes](https://roadmap.sh/kubernetes) 集群上。Kubernetes 代码库中所有专有的“树内”存储驱动程序都已（或正在）被移除，以支持 CSI。

[Kubernetes 数据保护工作组](https://github.com/kubernetes/community/blob/master/wg-data-protection/README.md) (DPWG) 由 [Kubernetes 存储特别兴趣小组](https://github.com/kubernetes/community/tree/master/sig-storage) (SIG-Storage) 于 2020 年成立。同样在 2020 年，CSI 规范发布了 `VolumeSnapShot`，该规范在 Kubernetes 1.20 中发布。以前，Kubernetes 备份和恢复只能通过 CSI 处理文件系统，或者诉诸专有存储驱动程序。CSI 块存储备份很快变得可能，并且比文件系统备份更加健壮。

## 社区驱动的努力

以下是将 CBT 添加到 CSI 和 Kubernetes 的简要概述。

2022 年 5 月，DPWG 启动了 [Kubernetes 增强提案 (KEP) #3314：变更块跟踪](https://github.com/kubernetes/enhancements/pull/4082)。在 SIG 领导、同行 SIG、供应商（包括 [Veeam](https://www.veeam.com/)）和 Kubernetes 社区的指导和审查下，KEP 3314 经历了三次重大重新设计。每一次都经过反复的概念阶段，从设计审查到辩护，每一步都改进范围以解决问题和差距。在 API 和安全特别兴趣小组 (SIG API 和 [SIG 安全](https://thenewstack.io/cncfs-special-interest-group-for-security/)) 帮助整合 Kubernetes 架构和安全最佳实践后，这种 CBT 设计得到了改进。最终，在 2023 年，第三个设计获得了 DPWG 的批准，代码原型完成，并提出了将 CBT 添加到 CSI 规范的建议。

[CSI 规范 1.11.0](https://github.com/container-storage-interface/spec/releases/tag/v1.10.0) 通过 `SnapshotMetadata` 服务发布了 CBT，并在 2024 年 6 月将 KEP-3314 的状态更新为“可实施”。第一个目标是 Kubernetes 1.31，作为带有原型代码的 alpha API，但准备测试管道、添加文档和学习其他 Kubernetes 和 CSI 维护者任务导致其推迟到 Kubernetes 1.32。

## 云原生 CBT 设计
CSI CBT 实现的目标受众是 Kubernetes 云原生备份和存储供应商。CBT 设计过程包括两个新领域：

- 存储供应商和项目应采用和部署 SIG-Storage CSI CBT 元数据服务 sidecar 容器和自定义资源。然后，CSI 驱动程序应实现：
    - 添加新的 `SnapshotMetadata` 服务，允许容器编排器获取快照的已分配或已更改的块元数据。请参阅：
      - [external-snapshot-metadata](https://github.com/kubernetes-csi/external-snapshot-metadata)
      - [Snapshot Metadata Service RPCs](https://github.com/container-storage-interface/spec/blob/v1.10.0/spec.md#snapshot-metadata-service-rpcs) spec
    - 备份供应商和项目应采用新的 Kubernetes API，这些 API 通过 gRPC 使用 CBT
        - KEP 目前是 [“v1alpha” 实现](https://github.com/kubernetes/enhancements/pull/4082) CSI 规范

以下安全图显示了备份软件和集群存储如何协调并向 `VolumeSnapShot` 提供 CBT 访问权限：

![](https://cdn.thenewstack.io/media/2024/10/5e375c64-volumesnapshot.png)

更多技术资源：

- [KEP 3314 设计幻灯片和图表](https://docs.google.com/presentation/d/11nCmMkOEm5sY7zGQeXmsAV2wR7mb8HUYPKWyXhyD86o/edit#slide=id.p)
- 云原生 Rejekts 2023 演讲：“彻底改变 Kubernetes 中的数据备份：释放 CSI 变更块跟踪的力量”的 [摘要](https://cfp.cloud-native.rejekts.io/cloud-native-rejekts-na-chicago-2023/talk/HGPYB3/) 和 [视频](https://www.youtube.com/watch?v=sV1skj7OW7Y&list=PLnfCaIV4aZe-4zfJeSl1bN9xKBhlIEGSt&index=29) (30 分钟)
- [DPWG：数据保护工作流程](https://github.com/kubernetes/community/blob/master/wg-data-protection/data-protection-workflows-white-paper.md) 白皮书

## 请分享您的反馈
云原生 CSI CBT 的旅程刚刚开始实施阶段。Kubernetes DPWG 和 CSI 联盟希望您对 CSI CBT 提供反馈。

随着 CSI CBT 进入 alpha 阶段，您可以帮助采用和改进。请宣传并提供可以纳入 beta 阶段的反馈。

- **对于存储供应商和项目**：采用 CSI CBT 是否与通过新的 CSI CBT sidecar 容器 API 公开现有功能一样简单？这取决于 CSI 驱动程序的当前架构以及您底层存储 CBT 功能。请告诉我们这个示例是否有用。
- **对于备份供应商和项目**：CSI CBT 的采用是否应该像使用支持 CSI CBT 存储供应商的新 Kubernetes API 一样简单？模拟提供程序和测试在哪里，它们是否满足您的需求？
- **对于 Kubernetes 社区**：联系您的备份和存储供应商和项目，并要求他们采用 CSI CBT 以改进您的数据保护。

帮助 CSI CBT 取得成功。加入 [DPWG 双周会议或在 Slack 频道和邮件列表中联系我们](https://github.com/kubernetes/community/blob/master/wg-data-protection/README.md#meetings)；我们随时为您解答问题。此外，注册参加 [Kubernetes 数据保护工作组深入探讨](https://kccncna2024.sched.com/event/1hovn/kubernetes-data-protection-wg-deep-dive-dave-smith-uchida-veeam?iframe=no&w=100%25&sidebar=yes&bg=no) 会议，该会议将于 11 月 13 日星期三在 KubeCon + CloudNativeCon 北美举行。

每天，越来越多的人问：“现在是迁移到 Kubernetes 的时候了吗？”将 CSI CBT 带入云原生存储消除了更长的 RPO，这是与传统基础设施相比的一个关键劣势。我们渴望与云原生生态系统和社区合作，实施 CSI CBT 并推动世界一流的云原生数据保护向前发展。

*要详细了解 Kubernetes 和云原生生态系统，请加入我们参加 **KubeCon + CloudNativeCon 北美**，该活动将于 2024 年 11 月 12 日至 15 日在犹他州盐湖城举行。*
