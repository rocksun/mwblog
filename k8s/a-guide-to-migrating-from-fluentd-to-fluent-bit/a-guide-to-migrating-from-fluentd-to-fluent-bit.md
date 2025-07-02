<!--
title: Fluentd到Fluent Bit迁移指南
cover: https://cdn.thenewstack.io/media/2025/06/0e44e613-birds.jpg
summary: 本文介绍了从 Fluentd 迁移到 Fluent Bit 的原因、区别、方法和注意事项。迁移能带来更高的性能、更好的遥测支持和更灵活的配置。建议逐步迁移，并考虑采用遥测管道架构。
-->

本文介绍了从 Fluentd 迁移到 Fluent Bit 的原因、区别、方法和注意事项。迁移能带来更高的性能、更好的遥测支持和更灵活的配置。建议逐步迁移，并考虑采用遥测管道架构。

> 译自：[A Guide To Migrating From Fluentd To Fluent Bit](https://thenewstack.io/a-guide-to-migrating-from-fluentd-to-fluent-bit/)
> 
> 作者：Anurag Gupta

*编者注：本文是系列文章的一部分。另请阅读基于 Manning 图书的节选，“[使用 Kubernetes 的 Fluent Bit](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)”：*

Fluentd 创建于 14 年前，至今仍是企业中部署最广泛的日志收集技术之一。Fluentd 的分布式插件架构和高度宽松的许可使其成为[云原生计算基金会 (CNCF)](https://www.cncf.io/)的理想选择，现已成为毕业项目。然而，企业现在正被遥测数据淹没，需要具有更高性能、对不断发展的模式和格式的更多原生支持以及更高的处理灵活性的解决方案。Fluent Bit 应运而生。

[Fluent Bit](https://chronosphere.io/learn/fluent-bit-v4-0/?utm_source=TNs&utm_medium=sponsored+content&utm_content=inline-mention&utm_campaign=tns+platform) 最初在 [Fluent 生态系统](https://chronosphere.io/fluent-bit/?utm_source=TNs&utm_medium=sponsored+content) 中作为一个子项目发展，后来从 Fluentd 扩展到支持所有遥测类型——日志、指标和追踪。Fluent Bit 现在是两者中更受欢迎的一个，拥有超过 150 亿的部署，并被 [Amazon](https://aws.amazon.com/?utm_content=inline+mention)、[Google](https://cloud.google.com/?utm_content=inline+mention)、[Oracle](https://developer.oracle.com/?utm_content=inline+mention) 和 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 等公司使用。Fluent Bit 还与 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry/) 信号、格式和协议完全一致，这确保了用户能够随着遥测数据的增长和发展而继续处理这些数据。

作为这些项目的维护者，我们最常被问到的问题包括：

* 我们如何迁移？
* 我们应该注意什么？
* 迁移能给我们带来什么商业价值？

本文旨在通过示例回答这些问题。我们希望让从 [Fluentd 迁移到 Fluent Bit](https://chronosphere.io/fluent-bit-academy/?utm_source=TNs&utm_medium=sponsored+content&utm_content=inline-mention&utm_campaign=tns+platform) 成为一个简单的决定。

## 为什么要迁移？

以下是用户从 Fluentd 切换到 Fluent Bit 的一些原因：

1. 在您已使用的相同资源上获得更高的性能
2. 完全支持 OpenTelemetry 的日志、指标和追踪，以及 Prometheus 对指标的支持
3. 更简单的配置和路由到多个位置的能力
4. 更快地添加自定义处理规则
5. 集成监控以更好地了解性能和数据流

## Fluentd 与 Fluent Bit：有什么区别

### 背景

要了解项目之间的所有差异，重要的是要了解每个项目的背景以及它所构建的时代。对于 Fluentd，主要语言是 Ruby，最初旨在帮助用户将数据推送到 Hadoop 等大数据平台。该项目遵循分布式架构，插件在安装和部署主二进制文件后安装。

另一方面，Fluent Bit 是用 C 编写的，专注于在较小的系统（容器、嵌入式 Linux）中的超高性能。该项目借鉴了 Fluentd 的插件，而是选择完全嵌入式插件，这些插件是核心二进制文件的一部分。

### 性能

从 Fluentd 切换到 Fluent Bit 的明显区别和主要价值在于性能。使用 Fluent Bit，您可以使用相同的资源处理的日志量可能比原来高 10 到 40 倍，具体取决于您使用的插件。Fluent Bit 从一开始就被编写为具有超高性能，专注于尽可能快地传输数据以进行数据分析。后来，人们发现性能足够高效，可以在不影响使代理尽可能快的使命的情况下添加更多的边缘处理。

### 路由

Fluent Bit 的其他部分是从 Fluentd 遇到的挑战演变而来的，例如缓冲和路由。对于 Fluentd，多路由是事后才考虑的，用户需要“复制”数据流以将数据路由到多个点。这使得配置管理成为一场噩梦，此外还基本上复制了路由数据的资源需求。

在 Fluent Bit 中，缓冲区存储一次，这允许多个插件“订阅”数据流。这确保了数据存储一次并订阅多次，从而允许进行多路由，而无需在性能和配置疲劳之间进行权衡。

### 遥测信号焦点

虽然 Fluentd 最初是一个数据传输器，但它后来发展成为一个日志记录代理，用于 [Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) 等项目和 Splunk 等公司。另一方面，Fluent Bit 最初是一个嵌入式指标收集器，日志文件随后才进入。随着 Fluent Bit 的采用开始超过 Fluentd 的功能，添加了 OpenTelemetry 日志/指标/追踪、Prometheus Scrape 和 Remote Write 支持、eBPF 和分析支持等功能。

今天，Fluent Bit 与 OpenTelemetry 模式、格式和协议保持一致，旨在成为一种轻量级实现，具有高度的性能。

### 自定义处理

Fluentd 和 Fluent Bit 具有许多相同的处理器名称，但在自定义处理方面，选项却大不相同：

* 对于 Fluentd，选项是 `enable_ruby`，它允许在配置中使用自定义 Ruby 脚本来执行操作。这对于小型任务可以有效地工作；但是，随着逻辑变得越来越复杂，它会带来很大的惩罚，从而增加了更多的性能瓶颈。

* 对于 Fluent Bit，自定义处理是用 Lua 语言完成的，这提供了极大的灵活性。但是，与 Fluentd 不同，Fluent Bit 的 Lua 处理器性能非常出色，可以大规模使用（100+ TB/天）。

### 自定义插件

这两个项目都允许自定义插件来帮助您连接到源或目标。对于 Fluentd，这些自定义插件是“Ruby Gems”，您可以下载并将其安装到现有或新的安装或部署中。对于 Fluent Bit，自定义插件是用 Go 编写和编译的。还有一些新的举措，允许您用您想要的任何语言编写自定义插件，并将它们编译成 WebAssembly。

我们从 Fluentd 的分布式插件架构中吸取的一个教训是，插件的数量可能会呈指数级增长。然而，通常所需的高质量和维护使得许多插件被放弃且不受支持。对于 Fluent Bit，插件都集成到源代码本身中，这确保了与每个版本的兼容性。自定义插件仍然独立于主存储库。但是，我们正在寻找方法，允许它们也共享主 GitHub 存储库中本机 C 插件的相同优势。

### 监控

了解数据如何在您的环境中传输通常是部署 Fluentd 或 Fluent Bit 的用户提出的首要请求。对于 Fluentd，启用这些设置可能需要通过“monitor_agent”或使用第三方 Prometheus 导出器插件进行复杂的配置。这些监控插件也增加了 Fluentd 的维护开销，这会影响性能。

Fluent Bit 将监控作为其核心功能的一部分，并且可以通过本机插件（`fluentbit_metrics`）检索，或者可以在 HTTP 端口上进行抓取。Fluent Bit 的指标也比 Fluentd 的包含更多信息，这使您可以了解字节、记录、存储和连接信息。

## 如何开始从 Fluentd 迁移到 Fluent Bit

我们要回答的下一个问题是：如何开始？

第一个重要步骤是了解 Fluentd 的部署方式、环境中发生的处理以及数据流向何处。

**您无需担心什么：**

1. **架构支持：** 两个应用程序都支持 x86 和 ARM。
2. **平台支持：** Fluent Bit 支持与 Fluentd 今天相同的平台，甚至更多。旧系统可能有所不同；但是，重要的是要注意，这些系统在任何 OSS 项目中都没有维护。
3. **正则表达式：** 如果您使用 Onigmo 解析器库构建了一个大型正则表达式库，您可以放心地知道 Fluent Bit 支持它。

## 部署

### 作为代理部署（Linux 或 Windows 包）

当 Fluentd 作为代理部署在 Linux 或 Windows 上时，其主要功能是收集本地日志文件或 Windows 事件日志，并将它们路由到特定目标。值得庆幸的是，Fluent Bit 的本地收集能力与 Fluentd 的能力相同，包括在失败时恢复、存储上次收集的日志行和本地缓冲的能力。

### 在 Kubernetes 中作为 DaemonSet 部署

如果 Fluentd 在您的 Kubernetes 集群中作为 DaemonSet 运行，您应该首先检查正在运行的镜像。由于 Fluentd 具有分布式插件，因此 DaemonSet 镜像可能包含特定的插件，这确保您可以直接从读取 Kubernetes 日志到最终目标。[此示例](https://hub.docker.com/r/fluent/fluentd-kubernetes-daemonset) 包含 OpenSearch 和 Kafka 作为插件，因此您应该验证您使用的镜像是否具有与 Fluent Bit 相同的插件。Fluent Bit 还支持对所有日志进行 Kubernetes 富集，提供有关命名空间、pod、标签等的数据。

### 作为聚合器/收集器部署

如果您的 Fluentd 部署用于从 syslog、网络设备或 HTTP 请求收集日志，您可以首先验证 Fluent Bit 是否具有相同的功能。例如，Fluent Bit 具有 syslog、TCP、HTTP 和 UDP 插件，可以覆盖大多数这些用例。此外，Fluent Bit 还可以接收 OpenTelemetry HTTP1/gRPC、Prometheus Remote Write、HTTP gzip 和 Splunk HTTP Event Collector (HEC) 作为额外的入站信号。

### 添加遥测管道

从 Fluentd 迁移到 Fluent Bit 时，我们还建议考虑在代理和目标之间添加遥测管道。这允许您将更大的处理逻辑块在 Fluentd 代理中向下游移动。

[![数据源（输入）、转换和路由数据（处理）以及数据目的地（输出）。](https://cdn.thenewstack.io/media/2025/06/2535bb3a-image1a-1024x470.png)](https://cdn.thenewstack.io/media/2025/06/2535bb3a-image1a-1024x470.png)

### 配置

Fluentd 和 Fluent Bit 之间的配置语法差异很大。虽然两者最近都开始更多地支持 YAML，但大多数旧的 Fluentd 配置仍然会使用类似于 XML 的特定于域的配置语言编写。

一些一般说明：

1. 考虑一次验证一个插件，然后扩展到单个路由（例如，将系统日志路由到 OpenSearch）。
2. 缓冲和线程设置在 Fluent Bit 中并不重要。
3. 安全设置应该相似。

如有疑问，联系 [Fluent 社区](https://www.launchpass.com/fluent-all) 有助于解决一些更细粒度的设置。

### 自定义插件

迁移时，重要的是确保 Fluent Bit 支持所有插件（源和目标）。您还应该检查它是否支持有关身份验证、授权或访问的特定设置。这将是一个手动过程，可能需要一些时间。但是，这也将使您有机会重新审视您过去对特定数据格式或插件设置所做的决定。

### 自定义处理逻辑

如果您在 Fluentd 中有标签、过滤器或其他处理逻辑，重要的是要注意您尝试实现的功能。虽然看起来只是交换那些过滤器可能是最容易的，但您也应该考虑将它们直接迁移到 [Fluent Bit 处理器](https://chronosphere.io/learn/explaining-the-fluent-bit-processor/) 的方法。

如果您有相当数量的自定义 Ruby，您可以使用大型语言模型 (LLM) 来帮助将其转换为合适的 Lua。

### 每次迁移一部分

您不需要一次迁移所有功能。由于 Fluent Bit 轻量级且性能出色，因此您可以考虑让每个代理处理不同部分的工作负载。随着时间的推移，您可以按照上面的逻辑继续迁移，而不必担心日志收集中断。

## 结论

虽然从 Fluentd 迁移到 Fluent Bit 似乎是一项艰巨的任务，但您有很多关于如何攻击以及在哪里集中精力以实现最大影响的选择。当然，迁移也是重新评估某些逻辑以进行改进，甚至引入新的架构模式（例如遥测管道）的好时机。

如果您正在寻找指导或协助帮助，请告诉我。我曾帮助许多人从 Fluentd 迁移到 Fluent Bit，甚至协助将某些部分现代化为遥测管道。