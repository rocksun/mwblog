
<!--
title: Grafana的应用平台：WebAssembly、Kubernetes和API
cover: https://cdn.thenewstack.io/media/2024/05/bb7aadd0-ramiro-mendes-2jmjc_jqbbk-unsplash-1.jpg
-->

Grafana 的功能将得到扩展，以适应存储、多 API 管理等应用程序，并扩展其可观测性功能，以提供事件驱动的功能、Kubernetes 管理和其他功能。

> 译自 [Grafana’s Radical App Platform: WebAssembly, Kubernetes and APIs](https://thenewstack.io/grafanas-radical-app-platform-webassembly-kubernetes-and-apis/)，作者 B Cameron Gain。

[Grafana Labs](https://grafana.com/) 正在扩大其广受欢迎的 [Grafana 面板](https://thenewstack.io/why-you-want-easy-to-setup-grafana-dashboards/) 的范围，以实现全面的可观测性和应用程序支持，超越其当前的插件选项。

正如最近在阿姆斯特丹举行的 [GrafanaCon 2024](https://thenewstack.io/grafana-11-no-need-to-create-promql-queries-for-prometheus/) 中“开源 Grafana 应用平台用户指南”的演讲中所揭示的那样，以及与 [Ryan McKinley](https://www.linkedin.com/in/ryan-mckinley) 的讨论中，Grafana 杰出工程师，插件的覆盖范围以及 Grafana 将如何适应应用程序及其 API 管理是其新推出的 [Grafana 应用平台](https://github.com/grafana/grafana-app-sdk) 的项目中的项目之一。这意味着，一旦该项目实现普遍可用性，Grafana 的功能将得到扩展，以适应存储和多个 [API 管理](https://thenewstack.io/api-management/) 等应用程序，并将扩展其可观测性功能，以提供事件驱动的功能、Kubernetes 管理和其他功能，例如 [GitOps](https://thenewstack.io/i-need-to-talk-to-you-about-kubernetes-gitops/) 与 Argo 和 [Kubectl](https://kubernetes.io/docs/reference/kubectl/) 一起使用。

“目前，我们有一个强大的 [插件生态系统](https://thenewstack.io/saltstack-plugin-oriented-programming-could-help-open-source-woes/)，但它主要关注数据源和面板的关键工具，”McKinley 在他的演讲中说。“对于应用程序，你可以构建东西，但当你将它们与 Grafana 面板集成时，你几乎完全靠自己。”

![Grafana 使用 SDK 的应用程序的“不可知”视图。](https://cdn.thenewstack.io/media/2024/05/b533feaa-capture-decran-2024-05-13-155246.png)

*Grafana 使用 SDK 时对应用程序持“不不可知论”的看法。*

Grafana 目前有一个端点，允许用户拥有一个 [HTTP 端点](https://thenewstack.io/simple-http-load-testing-with-slos/) 来执行“你想要的任何操作，但你无法访问存储或访问控制，”McKinley 说。“我们正在尝试构建一个平台，使你能够构建我们在 Grafana 核心构建的所有正常事物，”他说。“因此，这应该能够构建更动态、更强大的应用程序。”

根据 Grafana 的文档，Grafana 的应用平台提供了一个用于生成代码和项目的 CLI。提供库。通过这种方式，Grafana 的应用平台允许用户集成应用程序，为他们想要与 Grafana 集成的应用程序提供更广泛的可用性和选择。这种集成超出了使用 Grafana 的现状，通常包括选择一个插件列表，然后专门使用这些插件。

![如 GitHub 页面所示，Grafana 应用平台仍处于开发中。](https://cdn.thenewstack.io/media/2024/05/f1c774c9-capture-decran-2024-05-13-155945-1024x122.png)

*正如 GitHub 页面上所示，Grafana 应用程序平台仍处于开发中。*

同时，你目前可能需要对其进行可观测性的其他应用程序在很多方面仍然超出该范围，或者在与 Grafana 面板集成时遇到困难，需要你创建自己的 SDK。一旦应用平台完成，情况就相反了：你可以创建并引入你的应用程序，并且通过平台管理器的设计和重新设计，你可以通过将应用程序与类似于用户从可用插件列表中进行选择时的功能集成到应用程序中。这涵盖了你选择的存储、Kubernetes 集群或其他类型的应用程序管理的可观测性。

在引入其他选择之前，应用平台 SDK 目前处理与存储系统的交互。根据该项目的文档，存储功能涵盖了用于对存储中的资源执行正常操作的简单界面的浮出，以及创建对存储系统中的资源的更改做出反应的控制器/操作员循环。

## Wasm 呢？

在演讲的问答环节中，有人问了一个关于将 Wasm 应用程序与 Grafana 集成的相关问题。“我们绝对在讨论我们在这里有哪些选择，以及哪一个最适合 Wasm，”McKinley 说。资源迁移可能性 [WebAssembly](https://thenewstack.io/webassembly/) 提供的“将非常强大，”他说。

虽然目前重点是 Go 函数，但 McKinley 承认了将 Wasm 纳入资源迁移和简化 API 服务器开发的潜在能力，方法是启用更具声明性风格的更改存储。此外，Ryan 看到了 Wasm 的安全优势，称其“提供了一个强大的安全故事”。

在与 Grafana 首席技术官 [Tom Wilkie](https://uk.linkedin.com/in/tomwilkie) 的离线讨论中，Wilkie 表示，他被利用 WebAssembly 在应用程序中运行不受信任的代码时增加一层隔离的想法所吸引。他们注意到了性能开销，但发现使用 Wasm 编译的 JavaScript 引擎在应用程序中执行 JavaScript 代码的概念是一个引人注目的用例。“你可以在你的应用程序中嵌入浏览器中开始运行不受信任的代码，”Wilkie 说。“这是一个超级有趣的用例。”

然而，在后续对话中，McKinley 说：“我想采用 WebAssembly 方法——但它还没有出现在任何路线图或甚至原型中。”

## 告别“Grafana API Land”

使用应用程序平台的 API 的方法和管理将发生改变。用户不必通过一个自定义 API 管理所有内容，而是可以使用许多 API。McKinley 说，多个 API 被聚合在一个界面下。他解释说，使用你今天的 Grafana 面板，API 插件可用，并且使用你的插件 ID，将提供资源。使用应用程序平台，用户将可以访问单个 API。但通过该 API，在底层，“它将 API 作为一个单独管理的围墙花园单独管理起来，”McKinley 说。

Grafana 高级软件工程师 [Stephanie Hingtgen](https://www.linkedin.com/in/stephanie-hingtgen) 在与 McKinley 的谈话中描述了由此产生的应用程序平台的主要功能将包括对象和 API 的模式和版本控制、对象存储、监视对象、对象准入控制和代码功能。Hingtgen 描述了使用应用程序平台，对象如何存储在持久存储层中，“监视功能”可供用户使用，这意味着存储引擎可以通知操作员，以便“根据它看到的内容采取行动，当存在更改时，将状态引导至我们期望的状态”。Hingtgen 说，这是通过允许用户“在需要时进行同步更改”的钩子来完成的。

## 更多 Kubernetes

McKinley 说，Kubernetes 将为应用程序平台的功能、操作和管理提供底层基础设施，因为它“在底层运行”。但是，如果用户组织尚未采用 Kubernetes，他们将得到支持。

“我们正在使用 Kubernetes 的基本构建块来构建面向用户的应用程序。因此，我们认为与数据计划相比受控内容的许多规则将非常不同，”McKinley 说。“因此，如果你在办公室里不使用 Kubernetes，你的行为不会改变，但我们正在重复使用用于构建 Kubernetes 的标准构建块来构建这个应用程序平台。”

那么，如果你的组织大量投资于 Kubernetes 基础设施，这意味着什么？使用 Grafana 应用程序平台，可以使用标准 Kubernetes 工具来管理部署。你将能够使用 Argo for GitOps 进行 CI+CD，使用 Velero 进行备份，使用 kubectl 进行资源管理。
