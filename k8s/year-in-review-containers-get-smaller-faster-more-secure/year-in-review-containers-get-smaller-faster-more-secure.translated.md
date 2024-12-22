# 年度回顾：容器更小、更快、更安全

![Featued image for: Year in Review: Containers Get Smaller, Faster, More Secure](https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1-1024x576.png)

Yelp 使用数千个容器作为其网络规模运营的一部分。Yelp 软件工程师在今年早些时候的 KubeCon+CloudNativeCon 北美会议上的一次演讲中表示，其面临的首要挑战之一是容器安全。

“如果你从攻击者的角度考虑这个问题，他们是从容器开始的，”Robinson 说。一旦进入，恶意攻击者就会四处查看，如果他们找到通往你的存储桶的通道，他们就会去获取有价值的数据。

对于开发者来说，“最困难的挑战是在满足业务需求的同时保证应用程序的安全，”他说。“在开发产品和安全地开发产品之间总是存在这种张力。”

该组织已经围绕其容器部署了数千种警报机制，但这只会导致工程师产生警报疲劳。他解释说，Yelp 真正需要的是一种大规模强制执行安全最佳实践的方法。

因此，Yelp 建立了一个容器安全成熟度模型，以此来抽象并理解访问级别、数据敏感性和影响级别。

一旦建立了最佳实践，就可以添加自动合规性检查。

现在容器已经陪伴我们十多年了，为 Yelp 等公司的网络规模和企业级应用程序提供动力，尖端技术仍在不断发展。

以下是 2024 年容器领域的一些发展。

## 超越发行版的构建

Docker 容器最初的想法是它们将构建在 Linux 发行版（通常是 Debian）上，这将提供运行应用程序的核心组件。然而，这意味着每个容器镜像都包含数百 MB 的无用库，这些库占用空间并构成安全威胁。

因此，在过去几年中，人们做了大量工作来去除容器中不必要的组件，这种方法有时被称为 *distroless*。

六月，Canonical 推出了基于标准化开放容器倡议 (OCI) 格式构建的 Docker 打包开源软件的容器化版本，因此 LTS 容器应该可以在任何符合 OCI 的运行时环境中运行。

这些“distroless”容器非常适合 Kubernetes 环境，在这些环境中，它们可以打包到一个 Pod 中以实现最大的计算效率。

