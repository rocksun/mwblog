<!--
title: 十年磨一剑：werf，Kubernetes 软件交付的进化之路
cover: https://cdn.thenewstack.io/media/2020/10/4ce6790a-werf.png
summary: werf 是一个拥有十年历史的云原生一体化 CLI 工具，专注于自动化容器镜像的构建与部署至 Kubernetes。它整合了 Git、Docker、Helm 等主流技术，简化 DevOps 流程。作为 CNCF 沙盒项目，werf 及其子项目在开源社区持续发展，被全球广泛采用，体现了内部工具开发与开源奉献的价值。
-->

werf 是一个拥有十年历史的云原生一体化 CLI 工具，专注于自动化容器镜像的构建与部署至 Kubernetes。它整合了 Git、Docker、Helm 等主流技术，简化 DevOps 流程。作为 CNCF 沙盒项目，werf 及其子项目在开源社区持续发展，被全球广泛采用，体现了内部工具开发与开源奉献的价值。

> 译自：[A decade of werf, a software delivery tool for Kubernetes](https://thenewstack.io/a-decade-of-werf-a-software-delivery-tool-for-kubernetes/)
> 
> 作者：Dmitry Shurupov

各种云原生项目正在庆祝它们的第一个十年。虽然有一些显而易见的大牌，例如 Kubernetes 本身、Helm 和 Cilium，但生态系统要广泛得多，也包括一些存在已久的知名度较低的工具。我从 [werf 项目](https://werf.io/)成立之初就参与其中，至今已有十年，我想分享它的故事，为当前云原生世界的更广阔图景做出贡献。

什么是 [werf](https://thenewstack.io/werf-automates-kubernetes-based-gitops-workflows-from-the-command-line/)？它基本上是一个固执己见、一体化的命令行界面 (CLI) 工具，用于构建容器镜像并将其部署到 Kubernetes。此时，你可能会想，既然今天我们已经有这么多执行类似任务的工具，为什么还需要它呢？问得好！为了回答这个问题，我建议深入了解项目的历史，以理解它的独特之处、其背后的原因和演变。

werf 起源于一家专注于 Linux 的 DevOps 服务提供商，该公司面临为各种客户自动化众多容器编排例程的挑战。这发生在 2015-2016 年，当时容器已广泛使用，甚至 [Kubernetes 也已存在](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/)，尽管它尚未非常流行。

当我们谈论将应用程序作为容器运行时，工程师们对它们做的第一件事是什么？他们通过调用 `docker build` 和其他几个命令来构建镜像。这正是 werf 的起点：为这些操作制作一个封装器，并通过嵌入多项增强功能来改进此过程，例如不同的构建阶段、智能缓存、添加第三方工件，甚至支持 Chef。（同样，那是在此类配置管理工具广泛使用的时候，这种集成对于运维世界来说似乎很自然。）

重要的是，它不是一种通用类型的封装器。从一开始，它就是一个强烈专注于自动化成熟工作流的工具，因此强制执行关于如何构建、标记镜像的特定观点。虽然这种方法是固执己见的，但它基于真实世界的基础设施运营经验，并非针对单一公司，而是针对不同行业和规模的众多客户。促进容器编排的相同最佳实践是创建 werf 的真正意义，这种思想自那时起一直延续。

werf 获得的下一个重要功能是部署。构建容器镜像后，你希望在某个环境中运行它，对吗？那时（2017 年），很明显 Kubernetes 将是运行容器化工作负载的首选平台，并且 Helm 也已经存在。因此，werf 使用 Helm 来实现向 Kubernetes 的部署。这是项目的另一个核心思想：尽管对你如何完成工作持固执己见的态度，但你用来实现这一目标的基础技术都是主流的：git、Docker、Helm、Kubernetes……在某种程度上，werf 成为了这些技术的“粘合剂”——例如，你可以执行一个命令 `werf converge`，来（重新）构建你的应用程序并（重新）部署它到 Kubernetes。

多年来，werf 中添加了其他重要的功能和最佳实践，例如并行构建、基于内容的镜像标记、部署期间的高级资源跟踪、清理容器注册表的复杂方法、用于分发发布工件的捆绑包、GitLab CI/CD 和 GitHub Actions 的即用型集成，以及用于封闭构建的所谓 [Giterminism](https://werf.io/docs/v2/usage/project_configuration/giterminism.html) 等等。

最终，werf 演变成了一个一体化的 CLI 工具，集成了许多功能，经过其创建者以及后来许多其他公司多年的生产使用验证。项目背后的另一个基本思想促成了其日益增长的采用。

werf 的创建者积极参与开源，因为他们的整个服务业务都建立在部署、配置和维护 Linux 服务器以及网络服务所需的无数其他开源软件之上。这使得 werf 从一开始就因意识形态和实际——或者说专业——原因而开源并在 GitHub 上可用。

有趣的是，在 werf 中实现许多功能最终促成了其他开源项目的创建，这些项目本身也证明是有用的。其中一些例子包括：

*   **[Nelm](https://github.com/werf/nelm)** 是一个 Helm 分支，它在许多方面增强了其功能，包括部署期间的高级资源跟踪、部署资源的灵活排序、改进的 CRD（自定义资源定义）管理和部署规划。如今，Nelm 不仅作为 werf 中的部署引擎使用，还被许多用户作为独立的 CLI 工具使用。
*   **[Trdl](https://github.com/werf/trdl)** 是一种从 Git 仓库安全地向最终用户交付软件更新的解决方案。它是安装/调用 werf 二进制文件的默认和首选方式。
*   **[Kubedog](https://github.com/werf/kubedog)** 是一个用于在部署期间监视和跟踪 Kubernetes 资源的库。Nelm 使用它来跟踪资源，其他一些工具也受益于利用它。
*   **[Lockgate](https://github.com/werf/lockgate)** 是一个用于 Go 语言的分布式锁定库。

鉴于越来越多的用户采用 werf 来满足他们的需求，并愿意为项目提供更强的保证，我们决定将其捐赠给一个值得信赖的基金会。2022 年底，werf 成为了 [云原生计算基金会](https://cncf.io/?utm_content=inline+mention) (CNCF) 沙盒项目，向更广泛的技术社区表明此工具将保持开源，并且不会由单一供应商拥有。

在过去的十年里，云原生生态系统发生了显著演变，为软件工程师提供了令人印象深刻的各种工具和解决方案。与此同时，werf 也经历了一个漫长的发展过程，从一个简单的封装器发展成为一个全面的解决方案。作为一个固执己见且一体化的工具，它如今主要专注于特定的用例，例如其他 DevOps 机构、希望确保在 Kubernetes 中交付软件的严格规则的组织，以及一些喜欢 werf 所倡导原则的用户。（顺带一提，或许 werf 的子项目 Nelm 具有更大的大规模采用潜力。）尽管如此，werf 如今在全球至少 18,000 个项目中被积极使用，并保持着强劲的开发步伐，不断为其现有和潜在用户添加独特功能。

对我而言，werf 的故事展示了对内部工具的热情、持续开发，加上对开源的奉献，如何能够造福更广泛的工程社区，甚至可能激励他人。