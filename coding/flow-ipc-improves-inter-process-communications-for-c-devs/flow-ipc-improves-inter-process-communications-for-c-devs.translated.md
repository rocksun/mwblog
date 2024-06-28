# Flow-IPC 提升 C++ 开发人员的进程间通信

![Flow-IPC 提升 C++ 开发人员的进程间通信 特色图片](https://cdn.thenewstack.io/media/2024/06/9b33ed37-robots-1024x575.jpg)

进程间通信 (IPC) 对现代计算至关重要，它使多个处理器核心能够同时执行线程。本质上，IPC 允许不同的线程，甚至独立的程序，高效地共享数据。例如，当您流式传输视频时，一个线程可能处理视频解码，而另一个线程处理渲染。

当这些线程在不同的程序中运行时，例如 Web 服务器和安全服务器，就会出现挑战。在这些程序之间传输 [大量数据](https://thenewstack.io/data/) 的传统方法可能很慢且效率低下，这通常是由于不同的操作系统管理内存的方式造成的。开源 [Flow-IPC](https://www.akamai.com/blog/developers/flow-ipc-introduction-low-latency-cpp-toolkit) 通过使 IPC 对于 C++ 开发人员变得快速而直接来解决这一挑战。

**Flow-IPC：一个开源项目**

Akamai 在 2022 年收购 Linode 标志着向云原生计算的战略加速。我们将上游贡献纳入我们的业务战略，并倡导开源。本着这种精神，我们在今年早些时候 [推出了 Flow-IPC](https://www.akamai.com/blog/developers/flow-ipc-introduction-low-latency-cpp-toolkit)。它是一个开源 [中间件](https://thenewstack.io/case-containerizing-middleware/)（Apache 2.0 和 MIT 许可证），专门设计用于帮助 C++ 程序员简化他们的 IPC。

Flow-IPC 最初是 Akamai 内部的一个工具，用于一个需要将大型应用程序拆分而又不影响性能的项目。现有的 IPC 解决方案要么太慢，要么太复杂。从一开始，我们就将 Flow-IPC 设计为 C++ 中 IPC 的通用解决方案。[将 Flow-IPC 开源](https://www.linode.com/blog/open-source/flow-ipc-introduction-low-latency-cpp-toolkit/) 并与开发人员社区共享，是促进创新并简化任何需要 [使用 C++](https://thenewstack.io/google-spends-1-million-to-make-rust-c-interoperable/) 来管理多个线程共享数据的开发人员生活的一种方式。

我们在 2024 年 4 月 [公开发布了 Flow-IPC](https://www.linode.com/blog/open-source/flow-ipc-introduction-low-latency-cpp-toolkit/)，该项目在 [Hacker News](https://news.ycombinator.com/item?id=40028118) 和其他社区平台上获得了积极的响应。开发人员分享了他们自己的 IPC 挑战和解决方案，从而引发了建设性的讨论和宝贵的反馈。

Flow-IPC 是为服务器端系统开发社区中的广泛受众设计的。虽然它目前专注于 C++，但它有可能扩展到其他编程环境。同样，它目前支持在 x86-64 上运行的 Linux。我们计划根据需求将该项目扩展到 macOS 和 ARM64，然后扩展到 Windows 和其他操作系统变体。

Flow-IPC 是一个具有可扩展 C++17 API 的库，目前可用于在进程边界之间进行本地通信。它托管在 GitHub 上，并附带完整的文档、自动化测试和演示，以及一个 CI 管道，该管道在各种 GNU 编译器集合 (GCC) 和 Clang 编译器版本和构建配置中进行测试，包括通过运行时清理器（如 ASan（防止内存滥用）、TSan（防止竞争条件）和 UBSan（防止各种未定义行为））进行硬化。

**将 Flow-IPC 与其他解决方案进行比较**

[Flow-IPC](https://tfir.io/akamais-open-source-project-flow-ipc-solves-ipc-latency-challenges-in-c/) 提供了简单性和效率。与 gRPC 等通用解决方案（优雅但会引入延迟）不同，Flow-IPC 最小化了数据复制，并无缝集成到现有系统中。传统的 IPC 会根据有效负载大小引入延迟；在我们的测试中，传输速度已达到一秒范围。Flow-IPC 可以像 100KB 有效负载一样快地传输高达 1GB 的数据结构有效负载——以微秒为单位。这相当于提高了三到四个数量级。商业级内存分配器与共享内存集成在一起，以进一步提高性能。

**未来展望**

我们很高兴看到社区将 [Flow-IPC](https://sdtimes.com/softwaredev/sd-times-open-source-project-of-the-week-flow-ipc/) 带到哪里。我们欢迎贡献、功能请求和错误报告，因为我们将继续开发和完善该项目。
我们有一些想法，在未来发展方面具有巨大潜力。短期内，与 [capnp-rpc](https://capnproto.org/rpc.html) 以及可能与 [gRPC](https://grpc.io/) 集成是轻而易举的事。协议和 API 将保持这些优雅框架所期望的，而 Flow-IPC 将提供底层的零拷贝性能。从长远来看，凭借其可扩展的设计，Flow-IPC 可以扩展到网络 IPC，此外，通过远程直接内存访问 (RDMA)，超高速局域网性能也是可能的。

Flow-IPC 在开源社区中越来越受欢迎，我们期待与 C++ 开发人员合作，使其变得更好。这是我们正在进行的项目的一个例子，通过开源模式将我们的技术带给全球的开发人员。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。