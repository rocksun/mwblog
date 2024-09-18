# Testcontainers 是什么，你为什么应该关心？
![Testcontainers 是什么，你为什么应该关心？的特色图片](https://cdn.thenewstack.io/media/2024/09/d2ea2f8b-what-are-testcontainers-1024x576.jpg)

在现代软件开发中，随着分布式系统和 [微服务架构](https://thenewstack.io/microservices/) 的持续趋势，以及巨大的集成界面，编写软件也意味着与其他系统集成。集成测试是确保被测系统持续正确性的绝佳工具，并且可以在开发周期中提供系统行为的快速且持续的反馈。

然而，集成测试通常需要外部依赖项，例如数据库、消息代理或 Web 服务器，所有这些依赖项都有自己的配置和正确运行的特殊性。传统上，管理这些依赖项很麻烦，容易出现不一致，并且难以在不同机器上复制。

从历史上看，这使得集成测试因编写和维护成本高而声名狼藉。你要么必须遵循可能过时的文档以费力的手动方式设置环境（最终只得到一个略微损坏的环境），要么使用集中维护的共享测试环境，这通常会导致测试污染。

这就是 [Testcontainers](https://testcontainers.com/) 的用武之地。我的同事 [Oleg Šelajev](https://2024.allthingsopen.org/speakers/oleg-selajev) 将在 All Things Open 2024 上以“ [制作你自己的 Testcontainers 模块，既有趣又有利可图！](https://2024.allthingsopen.org/sessions/making-your-own-testcontainers-module-for-fun-and-profit)”为题的演讲中展示这一点。

## 了解 Testcontainers

Testcontainers 是一个开源库，用于提供一次性、轻量级的数据库、消息代理、Web 浏览器或几乎可以在 Docker 容器中运行的任何东西的实例。通过利用 [Docker](https://www.docker.com/?utm_content=inline+mention) 根据需要从你的代码库中启动这些服务的轻量级、隔离的实例，Testcontainers 解决测试和开发期间的环境管理问题。

Testcontainers 允许开发人员使用 [基础设施即代码 (IaC)](https://thenewstack.io/infrastructure-as-code/) 方法，以最小的工作量创建可靠且可重复的测试和开发环境。它使用熟悉的语言编写生产和测试代码，并帮助确保代码针对真实、一致的服务进行测试。这种方法减少了设置和拆除测试环境的摩擦，并使测试更可靠、更容易维护。对于开发人员来说，Testcontainers 是一款改变游戏规则的产品，它简化了测试过程，并实现了更自信、更稳健的开发。

### 清理

Testcontainers 还会自动清理它创建的所有 [Docker](https://roadmap.sh/docker) 资源，确保你的系统在运行测试后保持整洁。此清理过程与你正在使用的测试框架（例如 JUnit）无缝集成，其中容器会在测试执行后自动停止并删除。

此外，Testcontainers 依赖于一个名为 [Ryuk](https://hub.docker.com/r/testcontainers/ryuk) 的专用辅助容器，它会监视并确保所有资源都得到正确清理，即使在测试进程可能崩溃或意外终止的情况下也是如此。通过将此清理过程绑定到测试进程的生命周期，并使用 Ryuk 作为监视程序，Testcontainers 保证不会留下任何杂散容器、网络或卷，从而保持你的环境清洁，并最大程度地降低后续测试运行中资源耗尽或冲突的风险。

### 模块

Testcontainers 提供了一组丰富的模块，其中封装了在测试上下文中使用容器的最佳实践，从而使将各种技术集成到你的测试套件中变得更加容易。这些模块是针对特定技术（例如数据库（例如 [PostgreSQL](https://roadmap.sh/postgresql-dba)、MySQL）、消息代理（例如 [Kafka](https://thenewstack.io/top-10-tools-for-kafka-engineers/)、RabbitMQ）甚至像 Selenium 这样的用于浏览器测试的成熟应用程序环境）定制的预配置 Docker 容器。

通过使用这些模块，开发人员可以利用经过尝试和测试的配置，这些配置针对测试场景中的可靠性和效率进行了优化。[Testcontainers 模块目录](https://testcontainers.com/modules/) 提供了可用模块的全面列表，使你能够快速查找和实现所需的容器化服务。

以下两个最小示例展示了在
[Java](https://thenewstack.io/java/) 和 [Go](https://thenewstack.io/go/)：如何使用 [Redis](https://redis.com/?utm_content=inline+mention) 镜像定义 Docker 容器，配置其公开端口，并以等待容器内 Redis 应用程序就绪的方式启动容器。

在 Java 中：

```
GenericContainer redis = new GenericContainer("redis:5.0.3-alpine")
    .withExposedPorts(379);
redis.start()
```

在 Go 中：

```
container, err := testcontainers.GenericContainer(ctx, testcontainers.GenericContainerRequest{
    ContainerRequest: testcontainers.ContainerRequest{
        Image: "redis:5.0.3-alpine",
        ExposedPorts: []string{"6379/tcp"},
        WaitingFor: wait.ForLog("Ready to accept connections"),
    },
    Started: true,
})
```

### Testcontainers Cloud

除了这些广泛建立的开源库之外，Testcontainers 还提供了一个产品，可以将这些容器无缝地卸载到云中，而无需对 Testcontainers 代码进行任何更改：

[Testcontainers Cloud](https://testcontainers.com/cloud/)。通过利用 Testcontainers Cloud，您可以显著减少本地计算机上的负载，释放资源以执行其他任务，同时仍然运行复杂、资源密集型的测试。

这种方法可以加快您的开发工作流，并使您的测试环境与所需的 Docker 运行时（例如，x86）具有架构同等性，因为容器是在一致且可扩展的云环境中执行的。无论您是处理繁重的工作负载还是只想简化测试流程，Testcontainers Cloud 都提供无缝集成，既能提高性能，又能提高可靠性，让您能更多地专注于编码，而无需管理本地资源。

## 总结

Testcontainers 是一款多功能且强大的工具，它改变了开发人员处理集成测试和本地开发的方式。通过提供一个易于使用的界面来启动针对特定测试需求量身定制的 Docker 容器，并且可以直接从所用编程语言的熟悉性中访问，Testcontainers 消除了与管理测试环境相关的常见挑战。

借助封装最佳实践的模块、自动清理以保持系统整洁以及将容器执行卸载到 Testcontainers Cloud 的能力，这种方法为在测试流程中保持一致性、可靠性和效率提供了一个全面的解决方案。

无论您是希望简化本地工作流的开发人员，还是旨在扩展云中测试的团队，Testcontainers 都为您提供了必要的工具，以确保您的代码在不同环境中无缝运行。通过采用 Testcontainers，您不仅可以提高测试质量，还可以为更强大、更自信的开发周期铺平道路。

**不要错过我们的 All Things Open 2024 会议：制作您自己的 Testcontainers 模块，既有趣又有利可图！**

## 了解更多信息

- 有关最新 Testcontainers 新闻，请订阅
  [Docker 时事通讯](https://www.docker.com/newsletter-subscription/)。
- 通过
  [创建免费帐户](https://testcontainers.com/cloud) 开始使用 Testcontainers Cloud。
- 有关 Testcontainers 的问题？在
  [Testcontainers Slack](https://testcontainers.slack.com/) 上联系。
- 了解
  [Testcontainers 最佳实践](https://www.docker.com/blog/testcontainers-best-practices/)。
- 开始使用
  [Testcontainers 指南](https://testcontainers.com/getting-started/)。
- Docker 新手？
  [开始](https://docs.docker.com/desktop/)。 [
  YOUTUBE.COM/THENEWSTACK
  技术发展迅速，不要错过任何一集。订阅我们的 YouTube
  频道以流式传输我们所有的播客、访谈、演示等。
  ](https://youtube.com/thenewstack?sub_confirmation=1)