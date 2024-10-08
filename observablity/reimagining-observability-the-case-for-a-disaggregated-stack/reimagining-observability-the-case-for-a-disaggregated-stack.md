
<!--
title: 重新构想可观测性：分散式堆栈的案例
cover: https://cdn.thenewstack.io/media/2023/11/3127850d-unreliable-observability-costs.jpg
-->

在现代分布式架构中采用解耦的 o11y 堆栈，在成本效益和可重用性方面具有显著优势。

> 译自 [Reimagining Observability: The Case for a Disaggregated Stack](https://thenewstack.io/reimagining-observability-the-case-for-a-disaggregated-stack/)，作者 Neha Pawar。

[可观测性](https://thenewstack.io/observability/), 通常缩写为 o11y，对于[理解系统的状态和行为](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/)至关重要，它通过收集、处理和分析遥测数据来实现。然而，在 2024 年，我观察到传统的 o11y 堆栈正在失去吸引力，现在是时候采用分散式 o11y 堆栈了。

[分散式堆栈有关键优势](https://thenewstack.io/rethinking-observability/)，例如灵活性、数据自治、可扩展性和成本效益。此外，对于数据团队来说，还有一些可操作的建议和蓝图，用于构建他们的数据架构以采用这种分散式模型。

![](https://cdn.thenewstack.io/media/2024/08/74975976-picture1.png)

## 可观测性堆栈

以下是典型 o11y 堆栈的结构：

- **代理**：这些进程与您的微服务和应用程序一起运行在您的基础设施上，收集 o11y 数据并将其发送到中心位置以进行进一步分析。
- **收集**：此层收集来自所有不同代理的传入数据，并促进其传输到后续层。
- **存储和查询**：此层存储来自收集步骤的数据，并使其可供查询。
- **可视化**：这包括用于查询此数据的应用程序，例如用于指标可视化、监控、警报、日志探索和分析的工具。

当今 o11y 领域中突出的解决方案包括 Datadog 和 Splunk 等技术。

## 分散式堆栈的兴起

**问题和机遇**

当今可用的 o11y 解决方案的两个主要问题是**灵活性不足**和高**成本**。这些问题源于提供商通常提供非此即彼的解决方案。例如，虽然 Datadog 提供全面的监控功能，但我们无法使用该平台来生成相同数据的实时洞察。类似地，一些解决方案专注于端到端解决方案，可能需要针对高效存储和查询计算进行优化，从而以简单性为代价换取成本。

![](https://cdn.thenewstack.io/media/2024/08/8a9e7f85-picture1.png)

如今，许多公司正在转向分散式堆栈，它提供了以下关键优势：

- **灵活性**：公司通常拥有高度个性化的数据堆栈，并且可以选择适合其需求的每个层的特定技术。
- **可重用性**：数据是任何公司最重要的商品。通过分散式堆栈，他们可以构建一个平台来利用其数据集用于各种用例（包括可观测性）。
- **成本效益**：分散式堆栈允许选择存储优化的系统，从而降低整体服务成本。

![](https://cdn.thenewstack.io/media/2024/08/8ed7f844-picture1.png)

审查每个层，并了解分散式堆栈如何帮助克服相应问题。

**代理**

供应商在其代理方面投入了大量资金，这些代理针对其堆栈进行了定制，并具有特定的格式。这种特殊性增加了解决方案的整体成本。此外，不同的公司具有不同的数据治理要求，这可能需要额外的工作来适应专有代理。

与此同时，可观测性代理已成为商品，出现了 OpenTelemetry 等标准。这些标准使数据轻松发送到各种后端，消除了与特定后端绑定的特定格式的约束，并为堆栈的其余部分打开了无限的可能性。

![](https://cdn.thenewstack.io/media/2024/08/eda64dda-picture1.png)

**收集**

特定于供应商的收集系统需要能够处理以下挑战

- **容量**：各种规模的公司都会为日志和指标生成非常高的数据量。预计每天会生成数十或数百 TB 的数据。
- **多样性**：指标、日志和跟踪采用各种格式，可能需要特殊处理。
- **网络成本**：这些专有收集系统通常驻留在不同的云 VPC 中，从而增加了出口成本。

在分散式堆栈中，Kafka 和 RedPanda 等流式系统是收集层的热门选择，并且通常已经作为数据生态系统的一部分部署。许多知名组织已在规模上测试了这些系统，用于高吞吐量、实时摄取用例。例如，Kafka 已知在 LinkedIn 和 Stripe 等组织中达到每秒 100 万+ 事件的规模。这些系统与代理格式无关，可以轻松与 OTEL 或其他格式交互。它们还具有良好的连接器生态系统，并与存储系统具有原生集成。

![](https://cdn.thenewstack.io/media/2024/08/b0353e89-picture1.png)

**存储和查询**

存储和查询层是最具挑战性的部分，对系统的成本、灵活性和性能有重大影响。当今解决方案的存储和查询层的一个主要问题是缺乏灵活性，无法将数据用于其他目的。在全有或全无的解决方案中，一旦数据进入供应商的堆栈，它基本上就被锁定。您无法使用数据存储在它之上构建其他应用程序。

另一个方面是 o11y 规模的成本和性能。存储和查询系统必须以极高的速度处理海量数据。数据的多样性意味着您将看到更多输入格式、数据类型和具有高基数维度的非结构化有效负载。这种多样性使得数据摄取到这些系统变得复杂，对最佳存储格式、编码和索引的需求变得很高。

![](https://cdn.thenewstack.io/media/2024/08/4b9bf8a2-picture1.png)

在去中心化堆栈的情况下，选择合适的存储系统至关重要。在做出此选择时，以下是一些需要考虑的事项。

**与实时源的集成**

系统必须与实时流式源（如 Kafka、RedPanda 和 Kinesis）无缝集成。可插拔架构至关重要，它允许轻松添加自定义功能，例如针对 Prometheus 或 OTEL 等专用格式的解码器，而无需付出太多努力。这种灵活性对于 o11y 数据尤其重要，因为它需要支持来自不同代理的各种数据格式。

**高效存储指标数据的能力**

以下是一个包含典型指标事件的示例，其中包含一个表示事件时间戳（以毫秒为粒度）的时间戳列、一个表示系统发出的指标的指标名称和值列，以及一个标签列。

![](https://cdn.thenewstack.io/media/2024/08/e5a23b8e-picture1-1024x577.png)

此类数据集存在一些挑战：

* **高基数列**：它们需要特殊处理，例如 Gorilla 编码以实现高效压缩。
* **各种索引技术**：范围索引、倒排索引或排序索引，用于高效查找和过滤时间戳、高度可变的指标值和指标名称。
* **高级数据布局**：能够对频繁访问的列进行分区，以最大程度地减少查询处理期间的工作量（仅处理某些分区）。
* **JSON 列支持**：“标签”列通常表示为包含各种维度名称-值对（例如：服务器 IP、Kubernetes 版本、容器 ID 等）的 JSON 映射。按原样摄取数据将把责任推卸给查询处理，然后需要进行运行时 JSON 提取。另一方面，在摄取时物化所有这些键也很具有挑战性，因为键是动态的并且一直在变化。

现有技术有一些解决方法来克服这些挑战。例如，Prometheus 将每个键值对视为一个唯一的时间序列，这简化了 JSON 处理，但会遇到可扩展性问题。在某些系统（如 DataDog）中，随着从这些标签中添加更多顶级维度，成本会增加。如果您使用键值存储，您将再次面临高组合爆炸和在实时数据同步时丢失新鲜度的风险。因此，您选择的存储系统能够处理如此高的基数以及复杂的数据类型和有效负载至关重要。

**高效存储日志数据的能力**

典型的日志事件包括时间戳和几个顶级属性（如线程名称、日志级别和类名），然后是一个大型非结构化文本有效负载，即日志行。对于时间戳和属性，您需要与指标数据所需的编码和索引功能类似的功能。日志消息本身是完全非结构化的文本。查询此非结构化文本涉及自由格式文本搜索查询，以及按其他属性进行过滤和执行聚合。因此，强大的文本索引功能对于高效处理正则表达式匹配和自由格式文本搜索至关重要。

![](https://cdn.thenewstack.io/media/2024/08/c8e9862b-picture1-1024x579.png)

存储整个日志消息会导致极高的日志数据量。由于合规性要求或离线分析和回顾，日志通常需要长期保留，从而导致巨大的存储需求（每天数十 TB）和巨大的成本。实用的压缩算法至关重要。例如，Uber 工程师开发的压缩日志处理器 (CLP) 旨在以高度可压缩的格式对非结构化日志消息进行编码，同时保留可搜索性。[CLP 在 Uber 的 Pinot 安装中被广泛采用，与原始日志相比，[CLP 在 Spark 日志上实现了 169 倍的压缩率](https://www.uber.com/blog/reducing-logging-cost-by-two-orders-of-magnitude-using-clp/)。

管理与大量数据相关的巨额成本的另一个重要功能是能够使用多种存储层，例如 SSD、HDD 和云对象存储。这种分层不应该以牺牲灵活性或增加运营负担为代价。理想情况下，系统应该原生处理分层和数据移动策略的复杂性。这对于 o11y 数据尤其重要，因为 o11y 数据通常需要长期保留，即使除了最近几天或几周之外的查询并不频繁。利用更具成本效益的存储来存储较旧的数据对于有效管理这些成本至关重要。

一些系统，例如 Loki，提供 100% 的对象存储持久性。其他系统，如 Clickhouse 和 Elastic，提供多个层级，但依赖于延迟加载等技术，这可能会导致严重的性能损失。像 Apache Pinot 这样的系统提供分层并应用高级技术，包括能够将部分数据（例如索引）本地固定以及使用块级获取和获取和执行的流水线，从而显着提高性能。

**跟踪数据的注意事项**

现在让我们谈谈跟踪事件。这些事件包含每个跨度的跨度调用图和相关属性。由于有效负载的半结构化、嵌套性质，在经济高效地存储这些数据并有效地查询它们时，会遇到类似于指标数据的挑战。对有效地摄取和索引这些有效负载的原生支持至关重要。

![](https://cdn.thenewstack.io/media/2024/08/1feb6117-picture1.png)

为了总结这些挑战，我们需要一个能够经济高效地处理 PB 级存储并管理长期保留的系统。它必须以高速摄取各种格式，并以高新鲜度和低延迟提供数据。该系统应该有效地编码和存储复杂的半结构化数据。强大的索引至关重要，因为优化性能和最小化工作负载的系统将更有效地扩展。

与一体化解决方案相比，专门为低延迟、高吞吐量实时分析而构建的系统（例如 Apache Pinot、Clickhouse、StarRocks 和 Apache Druid）更适合存储和查询 o11y 数据（有关此领域的流行系统的更多信息，请参阅 [此处](https://startree.ai/blog/a-tale-of-three-real-time-olap-databases)）。这些系统具有来自许多实时数据源的丰富的摄取集成，并且这些配方已被证明可以扩展到不同领域的用例。它们的列式存储使它们在最佳地处理存储方面更加高效，提供了各种编码和索引技术。许多提供了良好的文本搜索功能（例如，Elastic Search 以其免费文本搜索查询功能而闻名）。Apache Pinot 和 Clickhouse 还提供原生存储分层功能。

Apache Pinot 提供了一个蓝图，用于解决 o11y 的每一个细微差别，如下图所示。您还可以查看有关 [Apache Pinot 中的 o11y 策略](https://www.rtasummit.com/agenda/sessions/570394) 的技术演讲。

![Apache Pinot 中的可观察性功能](https://cdn.thenewstack.io/media/2024/08/0a383142-picture1.png)

*图：Apache Pinot 中的可观察性功能。*

它还具有一个可插拔的架构，可以轻松支持新格式、专门的数据类型和高级压缩技术。它有一个可靠的索引故事和高级索引故事，例如 JSON 索引，增强了它有效处理 JSON 有效负载的能力。成功的实际实施示例包括 Uber 和 Cisco，它们利用这些利基系统来增强其 o11y 解决方案，证明了它们在以高性能和成本效益管理大量数据方面的有效性。

**与可视化工具集成**

像 Grafana 这样的工具因其易用性和丰富的自定义选项而变得越来越流行，允许用户构建全面的仪表板。可用的窗口小部件从时间序列、热图、条形图、仪表等不等。此外，Grafana 支持使用广泛的自定义集成创建完整的应用程序。它为不同的后端提供灵活的可插拔连接器，避免供应商锁定。构建插件（无论是作为完整的连接器还是面板）都很简单。流行的存储系统，如 Clickhouse、Elastic 和 Pinot，都有 Grafana 插件。Grafana 还支持 LogQL 和 PromQL 等查询协议，这些协议越来越受欢迎。

![](https://cdn.thenewstack.io/media/2024/08/79a4a9c7-picture1.png)

另一个流行的工具是 Superset，它以其丰富的 UI 小部件以及易用性和自定义性而闻名。Superset 与许多流行的数据库无缝集成，允许用户快速创建和共享仪表板，并且与 Grafana 类似，它提供了广泛的图表功能。

## BYOC

之前，我们看到供应商解决方案成本高昂的原因之一是，将数据从您帐户中的代理传输到供应商帐户中堆栈的其他部分时，数据出站成本很高。对于支持 BYOC（自带云）的供应商，这个问题就消除了。代理和堆栈的其余部分都保留在您的帐户中，确保您的数据不会离开您的场所，从而避免与数据传输相关的额外成本。

## 结论

在现代分布式架构中采用解耦的 o11y 堆栈，在成本效益和可重用性方面提供了显著优势。通过解耦 o11y 堆栈的各个组件（例如代理、收集、存储和可视化），企业可以选择最适合特定需求的最佳解决方案。这种方法增强了灵活性，使组织能够集成像 Kafka、RedPanda、Clickhouse、Pinot、Grafana 和 Superset 这样的专业系统，这些系统在规模上已证明其能力。

解耦模型通过消除数据出站费用和利用更有效的存储解决方案，解决了与传统的一揽子供应商解决方案相关的成本过高问题。此外，独立使用不同层的灵活性促进了可重用性和数据自主性，防止数据锁定，并使组织能够更好地适应不断变化的需求。

通过采用解耦的 o11y 堆栈，组织可以实现更高的敏捷性，优化性能，并显着降低成本，同时保持扩展和调整其 o11y 解决方案以满足不断变化的业务需求的能力。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。