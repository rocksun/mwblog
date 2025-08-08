
<!--
title: 应用开发日志框架指南
cover: https://cdn.thenewstack.io/media/2025/08/ecd84b22-logging-framework.jpg
summary: 本文介绍了日志记录框架的价值、典型结构(Logger Context, Appender, Logger, Filter, Formatter, Configuration, Logger Config)以及Appender结构。选择框架时应考虑日志级别控制、灵活配置和与日志路由工具的兼容性。
-->

本文介绍了日志记录框架的价值、典型结构(Logger Context, Appender, Logger, Filter, Formatter, Configuration, Logger Config)以及Appender结构。选择框架时应考虑日志级别控制、灵活配置和与日志路由工具的兼容性。

> 译自：[Using Logging Frameworks for Application Development](https://thenewstack.io/using-logging-frameworks-for-application-development/)
> 
> 作者：Manning Book Authors

##### *编者注：本文节选自 Manning 出版的书籍 [Logging Best Practices: A Practical Guide to Cloud Native Logging](https://chronosphere.io/resource/logging-best-practices)。本书提供了一个实用的框架，可将日志记录从被动的调试工具转变为主动的竞争优势，您可以下载该书进行完整阅读。*

---

日志记录框架是一个结构化的工具集，用于处理日志的生成、格式化、过滤和路由方式。它使开发人员能够在不修改代码的情况下[配置日志行为](https://thenewstack.io/logging-best-practices-defining-error-codes)（例如日志级别或目标），从而提高可观测性并减少跨环境的摩擦。与单独的日志事件相比，它还传达了有关应用程序行为的更多含义和价值。

本节选自 Manning 出版的书籍 *[Logging Best Practices](https://chronosphere.io/resource/logging-best-practices/?utm_source=TNS&utm_medium=sponsored-content)*，探讨了日志记录框架的格局，因为它们在功能和设计上都具有一系列共性。对其有一个大致的了解将帮助您了解“可能实现的艺术”，并在选择框架时做出明智的决定。

通过[下载本书](https://chronosphere.io/resource/logging-best-practices/?utm_source=TNS&utm_medium=sponsored-content)，您可以了解不同语言中更主流的框架是否支持直接连接到 Fluentd 的能力，Fluentd 是企业中[应用最广泛](https://thenewstack.io/what-are-the-differences-between-otel-fluent-bit-and-fluentd)的日志收集技术之一。Fluentd 为多种编程语言提供日志记录库，因此我们还将研究这些库，以了解它们如何适应我们拥有的选项。

如果框架或 Fluentd 库不是一种选择，您可以让应用程序写入文件，因为 [Fluentd](https://chronosphere.io/learn/fluentd-to-fluent-bit-a-migration-guide/?utm_source=sponsored-content&utm_id=TNS) 可以使用此类信息。但是，通过文件连接的效率低于直接连接应用程序。

如果您正在使用函数即服务 (FaaS)，例如 [AWS](https://aws.amazon.com/?utm_content=inline+mention) Lambda 或来自 [Oracle](https://www.oracle.com/developer?utm_content=inline+mention) Cloud、[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure 和 [Google](https://cloud.google.com/?utm_content=inline+mention) 的函数服务，甚至是通过 [Fn Project](https://fnproject.io/) 自托管的函数，您会认识到这些服务非常短暂。因此，从这些非常短暂的服务中高效地记录日志更具挑战性。尝试连接到存储可能更难配置且连接速度更慢，因此更适合基于网络的日志记录。

## 日志记录框架的价值

无论日志记录框架的起源如何，所有框架都在不同程度上解决了以下关键主题：

* 提供一种使用日志级别分类轻松输出[日志事件](https://chronosphere.io/learn/what-is-log-file-and-log-data?utm_source=sponsored-content&utm_id=TNS)的方法。
* 允许通过配置控制发送的日志事件。
* 将日志事件定向到不同的输出形式，例如文件、stdout、HTTP 等。

虽然日志级别可以追溯到 Syslog 标准 ([RFC 5424](https://tools.ietf.org/html/rfc5424))，但对于应用程序开发（而不是导致 RFC 5424 定义的操作系统级工具），对日志记录库影响最大的因素之一是 Apache Log4J。这种影响可以归因于以下事实：Apache 软件基金会将设计和实现移植到了几种不同的语言中。但它的影响远不止于此。

虽然有可能基于相同的需求得出非常相似甚至相同的答案，但您可以在许多其他语言的日志记录框架中看到非常相似（如果不是相同）的 API 和功能。一些未与 Apache 软件基金会关联的日志记录框架公开承认借鉴了 Log4J 的设计原则。

为了公开透明，这些作者之一进入开源领域是在他们开始使用 [Java](https://thenewstack.io/introduction-to-java-programming-language/) 1.2 进行开发时，因此我们的观点可能有点偏颇。

遵循 Log4J 路线的优点在于第三方可以实现框架的某些部分，因此应用程序看不到任何差异。不过，配置可以更改行为，例如日志的存储方式，从平面文件到数据库。我们将在接下来的几节中更详细地介绍这一点。

*注意 对 Log4J 的引用可能会引起一些混淆，因为有两个版本：Log4J 和 Log4J2。今天引用 Log4J 时，您可以假定它指的是版本 2。版本 1 在 2015 年末被声明为已终止生命周期。版本 1 和版本 2 在概念上并没有根本的不同。但是，版本 2 经过重写，以解决版本 1 实现的一些弱点；这意味着可以编写该实现来利用新的语言功能。*

## 日志记录框架的典型结构

鉴于 Log4J 对许多日志记录框架和语言的影响，最好从检查 Log4J 结构开始。这样做，您可以轻松理解和掌握其他框架。下图说明了这种结构以及与不同类别的关系（我们使用了 [UML 类表示法](https://www.omg.org/spec/UML)，并进行了一些调整，如键所示）。

如图所示，涉及的类或模块是 Logger Context、Configuration、Filter、Logger、Logger Config、Formatter 和 Appender。

[![使用 UML 类表示法表示的常见日志记录结构，包括指示关系中的数量，例如 0 或 1 到多。](https://cdn.thenewstack.io/media/2025/08/c6dbaaea-logging-structure.png)](https://cdn.thenewstack.io/media/2025/08/c6dbaaea-logging-structure.png)

使用 UML 类表示法表示的常见日志记录结构，包括指示关系中的数量，例如 0 或 1 到多。

在以下各节中，我们将介绍每个组件所扮演的角色。我们根据其逻辑对日志记录框架的使用和行为的影响程度对组件进行了排序。

### Logger Context

这是应用程序中框架的基础。它负责保存对特定记录器对象的引用。它将处理任何配置文件，并根据需要创建必要的记录器对象。

记录器上下文通常构成所有日志记录元素的“一站式商店”；在应用程序中，此类用于检索一个对象，该对象将处理日志事件的相关处理（由记录器对象的实例表示）。

当在记录器上下文中请求记录器对象时，它可以派生或使用参数来确定要提供的记录器对象。如果没有与提供的标识符（通常是逻辑名称或类路径）关联的特定日志记录配置，则将提供默认的日志记录行为。

根据实现方式，它还可以协调任何细节，例如连接池等。这是确定具有单个对象的唯一位置，使其成为所有 Log4J 配置值的根。

### Appender

附加器的任务最容易理解，并且是处理日志事件的关键。根据特定的日志记录框架实现，附加器可能被称为适配器或传输，因为此层负责获取日志事件并将其发送到适当的目标。例如：

* 使用诸如 TCP/IP 消息之类的技术传输它们。
* 使用 API 调用来调用诸如 Logstash 之类的服务。
* 将日志事件写入或附加到文件末尾（因此得名）。

每个附加器将使用过滤器来控制它可能需要附加的日志事件。附加器还可以使用格式化程序将事件的内部表示形式转换为应如何输出；这可以从 JSON 到制表符分隔的行。某些类型的附加器只能以特定方式发出日志事件；这种关系有时会被简化并合并到一个类或模块中。

在日志记录框架的配置中，可以（并且预期）看到配置了几个不同的附加器，以解决将某些事件发送到具有不同日志级别的多个目标的问题。

### Logger

可以定义多个记录器（或仅上下文默认值），以便不同的应用程序部分可以以不同的方式使用日志记录 - 例如，用于记录[官方审计事件](https://chronosphere.io/resource/how-to-transform-your-logs-to-meet-your-observability-and-security-needs/?utm_source=sponsored-content&utm_id=TNS)的单独记录器与通用应用程序审计跟踪进行对比。

官方审计事件可能需要发送到数据库，并且包括审计在内的所有事件都应发送到日志记录框架。然后可以在代码中选择这些记录器。将有不同的配置，其中包含不同的记录器，例如要使用哪个附加器、要应用哪些过滤器等。

通过拥有多个记录器，您可以从更改代码库的不同部分的配置中受益，甚至可以为应用程序的某些部分提供多个配置（例如，将错误记录到 stdout，并将所有内容记录到文件中）。

### Filter

过滤器确定应发出哪些日志事件，主要是通过确定日志事件的级别是否高于或低于配置中设置的阈值。由于过滤器与附加器相关联，因此可以使用不同的日志级别配置不同的日志目标。

例如，您可以将控制台附加器的日志级别设置为 Warning，并将文件附加器的日志级别设置为 Info。结果是只有 Warning 和 Error 事件才会进入控制台，但文件中包含更多详细信息。

### Formatter

如附加器所述，格式化程序的任务是构造附加器输出，以便日志条目以所需或要求的形式显示（例如，以 12 小时或 24 小时格式显示时间）。某些附加器允许灵活性（例如，文件附加器）。

### Configuration

通常，您希望通过配置而不是代码来驱动应用程序的日志记录，因为这允许在不必进行侵入性代码更改的情况下配置日志记录。这也使得在验证配置时可以更快地进行周转。它允许根据部署上下文更改日志的处理方式。

例如，您可以进行配置，将所有内容发送到开发机器的 stdout。但是，在测试和生产环境中，配置设置为将日志发送到 Elasticsearch。

### Logger Config

记录器配置是特定记录器的整个日志记录配置的子集（请参阅上面的“Logger”部分）。这将跟踪相关的配置部分，并将其转换为代码中的正确对象。这可能包括使用诸如工厂设计模式之类的内容。

## Appender 结构

通常，附加器是通过继承或封装的层次结构构建的，因此每一层复杂性都可以利用更简单的操作。最终，这将取决于标准接口定义，因此无论附加器如何，它们都以相同的方式进行协调，就像 Fluentd 对其插件所做的那样。

该图显示了 Log4J 如何通过从实现接口并提供通用逻辑的基类继承来组织其附加器，然后对其进行扩展以提供一组基本附加器，例如控制台附加器。

从此派生层开始，该层构建了专业化的增加。这在 `AbstractOutputStreamAppender` 中最为明显，它随后用于常规套接字用例，并进一步专门用于将日志发送到符合 Syslog 的解决方案中。

[![Log4J 的一些附加器如何相关的 UML 表示形式。](https://cdn.thenewstack.io/media/2025/08/d226aee1-log4j-appenders.png)](https://cdn.thenewstack.io/media/2025/08/d226aee1-log4j-appenders.png)

Log4J 的一些附加器如何相关的 UML 表示形式。

要继续阅读，请下载 *[Logging Best Practices](https://chronosphere.io/resource/logging-best-practices/?utm_source=TNS&utm_medium=sponsored-content)*，以了解有关如何评估日志记录框架和优化架构的更多信息。

## 常见问题解答

**问：** 如何为我的应用程序选择合适的日志记录框架？

**答：** 选择一个满足以下条件的框架：

* 支持日志级别控制和灵活配置。
* 提供多个附加器（例如，文件、stdout、HTTP）。
* 与您的语言/平台生态系统保持一致。

寻找社区采用（例如，Java 中的 Log4J，它对其他语言的影响）、可扩展性以及与 Fluentd 等日志路由工具的兼容性。

**问：** 日志记录框架中的“附加器”是什么？

**答：** 附加器是一个将日志事件发送到特定目标（例如文件、控制台或远程服务）的组件。它通常包括过滤器和格式化程序来控制记录什么以及如何记录。Log4J 风格的附加器在许多框架中很常见。

**问：** 记录器和记录器上下文之间有什么区别？

**答：** 记录器上下文是管理所有记录器实例、处理配置和协调日志记录行为的中心点。记录器是您的代码用于发出日志事件的实际对象，通常按模块或目的进行范围限定（例如，[审计日志](https://chronosphere.io/learn/audit-log-definition-guide/?utm_source=sponsored-content&utm_id=TNS)与常规日志）。

**问：** 我可以在不修改应用程序代码的情况下更改日志记录行为吗？

**答：** 可以。大多数现代日志记录框架都是配置驱动的。您可以根据环境（例如，开发环境的 stdout，生产环境的 Elasticsearch）通过配置文件更改日志级别、输出或格式，从而实现灵活性和更快的部署周期。