
<!--
title: eBPF如何塑造Linux和平台工程的未来
cover: ./cover.png
-->

eBPF 允许用户在 Linux 内核中加载和安全运行自定义程序，而无需直接更改内核本身。可能性是无限的。

> 译自 [How eBPF is shaping the future of Linux and platform engineering](https://www.infoworld.com/article/3715503/how-ebpf-is-shaping-the-future-of-linux-and-platform-engineering.html)，作者 Travis Van。


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

Borkmann 在网络堆栈中开发内核的工作让他站在满足 SDN 和云原生网络需求的前线。Linux 需要更新的抽象，因为其许多构建块在十多年前就已经设计好了——cgroup（CPU、内存处理）、命名空间（网络、挂载、pid）、SELinux、secomp、Netfilter、Netlink、AppArmor、Auditd、Perf 等。Borkmann 看到 netfilter 的 nftables 等技术被推为“下一代”Linux 网络，以及 Open vSwitch（OVS），它当时是最先进的 SDN 项目。他认为有更好的方法。

Linux 内核正在不断扩展以跟上更高的网络速度，但没有提供足够的灵活性来编程新的自定义功能。另一个限制是“绝不破坏用户空间”。也就是说，Linux 内核必须继续支持所有在云原生应用程序出现之前很久就开发的软件。不幸的是，这些“遗留包袱”将一些网络创新从内核移动到了用户空间。

总之，新的云操作模式为我们带来了更多的自动化、提取转换加载 (ETL) 和规模，以及更严苛的网络性能要求。然而，Linux 内核中的自包含子系统并未对将所有这些新的云上下文中送入内核、聚合这些内容以及对其进行操作达成公约。

在 Linux 编程中，数据包处理（解析、操作、过滤和转发）是“可能实现的功能”的一个基础关注点。这是内核开发人员对通过堆栈传输的网络数据包进行路由、控制和检查的机制。数据包处理对于内核的网络堆栈，就如同化油器对于发动机，通量电容对于 Doc 的狄罗伦一样。

应用程序开发者大多数都在用户空间内编写其应用程序，使用保护他们免受需对内核进行的系统调用的抽象。因此，当应用程序需要与硬件进行接口（写入屏幕、写入文件、发送网络数据包）时，它必须请求内核提供帮助。用户空间无法直接执行此操作（出于多种原因，例如系统安全性）。内核提供用户空间应用程序和硬件之间的通用且泛用的接口，并协调同时运行的多个用户空间进程。

从虚拟化到容器的演进过程中，许多不同的数据包筛选方法竞争在 Linux 内核中占有一席之地：iptables、nftables、OVS、Linux 流量控制 (TC) 等。eBPF 最终胜出成为首选方法，因为它将表达能力与验证器的安全性相结合（同时以本机性能执行程序）。换句话说，eBPF 允许用户以这些备选方案无法实现且不会导致内核崩溃的方式对内核进行编程。



## 一个更为“可编程”的 Linux 内核

开始时，Borkmann 被 eBPF 的灵活性及其给网络带来的性能所吸引，但很明显，这项新技术的好处远远超出了网络领域。

“一旦 eBPF 实现了此项基础功能，让你能够构建内容并立即部署，它便解决了一个大问题，”Borkmann 说。“你可以编写嵌入 eBPF 的编排计划，并将其部署到任何底层内核版本。你无需再为核心内核 ABI 稳定性向大型供应商支付巨额费用，现在只需使用 eBPF 即可，而不必再使用模块来针对大量不同的用例扩展内核。”

eBPF 转变为一种通用汇编语言，该语言允许用户在 Linux 内核中加载和安全运行自定义程序，这是一种在运行时向操作系统中添加各种功能的方法。它具有严格的类型，具有稳定的指令集，并且其扩展具有后向兼容性。

Borkmann 解释道：“你可以将其视为一种新型的软件，能够弥合典型的单内核与微内核之间的差距”。“它是你受信任的用户空间中内核的安全扩展。关于 eBPF 很重要的一个方面是，它与常规内核代码一样快，这是由于 eBPF 不是沙箱，并且验证程序可以完全理解该程序以确定它是否可以在受信任的环境中安全运行，然后再 JITed [即时编译] 为本机代码。”

eBPF 不仅安全且快速，还可以在本机速度下运行。它极其灵活，允许不同用户以不同方式使用它。“eBPF 的强大之处在于你可以仅当你作为用户有该用例或需要以某种方式处理某些内容时启用代码，”Borkmann 说。“这不会惩罚他人。它不像以硬编码方式编入内核的东西，这将使关键路径越来越慢——性能死亡是一千次的削减。”


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