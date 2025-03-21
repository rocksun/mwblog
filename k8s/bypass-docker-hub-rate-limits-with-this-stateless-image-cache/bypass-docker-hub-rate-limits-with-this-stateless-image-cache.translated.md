# Spegel：用于本地存储镜像工件的无状态缓存

![Spegel：用于本地存储镜像工件的精选图片](https://cdn.thenewstack.io/media/2025/02/462544f1-spegel-1024x683.jpg)

对于那些在家运行小型实验集群的人来说，这些仓库限制可能是一个“主要的痛点”，开发者 Philip Laine 指出。

Laine 是 [Spegel](https://spegel.dev/) 的作者，这是一个 [开源项目](https://github.com/spegel-org/)，它将点对点文件共享引入到容器注册表的世界。

Spegel 可以帮助爱好者们保持在他们的配额之下，并帮助更大的组织更快地部署他们的 Kubernetes 工作负载集群。

当 Kubernetes 启动或恢复一个节点时，每个节点必须从附近的注册表（无论是云、公共的还是单独自托管的）拉取每个工作负载镜像的副本。

Spegel 在每个节点上 [建立一个分布式注册表](https://spegel.dev/docs/)，因此每个唯一的容器可以被下载一次，然后复制到其他节点。

在本月早些时候的 [FOSDEM 演讲](https://fosdem.org/2025/schedule/event/fosdem-2025-4934-cache-me-if-you-can-p2p-image-sharing-in-kubernetes-with-spegel/) 中介绍这项技术时，[Spegel](https://github.com/spegel-org/) 的创建者发布了 [基准测试](https://github.com/spegel-org/benchmark)，显示镜像检索时间可以提高 82%。

这种方法还可以加快工作负载启动时间并减少网络流量。

## 无状态集群本地 OCI 注册表

云原生当前瓶颈是将工作负载分发到运行时。

但是，操作可能会因镜像注册表的速率限制而受阻，或者如果注册表离线则完全停止。或者镜像可能会消失，例如 [Quay 最近发生的事情](https://www.redhat.com/en/blog/about-the-quay.io-outage-post-mortem)。

Laine 告诉观众：“如果你无法拉取实际运行的应用程序的镜像，那么拥有一个可以扩展到 10,000 个节点的集群是没有意义的。”

如果镜像非常大，仅仅是网络传输时间就会减慢速度，对于速率限制来说更是如此：例如，[Docker Hub](https://www.docker.com/?utm_content=inline+mention) 将镜像的下载速度限制为 100MB/s。

## 像 BitTorrent，但用于容器

Laine 回忆起 2018 年左右的一次聚会演讲，一位系统管理员讲述了他的组织如何在 Docker Hub 中断期间，在其自身用户量急剧增加的情况下开展工作。由于它依赖于来自临时离线的 Hub 的几个关键镜像，因此操作无法扩展。

系统管理员的解决方案是 [ssh](https://thenewstack.io/dr-torq-go-remote-with-ssh/) 进入一个旧节点，然后导出镜像，然后基本上不断地将镜像 [复制](https://thenewstack.io/linux-lesson-copy-files-over-your-network-with-scp/) 到新节点，因为它们上线了。

Laine 说：“即使这是一个非常肮脏的解决方案，它也奏效了。”

这个变通方法激发了 Laine 的一个想法：“为什么我们不一直这样做呢？”

因此开始了 Spegel 的工作，这是一个符合 OCI 的只读注册表。

根据 Laine 的说法，该实现结果出人意料地容易，他也是 [Flux](https://thenewstack.io/why-flux-isnt-dying-after-weaveworks/) GitOps 工具的核心开发人员之一。

一个镜像实际上是多个组件的集合。在顶层是所有其他包含组件的索引。它以 JSON 格式 [引用](https://oci.dag.dev/?image=ghcr.io%2Fspegel-org%2Fspegel%3Av0.0.30) 所有其他层及其摘要或内容本身的加密哈希。

[Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) 的开放容器接口 (OCI) 规定了容器的结构。OCI 分发规范描述了客户端如何从 [注册表](https://thenewstack.io/tutorial-host-a-local-podman-image-registry/) 拉取镜像，这是逐层完成的。

Spegel 允许 Kubernetes 节点从彼此拉取镜像。如果所有节点都没有该镜像，则请求会回退到原始注册表。

OCI 的 [containerd 格式](https://thenewstack.io/dockers-quest-simplicity-evolution-containerd/) 提供的一个优势是它在磁盘上存储未压缩的镜像层。文件名是哈希值。

“这意味着 Spegel 可以利用 Containerd。它没有做任何类型的存储。因此，注册表的作用是充当代理。“根本没有状态，”他说。

每个节点都有一个 OCI 注册表，它首先在本地主机上查找该层。如果未找到，Spegel 会拦截该请求并在其他节点上查找请求的层。如果找到，它会代理该请求。
Speqel 有三个组件：注册表、路由和发现组件，以及广告机制。

“这有点像 BitTorrent，”他说。“这是一堆客户端向其他客户端做广告。”

注册表会查看磁盘上的所有内容，然后在分布式哈希表中对其进行广告。该软件使用了广泛使用的 [Kademlia 分布式哈希表](https://github.com/libp2p/specs/tree/master/kad-dht) 的 [Go 实现](https://github.com/libp2p/go-libp2p-kad-dht)。当请求进入时，Spegel 只是在哈希表上查找它。

## 新的 Docker 速率限制

Laine 说，今天，Spegel 的大多数用户往往是希望避免 Docker Hub 速率限制的家庭实验室爱好者。其他用途可能是在气隙部署中或运行非常大的机器学习模型，如果本地完成，这些模型可以更快地复制。

3 月 1 日，Docker Hub 最新速率限制开始生效，用于从 Docker Hub 拉取镜像。专业（付费）帐户不再限制镜像拉取的次数，个人帐户[将限制](https://www.docker.com/blog/revisiting-docker-hub-policies-prioritizing-developer-experience/)为每小时 100 次拉取（如果未经验证，则为 10 次）。

Spegel 与云提供商的[兼容性](https://spegel.dev/docs/getting-started/#compatibility)因其对 OCI 规范的遵守程度而异。Spgel 与 [Amazon Kubernetes Service](https://aws.amazon.com/?utm_content=inline+mention) 配合良好，与 [Azure Kubernetes Service](https://azure.microsoft.com/en-us/products/kubernetes-service) 有一定的兼容性，但到目前为止，与 [Google Kubernetes Engine](https://cloud.google.com/?utm_content=inline+mention) 完全不兼容。

它也与 [MiniKube](https://thenewstack.io/install-minikube-on-ubuntu-linux-for-easy-kubernetes-development/) 配合良好。它实际上嵌入在 SUSE 的 [K3s](https://thenewstack.io/ranchers-k3s-joins-cncf-sandbox-as-first-kubernetes-distribution/) 和 [RKE2](https://thenewstack.io/suse-upgrades-its-rancher-kubernetes-management-family/) Kubernetes 发行版中。

最终，Spegel 可能会帮助我们重新思考如何通过点对点共享的力量来实现镜像分发，这将使业余爱好者和最大的大规模 Kubernetes 用户受益。

*TNS 分析师 Lawrence Hecht 为这篇文章做出了贡献。注意：这篇文章于 2 月 24 日更新，以反映修订后的 Docker Hub 速率限制。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。