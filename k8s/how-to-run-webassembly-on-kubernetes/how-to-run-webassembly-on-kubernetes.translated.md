# 如何在 Kubernetes 上运行 WebAssembly
![如何在 Kubernetes 上运行 WebAssembly 的特色图片](https://cdn.thenewstack.io/media/2024/07/8f350ba4-berlin-4068968_1280-1024x663.jpg)

前几天，我和一位平台工程师聊天。“你做 WebAssembly 的事情，对吧？似乎每个人都在谈论它作为一种新的无服务器方式。这意味着什么？”最初被设想为一种浏览器技术，[WebAssembly](https://thenewstack.io/webassembly/) (Wasm) 现在出现在许多地方。在 Kubernetes 世界中，它提供了一种新的运行无服务器的方式——有时被称为 FaaS 或函数即服务。

[Kubernetes](https://thenewstack.io/kubernetes/) 刚刚度过了它的[十周年纪念](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/)。在 2015 年和 2016 年的早期，我们谈论了[Kubernetes 作为 Docker](https://thenewstack.io/docker-versus-kubernetes-start-here/) 的编排器。它位于[Docker](https://www.docker.com/?utm_content=inline+mention) 之上，并安排容器在 Docker 实例上运行。
但 Docker 本身并不真正支持这一点。他们创建了自己的编排器 Swarm，他们认为它优于 Kubernetes。并且有一些不好的血统。DockerCon 禁止关于 Kubernetes 的演讲，但 Docker 人员出现在 KubeCon 上讨论 Swarm 如何比 Kubernetes 更好。几年后，我们都原谅了并继续前进。但在那一刻，两者之间的冲突将 Kubernetes 引向了令人兴奋的方向。Kubernetes 开发人员没有停留在以 Docker 为中心，而是向上抽象层跳了一步，开始将 Kubernetes 称为*容器编排器*。他们开始尝试支持其他容器运行时，例如 CoreOS 的 rkt（发音为“rocket”）。

从容器运行时的细节中抽象出来具有很大的优势。一个由一家公司控制创新的领域突然对所有人开放。[Red Hat](https://www.openshift.com/try?utm_content=inline+mention)、三星、[微软](https://news.microsoft.com/?utm_content=inline+mention)、[谷歌](https://cloud.google.com/?utm_content=inline+mention) 以及许多其他信誉良好的工程组织可以将他们强大的才能带到这个领域。

现在，十年后，好处显而易见。Containerd 现在是一个由[云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention) 管理的成熟项目，它提供了如此多的灵活性，以至于开发人员添加了各种 containerd“垫片”来支持大约十几个不同的底层运行时。

其中一项支持的技术是 Wasm。

## 从浏览器到云
Wasm 的开发是为了解决一个特定的问题：获取来自 C、C++、Rust、Go 和 Zig 等语言的库代码，并使它们可用于在 Web 浏览器中运行的 JavaScript 代码。在某种程度上，Wasm 的设计是为了纠正 Java Applet、Silverlight、Flash 和其他非 JS 浏览器语言所犯的错误。在这方面，Wasm 已经取得了成功。每个主流浏览器都支持 Wasm，从 Office 365 到 Figma，Wasm 为一些复杂的 Web 应用程序提供动力。

但 Wasm 的安全模型、跨平台支持和紧凑的字节码格式使其非常适合浏览器之外的其他应用程序。BBC 和[亚马逊](https://aws.amazon.com/?utm_content=inline+mention) 在他们的嵌入式流媒体播放器中使用它。Shopify 将其用作插件语言。SingleStore 在其数据库中支持 Wasm 存储过程。最有趣的是，Wasm 正在云端取得进展。

## 无服务器是最佳选择
无服务器计算由 AWS 的 Lambda 服务引入，允许开发人员编写事件处理程序而不是整个服务器守护程序。当请求进来时，事件处理函数启动，处理该请求（如果需要，返回响应），然后关闭。虽然容器或 VM 运行数小时、数天、数月甚至数年，但无服务器函数运行从几毫秒到几分钟不等。但是，如果您的函数只运行几毫秒，那么运行时的性能就是首要问题。早期的无服务器解决方案往往性能不佳。

这就是 Wasm 发光的地方。Wasm 运行时可以在不到一毫秒的时间内冷启动。这意味着 Wasm 函数可以在眨眼之间从零个实例扩展到数十万个实例——然后同样快地缩减回零。在一个云账单巨大的时代，这种微不足道的资源使用和出色的性能意味着可以缩减云资源！运行 Wasm 比运行容器需要更少的服务器。

## Containerd，遇见 Wasm
随着 Knative、OpenWhisk、Fn Project 和其他 Kubernetes 无服务器框架难以有效地执行，在 Kubernetes 内部有一代新的无服务器的明显空间。
这就是[SpinKube](https://spinkube.dev) 的用武之地。SpinKube 在 KubeCon 巴黎公开发布，并有望成为 CNCF 沙盒项目，它提供了将 Wasm 支持添加到 containerd 的所有基础设施，然后在 Kubernetes 中与容器并排支持 Wasm 应用程序。Containerd 的设计非常出色，以至于 Wasm 二进制文件可以与容器一起调度到同一个 Kubernetes Pod 中，并且两者可以并排运行。这意味着一种新型的超高性能无服务器 Kubernetes 可以增强现有的容器应用程序。那些希望全面采用无服务器的人，可以快速轻松地将他们的 Lambda 和 Azure Functions 代码移植到 Kubernetes 上。另一方面，那些希望开始减少集群内部浪费的人，可以使用 Wasm 函数替换 sidecar 或低流量微服务……然后逐渐迁移对他们有意义的部分。

合适的技术满足了其初始设计的潜力。伟大的技术超越了其初始设计。Kubernetes 和 Wasm 都做到了这一点，将它们结合在一起，以解决现代 Kubernetes 集群中实际的性能和成本问题。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。