<!--
title: 使用OpenTelemetry测试事件驱动的架构
cover: https://cdn.thenewstack.io/media/2024/02/a327aa4f-telescope-1024x576.jpg
-->

消息隔离方法为测试基于Kafka的异步工作流提供了可扩展、经济实惠的解决方案。

> 译自 [Testing Event-Driven Architectures with OpenTelemetry](https://thenewstack.io/testing-event-driven-architectures-with-opentelemetry/)，作者 Anirudh Ramanathan 是Signadot的首席技术官，他专注于云原生开发。在此之前，他曾在Google工作，专注于Kubernetes核心控制器和可扩展性。

在云原生环境中，异步架构对于解耦服务、增强可伸缩性和增强系统可靠性至关重要。消息队列构成了异步架构的基础，您可以从诸多选项中选择一个，从开源工具如Kafka和RabbitMQ到托管系统如Google Cloud Pub/Sub和AWS SQS不等。然而，测试排队的异步工作流呈现出独特的挑战。本文探讨了使用[OpenTelemetry](https://thenewstack.io/opentelemetry-gaining-traction-from-companies-and-vendors/)测试这些工作流的实用方法，重点关注成本效益、资源优化和运维简单性。

## 使用队列测试事件驱动工作流的挑战

向您的环境添加像[Kafka](https://thenewstack.io/decoding-kafka-why-its-worth-the-complexity/)这样的队列涉及复杂的设置，涉及多个代理、生产者和消费者。试图[复制一个带有队列的环境](https://thenewstack.io/environment-replication-doesnt-work-for-microservices/)进行测试涉及大量的操作性提升，需要考虑诸如安全性、复制、分区和保持副本更新等问题。当尝试使用不同语言和框架的服务消费消息时，复杂性会升级，使得隔离的端到端测试成为一项具有挑战性的任务。

请注意，在这些各种模型中以及接下来的示例中，“租户”有特定的含义。

通过“租户”，我们指的是需要在隔离环境中运行测试场景的开发人员或团队。如果两个团队在密切合作并共同发布，则它们可能是一个单一的租户。但通常，它将意味着一个团队想要测试一些更改，而不让这些更改影响其他人。

## 测试事件驱动工作流的策略

当使用具有许多发布者和订阅者的大型复杂队列时，创建测试环境的两种方法是最常见的解决方案。通过隔离基础设施，为每个租户复制整个集群以及所有相关服务、发布者和订阅者。通过隔离主题，配置队列以使用专用通道进行测试发布者和订阅者。这两种方法都有其缺点，包括维护和设置成本，以及这些新测试环境与生产环境之间的最终（有时是可疑的）准确性。目前，我们将考虑一个为多个租户提供高度可扩展解决方案的解决方案，其环境与生产环境非常相似。

### 使用共享队列进行消息隔离

与其复制不应由租户更改的组件，我们可以专注于要隔离的集群部分：服务之间传递的消息。通过消息隔离，我们可以共享所需的任何资源，甚至让我们的测试服务与其他服务的“基线”版本进行通信。

这始于建立一个安全共享的基线环境，通过OpenTelemetry添加上下文传播，使用动态路由对请求和消息进行动态路由。这种方法可以最大程度地减少基础设施设置、运维开销和成本，同时通过持续集成确保环境保持最新。还可以轻松添加额外的测试租户。

![Zoom](https://cdn.thenewstack.io/media/2024/02/abd3956c-image2.png)

## 实施基于消息隔离的测试

在这种模式中，每个租户都被分配了一个唯一的ID，与特定服务版本的映射相关联。对于大多数服务，任何租户都希望与基线版本进行交互，只有少数选择的服务与更新的版本同步。这些修改后的服务可以像平常一样相互通信，或者与群集中的其他服务通信。

租户ID用于同步（HTTP、gRPC）和异步（排队）通信中的路由。也就是说，对于单个服务的消息往来以及队列中的消息进出，都需要专门的路由指令。实现这一点的方法之一是使用[服务网格](https://www.signadot.com/environment-isolation-service-mesh)。

任何排队系统都支持添加任意头部来影响路由。在Apache Kafka中，生产者在消息头中包含租户ID，而消费者则使用这些ID进行选择性消息处理。此设置需要修改Kafka消费者，并利用OpenTelemetry进行上下文传播。当使用RabbitMQ时，这个过程也是相当相似的，它也可以将每个消息与租户ID嵌入在一起。

### 运维架构

为了基于请求隔离的测试和实验而实现消息隔离，有几个必要的组件。

- **使用 OpenTelemetry 进行上下文传播**：利用 OpenTelemetry 在服务和队列之间传播租户ID，确保消息路由的一致性。要为 Kafka 生产者和消费者添加上下文传播功能，您可以参考 OpenTelemetry 文档中提供的具体示例。该[示例](https://opentelemetry.io/blog/2022/instrument-kafka-clients/)展示了您如何从生产者通过 Kafka 将租户ID传播到消费者。[RabbitMQ 也支持上下文传播](https://opentelemetry.io/docs/specs/semconv/messaging/rabbitmq/)，并且 Google Cloud 和 [AWS](https://aws.amazon.com/?utm_content=inline-mention) 上的公共云排队服务也具有类似的支持。
- **选择性消息消费**：在队列消费者中实现基于租户ID的消息过滤逻辑，每个消费者都在自己的组中运行。
- [服务网格或其他路由系统](https://aws.amazon.com/?utm_content=inline-mention)：对于租户来说，配置他们的集群只将测试消息发送到他们的系统，而将所有其他请求正常路由，可以配置一个服务网格或其等效物，根据请求头部路由流量。

![](https://cdn.thenewstack.io/media/2024/02/fb7df728-image1.png)

*在这个例子中，一个租户可以启动服务的新版本（B” 和 C”），并将它们添加为生产者和消费者，而不会干扰其他团队的测试流程。*

对于这些新的消费者组，一个直接的命名约定是将服务的原始消费者组附加上“-[沙箱名称]”。

### 非请求范围的流程

当为不以单个请求开始的流程实现该系统时，需要考虑一些因素。例如，如果一个定时作业正在从表中读取行，处理它们，并将每个行作为消息发布到队列中，您需要在读取每一行时发出租户ID，这就需要您为您的目标设计系统。一旦明确了基线和“测试中”版本的消费者将如何对来自数据库的消息进行分区，系统就需要相应地进行设计。

## 结论

[消息隔离方法](https://thenewstack.io/publish-subscribe-introduction-to-scalable-messaging/)为测试基于Kafka的异步工作流提供了可扩展、经济实惠的解决方案。它减少了对庞大基础设施的需求，同时保持了高度的隔离性和灵活性。这种方法可以扩展到其他消息队列，是现代异步应用的战略选择。

本文的后续内容将涵盖使用Signadot实现异步工作流消息隔离的具体细节。

要获取有关使用内部队列进行测试的深入见解和详细的实现建议，请加入Signadot社区Slack频道的讨论。
