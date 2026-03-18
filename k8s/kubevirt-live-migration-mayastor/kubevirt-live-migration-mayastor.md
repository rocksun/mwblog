<!--
title: KubeVirt：它是什么，为何备受青睐？
cover: https://cdn.thenewstack.io/media/2026/03/06dd6b56-taufik-ramadhan-ztx9pfurtt0-unsplash-scaled.jpg
summary: KubeVirt将虚拟机引入Kubernetes，实时迁移至关重要。Mayastor通过RWX支持该功能，并探讨了NFS过渡方案与未来原生多写入块解决方案的优缺点及安全性。
-->

KubeVirt将虚拟机引入Kubernetes，实时迁移至关重要。Mayastor通过RWX支持该功能，并探讨了NFS过渡方案与未来原生多写入块解决方案的优缺点及安全性。

> 译自：[What is KubeVirt and why it’s growing](https://thenewstack.io/kubevirt-live-migration-mayastor/)
> 
> 作者：Tiago Castro

**KubeVirt** 是一个开源项目，它将虚拟机引入 Kubernetes 控制平面，让团队在相同的编排、工具和生命周期模型下并行运行虚拟机和容器。它将虚拟机打包成 Kubernetes 对象，因此运维人员可以使用单一平台以及相同的 CI/CD、可观测性和策略工具来管理这两种工作负载类型。

由于实际原因，KubeVirt 的采用最近加速了。历史上依赖 VMware 的组织正在重新评估其虚拟化堆栈，许多组织希望减少供应商锁定，并围绕 Kubernetes 整合基础设施。这种转变正在推动对容器原生虚拟化的兴趣，以在不彻底更换的情况下实现虚拟机工作负载的现代化。

## 实时迁移的意义

**实时迁移** 是指在最小或没有停机时间的情况下，将正在运行的虚拟机从一台主机移动到另一台主机的能力。在传统的管理程序环境（例如 VMware vMotion）中，实时迁移会保留客户机内存、设备状态和网络连接，因此应用程序在虚拟机移动时仍能继续运行。KubeVirt 在 Kubernetes 内部实现了相同的概念：它在虚拟机继续运行时在节点之间传输内存和设备状态，从而实现维护、负载再平衡和无中断故障转移。

> “如果没有共享存储，目标节点就无法在源节点仍在运行时挂载虚拟机磁盘，因此无法进行实时迁移。”

KubeVirt 实时迁移的一个关键要求是，虚拟机的磁盘必须能够同时从源节点和目标节点访问——用 Kubernetes 的术语来说，支持虚拟机的 PersistentVolumeClaim 必须支持 **ReadWriteMany (RWX)**。如果没有共享存储，目标节点就无法在源节点仍在运行时挂载虚拟机磁盘，因此无法进行实时迁移。

## 为什么实时迁移很重要

**实时迁移** 实现了生产环境中重要的多项操作能力：

*   **零或接近零停机维护：** 在不停止虚拟机的情况下排空和升级节点。
*   **资源再平衡：** 将高负载虚拟机移动到负载较低的节点以优化利用率。
*   **计划内故障转移和弹性：** 在硬件故障之前或为应对性能下降而撤离节点。

对于希望将虚拟机作为 Kubernetes 中的一等公民的云原生团队而言，实时迁移是一项基础功能。

## Mayastor 和 RWX 差距

**Mayastor** 是 OpenEBS 系列中一个高性能的容器原生块存储引擎。它提供复制的块卷，并通过 [NVMe-over-Fabrics](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/) (NVMe-oF) 目标暴露它们以实现低延迟访问。Mayastor 的设计侧重于 **块** 语义和同步复制以实现耐用性和性能。

Mayastor 默认情况下不提供原生的 Kubernetes RWX 块卷模式。文档中记载的解决方法是在 Mayastor 卷之上 [运行一个 NFS 服务器](https://thenewstack.io/linux-create-and-connect-to-an-nfs-share/)，并导出该文件系统，为虚拟机提供共享的 ReadWriteMany 访问。OpenEBS 文档将此模式描述为一种通过分层 NFS 服务器 Pod 和 NFS CSI 驱动程序来实现带复制 Mayastor 卷的 KubeVirt 实时迁移的方法。

**在 Mayastor 之上运行 NFS 是个好主意吗？** 这是一个实用的临时解决方案，但并非适用于所有工作负载。NFS 引入了一个额外的软件层，改变了性能特性（特别是对于期望原始块语义的 I/O 模式），并创建了一个必须高可用且配置正确的单一服务器进程。对于高性能虚拟机磁盘或对延迟和 I/O 语义敏感的工作负载，NFS 可能成为瓶颈和复杂性的来源。共享原始块设备方法将有助于减少文件系统开销，允许 KubeVirt 直接访问底层存储。

> “在 Mayastor 之上运行 NFS 是个好主意吗？这是一个实用的临时解决方案，但并非适用于所有工作负载。”

向 KubeVirt 提供原始块设备与暴露主机挂载文件相比也提高了隔离性，更进一步地，通过直接 virtio 路径（绕过额外的宿主文件系统/nvmf/块层）为虚拟机提供服务可以减少攻击面和延迟，但它也带来了必须管理的工程和操作权衡。由于这些原因，NFS 作为兼容性垫片很有用，但不能长期替代 Kubernetes 原生多写入器块解决方案。

## 将 Mayastor 块卷作为 RWX 用于 KubeVirt

由于 KubeVirt 的 virt-launcher 在迁移期间处理来自源节点和目标节点的虚拟机 I/O，因此有机会 **安全地** 将 Mayastor 块卷暴露为多节点可写，**特别是针对 KubeVirt**。Mayastor 已经暴露了 NVMe-oF 目标并为发起方实现了主机访问控制；这意味着它可以添加额外的发起方节点以允许多个主机并发连接相同的命名空间。换句话说，存储引擎已经具备了向多个节点呈现块设备的管道。

关键的促成因素是存储类和访问模式策略，它明确允许 **多节点写入器** 访问，但将其限制在 KubeVirt 用例中。由于 KubeVirt 在迁移期间协调虚拟机的 I/O（确保只有 virt-launcher 进程访问磁盘并且虚拟机的设备状态一致），这种受控的多写入器模式可以是安全的——**但前提是** 消费者是 KubeVirt 并遵循迁移协议。

## 安全性、限制和后续步骤

这种方法必须受到策略和工程控制的保护：

*   **存储类范围限定：** 创建存储类，仅针对标记或注释为 KubeVirt 虚拟机磁盘的工作负载宣传多节点写入器功能。
*   **访问控制：** 使用 Mayastor 的 NVMe-oF 发起方允许列表和身份验证来限制哪些节点可以并发连接命名空间。
*   **操作保障：** 确保遵守迁移协议和 virt-launcher 语义，从而避免两个独立的写入器同时损坏数据。
*   **故障处理：** 设计用于迁移期间的部分故障。如果迁移中断（网络闪断、节点崩溃或存储故障），系统必须避免死锁，即源和目标都认为它们拥有磁盘。这是难题的下一部分：强大的协调和恢复逻辑，能够检测中断的迁移并安全地回滚或完成它们而不会丢失数据。

## 结论

KubeVirt 将虚拟机引入 [Kubernetes，以帮助团队实现现代化](https://thenewstack.io/kubernetes-helps-teams-modernize-faster-even-on-premises/)，摆脱传统管理程序，而实时迁移是生产虚拟机移动性不可或缺的功能。Mayastor 的架构——复制块存储加上 NVMe-oF 暴露——为其提供了一条独特路径，可以在没有 NFS 垫片的情况下支持 KubeVirt 实时迁移，但这样做需要 **小心、受限的** 多写入器语义，这些语义仅在 KubeVirt 控制 I/O 时才是安全的。目前务实的方法是在 Mayastor 之上使用 NFS 以实现兼容性，但更清晰、更高性能的未来是带有强大访问控制和强大迁移故障处理的 KubeVirt 专用多节点块模式。

*这篇客座专栏在 [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 之前发表，这是云原生计算基金会的旗舰会议，将于 2026 年 3 月 23 日至 26 日在荷兰阿姆斯特丹汇集领先的开源和云原生社区的采用者和技术专家。*