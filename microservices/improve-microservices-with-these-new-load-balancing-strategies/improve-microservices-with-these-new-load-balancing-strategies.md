
<!--
title: 使用新的负载均衡策略改进微服务
cover: https://cdn.thenewstack.io/media/2024/11/ea4cc416-colton-sturgeon-6kkyyqtedwq-unsplash-scaled.jpg
-->

通过使用 Ribbon 等工具在客户端和使用 Nginx 在服务器端确保适当的负载分配，可以增强系统可扩展性和弹性。

> 译自 [Improve Microservices With These New Load Balancing Strategies](https://thenewstack.io/improve-microservices-with-these-new-load-balancing-strategies/)，作者 Dhruv Kumar Seth。

从单体架构到[微服务的转变](https://thenewstack.io/how-to-fail-at-microservices/)已成为当代软件开发工作流中的一种实践。尽管创建和启动单体系统看起来很简单，但随着时间的推移，它们在扩展和管理复杂应用程序时会造成重大障碍。

另一方面， [微服务](https://thenewstack.io/microservices/)提供了一种更[模块化的方法](https://www.developer-tech.com/news/microservice-architecture-vs-modular-architecture/)，使各个元素能够自主开发和部署。但是，在多个节点上分布计算会带来新的挑战，尤其是在可扩展性、效率和可靠性方面。实施有效的负载均衡策略对于解决这些问题至关重要。建立负载均衡技术对于有效应对这些挑战至关重要。

管理流量使公司能够利用微服务的好处，与旧的单体系统相比，提供更具可扩展性和可靠性的 API。本文探讨了通过高级负载均衡技术克服这些挑战的策略。

## 克服可扩展性和效率挑战

从单体架构到微服务的转变在可扩展性和效率方面带来了障碍，同时努力实现最佳性能提升。在单体系统中，所有组件都是相互连接的，这使得初始设置更加简单，但随着应用程序的扩展，灵活性受到限制。另一方面，微服务采用了一种策略，允许每个服务独立地进行扩展和部署。

这种转变带来了自己的一系列关键挑战：

- **通信变得更加复杂：** 在微服务架构中，服务通过网络进行通信，通常跨越基础设施边界。这引入了网络延迟和额外的负载，而这些负载仅存在于所有组件在内部进行交互的单体系统中。
- **负载均衡挑战：** 与负载均衡相对简单的单体系统不同，微服务需要智能流量分配以确保高可用性和高效的资源利用。传统负载均衡器可能需要充分了解微服务的动态特性，从而导致流量路由效率低下、实例利用率不足以及潜在的服务中断。
- **管理可扩展性和负载分配：** 随着微服务的扩展，确保跨服务的均匀负载分配变得更加复杂。负载均衡器必须处理服务的动态扩展以维持性能、防止瓶颈并确保系统可靠性。
- **资源开销：** 微服务中的有效负载均衡需要额外的基础设施，例如 API 网关和服务发现工具，以正确路由流量。这种增加的复杂性会导致更高的资源 [管理和运营](https://thenewstack.io/chaos-to-control-3-steps-for-automating-incident-management/) 成本。正确理解这些挑战对于在保持最佳负载均衡的同时最大化微服务的好处至关重要。

确保顶级可用性和性能的一个关键方面是使用负载均衡技术，该技术可以在服务之间有效地分配流量。组织必须克服这些障碍才能利用微服务的可扩展性和适应性。通过实施负载均衡方法，企业可以创建可扩展且高效的系统。

## 如何使用负载均衡

在微服务设置中进行负载均衡既棘手又至关重要，因为它直接影响系统可用性和性能级别。为了确保没有一个实例因用户请求而过载，并保持[操作，即使一个实例遇到问题](https://thenewstack.io/ai-powered-service-models-speed-troubleshooting/)，在各种服务实例之间分配最终用户请求至关重要。这涉及利用服务发现来精确定位动态负载均衡的情况，以适应负载变化，并实施容错健康检查以监控和将流量从故障实例中重定向，以维持系统稳定性。这些策略共同作用，以保证微服务设置的稳固和高效。

### 实施服务发现

1. **使用 Consul 进行服务注册和发现**：Consul 是一款服务网络工具，通过根据服务变更向负载均衡器分发更新，来协助动态基础设施。在微服务架构中，发现变得更加容易，因为 Consul 兼作服务注册和 DNS。HAProxy 和 Nginx 是集成简单的负载均衡器，服务可以使用 [少量配置](https://developer.hashicorp.com/consul/tutorials/archive/load-balancing-haproxy) 直接寻址服务。Consul 节点的架构布局使得跨多个数据中心环境的分布式 Consul 集群对于可扩展的微服务架构是可行的。内部运行状况检查和简单的键值存储持续监控服务的可用性。
2. **Eureka 与 Consul**：**优缺点：**：一些著名的服务发现工具是 Netflix 开发的 Eureka 和 HashiCorp 的 Consul。对 Spring Cloud 的支持相对容易部署，并为涉及 Spring Cloud 负载均衡器 Ribbon 等功能的负载均衡的客户端提供合理的支持。同时，Consul 与多中心环境配合得很好，被认为更灵活、功能更丰富，并且专为服务发现和 [DNS 解析](https://stackshare.io/stackups/consul-vs-eureka) 而设计。同时，尽管 Eureka 需要外部工具来配置安全性，但它包含精细的方面，如集成运行状况监控，这使得 Consul 更适合执行详细服务发现管理的企业。

**Eureka 与 HashiCorp**

| 功能/方面 | Eureka（Netflix） | Consul（HashiCorp） |
|---|---|---|
| 集成 | 与 Spring Cloud 和 Ribbon 强集成，用于客户端负载均衡。 | 专为更广泛的环境设计，支持多数据中心设置。 |
| 灵活度 | 灵活度较低，主要适用于 Spring Cloud 环境。 | 高度灵活且功能丰富，支持各种基础设施。 |
| 服务发现 | 主要专注于客户端服务发现和负载均衡。 | 提供服务发现和基于 DNS 的解析，使其更通用。 |
| 运行状况监控 | 内置运行状况监控，但某些安全配置需要其他工具。 | 包括集成运行状况监控，使其适用于详细的服务发现管理。 |
| DNS 支持 | 没有本机 DNS 支持。 | 服务的本机 DNS 解析，简化了服务发现。 |
| 最佳用例 | 适用于基于 Spring 的微服务生态系统。 | 适用于具有多数据中心和多云环境的大型企业。

### 动态负载均衡技术

微服务架构旨在将应用程序划分为独立的服务，以进行单独的部署和扩展。然而，这种分散的方法对处理服务之间的流量提出了挑战。动态负载均衡方法在微服务架构中发挥作用，通过确保将请求分发到正确的服务实例，从而增强可扩展性、可靠性和对故障的弹性。

### 微服务的流行动态负载均衡技术

1. **具有自适应权重的轮询**：每个微服务都可以根据性能指标（如 CPU 利用率和内存使用率或其处理数据流量的效率）及时调整其权重。轮询策略经过定制，优先将流量路由到在发生变化条件时表现出更强适应性的微服务。
2. **感知延迟的负载均衡**：在微服务设置中，对延迟敏感的应用程序（如提供 API 的应用程序）在根据响应方式定向流量时具有优势。负载均衡器会跟踪每个服务节点的响应时间。它会动态地将流量引导到最适合处理请求的节点。此策略通常使用微服务设置中的流行代理服务器 [Envoy](https://www.envoyproxy.io/) 或 [Linkerd](https://linkerd.io/) 来实现。
3. **有状态服务的哈希一致性**：在处理需要保持会话或在一段时间内管理状态信息的微服务时，使用哈希方法处理连接到它们的请求或客户端之间的请求，以确保从客户端或类型的请求始终如一地定向到相应的服务实例，这有助于均匀地分配流量，同时还跟踪这些服务执行的操作或任务的状态。此方法适用于缓存系统（如 Redis）和其他在操作期间依赖于维护状态的微服务。
4. **具有动态监控的最小连接**：此方法将流量定向到具有最小连接数的微服务实例；在某些服务需要更大的处理能力来处理每个请求的情况下，此方法效果很好。动态监控功能使负载均衡器能够评估连接负载并对路由决策进行实时调整。
5. **为微服务负载均衡配置 Nginx**：Nginx 是一个灵活的反向代理服务器，可将流量转发到多个微服务实例。至于为微服务配置具有负载均衡功能的 Nginx，可以在 [Nginx 配置文件](https://shape.host/resources/load-balancing-microservices-with-nginx-in-docker-environment) 中指示多个后端服务器。Nginx 负载均衡器支持轮询、最小连接和 IP 哈希平衡算法，并希望有不同的流量模式。Nginx 可以通过利用其内置的运行状况检查机制从负载均衡池中消除不健康的实例，并保证流量的平稳分配。
6. **使用 Ribbon 实现客户端负载均衡**：Ribbon 是一个客户端负载均衡器，主要与使用 Spring Cloud 构建的应用程序相关。这有助于通过提供特定的算法（如轮询或加权响应时间）来覆盖流量控制，而无需使用外部负载均衡器。Ribbon 使用 Eureka 或 Consul 进行服务发现，选择一个健康的实例来处理流量，从而提高了 [系统的冗余性](https://www.nexsoftsys.com/articles/client-side-load-balancing-using-spring-ribbon.html#:~:text=Technology%3A%20Ribbon%20is%20the%20client)。对于小规模微服务架构来说，它非常宝贵，因为它可以避免额外的负载均衡器层。

## 运行状况检查和容错

1. **设置断路器 Hystrix**：Hystrix 是 Netflix 创建的工具，用于管理微服务设置中部分的延迟和错误，以提高系统可靠性和正常运行时间效率。通过使用断路器及时监视每个微服务的运行状况，Hystrix 可以在 [发现故障](https://github.com/afex/hystrix-go) 时切断请求。这种主动方法通过将流量定向到预先设置的操作来帮助避免故障，从而确保一个服务的问题不会影响整个应用程序的性能。Hystrix 断路器功能有助于隔离故障，以便在某些服务暂时无法工作时，系统其余部分可以继续运行。
2. **有效实施重试和超时**：策略性地实施超时和重试对于确保微服务的容错性和对网络问题的弹性至关重要。重试通过重复请求尝试来帮助管理网络故障；另一方面，超时可防止无响应服务导致长时间延迟。通过 Ribbon 管理的客户端重试和超时以及通过 Nginx 控制的服务器端配置有效地提高了可靠性。与仅依赖默认 [超时设置](https://blog.nginx.org/blog/creating-nginx-rewrite-rules) 相比，提供了鲁棒性。将这些方法与 Hystrix 系统架构中的断路器功能相结合，通过各种容错机制（如重试、超时和断路器）防止宕机并有效地控制问题，从而提高了可靠性。这些元素帮助系统适应网络不可预测性并独立解决故障，从而促进了强大且有弹性的微服务框架。
3. **通过集中监控提高系统可靠性**：ELK 堆栈（Elasticsearch、Logstash、Kibana）、Prometheus 和 Grafana 等日志记录和监控工具提供了对服务性能指标（如请求延迟和错误率）的监控。通过创建警报，团队可以在问题影响用户之前采取措施来解决问题。这种广泛的监督通过查明瓶颈并促进快速解决问题来提高系统弹性。
4. **主动弹性测试的混沌工程**：混沌工程涉及使用 Netflix Chaos Monkey 等工具在受控环境中复制故障。随着团队故意引入中断，他们可以评估容错机制的有效性。发现弱点以增强弹性。此方法通过确保可靠且高效的容错策略，为系统做好应对挑战的准备。

## 优化微服务中的 API 性能

API 网关用作入口点，所有用户都可以通过该入口点提交其请求并根据请求的内容将其路由到微服务。它处理与其他问题相交的各种任务，如安全检查、身份验证速率限制问题和监控能力

### 1. 设置 Kong API 网关的分步指南

Kong 是一个著名的开源 API 网关。以下是如何快速入门：

a) 要安装 Kong，请使用软件包管理器，如 brew（适用于 macOS）或 apt（适用于 Ubuntu）。
b) 设置数据库：默认情况下，Kong 使用 PostgreSQL。更新 Kong 的配置文件并设置数据库。
c) 运行迁移：执行 `kong migrations bootstrap` 以配置数据库架构。
d) 启动 Kong：要启动网关，请键入 `run kong start`。
e) 添加服务：要添加新服务，请使用 Kong 的 Admin API。

```
curl -i -X POST http://localhost:8001/api_uri \
--data name=my-service \
--data url='http://app-service-domain:port'
```

f) 添加路由：将服务链接到路由：

```
curl -i -X POST http://localhost:8001/api_uri/app-service/routes \
--data 'paths[]=/my-route'
```

现在，对 `/my-route` 的请求将转发到您的服务。

### 2. 实施速率限制和节流

速率限制保证公平使用并有助于阻止 API 滥用。在 Kong 中：

激活限制速率的插件：

```
curl -i -X POST http://localhost:8001/api_uri/my-service/plugins \
     --data "name=rate-limiting" \
     --data "config.minute=5" \
     --data "config.hour=1000"
```

通过此配置，客户端可以每分钟向 `my service` 发出最多 5 个请求，每小时最多发出 1000 个请求。如果超过这些限制，Kong 将返回 HTTP 状态代码（通常为 429 请求过多）以指示已达到速率限制。高级节流插件可以根据各种条件应用限制，以满足更复杂的速率限制需求，从而对请求处理提供细粒度控制。此插件允许根据用户角色、IP 地址和时间窗口等因素进行配置，从而进一步帮助优化和保护 API 使用。

## 异步通信模式

在微服务设计中，异步通信可以显著提高可扩展性和性能。

### 使用 Apache Kafka 实现事件驱动架构

1. 安装并启动 Zookeeper 和 Kafka 服务器。
2. 生成主题：要生成新主题，请使用 `kafka-topics.sh`。
3. 设置生产者：在微服务中使用 Kafka 的生产者 API 发布事件：

```java
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
Producer&lt;String, String&gt; producer = new KafkaProducer&lt;&gt;(props);
producer.send(new ProducerRecord&lt;&gt;("my-topic", "key", "value"));
```

4. 设置消费者：其他服务可以消费这些事件：

```java
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("group.id", "my-group");
props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
 
KafkaConsumer&lt;String, String&gt; consumer = new KafkaConsumer&lt;&gt;(props);
consumer.subscribe(Arrays.asList("my-topic"));
 
while (true) {
 ConsumerRecords&lt;String, String&gt; records = consumer.poll(Duration.ofMillis(100));
 for (ConsumerRecord&lt;String, String&gt; record : records) {
  System.out.printf("offset = %d, key = %s, value = %s%n", record.offset(), record.key(), record.value());
 }
}
```

## 使用 RabbitMQ 实现请求-响应模式

RabbitMQ 非常适合传统消息模式。但是，Kafka 更适合事件流：

1. 使用 Docker 或包管理器安装 RabbitMQ。
2. 建立队列：使用 RabbitMQ 的客户端库或管理界面。设置请求者：

```java
ConnectionFactory factory = new ConnectionFactory();
factory.setHost("localhost");
try (Connection connection = factory.newConnection();
    Channel channel = connection.createChannel()) {
    String replyQueueName = channel.queueDeclare().getQueue();
    String corrId = UUID.randomUUID().toString();
    AMQP.BasicProperties props = new AMQP.BasicProperties.Builder()
        .correlationId(corrId)
        .replyTo(replyQueueName)
        .build();
 
    channel.basicPublish("", "rpc_queue", props, message.getBytes());
<em>    
    // ... wait for response on replyQueueName</em>
}
```

- 实现响应者：

```java
ConnectionFactory factory = new ConnectionFactory();
factory.setHost("localhost");
try (Connection connection = factory.newConnection();
    Channel channel = connection.createChannel()) {
    channel.queueDeclare("rpc_queue", false, false, false, null);
    channel.basicQos(1);
 
    Object monitor = new Object();
    DeliverCallback deliverCallback = (consumerTag, delivery) -&gt; {
        AMQP.BasicProperties replyProps = new AMQP.BasicProperties.Builder()
            .correlationId(delivery.getProperties().getCorrelationId())
            .build();
 
        String response =<em> // ... generate response</em>
 
        channel.basicPublish("", delivery.getProperties().getReplyTo(), replyProps, 
    response.getBytes());
        channel.basicAck(delivery.getEnvelope().getDeliveryTag(), false);
 
        synchronized (monitor) {
            monitor.notify();
        }
    };
 
    channel.basicConsume("rpc_queue", false, deliverCallback, consumerTag -&gt; { });
 
    while (true) {
        synchronized (monitor) {
            try {
                monitor.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

在实际场景中实现这些模式时，这些模式可以帮助开发人员提高其在微服务上运行的 API 的效率和性能，以有效管理预期的增加的流量。API 网关作为入口点，允许服务之间的通信方法，从而取代同步通信方法。

## 微服务与单体：性能比较

单体应用程序通常采用集中式缓存方法，其中数据在单个级别上硬件化。对于简单的架构来说，这是可以的，但随着[参数增加](https://hatchworks.com/blog/software-development/monolithic-vs-microservices/#:~:text=Scalability%20and%20Performance%20Needs%3A&text=Monolithic%3A%20Scaling%20means%20scaling%20the)，速度会变慢。另一方面，微服务使用分布式缓存，其中缓存位于每个服务附近。这种分散化提高了数据可访问性，降低了延迟，并增加了缓存内聚性和一致性问题。因此，如果要扩展实际应用程序而不因性能不佳而遭受损失，分布式缓存非常重要。

一些软件定义网络具有单体结构，其中负载均衡器的概念是僵化的，固定在核心。另一方面，微服务使用客户端和服务器端负载均衡，并且流量可以在服务的不同实例之间均匀分布。这使得扩展微服务、在出现拥塞时创建新实例以及提高系统的功能和鲁棒性变得容易。

随着 API 变得更大，性能也可能成为单体应用程序中的问题；每个请求都必须经过所有层。它的响应时间是单体结构的两倍，因为请求可以被定向到相应且经过优化的服务。在微服务架构中，吞吐量通常甚至高于单体应用程序，因为流量不会像大量单个服务那样高度集中，从而可以有效利用资源，并且在高流量情况下不太可能出现宕机。

| 方面 | 单体架构 | 微服务架构 |
|---|---|---|
| 缓存效率 | 集中式缓存，其中所有软件都缓存在一个位置。适用于小规模应用程序，但随着系统扩展，它可能会出现问题。 | 分布式缓存为每个服务创建了许多本地定制的缓存，从而提高了数据可用性并降低了延迟。但是，它也可能引发一致性和连贯性问题。 |
| 负载均衡 | 静态、集中式负载均衡。灵活性有限，在高负载下可能导致潜在瓶颈。 | 动态负载均衡，既有客户端（例如 Ribbon）又有服务器端（例如 Nginx）。支持自主服务可扩展性，提高系统稳健性和灵活性。 |
| API 响应时间和吞吐量 | 由于 API 查询涉及完整的堆栈遍历，因此延迟会随着应用程序大小而增加。由于单体结构无法同时管理多个请求，因此吞吐量受到限制。 | API 引导用户使用特定且经过优化的服务。通过增强的缓存和负载均衡，系统可以管理更大的吞吐量，提高性能，更有效地利用可用资源，并减少宕机。 |

*表 1. 基于缓存效率、负载均衡和 API 响应时间比较微服务和单体架构的性能。*

## 结论

以受控方式从单体架构迁移到微服务架构可以实现多种好处。本文讨论了平衡负载的方法，例如利用 Consul 进行服务发现、使用 Nginx 进行负载均衡以及使用 Ribbon 进行客户端负载均衡。涵盖的其他主题包括设置 API 网关和实现通信模式，为高效的微服务创建基础。

这些技术、API 网关实现和异步通信模式构成了高效微服务的有力基础。借助分布式缓存、智能负载均衡和事件驱动的系统设计，微服务在性能、可扩展性和弹性方面优于当今的单体架构。后者在资源利用和响应时间方面效率更高，因为可以根据需要扩展各个组件。

但是，必须记住，此处引入的性能改进类型意味着更高的复杂性。其实现是一个复杂的过程，需要反复监控和优化。如果实施得当，最终产品可以承受更大的容量，并且可以进一步扩展，并且比单体类型具有更好的工作负载和用户界面适应性。展望未来，微服务架构正在稳步发展。新的云形态和卓越的 AI 优化解决方案可能会进一步坚持建立有机、高效、可扩展且响应迅速的 API 平台。

本文是 The New Stack 的贡献者网络的一部分。对影响开发人员的最新挑战和创新有见解吗？我们很乐意听取您的意见。通过填写此表格或向 mattburns@thenewstack.io 发送电子邮件，成为贡献者并分享您的专业知识。
