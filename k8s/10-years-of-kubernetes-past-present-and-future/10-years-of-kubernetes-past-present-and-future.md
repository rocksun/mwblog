
<!--
title: Kubernetes十年：过去、现在和未来
cover: https://cdn.thenewstack.io/media/2024/06/cc7e67b0-music-8261454_1280.png
-->

Matt Butcher 回顾了事情的开端、Kubernetes 如何走向成熟，以及它如何展示了扩展到 WebAssembly 运动的潜力。

> 译自 [10 Years of Kubernetes: Past, Present, and Future](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/)，作者 Matt Butcher。

今年，[Kubernetes](https://thenewstack.io/kubernetes/) 迎来了十周年。作为一名从社区早期就参与其中的开发者，我借此机会回顾了 Kubernetes 的发展历程、走向成熟的过程，以及它现在如何展示出扩展到 [WebAssembly](https://thenewstack.io/4-big-developments-in-webassembly/) 运动的潜力。

而且，由于我是 Swiftie，我按照我最喜欢的音乐家的风格将这些内容分成了几个时代。

## 时代 1：Kubernetes 还比较简单

首先，是 [Borg](https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/)。在 2010 年代初期，我在 Google 短暂工作过一段时间，然后离开加入了一家名为 Deis 的 PaaS 初创公司。我在 Google 的 Nest 部门（生产恒温器和火灾警报器）。与 Google 其他部门不同，Nest 当时使用 Apache Mesos 和 Apache Zookeeper 来编排其虚拟机。但是，我还使用 AppEngine 构建了一个内部应用程序。通过它，我接触到了 Google 内部 LXC 容器调度程序。Borg 非常强大。它在全球范围内扩展。并且需要数百名工程师来维护。有一次，我考虑过加入 Borg 团队之一。相反，我离开了 Deis，去构建当时巨头 Heroku 的开源替代品。

Deis 是 [Docker](https://thenewstack.io/ebooks/docker-and-containers/the-docker-container-ecosystem/) 容器领域的早期参与者。团队成员致力于 Docker 网络，并为 CoreOS 的工具做出了大量贡献。但我们正在寻找一个强大的编排系统，可以简化我们 PaaS 的调度代码。当 [Google 开源 Kubernetes](https://thenewstack.io/a-kubernetes-documentary-shares-googles-open-source-story/) 时，我感到非常兴奋。它拥有 Borg 的所有优点，但包装得更简单。

简单。这是我当时用来描述 Kubernetes 的词。

它 *简单*，因为我无需描述生命周期或运行某项内容的一组程序指令，只需 *声明* 应该运行什么。Kubernetes 接受该声明并使其生效。

它很简单，因为我无需编写代码，只需编写几十行 YAML（当时，确实只有几十行）。然后，我只需使用一个简单的 CLI 上传该 YAML。

而且它很简单，因为只有几种 Kubernetes 对象。Pod、ReplicationController、服务和机密是我日常真正需要的。

在 Deis，我们在 Kubernetes 上重新构建了我们的整个 PaaS，在此过程中构建了 Helm 并创建了 Kubernetes 儿童插图指南。在容器生态系统中，我们都在快速发展（并打破常规）。我仍然记得 Kubernetes 团队宣布可以运行 [1000 节点集群](https://kubernetes.io/blog/2016/03/1000-nodes-and-beyond-updates-to-kubernetes-performance-and-scalability-in-12/) 的那一天。第一个 KubeCon 在一个酒店宴会厅举行。CNCF 成立为 Kubernetes IP 的中立管理者。当 [Brendan Burns](https://www.linkedin.com/in/brendan-burns-487aa590/) 离开 Google 加入 Microsoft 以创建专门的 Kubernetes 团队时，我确信该生态系统已经跨越了一个重要的门槛。

Kubernetes 即将取得成功。

## 时代 2：成长中的烦恼和收益

虽然从某种意义上说，Kubernetes 早期的稀疏性和简单性很有吸引力，但它也存在局限性。要在生产中运行微服务，需要其他功能。ReplicationController 让位于 ReplicaSet，后者促进了部署、DaemonSet、有状态集和其他更高级别的控制功能。ConfigMap 加入机密，Volume 系统不断发展和成熟。自动伸缩器、作业和 RBAC 进入了 Kubernetes 核心。第三方资源让位于更灵活的自定义资源描述 (CRD)。CRD 已成为扩展 Kubernetes 资源（类型）系统的标准方式。

曾经简单的系统很快变得复杂。但并非没有道理。如果 Kubernetes 要在曾经仅为 Borg 保留的级别上实现编排的民主化，它需要促进各种配置、用例和安全策略。

并非所有更改都是技术性的。Kubernetes 周边的生态系统也发生了变化。CNCF 发展成为一个成熟且范围广泛的基金会。从 TOC 到 SIG，再到 TAG，以及对项目孵化、沙盒和毕业的精心构建，CNCF 为生态系统增加了所需的严谨性。至于 Helm，我们“离开”了 Kubernetes 项目（我们曾经是一个子项目），并成为最早的 CNCF 沙盒项目之一，这使我们能够拥有自己的发布节奏、构建基础设施和治理策略。这一切都得益于 CNCF 不断壮大的流程。容器运行时空间中的一些动荡导致了开放容器计划 (OCI) 的创建，该计划已发展成为一个保护容器规范核心的标准机构。

当时，每一次变化都让人感觉动荡不安。我们都意识到，如果 Kubernetes 要赢得当时我们称之为“编排器之战”，它还有很长的路要走。Apache Mesos、CoreOS Fleet、Docker Swarm 和 HashiCorp Nomad 都在 [ 与 Kubernetes 展开激烈的竞争](https://thenewstack.io/configuration-management-orchestration/)。即使 Mesos 是现任者，Kubernetes 也在技术方面和社区发展方面超越了它（和其他竞争对手）。声明式配置的想法引起了积极的共鸣，很快 Kubernetes 就出现在一家又一家公司中。

## 时代 3：稳定性与创新

每个成功的开源项目都会遇到一个时刻，即开发功能的压力与对稳定性的需求正面冲突。在项目的早期，开发人员可以以改进的名义进行重大更改，而用户会接受甚至支持这种更改。在这些早期阶段，即使这意味着痛苦的迁移，我们也渴望改进。

但随着软件对组织运作变得至关重要，对重大更改的容忍度也在下降。稳定性是一个原因，因为重大更改会导致代价高昂的停机时间。此外，随着越来越多的公司、团队和项目采用该技术，为每次新版本的软件重建所有工作负载在资金和时间上都变得非常昂贵。

Kubernetes、Helm 和其他项目开始将稳定性置于速度之上。虽然这引起了希望合并和发布其功能的工程师的大量抱怨，但它促进了 Kubernetes 在企业中的地位。

然而，这种方法的一个缺点是，当添加新功能时，它不能破坏现有行为。这更复杂。Kubernetes 的代码库规模不断扩大，YAML 清单格式变得更加冗长。在 Helm 开发的早期，我们在 Kubernetes 中遇到了一个有趣的限制：任何一个 Kubernetes 清单的最大大小为 1M。我以比尔·盖茨的方式评论道，“是的，但没有人会需要一个 1 兆字节的 Helm 图表！它们只是 YAML 文件！”但随着 Kubernetes YAML 变得越来越复杂，Helm 的功能也变得越来越复杂，我们达到了 1M 的限制。我们添加了图表压缩，然后在几年后再次达到限制。有一天，我在 LinkedIn 上看到一位工程师将他们的头衔列为“Helm 图表开发人员”。震惊之余，我意识到，即使我在构建 Helm 时认为它是一个简单的系统，它也已经发展成为一个需要工程师培养特定技能的工具。

2019 年，我开始绝望，认为 Kubernetes 正在发展成为一个庞然大物，即使是参与其中的人也很快会无法理解它。即使在某个时候有发生这种情况的危险，我们似乎已经安全地解决了这个问题。得益于技术领导力，Kubernetes 调整了新的方向。开发人员不再专注于添加功能，而是专注于构建可扩展性机制。出现了可靠的 CRD 模式。控制平面变得更加灵活。随着策略控制等企业功能的巩固，它们以一种允许各种扩展点的方式进行巩固。简而言之，Kubernetes 通过允许其他人选择他们希望以附加组件的形式容忍复杂性的位置，从而阻止了内部复杂性。

这一举措挽救了 Kubernetes。它也为超越容器的未来奠定了基础。

## 时代 4：未来是 Wasm

Kubernetes 的一个关键灵活点是容器运行时。Kubernetes 曾经需要 Docker 守护程序，但现在只需要一个符合 Kubernetes 生命周期预期的调度系统。Containerd、CRI-O 和其他低级容器工具将曾经单一的容器运行时分解为功能单元。这是通往未来的门户。

WebAssembly——缩写为 Wasm（与“awesome”同音）——最初是一种字节码格式，旨在在 Web 浏览器中与 JavaScript 一起运行。它的承诺是更强大的客户端编码。有了 Wasm，我们将能够编译旧 C 库，然后从 JavaScript 访问它们。我们能够将高性能特性（如矢量数学）委托给比 JavaScript 更合适的语言。而且，我们将在一个安全沙箱中获得所有这些特性，该沙箱甚至可以保护 JavaScript 运行时免受恶意字节码的侵害。

2018 年，我在 Microsoft 的团队花费了一段时间来维护 Helm、Brigade 和其他 CNCF 项目，还有一段时间试图解决容器生态系统中的新问题。我们非常想解决的一个问题与无服务器函数（如 AWS Lambda）有关。对于我们来说有两点很明确：

- 为无服务器函数提供支持的现有技术并不理想。虚拟机和容器设计都假定访客工作负载将运行数小时、数天或数月。启动时间并非重大考虑因素，因为启动相对不太频繁。
- 最流行的无服务器函数实现（AWS Lambda、Azure Functions、CloudFlare Workers 等）由大型公司负责运营并运行在 Kubernetes 之外

第二点，我们在微软反复听到，这对那些以 Kubernetes 为标准的企业来说是一种烦恼。正如一位平台工程师曾经对我说：“我们有这个整洁安全的 Kubernetes 集群来托管我们的服务器工作负载，以及这个由一次性策略控制、服务和进程组成的弗兰肯斯坦怪物来支持我们的 AWS Lambdas。”

Wasm 可能会在某种程度上取代容器的风险（或理由）很小。WebAssembly 的优点——快速的启动时间、较小的二进制文件大小和快速的执行速度——非常适合没有长期运行的服务器进程的无服务器工作负载。但 WebAssembly 中没有任何一个能比在容器中封装的长期运行服务器进程更加出色。事实上，情况恰恰相反：目前，如果没有对代码（或 WebAssembly 运行时本身）进行实质性更改，几乎没有服务器可以编译成 WebAssembly。

谈及无服务器函数，WebAssembly 以其亚毫秒的冷启动、接近本地的执行速度和强健的安全沙箱成为理想的计算层。

如果 WebAssembly 不能取代容器，则我们的设计目标应该是补充容器。在 Kubernetes 中运行 WebAssembly 应涉及与现有 Kubernetes 功能的最深入可能的集成。这就是 SpinKube 的用武之地。SpinKube 封装了一组由 Microsoft、Fermyon、Liquid Reply、SUSE 等创建的开源工具，将 WebAssembly 支持直接集成到 Kubernetes 中。WebAssembly 应用程序可以使用机密、config map、卷装载、服务、sidecar、网格等。而且，这是开箱即用的。不仅如此，容器和 WebAssembly 还可以并排在同一个 Pod 中运行。一个应用程序可以拥有一个长期运行的服务器进程（例如）在一个容器中执行，同时少数 WebAssembly sidecar 以无服务器函数的形式执行。以前从未有过一种方法可以在一个操作单元中无缝地混合 serverless 和 server 工作负载。

由于 WebAssembly 所需的系统资源远少，Kubernetes 集群中的单个节点可以运行数百甚至数千个 WebAssembly 应用。虽然你自己的集群也许永远不需要那么多应用，但使用这些精简的应用后，你的 Kubernetes 集群肯定会物超所值，同时群集所需的运算能力（以及集群成本）也会大幅下降。

这个故事中令人印象深刻的是，Kubernetes 本身就是 WebAssembly 得以取得巨大成功的理由。过去几年为使 Kubernetes 具有可扩展性、可插入性和高度可配置性所作出的努力获得了回报，即使是一个全新的运行时也能在默认的容器运行时旁边安插！

## 超越目标

正如我之前所述，粗略浏览一下软件知识便能教会我们一些关于项目演变的深刻道理。好的软件项目能达到最初的设计目的。伟大的项目则超越了预期。TCP/IP 最初仅用于美国政府内部通信。HTML最初设计用于传输物理论文。JavaScript最初用于弹出浏览器警告和与 Java Applets 通信。

伟大的软件项目超越了它们的最初设计意图。从一开始，Kubernetes 社区就清楚地理解我们共同构建的内容：

自Kubernetes社区成立以来，我们对共同构建的目标有着一个明确的理解：

Kubernetes是一个为Docker容器提供的开源编排系统。它处理计算集群中节点上的调度，并且主动管理工作负载，以确保其状态与用户声明的意图相符。使用“标签”和“Pod”的概念，它将构成应用程序的容器分组到逻辑单元中，以便于管理和发现。

该项目肯定实现了这一早期目标，并且现在已经超越了这一目标。

Kubernetes 起初是一个 Docker 调度程序。WebAssembly 则是一种浏览器运行时。我们亲眼目睹了这两个项目如何飞速超越其最初的设计。它们每个都展现出作为一项伟大技术的潜质。两者的融合将会开辟分布式计算的新天地。

