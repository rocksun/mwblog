# 将移动信号发送到 OpenTelemetry Collector

![将移动信号发送到 OpenTelemetry Collector 的专题图像](https://cdn.thenewstack.io/media/2024/11/47c27d1e-metrics-1024x576.jpg)

提供有意义的体验是任何移动应用程序的主要目标。购物者想要购物；影响者想要上传他们最新的热门帖子；遛狗者想知道何时何地带他们的下一只小狗。最终决定应用程序运行情况的是用户，而不是计算输出。

创建更好的用户体验需要移动[可观测性](https://thenewstack.io/observability/)。为了将用户的行为与整个软件堆栈的性能联系起来，[开发人员应将他们的移动遥测数据](https://thenewstack.io/developing-a-mobile-crash-model-for-opentelemetry/)与其他整体系统健康指标结合起来。

幸运的是，这正是[OpenTelemetry](https://opentelemetry.io/)存在的原因。使用跟踪、日志和指标等信号，[OpenTelemetry（或“OTel”)](https://thenewstack.io/why-the-latest-advances-in-opentelemetry-are-significant/)试图创建一种共享语言，将从不同软件系统收集的应用程序数据（或“遥测数据”）连接起来。将后端架构中的微系统信息统一起来的 OpenTelemetry 组件也可以将移动遥测数据链接到该架构中的 Web 服务和数据库。

在本教程中，我们将展示如何使用 [OpenTelemetry Collector](https://thenewstack.io/how-the-opentelemetry-collector-scales-observability/) 将移动应用程序中的信号链接到示例跟踪后端。

## OpenTelemetry Collector

从移动应用程序导出遥测数据时，您需要一种方法来接收（或摄取）和处理应用程序的信号，然后再开始分析这些数据。传统上，这是通过部署供应商代理作为“中间人”来完成的，这些代理使用专有格式连接和处理应用程序信号。

OpenTelemetry 使用 Collector 的概念来实现此目的。

根据[其文档](https://opentelemetry.io/docs/collector/)，OTel Collector “提供了一种与供应商无关的实现，用于接收、处理和导出遥测数据。” OTel Collector 是来自移动应用程序的跟踪的强大入口点，因为它将作为我们移动遥测管道中的初始摄取、过滤和转发点。

## 捕获移动遥测数据

为了从 iOS 应用程序中获取跟踪，我们将使用 [Embrace Apple SDK](https://github.com/embrace-io/embrace-apple-sdk/) 中的工具，这是一个开源的、Swift 原生软件开发工具包，[构建在 OTel 之上](https://embrace.io/blog/embraces-ios-sdk-is-built-on-otel-but-what-does-this-mean/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-collector)。Embrace SDK 捕获了各种针对视图和推送通知等移动概念的自动工具，然后将它们作为 OpenTelemetry [跟踪](https://thenewstack.io/spans-what-are-they-and-why-should-mobile-engineers-care/)和日志发出。

我们将使用 Embrace Apple SDK 将兼容的 [OTel Exporter](https://opentelemetry.io/docs/languages/js/exporters/) 附加到应用程序，然后将移动跟踪发送到 OTel Collector。移动应用程序将是 [Embrace Outdoors 应用程序](https://github.com/embrace-io/embrace-outdoors-demo)，它也是开源的。Embrace Outdoors 使用 Embrace Apple SDK 为 iOS 应用程序添加重要的移动工具，例如自动网络捕获和关键用户流的手动跟踪。例如，以下是登录流程一部分的示例跟踪：

通常在 [启动 SDK](https://embrace.io/docs/ios/open-source/) 时（通常尽可能接近应用程序启动），会在 Embrace Apple SDK 中配置导出器。在这里，我们可以附加由 OTel 生态系统中的工程师维护的任何兼容的 [Swift 语言 OTel 导出器](https://github.com/open-telemetry/opentelemetry-swift/tree/main/Sources/Exporters)。但是，OpenTelemetry 协议 (OTLP) 还创建了一组通过 HTTP 或 gRPC 传输的规则，以便任何遵循该协议的导出器都可以发送遥测数据。

### 配置 OTel 导出器

让我们使用 gRPC 设计我们自己的导出器，以发送到本地 OTel Collector。此导出器需要符合 OpenTelemetry 协议 (OTLP) 并导入 Swift NIO 和 gRPC 库。然后，我们将把它连接到为 gRPC 指定的本地主机端口 4317。

然后，当我们配置 SDK 时，我们将把这个导出器添加到 SDK 中：

现在导出器已连接到我们的应用程序，我们在应用程序中创建的任何跟踪都将近乎实时地导出。这意味着网络调用将在完成后自动发送有效负载，并且我们从头到尾跟踪的复杂交互将以瀑布视图显示，如上面的登录示例所示。
由于 Embrace SDK 构建于 OpenTelemetry 之上，我们可以将遥测数据发送到任何我们想要的地方。（当然，前提是该位置也支持 OTel。）

在下一节中，我们将配置 OTel 收集器，以便在名为 [Zipkin](https://zipkin.io/) 的分布式跟踪工具中查看我们的跟踪。Zipkin 是一个开源可视化工具，虽然它独立于 OTel，但可以在收集器中进行配置。

## 配置 OTel 收集器

为了配置 OTel 收集器，我们将使用 Docker 和一些概述收集器及其功能的 YAML 文件。其中一个 YAML 文件 `collector-config.yaml` 将包含我们希望收集器具备的特定功能，而另一个文件 `docker-compose.yaml` 将部署收集器和 Zipkin。为了避免以后出现任何问题，请立即打开 Docker。

OTel 收集器具有各种功能，允许公司大规模使用它来进行数据采集、处理和转发。这些功能包括重要的安全属性、采样设置以及其他超出本教程范围的功能。就我们的目的而言，我们将使用接收器和导出器。

[OTel 接收器](https://github.com/open-telemetry/opentelemetry-collector/blob/main/receiver/README.md) 是“数据进入 OpenTelemetry 收集器的方式”。很简单。我们将配置一个接收器，通过上面列出的 gRPC 端口查找移动数据。OTel 的 gRPC 默认网络端口是 4317，因此收集器内置了此首选项。在 `collector-config.yaml` 中添加以下内容：

从 iOS 应用的导出器接收遥测数据后，我们希望收集器本身将遥测数据发送到 Zipkin。Zipkin 发行版有自己的端口 9411，因此请务必在 `collector-config.yaml` 中也定义它：

我们已经定义了接收器和导出器，但现在我们需要定义 OTel 收集器如何使用这些项目作为服务运行。在 `collector-config.yaml` 的末尾，定义此 OTel 收集器中的跟踪服务（为了清晰起见，包含了整个文件）：

这是我们收集器的完整配置。我们将在其中添加更多内容，以了解移动跟踪如何更好地服务于我们的目的，但这将在下一节中介绍。在此之前，我们需要了解如何部署收集器。

### 部署收集器

在 `docker-compose.yaml` 中，让我们定义部署我们的架构所需的组件：收集器和 Zipkin。此文件只是列出了组件应使用的 Docker 镜像以及它们之间的关系。例如，在下面的配置中，收集器将使用最新的可用镜像，并将依赖 Zipkin 作为发送目标。

您的 `docker-compose.yaml` 文件应如下所示：

您现在可以使用命令 `docker compose up` 部署 OTel 收集器，并连接 Zipkin。您的终端应同时显示来自收集器和 Zipkin 的输出：

## 优化您想要使用的移动信号

随着收集器的运行和 iOS 应用的使用，您将开始看到跟踪通过收集器运行到 Zipkin。通过将 gRPC 导出器附加到 iOS 应用，并将 OTel 收集器配置为导出到 Zipkin，我们可以重新创建之前在 Embrace 仪表板中看到的登录跟踪，并将其显示在 Zipkin 中：

提醒一下，您可能希望从 Zipkin 或您发送移动跟踪的任何位置排除某些信息。

例如，为了测量 SDK 初始化时间，并希望为其他移动库树立榜样，Embrace Apple SDK 提供了一个 `emb-setup` 跟踪。此跟踪可以与其他应用信号和库初始化相结合，以创建特定于正在启动的应用的“应用启动”测量，而不是一刀切的测量。但是，Embrace Outdoors 应用中的其他库要么不是基于 OTel 构建的，要么不允许我们测量它们的进程，因此 `emb-setup` 跟踪目前不可操作。

我们不需要 `emb-setup` 跟踪，但深入研究移动代码以将其删除需要深入调查和包装原生库。相反，让我们使用 OTel 收集器来排除该跟踪。这样做要简单得多，因为收集器提供了一组 [处理器](https://github.com/open-telemetry/opentelemetry-collector/blob/main/processor/README.md) 来调整我们在接收数据后但在导出数据之前的数据。

我们可以添加一个 [过滤器处理器](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/filterprocessor/README.md)，它将通过将处理器添加到我们的 `collector-config.yaml` 来阻止任何 `emb-setup`：

确保将其添加为收集器跟踪服务的一部分：

进行此更改后，Embrace SDK 设置跟踪将从导出中排除，因此也将从 Zipkin 的可视化中排除。您可以根据需要添加任意数量的处理器来排除、转换和采样遥测数据。

## 结论
Embrace Apple SDK 是 [otel-swift](https://github.com/open-telemetry/opentelemetry-swift) 插件的超集，专为移动设备设计。它的功能允许您将移动遥测数据发送到与后端可观测性数据相同的位置。

为什么开发团队应该将这些结合起来？如果您没有考虑用户体验，您如何知道您的系统是健康的？例如，您的网络不应该仅仅反映传输数据的服务。它们需要将[应用程序实例和用户视为同一网络系统的客户端](https://thenewstack.io/why-your-mobile-app-needs-client-side-network-monitoring/)。只有这样，您才能将这些信息转化为[有意义的指标](https://embrace.io/blog/mobile-slo-guide/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-collector)，来反映整个生态系统的健康状况和性能。

如果您有任何疑问或想了解更多关于在移动应用中设置 OpenTelemetry 的信息，您可以加入 [Embrace Slack Community](https://community.embrace.io/)。此外，访问 [Embrace 网站](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-collector) 以了解更多关于如何提供最佳用户体验的信息。

[Tech moves fast, don't miss an episode. Subscribe to our YouTube channel to stream all our podcasts, interviews, demos, and more.](https://youtube.com/thenewstack?sub_confirmation=1)