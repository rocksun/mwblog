# 揭示应用网络的未来：趋势和影响

让我们在现代分布式架构的背景下，审视透明、同步和异步网络的迁移和转型。

翻译自 [Unveiling the Future of Application Networking: Trends and Impacts](https://thenewstack.io/unveiling-the-future-of-application-networking-trends-and-impacts/) 。

![](https://cdn.thenewstack.io/media/2023/06/fa805170-shutterstock_1-1024x540.jpg)

应用网络功能的发展方向在哪里，这将如何影响我们未来设计和处理分布式应用程序的方式？揭示的内容可能会让您感到惊讶。让我们探索[应用网络](https://www.diagrid.io/blog/evolution-of-cloud-computing)的变革，重点关注应用云的兴起所带来的网络关注点的转移。通过解开透明、同步和异步网络的复杂性，我们来研究这些方面在现代分布式架构中的迁移和转型。

## 透明网络下沉到平台层面

分布式应用由多个组件通过[网络](https://thenewstack.io/networking/)相互交互。这些交互可以在运行时通过服务网格和其他类似的技术透明地对应用进行控制，或者可以通过显式实现的模式（如点对点集成、事件驱动或基于编排的交互）在应用内部进行控制。

在这里，我将透明网络定义为可以在应用程序相互交互的行为中添加的控制和监控机制，而不需要开发人员和应用实现者知道。比如，想象一下由 Kubernetes 执行的服务发现或负载均衡，而应用程序无需了解其具体实现方式。再想象一下由 [Istio](https://istio.io/latest/docs/tasks/traffic-management/circuit-breaking/) 的 Sidecar 执行的流量转移、重试和断路等鲁棒性功能。再想象一下通过 [Cillium](https://isovalent.com/blog/post/2022-05-03-servicemesh-security/) 的基于 eBPF 实现，从 Linux 内核获得的 mTLS 、[身份验证](https://roadmap.sh/guides/basics-of-authentication)和授权，以及网络追踪和可观测性。

所有这些功能可以在运行时添加到分布式应用中，而无需更改应用代码，也无需开发人员在应用程序内部实现一行代码。

![](https://cdn.thenewstack.io/media/2023/06/c578f997-image1a-e1687960648942.png)
*透明网络功能与运行时平台融为一体。*

过去，这些问题通常由开发人员在应用层通过特定于语言的库（如 Java 生态系统中的 [Apache Camel](https://camel.apache.org/) 或 [Spring Cloud Netflix](https://spring.io/projects/spring-cloud-netflix) ）来解决，但如今这些问题越来越多地被委托给多语言运行时（如 [Dapr](https://dapr.io/) ），或通过透明的 Sidecar（如 [Envoy](https://www.envoyproxy.io/)）委托给平台层，甚至在 [eBPF 技术](https://cilium.io/blog/2020/11/10/ebpf-future-of-networking/)和封闭源网络云服务的情况下与计算平台深度嵌入。

## 同步网络逐渐远离应用程序

应用程序之间的同步交互是指不需要任何中间持久状态存储（如消息代理）来将请求转移到应用程序之间的媒介的交互。因此，我在这里描述的同步交互通常是由客户端应用程序发起的阻塞交互，并在同一调用中到达目标服务。在这里考虑的应用程序责任包括与各种外部 API 的连接器、解决方案内服务之间的调用以及协议转换。这还包括基于内容的路由、过滤和请求的轻量级转换，多个消息的聚合或将大型消息拆分为多个消息。最后一组可以使用持久状态存储完成，但在这里我考虑的是在运行时即时进行，而无需持久化。广义上讲，这些应用程序网络关注点包括《[企业集成模式](https://www.enterpriseintegrationpatterns.com/patterns/messaging/)》一书中列出的消息路由和消息转换模式。

尽管这些关注点传统上是由应用程序内部实现的，并且在 Java 生态系统中很受欢迎，例如通过 Apache Camel 和 Spring Integration 等项目，但今天我们可以看到这些功能正在向专门构建的即插即用运行时移动。这些运行时可以与许多多语言应用程序一起使用。其中的示例包括 Dapr Sidecar、[Apache Kafka Connect](https://kafka.apache.org/documentation/#connect_transforms)、[Knative Event Sources](https://knative.dev/docs/eventing/sources/)、[NATS](https://nats.io/) 以及各种托管的基于云的连接器和流量路由服务，例如用于路由流量的 AWS API Gateway 或用于路由事件的 [AWS EventBridge](https://aws.amazon.com/eventbridge/) 等。

在所有这些示例中，应用程序将消息传递给单独的运行时，其中执行消息路由和转换逻辑，然后将结果传递回应用程序或转发给另一个应用程序。应用的路由、过滤和转换逻辑会影响数据的形状和流向。

![](https://cdn.thenewstack.io/media/2023/06/78513230-image2a-e1687960719349.png)
*同步连接模式转移到即插即用运行时。*

与透明功能可以在应用实现后由运维团队应用不同，同步网络功能由开发人员使用，并且应用程序必须在设计和实现时考虑这一点。

因此，我们可以看到同步网络功能不会透明地下沉到平台中，而是从库转变为专门构建的可重用运行时和云服务，可以在需要时插入任何应用程序中，而不会影响应用程序的实现。通过使用[六边形架构](https://alistair.cockburn.us/hexagonal-architecture/)的原则设计应用程序，并通过采用通用的开放标准来将应用程序与外部依赖解耦，可以实现这一点。

目前，在此领域没有普遍采用的标准或实现，但有一些常用的消息模式（如过滤器、基于内容的路由器、监听器、聚合器和拆分器），这些模式通常通过特定于领域的语言或使用[通用表达式语言](https://github.com/google/cel-spec)规范实现，并对以 JSON 或 [ProtoBuf](https://protobuf.dev/) 格式进行的数据以及在 HTTP 或 gRPC 协议上传输的 [CloudEvents](https://cloudevents.io/) 包装进行操作。

## 异步网络朝着云的方向发展

异步网络允许应用程序将状态存储到外部系统中供其自身使用，或在与另一个服务交换数据之前进行临时存储。例如，开发人员可以使用外部状态存储（如 [Redis](https://redis.com/) ）进行键值访问，或使用对象存储（如 [AWS S3](https://aws.amazon.com/s3/) ）存储状态并使服务无状态化。应用程序可以使用消息代理（如 Apache Kafka ）发布另一个服务可能感兴趣的事件。应用程序可以启动存储在持久化工作流引擎（如 [Conductor](https://conductor.netflix.com/) ）中的业务流程，该工作流引擎需要协调与其他服务的交互。当我们查看源服务和目标服务之间的端到端交互时，状态会在与其他服务交换之前在中间系统中持久化。这些异步网络交互样式通过一些众所周知的方法（如发布/订阅、键值访问、编排、定时作业、分布式锁等）以可预测和可靠的方式在参与者之间分布状态。

![](https://cdn.thenewstack.io/media/2023/06/2d4e8912-image3a-e1687960793821.png)
*异步网络基础设施正在转变为SaaS（软件即服务）。*

每种异步网络模式都提供了一种基于状态的独特交互方式。键值和对象存储用于存储通常从同一应用程序访问的状态。消息代理用于发布方服务与一个或多个接收方服务之间的异步通信。工作流引擎用于协调多个应用程序之间的复杂有状态交互，或者按时间间隔触发服务端点。

还有其他一些专门的有状态应用程序基础设施示例：例如，将应用程序配置从中央配置存储中分发、分发密钥、使用分布式锁实现对资源的互斥访问等。这些交互对应用程序是显式的，开发人员需要以适应这些专门系统的方式开发应用程序。在各自领域中，有许多正在被广泛采用的 API 标准。例如，[Redis](https://redis.com/?utm_content=inline-mention)、[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline-mention) 和 [Amazon Web Services（AWS）](https://aws.amazon.com/?utm_content=inline-mention)的 S3 是键值和文档访问的常用 API 示例。Apache Kafka、[AMQP](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)、[NATS](https://nats.io/) 是异步交互协议的示例。 [Camunda](https://github.com/camunda/camunda-bpm-platform)、Conductor 和 [Cadence](https://cadenceworkflow.io/) 是有状态编排引擎的示例。

虽然这些项目专注于单一类型的有状态交互，并提供实现和 API ，但 Dapr 项目专注于为不同交互样式提供统一的 API ，并将它们插入现有的后端实现中。例如， [Dapr 状态存储 API](https://docs.dapr.io/reference/api/state_api) 可以与 Redis、MongoDB、PostgreSQL 等一起使用。[Dapr 发布订阅 API](https://docs.dapr.io/reference/api/pubsub_api/) 可以与 Kafka、AWS SQS、GCP Pub/Sub、Azure EventHub 等一起使用。其配置、密钥和[分布式锁 API](https://docs.dapr.io/developing-applications/building-blocks/distributed-lock/distributed-lock-api-overview/) 也可以插入现有基础设施系统，并提供了一个统一的多语言高级 HTTP 和 gRPC 协议来抽象这些后端。

为了应对管理状态的固有复杂性，该行业正在目睹一个令人瞩目的转变，即异步网络能力越来越多地作为 SaaS 解决方案提供。这种转变简化了采用过程，简化了可扩展性，并提升了这些服务的可管理性。

广泛使用的消息代理 Apache Kafka 现在可作为 Confluent Cloud 和 AWS 托管的 Apache Kafka（MSK） 访问。同样，传统上在内部管理的键值存储（如 Redis ）和文档存储（如 MongoDB ）已经发展成为云服务。Redis Labs 的全面托管云服务和 MongoDB Atlas 的全球可用服务集成了资源和工作负载优化。

同样，有状态的工作流系统也进入了 SaaS 领域，简化了开发人员在应用程序之间进行复杂有状态交互的任务。 AWS Step Functions 、 Temporal Cloud 、 Orkes 和 Diagrid Cloud 都是这一演进的先驱。将有状态网络项目转变为 SaaS 的这一趋势是为了抽象状态管理的复杂性。它使开发人员能够专注于业务逻辑，而不是复杂的异步交互。

## 应用程序网络的分歧路径

分布式应用程序由分布在多个进程中的多个组件组成，它们通过网络相互交互。分布式应用程序的主要优势，如更快的发布周期和可扩展性，取决于不同的网络模式如何促进依赖关系的隔离和状态在参与者之间的分布。然而，网络在分布式系统编程模型、可靠性、安全性和可观测性方面带来了新的挑战。与容器的采用类似，容器将重要的应用程序责任从开发人员转移到运维团队，我们也可以观察到不同类型的网络关注点的转变。

透明网络功能虽然在功能上有限，但随着其集成到平台提供中变得越来越普遍。有了适当的平台功能，开发人员不再需要关注网络安全、可观测性和流量管理。

无状态交互将网络与数据格式的知识和消息转换逻辑相结合。这样的交互通过标准连接器和作为专门构建的分布式系统中间件实现的企业集成模式越来越多地变得可重用。开发人员不必在每种语言和应用程序堆栈中不断重新发明轮子，而是可以在运行时将这些功能插入到他们的应用程序中。在足够长的时间内，这些网络模式将变成可重用的库、专门构建的框架和Sidecar ，并最终转变为基于云的 API 。

异步交互具有更高的复杂性，因为它们需要在幕后进行状态管理。这些网络交互通常作为专门的独立软件或托管服务提供，最好由广泛采用的 API 作为前端。与下沉到计算层并主要由运维团队使用的透明 API 不同，异步网络交互出现在为应用程序开发人员创建的云提供中。

![](https://cdn.thenewstack.io/media/2023/06/e0e744c5-image4-e1687960847659.png)
*应用程序网络责任的演变*

这种网络责任的演进预计将进一步将透明运行时和网络功能融入到计算平台中。与此同时，显式功能将继续整合，形成通用的 API ，并成为无处不在的无服务器能力。在不同的网络任务中适当地委托责任，并选择适当的标准化 API ，变得越来越重要。因此，这一巨大趋势将使开发人员能够专注于实现业务逻辑，通过透明方式或通过广泛认可和可移植的 API 集成其他能力。