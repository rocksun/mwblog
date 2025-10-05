
<!--
title: Dapr 携手 WebAssembly：微服务新范式
cover: https://cdn.thenewstack.io/media/2025/09/a96a9fc9-curated-lifestyle-_w5riuf9y-4-unsplash.jpg
summary: Dapr作为CNCF毕业的分布式应用运行时，Dapr 1.16增强多应用工作流和联邦身份支持。它通过易用API和抽象基础设施，简化微服务开发，使开发者能专注于业务逻辑，并获广泛应用。
-->

Dapr作为CNCF毕业的分布式应用运行时，Dapr 1.16增强多应用工作流和联邦身份支持。它通过易用API和抽象基础设施，简化微服务开发，使开发者能专注于业务逻辑，并获广泛应用。

> 译自：[How Dapr and WebAssembly Team Up for Microservices](https://thenewstack.io/how-dapr-and-webassembly-team-up-for-microservices/)
> 
> 作者：B. Cameron Gain

[Dapr](https://dapr.io/) 的分布式应用运行时概念很简单，但启用它却异常复杂（尽管其使用起来很简单）。

根据项目文档，Dapr 被设计为可移植的、事件驱动的运行时，专为在云边缘构建无状态和有状态应用的开发者而设计，同时允许他们使用自己选择的语言和框架。它旨在将构建 [微服务应用](https://thenewstack.io/introduction-to-microservices/) 的最佳实践编码为开放、独立的 [API](https://thenewstack.io/what-is-api-management/)，这些API被称为构建块。

## Dapr 1.16

[Dapr 1.16](https://blog.dapr.io/posts/2025/09/16/dapr-v1.16-is-now-available/) 版本最棒的功能是多应用工作流。Diagrid 的高级开发者倡导者 Marc Duiker 告诉我，它允许开发者指定哪些应用应执行特定的工作流活动。他说，这在活动需要特定硬件（如 GPU）或应在特定地理位置运行时非常重要。

Duiker 说：“此外，我认为 Dapr 对联邦身份的支持在构建安全应用方面非常重要。使用像 [SPIFFE](https://spiffe.io/) [Secure Production Identity Framework For Everyone] 这样强大的开源标准是一个很好的补充，许多企业会欢迎，因为它与所有主要的云服务提供商兼容。”

由于其在分布式系统（包括 Kubernetes）中已被证明的可行性，Dapr 已成为运维团队的最爱。其最受赞赏的功能包括用于强制零信任策略的强大安全机制，以及在整个基础设施中无缝集成的能力。开发团队尤其经常强调其简单易用的 API，这在 [Kubernetes](https://thenewstack.io/kubernetes/) 环境中特别有帮助。Dapr 允许开发者专注于创建解决问题的逻辑，而运行时负责处理基础设施问题，而不是要求开发者掌握复杂的 Kubernetes 概念、命令和基础设施设置。

## CNCF 毕业

最近，由微软主导的 Dapr 项目取得了几个重要的里程碑，包括从 [CNCF](https://cncf.io/?utm_content=inline+mention) (云原生计算基金会) 毕业。这一消息是在今年早些时候的 [KubeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 上宣布的。在活动中，演讲强调了 Dapr 对 [WebAssembly (Wasm)](https://thenewstack.io/webassembly/) 日益增长的使用适应性。在 Kubernetes 环境中，这使得组织能够利用 Wasm 扩展的安全功能、超低延迟以及其他有助于其日益普及的特性。

[CNCF 毕业](https://thenewstack.io/dapr-graduates-cncf-and-connects-to-webassembly/) 本身就是一个重要的里程碑，这得到了近期统计数据的支持，这些数据表明 Dapr 在开发者和运维社区中获得了越来越多的认可和使用。（具体数据未提供，但会突显这一进展。）

该项目最初于 2019 年在微软发布，并于 2021 年 11 月被 CNCF 孵化器接受。自那时以来，Dapr 已发展到来自 400 多个组织的 3,700 多名独立贡献者。它被数万家组织使用，包括 Grafana、FICO、HDFC Bank、SharperImage 和 Zeiss 等。如今，它由隶属于八个组织的 21 名个人维护，他们每季度发布常规版本，包含许多新的开发者 API，包括工作流、密钥、加密、配置管理和大型语言模型（LLM）。CNCF 在一份声明中表示，Dapr SDK 的总下载量已超过 7000 万次，镜像拉取量达到 5000 万次。

## 提供最佳开发者体验

Dapr 集成的项目包括用于[可观测性](https://thenewstack.io/introduction-to-observability/)数据的 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry/)、用于指标的 Prometheus、用于识别和保护服务的 SPIFFE、用于在应用服务之间发送通信的 [gRPC](https://thenewstack.io/grpc-a-deep-dive-into-the-communication-pattern/) 和 Cloud Events。Dapr 控制平面，除其他功能外，还为每个应用部署 Dapr sidecar，托管在 Kubernetes 上，并通过 Helm chart 部署。

在 KubeCon+CloudNativeCon 的演示演讲“下一级能力：用 WASM 和 Dapr 英雄团队增强您的 IDP！”中，Pulumi 的高级解决方案架构师 Engin Diri 展示了如何使用 WebAssembly 提供商 Fermyon 的开源 SpinKube 和 Dapr，结合 KEDA (Kubernetes Event-driven Autoscaling)，来提供“最佳的开发者体验和可能性”，Diri 说。“让我们把 SpinKube 带到下一个层次，并问自己：我们如何帮助开发者更高效，减少对周围一切的思考？”Diri 说。“如果你不熟悉，这个概念的灵感来自法国大革命的‘三巨头’。在我们的案例中，我创建了 SpinKube 三巨头：Dapr、KEDA 和 SpinKube。这就是为什么我认为 Dapr、KEDA 和 SpinKube 构成了完美的组合。”

如上所述，Dapr 为基础设施提供了抽象，因此开发者可以完全专注于创建应用程序。Diri 在他的演讲中解释说，通过 Dapr，Dapr 操作员会自动将 sidecar 机制注入到部署中。他展示了开发者只需要知道存在一个 Pub/Sub 类型的组件。他们不需要知道它是 Kafka、RabbitMQ 还是其他什么，Diri 说。Dapr 提供了一个 SDK 或 API 用于在应用程序内部进行通信，从而消除了不必要的复杂性，Diri 说。

Diri 表示，Dapr 构建在 Actor 模型之上，这使得基于通信模式（即谁与谁通信）来构建代码变得更加容易。这种抽象极其有用。Dapr 还包含多个构建块，如状态管理、发布/订阅（Pub/Sub）、安全和可观测性。开发者无需担心这些组件的底层实现——它可能是 RabbitMQ、Kafka 或其他服务。这些模块化组件可以轻松实现，例如 Key Vault、[AWS](https://aws.amazon.com/?utm_content=inline+mention) Secret Manager 或 HashiCorp Vault 用于秘密管理。Diri 说：“作为一名开发者，我不需要考虑这些复杂性。”