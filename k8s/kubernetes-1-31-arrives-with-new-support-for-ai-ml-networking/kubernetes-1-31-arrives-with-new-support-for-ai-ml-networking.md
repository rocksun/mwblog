
<!--
title: Kubernetes 1.31新增对AI/ML和网络的支持
cover: https://cdn.thenewstack.io/media/2024/08/05686cc8-kubernetes-1-31.png
-->

此版本代号为“Eli”，引入了设备资源分配，该功能标准化了访问硬件加速器的流程。

> 译自 [Kubernetes 1.31 Arrives with New Support for AI/ML, Networking](https://thenewstack.io/kubernetes-1-31-arrives-with-new-support-for-ai-ml-networking/)，作者 Chris J Preimesberger。

通常，一个软件版本包含很多[版本号](https://thenewstack.io/rustlangs-semantic-versioning-still-breaks-too-many-apps/)并不被认为是[“主要”版本](https://thenewstack.io/tricks-api-versioning/)。这被称为“点”版本。主要的版本通常被简化为简单的 X.0 或 XX.0。

但是，不要忽视 Kubernetes 的 v1.31.0，它今天正式发布。该版本的负责人 [Angelos Kolaitis](https://github.com/neoaggelos) 表示，他认为这是一个“主要次要版本”，并且它足够重要，值得关注。

[Kubernetes](https://www.thenewstack.io/Kubernetes)，也称为 K8s，[最初由](https://thenewstack.io/how-the-kubernetes-community-celebrated-its-10th-anniversary/) [Google](https://cloud.google.com/?utm_content=inline+mention) 开发，是一个开源平台，旨在自动化容器化应用程序的部署、扩展和管理。在过去十年中，它在 IT 系统中的普及率和生产使用率大幅提升。

Kolaitis 表示，这个最新版本（Kubernetes 每年按计划发布三个版本）在支持[AI/ML 工作负载处理](https://thenewstack.io/ai/)和[网络](https://thenewstack.io/networking/)方面取得了重大进展。

## Kubernetes 1.31.0 的新特性

为了支持 AI/ML 工作负载，v1.31.0 引入了一种针对[(OCI) 镜像](https://thenewstack.io/how-bumblebee-eases-ebpf-observability-with-oci/) 的卷类型，使开发人员能够通过简单地更换镜像来轻松更改工作负载中使用的大型语言模型。OCI 镜像现在用作 Kubernetes 中的卷源，因此更改模型或模型权重变得更加简单。

Kolaitis 表示：“使用特定模型的开发人员现在可以像更改镜像一样更改一些 OCI 元素，例如在想要升级或尝试新事物时进行部署。这是一个非常熟悉的流程。”

OCI ([开放容器倡议](https://thenewstack.io/open-container-initiative-creates-a-distribution-specification-for-registries/)) 指的是一组开放标准和规范，用于管理容器镜像的创建、分发和执行。

新版本以更标准化和高效的方式公开有关 Pod 使用的硬件设备（如 GPU）的信息。最后，它为新的设备资源分配 (DRA) 功能提供了初步支持，该功能有助于标准化访问和管理硬件加速器（如 GPU）的过程。

在网络方面，v1.31.0 改进了 Kube-proxy，这是一个关键的网络组件，负责集群内的服务发现和负载均衡，它使用新的 nftables 存储桶，有助于解决性能限制。存储桶用于在 nftables 中实现速率限制和流量整形机制。它们有助于防止网络拥塞，确保公平的带宽分配，并防止潜在的攻击，例如拒绝服务 (DoS) 攻击。

Kolaitis 表示，新版本还继续简化和稳定其核心网络组件，提供更高的可靠性和稳健性，而无需用户进行更改。

## DRA 的作用是什么？

Kolaitis 表示，设备资源分配 (DRA) 功能是标准化访问硬件加速器过程的重要一步。DRA 使得能够更有效地将硬件设备（如 GPU、现场可编程门阵列 (FPGA) 或网络接口卡 (NIC)）分配和管理到特定的 Pod。

关于 DRA 的关键数据点：

* **设备插件**：Kubernetes DRA 使用设备插件与底层硬件交互，使集群能够发现设备。
* **资源管理**：一旦设备被识别，它们就会成为 Kubernetes 中可管理的资源，类似于 CPU 或内存。
* **Pod 分配**：用户可以在其 Pod 规范中请求特定的设备或设备数量，Kubernetes 的调度程序会尝试将这些 Pod 放置在具有匹配可用设备的节点上。
* **独占访问**：DRA 确保对分配的设备的独占访问，防止多个 Pod 争用相同的硬件资源。
* **扩展资源 API**：Kubernetes 中的扩展资源 API 使得能够表示和分配这些专用硬件设备。

## Kubernetes 1.31 中的其他改进

v1.31.0 中的其他改进包括：

* Kubernetes 对 AppArmor 的支持现已正式发布。
* 持久卷最后阶段转换时间功能在 v1.31 中正式发布。
* nftables 后端在 v1.31 中进入测试阶段，位于新添加的功能开关之后。
- 服务的流量分配在 v1.31 中进入测试阶段，默认启用。
- 对匿名 API 访问进行了新的限制。

[点击此处](https://deploy-preview-47281--kubernetes-io-main-staging.netlify.app/blog/2024/08/13/kubernetes-v1-31-release/) 访问完整的博客文章，详细介绍 v1.31.0 版本。

[点击此处](https://github.com/kubernetes/sig-release/tree/master/releases/release-1.31) 查看 GitHub 版本说明。

