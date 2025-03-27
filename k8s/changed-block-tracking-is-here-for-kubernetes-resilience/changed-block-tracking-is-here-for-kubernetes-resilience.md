<!--
title: Kubernetes弹性：变更块追踪已就绪
cover: https://cdn.thenewstack.io/media/2025/03/38e60fab-changed-block-tracking-kubernetes-resilience.jpg
summary: K8s弹性恢复迎来新突破！CSI规范引入**Changed Block Tracking (CBT)**，提升备份效率，RPO/RTO不再是难题。Data Protection Working Group (DPWG)力推KEP#3314，结合gRPC，云原生数据保护比肩传统方案。KubeCon见！
-->

K8s弹性恢复迎来新突破！CSI规范引入**Changed Block Tracking (CBT)**，提升备份效率，RPO/RTO不再是难题。Data Protection Working Group (DPWG)力推KEP#3314，结合gRPC，云原生数据保护比肩传统方案。KubeCon见！

> 译自：[Changed Block Tracking Is Here for Kubernetes Resilience](https://thenewstack.io/changed-block-tracking-is-here-for-kubernetes-resilience/)
> 
> 作者：Mark Lavi

当 IT、虚拟化、备份、存储和运维团队探索 [Kubernetes](https://thenewstack.io/kubernetes/) 时，他们会将其存储和数据保护能力与传统的裸机和虚拟机 (VM) 设施进行比较。由于 [云原生架构](https://thenewstack.io/cloud-native/) 本质上是分布式的、API 驱动的和松散耦合的，因此云原生运维需要新的工具和技能来实现与旧技术相同的业务成果。

业务连续性涵盖备份、[灾难恢复 (DR)](https://thenewstack.io/k8s-backup-and-disaster-recovery-is-more-important-than-ever/)、针对勒索软件的网络弹性以及审计合规性；它通常通过两个指标来衡量：[恢复点目标 (RPO) 和恢复时间目标 (RTO)](https://thenewstack.io/defining-low-data-loss-downtime-tolerances-in-kubernetes/)。当努力快速达到这些指标时，与传统产品相比，云原生数据保护通常缺少一个关键领域：[changed block tracking (CBT)](https://thenewstack.io/kubernetes-advances-cloud-native-data-protection-share-feedback/)。

## Kubernetes 社区如何构建与 CSI 对齐的 CBT

自 2018 年以来，Kubernetes 弃用了“in tree”存储驱动程序，转而支持容器存储接口 (CSI) 规范，以进行行业范围的协作和标准化。CBT 从根本上提高了备份效率，因此需要具有 CBT 的专有存储驱动程序来满足业务需求。

两年来，[Kubernetes Data Protection Working Group (DPWG)](https://github.com/kubernetes/community/blob/master/wg-data-protection/README.md) 致力于引入 CBT 以满足 CSI 规范和 Kubernetes API，并消除 Kubernetes 采用的这一障碍。

2022 年 5 月，DPWG 启动了 [Kubernetes Enhancement Proposal (KEP) #3314](https://github.com/kubernetes/enhancements/pull/4082) 以实现 CBT。在 Kubernetes 特别兴趣小组 (SIG) 领导、同行 SIG、供应商和 Kubernetes 社区的指导和审查下，KEP 经历了三次重大重新设计。每次重新设计都经历了概念和设计阶段，并且每个步骤都改进了其范围以解决问题和差距。

在与 API 和 Security SIG 审查后，CBT 设计被纳入 Kubernetes 架构和安全最佳实践中。最终，在 2023 年，第三个设计获得了 DPWG 的批准，代码原型已完成，并提出了将 CBT 添加到 CSI 规范的建议。

[CSI specification 1.11.0](https://github.com/container-storage-interface/spec/releases/tag/v1.10.0) 通过 SnapshotMetadata 服务使用 CBT 增强了 VolumeSnapshot；它已发布，KEP-3314 的状态已于 2024 年 6 月移至“可实施”。从那时起，作为 Kubernetes 和 CSI 的维护者，DPWG 已经实现了具有端到端测试管道的 alpha API。

## Kubernetes CSI Changed Block Tracking 的作用

现在，存储供应商和项目可以采用和部署 SIG-Storage CSI CBT 元数据服务 sidecar 容器和自定义资源。备份供应商和项目可以采用新的“v1alpha”Kubernetes API，这些 API 通过 gRPC 使用 CBT。

通过 Kubernetes CSI CBT 增强云原生存储和备份的结合意味着 Kubernetes 数据保护可以与传统的行业业务连续性指标相媲美。

云原生生态系统和社区正在实施 Kubernetes CSI CBT，并推动世界一流的云原生数据保护向前发展！

如需更多信息，请参加在伦敦举行的 [KubeCon + CloudNativeCon Europe 2025](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)，参加 4 月 2 日星期三英国夏令时 17:00 – 17:30 在 [Level 1 | Hall Entrance S10 | Room D](https://kccnceu2025.sched.com/venue/Level+1+%7C+Hall+Entrance+S10+%7C+Room+D) 的数据处理和存储轨道中的高级讲座“Kubernetes Backup Legitimized: CSI Changed Block Tracking Has Arrived”。本次演讲将概述 Kubernetes CSI CBT 的架构、安全性、测试和可扩展性，包括演示、供应商和项目 alpha 反馈的更新，以及如何进行协作。

*要了解有关 Kubernetes 和云原生生态系统的更多信息，请加入我们在伦敦举行的 *[KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/), 4 月 1 日至 4 日。*