
<!--
title: Dapr从CNCF毕业并连接到WebAssembly
cover: https://cdn.thenewstack.io/media/2024/11/330ffd42-katelyn-perry-wtzwmhmkgoi-unsplash.jpg
-->

由微软领导的 Dapr 项目已经取得了几个重要的里程碑，包括从 CNCF 毕业以及越来越多地使用 WebAssembly。

> 译自 [Dapr Graduates CNCF and Connects to WebAssembly](https://thenewstack.io/dapr-graduates-cncf-and-connects-to-webassembly/)，作者 B Cameron Gain。

盐湖城 —— 最近，由微软领导的Dapr项目取得了几个重要的里程碑，包括从云原生计算基金会（CNCF）毕业。这一消息是在KubeCon + CloudNativeCon大会上宣布的。在大会上，讨论强调了Dapr对日益增长的WebAssembly（Wasm）使用的适应性。在Kubernetes环境中，这使得组织能够利用Wasm的扩展安全特性、超低延迟以及其他有助于其日益被采用的特性。

Dapr，即分布式应用运行时，因其在分布式系统中的可行性而受到运维团队的青睐，包括Kubernetes。其中最受赞赏的特性是强大的安全机制，用于执行零信任政策，以及它能够无缝整合到整个基础设施中。开发团队尤其强调其简单易用的API，这在Kubernetes环境中特别有用。Dapr允许开发者专注于创建解决问题的逻辑，而运行时处理基础设施问题，而不是要求开发者掌握复杂的Kubernetes概念、命令和基础设施设置。

## 关键里程碑

CNCF毕业本身就是一个重要的里程碑，这一成就得到了近期统计数据的支持，数据显示Dapr在开发者和运维社区中的接受度和使用量不断增长。（具体统计数据未提供，但将强调这一进展。）

该项目最初于2019年在微软发布，并在2021年11月被接受进入CNCF孵化器。从那时起，Dapr已经发展到来自400多个组织的3700多名个人贡献者。它被成千上万的组织使用，包括Grafana、FICO、HDFC Bank、SharperImage、Zeiss等。今天，它由21名与八个组织有关联的个人维护，他们每季度发布常规版本，并引入了许多新的开发者API，包括工作流、机密、密码学、配置管理和LLMs。Dapr SDKs总共有超过7000万次下载，其中镜像拉取量达到5000万次，CNCF在一份声明中说。“

Dapr的API方法结合其快速更换底层基础设施的能力，无论是存储、消息代理还是机密存储，使任何开发者都能够应对构建微服务架构的复杂性并提供业务价值，”Dapr维护者和指导委员会成员，以及Diagrid的首席执行官和联合创始人Mark Fussell在一份声明中说。


## 集成的项目

Dapr集成的项目包括用于可观测性数据的OpenTelemetry、用于指标的Prometheus、用于识别和保护服务的SPIFFE（每个人都适用的安全生产身份框架）、用于应用程序服务之间发送通信的gRPC和CloudEvents。Dapr控制平面，除了其他能力外，还为每个应用程序部署Dapr边车，并托管在Kubernetes上，使用Helm图表进行部署。

“在当今竞争激烈的环境中，组织能够快速交付可靠和可扩展的应用程序比以往任何时候都更加重要，”CNCF的CTO Chris Aniszczyk在一份声明中说。“Dapr为开发边缘和云原生应用程序提供了全面的解决方案，节省了开发者宝贵的时间，并使他们能够专注于创新。”

![](https://cdn.thenewstack.io/media/2024/11/d0309406-capture-decran-2024-11-21-203850-1024x555.png)

Dapr 的 Wasm sidecar 也越来越受欢迎。自 Dapr 诞生以来，它的设计初衷就是让开发者专注于构建应用程序，而无需担心底层基础设施。[Engin Diri，](https://github.com/dirien) [Pulumi](https://www.pulumi.com/) 的高级解决方案架构师，在 [Rejekts](https://cloud-native.rejekts.io/) 和 KubeCon + CloudNativeCon 期间告诉我，加入 Wasm 后，目标“也是为了让周围的开发者体验更轻松”。

Dapr 有助于改善开发者体验，因为它可以用来创建一个“围绕公司选择的任何实现”的抽象层，Diri 说。“开发团队不需要担心它背后的具体技术。例如，他们只需要一个发布或订阅事件的方法，就可以对消息做出反应，”Diri 说。“这就是很酷的地方：开发者可以专注于尽快交付价值，而无需担心底层实现，他们不必考虑他们使用的是 [Kafka](https://thenewstack.io/top-10-tools-for-kafka-engineers/) 还是 [RabbitMQ](https://thenewstack.io/rabbitmq-is-boring-and-i-love-it/)，因为 Dapr 抽象了这些细节。使用 Dapr，你只需通过 API 获取输入，仅此而已。”

Dapr 可以使 WebAssembly 更轻松，WebAssembly 可以使使用 @daprdev 的部署比容器基础设施更快。

> 今天， @PulumiCorp 的 Engin Diri 在 #WasmCon 上的演讲：Next-Level Powers: Enhance Your IDP with the WASM and Dapr Hero Team-Up! [@thenewstack](https://twitter.com/thenewstack) [pic.twitter.com/SQl7YIAzxK] — BC Gain (@bcamerongain) [November 12, 2024]


在 KubeCon + CloudNativeCon 的演示演讲“Next-Level Powers: Enhance Your IDP with the WASM and Dapr Hero Team-Up!” 中，Diri 展示了如何使用 WebAssembly 提供商 [Fermyon](https://www.fermyon.com/?utm_content=inline+mention) 的开源 [SpinKube](https://thenewstack.io/why-platform-engineers-are-embracing-webassembly-for-serverless/) 和带有 KEDA（Kubernetes Event-driven Autoscaling）的 Dapr 来提供“最佳开发者体验和可能性”，Diri 说。“让我们将 SpinKube 提升到一个新的水平，并扪心自问：我们如何才能帮助开发者更有生产力，更少地考虑周围的一切？”Diri 说。“如果你不熟悉，这个概念的灵感来自法国大革命的‘三头政治’。在我们的例子中，我创建了 SpinKube 三头政治：Dapr、KEDA 和 SpinKube。这就是为什么我认为 Dapr、KEDA 和 SpinKube 构成了完美的三剑客。”

## 专注于应用程序

如上所述，Dapr 提供了对基础设施的抽象，因此开发者可以完全专注于创建应用程序。Diri 在他的演讲中解释说，使用 Dapr，Dapr operator 会自动将 sidecar 机制注入到部署中。他展示了开发者只需要知道存在一个 Pub/Sub 类型的组件。他们不需要知道它是 Kafka、RabbitMQ 还是其他东西，Diri 说。Dapr 提供了一个 SDK 或 API 来在应用程序内进行通信，消除了不必要的复杂性，Diri 说。

![](https://cdn.thenewstack.io/media/2024/11/0df46fd0-capture-decran-2024-11-21-203930-1024x560.png)

Dapr 建立在 actor 模型之上，这使得根据通信模式（即谁与谁通信）构建代码更容易，Diri 说。这种抽象非常有帮助。Dapr 还包含多个构建块，例如状态管理、[Pub/Sub](https://thenewstack.io/publish-subscribe-introduction-to-scalable-messaging/)、安全性和可观察性。开发者无需担心这些组件的底层实现——它可能是 RabbitMQ、Kafka 或其他服务。模块化组件可以轻松实现，例如 Key Vault、[AWS](https://aws.amazon.com/?utm_content=inline+mention) Secret Manager 或 HashiCorp Vault 用于密钥管理。“作为一名开发者，我不需要考虑这些复杂性，”Diri 说。

“通过结合这些部分——抽象基础设施、事件驱动扩展和用于高效 WASM 工作负载的 SpinKube——你将获得一个高效的系统，”Diri 在演讲中说。

