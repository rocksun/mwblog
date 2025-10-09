<!--
title: Kubernetes有状态应用备份与恢复实战
cover: https://cdn.thenewstack.io/media/2025/10/cccaf292-kubernetes-stateful-backup-recovery.jpg
summary: 本文介绍了Kubernetes有状态应用备份恢复策略，包括卷快照、应用级备份、增量备份及异地存储。推荐使用Velero、Stash等工具，并强调定期测试、加密备份及监控的重要性，以确保业务连续性。
-->

本文介绍了Kubernetes有状态应用备份恢复策略，包括卷快照、应用级备份、增量备份及异地存储。推荐使用Velero、Stash等工具，并强调定期测试、加密备份及监控的重要性，以确保业务连续性。

> 译自：[A Practical Guide to Kubernetes Stateful Backup and Recovery](https://thenewstack.io/a-practical-guide-to-kubernetes-stateful-backup-and-recovery/)
> 
> 作者：Adetokunbo Ige

[Kubernetes](https://thenewstack.io/kubernetes/) 是一个非常强大且稳健的平台，用于编排容器化应用程序，在管理有状态和无状态应用程序方面表现出色。管理[有状态应用程序](https://thenewstack.io/how-to-better-manage-stateful-applications-in-kubernetes/)可能具有挑战性，因为需要保持数据一致性、完整性和可用性。

适当、完善记录和经过测试的备份和恢复策略至关重要，这样当发生灾难时，您就可以轻松恢复服务，而不会丢失任何数据。在 Kubernetes 环境中实现备份和恢复有不同的方法，因此您必须确保所使用的策略与您的用例相符。

我将引导您了解可在 Kubernetes 环境中用于业务连续性的备份和恢复的基本策略和工具。

## 为什么备份和恢复对有状态应用程序至关重要？

有状态应用程序中的数据丢失可能是灾难性的。与无状态应用程序不同（它们不需要持久存储，并且可以随时轻松扩展和替换），为您的有状态应用程序制定经过测试且可靠的备份和恢复策略至关重要。有状态应用程序的示例包括：

## 理解 Kubernetes 有状态工作负载

[StatefulSet](https://thenewstack.io/how-to-run-databases-on-kubernetes-an-8-step-guide/) 在 Kubernetes 中是用于管理有状态应用程序的工作负载 API 对象。StatefulSet 提供使 Pod 能够保持粘性身份、唯一的网络身份、持久卷 (PV) 和持久卷声明 (PVC) 的能力。StatefulSet 使获取每个 Pod 的身份变得更容易，从而使执行数据库备份和恢复变得更容易。

## Kubernetes 有状态应用程序的备份策略

### 1. 卷快照

Kubernetes 提供了一种标准化的方法，可以在特定时间复制卷内容，而无需创建全新的卷。当数据库管理员想要快速恢复到以前的状态时，卷快照非常方便和强大。当需要在 Kubernetes 集群上执行维护活动时，这也会很有用。备份将在活动之前执行，管理员将在活动之后执行恢复。

**如何使用卷快照：** Kubernetes 通过容器存储接口 (CSI) 快照 API 内置支持管理卷快照，该 API 与云环境中的存储无缝集成。

可考虑的卷快照工具：

*   [Velero](https://velero.io/) 是一个流行的开源工具，用于执行 Kubernetes 资源（例如 PVC 和 PV）的备份、恢复和迁移。它还执行定期备份并与主要的云提供商集成。
*   您还可以设置一个 Kubernetes cron job。创建一个 Kubernetes cron job 资源，安排定期任务来执行 rsync 命令。rsync 工具将数据从 PV 同步或备份到备份位置，例如外部存储、云存储或另一个 PV。

### 2. 应用程序级别备份

有状态应用程序（尤其是数据库）需要一致的常规备份。简单地复制数据可能导致数据损坏，因此最好利用数据库的内置工具执行备份。

可考虑的数据库备份工具：

*   PostgreSQL：使用 pg\_dump。
*   MySQL：使用 mysqldump。
*   使用 Velero 进行定期备份。

### 3. 增量和差异备份

在数据库非常大的情况下，执行增量和差异备份将非常方便。增量和差异备份将仅备份已更改的数据，从而节省时间、带宽和存储。

*   增量备份：捕获自上次备份以来的更改。
*   差异备份：捕获自上次完整备份以来的更改。

可考虑的增量和差异备份工具：

*   [Restic](https://restic.net/) 支持高效且加密的增量备份。
*   [BorgBackup](https://github.com/HubbeKing/borg-k8s-volume-backup) 可用于备份节点上的 Kubernetes 卷。

### 4. 异地和多区域备份

为防止数据库位置的单点故障并防止数据库位置故障，请将备份存储在异地或多个区域。要在云中存储备份，您可以尝试：

*   **Amazon S3：** S3 是一种可靠且可扩展的对象存储服务，可以将数据复制到其他区域。
*   **Google Cloud Storage：** GCP Cloud Storage 与 GCP 服务集成，可存储任意量的数据并随时检索。
*   **Azure Blob Storage：** 它与 Microsoft Azure 服务集成，在云中提供可扩展、经济高效的对象存储。

## Kubernetes 有状态应用程序的恢复策略

有许多策略可以用于有状态应用程序的数据恢复。

### 1. 从卷快照恢复

以下方法可用于从 Kubernetes 环境中恢复卷快照。您还需要在尝试恢复之前验证卷快照的完整性。

*   使用 Velero 执行卷恢复。
*   使用 Kubernetes 资源将 VolumeSnapshot 恢复到新的 PV 中。

### 2. 应用程序级别恢复

使用数据库提供的内置工具执行数据库恢复。您只能使用这些工具恢复用相同工具创建的备份（例如，如果使用 mysqldump 执行 MySQL 备份）。

特定于数据库的恢复工具：

*   PostgreSQL：使用 pg\_dump。
*   MySQL：使用 mysqldump。
*   使用 Velero 进行定期备份。

### 3. 使用 Velero 进行完整的 Kubernetes 恢复

Velero 既可以备份也可以恢复 Kubernetes 资源。您可以使用 Velero 恢复 Kubernetes 资源，例如 StatefulSet、ConfigMap、Kubernetes Secret、PV 和 PVC。

所有资源成功恢复后，您可以重新挂载 PV。

## 备份和恢复的推荐最佳实践

在建立备份和恢复策略时，请确保它包含以下最佳实践：

*   执行定期、计划性备份和保留策略。
*   组织对备份进行定期测试（备份恢复），以验证其完整性和真实性。这可以自动化并生成报告进行分析。
*   监控备份失败并发送警报。您可以使用 Nagios 或 Datadog 等工具执行备份监控。
*   记录您的恢复过程。
*   对备份进行加密以确保安全。

## 灾难恢复自动化工具

以下工具可用于在 Kubernetes 环境中自动化备份和恢复。

*   Velero 是一个开源工具，用于备份和恢复 Kubernetes 工作负载。它还支持云存储和快照。
*   [Stash](https://stash.run/) 是一种原生的 Kubernetes 灾难恢复解决方案，用于备份和恢复 Kubernetes 中的卷和数据库。
*   [Ark](https://github.com/shubheksha/ark) 是一个由 [Heptio](https://github.com/heptio) 创建的开源工具，用于备份和恢复 Kubernetes 集群和 PV。Ark 允许您备份 Kubernetes 集群中的全部或部分资源，包括 PV、部署、标签等。

## 结论

定期进行灾难恢复 (DR) 演练非常重要，以确保在灾难情况下业务连续性。您还可以定期进行混沌工程等活动，这将在您的 Kubernetes 集群上模拟故障并验证您的基础设施的恢复过程。

通过实施符合您用例的备份和恢复流程策略，利用 StatefulSet、PV 快照和 PVC；使用 Velero 等备份解决方案；并维护备份和恢复策略，您可以确保您的有状态应用程序能够抵御数据丢失或损坏。

精心设计的备份和恢复策略不仅可以降低与数据丢失相关的风险，还可以提高 Kubernetes 管理应用程序的整体可靠性和可信度。这是对您的基础设施设置的未来投资，确保即使面对意外中断，运营也能持续顺利运行。

想要更深入地探索 Kubernetes 的可能性吗？查看 Andela 的指南《[使用 GitHub 和 Argo CD 为 Kubernetes 构建可伸缩的 CI/CD 流水线](https://www.andela.com/blog-posts/make-a-scalable-ci-cd-pipeline-for-kubernetes-with-github-and-argo-cd/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=kubernetes&utm_term=writers-room)》，继续您的 Kubernetes 之旅。