# Dapr Graduates from CNCF and Connects to WebAssembly

![Dapr Graduates from CNCF and Connects to WebAssembly](https://cdn.thenewstack.io/media/2024/11/330ffd42-katelyn-perry-wtzwmhmkgoi-unsplash-1024x683.jpg)

Salt Lake City — The Microsoft-led [Dapr](https://dapr.io/) project recently hit several key milestones, including graduating from the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention).  The news was announced at [KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/), where presentations highlighted Dapr’s adaptation to the growing use of [WebAssembly (Wasm)](https://thenewstack.io/webassembly/).  In Kubernetes environments, this allows organizations to leverage Wasm’s extended security features, ultra-low latency and other attributes contributing to its growing popularity.

[Dapr, the distributed application runtime](https://thenewstack.io/zero-trust-security-for-distributed-applications-with-dapr-open-source/), has become a darling of operations teams due to its proven viability in distributed systems, including [Kubernetes](https://thenewstack.io/kubernetes/). Among its most appreciated features are its robust security mechanisms for implementing [zero-trust](https://thenewstack.io/why-you-should-have-100-faith-in-zero-trust/) policies and its ability to seamlessly integrate across infrastructures. Development teams, in particular, often highlight its easy-to-use APIs, which are especially helpful in Kubernetes environments.  Instead of requiring developers to master complex Kubernetes concepts, commands and infrastructure setups, Dapr allows them to focus on creating the logic that solves the problem, while the runtime handles the infrastructure concerns.

## Key Milestones

The CNCF graduation itself is a significant milestone, further solidified by recent statistics indicating the growing adoption and usage of Dapr within the developer and operations communities. (Specific statistics were not provided, but these figures would highlight this progress.)

The project was first announced at Microsoft in 2019 and accepted into the CNCF Incubator in November 2021. Since then, Dapr has grown to more than 3,700 individual contributors from over 400 organizations. It is used by thousands of organizations, including [Grafana](https://thenewstack.io/can-grafana-adaptive-metrics-help-slash-observability-costs/), FICO, HDFC Bank, SharperImage, Zeiss and others. Today, it is maintained by 21 individuals affiliated with eight organizations, who release regular versions each quarter, packed with many new developer APIs, including workflows, secrets, encryption, configuration management and [LLMs](https://thenewstack.io/why-llms-within-software-development-may-be-a-dead-end/).  The CNCF said in a statement that Dapr SDK downloads have surpassed 70 million, with 50 million container image pulls.

“Dapr’s API approach, coupled with its ability to quickly swap underlying infrastructure — whether it’s storage, message broker or secret store — empowers any developer to tackle the complexities of building microservice architectures and delivering business value,” said [Mark Fussell](https://www.linkedin.com/in/mfussell/), Dapr maintainer and steering committee member, and CEO and co-founder of [Diagrid](https://www.diagrid.io/), in a statement.


## Integrated Projects

Projects Dapr integrates with include [OpenTelemetry](https://thenewstack.io/why-the-latest-advances-in-opentelemetry-are-significant/) for [observability](https://thenewstack.io/observability/) data, Prometheus for metrics, [SPIFFE, the Secure Production Identity Framework For Everyone](https://thenewstack.io/the-rise-of-workload-identity-in-cloud-native-with-spiffe-spire/) for identifying and securing services, [gRPC](https://thenewstack.io/grpc-a-deep-dive-into-the-communication-pattern/) and [CloudEvents](https://thenewstack.io/cncf-cloudevents-a-lil-message-envelope-that-travels-far/) for sending communications between application services. The Dapr control plane is hosted on Kubernetes and deployed using Helm charts, and one of its functions is to deploy a Dapr sidecar for each application.

“In today’s competitive landscape, it’s more critical than ever for organizations to be able to quickly deliver reliable and scalable applications,” said [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/), CTO of CNCF, in a statement. “Dapr provides a comprehensive solution for developing edge and cloud-native applications, saving developers valuable time and enabling them to focus on innovation.”
Dapr 的 Wasm sidecar 也越来越受欢迎。自 Dapr 诞生以来，它的设计初衷就是让开发者专注于构建应用程序，而无需担心底层基础设施。[Engin Diri，](https://github.com/dirien) [Pulumi](https://www.pulumi.com/) 的高级解决方案架构师，在 [Rejekts](https://cloud-native.rejekts.io/) 和 KubeCon + CloudNativeCon 期间告诉我，加入 Wasm 后，目标“也是为了让周围的开发者体验更轻松”。

Dapr 有助于改善开发者体验，因为它可以用来创建一个“围绕公司选择的任何实现”的抽象层，Diri 说。“开发团队不需要担心它背后的具体技术。例如，他们只需要一个发布或订阅事件的方法，就可以对消息做出反应，”Diri 说。“这就是很酷的地方：开发者可以专注于尽快交付价值，而无需担心底层实现，他们不必考虑他们使用的是 [Kafka](https://thenewstack.io/top-10-tools-for-kafka-engineers/) 还是 [RabbitMQ](https://thenewstack.io/rabbitmq-is-boring-and-i-love-it/)，因为 Dapr 抽象了这些细节。使用 Dapr，你只需通过 API 获取输入，仅此而已。”

Dapr 可以使 WebAssembly 更轻松，WebAssembly 可以使使用 @daprdev 的部署比容器基础设施更快。

> 今天， @PulumiCorp 的 Engin Diri 在 #WasmCon 上的演讲：Next-Level Powers: Enhance Your IDP with the WASM and Dapr Hero Team-Up! [@thenewstack](https://twitter.com/thenewstack) [pic.twitter.com/SQl7YIAzxK] — BC Gain (@bcamerongain) [November 12, 2024]


在 KubeCon + CloudNativeCon 的演示演讲“Next-Level Powers: Enhance Your IDP with the WASM and Dapr Hero Team-Up!” 中，Diri 展示了如何使用 WebAssembly 提供商 [Fermyon](https://www.fermyon.com/?utm_content=inline+mention) 的开源 [SpinKube](https://thenewstack.io/why-platform-engineers-are-embracing-webassembly-for-serverless/) 和带有 KEDA（Kubernetes Event-driven Autoscaling）的 Dapr 来提供“最佳开发者体验和可能性”，Diri 说。“让我们将 SpinKube 提升到一个新的水平，并扪心自问：我们如何才能帮助开发者更有生产力，更少地考虑周围的一切？”Diri 说。“如果你不熟悉，这个概念的灵感来自法国大革命的‘三头政治’。在我们的例子中，我创建了 SpinKube 三头政治：Dapr、KEDA 和 SpinKube。这就是为什么我认为 Dapr、KEDA 和 SpinKube 构成了完美的三剑客。”

## 专注于应用程序

如上所述，Dapr 提供了对基础设施的抽象，因此开发者可以完全专注于创建应用程序。Diri 在他的演讲中解释说，使用 Dapr，Dapr operator 会自动将 sidecar 机制注入到部署中。他展示了开发者只需要知道存在一个 Pub/Sub 类型的组件。他们不需要知道它是 Kafka、RabbitMQ 还是其他东西，Diri 说。Dapr 提供了一个 SDK 或 API 来在应用程序内进行通信，消除了不必要的复杂性，Diri 说。

Dapr 建立在 actor 模型之上，这使得根据通信模式（即谁与谁通信）构建代码更容易，Diri 说。这种抽象非常有帮助。Dapr 还包含多个构建块，例如状态管理、[Pub/Sub](https://thenewstack.io/publish-subscribe-introduction-to-scalable-messaging/)、安全性和可观察性。开发者无需担心这些组件的底层实现——它可能是 RabbitMQ、Kafka 或其他服务。模块化组件可以轻松实现，例如 Key Vault、[AWS](https://aws.amazon.com/?utm_content=inline+mention) Secret Manager 或 HashiCorp Vault 用于密钥管理。“作为一名开发者，我不需要考虑这些复杂性，”Diri 说。

“通过结合这些部分——抽象基础设施、事件驱动扩展和用于高效 WASM 工作负载的 SpinKube——你将获得一个高效的系统，”Diri 在演讲中说。

[YOUTUBE.COM/THENEWSTACK

技术发展日新月异，不容错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)