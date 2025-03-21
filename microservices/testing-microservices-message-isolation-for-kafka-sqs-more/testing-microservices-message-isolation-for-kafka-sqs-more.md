
<!--
title: 测试微服务：Kafka、SQS等的消息隔离
cover: https://cdn.thenewstack.io/media/2025/03/c0fae648-messages.png
summary: 还在为微服务异步测试发愁？消息隔离来帮你！通过 OpenTelemetry 传播上下文，在 Kafka、RabbitMQ、Google Cloud Pub/Sub 和 AWS SQS 等消息队列中实现消息复制和选择性处理，无需复制基础设施即可进行高效测试，显著提升开发者速度，快来get！
-->

还在为微服务异步测试发愁？消息隔离来帮你！通过 OpenTelemetry 传播上下文，在 Kafka、RabbitMQ、Google Cloud Pub/Sub 和 AWS SQS 等消息队列中实现消息复制和选择性处理，无需复制基础设施即可进行高效测试，显著提升开发者速度，快来get！

> 译自：[Testing Microservices: Message Isolation for Kafka, SQS, More](https://thenewstack.io/testing-microservices-message-isolation-for-kafka-sqs-more/)
> 
> 作者：Arjun Iyer

当我和工程领导者谈论测试事件驱动的微服务时，我经常听到一个共同的痛点：“我们的异步流程几乎不可能可靠地进行测试。”

之前，我们探讨了 [OpenTelemetry 和消息隔离](https://thenewstack.io/shift-left-meets-kafka-testing-event-driven-microservices/) 如何在不复制基础设施的情况下测试基于 Kafka 的工作流程。这种方法引起了许多团队的共鸣，他们面临着以经济高效的方式测试异步流程的挑战，但我收到了许多关于将这种模式扩展到其他消息代理的问题。

*   “这适用于 AWS SQS 吗？”
*   “我们可以将此应用于 RabbitMQ 吗？”
*   “Google Pub/Sub 呢？”

简而言之，答案是肯定的。消息隔离模式适用于大多数流行的消息代理，但实现细节因每个系统的架构和术语而异。

## 通用模式：消息隔离

在深入研究特定平台之前，让我们回顾一下核心问题和我们的方法：

**问题**

通过消息队列进行通信的微服务测试提出了几个挑战：

* 设置单独的测试环境既昂贵又难以维护。
* 如果没有完整的系统测试，异步工作流程很难验证。
* 集成问题通常只在代码合并后才会出现。
* Mock 经常偏离实际，导致误报。

**解决方案**

我们的消息隔离方法通过以下关键原则解决这些挑战：

1. **共享基础设施：** 使用所有沙箱都可以访问的单个基线环境。
2. **传播上下文：** 通过 OpenTelemetry 在消息元数据中传递路由键。
3. **复制消息：** 允许基线和沙箱服务接收相同消息的副本。
4. **选择性处理：** 根据沙箱路由键过滤消费者中的消息。

目标很简单：使多个开发人员能够隔离地测试他们的更改，而不会相互干扰，同时避免复制整个消息传递基础设施的成本和复杂性。

## Apache Kafka：参考实现

Kafka 仍然是我们消息隔离测试的参考实现，因为它具有强大的消费者组模型。在 Kafka 中，多个消费者组可以独立处理来自同一主题的相同消息，从而为我们的测试方法创建了一种自然的模式。

使用 Kafka，每个生产者都在消息头中包含一个路由键，并且消费者组提供隔离机制。当开发人员部署其服务版本进行测试时，它会加入一个唯一的消费者组（例如 `my-service-group-sandbox123`），接收所有消息的副本，而基线版本继续在其原始消费者组中运行。

![](https://cdn.thenewstack.io/media/2025/03/c2801a11-kafka-isolation-1024x512.jpg)

## RabbitMQ：交换机和绑定

RabbitMQ 的架构与 Kafka 不同，因为它使用交换机和绑定作为生产者和消费者之间的中介，从而允许更灵活的路由模式。

在 RabbitMQ 中，交换机通过绑定将消息分发到队列。消息隔离模式的工作原理是为沙箱服务创建临时队列，这些队列绑定到与基线队列相同的交换机。例如，如果您的基线服务从绑定到主题交换机的队列中使用，则您的沙箱版本将创建一个新的临时队列，该队列绑定到具有匹配路由键的同一交换机。

虽然 RabbitMQ 通过绑定模式提供 Broker 级别的过滤，但我们仍然需要消费者端的过滤来根据中央映射服务检查沙箱路由键。消费者将从消息头中提取路由键，调用映射服务以确定是否应处理该消息，然后相应地进行处理。

![](https://cdn.thenewstack.io/media/2025/03/d21b299b-rabbitmq-isolation-diagram-1024x589.jpg)

## Google Cloud Pub/Sub：订阅

Google Cloud Pub/Sub 围绕主题和订阅组织消息，使消息隔离变得简单。一个主题可以有多个订阅，每个订阅都会收到发布到该主题的每条消息的副本——这与我们的沙箱模型完美契合。

对于沙箱测试，请为您的基线服务使用的相同主题创建临时订阅。订阅者将实现消费者端过滤，以从消息属性中提取路由键，根据映射服务进行检查并相应地处理消息。

![](https://cdn.thenewstack.io/media/2025/03/0d6608b0-pubsub-isolation-diagram-1024x589.jpg)

## AWS SQS：特殊情况

AWS SQS 为消息隔离提出了一个独特的挑战，因为它本身不支持我们在其他代理中依赖的扇出模式。在 SQS 中，消息由单个消费者使用；没有内置机制允许多个消费者接收同一消息，并且消息在处理后会自动删除。

因此，我们需要考虑其他方法：

**选项 1：SNS + SQS 模式**

使用 Amazon SNS (Simple Notification Service) 作为入口点，将消息扇出到多个 SQS 队列。发布者将消息发送到 SNS 主题，该主题将副本传递到多个订阅的 SQS 队列——一个用于基线，每个沙箱环境各一个。这种方法不需要更改现有的消费者，因为他们继续从他们专用的队列中读取。

**选项 2：专用测试队列**

为使用沙箱生产者和消费者进行测试创建临时 SQS 队列。部署一个新的生产者实例，将消息发送到临时测试队列，并将您的测试消费者配置为从此新队列中读取。每个沙箱都有自己隔离的队列、生产者和消费者。

对于大多数团队来说，选项 1 提供了最简洁的解决方案。设置一个 SNS 主题，该主题发布到您的基线 SQS 队列和任何临时测试队列，从而保持了解耦的架构，同时实现测试所需的隔离。与复制整个基础设施的成本相比，消息复制的开销通常可以忽略不计。

![](https://cdn.thenewstack.io/media/2025/03/f704f37a-sqs-isolation-diagram-1024x704.jpg)

## NATS：主题和队列组

[NATS](https://nats.io/) 以其轻量级和高性能的设计，提供了非常适合沙箱测试的功能。我们可以利用 NATS 队列组，其功能类似于 Kafka 消费者组。
通过创建特定于沙箱的队列组，测试服务可以接收消息副本，而不会干扰基线服务。您的测试服务将加入一个唯一的队列组（例如 `service-sandbox123`），订阅与您的基线服务相同的主题，并根据路由键实现消费者端过滤。

![](https://cdn.thenewstack.io/media/2025/03/b3db66e2-nats-isolation-diagram-1024x512.jpg)

## 平台团队实施

当平台团队构建处理特定于沙箱的逻辑的可重用组件时，消息隔离方法变得更易于维护。

**创建沙箱感知型消费者库**

平台团队可以在标准客户端库周围创建轻量级包装器，以自动处理沙箱过滤：

```java
public class SandboxAwareKafkaConsumer<K, V> extends KafkaConsumer<K, V> {
    private final SandboxMappingService mappingService;
    private final String sandboxId;
 
    // Constructor and configuration similar to standard KafkaConsumer
 
    @Override
    public ConsumerRecords<K, V> poll(Duration timeout) {
        // Get records using parent implementation
        ConsumerRecords<K, V> allRecords = super.poll(timeout);
 
        // Filter records based on routing key in headers
        return filterRecordsBySandbox(allRecords);
    }
}
```

应用程序开发人员的使用方式与标准消费者完全相同：

```java
// Developers simply use the platform-provided implementation
SandboxAwareKafkaConsumer<String, String> consumer =
    new SandboxAwareKafkaConsumer<>(props);
consumer.subscribe(Arrays.asList("my-topic"));
 
// The filtering happens automatically in the poll() method 
```

这种方法使沙箱过滤对应用程序团队完全透明。

**沙箱生命周期管理**

平台团队可以围绕沙箱的生命周期提供标准化钩子，以自动执行资源管理：

![](https://cdn.thenewstack.io/media/2025/03/fe087d4b-screenshot-2025-03-18-at-1.03.08%E2%80%AFpm-1024x349.png)

当开发人员创建一个新的沙箱进行测试时：

- 平台自动在中央映射服务中注册沙箱 ID。
- 使用一致的命名创建必要的消费者组、队列或订阅（`service-{sandbox-id}`）。
- 测试完成后，所有特定于沙箱的资源都会自动删除。

这种基于钩子的方法使沙箱隔离成为平台核心功能的一部分，而不是每个开发团队的负担。

## 结论

消息隔离模式适用于所有主要消息代理，但实现细节因每个系统的架构而异。该方法始终如一地提供三个关键优势：

1. **成本效率：** 共享基础设施而不是复制它。
2. **测试保真度：** 针对真实依赖项而不是模拟进行测试。
3. **开发者速度：** 在开发过程中尽早发现问题。

在 [Signadot](https://www.signadot.com/)，我们已经在使用不同消息传递系统的数十个客户环境中实施了这些模式。[Brex](https://www.signadot.com/case-studies/brex-uses-signadot-to-scale-developer-testing-across-100s-of-engineers)、[Earnest](https://www.signadot.com/case-studies/how-earnest-empowers-developers-for-early-testing) 和 [ShareChat](https://www.signadot.com/case-studies/sharechat-chooses-signadot-giving-devs-high-quality-testing-feedback) 等公司已经使用这些方法来转变他们的微服务测试。如果您有兴趣探索如何将这些概念应用于您的特定环境，请注册并加入我们的 [community Slack channel](https://signadotcommunity.slack.com/join/shared_invite/zt-1estxm8pv-qfiaNfiFFCaW~eUlXsVoEQ#/shared-invite/email)。

随着微服务架构的不断发展，对异步工作流进行有效的测试变得越来越重要。无论您选择哪种消息代理，消息隔离模式都提供了一种实用且可扩展的方法。