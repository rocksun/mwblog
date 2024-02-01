<!--
title: 工业物联网工作负载架构设计蓝图
cover: https://cdn.thenewstack.io/media/2024/01/3a156c8c-iiot-1024x576.jpg
-->

拥有工业物联网（IIoT）系统的制造商可以以此参考架构为模型，推动创新、适应性和持续改进。

> 译自 [Architecting for Industrial IoT Workloads: A Blueprint](https://thenewstack.io/architecting-for-industrial-iot-workloads-a-blueprint/)，作者 Dunith Danushka 是 Redpanda Data 的高级开发者倡导者，他创建了有关构建现代流数据应用程序的开发者友好的内容。他在设计、构建和操作实时、事件驱动架构方面拥有超过 10 年的经验，喜欢分享他的经验...

制造业格局自工业革命以来发生了翻天覆地的变化。在过去，那些拥有最多人力或最庞大机器队伍的人占据了市场的大部分份额。快进到今天，机器不再是制造业的焦点，而是[它们产生的数据](https://thenewstack.io/data/)。

物联网（IoT）、大数据分析和[云计算](https://thenewstack.io/edge-computing/edge-computing-vs-cloud-computing/)的出现已经将制造范式从劳动密集型过程转变为数据驱动的自动化工厂。将数据用于理解、运作和控制机器的企业在市场上以持续创新、效率和成本削减方面取得了明显的竞争优势。

作为朝着这个方向的一种引导，让我们看一下在制造厂中可以高效实施的工业物联网（IIoT）工作负载的参考架构。但首先，让我们就什么是IIoT达成一致。

## 工业4.0和IIoT

虽然IoT这个术语涵盖了各行各业的各种应用，但IIoT专注于在工业领域集成智能设备和先进分析，以提高效率、生产力和整体运营。例如，在制造业中，IIoT传感器通常用于捕获有关机器性能的数据，以预测设备故障并实时自动化质量控制。

工业物联网（IIoT）的影响不可低估，证据只在不断加强。例如，[麦肯锡的一项研究](https://www.mckinsey.com/~/media/mckinsey/business%20functions/mckinsey%20digital/our%20insights/iot%20value%20set%20to%20accelerate%20through%202030%20where%20and%20how%20to%20capture%20it/the-internet-of-things-catching-up-to-an-accelerating-opportunity-final.pdf)揭示，由物联网驱动的预测性维护可以将停机时间减少45%，并将成本削减多达30%。因此，IIoT继续迅速将制造业从以机器为中心的行业转变为以数据为中心的行业。这种转变主要是由于引入了以下三个支柱：

- **连接性**：IIoT涉及将工业设备、设备和系统连接到网络基础设施，使它们能够相互通信。这种连接性使得实时收集和共享数据成为可能。
- **数据收集与分析**：IIoT设备生成并收集大量数据。使用先进的分析工具可以分析这些数据，提取有价值的见解，优化流程并做出数据驱动的决策。
- **自动化与控制**：IIoT通过将传感器、执行器和其他设备连接到控制系统实现自动化。这可以实现对工业过程更高效、更精确的控制。

## 工业物联网的参考架构

IIoT是一个包含多个子领域的宽泛领域，因此实施IIoT架构的制造商应该对该领域有清晰的概述，以帮助控制其IIoT项目的长期成本和复杂性。

为此，我们提出以下用于IIoT应用的参考架构，该架构利用流数据进行快速、数据驱动的决策。

![Zoom](https://cdn.thenewstack.io/media/2024/01/996e60c7-image4.png)

*建议的IIoT参考架构的示意图*

下表总结了此解决方案的关键组件及其职责。

组件         | 角色
-------------|------
可编程逻辑控制器（PLC）设备和机器上的物联网传感器 | 发送遥测数据
Redpanda 集群 | 遥测数据摄入和事件驱动工作流
Apache Flink 集群 | 用于有状态的流处理和流式 ETL（提取、转换、加载）
机器学习模型 | 用于对遥测数据进行预测分析
时间序列数据库 | 设备监控和运行诊断
工作流引擎 | 触发已部署的自动化业务工作流
数据湖和数据仓库 | 存储冷数据，可用于实验和流程优化
业务应用系统 | 内部业务系统，如库存、供应链等

在详细探讨每个组件之前，请允许我介绍 [Redpanda](https://redpanda.com/)，它作为一个中央数据枢纽连接不同组件之间的数据流。

## Redpanda 作为中央数据枢纽

[Redpanda](https://redpanda.com/what-is-redpanda) 是一个简单、强大且成本效益高的流数据平台，完全兼容 Apache Kafka API，同时消除了通常 Kafka 复杂性。设计成为“流数据的便捷按钮”，Redpanda 不依赖外部依赖（如 JVM 或 KRaft），并提供[人性化的命令行界面（CLI）](https://redpanda.com/blog/get-started-rpk-manage-streaming-data-clusters)和[丰富的 Web 用户界面（UI）](https://redpanda.com/redpanda-console-kafka-ui)，极大简化了与实时数据的工作。

那么，在工业物联网（IIoT）架构中为什么要使用 Redpanda 呢？在中央位置收集来自高容量流的数据使得下游应用能够从单一位置高效地消费数据，而无需使用点对点集成通道。

作为这些数据流的中央数据枢纽，Redpanda 实现了可扩展的实时数据摄入，并提供持久的数据保留，直到下游应用消费。它还解耦了数据生产者和消费者，使它们能够独立扩展和演进。

Redpanda 的精简、成本效益高的设计仅[消耗 JVM-based 替代方案（如 Kafka）三分之一的资源](https://redpanda.com/platform-tco)。这种精简的基础设施占用对于需要在资源受限的环境中（如[边缘设备](https://thenewstack.io/edge-computing/)）部署实时流数据解决方案的制造厂尤为有用。此外，[Redpanda 的分层存储](https://redpanda.com/blog/cloud-native-streaming-data-lower-cost)将旧数据卸载到流畅的云对象存储中，如 [Amazon S3](https://aws.amazon.com/s3/)，显著降低了遥测数据保留成本。

现在我们了解了架构的核心，让我们深入了解周围组件如何贡献于工业物联网的三大支柱。

## 连接和通信

在启用工业物联网的环境中，第一步是建立与机械设备的通信接口。在此步骤中，有两个主要目标：从机器中读取数据（遥测）和向机器写入数据（控制和自动化）。

在制造工厂中的机器可能具有传统/专有的通信接口和现代物联网（IoT）传感器。如今，大多数工业机器由[可编程逻辑控制器](https://en.wikipedia.org/wiki/Programmable_logic_controller)（PLC）操作。PLC是一种专为控制制造过程（如装配线、机器和机器人设备）或需要高可靠性、易编程和过程故障诊断的任何活动而设计和适应的工业计算机。

然而，PLC在外部世界上通过诸如HTTP和MQTT等协议提供有限的连接接口，限制了对外部数据的读取（用于遥测）和写入（用于控制和自动化）。[Apache PLC4X](https://plc4x.apache.org/)通过在传统和专有PLC协议上提供一组API抽象来弥合这一差距。

PLC4X是一个针对工业物联网设备的开源通用协议适配器，支持包括但不限于Siemens S7、Modbus、Allen Bradley、Beckhoff ADS、OPC-UA、Emerson、Profinet、BACnet和Ethernet等协议的通信。PLC4X的最大优势在于它提供了一个Kafka Connect连接器。这使应用程序能够像使用JDBC连接数据库一样从和向PLC设备读写数据。

除了PLC，现代机器还配备有通过MQTT协议进行通信的IoT传感器，从而使得可以使用MQTT sink和source连接器进行数据交换。

![Zoom](https://cdn.thenewstack.io/media/2024/01/341dbe19-image1.png)

*从机器到Redpanda的连接性*

## 数据收集与分析

无论上述使用何种通信机制，从机器收集的数据都会实时注入到 Redpanda 中，以供下游消费。这些遥测数据携带着丰富的信息，例如：

- **运行指标** – 运行时长（机器运行的总时间）、启动和停止时间
- **性能指标** – 速度和每分钟转数（RPM）、吞吐量和效率
- **健康指标** – 温度、压力、振动和噪音水平
- **资源利用** – 能耗、材料使用
- **故障和警报** – 错误代码和警告消息

在注入到 Redpanda 之后，遥测数据源必须经过清理和标准化，以生成下游应用期望的输出格式。这涉及事件过滤、协议转换、丰富化和聚合用于分析。可采用具有[与 Redpanda 本地集成的](https://redpanda.com/blog/stream-processing-apache-flink-etl)状态流处理器，如 Flink，来实现此目的。

经过处理的数据然后可以被注入到时间序列数据库，例如 InfluxDB 或 Prometheus，用于时间序列处理、可视化和交互式分析。这包括实时分析用例，如：

- **远程设备监控**：监测遥测数据以实时检测和响应故障或异常。通过触发警报并允许快速干预，最小化了故障的影响。
- **预测性维护**：分析实时遥测数据以检测表明潜在设备故障的异常或模式。这使得能够进行主动维护，减少停机时间并延长机械寿命。
- **能源优化**：基于实时遥测数据对能耗进行持续监测，以识别节能机会并优化资源利用。

同时，遥测数据源还可以路由到数据仓库和数据湖等离线用例的目的地，如监管报告、临时探索和机器学习工作负载。这些用例包括但不限于使用历史遥测数据进行：

- **训练机器学习（ML）模型**，用于预测性维护或异常检测。
- **根本原因分析**，确定故障根本原因。
- **历史性能分析**，识别趋势、模式和性能基准。
- **监管报告**，生成符合行业法规的报告。

在 Kafka Connect 中部署适当的 sink 连接器可以将遥测数据摄入到 [Redpanda Cloud](https://redpanda.com/redpanda-cloud)，它提供了内置的 sink 连接器，将数据发送到 [Amazon Web Services（AWS）](https://aws.amazon.com/?utm_content=inline-mention)S3、Google Cloud Storage、Google BigQuery、Snowflake 等目的地。

![Zoom](https://cdn.thenewstack.io/media/2024/01/c4e9223f-image3.png)

*遥测数据的实时和离线分析*

## 自动化与控制

机器操作的自动化和远程控制通过消除需要人工干预的操作，提高了工厂生产线的效率。

工业物联网（IIoT）设备可以向 Redpanda 主题发布事件，触发实时的自动响应和控制操作。发布到 Redpanda 的控制主题的事件可以触发部署在具有状态的工作流引擎中的业务流程，如 [Camunda](https://camunda.com/)、[jBPM](https://www.jbpm.org/) 和 [Activiti](https://www.activiti.org/)。

这使得 IIoT 设备与业务应用之间的数据流动变得无缝，以实现以下用例：

- **远程控制机器**：在危险的工作环境中部署的机器可以通过连接的 IIoT 设备进行远程控制和监控。这样，人类可以完全免受潜在危害。
- **工厂生产线自动化**：生产流程可以进行调度、控制和监控，以减少手动干预。例如，当原材料使用达到一定阈值时，可以自动发送采购订单以进行库存补充。

## 从参考架构到强大的工业系统

已经部署了 IIoT 系统或计划采用 IIoT 的制造商可以将此参考架构用作在工业领域推动创新、适应性和持续改进的蓝图。然而，将它们从纸面上实现到实践中取决于您的流数据设置和可用资源来运行它们。

Redpanda 为处理工业物联网（IIoT）设备生成的实时遥测数据提供了一个强大且易扩展的平台，并可作为[完全托管的云服务](https://redpanda.com/redpanda-cloud)或自托管平台提供。

要让您的 IIoT 数据流动起来，请[免费试用 Redpanda](https://redpanda.com/try-redpanda) 或从 [GitHub](https://github.com/redpanda-data/redpanda/) 获取 Community Edition。

