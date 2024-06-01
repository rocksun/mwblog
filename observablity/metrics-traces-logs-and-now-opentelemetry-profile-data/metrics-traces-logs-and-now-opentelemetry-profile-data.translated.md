# 指标、跟踪、日志——现在还有 OpenTelemetry 配置文件数据

![指标、跟踪、日志——现在还有 OpenTelemetry 配置文件数据：特色图片](https://cdn.thenewstack.io/media/2024/05/2dad2a19-getty-images-4oxm-5dcxt0-unsplash-1-1024x683.jpg)

[OpenTelemetry](https://thenewstack.io/opentelemetry-gaining-traction-from-companies-and-vendors/) 的分析器代表着其创建者所说的另一个里程碑，作为开源领域最具活力和最重要的项目之一，尤其是在可观测性方面。如果它能满足 OpenTelemetry（OTel）创建者的雄心，那么持续分析信号可能至少与 [指标、跟踪和日志](https://thenewstack.io/metrics-logs-and-traces-more-similar-than-they-appear/) 数据一样关键。

OTel 分析目前还不可用——其 1.0 版本的普遍可用性目标是今年年底。[Morgan McLean](https://ca.linkedin.com/in/morganmclean)，[Splunk](https://www.splunk.com/) 产品管理高级总监，也是 OpenTelemetry 的主要创建者之一，告诉 The New Stack。

“虽然它为开发人员及其组织提供了一种简单而强大的方式来降低基础设施成本并通过让他们了解各个代码功能来提高性能，但分析仍然不是非常知名，并且在业界的使用程度不如指标、日志和跟踪分析。”McLean 说。“随着 OpenTelemetry 中增加了分析功能，我们预计持续生产分析将成为主流。”

## 关于分析

持续分析在一定程度上已向公众开放六年多。随着 OpenTelemetry 中增加了分析功能，我们预计持续生产分析将成为主流。

要了解分析器为何重要，有必要将其置于上下文中。首先，有 [遥测数据](https://thenewstack.io/lightsteps-opentelemetry-extension-helps-make-lambda-telemetry-data-more-accessible/)，包括日志、指标，最近还有跟踪，提供需要审查或收集的数据。但是，一旦通过监控收集并观察到它，如果数据没有以适当的方式进行解析或引导以消除不相关的遥测数据，那么它就没有多大意义。

同时，使用不同遥测数据作为操作员观察事件或性能在一定程度上是有用的。但它达不到可观测性的要求，可观测性涉及根据使用监控收集的此数据进行推断来得出可操作的见解。

[OpenTelemetry 提供了一个标准化流程](https://opentelemetry.io/) 来实现可观测性。它与供应商无关，用于理解由指标、日志和跟踪组成的遥测数据。它不仅仅是与供应商无关，因为它旨在允许用户将他们选择的可观测性工具集成到一种通用方法中，从而统一它们。

通过这种方式，OpenTelemetry 在集成中发挥着关键作用，作为在各种环境中实现无缝数据监控和分析的中心组件。借助 OpenTelemetry，这种集成的最新演变突显了它的重要性：这体现在增强的分析功能中，使用户能够更深入地了解系统性能和资源利用率。

## 深入了解

OpenTelemetry 的分析器应该对用户很有用，因为它通过扩展到代码级别来深入进行可观测性分析。它通过扩展在统一流中提取的遥测数据来实现对指标、跟踪和日志的更深入分析，该流扩展到整个网络中的应用程序的代码级别。代码被分析并存储。

在实践中，这意味着当出现问题或查看可观测性数据流提供的某些性能方面时——例如当 CPU 运行缓慢或最终用户的数据请求花费太长时间时——该配置文件会识别有问题的代码。借助正确的附加可观测性工具，应该可以更快地提供修复程序，因为用户可以通过查询更轻松地查明问题代码。

![](https://cdn.thenewstack.io/media/2024/05/97776cb6-capture-decran-2024-05-16-172348.png)

消息之间的关系。来源：OpenTelemetry 项目

在博客文章中，
### 奥斯汀·帕克

[奥斯汀·帕克](https://twitter.com/austinlparker)，[Honeycomb](https://www.honeycomb.io/?utm_content=inline+mention) 的开源总监，描述了分析并提供了示例，并指出分析支持双向链接。这意味着用户可以从遥测数据提供的方面深入挖掘代码级别，以了解相应的分析。帕克传达的示例包括：

**指标到分析**：CPU 或内存使用率的峰值转换为在运行时消耗资源的代码。

**跟踪到分析**：除了能够精确定位高延迟在网络中表现的位置外，附加到跟踪或跨度的分析还揭示了导致高延迟的代码。

**日志到分析**：日志与指标和跟踪一起仍然是可观察性的关键部分，但除了使用日志来跟踪内存不足错误等问题外，还会显示导致额外内存消耗的代码以进行进一步分析。

### 重大贡献

该项目应该在今年完成或致力于其一般可用性功能——当然，这要归功于社区的持续努力。该项目的创建者强调了 OpenTelemetry 社区中的一些主要贡献者，包括以下人员：

- Felix Geisendörfer（Datadog）
- Alexey Alexandrov（
- Dmitry Filimonov（Grafana Labs）
- Ryan Perry（Grafana Labs）
- Jonathan Halliday（
[Red Hat](https://www.openshift.com/try?utm_content=inline+mention)）

此外，Elastic 和 Splunk 正在进行重大捐赠。根据提案文档，Elastic 分析代理的捐赠将：

“通过成熟、功能丰富且高效的分析解决方案填补 OpenTelemetry 组件架构中的空白。通过此举，eBPF 和分析中的尖端技术将通过 OpenTelemetry 成为收集生产分析数据的标准。使用 OpenTelemetry 在广泛的语言/技术中收集分析数据将带来无摩擦的部署体验。”

此次捐赠是在可观察性工具 Elastic Common Schema (ECS) 和 OpenTelemetry Semantic Conventions “联姻”之后进行的。具体来说，开源 Elastic 的创建者正在向 OpenTelemetry 贡献 ECS，并致力于这两个项目的联合开发。

McLean 说，Elastic 和 Splunk 的贡献“对于使分析成为 OpenTelemetry 中的一流信号至关重要”。

正如 McLean 解释的那样，大多数分析器不使用
[eBPF](https://thenewstack.io/what-is-ebpf/)，因为语言运行时（如 [JVM](https://thenewstack.io/parity-check-node-js-jvm-containers/)、.NET CLR、Go 运行时等）内置了此功能。OpenTelemetry 将同时追求直接语言分析和基于 eBPF 的分析。直接分析语言运行时通常会提供更多数据并且需要更少的处理，而基于 eBPF 的分析可以应用于没有内置分析功能的语言，更容易设置，并且只需要很少的处理（比直接处理稍多），McLean 解释说。

Elastic 分析代理以及 ECS 与 OTel 的集成突出了 Elastic 和 OTel 的综合覆盖范围，以及其创建者致力于允许用户将遥测数据合并到一个面板中以进行更全面的可观察性分析。事实上，ECS 与 OTel 的集成帮助 OTel 项目朝着与任何可观察性工具或流程完全兼容和标准化的最终目标迈进。

换句话说，Elasticsearch 和 OpenTelemetry——尤其是在它们在 2024 年之前几周发布一般可用性之后——都是非常流行的平台，可以集成和处理来自各种来源的数据日志、指标和跟踪。许多人应该会赞赏它们进一步的集成。

Splunk 已开始捐赠其 .Net 分析器。其项目创建者解释说，这将允许 OTel 从
[C#](https://thenewstack.io/microsoft-we-are-not-abandoning-c-for-rust/)、F# 和其他 .NET 应用程序中获取分析。

Splunk 为 OpenTelemetry 提供的分析器的工作仍在进行中，Elasticsearch 的贡献也是如此。根据
[项目文档](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/pull/3196)，连续分析配置通过 [OpenTelemetry .NET 自动检测](https://opentelemetry.io/docs/zero-code/net/) 在启动期间以调试日志级别记录分析配置来演示。该分析器利用 .NET 分析来执行定期调用堆栈采样。对于每个采样周期，运行时都会暂停，所有托管线程的样本都会保存到缓冲区中；然后，运行时恢复。

## 状态和未来
### OpenTelemetry Profiler 今年应该会最终确定。

它代表着该项目在 2023 年完成 OpenTelemetry 日志功能后的最新里程碑。对于未来，该项目的创建者在 [OTEL 规范](https://github.com/open-telemetry/opentelemetry-specification) 的文档中将这些功能列为“未来功能”：

- 配置文件数据模型
- 配置文件 API
- 配置文件 SDK

“就我个人而言，当我们组建 OpenTelemetry 时，重点是跟踪和指标，而日志是之后的明显下一步。当时，我还帮助推出了我认为是第一个公开可用的分布式分析产品，我真的很高兴让所有开发人员了解他们的实际代码在生产中的表现，”McLean 说。“将配置文件作为 OpenTelemetry 中的一流信号并使此类工具易于访问一直是我自启动 OTel 以来一直以来的梦想和目标，看到它实现真是太棒了。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。