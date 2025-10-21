<!--
title: 在机密虚拟机中实现裸金属级GPU性能
cover: https://cdn.thenewstack.io/media/2025/10/7ce2e124-openinfra.png
summary: NVIDIA强调在OpenInfra Summit上，AI工作负载需结合Kata Containers和机密计算，实现GPU裸金属性能下的虚拟机隔离及硬件内存机密性，NVIDIA VRA解决PCIe拓扑挑战。
-->

NVIDIA强调在OpenInfra Summit上，AI工作负载需结合Kata Containers和机密计算，实现GPU裸金属性能下的虚拟机隔离及硬件内存机密性，NVIDIA VRA解决PCIe拓扑挑战。

> 译自：[How To Get Bare-Metal GPU Performance in Confidential VMs](https://thenewstack.io/how-to-get-bare-metal-gpu-performance-in-confidential-vms/)
> 
> 作者：Steven J. Vaughan-Nichols

PARIS — 在 [OpenInfra Summit Europe 2025](https://summit2025.openinfra.org/) 大会上，[NVIDIA](https://www.nvidia.com/fr-fr/) 希望向 AI 开发者、运维人员和用户明确指出：如果您想在任何地方——本地、公共云或[边缘](https://thenewstack.io/6-design-principles-for-edge-computing-systems/)——在 GPU 上运行[敏感的 AI 工作负载](https://thenewstack.io/is-ai-a-trillion-dollar-bubble-or-a-world-changing-juggernaut/)，您需要虚拟机 (VM) 级别的沙盒隔离和硬件支持的内存机密性。这意味着，NVIDIA 首席系统工程师 Zvonko Kaiser 表示，您应该将 [Kata Containers](https://katacontainers.io/)（用于容器的轻量级虚拟机）与[机密计算](https://thenewstack.io/confidential-computing-is-transforming-data-encryption-in-healthcare-finance/)结合起来，以在保留裸金属 GPU 性能的同时，防止云运营商检查您的模型和数据。

对于不熟悉的朋友们，[Kata](https://thenewstack.io/container-security-and-the-importance-of-secure-runtimes/) 是一个开源项目，它将轻量级虚拟机与容器运行时结合在一起。它利用硬件虚拟化技术为每个容器启动一个独立的虚拟机，从而在容器之间提供了强大的隔离。每个容器又运行一个最小化、精简的 Linux 内核。Kata Containers 旨在提供容器的性能优势以及虚拟机的安全性和工作负载隔离。

## 理解 Kata Containers 和轻量级虚拟机

“Kata 是微虚拟机……它正好符合云原生领域，”Kaiser 告诉听众。他认为 Kata 提供了容器运行时所缺乏的隔离，同时仍然与 Kubernetes 工作流集成。

机密计算带来的是内存中的数据和应用程序加密。我们长期以来一直通过加密在数据处于静态或在网络传输中时实现安全。现在，我们在内存中也实现了这一点。

Kaiser 解释说，将它们结合的目的是颠覆传统的威胁模型。经典的 [Kata 用法](https://thenewstack.io/kata-containers-secure-lightweight-virtual-machines-container-environments/)假设工作负载不受信任，因此它保护主机免受容器影响。机密计算，利用 SEV/TDX 等 CPU 安全功能，则认为：“我们不信任基础设施。”因此，通过加密虚拟机，即使您的云提供商也无法对客户机内存进行快照或检查。

## 机密计算和证明的作用

为了确保这确实有效，他强调了证明作为将整个堆栈粘合在一起的机制的重要性。只有在经过密码学证明虚拟机及其启动/客户机状态与预期配置匹配后，秘密或密钥才能释放给工作负载。这使得控制平面、工作节点和 Pod 之间能够建立全栈信任模型。“证明您的状态……确实是您正在衡量的状态的过程”是机密部署的核心，Kaiser 说道。

AI 和 NVIDIA 的结合点在于利用这些技术让您能够在机密虚拟机中像使用裸金属一样使用 GPU。Kaiser 解释了 NVIDIA 如何努力使 GPU 工作负载“提升并迁移”到 Kata/机密虚拟机中，而不损失性能或功能。

## 为 AI 工作负载实现裸金属 GPU 性能

为此，NVIDIA 利用 Kubernetes 构建块、GPU Operator 和容器设备接口 (CDI)——以便驱动程序、库和设备映射能够完全按照裸金属上的方式呈现给容器。“我们只是将我们在裸金属上已有的这种模式，放入到最终环节，以便在 Kata 中运行的容器能够感受到并表现得与在裸金属上运行完全相同。”

这项工作包括支持 PCIe 直通、[单根 I/O 虚拟化 (SR-IOV)](https://learn.microsoft.com/en-us/windows-hardware/drivers/network/overview-of-single-root-i-o-virtualization--sr-iov-)、[GPUDirect](https://developer.nvidia.com/gpudirect) [远程直接内存访问 (RDMA)](https://www.digitalocean.com/community/conceptual-articles/rdma-high-performance-networking) 以及每个 Pod 的运行时配置，以便一个 Pod 可以使用 PF 直通，而另一个使用 SR-IOV。至关重要的是，Kata 对客户机内核的依赖将用户空间与主机内核更改解耦。这降低了主机更新会破坏工作负载虚拟机内部 GPU 驱动程序的风险。

## 使用 NVIDIA VRA 解决 PCIe 拓扑挑战

这听起来可能很复杂，但据 Kaiser 说，真正困难的部分是拓扑。NVIDIA 的解决方案是其[虚拟化参考架构 (VRA)](https://docs.nvidia.com/ai-enterprise/planning-resource/reference-architecture-for-multi-tenant-clouds/latest/architecture-overview.html)。NVIDIA 即将更详细地发布这种解决 PCIe 拓扑和虚拟机内部 GPU 对等通信棘手问题的方法。它支持两种方法：

*   **扁平化层次结构：** 在这种方法中，您简化拓扑以使配置更容易。云提供商有时已将其用于机密 AI 部署，但代价是隐藏了有用的对等链接。
*   **主机拓扑复制：** 检测主机的 PCIe/输入-输出内存管理单元 (IOMMU) 布局并在客户机内部镜像它，保留 PCIe 地址转换服务 (ATS) 和 PCIe 访问控制服务 (ACS) 标志，从而支持 GPU 对等 DMA 和 GPUDirect 行为。

为什么是两种？所以“您可以扁平化层次结构，因为您说您不关心层次结构……或者您可以说‘我想要主机复制，因为我正在处理 P2P 对象。’因此，两种模式都受支持。”Kaiser 解释道。

NVIDIA 还解释了针对 [IOMMU](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/conceptual/iommu.html) 分组和 PCIe 插槽限制的实用变通方法。例如，您可以仅将所需的 GPU 设备选择性地映射到客户机根端口，而将不相关的外围设备留在桥接端口上。这避免了不必要的设备直通和复杂性。

Kaiser 表示 NVIDIA 正在与 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)、[IBM](http://www.ibm.com/products/webmethods-hybrid-integration?utm_content=inline+mention) 和开源 Kata 社区合作，将 VRA 和工具上游化，包括主机拓扑检测和性能指南。其他即将发布的出版物涵盖了机密虚拟机的 CPU 绑定、ACS/ATS 设置以及 GPUDirect/RDMA 调优，并强调避免嵌套虚拟化，以便运营商可以在 L1 运行虚拟机即服务模式，并在各层之间实现一致的证明。简而言之，“我们希望将所有内容上游化，以便人们可以将其作为参考架构进行复制。”Kaiser 说道。

## 开源协作和上游化工作

这一切听起来很棒，但 Kaiser 谨慎地指出了权衡。将 Kata 与机密计算结合并非万能药。虚拟机突破仍然是理论上的风险；机密虚拟机降低了提供商检查内存的能力，但并未消除所有攻击面。尽管如此，这种组合方法大大减少了云运营商或共同租户访问敏感模型工件或训练数据的机会。

尽管如此，一旦发布并可用，NVIDIA 规模化运行敏感 AI 工作负载的方法几乎肯定会催生新的 AI 堆栈，它结合了轻量级虚拟机隔离 ([Kata](https://thenewstack.io/kata-containers-demo-a-container-experience-with-vm-security/))、硬件内存加密和证明（机密计算）以及 GPU 设备映射抽象（CDI + GPU Operator），并通过精心处理 PCIe 拓扑和 IOMMU 约束来保持安全性和性能。