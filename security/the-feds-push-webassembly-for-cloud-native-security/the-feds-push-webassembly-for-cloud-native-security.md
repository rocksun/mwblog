
<!--
title: 联邦政府推动WebAssembly提升云原生安全
cover: https://cdn.thenewstack.io/media/2024/12/aa7a059d-planet-volumes-92k84okjqrw-unsplash-1.jpg
-->

美国政府表示，WebAssembly尤其应该并且能够集成到云原生服务网格领域，以增强安全性。

> 译自 [The Feds Push WebAssembly for Cloud Native Security](https://thenewstack.io/the-feds-push-webassembly-for-cloud-native-security/)，作者 B Cameron Gain; Alex Williams。

随着 [Wasm](https://thenewstack.io/what-makes-wasm-different/) 的广泛采用，使用 [WebAssembly](https://thenewstack.io/webassembly/) 可能会成为满足安全合规性要求并解决其他持续存在的安全难题的强制性要求。

根据美国 [国家标准与技术研究院 (NIST)](https://thenewstack.io/nist-secures-encryption-for-a-time-after-classical-computing/) 今年早些时候发布的一篇论文 [“云原生应用程序的数据保护方法”](https://doi.org/10.6028/NIST.IR.8505.ipd) ，WebAssembly 尤其应该集成到云原生服务网格领域以增强安全性。该论文中概述的框架可能会导致未来对 WebAssembly 或云原生环境的合规性要求，同时为更广泛地使用 WebAssembly 进行安全奠定基础。

该论文全面概述了如何在现代云原生应用程序架构中利用 Wasm 进行数据保护，同时批判性地审查了其安全隐患和未来发展领域。

该论文强调了 WebAssembly 模块及其就地或代理方法如何使 WebAssembly 成为数据在服务之间传输时进行数据分类的有力候选者。使用 Wasm，可以提供跨任何类型数据（分布在一个或多个云原生环境中）的数据检查。

随着 SaaS 解决方案的出现以及需要更安全地通过这些管道传输更多数据，对 Wasm 代理范围和扩展功能的需求变得尤为明显。“过去 10 年发生的 SaaS 事件，许多产品将数据从客户的云环境发送到 SaaS 环境：这与网络安全并不太相符，并增加了摩擦，”来自 [LeakSignal](https://www.leaksignal.com/) 的  告诉 The New Stack。“与 NIST 的主管计算机科学家 共同撰写了这篇论文。”“你从需要获得所需内容的非常充满摩擦的安装转变为理解网络流量。Wasm 的作用是绕过所有这些，因为它今天在许多环境中都在 Envoy 代理内部运行。”

在云原生世界中，所有数据流量都强制通过 [服务网格](https://thenewstack.io/service-mesh/) [Istio](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/) 的代理和 Wasm，其模块化或“沙箱”设计。“你可能有 10,000 个容器位于 Istio 代理后面，而所有日志流量、所有 Web 流量，甚至数据库流量都必须进入代理，然后才能到达目的地，”  说。“所以我们可以用 Wasm 查看所有这些。”

除了 Istio 的代理之外，Wasm 的覆盖范围比 [eBPF](https://thenewstack.io/ebpf-is-coming-for-windows/) 更广泛，涵盖通过 HTTP、gRPC 或 [GraphQL](https://thenewstack.io/graphql-federation-the-missing-api-for-your-platform-strategy/) 的数据传输，或者网络流量流向何处，  说。“这没关系，因为它们仍然都通过第七层到第四层的管道传输，”  说。

NIST 论文的分析与 [Fermyon](https://www.fermyon.com/?utm_content=inline+mention) 使用的开源 SpinKube 安全功能相关。“WebAssembly 在安全性和可移植性方面的双重关注是独一无二的，”Fermyon 联合创始人兼首席执行官  告诉 The New Stack。“虽然这种设计对于浏览器环境是必要的，但这正是 WebAssembly 如此适合 NIST 概述的案例的原因。”

## 大政府

NIST 论文主要发布的是基于既定科学方法的信息。虽然它不是美国联邦政府 [关于改进国家网络安全的行政命令](https://www.gsa.gov/technology/it-contract-vehicles-and-purchasing-programs/information-technology-category/it-security/executive-order-14028) 的一部分，但该论文的发现对社区具有重大影响。本文中描述的 WebAssembly 的安全优势可能会被纳入强制性合规性要求，为什么不呢，将来有一天可能会被纳入美国政府的行政命令。例如，[Google](https://cloud.google.com/?utm_content=inline+mention) 和 Microsoft 已经在为未公开的项目研究论文中描述的协议。
Butcher表示：“NIST在硬科学领域，包括计算机科学领域，拥有悠久的研发历史。由于他们的科学是‘实践性的’（例如原子钟），我认为他们的观点既尊重理论也尊重实践。”

本文揭示的关键发现包括（除了对WebAssembly的历史、结构和其他背景信息的深入分析）：

Wasm模块为数据保护提供了几个优势，包括：

- 无需修改核心代码即可扩展代理。
- 通过沙箱实现安全性和隔离性。
- 跨不同平台的可移植性。
- 与传统的代理扩展相比，具有更好的性能潜力。

可在Wasm模块中实现的关键数据保护技术包括：

- 动态数据屏蔽
- 用户和实体行为分析
- 数据丢失防护

Wasm模块可用于保护各种场景中的数据，包括：

- 网络流量
- API安全
- 微分段
- 日志流量
- 大型语言模型 (LLM) 交互
- 信用卡交易

本文提供了Wasm执行环境的详细安全分析，涵盖以下方面：

- 内存模型和安全性
- 控制流完整性
- 防范侧信道和注入攻击

Wasm安全模型旨在保护用户免受有缺陷/恶意模块的侵害，同时为开发人员提供构建安全应用程序的有用基元。

尽管Wasm提供了许多安全优势，但仍然存在一些漏洞，例如代码重用攻击和竞争条件的可能性。

本文强调需要持续改进Wasm模块中的数据保护技术，以应对日益复杂的攻击。

Wasm模块可以为监控工具提供遥测数据，从而实现对敏感数据流的可视化。

TechTarget’s Enterprise Strategy Group的分析师指出，本文重点介绍了Wasm从浏览器环境向服务器端应用程序的转变，尤其是在云原生和微服务架构中。

## 大科学
作者指出，WebAssembly的修复与这类新的代理内应用程序相一致，以实现这些目标。本文还重点介绍了WebAssembly的一些众所周知的安全属性。大型云提供商尤其正在探索这种基于代理的方法，以利用WebAssembly提高安全性。虽然一些实现遇到了延迟增加的问题，但随着开源生态系统中标准的制定，正在努力解决这些问题。这些努力涉及云提供商、无服务器提供商和WebAssembly供应商（例如Fermyon和Cosmonic）之间的合作。

Butcher表示：“由于Wasm体积小且可移植性高，它可能成为无服务器应用程序的理想‘安全卫士’。如果他们能够解决性能开销问题，这可能会对应用程序级安全性产生重大影响。”

本文的作者还描述了WebAssembly模块如何通过其范围提供[可观察性](https://thenewstack.io/observability/)数据，从内核向外扩展。这种可观察性对于监控敏感数据流尤其宝贵。但是，正如作者警告的那样，这种方法必须不断发展以应对日益复杂和复杂的攻击。

Butcher表示：“以前，遥测是一个附加组件，是应用程序开发人员和运维团队之间的协商点。这方面的工具最近激增。WebAssembly的字节码格式与当今的工具完美契合，使其成为最易于使用的现代环境。”

目前，WebAssembly似乎是减轻云原生环境臭名昭著的安全缺陷的有力候选者。Wasm在许多领域都具有显著的颠覆性潜力，其中安全就是一个领域。Volk表示：“这项技术所需要的是大型生产部署，由知名厂商向世界展示，包括风险投资公司，证明其承诺是真实的。我绝对可以看到基于Wasm的‘安全代理’巡逻[Kubernetes](https://thenewstack.io/kubernetes/)集群以阻止坏人。”
