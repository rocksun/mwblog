当 [Docker 在 2013 年横空出世](https://www.infoworld.com/article/3639596/docker-really-did-change-the-world.html) 时，[Linux 容器](https://www.infoworld.com/article/3204171/what-is-docker-the-spark-for-the-container-revolution.html) 似乎一夜之间就取得了成功。但容器（以及微服务和 [Kubernetes](https://kubernetes.io/blog/2018/07/20/the-history-of-kubernetes-the-community-behind-it/)）的演变实际上是几十年来的积累，其基础是 Linux 操作系统中的内核原语。Docker 使用这些原语，即 cgroups 和 namespaces，作为构建块来创建轻量级、易于使用的软件打包格式。Linux 容器多年来一直被 Google 和其他 [行家？] 使用，但 Docker 使其易于被主流开发人员访问。

而这正是我们今天在 [eBPF](https://ebpf.io/) 周围看到的情况——另一项源自 Linux 内核原语的技术。如今，每个主要的网络、可观察性和安全供应商都在宣称提供“基于 eBPF 的”产品。像 Cilium、Tetragon 和 Falco 这样的 eBPF 工具正在企业架构和云服务提供商产品中扎根。据其创造者之一说，这仅仅是基于 eBPF 的突破的开始。

InfoWorld 与 Daniel Borkmann 进行了交谈——eBPF 的共同创造者，也是 Linux 内核当前的 eBPF 共同维护者——以了解更多关于该技术起源的信息，为什么 eBPF 已成为编程和定制 Linux 内核的标准方法，以及这对 Linux 和 [平台工程](https://www.infoworld.com/article/3691820/what-is-platform-engineering-evolving-devops.html) 的未来意味着什么。

## 从 Solaris 学生到 Linux 内核维护者
Daniel Borkmann 走向 eBPF 的道路始于对理解 Solaris 内部机制的追求，Solaris 当时仍在大学的计算机科学课程中教授。然而，一个主要障碍是缺乏源代码来查看“魔法发生的地方”。Borkmann 发现操作系统课程中的理论非常有趣，但真正让他醍醐灌顶的是他深夜研究 Linux 内核源代码、Git 日志和邮件列表。他开始编写与内核交互的低级用户应用程序。

很快，Borkmann 开始探索数据包过滤器、[tcpdump 和 libpcap](https://www.tcpdump.org/)，以及数据包在进出时遍历不同层时网络堆栈的工作原理。他在业余时间编写了一个更高效的 tcpdump 克隆，并开始向 Linux 网络堆栈发送一些代码改进。在他硕士学习开始时，他最终获得了第一份在德国莱比锡的一家当地初创公司开发 Linux 内核代码的付费工作。

Borkmann 在 2010 年提交了他的第一个补丁到 Linux 内核，当时他还是一个“完全的新手”（他的原话），目的是扩展 netpoll 以允许每个接口执行多个 rx_hooks，并且意外地引入了一个错误，该错误会导致内核死锁，该错误很快被另一位贡献者发现并修复。但他被迷住了。Linux 内核开发是一个迷人的环境，他知道这是他的使命。

Borkmann 搬到苏黎世，完成关于为内核开发可组合网络堆栈的硕士论文。从 FreeBSD 的 netgraph 中汲取灵感，他的实验是尝试将网络块卸载到 FPGA 上，并为数据包处理构建可组合的图。但在此过程中，他有时发现学术论文过于枯燥，缺乏长期的现实世界影响，并意识到全职为 Linux 内核做出贡献会更有意义。他发现了一位名叫 Thomas Graf 的 Linux 贡献者（最终他们都成为了 Cilium 的共同创造者），他的电子邮件有一个瑞士域名（.ch），自发地联系了他——并被邀请加入 Red Hat 的 Linux 内核网络团队。

现在，Borkmann 是全球 Linux 内核贡献者中排名前 1% 的人之一。

## 重新思考 Linux 操作系统中的网络
eBPF 背后的起源故事实际上始于 2011 年，当时软件定义网络 (SDN) 正在兴起，Linux 的采用率正在飙升。Linux 子系统需要跟上微服务架构和分布式应用程序的新范式，这些应用程序运行在 Linux 机器集群中，而不是单个服务器和主机操作系统上。
Borkmann's work on network stack kernel development has put him at the forefront of meeting the demands of SDN and cloud-native networking. Linux needs updated abstractions because many of its building blocks were designed over a decade ago—cgroups (CPU, memory handling), namespaces (network, mount, pid), SELinux, seccomp, Netfilter, Netlink, AppArmor, Auditd, Perf, etc. Borkmann saw technologies like netfilter's nftables being touted as the "next generation" of Linux networking, along with Open vSwitch (OVS), which was the state-of-the-art SDN project at the time. He believed there was a better way.

The Linux kernel has been stretched to keep up with higher network speeds, but it doesn't offer enough flexibility for programming new custom functionality. Another limitation is the "never break userspace" rule. That is, the Linux kernel must continue to support all software developed before the advent of cloud-native applications. Unfortunately, this "legacy burden" has shifted some networking innovation from the kernel to userspace.

In short, the new cloud operating system model brings more automation, updates, and scale, along with more demanding network performance requirements. But the self-contained subsystems within the Linux kernel have no conventions for driving, aggregating, and processing all of these new cloud contexts within the kernel.

In Linux programming, packet processing—parsing, manipulating, filtering, and forwarding—is a foundational question of "what is possible." It's the mechanism by which kernel developers route, control, and inspect network packets as they travel through the stack. Packet processing is to the kernel's network stack what the carburetor is to an engine, what the time machine is to Doc's DeLorean.

Application developers primarily write their applications in userspace, using abstractions to shield them from the system calls that would be required to interact with the kernel. So, when an application needs to interact with hardware—write to the screen, write to a file, send a network packet—it must ask the kernel for help. Userspace cannot do this directly (for a variety of reasons, such as system security). The kernel provides a common, generic interface between userspace applications and hardware, and it coordinates multiple userspace processes running concurrently.

In the evolution from virtualization to containers, many different packet filtering methods vied for a place within the Linux kernel: iptables, nftables, OVS, Linux Traffic Control (TC), and so on. eBPF emerged as the preferred method due to its expressiveness and the security provided by its verifier (native performance when executing programs). In other words, eBPF allows users to program the kernel in ways that these alternative methods cannot, and without the risk of crashing the kernel.

## A More "Programmable" Linux Kernel
While Borkmann was initially drawn to the networking flexibility and performance that eBPF brought, it became clear that the benefits of this new technology could extend far beyond networking.

"Once eBPF brought this foundational capability, you could build things and deploy them immediately, it solved a huge problem," Borkmann said. "You could write your orchestrator with eBPF embedded in it, and deploy it to any underlying kernel version. And, instead of paying a lot of money to large vendors for core kernel ABI stability, now you can just use eBPF directly, without modules, to extend the kernel to meet many different use cases."

eBPF has become a general-purpose assembly language that allows users to load and securely run *custom* programs within the Linux kernel—a way to add *all* types of functionality to the operating system at runtime. It has strict types, a stable instruction set, and its extensions are backward compatible.

"Think of eBPF as a new type of software that bridges the gap between a typical monolithic kernel and a microkernel," Borkmann explained. "It's a secure extension to the kernel from your trusted userspace. The beauty of eBPF is that it's as fast as regular kernel code because eBPF isn't sandboxed, but rather the program is fully understood by the verifier to determine if it can run securely in a trusted environment, and then it's JIT [just-in-time compiled] to native code."

eBPF is not only secure and fast, running at native speeds. It's also very flexible, allowing different users to use it in different ways. "The power of eBPF is that you can enable code from a user perspective only when you have a use case or need to handle something in a particular way," Borkmann said. "It doesn't penalize anyone else. It's not like something hardcoded into the kernel that makes the critical path slower and slower—performance degrades due to countless cuts."
“在 eBPF 出现之前，大多数用户使用企业 Linux 发行版，或者直接运行设备上安装的内核版本，”Cilium 的 Graf 说。“eBPF 从根本上改变了这一点，因为有了运行时的存在，任何想法都可以转化为 eBPF 程序，并在几天内而不是几年内在运行时加载。这意味着我们可以更好地重建一切。我们必须决定首先重建什么。”

## 内核工程走向主流

与 Google Borg 和其他诞生于超大规模企业的技术一样，eBPF 最初只被少数拥有内核开发技能的软件工程团队采用。并非所有开发人员都具备必要的低级 C 编程技能来进行内核工程和编写 eBPF 程序。

但如今，这少数专家正在编写影响数百万用户的程序。eBPF 驱动的程序是平台工程团队最令人兴奋的领域，这些团队负责网络、安全和可观察性，而许多使用这些程序的人不需要了解使它们成为可能的底层 eBPF 抽象。“把它想象成来自云原生的一场无声的平台革命，”正如 Borkmann 在最近关于 eBPF 的研讨会上的一次 [主题演讲](https://conferences.sigcomm.org/sigcomm/2023/files/workshop-ebpf/1-CloudNative.pdf) 中所指出的那样。

以下是广阔的 eBPF 领域中众多应用的概览：

[Cilium](https://cilium.io/) 最初是 [容器网络接口](https://www.cni.dev/docs/spec/) (CNI) 的基于 eBPF 的实现，用于提供容器工作负载之间的第 3 层和第 4 层连接，但后来发展成为大多数云服务提供商 Kubernetes 产品的实际网络层。除了其他功能外，Cilium 还为 Kubernetes Pod 之间以及到外部服务的流量实现分布式负载均衡，并且能够完全替换 kube-proxy，使用 eBPF 中的高效哈希表实现几乎无限的扩展。它还支持高级功能，如第 3 层到第 7 层策略执行、集成入口和出口网关、带宽管理、与 Envoy 结合的服务网格以及深度网络可见性。
[Tetragon](https://tetragon.io/) 是另一个 eBPF 程序，它提供安全可观察性和运行时强制执行。通过利用 eBPF 的低开销，Tetragon 允许平台团队将网络流和其他内核事件与 Kubernetes 对象（标签、Pod、命名空间）绑定，直至非常具体的进程及其相关的进程树。在 [XZ Utils](https://www.csoonline.com/article/2077692/dangerous-xz-utils-backdoor-was-the-result-of-years-long-supply-chain-compromise-effort.html) 等软件供应链安全漏洞出现后，Tetragon 是一个开源项目，旨在为平台团队提供更深入的方法来查找特定软件在其环境中的运行位置，并在内核级别采取特定的策略操作。
[Pixie](https://px.dev/) 是一款可观察性工具，它使用 eBPF “自动捕获遥测数据，无需手动检测”。它已成为下一代应用程序性能管理和监控供应商的热门构建块。在 Google 上简单搜索“可观察性 AND eBPF”就可以看出这项技术如何改变了 eBPF 性能带来的遥测数据丰富性。推断云原生系统的实时状态历来涉及堆积监控数据，这些数据必须在将来进行关联。将这种遥测数据收集更靠近内核，有望带来更高的一致性和更低的资源使用率。
[Katran](https://engineering.fb.com/open-source/open-sourcing-katran-a-scalable-network-load-balancer/) 是一个 C++ 库，它可以挑战专有第 3 层和第 4 层负载均衡器的现状，采用一种基于内核包处理的新方法。并非每个人都能创建 eBPF 程序，但 [正在创建的程序](https://ebpf.io/applications/#major-applications) 针对的是企业基础设施中相对停滞的领域，并且迫切需要现代化以满足云原生用例的需求。
“未来十年的基础设施软件将由能够使用 eBPF 以及利用 eBPF 创建适合更高层平台的抽象的平台工程师来定义，”Borkmann 说。“将云原生上下文推入内核是缺失的，而 eBPF 解决了这个问题。”

在本月我们庆祝 [Kubernetes 10 周年](https://kubernetes.io/blog/2024/06/06/10-years-of-kubernetes/)之际，我们仍然处于分布式应用程序、容器编排和平台工程的早期阶段。可能很少有人会直接在内核级别进行 eBPF 工程，但数百万用户将使用基于 eBPF 的程序。如果您在大型公共云提供商平台之一上运行 Kubernetes 上的工作负载，那么您很可能已经在使用它了。