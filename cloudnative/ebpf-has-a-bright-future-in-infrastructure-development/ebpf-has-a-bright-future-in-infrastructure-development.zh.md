[思科](http://cisco.com/?utm_content=inline+mention)杰出软件工程师 [Daniel Borkmann](http://borkmann.ch/) 在 [Linux 开源峰会](https://ossna2025.sched.com/)上发表主题[演讲](https://ossna2025.sched.com/event/23B1m/keynote-ebpf-unlocking-innovation-in-the-linux-kernel-daniel-borkmann-distinguished-software-engineer-isovalent-at-cisco-and-co-creator-of-ebpf-and-cilium)，介绍了这项他帮助创建的技术的现状，并预测了它在未来的应用。他预测，未来十年，eBPF 将成为“基础设施开发者的战略平台选择”。

Borkmann 认为，eBPF 具有革命性意义，因为它缩短了将新技术引入内核的开发周期。到目前为止，向 Linux 内核添加某种扩展需要数年时间，而且成功的保证很少。现在，eBPF 允许用户[添加自己的内核技术](https://thenewstack.io/how-ebpf-turns-linux-into-a-programmable-kernel/)。

“我们正在从一个漫长的创新周期转向一个短的创新周期，”Borkmann 说，他也是一位拥有 15 年经验的 Linux 核心提交者。越来越多的基础设施工具提供商正在利用这种内核技术。

eBPF 擅长跨堆栈微调性能，从网络到 CPU 本身，从而提供更好的用户体验。它也擅长实施策略。

Meta 的 Facebook 在其 Layer 4 负载均衡器中广泛使用 eBPF，其中 100 个不同的 eBPF 应用程序执行各种任务。它用于所有 Android 手机的安全策略和流量控制，以及桥接到 IPv6 网络。

## eBPF 用于虚拟机

在网络领域，基于 eBPF 的 [Netkit](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/net/netkit.c) 驱动程序已[被证明很受欢迎](https://thenewstack.io/bytedance-to-network-a-million-containers-with-netkit/)，用于识别内核本身的命名空间，这以前是速度慢得多的网络驱动程序的任务。

Borkmann 说，这项工作实际上始于 Kubernetes 社区，作为一种最大限度地减少容器通信延迟的方法。Borkmann 参与了 [Cilium 项目](https://thenewstack.io/supercharge-service-mesh-with-ebpf-and-cilium/)，这是一个基于 eBPF 构建的网络数据包处理器。

“一旦我们将其部署到 Linux 内核中，超大规模企业也对此产生了兴趣，并将此推广到他们的整个集群中，”Borkmann 说。例如，Meta 使用 Netkit 将其命名空间解析的 [P99 延迟](https://thenewstack.io/p99conf-how-ebpf-could-make-faster-database-systems/) 从 12 秒缩短到 100 毫秒。

下一步是将 eBPF 带入 [虚拟机](https://thenewstack.io/vmware-vcf-9-0-finally-unifies-container-and-vm-management/) 的世界。

许多组织现在有两个平台，一个基于 Kubernetes，另一个基于旧的传统虚拟机 (VM)。每个平台都有自己的监控、指标和日志记录。

Borkmann 说，eBPF 可以帮助整合这两个世界。目前，正在进行将 NetKit 集成到 [KubeVirt](https://kubevirt.io/) 中的工作，KubeVirt 允许用户将虚拟机作为 Kubernetes pod 进行管理。

[![](https://cdn.thenewstack.io/media/2025/07/d60a6997-oss-ebpf-slide-01.png)](https://cdn.thenewstack.io/media/2025/07/d60a6997-oss-ebpf-slide-01.png)

Netkit 可以优化整个网络。

## eBPF 用于内核

Borkmann 说，你可以将 eBPF 视为一种“通用汇编语言”，尽管大多数开发人员永远不会看到它，而是选择他们选择的编程语言的接口。

两个主要的即时编译器（LLVM 和 GCC）支持各种前端语言（C、Rust 等），它们将其转换为 eBPF 字节码。指令集已由 IETF 工作组[标准化](https://datatracker.ietf.org/group/bpf/about/)（允许使用 [Windows 版 eBPF](https://thenewstack.io/ebpf-is-coming-for-windows/)）。有一个验证器来确保用户代码不会破坏系统的稳定性。

eBPF 的另一个用例是优化内核本身。

进程调度是另一个新兴的用例，它受益于一个新的 Linux 内核实用程序 [sched-ext](https://github.com/sched-ext/scx/)，它[支持](https://thenewstack.io/bpf-opens-a-door-to-linux-dynamic-scheduling-maybe-with-rust/)创建基于 eBPF 的内核线程调度程序。

Meta 和 Google 等超大规模企业已经在使用基于 eBPF 的调度程序。精细的调度策略已将这些公司的工作负载优化了 10% 左右。

SteamOS 也使用 eBPF 调度方法来优化游戏。

eBPF 可以帮助进行 AI 工作负载平衡：AI 堆栈的哪个部分正在消耗资源？基于 eBPF 的火焰图将显示完整的调用图。条形图越长，消耗的周期就越多。

最后，Borkmann 建议 eBPF 可以为内核的实时补丁奠定基础，在这种情况下，它将为正在应用的补丁提供安全检查。

[![](https://cdn.thenewstack.io/media/2025/07/95ddf2d6-oss-ebpf-slide-02.png)](https://cdn.thenewstack.io/media/2025/07/95ddf2d6-oss-ebpf-slide-02.png)

*披露：Linux 基金会支付了记者参加开源峰会的差旅费。*