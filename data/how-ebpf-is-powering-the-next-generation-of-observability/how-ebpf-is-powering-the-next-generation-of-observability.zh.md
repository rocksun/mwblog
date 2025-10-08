如果说数字化转型定义了2010年代，那么2020年代则完全是关于数字化优化。云原生应用的爆发导致了复杂性不断增加和云成本的螺旋式上升。组织正感受到压力——从不断膨胀的[可观测性](https://grafana.com/oss/beyla-ebpf/)账单到管理分散在众多监控工具中的遥测数据所面临的挑战。

[可观测性](https://grafana.com/oss/beyla-ebpf/)应该是现代基础设施的内置能力，而不是一个附加的成本中心。这正是 [Beyla](https://grafana.com/oss/beyla-ebpf/) 发挥作用的地方。Beyla 是一个基于 eBPF 的自动插桩代理，无需更改任何应用程序代码即可捕获 traces 和 metrics。但随着业界对基于 eBPF 的[可观测性](https://grafana.com/oss/beyla-ebpf/)的兴趣日益增长，很明显，这项创新需要在一个比单一供应商更广阔的平台发展。

为了确保基于 eBPF 的自动插桩能够造福整个生态系统，Beyla 被贡献给了 OpenTelemetry 项目。现在，该项目被称为 [OBI (OpenTelemetry eBPF-based Instrumentation)](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation)，它继续与社区合作发展，推动我们共同的目标：使高质量的遥测数据能够被每个平台团队访问，无论其技术栈或工具如何。

这一转变正在帮助重新定义[可观测性](https://grafana.com/oss/beyla-ebpf/)如何融入开发人员工作流程和平台工程策略。

## **eBPF：弥合开发者与平台之间的鸿沟**

平台工程的兴起是为了应对开发者日益增长的负担。尽管开发者希望交付功能，但底层基础设施变得比以往任何时候都更加复杂，尤其是在分布式系统中。平台团队旨在通过提供铺好的路径和可重用的模板来驯服这种复杂性，从而强制执行一致性、安全性和可靠性。

但[可观测性](https://grafana.com/oss/beyla-ebpf/)却常常成为一个症结。开发者不得不手动为其服务进行插桩，处理跨语言的不一致库，并在可见性和开销之间进行权衡。这正是 eBPF——以及现在的 OBI——发挥作用的地方。

有了 OBI，[可观测性](https://grafana.com/oss/beyla-ebpf/)的负担从应用程序团队转移到了平台团队。eBPF 在内核和用户空间层面工作，无需访问源代码即可收集遥测数据。它在协议层进行观察，这意味着无论你的服务是用 Rust、Go 还是 Java 编写，你都能获得一致、高保真度的数据。

## **打破语言障碍**

传统的 APM 工具通常依赖于特定语言的代理和运行时钩子，这在现代环境中表现不佳，特别是在处理编译型语言或高度优化的微服务时。这些方法通常无法将传入和传出的请求关联起来，导致 traces 碎片化或不完整。

OBI 基于 eBPF 构建，通过在协议层面收集信号来规避这些限制。eBPF 不依赖于运行时反射或代码注入，而是使用探针（如 uprobes 和 kprobes）附加到系统级事件和用户空间函数。这使得它能够观察请求流、跟踪线程模型，并理解服务何时以及如何进行通信，而与应用程序的内部逻辑无关。

这在不需要开发人员更改代码、链接额外库或管理插桩开销的情况下，生成了端到端 traces。随着 OBI 的引入，这种方法还解锁了一个强大的新信号：持续画像。

## **第四个信号**

现代[可观测性](https://grafana.com/oss/beyla-ebpf/)通常分为三个信号：metrics、logs 和 traces。每个都有其优点和缺点。

Metrics 成本低，但不够详细。Logs 非常详细，但成本高昂。Traces 对于理解分布式架构的行为至关重要，但难以插桩且存储成本高昂。而对于 logs 和 traces，长期分析变得非常昂贵。

但随着 eBPF 的出现，画像正日益重新成为第四个信号。因为许多用于 eBPF tracing 和 metrics 的相同技术也可以用于捕获 CPU 和 off-CPU 画像，eBPF 是构建画像工具的绝佳工具。画像在早期的单体系统中是一种基础工具，常用于性能调优和调试。随着系统转向分布式架构，持续画像变得更难实现，直到 eBPF 使其重新变得可行。

现在，APM 供应商能够使用分布式 traces 来创建这些持续画像，为平台团队提供优化云环境和更好地应对操作问题所需的信息。结果如何？更好的决策、更快的事件解决和更清晰的优化机会。例如，当服务开始消耗过多内存时，你不仅会看到峰值；你会确切地了解是哪个函数或线程导致了它，以及它是否与最近的部署有关。

## **混合架构，统一[可观测性](https://grafana.com/oss/beyla-ebpf/)**

老实说，大多数应用程序环境既不是完全基于微服务，也不是纯粹的单体。它们介于两者之间。这就是为什么最有效的[可观测性](https://grafana.com/oss/beyla-ebpf/)策略将分布式 tracing 与持续画像相结合，解锁了广度和深度。

想象一下，点击 trace 中一个缓慢的 span，并立即看到相应的 CPU 画像：无需猜测，无需上下文切换。有了 OBI，组织能够摆脱插桩的痛苦，进入一个[可观测性](https://grafana.com/oss/beyla-ebpf/)自动化、集成化和可操作化的新时代。

随着 OBI 加入 OpenTelemetry，它有望成为平台团队为开发者提供[可观测性](https://grafana.com/oss/beyla-ebpf/)的行业标准：语言无关、零插桩且为规模化而构建。数字化优化的承诺始于可见性。有了 OBI，这种可见性终于触手可及。

*KubeCon + CloudNativeCon North America 2025 将于 11 月 10 日至 13 日在佐治亚州亚特兰大举行。* [*立即注册*](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/)*。*