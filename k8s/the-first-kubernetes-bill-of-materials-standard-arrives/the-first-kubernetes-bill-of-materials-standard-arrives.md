# 第一个 Kubernetes 物料清单标准来了

翻译自 [The First Kubernetes Bill of Materials Standard Arrives](https://thenewstack.io/the-first-kubernetes-bill-of-materials-standard-arrives/) 。


软件物料清单已经成为代码安全防御中常见的一部分。现在，针对 Kubernetes 的也有了。

![](https://cdn.thenewstack.io/media/2023/06/09585507-rod-long-al7mll5dzk4-unsplash-e1686591219922-1024x724.jpg)

如果你还没有使用[软件物料清单（SBOM）](https://thenewstack.io/how-to-create-a-software-bill-of-materials/)，那么很快你将开始使用。它们被视为构建代码安全防御的基础工作。虽然有许多 SBOM 标准，比如[软件包数据交换（SPDX）](https://spdx.dev/)，[CycloneDX](https://cyclonedx.org/specification/overview/)，以及 GitHub 的[依赖项提交格式](https://docs.github.com/en/rest/dependency-graph/dependency-submission?apiVersion=2022-11-28)，但直到现在，针对流行的容器编排程序 Kubernetes 还没有一个专门的标准。现在有了 [Kubernetes 安全运营中心（KSOC）](https://ksoc.com/) 的 [Kubernetes 物料清单（KBOM](https://github.com/ksoclabs/kbom)）标准。

在这个早期阶段， KBOM 是一个初稿。它提供了 [JavaScript 对象表示法（JSON）](https://thenewstack.io/why-and-how-you-should-manage-json-with-sql/)的初始规范。已经证明它可以与 Kubernetes 1.19 及更高版本、超大规模的云服务提供商以及自行构建的 Kubernetes 配合使用。

通过 KBOM 的外壳界面，云安全团队可以全面了解其环境中的第三方工具。这一发展旨在加快对新的 Kubernetes 工具漏洞的响应速度。

## 有必要吗？

然而，既然已经存在许多 SBOM 标准，那么真的有必要开发一个专门针对 Kubernetes 的 SBOM 吗？鉴于超过 [96% 的组织使用 Kubernetes](https://www.cncf.io/announcements/2022/02/10/cncf-sees-record-kubernetes-and-container-adoption-in-2021-cloud-native-survey/) 来进行容器部署编排，显然在这方面存在着部署安全的差距。毕竟，[Kubernetes 的安全采用率仍然较低，2022 年只有 34%](https://www.helpnetsecurity.com/2022/07/28/kubernetes-security-shift-left-strategies-and-simplifying-management/) 。确切地了解环境范围是保护 Kubernetes 的一个主要障碍。

正如 KSOC 的首席技术官 Jimmy Mesta 解释的那样：“ Kubernetes 正在为许多我们熟知和喜爱的大型商业品牌进行应用编排。采用率不再是一个借口，然而从安全的角度来看，当涉及到标准和合规指南时，我们始终将 Kubernetes 本身排除在讨论之外，只关注应用部署之前的活动。”因此，“我们发布这个 KBOM 标准作为第一步，将 Kubernetes 纳入到合规指南的讨论中。”

为了满足这些需求，KBOM 提供了对 Kubernetes 集群元素的简明概述，包括：

* 工作负载数量。
* 托管服务的成本和类型。
* 内部和托管镜像的漏洞。
* 第三方定制，例如部署的自定义资源、身份验证和服务网格。
* 托管平台、Kubelet 等的版本详细信息。

听起来很有趣吗？确实如此。要参与贡献，您可以立即下载 CLI 工具或了解更多关于该标准的信息。您还可以通过 GitHub 页面参与这个基于 Apache 2 开源程序的开发。
