# Cloud Foundry 如何随 Kubernetes 发展

![Cloud Foundry 如何随 Kubernetes 发展专题图片](https://cdn.thenewstack.io/media/2024/10/38422f4b-railroad-1024x576.jpg)

Cloud Foundry (CF) 发生了重大演变，尤其是在其与 Kubernetes (K8s) 的关系方面。俗话说，变化是唯一的不变。

CF 和 K8s 最初被视为独立的实体，但逐渐 [融合](https://thenewstack.io/kubernetes-and-cloud-foundry-better-together/)，KubeCF 和 [Eirini](https://thenewstack.io/with-project-eirini-cloud-foundry-adapts-to-a-new-open-source-ecosystem/) 等项目使 CF 能够在 K8s 上原生运行。这种演变导致了 [cf-for-k8s](https://thenewstack.io/cloud-foundry-aims-to-bring-the-ease-of-cf-push-to-kubernetes/) 的开发，这是一个拥抱 Kubernetes 组件并提供简化开发人员体验的云原生 CF 发行版。

虽然 CF 仍然是管理大规模同构工作负载的强大平台，但它与 K8s 的集成扩展了其功能，并巩固了其在云原生领域的地位。

## Cloud Foundry 和 Kubernetes：多年来的发展历程

在 2017 年 Cloud Foundry 欧洲峰会上，我们的成员 SAP、IBM 和 SUSE 提出了将 Cloud Foundry 容器化的想法，从而催生了 Eirini 和 [Quarks](https://thenewstack.io/cloud-foundry-containerized-project-quarks-and-project-eirini/)。次年，开始了关于 Cloud Foundry 和 Kubernetes 的兼容性和集成的讨论。

最初尝试使用云提供商接口 (CPI) 在 K8s 上运行 CF 时遇到了困难，原因是“分裂脑协调器”问题。像 Fissile 和 SCF 这样的项目通过消除 BOSH 运行时方面，提供了一种在 K8s 上部署 CF 的更原生方法。

研究了嵌套容器的概念，强调容器是同级关系，而不是真正的嵌套关系。开发了一个名为“Cube”的原型，可以使用其他容器调度器部署 Cloud Foundry 应用程序，目标是结合 CF 和 K8s。

## KubeCF 的出现

2019 年，在 Kubernetes 上运行 Cloud Foundry 底层的转折点出现了。KubeCF 作为一个稳定可靠的容器化 Cloud Foundry 实现应运而生，直接使用和重新利用了 BOSH 发布工件。[VMware](https://tanzu.vmware.com?utm_content=inline+mention) 发布了由 Kubernetes 支持的 Pivotal Application Service (PAS) alpha 版本，展示了 Kubernetes 作为 PAS 底层容器编排的集成。

Cloud Foundry 基金会宣布 KubeCF 成为一个新的孵化项目，标志着 Cloud Foundry 和 Kubernetes 社区之间合作的一个重要里程碑。Eirini 项目使 Cloud Foundry 应用程序能够作为标准 Kubernetes 工作负载执行，从而无需单独的容器调度器。

## 两项技术比一项好吗？

2020 年，支持两种并行的方法来应用 Kubernetes 抽象。一方面，社区继续致力于 KubeCF，同时投入时间和资源开发一种使用云原生资源的更原生的 Kubernetes 方法。随着 cf-for-k8s 1.0（一个 Kubernetes 原生 Cloud Foundry 发行版）的发布，社区完全拥抱了 Kubernetes。Cloud Foundry 的核心组件已更新，以支持 kpack、Istio 和更广泛的 Kubernetes 集群版本。

KubeCF 也得到了维护，发布了 2.5 版本，标志着使 Kubernetes 成为 Diego 容器编排引擎替代方案的努力结束。此外，还发布了项目 Stratos 4.2（一个基于 Web 的管理控制台），该项目增强了管理 Kubernetes 和 Helm 图表存储库的功能。

## 三次尝试终获成功

目前，Cloud Foundry 社区正在开发 [Korifi 项目](https://thenewstack.io/cloud-foundry-launches-korifi-to-ease-kubernetes-development/)，该项目设想在 Kubernetes 上构建一个 Cloud Foundry，提供与 CF 相同的开发人员体验，同时与 Kubernetes 技术集成。我们的目标是保持与现有 CF 环境的兼容性，但也对可能牺牲一些兼容性的实用解决方案持开放态度。我们认识到，K8s 上的 CF 需要遵循 Kubernetes 实践和云原生方法。我们概述了将 CF 与 Kubernetes 技术集成的指导原则，同时在必要时保留特定于 CF 的概念。

社区认为，Korifi 应该与 Kubernetes 和云原生生态系统中的项目和技术集成，作为 CF 子系统的替代品。特别是在这些生态系统项目得到广泛采用和运营成熟的情况下。例如，用于应用程序工件生成的 kpack 和 [Cloud Native Buildpacks](https://thenewstack.io/streamlined-apm-integration-in-cloud-native-buildpacks/)，以及用于入口路由和服务网格的 Istio。
## 相同点！

Cloud Foundry 和 Kubernetes 之间有许多技术基础。从历史上看，它们都源于 Google 的 BORG 项目。BOSH 是 Cloud Foundry 的基石之一，被设计为 BORG 的下一代，因此命名为 BOSH（字母 S 在 R 之后，H 在 G 之后 - 因此 BORG -> BOSH）。

使用容器作为不可变工件进行部署，并对其进行编排以保持可靠性和可用性服务水平目标 (SLO)，是这两种工具的支柱。这两种工具都假设应用程序是按照 12 要素原则设计的，并且对要部署的有状态应用程序提供特殊支持。sidecar 模式也是这两种技术共同拥有的。

## 前进之路

科技世界肯定足够大，这两种技术可以共存。我认为选择 Cloud Foundry 还是 Kubernetes 并不是一场零和博弈。对于那些希望在操作虚拟机和基于容器的编排时获得融合体验的人来说，Cloud Foundry 将继续作为一个强大且维护良好的选择而存在。对于喜欢直接使用 Kubernetes 的修补匠来说，生态系统将提供全面支持。

有些人会寻求两全其美，对于他们来说，一种减少 CNCF 环境认知负担的固执抽象将是最佳选择。

*要详细了解 Kubernetes 和云原生生态系统，请于 11 月 12 日至 15 日在美国犹他州盐湖城参加 **KubeCon + CloudNativeCon North America**。*

---

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展日新月异，请勿错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、采访、演示等内容。