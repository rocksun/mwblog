
<!--
title: 国政府力推WebAssembly，而不是eBPF？
cover: https://cdn.thenewstack.io/media/2025/02/b7d02bd1-getty-images-mn20kmlxr9a-unsplash-1.jpg
-->

根据联邦政府的说法，WebAssembly 可以而且应该集成到整个云原生服务网格领域，以增强安全性。

> 译自 [The Feds Push for WebAssembly Security Over eBPF](https://thenewstack.io/the-feds-push-for-webassembly-security-over-ebpf/)，作者 B Cameron Gain。

使用 [WebAssembly](https://thenewstack.io/webassembly/) 可能会成为强制性要求，以满足安全合规性要求，同时解决其他持续存在的安全难题，因为 [Wasm](https://thenewstack.io/what-makes-wasm-different/) 得到更广泛的应用。

根据[美国国家标准与技术研究院 (NIST)](https://thenewstack.io/nist-secures-encryption-for-a-time-after-classical-computing/) 的一篇论文《[云原生应用的数据保护方法](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8505.pdf)》（作者：[Wesley Hales](https://www.linkedin.com/in/wesleyhales) 来自 [LeakSignal](https://www.leaksignal.com/)；[Ramaswamy Chandramouli](https://www.linkedin.com/in/ramaswamy-chandramouli-64b8446)，NIST 的一名主管计算机科学家）的观点，WebAssembly 可以并且应该集成到整个云原生服务网格领域，特别是为了增强安全性。该论文中概述的框架可能会导致未来对 WebAssembly 或云原生环境的合规性要求，同时也为更广泛地使用 WebAssembly 来实现安全性奠定基础。

该论文强调了 WebAssembly 模块及其原位或代理方法如何使 WebAssembly 成为数据在服务之间传输时进行数据分类的有力候选者。借助 Wasm，可以对跨一个或多个云原生环境分布的任何类型的数据进行数据检查。

“很多人都有 [eBPF](https://thenewstack.io/what-is-ebpf/) 这把锤子，并且认为一切都像钉子一样——但事实并非如此，”该报告的合著者 Hales 告诉 The New Stack。“eBPF 专为一件事而设计。”

eBPF 最初是为防御侧信道攻击而设计的，例如 Heartbleed 漏洞（该漏洞危及了 OpenSSL 加密库）和其他内核级别的相关漏洞。Hale 解释说，eBPF 允许你在发现漏洞后立即对其进行修补并阻止该活动。

“人们正在将它用于所有事情，因为它是一个简单的插入点。这是 eBPF 的优势之一——它易于安装并提供一定程度的可见性。但是，它无法访问第 7 层人类可读的文本，因为它在内核空间中运行，”Hale 说。

将来自第 4 层 eBPF 的数据包引入用户空间进行分析需要先镜像这些数据包，然后在容器中进行分析。“这创建了一个类似弗兰肯斯坦的过程，根本没有性能，”Hales 说。“Wasm 真正实现了我们正在做的事情的目的。我们实际上对 eBPF 进行了原型设计，但它根本不适合我们。”

## eBPF vs. Wasm

在比较 eBPF 安全性和 Wasm 安全性时，该论文的作者写道：

“与 eBPF 等技术相比，使用 Wasm 解析第 4-7 层中的人类可读文本具有多个优势，尤其是在处理复杂的应用层数据（如 HTTP）时。虽然 eBPF 在内核中直接进行数据捕获和操作非常强大，但将其用于解析详细的 HTTP 流量可能很复杂，并且对于某些应用程序来说可能过于繁琐。这种复杂性源于需要在内核中处理 HTTP 的复杂性——如果管理不当，这项任务可能会限制性能并引入安全问题。此外，eBPF 施加了许多限制，并且需要额外的精力来进行数据处理和通用计算。

“Wasm 提供了一个安全的沙盒环境，适合在多个平台上高效执行代码和解析应用层协议。Wasm 可以在用户空间和服务器环境中使用，从而可以更轻松地与现有的解析库和工具集成，降低复杂性，并可能提高解析操作的可靠性。它的可移植性以及嵌入各种运行时环境的能力使其成为网络流量分析任务的实用选择，包括那些涉及处理人类可读文本的协议的任务。”

在云原生世界中，所有数据流量都被迫通过 [服务网格](https://thenewstack.io/service-mesh/) [Istio](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/) 的代理和 Wasm，这归功于其模块化或“沙盒化”设计。“你可能有 10,000 个容器位于 Istio 代理后面，而所有日志流量、所有 Web 流量，甚至数据库流量都必须进入代理，然后到达目的地，”Hales 说。“因此，我们可以使用 Wasm 查看所有这些流量。”

## 大局

从这篇论文中可以得出的一个结论是，WebAssembly 的安全性并不优于 eBPF。它所要表达的是，并且需要重申的是，当退一步来看时——无论是在可观测性、安全性、全面的解决方案或策略，还是最佳实践方面——都不应该用一个来代替另一个。因此，例如，美国政府不太可能突然强制使用 WebAssembly，而不为某些用例实施或强制使用 eBPF。在商业领域，一个全面的安全或可观测性参与者或产品应该包括 eBPF 用于其一系列用例，而 WebAssembly 用于其他用例。

“[Ben Hirschberg](https://il.linkedin.com/in/ben-hirschberg-66141890)，” ARMO 的 CTO 兼联合创始人说：“eBPF 从来就不是一个通用的计算平台，它既有算法上的限制，也有内存上的限制。从安全的角度来看，将功能推送到内核（eBPF 所在的位置）也是一种不好的做法，因为它可以像 Wasm 一样在用户空间中完成。因此，在 WASM 中实现复杂的可观测性逻辑，而在 eBPF 中保留所需的最少功能更有意义。”

事实上，WebAssembly 从一开始就被设计为所谓的沙盒安全。“最广泛使用的沙盒应用程序环境是我保证你现在正在运行的环境：一个 Web 浏览器。浏览器是一个从根本上构建为运行不受信任代码的环境。WebAssembly 基于浏览器的传统是其一流沙盒技术的原因，” Fermyon 联合创始人兼 CEO [Matt Butcher](https://www.linkedin.com/in/mattbutcher) 说。“与容器和 eBPF 不同，安全性不是事后才考虑的；它是从开始到现在的核心功能。我对 Wasm 在安全敏感环境中的普及并不感到惊讶。”

Hales 解释说，除了 Istio 的代理之外，Wasm 提供的覆盖范围比 eBPF 更广泛，涵盖通过 HTTP、gRPC 或 [GraphQL](https://thenewstack.io/graphql-federation-the-missing-api-for-your-platform-strategy/) 的数据传输，或者网络流量到达的任何地方。“这无关紧要，因为它们仍然都通过第 7 层到第 4 层的管道传输，”Hales 说。

“可以将 Wasm 视为一种灵活的核心技术，具有定义明确的扩展方法，这很有用。它是平台中立的，这意味着它可以运行在许多操作系统和系统架构上。而且它现在几乎受到所有主要编程语言的支持，”Butcher 说。“从本质上讲，这使得 Wasm 比 eBPF 更具适应性。简而言之：Wasm 的构建是为了通用目的，而 eBPF 则不是。”
