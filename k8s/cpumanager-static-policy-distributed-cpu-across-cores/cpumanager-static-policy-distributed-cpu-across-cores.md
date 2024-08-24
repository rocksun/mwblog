
<!--
title: Kubernetes v1.31新的Kubernetes CPUManager静态策略：跨核心分配CPU
cover: https://kubernetes.io/blog/2024/08/22/cpumanager-static-policy-distributed-cpu-across-cores/cpu-cache-architecture.png
-->

在 Kubernetes v1.31 中，我们很高兴地宣布对 CPU 管理功能进行重大改进：CPUManager 静态策略的 distribute-cpus-across-cores 选项。此功能目前处于 alpha 阶段，默认情况下处于隐藏状态，标志着旨在优化 CPU 利用率并提高多核处理器系统性能的战略转变。了解该功能 传统上，Kubernetes 的 CPUManager 倾向于尽可能紧凑地分配 CPU，通常将它们打包到最少的物理核心上。

> 译自 [Kubernetes v1.31: New Kubernetes CPUManager Static Policy: Distribute CPUs Across Cores](https://kubernetes.io/blog/2024/08/22/cpumanager-static-policy-distributed-cpu-across-cores/)，作者 Jiaxin Shan。

## 了解该功能

传统上，Kubernetes 的 CPUManager 倾向于尽可能紧凑地分配 CPU，通常将它们打包到最少的物理内核上。但是，分配策略很重要，同一个物理主机的 CPU 仍然共享物理内核的一些资源，例如缓存和执行单元等。

![cpu-cache-architecture](https://kubernetes.io/blog/2024/08/22/cpumanager-static-policy-distributed-cpu-across-cores/cpu-cache-architecture.png)

虽然默认方法最大程度地减少了核间通信，并且在某些情况下可能是有益的，但它也带来了一个挑战。共享物理核心的 CPU 可能导致资源争用，进而可能导致性能瓶颈，特别是在 CPU 密集型应用程序中明显可见。

通过修改分配策略，新的 distribute-cpus-across-cores 特性解决了这个问题。启用时，此策略选项指示 CPUManager 尽可能跨多个物理核心分配 CPU（硬件线程）。此分布旨在最大程度地减少共享相同物理核心的 CPU 之间的争用，从而可能通过为它们提供专用核心资源来增强应用程序的性能。

从技术上讲，在此静态策略中，免费 CPU 列表按图中所示方式重新排序，目的是从单独的物理核心分配 CPU。

![](https://kubernetes.io/blog/2024/08/22/cpumanager-static-policy-distributed-cpu-across-cores/cpu-ordering.png)

## 启用该功能

要启用此功能，用户首先需要添加 --cpu-manager-policy=static kubelet 标志或 KubeletConfiuration 中的 cpuManagerPolicy: static 字段。然后用户可以向 Kubernetes 配置中的 CPU 管理器策略选项中添加 --cpu-manager-policy-options distribute-cpus-across-cores=true 或 distribute-cpus-across-cores=true。此设置指示 CPU 管理器采用新的分配策略。需要注意的是，此策略选项当前不能与 full-pcpus-only 或 distribute-cpus-across-numa 选项结合使用。

## 目前的局限性和未来的方向

与任何新功能一样，特别是处于 alpha 阶段的功能，存在局限性和未来改进的空间。目前的一个重大局限性是 distribute-cpus-across-cores 无法与其他在 CPU 分配策略方面可能冲突的策略选项结合使用。此限制可能会影响与某些工作负载和部署场景的兼容性，而这些场景依赖于更专门的资源管理。 

展望未来，我们致力于提高 distribute-cpus-across-cores 选项的兼容性和功能性。未来的更新将重点解决这些兼容性问题，允许此策略与其他 CPUManager 策略无缝结合。我们的目标是提供一个更灵活、更强大的 CPU 分配框架，可以适应各种工作负载和性能需求。

## 结论

在 Kubernetes CPU 管理器中引入 distribute-cpus-across-cores 策略，是我们不断改进资源管理和增强应用程序性能所做的一种持续努力。通过减少物理内核上的争用，该特性提供了一种更均衡的 CPU 资源分配方法，对运行异构工作负载的环境尤其有益。我们鼓励 Kubernetes 用户测试这一新特性并提供反馈，这将有助于指导其未来的发展。

本文旨在清晰地解释这一新特性，同时设定对其当前阶段和未来改进的预期。

## 延伸阅读

请查看节点任务页面上的控制 CPU 管理策略，以详细了解 CPU 管理器，以及它与其他节点级资源管理器之间的关系。