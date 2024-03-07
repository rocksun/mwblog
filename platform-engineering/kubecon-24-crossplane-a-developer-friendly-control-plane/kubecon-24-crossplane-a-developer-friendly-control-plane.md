
<!--
title: Crossplane：一款开发者友好的控制平面
cover: https://cdn.thenewstack.io/media/2024/03/8cbb2856-kubecon24-eu.jpg
-->

本月晚些时候前往 KubeCon+CloudNativeCon Europe 的人应在 Crossplane 展位停留，了解此云原生控制平面的最新版本。

> 译自 [KubeCon 24: Crossplane, a Developer-Friendly Control Plane](https://thenewstack.io/kubecon-24-crossplane-a-developer-friendly-control-plane/)，作者 Joab Jackson。

对于那些本月晚些时候前往巴黎参加 [KubeCon+CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)（3 月 19 日至 22 日）的人来说，务必在 [Crossplane 展位](https://thenewstack.io/crossplane-a-package-based-approach-to-platform-building/)（3 月 20 日至 22 日下午在 PP1-B 展位）驻足，了解云原生控制平面的最新版本 [Crossplane 15](https://github.com/crossplane/crossplane/releases/tag/v1.15.0)。

无法前往展位的访客还可以在整个展会期间在 G14 的 [Upbound](https://www.upbound.io/) 展位驻足，或在 3 月 19 日的 [平台工程日](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/co-located-events/platform-engineering-day/) 在四号桌驻足。Upbound 是管理 Crossplane 代码库的公司，该代码库是 [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline-mention) 的开源项目。

在 KubeCon 以及 [联合活动](https://colocatedeventseu2024.sched.com/?searchstring=crossplane&iframe=no) 中，还将有 [多场关于 Crossplane 的演讲](https://kccnceu2024.sched.com/?searchstring=crossplane&iframe=no)。

[Crossplane](https://github.com/crossplane/crossplane) 基于 Kubernetes，是一个专为构建 [云原生控制平面](https://thenewstack.io/cloud-native/) 而设计的框架，但它并不局限于基于 Kubernetes 的资源。它还具有可扩展性，允许平台工程师编排新型基础设施和应用程序。[市场](https://marketplace.upbound.io/) 提供开箱即用的配置，例如适用于 [AWS](https://aws.amazon.com/?utm_content=inline-mention)、[Azure](https://news.microsoft.com/?utm_content=inline-mention) 和 [Google Cloud Platform](https://cloud.withgoogle.com?utm_content=inline-mention) 的配置。

## Crossplane 用于平台工程

没有哪个特定行业是 Crossplane 的早期采用者。相反，用户分布在各个垂直领域。Upbound 的创始工程师兼 Crossplane 维护者 [Jared Watts](https://www.linkedin.com/in/jared-watts-jbw976/) 在接受 TNS 采访时表示，他们有一个共同点，即他们使用云原生资源，以至于他们需要一个专门的控制平面来管理所有这些资源。

Watts 说，Crossplane 可用于“定义一个一致的平台，其中包含组织合规所需的所有策略、配置和所有内容”。“然后为开发者提供一个很好的抽象，以便他们获得所需的设施。”

随着 [平台工程](https://thenewstack.io/year-in-review-platform-engineering-still-run-by-spreadsheet/) 的兴起，这种控制平面非常契合。“Crossplane 是平台工程的重要组成部分，因为它能够定义一个一致的平台，始终以一致的方式管理开发者所需的一切”，Watts 说。

Crossplane 提供的一个优势是它能够处理非 Kubernetes 资源，这对许多可能不愿意将所有资源迁移到云原生基础设施的商店来说是一个日益严重的问题。

Watts 说：“Crossplane 是 Kubernetes 的一个扩展。它教会 Kubernetes 了解所有外部资源，例如云资源和 Kubernetes 之外的全新基础设施。”

## Crossplane 用于开发者

Crossplane 的版本每季度发布一次，最新的 1.15 版本除了其他内容外，还承诺为开发者提供更好的体验。Watts 说。

命令行界面已更新，新增了三个 beta 命令行子命令：

* **crossplane beta validate**：使用 Kubernetes API 服务器的验证库针对架构验证组合。
* **crossplane beta init**：以更简单的方式启动新项目。
* **crossplane beta top**：提供 Crossplane pod 的快速资源利用率检查。

还修改了许多现有的 CLI，所有这些修改都是为了让开发者更轻松地配置云基础设施。

此外，新版本更好地支持组合函数。[组合函数](https://docs.crossplane.io/latest/concepts/composition-functions/) 最初在 1.11 版本中发布，引起了 Crossplane 社区的关注。Crossplane 函数是用于创建模板资源的自定义函数。

为了帮助更轻松地编写组合函数，Upbound 已发布了一个[Python 软件开发工具包](https://docs.crossplane.io/knowledge-base/guides/write-a-composition-function-in-python/) (SDK) 可帮助更轻松地生成这些函数（它们也可以用 [Go 编程语言](https://thenewstack.io/golang-co-creator-rob-pike-what-go-got-right-and-wrong/) 编写）。组合函数现在可以请求 Crossplane 有权访问的其他集群范围资源，例如虚拟私有云 (VPC)。

函数现在具有对 [Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/) 的可观测性支持：Crossplane 现在会针对发送的请求数、收到的响应数和函数运行时长的直方图发出基本函数指标。

## Crossplane：即将毕业的 CNCF 项目

该项目在 CNCF 方面也可能会有好消息。该项目自 2021 年以来一直处于孵化状态，现已申请毕业状态。

“我们正在声明该项目已经成熟、发展、扩展并被人们采用，”Watts 说。“它有人为其做出贡献，它有一个社区。它已经成熟，并且已准备好毕业。”

因此，也许在 KubeCon 上，我们会看到 Crossplane 作为成熟的 CNCF 项目毕业。
