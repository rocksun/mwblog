<!--
title: 博通捐赠 Velero 给 CNCF：或将重塑 Kubernetes 备份与灾难恢复
cover: https://cdn.thenewstack.io/media/2026/03/5549fe65-shahid-mehmood-jbggbq1q5a0-unsplash-scaled.jpg
summary: Broadcom 将 Velero 捐赠给 CNCF，解决 Kubernetes 备份与灾难恢复痛点。Velero 将由社区中立治理，强化数据保护与迁移，巩固 Broadcom 云原生地位。
-->

Broadcom 将 Velero 捐赠给 CNCF，解决 Kubernetes 备份与灾难恢复痛点。Velero 将由社区中立治理，强化数据保护与迁移，巩固 Broadcom 云原生地位。

> 译自：[Broadcom donates Velero to CNCF — and it could reshape how Kubernetes users handle backup and disaster recovery](https://thenewstack.io/broadcom-velero-cncf-kubernetes/)
> 
> 作者：B. Cameron Gain

Broadcom VMware 周一[宣布](https://news.broadcom.com/news/2026-kubernetes-ecosystem)，将把 Velero 捐赠给 CNCF 沙盒项目。该公司将此举描述为一种将 VMware vSphere Kubernetes Service 扩展到私有云和公共云中 Kubernetes 用户组织的方式。

借鉴用户组织的反馈，Broadcom VMware 与开源选项的集成不断扩大，这让用户在混搭 Kubernetes 基础设施支持方面拥有更多自由。除了将 Velero 捐赠给 CNCF，Broadcom 还通过与更多第三方开源供应商（包括 F5、Tigera Calico Enterprise 和 Kong API Gateway）的 API 兼容性来扩展 VMware vSphere Kubernetes Service。

在发布会前与媒体的简报中，Broadcom VMware 的代表试图向社区保证，它正在加大对开源的支持和贡献——特别是对最大的 CNCF 项目 Kubernetes——并选择 KubeCon + CloudNativeCon Europe 作为发布这些公告的场所。

随着 VMware 捐赠 Velero，更多的开源社区和用户组织可以通过为项目贡献力量，并获得 CNCF 的支持，更轻松地整合其需求。随着项目的直接和治理控制权从 Broadcom 转移，这一方面应有助于项目服务更大社区的需求。与此同时，对于 Broadcom 而言，这加强了其作为跨云原生和私有云领域的全栈 Kubernetes 提供商的地位。

> “备份和[灾难恢复]是许多组织的巨大痛点，因为他们正试图将新的云原生世界与传统的企业 IT 世界结合起来。”

## Kubernetes 无法填补的备份空白

Omdia 分析师 Torsten Volk 告诉 *The New Stack*，将 Velero 捐赠给 CNCF 是 Broadcom 获得云原生“街头信誉”的好方法。他表示，为分布式应用程序添加企业备份和数据迁移并不简单，但在任何现有环境中，这对于成功都至关重要。

Volk 表示：“备份和[灾难恢复]是许多组织的巨大痛点，因为他们正试图将新的云原生世界与传统的企业 IT 世界结合起来。如果没有备份和 DR，你就无法做到这一点。”“如果 VMware 能将 Velero 定位为 Kubernetes 用户首选的备份、DR 和迁移工具，这将显著提升该公司的云原生故事。”

## Velero 找到了中立的归属

Broadcom 已将 Velero 提交给 CNCF 沙盒，以将该项目过渡到中立的社区治理。Velero 是一款开源的 Kubernetes 原生工具，用于备份、恢复和迁移集群及应用程序。它保护集群级资源和持久数据，从而实现灾难恢复和工作负载可移植性。这至关重要，因为 Kubernetes 默认不提供内置的集群级备份。

Velero 的起源可追溯到 Heptio，VMware 在五年多前收购了该公司。Heptio 是一个以 API 为中心的项目，由前 Google 和 Kubernetes 联合创始人 Joe Beda 和 Craig McLuckie 创立。根据 ESG 和 CNCF 的数据，Broadcom 也一直是 Kubernetes 的主要贡献者。在 CNCF 的指导下，组织可能会更有信心依靠 Velero 进行有状态应用程序恢复以及跨不同环境的工作负载可移植性。

Broadcom VCF 部门产品营销副总裁 Prashanth Shenoy 在一次媒体和分析师简报会上表示：“Velero 真正有助于保护集群级资源和持久数据，从而为我们的客户实现灾难恢复和工作负载可移植性。”“Velero 对组织而言非常关键，因为 Kubernetes 默认不提供内置的集群级备份或恢复。”

Velero 了解它是一个用于备份、恢复和迁移 Kubernetes 集群和应用程序的开源 Kubernetes 原生工具。

随着 ingress-nginx 项目将于 2026 年 3 月退役，Broadcom 正将其 [Avi 负载均衡器](https://www.vmware.com/products/cloud-infrastructure/advanced-services/avi-load-balancer)定位为原生替代品和架构升级。Avi 负载均衡器并非 NGINX 的分支。Avi 正在利用 NGINX HTTP 协议处理引擎，这是一个非差异化组件。Avi 的软件定义架构本身就是专门构建的，许多提供功能（与性能、规模、操作简易性、高可用性、弹性、分析、VCF 集成等相关）的软件模块也是如此。

此外，Broadcom 还宣布与行业领导者建立新的验证和合作伙伴关系，包括 F5（用于 Big-IP Container Ingress Service）、Kong（用于 API Gateway）和 Tigera（用于 Calico Enterprise）。Shenoy 表示：“Broadcom 拥有 AVI 转换工具或应用程序，有助于实现从 ingress-nginx 到 Hubby 的自动化迁移，将可能具有高度破坏性的变化转变为我们客户非常平稳、自动化的过渡。”

作为 VKS 3.6 版本的一部分，Shenoy 表示，VCF 的网络和性能管理方面已进行“基础性变革”。Shenoy 说，一个主要的更新是“自带 CNI”模型，该模型允许客户在集群创建时明确选择 Isovalent (Cilium) 或 Tigera (Calico Enterprise) 等接口。此外，为了支持 AI 工作负载和数据库，VKS 现在使用 QD profiles 来自动化复杂的操作系统定制，这些定制“以前是手动的，并且容易出现配置漂移”。

> “把 QD profiles 想象成性能食谱，所以你创建一次配置，它就会说，嘿，这些数据库服务器应该这样配置……这会自动应用于所有 Kubernetes 集群。”

随着 VKS 3.6 的发布，Broadcom 还引入了 QD profiles，旨在简化有状态应用程序（如数据库、现代数据引擎和 AI 工作负载）的管理。Shenoy 说：“把 QD profiles 想象成性能食谱，所以你创建一次配置，它就会说，嘿，这些数据库服务器应该这样配置。”“这会自动应用于所有 Kubernetes 集群。因此，无需任何手动调整，也不会再出现配置漂移。”

在 2025 年的最后一个季度，Broadcom 开始将 Canonical Ubuntu 直接集成到 VMware Cloud Foundation (VCF) 中。对于那些希望继续依赖 Photon OS（已默认提供）的用户，Broadcom 正在通过 Ubuntu OS 扩展平台工程师和开发人员的选择。