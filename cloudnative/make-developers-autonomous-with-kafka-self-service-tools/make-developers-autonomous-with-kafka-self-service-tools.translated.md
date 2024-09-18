# 使用 Kafka 自助服务工具让开发人员自主

![为以下内容提供特色图片：使用 Kafka 自助服务工具让开发人员自主](https://cdn.thenewstack.io/media/2024/06/21407506-make-developers-autonomous-kafka-self-service-tools-1024x576.png)

Apache Kafka 是一种灵活的实时数据流解决方案，用于开发和部署高响应应用程序和数据管道，但随着开发人员项目的范围和数量的增加，它可能会成为开发人员摩擦的根源。

资源需求、

[数据访问和安全需求](https://thenewstack.io/protect-sensitive-data-and-prevent-bad-practices-in-apache-kafka/)

早期阶段的 Kafka 项目通常很简单，并且可以由开发团队在内部进行管理。但是，在投入生产并扩展到多个团队时，站点可靠性工程 (SRE) 团队、数据平台团队或运营团队通常会接管 Kafka 基础设施维护，以及为开发团队提供数据访问服务。

引入其他流程通常会导致延迟和额外工作（例如填写请求工单），从而减慢 Kafka 的采用速度，并降低已经使用 Kafka 的开发人员的生产力。

然而，事情不必如此。摩擦不是流程的功能，而是其实施方式。完全有可能为开发人员提供高效开发 Kafka 应用程序所需的工具，以及与平台团队合作配置资源和自助服务数据请求的流程，而不会引入瓶颈。

## 管理不当的 Kafka 会降低开发人员的生产力

在

[扩展 Kafka 部署](https://www.conduktor.io/blog/scaling-kafka-securely-for-your-organization/)

时，有几个关键因素会增加开发流程的阻力：

**过度集中的治理：**虽然对数据的严格控制对于合规性是必要的，但结构不合理的治理会延迟资源访问和变更审批。

**不熟悉 Kafka：**不了解 Kafka 生态系统（Kafka、Kafka Connect、Kafka Streams、MirrorMaker）的全部范围以及这些组件如何交互的开发人员可能会减慢进度，尤其是在加速期间。

**孤岛和沟通障碍：**与其他团队沟通不畅（尤其是不知道谁拥有特定资源的所有权）以及对数据本身了解不足（例如，了解哪些指标有意义）会造成操作阻力。

除了这些主要问题之外，为生产部署增加复杂性层的灵活安全策略（例如加密，Kafka 中未提供开箱即用的加密）以及您自己的特定用例数据和法规要求可能会增加进一步的开发障碍。

为开发人员解决这些问题——在不向平台团队提出他们不可能满足的期望或将 Kafka 维护和治理任务推回给他们的情况下——提出了一个挑战。

## 可以解决减速问题的 Kafka 自助服务工具

每个应用程序都有自己的规范、工作流和支持基础设施，这些将决定

[使用哪些工具是合适的](https://thenewstack.io/top-10-tools-for-kafka-engineers/)

。但是，您应该考虑在 Kafka 环境中引入一些关键组件，这些组件将提高开发人员的响应能力。

### 探索和故障排除

开发人员必须了解他们处理的数据，以便他们能够快速识别其代码中错误或意外结果的来源。他们应该采用适合其工作流的工具来实现此目的：

- 命令行界面 (CLI) 工具，如

[kcat](https://github.com/edenhill/kcat)、[kafkactl](https://github.com/deviceinsight/kafkactl)

和

[kafka-console-consumer](https://www.conduktor.io/kafka/kafka-consumer-cli-tutorial/#How-to-Consume-Data-in-a-Kafka-Topic-using-the-CLI?-0)

可以检查 Kafka 数据。

- UI 工具，如

[Conduktor](https://www.conduktor.io/)、[AKHQ](https://akhq.io/)

和

[Kafka-UI](https://github.com/provectus/kafka-ui)

提供其他功能和增强的开发人员体验。

### 监控和警报

需要定期评估基础设施可用性以及代码更新的性能和操作影响，以便持续开发不会影响生产可靠性。

[Prometheus](https://prometheus.io/)、[Burrow](https://github.com/linkedin/Burrow)

和

[Datadog](https://www.datadoghq.com/)

为监控 Kafka 部署提供了强大的组件。

### 所有权和发现
[Atlan](https://atlan.com/) 和 [OpenMetadata](https://open-metadata.org/) 是数据目录，可帮助开发者发现和浏览数据以检测模式并回答问题。对于大型组织，[Alation](https://www.alation.com/) 和 [Collibra](https://www.collibra.com/) 提供企业级数据智能平台，可对广泛的数据资产进行分类和保护。

数据所有权最佳实践可以反映在你的 [GitOps](https://thenewstack.io/gitops-for-kafka-at-scale/) 进程中。[记录有关资源的元数据](https://www.conduktor.io/blog/data-chaos-clarity-tag-everything-everywhere/)，包括其所有者，以便在创建资源后立即了解资源是什么以及谁负责该资源，从而消除查找资源和查找资源负责人的障碍。

### 数据集成

从多个来源集成数据或将数据移至其他团队或组织可以集成数据的某个位置是许多 Kafka 用例的功能。对于许多业务应用程序和数据共享用例，开发者需要拥有 Kafka Connect 进程（如 [Debezium](https://debezium.io/)) 的所有权，以便应用程序可以侦听状态和事件中的更改。务必确保配置和连接器让开发团队能够访问独立操作所需的一切，而不会授予他们过于广泛的访问权限。

另一种方法是管理连接器的中央团队。但是，如果没有每个特定应用程序和用例的完整上下文和理解，这可能会产生与预期相反的效果，即通过要求团队之间进行额外的来回沟通来降低效率，直到获得所需的访问权限和共享理解。

## 更自主开发团队的最佳实践

自助服务工具不是万能药，无法解决困扰开发工作流的组织问题。应实施代码配置（[GitOps](https://thenewstack.io/gitops-for-kafka-at-scale/)）和基础设施的 CI/CD，以帮助确保可靠且可重复的开发和测试环境——但对于 Kafka 和非 Kafka 都是如此。

你的团队成员还应对你的客户端配置有功能性理解，以避免配置错误：Kafka 生产者和消费者行为（批处理大小、缓冲区大小、超时）会影响 Kafka 性能，如果配置不正确，可能会导致资源使用过多、延迟增加和吞吐量降低。

在规划应用程序时，不言而喻，你应该仔细识别用例和要求，并选择适当的设计模式（例如编排、编舞、事件驱动、流处理或压缩/保留架构）。还应预先规划能够满足应用程序要求（尤其是在使用 Kafka 进行事件溯源的事件驱动架构中）的弹性和可扩展基础设施。

你的项目在早期阶段累积的技术债务越少，开发者花在验证数据管道是否正确实施以及正确的人员是否可以在没有技术或流程延迟的情况下访问所需数据上的时间就越多。

## 找到推动开发者成果的正确方法

学习工具和建立上述实践对于任何单个开发者或团队来说都是一项艰巨的任务。大多数产品都没有紧密集成，它们缺乏总体治理功能可能会导致理解和所有权不佳，并导致数据处理不当。

你可能一开始只采用其中一些工具或不同的工具。但是，无论你选择哪些特定的软件和工程实践，都可以使用一些原则来推动开发者获得无摩擦体验：
**实施有助于而非阻碍的防护措施：**在仅包含他们所需数据的限定上下文中赋予您的开发人员自主权。这可以减少错误，并帮助您遵守 GDPR 和加州消费者隐私法 (CCPA) 等隐私法规。

**优化 Kafka 基础设施以有效管理成本：**Kafka 成本可能会迅速变得昂贵。数据复制流程会创建多个真实来源，每个来源都需要基础设施和维护。虽然复制有时是必要的，通常是为了 [与第三方合作伙伴共享数据子集](https://www.conduktor.io/blog/sharing-data-with-partners/)，但如果可以通过其他方式（例如，使用严格控制的访问或 [虚拟化](https://www.youtube.com/watch?v=arbIMGEwPkw)）提供服务，那么值得对此提出质疑。

**提供强大的安全控制：**授予数据访问权限的平台必须提供创建和实施强大安全策略以及 [保护用户数据](https://thenewstack.io/protect-sensitive-data-and-prevent-bad-practices-in-apache-kafka/)（使用编辑和个人身份信息 (PII) 掩码）的机制。

而且，在更高的层面上：在设计您的应用程序及其支持的基础设施时，目标应该是促进自助服务和协作，而不是将责任从运维团队转移出去。开发人员需要自由，而运维团队需要知道他们的 Kafka 部署正在被正确使用，而无需对每个访问请求进行微观管理。

## 了解有关开发人员自主权和 Kafka 的更多信息

如果您想了解有关识别 Kafka 生态系统中的扩展挑战的更多信息，请查看我们的 [Conduktor 2.0 网络研讨会](https://www.conduktor.io/webcasts/conduktor-2-0-the-new-standard-for-teams-working-with-kafka/)，了解 Conduktor 如何解决团队和组织在处理大规模实时数据时面临的自助服务问题，从而缩短交付时间并从数据投资中获得更多价值。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。