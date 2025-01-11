# Kubernetes 上 WebAssembly 与容器的爱情故事

![Kubernetes 上 WebAssembly 与容器的爱情故事特色图片](https://cdn.thenewstack.io/media/2025/01/a44c06b5-freestocks-r_ov6smbbyk-unsplash-1-1024x683.jpg)

对于某些工作负载，使用[WebAssembly](https://thenewstack.io/webassembly/)正在成为 Kubernetes 环境中替代容器的最佳用例。[Wasm](https://thenewstack.io/what-makes-wasm-different/) 模块可以与[容器](https://thenewstack.io/containers/)并行运行，替代更重的容器，或者在需要非常快的冷启动时间时使用，因为 Wasm 模块可以进行扩展和缩减。

例如，重量级容器在 sidecar 和[服务网格](https://thenewstack.io/service-mesh/) 或使用[OpenTelemetry](https://thenewstack.io/honeycomb-ios-austin-parker-opentelemetry-in-depth/) 进行可观测性解决方案时尤其成问题。相比之下，用 WebAssembly 组件替换在 Kubernetes 上运行的 sidecar 容器，可以提供更好、更轻量级和更快的冷启动时间。

是的，

[#Wasm]可以在 Kubernetes 上发挥作用，在某些情况下替代容器。[@Microsoft]的 Zhou Jiaxiao 在他的[@KubeCon_]演讲“与容器工作负载并行运行 WebAssembly (Wasm) 工作负载”中详细介绍了其工作原理。[@thenewstack][@fermyontech][#webassembly][pic.twitter.com/WZ1egGyhDG]— BC Gain (@bcamerongain) [2024 年 11 月 15 日]

如下所示，在 Kubernetes 上使用容器运行 WebAssembly 是可行的，正如微软高级软件工程师 Zhou Jiaxiao 在 11 月盐湖城举行的[KubeCon+CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 上的演讲“与容器工作负载并行运行 WebAssembly (Wasm) 工作负载”中所说。

Zhou 在他的演讲中说：“多年来，我一直从事 WebAssembly 的工作，我经常听到人们说，‘我们可以在我现有的基础设施（即 Kubernetes）中运行 WebAssembly 吗？’因此，必须使 WebAssembly 与 Kubernetes 兼容或可在 Kubernetes 中运行。”

## 工作原理

![](https://cdn.thenewstack.io/media/2025/01/a013277e-capture-decran-2025-01-06-175647-1024x403.png)

来源：CNCF 和微软

WebAssembly 在 Kubernetes 上展现出良好的前景，这要归功于 WebAssembly 现在符合 OCI 注册表标准，成为 OCI 工件。这使得 Wasm 能够满足 Kubernetes 标准和容器化的 OCI 标准，特别是 OCI 工件格式。它还涉及与 Kubernetes Pod、存储接口等的兼容性。在这方面，它是朝着将 Wasm 用作容器替代方案迈出的一步。

此外，通过[containerd](https://thenewstack.io/azure-kubernetes-service-replaces-docker-with-containerd/)，WebAssembly 组件可以与 Kubernetes 环境中的容器并行分发。Zhou 将此比作单元容器的直接替换，并与[Istio](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/)、[Dapr](https://thenewstack.io/dapr-create-applications-faster-with-standardized-apis/) 和 OpenTelemetry Collector 等工具集成。

Zhou 指出，当在集群中将 WebAssembly 作为 sidecar 运行应用程序时，面临的两个主要挑战是分发和部署。一种简单的方法是将 Wasm 运行时捆绑到容器中，但更好的方法是将 Wasm 运行时卸载到 containerd 中的 shim 进程。这种方法允许 Kubernetes 编排 Wasm 工作负载。Zhou 说，WebAssembly 的 OCI 工件格式使得 Wasm 组件能够使用与容器相同的分发机制，负责分发部分。

Zhou 说，同样，可以将 Wasm 运行时和 Wasm 层捆绑到 containerd 中，并在 Kubernetes 中运行该容器。“显然，这是可行的。但我们想做得更好：我们想将 Wasm 运行时卸载到 containerd 中运行的 shim 进程中。”

因为 containerd 是 Kubernetes 的事实上的运行时，所以它可以由 Kubernetes 编排——“这正是我们所做的，”Zhou 说。借助 Zhou 担任维护者的[RunWASI](https://github.com/containerd/runwasi) 项目，可以使用一个用于编写 shim 的库来运行 WebAssembly 工作负载，它支持多个 WebAssembly 运行时：[Wasmtime](https://thenewstack.io/webassemblys-wasmtime-1-0-revamps-security-performance/)、[WasmEdge](https://thenewstack.io/demos-deploying-llms-with-wasmedge/)、[SpinKube](https://thenewstack.io/how-to-build-serverless-webassembly-apps-with-spinkube/) 和其他选项，可以与容器并行运行 WebAssembly，Zhou 说。
“秘诀在于shim架构，”周说。当containerd向shim发送RPC请求，要求shim创建一个容器并启动容器执行时，shim将创建一个新实例。周说，该实例将检查二进制文件的前几个字节，以查看这是Linux容器还是Wasm二进制文件。“如果是Wasm二进制文件，我们将使用内置于shim中的Wasm运行时来执行该实例；如果是Linux容器，我们将使用Linux运行时来运行该容器，”周说。“这都要归功于一个名为Yuki的令人惊叹的开源项目。它是用Rust编写的，我们使用Yuki的libcontainer执行器编写我们自己的Wasm运行时，并且可以将实例分派到Linux情况或Wasm情况。”

## 立即使用
![](https://cdn.thenewstack.io/media/2025/01/34e031ad-capture-decran-2025-01-02-182357-1024x224.png)
来源：CNCF和微软

周描述了在Kubernetes上使用WebAssembly的两种场景：首先，作为[Linux](https://thenewstack.io/steve-langasek-one-of-ubuntu-linuxs-leading-lights-has-died/)容器的直接替代品——“因为它们太重了，”周说。“我们想将其重写为WebAssembly，但我们仍然想使用sidecar容器来添加登录、OpenTelemetry等，”周说。第二种情况是，你有一个重量级的Linux容器，由于语言工具链问题，你无法将其编译为Wasm。但是，可以从你的Linux容器中“提取一些功能”或一些代码，将其编译为Wasm，并作为sidecar容器在同一个pod中运行，周说。

同样，周说，在Kubernetes上运行WebAssembly可以克服与容器相关的一些缺点。容器的大小通常为数百兆字节，有时整个操作系统都捆绑在容器内，这“使其膨胀，”周说。容器还有一些缓慢的冷启动时间，可能需要几秒钟，“对于某些用例（如突发函数工作负载）来说，这不够快，”周说。必须针对每种架构构建容器——为x86构建的容器将无法在Arm上运行——并且容器间通信有很多开销，周说。

特别是sidecar容器可能特别重且大。周说，一个[Linkerd](https://thenewstack.io/some-linkerd-users-must-pay-fear-and-anger-explained/) sidecar可能会消耗高达150兆字节的磁盘空间，因为它们已将整个[JVM](https://thenewstack.io/chicory-write-to-webassembly-overcome-jvm-shortcomings/)捆绑到sidecar中。sidecar容器会消耗额外的CPU、内存和网络资源，因为它们作为主要应用程序的sidecar运行。“因此，它们实际上正在与你的主要应用程序竞争资源消耗。鉴于sidecar容器和主应用程序可能由不同的团队管理，因此存在一些操作复杂性，”周说。“它们有不同的升级和版本控制。如果你的sidecar运行过于频繁，它可能会中断你的主应用程序，因此以上三点都会对pod扩展和集群效率产生积极影响。”

另一方面，WebAssembly的冷启动时间低于毫秒。“这非常有吸引力，因为现在你可以根据请求启动一个新的WebAssembly实例，并且它具有快速的Wasm间通信，”周说。“你可以将两个Wasm组件组合在一起，通信将是本地函数调用，这将为你的访客应用程序提供高密度。”

WebAssembly也有一些缺点。“并非所有Linux二进制文件都可以编译为WebAssembly。WASI可能不支持某些系统调用。并且语言工具并不理想，”周说。“我一直在努力将Go语言与WASI集成，但我们仍然没有[WASI P2](https://github.com/WebAssembly/WASI/blob/main/wasip2/README.md)用于[Go](https://thenewstack.io/golang-how-to-use-the-go-install-command/)。WASI是一项相对较新的技术，因此需要对一些安全边界进行生产测试。”

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)