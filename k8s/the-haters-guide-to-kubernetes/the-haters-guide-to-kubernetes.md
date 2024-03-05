
<!--
title: Kubernetes憎恨者指南
cover: ./cover.png
-->

在某些技术领域，Kubernetes 被认为是一个不必要的复杂时间浪费，初创公司应该避免使用。使用 Kubernetes 和一个小团队被视为过度工程的标志。

> 译自 [The hater’s guide to Kubernetes]([None](https://paulbutler.org/2024/the-haters-guide-to-kubernetes/))，作者 Paul Butler。

我自己也犯了[轻蔑的错误](https://twitter.com/paulgb/status/1568257167882436608)。

> 我可能有时会抱怨 Kubernetes，但它确实是一项伟大的技术。我强烈推荐给我的所有竞争对手。
> —— Paul Butler (@paulgb) [2022 年 9 月 9 日](https://twitter.com/paulgb/status/1568257167882436608?ref_src=twsrc%5Etfw)

尽管我说了一些挖苦的话，但"了不起的技术产品"确实是发自内心的称赞。在发那篇帖子的时候，我[写过](https://driftingin.space/posts/complexity-kubernetes)关于Kubernetes的复杂性对于它所做的事情来说是多么必要。

我们在[Jamsocket](https://jamsocket.com/) 已经运行 Kubernetes 生产环境几年了，我发现它运行得很好。Kubernetes 的宁静已经在内部实现。其中的一个关键是[剔除 Kubernetes 的一小部分](https://twitter.com/paulgb/status/1743361919535260053) 功能，并假装其余部分不存在。

这篇文章最初是关于我们使用 Kubernetes 方式的内部指南，因此它并不意味着对每个初创公司都有指导意义；尽管如此，我认为这是一个避免 Kubernetes 浩瀚海洋中许多沙洲的良好起点。

## 为什么要使用 Kubernetes？

在我看来，如果你想要以下三件事，Kubernetes 是最适合的途径：

1. 运行多个进程/服务器/计划作业。
2. 以冗余方式运行它们，并在它们之间进行负载均衡。
3. 将它们及其之间的关系配置为代码。

最基本的，Kubernetes 只是一个抽象层，它让你可以将一组计算机视为一台（无头）计算机。如果这是你的用例，并且你可以避免它的其他部分，你就可以走得很远。

有些人告诉我，第 2 点是过度杀伤，初创公司不应该专注于零停机时间部署或高可用性。但我们每天经常进行多次部署，当我们的产品出现故障时，我们的客户的产品也会为 *他们的* 用户出现故障。即使一分钟的停机时间也会被某人注意到。滚动部署让我们有信心随意且频繁地部署。

## 我们如何使用 Kubernetes

作为背景，
[Jamsocket](https://jamsocket.com) 是一项服务，用于动态启动 Web 应用程序可以与之通信的进程。有点像 AWS Lambda，但进程生命周期与 WebSocket 连接绑定，而不是与单个请求/响应绑定。

我们使用 Kubernetes 来运行支持此功能所需的长期运行进程。API 服务器、容器注册表、控制器、日志收集器、一些 DNS 服务、指标收集等。

我们 *不* 使用 Kubernetes 的一些事情：

- 短暂进程本身。我们很早就尝试过，但我们很快发现它有局限性（稍后会详细介绍）。
- 静态/营销网站。我们为此使用[Vercel](https://vercel.com/)。它更昂贵，但对于一家小型初创公司来说，一小时的工程时间的机会成本也是如此，而 Vercel 为我们节省的时间比它花费的时间更多。
- 任何我们不希望丢失的数据的直接存储。我们确实使用一些持久卷进行缓存或派生数据，但除此之外，我们在集群外部使用托管的 Postgres DB 和 Blob 存储。

值得注意的是，我们自己不管理 Kubernetes——使用 Kubernetes 的主要优点是我们可以将其基础设施级别的操作外包！我们对 Google Kubernetes Engine 很满意，虽然[Google Domains 惨败](https://blog.pragmaticengineer.com/google-domains-to-shut-down/) 动摇了我对 Google Cloud 的信心，但我至少可以安心地知道迁移到 Amazon EKS 相对简单。

## 我们随时使用的功能

有一些类型的 k8s 资源我们毫不犹豫地使用。我在这里只列出我们显式创建的资源；其中大多数资源隐式创建其他资源（如 Pod），我不会提及，但我们当然（间接地）使用它们。

- **部署：** 我们的大多数 Pod 都是通过部署创建的。对我们的服务功能至关重要的每个部署都有多个副本和滚动更新。
- **服务：** 具体来说，ClusterIP 用于内部服务，LoadBalancer 用于外部服务。我们避免使用 NodePort 和 ExternalName 服务，更喜欢将我们的 DNS 配置放在 Kubernetes 之外。
- **CronJob：** 用于清理脚本和类似内容。
- **ConfigMap** 和 **Secrets：** 用于将数据传递给上述资源。

## 我们谨慎使用的功能

**StatefulSet** 和 **PersistentVolumeClaim**：我们使用了一些 StatefulSet。配置比 Deployment 稍微复杂一些，但它们可以在重启后保留持久卷。我们更喜欢将重要数据持久化到 k8s 之外的托管服务中。我们没有针对卷的严格规则，因为有时在服务重启后保留缓存等内容会很好，但如果可能的话我会避免使用它们，因为它们可能会与滚动部署交互不良（死锁）。

**RBAC**：我们在一些地方使用了它，例如授予服务刷新机密的权限。它给我们的小型集群增加了足够的复杂性，所以我大多避免使用它。

## 我们积极避免的事情

- **手动编写 YAML**。YAML 有 [足够的陷阱](https://noyaml.com/)，所以我尽可能避免使用它。相反，我们的 Kubernetes 资源定义是使用 TypeScript 和 [Pulumi](https://www.pulumi.com/) 创建的。
- **非内置资源和操作符**。我之前 [写过](https://driftingin.space/posts/complexity-kubernetes) 关于 [控制循环](https://kubernetes.io/docs/concepts/architecture/controller/) 模式如何是一把双刃剑：它是使 K8s 强大的核心思想，但它也是间接性和复杂性的来源。[operator 模式](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) 和 [自定义资源](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) 允许第三方软件使用 Kubernetes 的强大基础设施进行自己的控制循环，这是一个理论上很棒但在实践中我发现很笨拙的想法。我们不使用 [cert-manager](https://cert-manager.io/)，而是使用 [Caddy](https://caddyserver.com/) 的证书自动化。
- **Helm**。Helm 因为操作符和没有 YAML 规则而不行，但我还认为使用非结构化字符串模板来生成机器可解析的内容意味着在没有收益的情况下引入脆弱性。[对我来说就像在黑板上钉钉子，抱歉。](https://v2.helm.sh/docs/charts_tips_and_tricks/#using-the-include-function)
- **名称中带有“网格”的任何东西**。我想它们对某些人有用，但对我来说没有用，对 [这个人](https://matduggan.com/k8s-service-meshes/) 也没有用。
- **Ingress 资源**。我还没有因此留下任何伤疤，我知道有些人会高效地使用它们，但我们成功使用 Kubernetes 的一个主题是避免添加不必要的间接层。配置 Caddy 对我们有效，所以我们只做这件事。
- **尝试在本地复制整个 k8s 堆栈**。我们不使用 k3s 或 kind 等工具来精确复制生产环境，而是只使用 Docker Compose 或我们自己的脚本，在当下启动我们真正关心的系统子集。

## 人类永远不应该等待 Pod

上面我提到了这样一个事实：我们在 Kubernetes 上短暂运行了短暂的、交互式的、会话生存的进程。我们很快意识到 Kubernetes 是为容器启动时间而设计的，而不是为了健壮性和模块化。作为一个一般规则，我的看法是 Kubernetes 适用于冗余运行一些长期运行的进程，但如果一个人正在等待 Pod 启动，[Kubernetes 是错误的选择](https://twitter.com/paulgb/status/1684718880353042432)。

我承认我在这里谈论我的书，但至少这是一本开源书：我们使用一个名为 [Plane](https://plane.dev/) 的 MIT 许可的 Rust 编排器，我们专门设计它来快速调度和运行交互式工作负载的进程（即有人在等待它们）。

## 更高级别的抽象

为了完整起见，我还应该提到一些已经出现的 Kubernetes 替代品非常好。特别是如果你不想要或不需要我最初列表中的要求 3（将基础设施指定为代码的能力）。对于 [我们的一个产品](https://y-sweet.cloud/)，我们选择使用 [Railway](https://railway.app/) 而不是我们的 k8s 集群，主要是为了预览环境。我非常尊敬的一些朋友对 [Render](https://render.com/) 赞不绝口（我涉猎过，但个人认为 Railway 的环境模型更简洁）。我也偏爱 [Flight Control](https://www.flightcontrol.dev/) 的自带云方法。

对于许多SaaS类型的应用程序来说，用那些工具(指前面提到的工具)你可能已经走得很远了。但是，如果你满足了本文开头列出的三个需求，并且采取了严格的方法，那么不要让任何人告诉你使用Kubernetes还为时尚早。