
<!--
title: 左移与Kafka相遇：测试事件驱动型微服务
cover: https://cdn.thenewstack.io/media/2024/10/3292dcd9-flow.jpg
-->

通过沙箱，开发者可以查看其更改的影响，而不会干扰其他开发者的测试或系统的常规流量。

> 译自 [Shift Left Meets Kafka: Testing Event-Driven Microservices](https://thenewstack.io/shift-left-meets-kafka-testing-event-driven-microservices/)，作者 Arjun Iyer。

在现代分布式系统中，异步通信模式越来越普遍。虽然现在有很多消息队列系统可用——从[Apache Kafka](https://thenewstack.io/apache-kafka-primer/)到[RabbitMQ](https://thenewstack.io/rabbitmq-is-boring-and-i-love-it/)，或者像[Google](https://cloud.google.com/?utm_content=inline+mention) Pub/Sub和[AWS](https://aws.amazon.com/?utm_content=inline+mention) SQS这样的云服务——我们将重点关注Apache Kafka作为具体的例子。但是，我们将讨论的模式和挑战适用于不同的消息队列实现。

消息队列构成了许多[微服务架构](https://thenewstack.io/microservices/)的支柱，实现了各种模式来处理不同的用例。在多对一模式中，多个生产者向单个消费者发送消息，这在数据聚合场景中很常见。

多对多模式允许多个生产者与多个消费者通信，这在事件驱动架构中非常有用。一对多模式，其中单个生产者向多个消费者广播消息，通常出现在通知系统中。

**测试异步系统的挑战**

在异步系统中测试更改会带来独特的挑战，尤其是在多个开发人员同时工作的共享环境中。考虑一个电子商务平台，其中订单处理服务发布触发多个下游流程的事件，例如支付处理、库存更新和发货通知。当开发人员需要测试此工作流程中任何服务的更改时，他们会面临重大挑战。

在共享环境中，多个开发人员同时测试更改往往会相互干扰。修改订单处理程序的开发人员可能会影响测试支付服务更改的另一个开发人员。当测试失败时，很难确定失败是由于他们的更改还是其他正在进行的测试的干扰造成的。模式更改尤其具有挑战性，需要团队之间仔细协调以避免破坏现有消费者的功能。

开发人员花费大量时间与其他团队协调测试窗口，等待其他人完成测试，并调试可能与他们的更改无关的问题。这导致反馈周期缓慢，生产力下降。不同开发人员更改之间缺乏隔离性使得难以自信地运行全面的集成测试。

解决这些挑战的一种方法是为每个开发人员启动完整的隔离环境。但是，这种方法也有其自身的问题。对于像Kafka这样的系统，每个[环境都需要复制](https://thenewstack.io/environment-replication-doesnt-work-for-microservices/)整个消息队列基础设施，包括代理、集群管理组件和所有相关服务。这很快就会变得非常昂贵且难以维护。设置这些环境需要大量时间，并且大规模运行多个完整环境的基础设施成本可能很高。

从开发人员体验的角度来看，这两种方法都存在明显的缺点。共享环境会导致测试干扰和复杂的协调需求，而重复的环境则会带来高成本和维护开销。这清楚地表明需要一种更好的方法，该方法可以在不增加完整环境复制开销的情况下提供开发人员所需的隔离性。

**使用沙箱进行动态流量路由**

领先的技术公司已经采用了一种更有效的方法，即使用动态流量路由和沙箱。沙箱是一个隔离的测试环境，允许开发人员测试他们的更改，同时与其他开发人员共享大部分底层基础设施。

此方法不复制整个系统，而是使用请求头将流量路由到特定服务版本。通过整个请求链传播这些标头的一种常用方法是使用[OpenTelemetry](https://opentelemetry.io/)库，该库提供内置的上下文传播功能。虽然OpenTelemetry通常以分布式跟踪而闻名，但其上下文传播功能本身就提供了巨大的价值，我们在这种方法中使用了它。
对于请求路由，我们只需要上下文传播功能——不需要实现分布式追踪。对于服务之间的同步通信，可以使用[Kubernetes环境中的服务网格或Sidecar](https://thenewstack.io/scaling-environments-with-opentelemetry-and-service-mesh/)在基础设施层实现动态路由。一个中心“路由”服务存储服务和路由键之间的映射，基础设施层会查询该映射以做出路由决策。

![根据请求头将请求流路由到沙箱服务B](https://cdn.thenewstack.io/media/2024/10/b41054a8-screenshot-2024-10-29-at-7.17.45%E2%80%AFam-1024x597.png)
根据请求头将请求流路由到沙箱服务B

**实现选择性消息处理**

对于异步系统，有一些特殊的考虑，我们将在下面描述。该解决方案涉及三个关键组件协同工作，以确保异步流中正确的消息路由：

首先，必须对生产者进行检测，以便在消息头中包含路由信息。当请求启动消息生产时，路由上下文将从传入请求中传播。

其次，当消费者服务的沙箱版本启动时，它会创建一个新的Kafka消费者组。这确保所有消息都被基线和沙箱消费者接收，消费者组名称通常从沙箱ID派生，用于追踪。

第三，也是最关键的是选择性消息处理逻辑。基线和沙箱消费者都会接收所有消息，但必须决定处理哪些消息。以下是做出此决定的方法：

![Kafka生产者和消费者使用消息头进行选择性消费](https://cdn.thenewstack.io/media/2024/10/62346a5b-mq-consumers.png)
Kafka生产者和消费者使用消息头进行选择性消费

```
123456789101112131415161718
// Consumer decision logic when receiving a message
function shouldProcessMessage(message, consumerType) {
  // Extract sandbox routing info from message
  sandboxID = message.headers.get("sandbox-id")
  // Get service mapping from central route service
  serviceMapping = routeService.getMapping(sandboxID)
  if (consumerType == "sandbox") {
    // Sandbox consumer only processes messages explicitly meant for it
    return serviceMapping.targetService == thisService
  } else {
    // Baseline consumer processes messages with no sandbox ID
    // OR messages meant for sandboxes of other services
    return !sandboxID || (serviceMapping.targetService != thisService)
  }
}
```

此逻辑确保即使在复杂场景下也能正确路由消息。

**不同消息队列模式的特殊考虑**

上述方法需要针对某些常见的消息队列模式进行调整。当使用具有更改数据捕获 (CDC) 的消息队列（例如带有 Kafka 的 Debezium）时，生产者会从数据库事务日志中读取数据。在这些情况下，源数据库记录需要包含路由信息，通常在元数据列中，然后 CDC 生产者可以将其包含在消息头中。这确保即使对于数据库启动的事件也能正确路由。

对于批量处理消息的系统，需要在批次级别做出路由决策。具有不同路由上下文的邮件应在单独的批次中处理，批次处理器在整个批次生命周期中维护路由上下文。这在高吞吐量系统中变得尤为重要，因为批量处理对于性能至关重要。

**开发者体验**

从开发者的角度来看，使用这种方法，测试异步工作流的更改变得非常简单。假设一个开发者正在修改一个从 Kafka 消费订单事件并更新运输系统的服务。以下是他们的体验：

首先，他们通过其平台团队提供的工具创建其修改服务的沙箱。在幕后，平台处理所有必要的设置——部署服务、设置消费者组和设置路由——但开发者只需要请求一个新的沙箱。

为了测试他们的更改，他们通过常规应用程序接口或 API 触发测试订单，包括一个简单的标头或参数，将流量路由到他们的沙箱。平台的检测会自动确保此路由信息通过整个系统传播，从初始请求，到消息队列，再到他们修改的服务。

然后，开发者可以观察他们的更改如何处理测试订单，而其他开发者的测试和常规流量则继续不受干扰地流经系统。消息路由、消费者组管理和上下文传播的所有复杂性都由平台提供的库和基础设施处理，使测试[对开发人员来说无缝](https://thenewstack.io/are-you-delivering-on-developer-experience/)。
这使开发人员能够快速迭代他们的更改，而无需担心干扰他人或管理复杂的架构。他们可以专注于其服务逻辑，而平台则确保其测试流量能够正确地通过异步系统。

**结论**

分布式系统的有效测试不需要大规模复制基础设施。凭借正确的架构和工具，团队可以实现更快、更可靠的测试，同时降低成本并提高开发人员的工作效率。

[Brex](https://www.signadot.com/case-studies/brex-uses-signadot-to-scale-developer-testing-across-100s-of-engineers)、[DoorDash](https://www.signadot.com/case-studies/how-developers-at-doordash-get-10x-faster-feedback) 和 [ShareChat](https://www.signadot.com/case-studies/sharechat-chooses-signadot-giving-devs-high-quality-testing-feedback) 等公司已成功使用 Signadot 实施了这种方法，Signadot 为同步和异步测试场景提供了开箱即用的解决方案。要了解如何在您的组织中实施此模式，请访问 [signadot.com](http://signadot.com) 并加入我们的 [社区](https://signadotcommunity.slack.com/join/shared_invite/zt-1estxm8pv-qfiaNfiFFCaW~eUlXsVoEQ#/shared-invite/email) Slack 频道。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。