# 简介

对于任何交付云原生应用的开发人员来说，OpenTelemetry 通常是应用运行的云原生环境的一部分。然而，如果您不是在该领域工作的工程师，那么 OpenTelemetry 可能不是您的可观测性和监控解决方案中的一套常见产品。

我们希望在本文和概念验证 (POC) 中展示的是，通过利用 OpenTelemetry 的强大功能和特性，实现 WebLogic Server 环境的可观测性现代化和提升。OpenTelemetry 将提供统一的、与供应商无关的遥测数据，从而增强性能监控，加速故障排除，并支持企业级 Java 应用中的主动式、数据驱动操作。

# 什么是 OpenTelemetry

OpenTelemetry 是云原生计算基金会 (CNCF) 的一个项目，它是 OpenTracing 和 OpenCensus 这两个先前项目合并的产物。它是一个框架和工具包，旨在促进构成可观测性三大支柱（traces（追踪）、metrics（指标）和 logs（日志））的数据的生成、导出和收集。OpenTelemetry 社区正在评估的第四个支柱——profile（剖析）——也即将到来。

OpenTelemetry 的一个主要目标是实现应用和系统的插桩，无论编程语言、基础设施和运行时环境如何。

OpenTelemetry 正在迅速成为可观测性的事实标准。Grafana Labs 2025 年的一项[调查](https://grafana.com/blog/2025/03/25/observability-survey-takeaways/?pg=survey-2025&plcmt=footer-cta-1)指出了一些有趣的统计数据：超过 50% 的受访者在生产环境中使用 OpenTelemetry，另有 38% 的人正在积极研究 OpenTelemetry 的使用。

![调查结果](/wp-content/uploads/sites/71/2025/10/Picture1-6.png)

# WebLogic Server 中的 OpenTelemetry

现在我们已经了解了可观测性和 OpenTelemetry 的背景，让我们开始介绍这个 POC。POC 的目的是演示使用 OpenTelemetry 配合 WebLogic Server 和 Oracle Database 23aiv8 实现可观测性。我们将涵盖可观测性的三大支柱：指标、追踪和日志。下表提供了概念验证中包含的产品和版本列表。

![产品和版本](/wp-content/uploads/sites/71/2025/10/Screenshot-2025-06-17-at-11.05.11-AM.png)

所有 OpenTelemetry 组件、Prometheus、Jaeger 和 OTel Collector 都部署在 Kubernetes 集群 (OKE) 中。将这些组件部署到 Kubernetes 集群纯粹是为了方便。我当时有一个运行中的 Kubernetes 集群，并且使用 Helm 使部署变得容易。

WebLogic Server (WLS) 部署运行在虚拟机上。WLS 域包含一个管理服务器和两个受管服务器。下图高层次地展示了组件的部署情况。

![架构](/wp-content/uploads/sites/71/2025/10/otelwithwls.png)

要从 WLS 中抓取遥测数据，我们需要提供对几个 Java jar 文件的访问权限。

下面的脚本演示了如何设置必要的环境变量。它被恰当地命名为：“enableOTEL.sh”。

![enableOTEL.sh](/wp-content/uploads/sites/71/2025/10/Screenshot-2025-06-17-at-11.14.56-AM.png)

要了解所有 OpenTelemetry 环境变量，请参阅 OpenTelemetry [文档](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/)。我将介绍几个关键的环境变量，这些变量是确保成功部署、配置和从 WLS 以及部署到 WLS 的应用中抓取 OpenTelemetry 信号所必需的。

**WEBLOGIC\_OTEL：** 这是一个自定义变量，在 “setDomainEnv.sh” 中设置和引用。这不是一个全新的 “setDomainEnv.sh” 脚本，它是 WLS 产品附带的标准脚本。该环境变量指向 OpenTelemetry Java 代理程序所在的位置。Java 代理程序也称为零代码插桩代理程序。

![setDomainEnv.sh](/wp-content/uploads/sites/71/2025/10/Screenshot-2025-06-17-at-11.24.25-AM.png)

下面显示的是 “setDomainEnv.sh” bash 脚本的片段。“#OpenTelemetry Start” 和 “#OpenTelemetry End” 之间的区域是获取 WLS 和 Oracle 数据库可观测性三大支柱的必要修改。

![setDomainEnv OTEL 配置](/wp-content/uploads/sites/71/2025/10/Screenshot-2025-06-17-at-11.24.42-AM.png)

**OTEL\_JDBC\_LIB：** 同样，这是一个自定义环境变量。如果您计划从 JDBC 返回追踪跨度，则需要此变量。我强烈建议在 WLS 上执行您的应用并计划获取遥测数据时使用它。

**OTEL\_SDK\_JAR：** 这是另一个自定义环境变量。如果您计划从 JDBC、数据库捕获追踪跨度，并且已将下面讨论的属性添加到数据库连接池中，则需要这两个 jar 文件。

![源 enableOTEL.sh](/wp-content/uploads/sites/71/2025/10/Screenshot-2025-06-17-at-11.43.51-AM.png)

如果找不到这些 jar 文件并且已添加数据库属性，那么在尝试通过 JDBC 连接访问数据库时，您将收到 “ClassNotFoundExceptions”。

**CHAOS\_DUKEY：** 此环境变量不是必需的。Chaos\_dukey 是一个用于在您的应用中注入延迟的框架。此处仅用于演示如果您想在应用测试中注入延迟，如何添加它。

注意：请勿在生产环境中使用此功能。

自定义脚本已构建并执行，WLS 服务器已启动并运行，我们现在需要向数据库连接池添加属性。让我们看一下。

WLS 实例启动后，启动远程控制台并访问“sources”并创建一个数据源。如果您不确定如何创建 JDBC 连接池，请参阅 WLS [文档](https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/14.1.2/tasks/jdbc.html#GUID-C84425E3-6B4C-4932-8BFA-6C7B1B68C66F)。

数据源和 JDBC 连接池创建后，更新 JDBC 连接池的属性，如下所示。

![远程控制台](/wp-content/uploads/sites/71/2025/10/Screenshot-2025-05-05-at-6.55.56-PM.png)

连接池属性：

键：**oracle.jdbc.provider.traceEventListener**

值：**open-telemetry-trace-event-listener-provider**

WLS 和数据库的所有配置都已完成，可以发送指标、追踪和日志（在 OpenTelemetry 中称为信号）。

## OpenTelemetry 配置

我们需要设置 OpenTelemetry 收集器来接收、处理和导出遥测数据。下面显示的 yaml 文件是 OpenTelemetry 收集器的配置。该配置通过 configMap 创建和更新。

![OTelCollector](/wp-content/uploads/sites/71/2025/10/Screenshot-2025-06-17-at-11.58.03-AM.png)

OTel 收集器是所有接收器、处理和导出器定义的地方。从上面的 yaml 文件中，我们将查看一些关键部分。

**接收器：** 接收器从一个或多个源收集遥测数据。它们可以是拉取或推送式的，并可能支持一个或多个数据源。grpc 协议在端口 4317 上接收，http 协议在 4318 上接收。默认情况下，这三种信号由 “otlp” 接收器消费。

**导出器：** 导出器将数据发送到一个或多个后端或目的地。在上面的 yaml 文件中，我们定义了 3 个导出器：调试、Jaeger 及其相关端点，以及 Prometheus 及其相关端点。稍后讨论的自定义指标被导出到 Prometheus。

**Services.pipeline：** 管道部分是配置管道的地方。管道由三种类型之一组成：追踪、指标、日志。

我们现在一切准备就绪，可以开始从 WLS 和部署的应用中抓取遥测数据了。现在，我们希望提供比零插桩代理程序提供的更多遥测数据。首先，让我们看看如何向应用代码添加追踪跨度。

![OpenTelemetry配置](/wp-content/uploads/sites/71/2025/10/Screenshot-2025-06-17-at-12.02.52-PM.png)

在上面显示的代码中，我们使用的是 Java 管理代理；因此，无需以编程方式创建 “SdkTracerProvider”、“OpenTelemetrySdk” 或创建 “OtlpHttpSpanExporter”。“WEBLOGIC\_OTEL” 环境变量为应用程序提供了管理代理。要访问 “OpenTelemetry”、“Tracer” 和 “Meter”，需要向 “GlobalOpenTelemetry” 类发送一个 “get” 请求。上面的代码演示了如何访问这些 OpenTelemetry 组件。

创建计数器是为了演示如何实例化自定义的 “LongCounter” 指标。其用法将在文档后面演示。

下面的代码片段展示了如何为方法创建追踪跨度。注解 “@WithSpan” 将生成一个名为 “CustomerResource.getCustomers” 的追踪跨度。“@WithSpan” 指定跨度的类型以及为跨度提供的名称。指定名称使得在仪表板中跟踪单个跨度变得非常容易。

![跨度定义](/wp-content/uploads/sites/71/2025/10/Screenshot-2025-06-17-at-12.06.31-PM.png)

应用程序部署并运行后，该跨度将在 Jaeger 控制面板中可见，如下所示。

![basicCustomer 追踪跨度](/wp-content/uploads/sites/71/2025/10/Screenshot-2025-05-06-at-10.53.47-AM.png)

您还会注意到上面有一个有趣的跨度，名为 “my-service”（在数据库的未来版本中，这个名称很可能会改变）。从新的 Oracle DB 23ai.V8 开始，追踪跨度现在可以在数据库中捕获。这个很棒的功能可以测量我们在数据库中花费的时间。

我想指出 Oracle 在其 JDBC 数据库驱动程序中提供的另一个重要功能。数据库驱动程序现在提供 OpenTelemetry 追踪。让我们看看有哪些可用功能。

![jdbc 追踪跨度](/wp-content/uploads/sites/71/2025/10/Screenshot-2025-05-06-at-11.23.21-AM.png)

上面显示的扩展跨度由 JDBC 驱动程序提供。作为开发人员，您无需在应用程序代码中进行任何操作即可获取这些跨度。请确保您已按照自定义脚本 “enableOTEL.sh” 中所示提供了 jar 文件。另外，请确保您已添加本文前面所示的数据库连接池属性。

现在让我们看看如何使用 OpenTelemetry 指标。我前面提到了 LongCounter 的使用。对于熟悉 Prometheus API 的人来说，LongCounter 是 OpenTelemetry 中与 Prometheus 中的 Counter 指标等效的指标。此计数器累计特定查询执行的总次数。

该指标由 OTel Collector 抓取，并最终导出到 Prometheus。然后您可以通过指标名称在 Prometheus 中进行搜索。Prometheus 控制面板中显示的是 “basicCustomer\_customer\_resource\_total” 指标。此指标指定了 “customer\_queries” 属性，并按执行的具体 SQL 查询对其进行细分。如下所示，有 “getCustomers” 的一个实例和 “getCustomerById” 的一个实例。

显然，这只是您可以使用 OpenTelemetry API 添加的许多潜在自定义指标之一。

![Prometheus](/wp-content/uploads/sites/71/2025/10/Screenshot-2025-05-06-at-4.24.51-PM.png)

# 为什么选择 OpenTelemetry

可观测性和监控不是一回事，它不仅仅是一套工具和实践。两者在构建更具弹性、可靠和高效的系统管理中都扮演着重要的角色。

云原生计算基金会 (CNCF) 对可观测性的定义：

* “可观测性是系统的一个属性，它定义了系统能够生成可操作洞察的程度。它允许用户从这些外部输出了解系统的状态并采取（纠正）行动。”
* “计算机系统通过观察低级信号（如 CPU 时间、内存、磁盘空间）和高级业务信号（包括 API 响应时间、错误、每秒事务数等）来衡量。这些可观测系统通过专门的工具（即所谓的可观测性工具）进行观察（或监控）。”
* “可观测系统为其操作员提供有意义的、可操作的数据，使他们能够实现有利的结果（更快的事件响应、更高的开发人员生产力），并减少繁重工作和停机时间。”
* “因此，系统的可观测性将显著影响其运营和开发成本。”

OpenTelemetry 项目的进一步定义和澄清：

* 可观测性让您可以在不了解系统内部工作原理的情况下，通过提问来从外部理解一个系统。
* 要对您的系统提问，您的应用程序必须正确插桩。也就是说，应用程序代码必须发出追踪、指标和日志等信号。当开发人员无需添加更多插桩即可排查问题，因为他们拥有所需的所有信息时，应用程序就已正确插桩。

总结

使用 OpenTelemetry、WebLogic Server 和 Oracle Database，您可以在请求的整个处理过程中获取遥测数据。指标、追踪和日志这三种信号将帮助工程师、管理员和 DBA 更深入地了解其应用程序和数据库操作的整体性能。此外，添加到 JDBC 和 Oracle 数据库的信号有助于工程师分析代码中、数据库中以及通过推断在网络遍历中花费的时间。

将 OpenTelemetry 与 Oracle WebLogic Server 结合使用具有诸多优势：

* 在云原生和非云原生环境中常用的一套标准工具。
* 统一的、与供应商无关的遥测数据，可增强性能监控、加速故障排除，并支持企业级 Java 应用中的主动式、数据驱动操作。
* 广泛的社区支持。
* OpenTelemetry 产品套件可以轻松地被 WebLogic Server 使用，而无需对 WLS 产品进行任何修改。
* Oracle 已将 OpenTelemetry 添加到 Oracle 数据库驱动程序和 db23aiV8 中。
* 在 OCI 中，追踪数据可以发送到 OCI APM。

请继续关注未来关于 OpenTelemetry、WebLogic Server 和 Oracle 数据库的更多博客文章。