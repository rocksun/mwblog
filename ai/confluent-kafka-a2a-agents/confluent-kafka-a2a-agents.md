<!--
title: Confluent平台重磅升级：A2A、智能异常检测与Kafka队列深度融合
cover: https://cdn.thenewstack.io/media/2026/03/ae01811c-car-communication-3100983_1280.jpg
summary: Confluent平台重大更新，新增A2A协议支持、多变量异常检测和Kafka队列功能。此次更新利用Kafka实现实时、事件驱动的代理间通信，增强可审计性和可追溯性。它旨在普及流式代理的实时能力，并简化消息队列架构，使Kafka能更广泛地应用于各类流数据工作负载，提供低延迟洞察。
-->

Confluent平台重大更新，新增A2A协议支持、多变量异常检测和Kafka队列功能。此次更新利用Kafka实现实时、事件驱动的代理间通信，增强可审计性和可追溯性。它旨在普及流式代理的实时能力，并简化消息队列架构，使Kafka能更广泛地应用于各类流数据工作负载，提供低延迟洞察。

> 译自：[Confluent adds A2A support, anomaly detection, and Queues for Kafka in major platform update](https://thenewstack.io/confluent-kafka-a2a-agents/)
> 
> 作者：Jelani Harper

Confluent 最近发布了对 Agent2Agent (A2A) 协议的支持，这是一个用于代理间通信的开放标准。该平台对这一流行协议的实现允许用户通过 A2A 利用 [Apache Kafka](https://thenewstack.io/apache-kafka-4-1-the-3-big-things-developers-need-to-know/) 来协调代理间通信。

通过这种范式，代理调用可以使用 Confluent 的流式代理（一组用于设计和部署能够即时响应数据状态变化的代理的能力）触发基于事件的操作。Kafka 还实时存储代理间通信，以实现可审计性和可追溯性。

> “如果你已经在其他地方投资了代理，那么如果你想把那个代理变成一个事件驱动的代理，这会是一个推动者。”

[Sean Falconer](https://www.linkedin.com/in/seanf)，[Confluent](https://www.confluent.io/) 的 AI 负责人，告诉 *The New Stack*，这种方法（于 2 月 26 日[宣布](https://investors.confluent.io/news-releases/news-release-details/confluent-intelligence-expands-real-time-business-data)）的主要优势之一是，它使 Confluent 之外设计的代理也能拥有流式代理的实时能力。

Falconer 说：“如果你已经在其他地方投资了代理，那么如果你想把那个代理变成一个事件驱动的代理，这会是一个推动者。”

Confluent 添加了多变量异常检测功能，进一步增强了这些可能性。该功能利用机器学习技术分析跨变量模式，并识别与操作或业务目标相关的模式。Falconer 表示，Kafka（用户现在可以通过新的 Kafka 改进提案 (KIP) [Queues for Kafka] 将其用于消息队列）是这两种能力及其综合的基础。

Falconer 说：“无论是点击流数据还是物联网数据，一旦产生，它就在 Kafka 中。当你将它与异常检测和流式代理等功能结合起来时，你就能理解业务中正在发生的这些关键时刻，从而能够以创建个性化产品或进行根本原因分析的方式应用人工智能。”

通过 Confluent 的 A2A 实现，人工智能可以涉及任何代理。

## Kafka 如何为异步 A2A 通信提供动力

A2A 协议包括[同步和异步](https://a2a-protocol.org/latest/)两种；Confluent 支持后者。Falconer 表示，通过此选项，代理会立即响应请求并提供其身份，并能回答有关其是否完成任务的问题。由于代理间通信是通过 [Kafka](https://kafka.apache.org/) 提供的，用户获得了许多优势，包括能够通过 Kafka 主题拥有大量的通信订阅者。Falconer 说：“你希望它能够进入你的可观测性工具、你的分析工具，而 Kafka 是一个非常好的媒介来实现这一点。”

## 系统表为代理提供内置审计追踪

Kafka 对多个独立消费者之间代理间通信的用处，既体现在其存储能力上，也体现在其通过主题实现的发布/订阅模型上。流式代理做出的每一个决策都会实时写入一个系统表，这本质上是一个具有特定模式用于记录信息的 Kafka 主题。随后，“当代理进行交互时，它会把所有东西都写入那里，” Falconer 解释道。系统表对于开发人员构建、测试和完善代理至关重要，它们还在受监管行业提供可观测性、可追溯性和一定的可解释性。此外，Falconer 说，通过 Kafka，“你可以将其消费到你的 Open Telemetry 系统或分析数据库中。”

## 多变量异常检测在流中运行，而非批处理

Confluent 的多变量异常检测增强了可观测性用例，它使组织能够评估多个因素及其关系，以确定事件是否异常。Falconer 表示，检测异常行为的各种机器学习技术同样适用于任何数据驱动的事件，包括股市变化。有些技术使用时间序列分析，例如自回归积分移动平均模型 ([ARIMA](https://www.ibm.com/think/topics/arima-model))，还有些技术评估数据的变异性，例如中位数绝对离差 ([MAD](https://arxiv.org/abs/1910.00229))。其他度量方法则考虑了季节性。

Falconer 说，利用这些方法的一个显著好处是“你不需要对它们进行批量训练”。“它们在你的流中一启动就开始学习。”

此外，Falconer 表示，由于它们依赖传统的统计机器学习方法（而不是语言模型规模的深度神经网络），“你可以以低成本运行大量此类模型，而且它们速度非常快，这对于监测物联网数据等任务来说非常棒。”

## Kafka 队列：在单个主题中实现发布/订阅和消息队列

[Queues for Kafka (KIP: 932)](https://cwiki.apache.org/confluence/display/KAFKA/KIP-932%3A+Queues+for+Kafka) 将 Kafka 的范围扩展到消息队列，而非其传统的发布/订阅方法。设计此构造的原因之一是简化使用 Kafka 正式消息队列的架构和技术堆栈，这在传统上需要额外的基础设施。

Falconer 表示：“Kafka 队列所做的可能是采用你用于基于日志的发布/订阅的同一个主题，并允许它充当队列。该主题将充当单一事实来源，然后你将其具体化以满足你的任何数据需求。”

尽管基于日志的发布/订阅模型和消息队列之间存在一些重叠，但它们最终需要不同的语义。Falconer 通过将它们比作餐厅里的两位服务员来阐明两者之间的区别，每位服务员负责一组独立的餐桌。

> “这是一个重要的协议，特别是对于企业代理的未来发展方向而言，未来企业将在各种企业系统中运行数百甚至数千个此类代理。”

对于类似于发布/订阅模式的服务员，即使他迟到了，也只有他能从那张桌子接单。Falconer 说：“但对于队列，其语义更像熟食店的取票台。没有人拥有特定数量的票。只有一个票号，谁有空谁就来接你的订单。”

两种方法都没有优劣之分；它们解决不同的问题。添加此功能使 Kafka 更适合开发人员支持不断增长的用例，而无需不必要地增加基础设施。

Confluent 对 A2A 协议的支持因其持续依赖 Kafka 而大大增强。这个开源框架使代理间通信即时可用，并将其存储起来以实现可追溯性、数据治理和可审计性。借助 Kafka 队列，代理对于基于队列的消息工作负载以及涉及 Kafka 发布/订阅模型的工作负载都同样适用。Confluent 的多变量异常检测确保组织在指标、日志和 KPI 方面获得低延迟洞察，这几乎适用于任何流数据应用程序。

因此，将 Kafka 应用于流数据 A2A 工作负载可能会成为标准实践。Falconer 反思道：“这是一个重要的协议，特别是对于企业代理的未来发展方向而言，未来企业将在各种企业系统中运行数百甚至数千个此类代理。”