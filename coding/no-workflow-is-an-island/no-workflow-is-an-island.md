<!--
# 没有工作流是孤岛
https://cdn.thenewstack.io/media/2023/10/568c6210-fishing-1024x748.jpg
 -->

Dapr 的统一 API 和模式，包括跨语言和框架的工作流，解放了开发者面对碎片化技术的困扰。

译自 [No Workflow Is an Island](https://thenewstack.io/no-workflow-is-an-island/) 。

几十年前，使用工作流建立业务流程在计算领域就已经出现，并成为业务自动化的基石。时至今日，现代应用已经变得非常复杂，包含各种计算类型，依赖事件驱动设计，与多个服务通讯，构建来处理故障并维持高水平安全。

在这种复杂性中，一个元素保持不变：业务工作流的作用。但是，开发者实现工作流的方法已经多样化，反映了可用选择的多样性。

让我们深入探讨对开发者友好的基于代码的工作流引擎，它们在分布式应用、[微服务](https://thenewstack.io/microservices/microservices-vs-monoliths-an-operational-comparison/)或[云原生架构](https://thenewstack.io/cloud-native/)中变得突出。我们的重点是集成工作流引擎与事件驱动消息传递、同步通信、状态存储等[开发者模式](https://www.diagrid.io/blog/dapr-as-the-ultimate-microservices-patterns-framework)的需求。

## 工作流编排和自动化

在软件开发时代，工作流引擎(或运行时)经历了重大演变，以解决[企业工作流编排](https://thenewstack.io/cloud-native/the-cloud-native-landscape-the-orchestration-and-management-layer/)和自动化场景的复杂性，必须与各种系统和服务集成，提供条件分支、并行执行、处理外部系统交互等功能。此外，它们的功能扩展到编排微服务和促进事件驱动架构。

工作流引擎通常以两种不同形式出现：面向开发者的基于代码的程序引擎和面向业务用户的基于域特定语言(DSL)的引擎。

虽然DSL引擎提供视觉设计、集成等优势，但在开发者中心工具上往往存在缺陷，如缺少调试、SDK集成、利用测试套件等能力，这使得基于代码的工作流更具优势。在进入实际应用示例前，让我们先探讨有界上下文的概念。

## 有界上下文

[有界上下文](https://www.martinfowler.com/bliki/BoundedContext.html)是域驱动设计中的一个概念，它注重在开发者和领域专家之间建立复杂业务领域的共同理解。[有界上下文是域驱动设计的构建块之一](https://thenewstack.io/from-monolith-to-microservices/)，通过将系统分割成可管理的隔离业务组件来管理大型软件系统的复杂性。

通常会在每个有界上下文的中心放置一个工作流。但是，没有哪个工作流是孤立的，因为它通常需要与其他有界上下文以及上下文内部进行通信。

![](https://cdn.thenewstack.io/media/2023/10/72568427-image3.png)

有界上下文具有清晰明确的边界，用于防止软件不同部分交互时出现歧义和冲突。有界上下文之间的通信和数据交换通过明确定义的接口、API和消息进行管理。

例如，想象一个包含“订单管理”、“库存管理”和“客户互动”有界上下文的电商平台。每个上下文都有自己的领域模型、业务规则和专属术语。订单管理上下文可能定义订单和处理流程，而库存管理上下文关注库存跟踪和管理。

## 应用有界上下文

让我们看一个例子，构建包含上述有界上下文的电商处理系统，如下图所示。

![](https://cdn.thenewstack.io/media/2023/10/cdb1f8be-image6.png)

深入订单管理有界上下文，它会包含一个编排活动的工作流，充分利用任务链、分支等模式。例如，该订单管理工作流的业务流程可能类似以下状态机:

![](https://cdn.thenewstack.io/media/2023/10/db63a12a-image2.png)

实现上，订单处理服务需要与上下文中的其他服务交互，比如支付服务确认支付。另外，订单服务也需要将状态和客户数据保存到数据库，因此需要从密钥库获取证书。这就需要工作流支持服务并在上下文内外通信。下图展示了订单管理上下文的一个示例实现。

![](https://cdn.thenewstack.io/media/2023/10/90e6e33b-image1.png)

跨有界上下文的同步和异步通信都是必要的。这里，同步通信用于在库存系统中预留商品，而消息用于通知客户应用订单完成。

为提高客户体验，必须确保在订单成功生成前不发送任何消息，这时[出站模式(outbox pattern](https://microservices.io/patterns/data/transactional-outbox.html)在订单管理和客户参与上下文之间很有用。

## 分布式应用开发者的挑战

这种设计方法使不同团队可以分割关注点并独立扩展和部署有界上下文。为充分利用分布式应用和微服务架构的优势，需要组合实现常见软件模式的各种技术。

例如，工作流的业务活动、服务发现的请求/响应、事件驱动的发布/订阅消息传递。对开发者的挑战在于确定使用哪些模式，然后集成大量库、运行时和 SDK。

通常，大多数后端开发者受限于特定语言，甚至该语言中的特定框架。比如，80% 的 Java 开发者使用 Spring，Node.js(42%)、Express(20%)和 Nest.js(5%)覆盖大多数 JavaScript 开发。C#有其所有 .NET 版本，Python 难以计数。

作为开发者，你要么依赖框架提供所需模式，如果不提供，则集成兼容的库或自己编写代码，而不是编写业务代码。

正如我们在示例中看到的，分布式应用需要组合模式创建更复杂的业务场景，包括调用其他服务的工作流、发布/订阅消息处理事件和维护数据隔离。

此外，还需要加入横切关注点的弹性模式来处理超时、重试、熔断器，以提高应用抵御网络和进程故障的弹性。安全模式包括建立信任的身份、认证和消息加密。最后，端到端追踪和使用指标报告的可观测性对监控和优化应用性能至关重要。

## 现在实现它

回到我们的应用示例，让我们探讨可以组合实现分布式架构优势的一些技术。其详尽列表本身就是一篇文章。

对于基于代码的工作流引擎，可以选择 [Apache Airflow](https://airflow.apache.org/)、[Cadence](https://cadenceworkflow.io/)、[Temporal](https://temporal.io/)等；一些开发者友好的基于 DSL 的工作流例如 [Netflix Conductor](https://conductor.netflix.com/index.html)，在使用[系统任务](https://conductor.netflix.com/documentation/configuration/workflowdef/systemtasks/index.html)通信时也很有用。服务发现和同步通信常用的选择包括工作在网络层面的服务网格，以及 NAT、Consul、gRPC 和 HTTP/REST。消息传递可以考虑 Apache Kafka、RabbitMQ、Redis Streams 或公有云的发布/订阅服务。

在所有通信上添加弹性，如果使用 Java 或 .NET，可以选择 Hystrix、Resilience4j 和 Polly 等工具，但使用 Python 等语言时，大多需要自行处理。安全和身份方面，有大量技术可进行安全通信、认证和授权，包括使用 API 网关和服务网格，具体选择取决于用例、技术栈和安全需求。

最后，对于可观测性，可以使用 OpenTelemetry、Log4j、Fluentd 等工具检测代码，或选择 Jaeger、Prometheus、Zipkin 等可观测性客户端库。

仅看这些有限的技术示例，开发者面临使用首选语言构建技术平台的艰巨任务。此外还需要添加部署、策略管理和运维所需的整体应用平台维护。

一个总体问题出现了：是否可以有一组更全面的模式和 API，可以组合工作，将所有语言和框架的开发者集中在一起，而不是像今天这样碎片化？如何避免重复发明轮子？

## Dapr — 统一 API 和模式用于分布式应用开发

[Dapr 项目](http://dapr.io/)引入了一组统一 API，使任何框架的开发者都可以通过 HTTP 或 gRPC 调用构建分布式微服务应用。这些 API 封装了常见软件模式，每个 API 可以独立使用，但真正的优势在于可以组合使用，同时应用必要的横切关注点。正如 Kubernetes 和容器通过提供统一平台 API 改变了计算格局，Dapr 为分布式应用开发带来了统一 API。

如下图所示，你可以从首选语言框架调用 Dapr API，如果需要，还可以与任何适应应用需求的语言特定 API 组合使用。此外，Dapr API 可以通过其组件模型连接到广泛的基础设施服务，创建与基础平台无关的可移植代码。

![](https://cdn.thenewstack.io/media/2023/10/bf4cc399-image4.png)

Dapr 的基于代码的[工作流引擎及其模式](https://www.diagrid.io/blog/in-depth-guide-to-dapr-workflow-patterns)旨在与 Dapr 的服务调用、发布/订阅、机密、键值存储和绑定 API 一起使用。这里未涵盖的其他 Dapr API 包括外部配置、加密、Actor 和锁等，每个 API 都与分布式系统模式对应。

将其应用到我们的订单管理应用程序，下图显示了如何在有界上下文内外使用统一的 Dapr API。

![](https://cdn.thenewstack.io/media/2023/10/394e665b-image5.png)

在不断发展的软件环境中，复杂性已成为常态，而工作流引擎对许多业务应用仍很重要。如我们在示例中所见，工作流需要与其他服务通信并得到支持。使用 Dapr，开发人员可以访问跨语言和框架的统一 API 和模式集，包括工作流，从而摆脱碎片化技术的挑战。

想了解更多 Dapr 相关信息或有疑问？加入 [Dapr Discord 服务](https://bit.ly/dapr-discord)器，与成千上万的 Dapr 开发者交流。

