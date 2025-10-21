<!--
title: 声明式配置之旅：为何链路追踪花了五年才“无视”健康检查？
cover: https://opentelemetry.io/img/social/logo-wordmark-001.png
summary: OpenTelemetry声明式配置利用YAML解决复杂配置，如耗时五年的健康检查排除。它取代环境变量，提供灵活、可持续的解决方案，目前Java已支持，其他语言正在扩展。
-->

OpenTelemetry声明式配置利用YAML解决复杂配置，如耗时五年的健康检查排除。它取代环境变量，提供灵活、可持续的解决方案，目前Java已支持，其他语言正在扩展。

> 译自：[The Declarative configuration journey: Why it took 5 years to ignore health check endpoints in tracing](https://opentelemetry.io/blog/2025/declarative-config/)
> 
> 作者：Gregor Zeitlinger

过去几年中，Java OpenTelemetry 最持久和最受欢迎的功能请求之一，就是能够高效地[丢弃健康检查端点的 Span](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/1060)——或任何其他低价值、高成本的端点。这个问题于2020年8月首次提出，然而一个全面的解决方案却在相当长的时间内难以捉摸。为什么我们花了五年时间才解决这个看似简单的问题？答案在于OpenTelemetry配置系统的基本原则以及迈向更健壮、更灵活方法——声明式配置——的旅程。

从一开始，OpenTelemetry 就依赖环境变量进行配置，这是因为环境变量在各种语言中普遍可用且易于解析。然而，随着对更复杂配置用例的需求增长，简单的基于字符串的环境变量的局限性日益明显，使得高级配置变得繁琐且难以管理。

声明式配置应运而生，这是一项强大的演进，它利用 YAML 文件来定义 OpenTelemetry 设置。这一转变允许从任何树形源读取数据，从根本上改变了我们处理复杂配置的方式。在本文中，我们将探讨声明式配置如何为过去的挑战提供优雅的解决方案，并通过 Java 中健康检查排除等实际用例展示其立竿见影的影响。

## 入门

配置文件与语言无关，因此一旦创建了一个文件，就可以将其用于所有 SDK。唯一的例外是带有特定语言名称的参数，这些参数仅与该语言相关（例如 `instrumentation/development.java.spring_batch` 参数）。请记住，声明式配置是**实验性的**，因此内容可能仍会发生变化。

以下是您可以用于入门的基本配置文件示例：

```
file_format: '1.0-rc.1'

resource:
  attributes_list: ${OTEL_RESOURCE_ATTRIBUTES}
  detection/development:
    detectors:
      - service: # will add "service.instance.id" and "service.name" from OTEL_SERVICE_NAME

tracer_provider:
  processors:
    - batch:
        exporter:
          otlp_http:
            endpoint: ${OTEL_EXPORTER_OTLP_TRACES_ENDPOINT:-http://localhost:4318}/v1/traces

meter_provider:
  readers:
    - periodic:
        exporter:
          otlp_http:
            endpoint: ${OTEL_EXPORTER_OTLP_METRICS_ENDPOINT:-http://localhost:4318}/v1/metrics

logger_provider:
  processors:
    - batch:
        exporter:
          otlp_http:
            endpoint: ${OTEL_EXPORTER_OTLP_LOGS_ENDPOINT:-http://localhost:4318}/v1/logs

```

您只需将 `OTEL_EXPERIMENTAL_CONFIG_FILE=/path/to/otel-config.yaml` 传递给应用程序，即可激活实验性的声明式配置选项。在撰写本文时，此变量仅适用于 Java agent 和 JavaScript。

## Java 中的声明式配置

现在让我们看看声明式配置在 Java 生态系统中的更广泛实现。作为该领域的先行语言，Java agent 2.21+ 现在已完全支持声明式配置，大多数 instrumentation 和功能都已可用。我们正在努力在2026年全年整合剩余功能，您可以在[项目看板](https://github.com/orgs/open-telemetry/projects/151)上跟踪我们的进展，并查看[尚未支持的功能列表](/docs/zero-code/java/agent/declarative-configuration/#not-yet-supported-features)。

根据您是全新开始还是从使用环境变量进行迁移，有几种资源可以利用：

*   上一节中介绍的基本（与语言无关）配置文件示例，是您在不需要进一步定制时最快的入门方式。
*   [迁移配置文件](https://github.com/open-telemetry/opentelemetry-configuration/blob/main/examples/sdk-migration-config.yaml)将旧的环境变量映射到 YAML 模式中，为已使用环境变量配置工作负载的用户提供了即插即用的替代方案。
*   [完整配置文件](https://github.com/open-telemetry/opentelemetry-configuration/blob/main/examples/kitchen-sink.yaml)（“大杂烩”）展示了整个模式，并以注释形式进行了文档标注。这对于希望查看所有可用选项及其默认值的用户很有用。

上述所有文件都适用于支持声明式配置的任何语言。

此外，还有许多特定于 Java agent 的设置，它们位于配置文件的 `instrumentation` 部分。例如，如果您的应用程序中存在系统属性 `otel.instrumentation.spring-batch.experimental.chunk.new-trace`，您可以通过移除 `otel.instrumentation` 前缀，在 `.` 处分割，并将 `-` 转换为 `_` 来创建声明式配置文件。

```
file_format: '1.0-rc.1'

# ...

instrumentation/development:
  java:
    spring_batch:
      experimental:
        chunk:
          new_trace: true

```

有了这个配置，开发人员可以继续像往常一样使用他们的 Java instrumentation，将遥测数据发送到他们选择的[可观测性]后端。此外，声明式配置文件提供了根据需要扩展和添加更多参数的灵活性，从而可以高度定制和细致地控制[可观测性]设置。

## 健康检查排除

正如引言中提到的，Java 社区中最受欢迎的功能请求之一是能够将健康检查（或其他不重要或嘈杂的资源）从生成跟踪中排除。

为此，您需要在 `tracer_provider` 配置中添加一个新的 `sampler` 块，如下所示：

```
file_format: '1.0-rc.1'

# ... the rest of the configuration ....

tracer_provider:
  # Configure sampling to exclude health check endpoints.
  sampler:
    rule_based_routing:
      fallback_sampler:
        always_on:
      span_kind: SERVER
      rules:
        # Action to take when the rule matches. Must be DROP or RECORD_AND_SAMPLE.
        - action: DROP
          # The span attribute to match against.
          attribute: url.path
          # The pattern to compare the span attribute to.
          pattern: /actuator.*
# ... the rest of the tracer_provider configuration ...

```

有关可用选项的更多详细信息，请参阅[Java 采样器文档](https://github.com/open-telemetry/opentelemetry-java-contrib/tree/main/samplers)。

亲自尝试：

1.  保存[完整配置](https://gist.github.com/zeitlinger/09585b1ab57c454f87e6dcb9a6f50a5c)
2.  使用 `-Dotel.experimental.config.file=/path/to/otel-config.yaml` 运行 Java agent

## 可用性

阅读了声明式配置后，您可能想知道它在哪里可用以及如何开始使用。您可以在[文档](/docs/languages/sdk-configuration/declarative-configuration)中找到有关如何入门以及支持哪些语言的指南。截至本文撰写之时，Java 完全合规，PHP、JavaScript 和 Go 部分合规。要查看最新状态，请查阅[合规性矩阵](https://github.com/open-telemetry/opentelemetry-specification/blob/main/spec-compliance-matrix.md#declarative-configuration)或[语言实现跟踪问题](https://github.com/open-telemetry/opentelemetry-configuration/issues/100)。

### Java

如前所述，[Java](/docs/zero-code/java/agent/declarative-configuration/) 中的声明式配置是实验性的，但已可使用。使用我们之前讨论的示例来设置您的新配置。如果您有疑问或反馈，请在 CNCF Slack 的 [`#otel-java`](https://cloud-native.slack.com/archives/C014L2KCTE3) 频道中联系。

*致其他语言维护者：创建一个桥接模块以将声明式配置设置和环境变量适配到通用接口是很有用的。对于 Java，这就是[声明式配置桥接器](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/declarative-config-bridge)。*

### JavaScript

JavaScript SDK 中的实现目前正在开发中。一个名为 [opentelemetry-configuration](https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-configuration) 的新包已经创建，它同时处理环境变量和声明式配置。通过这种方法，用户在环境变量和配置文件之间切换时无需更改其 instrumentation，因为新包会处理它并为这两种情况返回相同的配置模型。目前，此配置包正在添加到其他 instrumentation 包中，以便它们可以利用声明式配置。如果您有疑问，请在 CNCF Slack 的 [`#otel-js`](https://cloud-native.slack.com/archives/C01NL1GRPQR) 频道中联系。

### PHP

PHP 实现部分合规，您可以通过[从配置文件初始化](https://github.com/open-telemetry/opentelemetry-php/tree/main/src/Config/SDK#initialization-from-configuration-file)来开始使用它。如需帮助或反馈，请在 CNCF Slack 的 [`#otel-php`](https://cloud-native.slack.com/archives/C01NFPCV44V) 频道中联系。

### Go

Go 具有声明式配置的[部分实现](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/otelconf)。每个受支持的 schema 版本都有其对应的包目录。例如，导入 `go.opentelemetry.io/contrib/otelconf/v0.3.0` 将为您提供支持配置 schema 0.3.0 版本的代码。您可以在[包索引](https://pkg.go.dev/go.opentelemetry.io/contrib/otelconf)中找到所有可用版本。如果您对如何使用它有疑问，请在 CNCF Slack 的 [`#otel-go`](https://cloud-native.slack.com/archives/C01NPAXACKT) 频道中联系。

## 历程

那么，为什么我们真的花了五年时间才在跟踪中忽略健康检查端点呢？

声明式配置的历程，以及随之而来的健康检查排除解决方案，凸显了 OpenTelemetry 的一个核心原则：通过严格的规范构建可持续的解决方案。

从一开始，OpenTelemetry 对环境变量的依赖虽然普遍可用，但对于高级配置来说却日益复杂。新的环境变量最终被禁止使用，从而留下了一个需要更健壮解决方案来填补的空白。

正如我们在本博客文章中介绍的，替代方案是声明式配置。制定并就精确的语法和语义达成一致是一个耗时且有时令人筋疲力尽的过程。例如，我们讨论了关于如何嵌入环境变量的多个提案，直到我们提出了当前使用 `${OTEL_EXPORTER_OTLP_ENDPOINT:-http://localhost:4318}` 的解决方案。

这个过程为 OpenTelemetry 社区如何运作提供了一个有力的案例研究。它证明了建立共识、促进协作以及在不同项目中引入重要新功能并推动其实施所需的集体努力。

## 声明式配置的下一步是什么？

声明式配置的旅程远未结束。我们目前的重点是大力扩展语言支持，这对于确保开发人员，无论他们偏好何种工具，都能利用声明式方法的优势至关重要。

随着我们不断开发和完善这些功能，我们非常关注用户反馈。我们鼓励您开始尝试当前的实现，并积极沟通任何缺失的功能、痛点或改进领域。这种协作方法将帮助我们优先安排开发工作，并确保我们构建的解决方案真正满足社区的需求。您可以通过 CNCF Slack 的 [`#otel-config-file`](https://cloud-native.slack.com/archives/C0476L7UJT1) 频道分享您的反馈或问题。

除了提供反馈，还有其他方式可以参与并为声明式配置的发展做出贡献。每个 OpenTelemetry SDK 都有一个专门负责其实施的[特殊兴趣小组 (SIGs)](https://github.com/open-telemetry/community?tab=readme-ov-file#implementation-sigs)。加入这些 SIGs 提供了一个直接途径，可以了解开发现状，参与讨论，并发现贡献机会。无论是通过代码贡献、文档增强，还是仅仅分享您的经验，每一份贡献都有助于推动声明式配置生态系统的发展。您的积极参与是为现代应用程序开发培养一套强大而多功能的工具的关键。

期待您的来信！

## 更多资源

要了解更多关于声明式配置的工作，这里有一些额外的资源供您探索：