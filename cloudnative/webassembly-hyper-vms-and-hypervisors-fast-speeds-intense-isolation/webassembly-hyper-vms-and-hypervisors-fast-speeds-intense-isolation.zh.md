[虚拟机监控器](https://thenewstack.io/4-reasons-devops-engineers-still-rely-on-hypervisors/) 通过基于硬件的隔离提供了强大的安全性。为了在虚拟机监控器环境中提供额外的隔离层，[Hyperlight](https://thenewstack.io/microsofts-hyperlight-webassembly-for-vms-is-open-source/)——一种轻量级的 [虚拟机管理器 (VMM)](https://thenewstack.io/microsoft-open-sources-openvmm-rust-powered-vm-monitor/)，旨在嵌入到应用程序中——可以在微型虚拟机中安全地执行不受信任的代码，且具有极低的延迟和最小的开销。为了进一步隔离和提高延迟，[WebAssembly](https://thenewstack.io/webassembly/) (Wasm) 二进制文件通过软件故障隔离 (SFI) 提供了强大的安全性。

在本文中，我们将探讨将 WebAssembly 与 Hyperlight 结合使用时会发生什么——这种模型不仅集成了 Wasm 沙箱，而且集成了虚拟机监控器沙箱，而是将两者一致地集成在一起，从而提供深度防御。[Danilo (Dan) Chiarlone](https://github.com/danbugs) 告诉我，Wasm 沙箱在虚拟机监控器沙箱内运行，以执行 Wasm 二进制文件。

[![](https://cdn.thenewstack.io/media/2025/06/6bcf3e01-screenshot-2025-06-30-at-5.14.56%E2%80%AFpm-1024x453.png)](https://cdn.thenewstack.io/media/2025/06/6bcf3e01-screenshot-2025-06-30-at-5.14.56%E2%80%AFpm-1024x453.png)

在三月份于伦敦举行的 [Cloud Native Rejekts](https://cloud-native.rejekts.io/) 大会上，Chiarlone 和 [Mikhail Krinkin](https://www.linkedin.com/in/mikhail-krinkin-57892a86/?locale=en_US)（他也是一名 Microsoft 工程师）在他们的演讲 [“Wasm, Envoy, and Hyperlight Walk Into a Pod: No Vulnerabilities Allowed,”](http://cfp.cloud-native.rejekts.io/cloud-native-rejekts-europe-london-2025/talk/VKB9XD/) 中讨论了 WebAssembly 如何与使用 Hyperlight 作为微型虚拟机管理器的虚拟机监控器一起工作，以及它在扩展 [Envoy](https://thenewstack.io/envoy-gateway-offers-to-standardize-kubernetes-ingress/) 网络过滤器中的用例。

Chiarlone 说：“要强调的关键区别在于隔离方法的差异。WebAssembly (Wasm) 作为一种较新的技术，提供了自己的沙箱机制。相比之下，Hyperlight 利用了虚拟机监控器技术，该技术已使用了很长时间，并且通常是在公共云环境中运行第三方代码所必需的。”

## 隔离总览

[![](https://cdn.thenewstack.io/media/2025/06/64a9a2c2-screenshot-2025-06-30-at-5.15.10%E2%80%AFpm-300x283.png)](https://cdn.thenewstack.io/media/2025/06/64a9a2c2-screenshot-2025-06-30-at-5.15.10%E2%80%AFpm-300x283.png)

在创建 Hyperlight 应用程序时，您有一个主机和一个访客。访客应用程序是在 Hyperlight 沙箱内运行的程序，例如 Wasm 沙箱和 Wasm 二进制文件。默认情况下，Hyperlight 应用程序不向访客提供任何功能。为了安全起见，它们与外界完全隔离。因此，主机必须显式提供访客所需的任何功能。在演讲的示例中，主机提供了访客将数据传回 Envoy 所需的网络连接。

端到端，交互如下：（1）嵌入式应用程序创建一个 Hyperlight Wasm 沙箱，准备执行 Envoy 网络过滤器访客；（2）嵌入式应用程序调用隔离的访客来计算数据；（3）访客在以某种方式操作数据后，回调到主机。

[![](https://cdn.thenewstack.io/media/2025/06/a10eab5d-screenshot-2025-06-30-at-5.15.32%E2%80%AFpm-1024x346.png)](https://cdn.thenewstack.io/media/2025/06/a10eab5d-screenshot-2025-06-30-at-5.15.32%E2%80%AFpm-1024x346.png)

Hyperlight 具有丰富的类型系统，允许访客和主机之间进行通信。Krinkin 说，一个实际的考虑因素是，可以通过使用向量字节作为所有数据来规避所述类型系统的可能性。可以使用诸如 Protocol Buffers 或 [FlatBuffers](https://github.com/google/flatbuffers) 之类的工具进行序列化和反序列化，从而允许开发人员传入数据并接收任何所需的接口，而无需深入研究 Hyperlight 类型系统的细节，Krinkin 说。

Krinkin 说，Hyperlight 是用“纯 Rust”编写的，这引入了一些考虑因素。例如，需要样板代码才能实现 [Rust](https://thenewstack.io/rust-programming-language-guide/) 和 [C++](https://thenewstack.io/introduction-to-c-programming-language/) 之间的互操作性，因为主机-访客调用是双向发生的。Krinkin 说，虽然样板代码的数量并不少，但也不是特别复杂，因此不是主要问题。

Krinkin 说，一个令人惊讶但最终可预测的方面是 Hyperlight 主机是多线程的。截至 0.5.0 版本，Hyperlight 会生成一个新线程来执行沙箱，从而在线程和微型虚拟机之间建立一对一的关系。Krinkin 说，这给 Envoy 带来了特殊的挑战，Envoy 像许多网络应用程序一样，是异步的且基于回调的。“Envoy 中的大多数处理都在单个线程上进行，从而最大限度地减少了锁定的需求，” Krinkin 说。“因此，从不同的线程访问 Envoy 数据结构是有问题的，因为 Envoy 严重依赖于线程本地存储。在这种情况下，访问尝试通常返回 null 或完全失败。”

Krinkin 说，引入了额外的样板代码，以将所有回调重新路由到 Envoy 工作线程，从而确保正确访问 Envoy 的数据结构。“这是一个至关重要的集成考虑因素，” Krinkin 说。

虽然不是直接的集成问题，但 Hyperlight 提供了一种称为“调用上下文”的机制，可以在不重置每次调用之间的状态的情况下进行多次访客函数调用。使用调用上下文，嵌入式应用程序必须显式调用“finish”来重置状态。

如果没有调用上下文，当调用访客时，并且该访客初始化数据（例如内存段或其他结构），则当访客调用结束时，所有此类状态都会丢失。任何后续调用都从一张白板开始。这限制了当前可以放置在 Hyperlight Wasm 中的功能。“这种行为很容易被忽视，但它会严重影响设计决策，” Krinkin 说。

提出了一个基本的性能基准，以证明这些特征的含义。Krinkin 说，该基准涉及一个 Echo 函数，该函数执行最少的逻辑：将固定大小的随机数据有效负载发送到 Envoy，并测量响应的往返时间。“重复多次以计算平均延迟和可变性，” Krinkin 说。“还改变了有效负载大小以评估其对性能的影响。”

对于该基准，比较了几个实现：Hyperlight Wasm、没有 Wasm 的本机 Hyperlight 访客（不涉及 WebAssembly 运行时）以及类似 Echo 功能的 Proxy-Wasm 实现。“虽然 Proxy-Wasm 变体不是完美的同类比较，但它提供了一个有用的参考点，” Krinkin 说。“这种区别对于随附演示文稿的大多数观看者来说是很明显的，并且已得到明确承认。”

[![](https://cdn.thenewstack.io/media/2025/06/59790834-screenshot-2025-06-30-at-5.16.31%E2%80%AFpm-1024x646.png)](https://cdn.thenewstack.io/media/2025/06/59790834-screenshot-2025-06-30-at-5.16.31%E2%80%AFpm-1024x646.png)

“Hyperlight 当前的性能不是最佳的。但是，这被认为是起点，而不是终点。最初的分析导致了 Hyperlight 本机实现的优化。具体来说，虽然 Hyperlight Wasm 会主动清除调用之间的状态（这是一项昂贵的操作），但 Hyperlight 本机可以绕过此步骤，从而使运行时提高约 15%，” Krinkin 说。“仍然存在其他唾手可得的优化机会，并且一些开销也可能源于次优的集成。基准测试结果表明，将有效负载从 128 字节增加到 4 千字节（增加 30 倍）会导致更长的运行时间，但相对于整体系统开销而言，影响很小。”

与此同时，Hyperlight 最近的开发基准测试表明，与运行这些测试时相比，有了显着改进（访客函数调用提高了 50% 以上）。

## Hyperlight 总和

在演示过程中，Krinkin 实现了他所说的“深度防御”，并且实现相对简单，Krinkin 说。“但是，当前缺少性能，并且是需要改进的主要领域，” Krinkin 说。

Krinkin 说，C API 的开发工作正在进行中，以便于集成到非 Rust 代码库中。（Hyperlight 核心提供 C API，但目前 Hyperlight Wasm 不提供。）还计划将 Hyperlight Wasm 集成为额外的 Proxy-Wasm 引擎。Proxy-Wasm 是 Envoy 用于执行 WebAssembly 插件的本机框架，并且已经支持多个引擎，例如 V8。Krinkin 说，Hyperlight 可以成为这些受支持的引擎之一。

“性能将是关键重点。虽然仍然存在许多简单的优化，但还需要更深入的分析和工具。当前工具无法轻易地公开访客中的性能开销，因此很难进行分析，” Krinkin 说。开发工具以使 Hyperlight 执行更加透明至关重要。最后，由于 Hyperlight 的预期用例涉及对相对较小的计算进行沙箱处理，因此随着计算工作负载的减少，沙箱的开销变得更加重要——因此，优化 Hyperlight 的性能至关重要。”

随着性能的不断提高，Hyperlight 在 Wasm 的软件隔离之上提供额外的硬件隔离层，从而使自身脱颖而出，从而为某些环境（例如，公共云）提供所需的安全性级别，并为其提供微型虚拟机生命周期管理和执行工具，同时仍然可以作为库轻松插入任何用户应用程序。要了解有关最新发展的更多信息，请查看 [Hyperlight 存储库](https://github.com/hyperlight-dev/hyperlight)。