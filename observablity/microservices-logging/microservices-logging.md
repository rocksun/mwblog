<!--
title: 微服务日志实践指南 [包含最佳实践]
cover: ./cover.png
-->

微服务日志是在分布式微服务架构中跟踪和记录特定服务活动的实践。日志记录是任何软件系统的重要方面，对于微服务架构更为关键，因为有许多小型、独立的服务相互交互。

> 译自 [A Practical Guide to Logging in Microservices [Includes Best Practices]](https://signoz.io/blog/microservices-logging)。作者 Vaishnavi Abirami。

## 什么是微服务？

微服务架构是一种软件设计方法，其中一个大型应用被构建为一组小型、独立的服务。微服务架构的目标是通过更容易独立开发、测试和部署各个服务，从而提高软件系统的可扩展性和可维护性。

微服务架构的一个主要优势是它允许以更精细和细粒度的方式构建和演进软件系统。这使得能够更容易地对系统的各个部分进行更改，而不影响整个系统。

## 日志在微服务中的重要性

日志记录是任何软件系统的重要方面，尤其在微服务架构中尤为重要，因为可能有许多不同的服务同时运行并相互交互。

在微服务系统中，重要的是在服务级别记录事件和错误，以便能够追踪和调试可能在特定服务内部发生的问题。还重要的是要有一个集中式的日志系统，可以收集和存储来自所有不同服务的日志消息，以便能够全面了解系统并识别可能从单个服务的日志中看不出的模式或趋势。

## 以下是一些微服务日志记录的最佳实践：

1. 记录什么

事件和事务：捕获操作、事件和业务或系统事务，以提供对系统行为的洞察。错误：记录错误、异常和堆栈跟踪，以帮助排除故障并了解系统内的故障点。

2. 使用日志级别

利用各种日志级别（DEBUG、INFO、WARN、ERROR、FATAL）对日志进行分类，根据严重性和重要性，有助于过滤和关注最关键的问题。

3. 使用结构化日志

与记录非结构化消息相比，考虑使用结构化日志格式，如JSON。这将使搜索和分析日志更容易，也将更容易将日志发送到集中式日志解决方案。在集中位置，您可以进行搜索，例如查找“HTTP代码”为500或更高的日志。为了为您的微服务日志提供一致而可适应的格式，请使用结构化日志。

4. 为每个请求使用唯一的关联ID

想象一下，大量微服务每小时产生数百万条日志条目。如果发生异常情况，要确定根本原因将是具有挑战性的。在这种情况下，一个宝贵的工具是关联ID。对于发送到服务器的每个请求，将插入一个关联请求ID。标识符在每个需要完成请求的服务之间来回传递。如果您尝试调试问题，第一件事就是找到随请求一起提供的特殊标识。更好的做法是在处理错误日志时使用特殊ID。

5. 在日志中添加上下文数据

确保在日志中包含足够的上下文，以便能够理解导致错误或调试问题的事件。这可能包括请求URL、请求参数和用户ID等信息。

6. 不记录敏感数据

避免记录个人身份信息（PII）。PII包括密码、账号、社保号等。由于可能需要开发人员检查日志以满足调试需求，存在隐私问题。如果您的公司希望评估用户行为，请考虑通过日志记录对某些类型的敏感数据进行聚合，以保持用户匿名性。

7. 提供信息丰富的应用程序日志

当错误发生时，日志应包含理解错误所需的所有信息。通过微服务日志访问的信息越多，我们就能更有效、更迅速地进行故障排除。

至少，日志需要包含以下详细信息：

- 服务名称
- 用户ID
- 主机名
- 关联ID（可以是traceid的形式）
- 请求ID
- 时间戳
- 总持续时间（在请求结束时）
- 方法名称
- 调用堆栈（日志的行号）
- 请求方法
- 请求URI

8. 集中式日志解决方案

在微服务架构中，如果日志分散在多个服务中，追踪日志可能会很困难。使用SigNoz或Elastic等集中式日志解决方案可以帮助您在一个地方收集、查询和查看来自所有服务的日志。像SigNoz这样的日志分析工具提供仪表板，以可轻松消化的格式直观呈现日志数据。

9. 记录性能指标

除了记录事件和错误之外，还考虑记录性能指标，如响应时间和资源利用情况。这将使您能够监控服务的性能并识别任何潜在问题。

## 对集中式日志服务的需求

在微服务架构中，一个汇总所有服务日志的单一集中式日志服务应该是首选解决方案。在软件世界中，独特/不寻常的问题并不少见，我们当然不希望在多个日志文件或开发的仪表板之间来回查找，以了解是什么导致了相同的问题。

当一个或多个服务失败时，我们需要知道哪个服务遇到了问题以及原因。在微服务中解密完整的请求流程也很困难。例如，调用了哪些服务？以及该服务的调用顺序和频率是什么？

## 在日志中集成可观测性

如果应用程序日志包含请求上下文标识符（如跟踪ID、跨度ID、跟踪标志或基于[w3c跟踪上下文建议](https://www.w3.org/TR/trace-context/#traceparent-header)的用户定义行李），将在日志和跟踪之间提供更丰富的关联，以及在分布式系统的不同组件发出的日志之间提供关联。这将使在分布式系统中日志变得更加有价值。

但在继续之前，让我们简要了解一下什么是可观测性。

### 什么是可观测性？

我们认为可观测性的目标是快速解决客户问题。如果监控仪表板无法帮助工程团队快速识别性能问题的根本原因，那么创建监控仪表板就没有意义。

现代分布式软件系统有很多移动组件。因此，在设置监控时，您可能不知道解决问题所需的答案。这就是可观测性发挥作用的地方。

可观测性使应用程序所有者能够在调试应用程序问题时得到任何可能出现的问题的答案。

### 日志、指标和跟踪作为可观测性的支柱

日志、指标和跟踪通常被称为可观测性的三个支柱。这三个遥测信号在关联时可以更快地推动应用程序洞察。

对于强大的可观测性，具有无缝关联遥测信号的方式至关重要。例如，如果您看到特定服务的延迟目前很高，您能迅速深入相关的日志吗？您能够将指标与跟踪相关联，找出请求过程中问题发生的位置吗？

现在的问题是我们如何生成、收集和存储遥测信号，以便它们可以轻松关联并一起进行分析。这就是OpenTelemetry发挥作用的地方。

## 什么是OpenTelemetry？

[OpenTelemetry](https://opentelemetry.io/) 是一套旨在规范遥测数据（日志、指标和跟踪）的生成、收集和管理的 API、SDK、库和集成。OpenTelemetry 是由 Cloud Native Computing Foundation 创建的项目，是在合并了来自 Google 的 OpenCensus 和来自 Uber 的 OpenTracing 后形成的。

使用 OpenTelemetry 收集的数据是与供应商无关的，可以导出为多种格式。遥测数据已经成为观察分布式系统状态的关键因素。随着微服务和多语言体系结构的普及，有必要建立一个全局标准。OpenTelemetry 的目标是填补这个空白，并且目前在这方面做得非常出色。

SigNoz 是为原生支持 OpenTelemetry 而构建的。

我们以符合 OpenTelemetry 数据模型的方式发出日志、跟踪和指标，并通过 SigNoz 收集器发送数据，其中可以进行统一的丰富和处理。

OpenTelemetry 定义了[日志数据模型](https://opentelemetry.io/docs/specs/otel/logs/data-model/)。数据模型的目的是对 LogRecord 的定义、记录、传输、存储和由日志系统解释的数据有一个共同的理解。新设计的日志系统预期根据 OpenTelemetry 的日志数据模型发出日志。

现在让我们看一个将日志与跟踪相关联的实际示例。

## 在简单的 Go 应用程序中如何添加上下文信息到日志？

我们在一个示例的 Golang 应用程序中实现了日志和跟踪的关联。

我们对 Go 应用程序进行了工具化，以生成按照此[文档](https://signoz.io/docs/instrumentation/golang/)描述的方式的跟踪。

我们将进一步检查如何在日志中添加上下文信息。我们使用 zap 库进行日志记录。

为了在日志中添加跟踪上下文信息，如 traceID、spanID 和 traceFlags，我们实现了一个记录 zap 日志消息的日志包装器，将其记录为现有跟踪上的事件。必须将跟踪上下文作为第一个参数传递给日志包装器。如果上下文不包含跟踪上下文，则不会向日志添加任何内容。

**步骤1**：我们进行 zap 日志记录器的初始设置。

```go
type LoggerWithCtx struct {
    *zap.Logger
    context *context.Context
}

func Ctx(ctx context.Context) *LoggerWithCtx {
    return &LoggerWithCtx{
        Logger:  logger,
        context: &ctx,
    }
}

func (l *LoggerWithCtx) logFields(
    ctx context.Context, fields []zap.Field,
) []zap.Field {
    span := trace.SpanFromContext(ctx)
    if span.IsRecording() {
        context := span.SpanContext()
        spanField := zap.String("span_id", context.SpanID().String())
        traceField := zap.String("trace_id", context.TraceID().String())
        traceFlags := zap.Int("trace_flags", int(context.TraceFlags()))
        fields = append(fields, []zap.Field{spanField, traceField, traceFlags}...)
    }

    return fields
}

func (log *LoggerWithCtx) Info(msg string, fields ...zap.Field) {
    fieldsWithTraceCtx := log.logFields(*log.context, fields)
    log.Logger.Info(msg, fieldsWithTraceCtx...)
}
```

**步骤2**：其次，我们封装 zap 日志记录器和上下文以添加日志消息中的跟踪上下文信息。

```go
type LoggerWithCtx struct {
    *zap.Logger
    context *context.Context
}

func Ctx(ctx context.Context) *LoggerWithCtx {
    return &LoggerWithCtx{
        Logger:  logger,
        context: &ctx,
    }
}

func (l *LoggerWithCtx) logFields(
```

```go
func logFields(ctx context.Context, fields []zap.Field) []zap.Field {
    span := trace.SpanFromContext(ctx)

    if span.IsRecording() {
        context := span.SpanContext()
        spanField := zap.String("span_id", context.SpanID().String())
        traceField := zap.String("trace_id", context.TraceID().String())
        traceFlags := zap.Int("trace_flags", int(context.TraceFlags()))
        fields = append(fields, []zap.Field{spanField, traceField, traceFlags}...)
    }

    return fields
}

func (log *LoggerWithCtx) Info(msg string, fields ...zap.Field) {
    fieldsWithTraceCtx := log.logFields(*log.context, fields)
    log.Logger.Info(msg, fieldsWithTraceCtx...)
}
```

**步骤3：** 打算使用此日志方法的服务需要传递请求上下文对象，该对象将 trace_id、span_id 和 trace_flags 字段添加到结构化日志消息中。此选项仅适用于不支持 OTLP 的后端，并且而是解析日志消息以提取结构化信息。

```go
import log "github.com/vabira200/golang-instrumentation/logger"

log.Ctx(r.Context()).Info("Order controller called", metadata...)
```

**步骤4：** 在将包装器与 zap 库集成后，这是我们的日志外观（带有 traceid、spanid 和 traceflags）。这遵循 OpenTelemetry 的[日志数据模型](https://opentelemetry.io/docs/specs/otel/logs/data-model/)。为了比较，让我们看看集成包装器之前和之后的日志。

在集成之前：

```json
{
    "hostname": "baschidbs02-1-p.broadsoft.ims.comcast.net",    
    "level": "info",    
    "line": "order/order.go:48",    
    "requestId": "42b2b58d-e9bb-482a-89cf-3a8ab3e3d027",    
    "requestMethod": "POST",    
    "message": "Successfully completed order request",    
    "time":"2022-12-26T21:33:45",    
    "requestPath": "/orders",    
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",    
    "userId": "4538"
}
```

集成后：

```json
{

    "hostname": "baschidbs02-1-p.broadsoft.ims.comcast.net",    
    "level": "info",    
    "line": "order/order.go:48",    
    "requestId": "42b2b58d-e9bb-482a-89cf-3a8ab3e3d027",    
    "requestMethod": "POST",    
    "message": "Successfully completed order request",    
    "time":"2022-12-26T21:33:45",    
    "requestPath": "/orders",    
    "spanid": "da0bace5360a7303",    
    "traceid": "26a4a41da8170e6ee2bde8222056641b",    
    "traceflags": 1,    
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",    
    "userId": "4538"    
}
```


## 使用 SigNoz 进行 OpenTelemetry 日志收集

在此示例中，我们将配置我们的应用程序将日志写入日志文件。然后，SigNoz OpenTelemetry 收集器从日志文件中收集日志，并将其导出到 `clickhouselogsexporter`，从而在 SigNoz UI 中显示日志。

![](https://signoz.io/img/blog/2023/01/microservices-logging-signoz-working.webp)

*如何使用 SigNoz 收集和关联遥测信号。*

**使用 OpenTelemetry 收集应用程序日志的步骤**

克隆 SigNoz 的 GitHub 存储库：

```bash

git clone -b main https://github.com/SigNoz/signoz.git
cd signoz/deploy/
./install.sh
```

修改 `deploy/docker/clickhouse-setup` 目录中的 `docker-compose.yaml` 文件，通过为应用程序日志文件添加卷来进行修改。

```yaml
otel-collector:
    image: signoz/signoz-otel-collector:0.79.5
    command: ["--config=/etc/otel-collector-config.yaml"]
    user: root # required for reading docker container logs
    volumes:
      - ./otel-collector-config.yaml:/etc/otel-collector-config.yaml
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
      - /<path_to_application_log_file>/application.log:/tmp/application.log
```

在 `deploy/docker/clickhouse-setup` 中的 `otel-collector-config.yaml` 中添加 `filelog` 接收器。

```yaml
receivers:
  filelog:
    include: ["/tmp/application.log"]
    start_at: beginning
    operators:
      - type: json_parser
        timestamp:
          parse_from: attributes.time
          layout: '%Y-%m-%dT%H:%M:%S'
      - type: move
        from: attributes.message
        to: body
      - type: remove
        field: attributes.time
```

在这里，我们通过可用的 operator 收集日志，并使用 operator 将消息从属性移动到主体。您可以在[这里](https://signoz.io/docs/userguide/logs/#operators-for-parsing-and-manipulating-logs)阅读有关 operator 的更多信息。

有关 `filelog` 接收器的更多配置，请在[此处](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/filelogreceiver)查看。

接下来，我们将修改 `otel-collector-config.yaml` 中的 pipeline ，以包含我们上面创建的接收器。

```yaml
service:
....
 logs:
   receivers: [otlp, filelog]
   processors: [batch]
   exporters: [clickhouselogsexporter]
```

现在，我们可以重新启动 OTel collector 容器，以应用新更改并从应用程序日志文件中读取日志。如果查看跟踪选项卡，我们可以看到带有 traceID 和 span 的跟踪。

![](https://signoz.io/img/blog/2023/01/microservices-logging-trace.webp)

*在 SigNoz 中以火焰图形式可视化的跟踪数据。*

现在我们需要切换到日志选项卡，检查上述跟踪的相应日志。

![](https://signoz.io/img/blog/2023/01/microservices-logging-log.webp)

*SigNoz 仪表板中的日志选项卡。*

我们可以看到上述跟踪的完整日志，其中包含 traceid、spanid 和 traceflags。

![](https://signoz.io/img/blog/2023/01/microservices-logging-log-complete.webp)

*我们可以看到包含 traceID、spanID 和 traceflags 的完整日志信息。*

## 结论

在大规模处理日志的过程中是一项困难的任务。微服务架构每分钟会产生数百万条日志记录。对日志记录采用结构化方法，为软件系统添加可观察性，并使开发人员能够轻松分析和从日志数据中获取见解是确保应用程序高性能的关键。

拥有一个具有集中式日志记录的唯一日志模型确保所有开发人员在其日志消息中使用相同的字段。此外，通过使用诸如 traceID 之类的上下文信息增强日志，我们可以更好地将其与其他遥测信号关联起来。

当您的代码放弃您时，日志成为您最好的朋友！

## 相关文章

- [为什么需要微服务中的分布式跟踪？](https://signoz.io/blog/distributed-tracing-in-microservices/)
- [分布式跟踪中的上下文传播](https://signoz.io/blog/context-propagation-in-distributed-tracing/)
