## Fermyon 称 Kubernetes 上的 WebAssembly 现已可行

![Fermyon 称 Kubernetes 上的 WebAssembly 现已可行的特色图片](https://cdn.thenewstack.io/media/2024/03/3fc2b62c-ash-from-modern-afflatus-iirqxpcdq_y-unsplash-1-1024x653.jpg)

巴黎 —

[Fermyon](https://thenewstack.io/fermyon-cloud-save-your-webassembly-serverless-data-locally/) 是一个托管 [Spin](https://www.fermyon.com/spin) 应用程序和其他兼容 [WebAssembly](https://thenewstack.io/can-kubernetes-solve-webassemblys-component-challenges/) 工作负载的平台。Fermyon 现在通过发布开源 [SpinKube](https://spinkube.dev/) 和 [Kubernetes 的 Fermyon 平台](https://developer.fermyon.com/spin/kubernetes) 将 Kubernetes 添加到 Spin 的覆盖范围。

Fermyon 受益于大量开源贡献以及公司自己的研究和开发，以解决 WebAssembly 模块之间的兼容性问题，并使用它们来部署和运行无服务器应用程序，Spin 是一款用于开发和维护无服务器 WebAssembly 应用程序的工具。现在，它已将 Spin 的覆盖范围扩展到涵盖 [Kubernetes](https://thenewstack.io/kubernetes/) 部署。这允许用户和组织使用 Kubernetes 上的兼容 Wasm 工作负载通过 Spin 进行部署。

[@fermyontech] 的 [@matei_radu] 与 [@ralph_squillace] 和 [@technosophos] 向一间座无虚席的会议室展示了 [@kubernetesio] v. 容器上 [#webassembly] 的超轻量级特性。[@KubeCon_] [@thenewstack] [pic.twitter.com/fylL4Pcyn2]
— BC Gain (@bcamerongain)
[2024 年 3 月 21 日]

在 [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 期间，Fermyon 的首席技术官 [Radu Matei](https://www.linkedin.com/in/mateiradu?originalSubdomain=be) 解释并演示了如何使用 [SpinKube](https://spinkube.dev/) 在 Kubernetes 上部署带有轻量级 WebAssembly 模块的应用程序，与较大的容器相比。Fermyon Technologies 的首席执行官 [Matt Butcher](https://www.linkedin.com/in/mattbutcher/)、Fermyon 的首席软件工程师 [Michelle Dhanani](https://github.com/michelleN) 和 Microsoft Azure Core Upstream 的首席项目经理 [Ralph Squillace](https://github.com/squillace) 在他的演讲中加入了 Matei。演讲中还讨论了 WebAssembly 在 Kubernetes 上的未来以及扩展 WebAssembly 工作负载的代理选项，“从零扩展到数千个，然后瞬间再缩减回来”。

主要功能之一是它提供了一种简便的方法，可以像预期的那样在众多异构环境中部署和分发 Wasm。

也许你可以将此视为 [无服务器](https://thenewstack.io/serverless/) Kubernetes — 现在你可以使用 Spin 运行 Web 模块，并同时将其部署到一个或多个集群。换句话说，这个想法是，你可能不太关心你正在使用 WebAssembly 的低功耗但功能强大的模块，而更关心你可以通过单击一次同时将模块部署到 Kubernetes 上的众多端点。

虽然我们尚未测试 SpinKube，但计划在不久的将来进行测试，它似乎提供了多种功能。

首先是 SpinKube 如何设计为简化 Kubernetes 部署。Fermyon 表示，在众多声称简化或提供单一面板玻璃 Kubernetes 平台的平台中，SpinKube 也可以提供一种在 Kubernetes 上进行部署的简化途径，而复杂性大大降低。

我想在很多情况下，运维团队已经设置了 Kubernetes 和/或 Kubernetes 上的无服务器应用程序，[Amazon Elastic Kubernetes Service (EKS)](https://thenewstack.io/kubernetes-as-a-service-using-amazon-eks/)、Azure 等。开发人员只需使用 Spin 的部署工具即可同时将他们的应用程序部署到众多端点，而无需过多地关注 Kubernetes 在底层如何工作。

其次，容器（在公告中没有太多描述）可能会与 SpinKube 如何通过 WebAssembly 部署应用程序的方式产生一些重叠。以一种消耗更少电力的方式，同时绕过容器的结构，因为 Wasm 模块提供了部署的管道。它很可能在 Kubernetes 上以无服务器的方式完成。一旦我们更多地了解 SpinKube 和 [Kubernetes 的 Fermyon 平台](https://developer.fermyon.com/spin/kubernetes) 的机制，看看它如何发挥作用将会很有趣。

在 Kubernetes 上运行 Wasm 特别有趣，因为它为开发人员提供了与他们从 Fermyon Spin 了解的相同的便捷部署流程，
## WebAssembly 在 Kubernetes 和无服务器中的作用

[托斯滕·沃尔克](https://www.linkedin.com/in/torstenvolk)，[企业管理协会 (EMA)](https://www.enterprisemanagement.com/) 的分析师，告诉 The New Stack。与此同时，“现有的 Kubernetes 运维人员可以管理、移动和优化 WebAssembly 应用以及标准应用容器，”沃尔克说。“无需深入了解 Kubernetes 部署的细节，可以为开发人员节省大量时间，而运维人员可以专注于基础设施管理，而无需担心破坏基于 WebAssembly 的应用。这是一个双赢的局面。”

在服务器端，WebAssembly 成为一项引人注目的技术的原因在于它能够在几秒钟内从零扩展到数百万个实例，然后再返回，布切告诉 The New Stack。“在 Fermyon，我们已经能够实现极高的密度，在 Fermyon 云集群中的每个节点上运行三千个用户应用，”布切说。“一次又一次，工程师们询问我们如何在他们的 Kubernetes 集群中使用 WebAssembly 并获得一些同样的好处。这就是我们为 Kubernetes 构建 SpinKube 和 Fermyon Platform 的原因。我们的目标是在降低 Kubernetes 集群运营成本的同时，提供性能和密度。”

对于无服务器，WebAssembly 是一种“构建下一代无服务器的使能技术——比 AWS Lambda 更快、更便宜，”布切说。“通过将其无缝集成到 Kubernetes 中，我们使平台工程师能够将基于 WebAssembly 的无服务器与基于容器的服务并行集成，”布切说。“充分利用 Kubernetes 配置的所有好处——从安全性到可观察性再到开发——同时获得下一代超快速基于事件函数的好处。”

## Fermyon Platform for Kubernetes

Fermyon Platform for Kubernetes 由 SpinKube 提供支持。SpinKube 结合了 Spin 运算符、containerd Spin shim 和运行时类管理器（以前称为 KWasm）开源项目，以及来自 Microsoft、SUSE 和 Liquid Reply 以及 Fermyon 的贡献。Fermyon 表示，通过在 Wasm 抽象层运行应用程序，SpinKube 使应用程序开发人员能够轻松地将无服务器 WebAssembly 应用程序部署到 Kubernetes 中，从而有效利用节点资源，冷启动速度低于一毫秒。

Fermyon 传达的 Fermyon Platform for Kubernetes 功能包括：

- 密度提高 50 倍以上：Fermyon 表示，Fermyon Platform for Kubernetes 每个 Kubernetes 节点可以提供 5,000 多个无服务器应用程序，并具有自动缩放到零和亚毫秒级冷启动时间（其理念是增加密度可以降低成本并为每个节点增加更多容量）。
- 改善开发人员体验：使用 WebAssembly 组件模型，几乎没有 Kubernetes 专业知识的开发人员可以轻松构建和部署跨平台应用程序。
- 简化 Kubernetes 实施：通过将 Spin WebAssembly 应用程序部署到 Kubernetes，Fermyon 能够在托管提供商之间实现托管平台的标准化。
- Fermyon 表示，SpinKube 的创建旨在简化在 Kubernetes 上开发、部署和操作 Wasm 工作负载的体验，同时将 Spin 与 [runwasi](https://github.com/containerd/runwasi) 和 KWasm 开源项目结合使用。
- 根据 SpinKube 的文档，组织可以使用 WebAssembly 来处理其工作负载，以便：
  - 与容器镜像相比，工件的大小明显减小。
  - 可以通过网络快速获取工件并更快地启动（而 Fermyon 指出，仍需要实施“一些优化”来缩短工作负载的启动时间）。
  - 在空闲时间需要更少的资源。
  - 得益于 Spin 运算符，可以集成 Kubernetes 原语（DNS、探测、自动缩放、指标以及更多云原生和 CNCF 项目）。

Spin 运算符监视 Spin 应用自定义资源并在 Kubernetes 集群中实现所需状态。此项目的基石是使用 Kubebuilder 框架构建的，并包含 Spin 应用自定义资源定义 (CRD) 和控制器。

Fermyon 在 [Nomad](https://thenewstack.io/conductor-why-we-migrated-from-kubernetes-to-nomad/) 上运行，根据 Ferymon 文档，为了部署场景，将首先配置和安装此软件，同时使用 [Consul](https://thenewstack.io/3-consul-service-mesh-myths-busted/)。之后，组成 Fermyon 的组件将以 Nomad 作业的形式部署，包括 Bindle 服务器、[Traefik](https://thenewstack.io/traefik-proxy-v3-adds-webassembly-and-kubernetes-gateway-api-support/) 作为反向代理/负载均衡器和 [Hippo](https://docs.hippofactory.dev/)，用于管理基于 Spin 的应用程序的 Web UI。
根据一份声明，在 Microsoft 的 Azure Kubernetes 服务上将 Spin WebAssembly 与 SpinKube 结合使用，帮助蔡司集团实现了更快的可扩展性，并在无需大幅改变其运营态势的情况下实现了更高的密度。

“通过此举，我们能够处理数万个订单的 Kubernetes 批处理，并在不影响性能的情况下将计算成本降低了 60%。”蔡司集团杰出架构师 [Kai Walter](https://github.com/KaiWalter) 说。

“我们很高兴看到 WebAssembly 成为 Kubernetes 中的一流工作负载。SpinKube 和 Fermyon Platform for Kubernetes 将重塑我们在 Kubernetes 中执行高性能计算的方式。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。