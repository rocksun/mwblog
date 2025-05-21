<!--
title: 两全其美：Confluent整合流处理和批处理
cover: https://cdn.thenewstack.io/media/2025/05/6f195642-confluent.png
summary: Confluent推出快照查询，融合实时流处理与历史批处理，加速AI应用！基于Confluent Cloud for Apache Flink，结合Kafka topics与Iceberg/Delta Lake数据，优化查询性能。支持agentic AI和实时应用，提升开发者效率，简化数据混合，加速欺诈检测等用例。
-->

Confluent推出快照查询，融合实时流处理与历史批处理，加速AI应用！基于Confluent Cloud for Apache Flink，结合Kafka topics与Iceberg/Delta Lake数据，优化查询性能。支持agentic AI和实时应用，提升开发者效率，简化数据混合，加速欺诈检测等用例。

> 译自：[Best of All Worlds: Confluent Synthesizes Streaming and Batch Processing](https://thenewstack.io/best-of-all-worlds-confluent-synthesizes-streaming-and-batch-processing/)
> 
> 作者：Jelani Harper

数据流平台提供商 [Confluent](https://www.confluent.io/?utm_content=inline+mention) 今天发布了一项新功能，允许用户通过单个查询分析实时和历史数据。快照查询通过 [Confluent Cloud for Apache Flink](https://thenewstack.io/confluent-cloud-gets-apache-flink-tables/) 抢先体验版提供，它结合了批处理和流数据方法，以支持具有丰富数据的低延迟用例。

Confluent 还发布了 [Apache Flink](https://thenewstack.io/apache-flink-2023-retrospective-and-glimpse-into-the-future/) 工作负载的 IP 过滤功能，并增强了 Flink 的专用网络功能。

快照查询将来自 [Kafka topics](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/) 的数据与在 Tableflow 的 [Iceberg or Delta](https://thenewstack.io/the-open-format-movement-heats-up-snowflake-embraces-apache-iceberg/) 表中具体化的上下文数据混合在一起。用户可以从 Databricks 和 [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) 等环境查询此开放表格式数据。但是，用户无需依赖两个不同的系统（以及两套成本）来查询 Kafka topic 数据和以开放表格式具体化的数据，而是可以使用 Confluent Cloud 的资源来执行此操作。

对于希望构建 [agentic AI systems](https://thenewstack.io/how-ai-agents-will-transform-devops-workflows-for-engineers/)、实时应用程序和事件处理工作负载的开发人员来说，快照查询尤其有利，在这些工作负载中，最新数据需要历史数据丰富。新功能还有助于开发人员了解哪些历史数据对其实时用例最有意义。

Confluent 产品营销总监 [Jean-Sébastien Brunner](https://www.linkedin.com/in/jsbrunner) 评论说：“通过快照查询，您可以真正快速地查询所有这些数据并以交互方式进行开发。“为正确的项目找到正确的查询可能需要花费大量时间。因此，通过使用快照查询，您可以真正帮助您的开发人员更有效地编写该查询。”

## 数据混合

快照查询基于 [Confluent Cloud for Apache Flink](https://www.confluent.io/product/flink/) 的几个方面。它们依赖于基于 Flink 的查询优化器，该优化器确定查询的哪些数据来自 Kafka topics，哪些数据来自上述开放表格式。该功能利用 [Tableflow](https://www.confluent.io/blog/introducing-tableflow/) 在 Iceberg 和 Delta Lake 表中具体化 Kafka 数据，而 Flink 也负责数据混合过程。

这种混合使用户能够“拥有包含很长历史记录的 TB 级数据，并且在 Kafka 中，您可以拥有最新、实时的的数据，”Brunner 说。“我们使用快照查询所做的是将这两个数据集合并为一个查询。”Confluent 的数据混合过程从用户那里抽象出了大量的复杂性。组织只需选择是想使用系统的传统流模式还是快照模式进行查询。选择后者时，用户编写一个查询，而解决方案查询所需的开放表格式和 Kafka topic。

然后，该平台“将数据混合在一起并进行转换，没有重复项，”Brunner 说。混合步骤使来自 Tableflow 的数据能够有效地附加到 Kafka topic 的数据。由于多种因素，从开放表格式的检索得到了加速，包括这些格式容易公开的有关表内容的信息。

Brunner 认为，表的各个方面（包括元数据以及有关压缩和压缩的详细信息）有效地像索引一样发挥作用。“因此，如果您正在寻找特定的键，例如我想在某个地方寻找客户 X，我们可以很容易地找到它，而无需重新扫描 topic，”他提到。由此产生的成本、效率和提高的生产力收益不容忽视。

## 加速开发者

从快照查询中获得的价值同样适用于生产和开发用例。除了支持 [agentic AI](https://thenewstack.io/top-three-agentic-ai-use-cases-for-modern-it-operations/) 工作流程（其中代理需要根据客户交互与有关客户的参考数据交叉引用低延迟数据，例如）之外，这些查询对于欺诈检测等实时部署非常有用。“对于任何类型的交易，您可能需要历史信息，例如此用户进行了多少次交易，或者从该位置进行了多少次交易，”Brunner 说。“作为其中的一部分，您可能希望自动利用 Tableflow。”
虽然快照查询支持这些关键任务应用程序，但它们可以很容易地被设计用来加速开发人员的生命周期。例如，开发人员可能需要查询他们的历史数据，以确定分析欺诈检测等用例所需的所有上下文因素。Brunner 说，在流模式下，他们必须进行多次交互式查询才能收集到这些信息，“这将花费大量时间”。“通过使用快照，您可以加速这个过程，因为您可以快 100 倍地完成它。”

## 查询优化

快照查询速度和效率的提高直接归功于 Confluent 在 [Flink](https://flink.apache.org/) 中使用的查询优化。组织只需指定他们希望查询做什么，例如识别与实时检测欺诈相关的因素。查询优化器能够混合来自富集表和 Kafka 主题的数据，这意味着它有能力从每个资源中找到相关数据。

Brunner 提到：“你不需要告诉它数据来自 Tableflow 还是 Kafka。”“查询优化器知道从 Kafka 主题或 Tableflow 中获取数据。它是 Confluent 的 Flink 堆栈的一部分。当你编写 SQL 时，我们会将其组合、优化并运行它。” 事实上，优化器可能会确定来自开放表格式的富集数据对于回答查询是不必要的，而只需从相关的 Kafka 主题中检索信息。

## 语义问题

然而，对开发人员来说真正的好处是，当查询优化器确实从大量参考数据中检索信息时，它会将其与实时 [Kafka](https://kafka.apache.org/) 数据结合起来，并揭示哪些信息与解决欺诈检测等业务问题相关。一旦解决了这个后端开发人员的工作，就可以在生产环境中输入该特定查询以用于实时应用程序。通过这种方法，Brunner 说：“当你进行查询时，你可以确信你的流式查询可以工作并将其产品化，并获得 24/7 全天候在你的最新数据上运行的查询。”

此用例强调了快照查询和流模式查询之间的语义差异。前者基于 Brunner 所描述的“世界的状态”（或业务问题的状态），严格来说是在发出查询时。后者基于持续的、正在进行的更新。因此，在进行快照查询以查找业务问题的相关数据后，用户可以基于这些因素运行流式查询，以实时持续更新它们。

## 不言自明

Confluent 的快照查询通过将流式数据处理与批处理相结合来扩大其范围，从而增强开发人员和生产用例。用户可以利用 Confluent 在 Flink 中的查询优化器来自动执行大量繁重的工作，否则需要查询开放表格式中的大量数据。

更有益的可能是供应商所做的混合和转换工作，以使这些数据可以与来自 Kafka 主题的数据一起轻松查询。由此带来的性能、开发人员生产力和实时部署的提升是不言而喻的。