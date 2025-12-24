<!--
title: Kubernetes：驾驭动态资源分配，性能极致释放
cover: https://cdn.thenewstack.io/media/2025/12/29aab06c-kubecon25-belamaric-ohly-klues.jpg
summary: Kubernetes引入DRA，通过精细调度CPU、GPU、网卡等资源，优化资源密集型AI项目性能，解决硬件不对齐问题，提升效率。主流厂商已支持。
-->

Kubernetes引入DRA，通过精细调度CPU、GPU、网卡等资源，优化资源密集型AI项目性能，解决硬件不对齐问题，提升效率。主流厂商已支持。

> 译自：[Kubernetes: Get the Most from Dynamic Resource Allocation](https://thenewstack.io/kubernetes-get-the-most-from-dynamic-resource-allocation/)
> 
> 作者：Joab Jackson

随着数据中心电力和硬件价格的飞涨，大多数组织很快将寻求从现有投资中榨取更多效率，尤其是在 Kubernetes 上运行[资源密集型 AI 项目](https://thenewstack.io/the-ai-competition-is-now-a-high-stakes-construction-race/)的组织。

在过去一年中，来自[云原生计算基金会](https://cncf.io/?utm_content=inline+mention)的一个跨基础工作组一直在积极开发 Kubernetes 调度器的增强功能，该功能将允许用户更具体地将作业分配给其节点中的 CPU、网卡、GPU 和各种 AI 加速器，从而让他们享受到各种效率和性能改进。

随着最近发布的 [Kubernetes 1.34](https://thenewstack.io/kubernetes-v1-34-introduces-benefits-but-also-new-blind-spots/) 和上周发布的 [Kubernetes 1.35](https://thenewstack.io/kubernetes-1-35-timbernetes-introduces-vertical-scaling/)，DRA 的核心部分已经安装并准备投入生产。

“用户定义的资源放置是我在过去六七年中在这个社区见过的最大改进，”Fluidstack 技术人员 [Byonggon Chun](https://www.linkedin.com/in/byonggonchun/) 在 [KubeCon + CloudNativeCon 2024 North America](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) 的一次演讲中热情地表示。

## 什么是 DRA？

英特尔高级软件工程师 [Patrick Ohly](https://github.com/pohly) 在 KubeCon 的另一场[演讲](https://youtu.be/Op4DNDTij1U)“DRA 正式发布！”中指出，你可以将 DRA 视为一组新的可扩展 Kubernetes API，它是设备插件的更丰富替代品。

旧式的插件只能提供节点上可用设备的数量。通过 DRA，每个设备都用一组属性（称为 `ResourceSlice`）来描述，其中可能包括可用的内存量或计算核心的数量。

此信息提供给 Kubernetes 的内置作业调度器 `kube-scheduler`（Kubernetes 还有许多高性能的第三方调度器，因此如果你正在使用这些调度器，请检查它是否已支持 DRA）。

在提交作业时，用户会提交一个 `ResourceClaim`，指定作业所需的组件，例如 GPU。调度器会将请求与可用设备池进行匹配并执行作业。

“你可以根据工作负载的需要任意混合搭配，”Ohly 解释道。

用户甚至可以指定配置设置，这些设置甚至可以告诉设备如何配置底层硬件。

[![](https://cdn.thenewstack.io/media/2025/12/663981bf-kubernetes-dra-01.jpg)](https://cdn.thenewstack.io/media/2025/12/663981bf-kubernetes-dra-01.jpg)

DRA 将是为 GPU 和 CPU 集群调度工作的理想选择。“当你提交 GPU 请求时，调度器知道如何找到拥有 GPU 的节点，而不是只有 CPU 的节点，”英伟达杰出工程师 [Kevin Klues](https://www.linkedin.com/in/klueska/?originalSubdomain=de) 在“DRA 正式发布”演讲中解释道。

许多公司已经发布了 DRA 兼容的驱动程序，包括[英特尔](https://github.com/intel/intel-resource-drivers-for-kubernetes)、[英伟达](https://github.com/NVIDIA/k8s-dra-driver-gpu)、[谷歌](https://github.com/google/dranet)、[AMD](https://github.com/ROCm/k8s-gpu-dra-driver) 和 [Furiosa](https://github.com/furiosa-ai/furiosa-dra-driver-guide)。

[谷歌](https://cloud.google.com/?utm_content=inline+mention)和 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 还合作开发了 [DRANET](https://dranet.dev/docs/)，这是一款用于高性能工作负载的 Kubernetes 网络驱动程序，两家公司已将其[捐赠给 CNCF](https://youtu.be/KOqyTeFf6K8?list=PLj6h78yzYM2PEePwKKCnyqIQQrHvDZko-)。

## 优化 DRA

但 DRA 最终不仅仅是为作业找到合适的节点，还在于优化资源调度，以便用户从其硬件中获得最佳性能。

DRA 有助于解决未对齐问题，谷歌软件工程师 [Gaurav Ghildiyal](https://www.linkedin.com/in/gaurav-kumar-ghildiyal/?originalSubdomain=in)（曾参与 DRANET 工作）在另一场 KubeCon 演讲“通过 DRA 中的硬件对齐实现峰值性能”中解释道。

如果你在 CPU 和 GPU 集群上运行 AI/ML 作业，你可能已经注意到性能存在很大差异。

在基准测试中，Ghildiyal 和 Chun 已经演示了工作负载在最好的情况下如何仅达到完整效率的 40%。

[![服务器架构图。](https://cdn.thenewstack.io/media/2025/12/177ed4ab-kubecon-hardware-alignment.jpg)](https://cdn.thenewstack.io/media/2025/12/177ed4ab-kubecon-hardware-alignment.jpg)

现代服务器可能拥有多个 CPU，并可托管多个 GPU，这些 GPU 可能位于不同的 PCI 数据总线上，或者拥有独立的内存区域 (Ghildiyal)。

即使在同一节点上，在两个 GPU 之间移动数据也可能导致显著的性能可变性，这取决于数据是否必须跨越同一服务器上的不同 CPU 或内存区域。

当 CPU 流量必须跨越内存边界到达 GPU 时，两者之间的数据传输时间会延长。或者 GPU 和网卡位于不同的内存或 PCI 域时，数据在它们之间传输所需的时间会更长。

传统上，K8s 无法理解将 CPU 分配给同一总线上的 GPU。

[![](https://cdn.thenewstack.io/media/2025/12/4bfe39c6-gaurav_ghildiyal-byonggon_chun-300x225.jpg)](https://cdn.thenewstack.io/media/2025/12/4bfe39c6-gaurav_ghildiyal-byonggon_chun-300x225.jpg)

*谷歌的 Gaurav Ghildiyal（左）和 FluidState 的 Byonggon Chun（图片来源：Joab Jackson/TNS）*

DRA 为用户指定了基础，例如，GPU 和网卡应该位于同一 PCI 总线上。

DRA 将设备局部性暴露给调度器，这样调度器就可以进行局部性感知调度。用户可以提交一个包含所需特定资源的 `ResourceClaim`，调度器可以搜索 `ResourceSlice` 索引以查找可用资源。

“关键点是，我们现在有了一种方法，可以向通用调度器宣传设备局部质量，这在很长一段时间内都是不可能的，”Chun 在硬件对齐的演讲中解释道。

## 资源对齐

Ghildiyal 指出，许多工作负载都受益于资源对齐。

其中之一是 LLM 推理和训练，这是一个分布式工作负载问题，其中多个 GPU 希望彼此通信（通常通过 RDMA）。理想情况下，网卡应该与 GPU 位于同一 PCI 总线上。

在 GPU 与网卡分离的情况下，工作负载数据不仅可能经历更长的传输时间，还会在跨 CPU 的插槽间互连结构上产生“大量拥塞”。

[![性能时间对比图。](https://cdn.thenewstack.io/media/2025/12/d932fa40-kubecon-hardware-alignment-02.jpg)](https://cdn.thenewstack.io/media/2025/12/d932fa40-kubecon-hardware-alignment-02.jpg)

*硬件未对齐导致的性能差异 (Ghildiyal)。*

基于 DRA 的预防措施可能会在 `ResourceClaim` 上附加一个资源约束（“*resource.kubernbetes.io/pcieRoot*”），告诉调度器只选择网卡和 GPU 位于同一 PCI 总线上的节点。

另一个受益的工作负载是将 LLM 数据加载到 GPU 中。在这里，CPU 与 GPU 的对齐可以节省大量时间，如下图所示：

[![同一服务器上 CPU/GPU 对齐的示意图 ](https://cdn.thenewstack.io/media/2025/12/39176102-kubecon-hardware-alignment-03.jpg)](https://cdn.thenewstack.io/media/2025/12/39176102-kubecon-hardware-alignment-03.jpg)

*单服务器上的 CPU/GPU 对齐。*

同样，CPU 和网卡之间的对齐对于网络密集型应用程序（如数据库）也将是有益的。

在两位演示者进行的基准测试中，一组未对齐的资源仅具有完全对齐资源吞吐量的 71%（Ghildiyal 表示，更高的网络带宽将使其进一步受益）。

Ohly 表示，尽管 DRA 的核心组件已可供使用，但工作组计划开发更多功能以实现更大的资源控制，例如扩展硬件拓扑的能力。因此，未来几年对于 Kubernetes 调度器来说将是充满挑战的。