在今年早些时候的 Kubecon EU 演讲“[Building Container Images the Modern Way](https://www.youtube.com/watch?v=nZLz0o4duRs&list=PLn5JwIxcXmNqDljfxkBKNY88sd8KYKCnY&index=2)”中，安全公司 Chainguard 的技术社区倡导者对构建最小化容器的其他工作进行了概述。

容器基本上是应用程序打包格式。它是一个文件系统和元数据。

镜像应该包含什么？它应该将额外文件保持在最低限度，快速且可重现，并且在不同的系统之间具有通用性。

他指出，Docker 和 Google 都为此方法提供了替代方案，这是一种涉及多阶段构建的方法。

Mouat 说，多阶段 Docker 构建与最小的运行时镜像相结合，可能是构建镜像的最佳方法之一。

![code for building the Go app containe.](https://cdn.thenewstack.io/media/2024/12/ddb380e2-mouat-01.png)

使用 Go 静态镜像构建 Go 应用程序，生成的文 件大小只有几兆字节。

Chainguard 和 Google 都提供了用于构建的最小镜像。Mouat 说，如果你想运行静态镜像并且不需要 TLS 等任何操作系统功能，你甚至可以使用 scratch 镜像。

另一种至少可用于 Go 应用程序的方法是 ko。ko 从 `go build` 命令构建而来，甚至不需要安装 docker。

![ko, a Go builder](https://cdn.thenewstack.io/media/2024/12/556e8e29-demo-1024x386.png)

ko 运行中。
希望构建自己无发行版镜像的人可以使用[Google Bazel](https://bazel.build/)或Chainguard的[Apko](https://github.com/chainguard-dev/apko)（基于[Chainguard的Wolfi](https://github.com/wolfi-dev)），尽管Mouat告诫应尽可能避免这种方法。

“Bazel功能强大，”但它也可能非常令人困惑，Mouat说。帮助命令会生成几乎一整本书的信息。此外，它还有一些奇怪的行为。例如，它使用Google基础镜像，而不是为每个新镜像构建自己的镜像。

“如果你想使用Bazel，你必须知道自己在做什么。”

Apko在功能方面不如Bazel强大，但它提供了按位可重现的构建，这意味着对完全相同的镜像进行两次构建时，比较结果将完全相同（包括SHA-1哈希值）。

在策略繁重的环境中，按位可重现性是确保安全性的一个主要因素。Chainguard使用它来构建最小的无发行版运行时镜像。

Mouat讨论的其他方法包括[BuildPacks](https://thenewstack.io/safer-image-builds-with-cloud-native-buildpacks-and-wolfi/)、[BuildKit和Dagger](https://thenewstack.io/solomon-hykes-dagger-brings-the-promise-of-docker-to-ci-cd/)和[Nix](https://thenewstack.io/nixos-a-combination-linux-os-and-package-manager/)。

## 零开销容器网络
Linux内核的[6.7版本](https://lwn.net/Articles/949960/)引入了对Netkit的支持，Netkit是一个[可通过eBPF编程](https://thenewstack.io/p99conf-how-ebpf-could-make-faster-database-systems/)的网络设备，它缩短了网络数据包从一个容器移动到另一个容器（即使这两个容器都在同一主机上）时在网络堆栈上下移动的一些路径。

与其他虚拟网络设备一样，这些设备也添加到主机和容器的命名空间中，主机是主要的。

在今年早些时候[ScyllaDB的P99大会](https://thenewstack.io/p99-conf-3-ways-to-squash-application-latency/)上的演讲中，Isovalent首席开源官将这种方法称为“[零开销容器网络](https://www.p99conf.io/session/zero-overhead-container-networking-with-ebpf-and-netkit/)”。

使用容器时，应用程序与其主机和其他应用程序隔离，并拥有自己的网络命名空间，与主机的网络命名空间分开。连接是通过虚拟网络设备建立的。

“因此，进出容器化应用程序的数据包实际上必须通过网络堆栈两次，”Rice解释说。此外，数据包可能会丢失，拥塞控制算法会启动，进一步降低吞吐量。

一个基于eBPF的程序用于通过将网络数据包直接切换到容器的网络命名空间来绕过入口主机路由，“因此它看起来像是通过虚拟线到达容器内的虚拟网络设备，”Rice解释说。

对于出口流量，eBPF辅助函数可以查询内核转发信息库以查找下一个路由跳跃点。

通过将eBPF函数附加到容器自身的网络堆栈，可以获得进一步的性能提升，这在名为tcx（TC Express）的项目中实现，[在6.6内核中首次亮相](https://lore.kernel.org/all/20230719140858.13224-1-daniel@iogearbox.net/)，将数据包到达BPF功能所需的CPU周期数减少了大约一半（从59个周期减少到33个周期）。

结果，“Netkit设备实现了与本地主机网络相同的吞吐量，”Rice说。

[Isovalent](https://isovalent.com/)的工程师参与了该项目，并在今年[为其Cilium云原生网络平台](https://thenewstack.io/can-cilium-be-a-control-plane-beyond-kubernetes/) [添加了NetKit支持](https://isovalent.com/blog/post/cilium-netkit-a-new-container-networking-paradigm-for-the-ai-era/)。

## Dockerfile仍然占据主导地位
尽管在开发和运营方面都取得了所有这些进展，但大多数开发人员仍然习惯于使用传统的[Dockerfile](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)，它们是包含有关如何构建容器镜像的指令的文本文件。

“我非常讨厌Dockerfile，但它们一直是人们采用容器的一种务实（且现在无处不在）的方法，我认为它们不会很快消失，”Chainguard创始人兼首席技术官说。

该公司在实践中，例如维护黄金镜像和严格的管道，非常务实，Moore指出。

如上所述，Chainguard采用“最后一英里”镜像构建方法，使用“无发行版”镜像和ko、[Jib](https://cloud.google.com/java/getting-started/jib)和[CNCF buildpacks](https://www.cncf.io/projects/buildpacks/)等工具。
“Chainguard的镜像采用率正在飞速增长，但我们仍然看到很多人将它们放入传统的Chainguard Dockerfiles中，”Moore说。

“虽然看到有趣的新想法再次出现是一件好事，但我很难想象任何想法能够对现在无处不在的格式构成严重的冲击，”Fermyon Technologies首席执行官Matt Butcher说。“尽管许多想法很有趣，但事实证明，Dockerfiles总体上更容易。”

*TNS分析师Lawrence Hecht为本报告做出了贡献。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)  技术发展日新月异，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。