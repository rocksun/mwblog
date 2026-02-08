# 使用 OpenTelemetry 日志去重处理器减少日志量

作者：

**[Juraci Paixao Krohling](https://github.com/jpkrohling) (OllyGarden)**

|

2026年1月20日 星期二

![封面图片展示了日志去重概念](/blog/2026/log-deduplication-processor/cover.png)

您的日志中可能至少有80%是重复的噪音。连接重试、健康检查、心跳消息：相同的日志行每分钟重复数千次。您为每个日志支付存储费用，而有用的信号则淹没在噪音中。OpenTelemetry Collector 的日志去重处理器为这个问题提供了一个优雅的解决方案。

## 重复日志问题

现代分布式系统会生成海量的日志，但其中大部分日志的价值递减。考虑一个典型的微服务，当其下游依赖项不可用时会记录连接错误。如果该服务每100毫秒重试一次，持续30秒，那么对于单一事件就会产生300条几乎相同的日志条目。每个条目都会消耗您日志后端中的存储、网络带宽和处理能力。

健康检查端点使问题更加复杂。Kubernetes 探测、负载均衡器检查和监控系统都会定期生成日志条目。一个单一的服务每小时可能记录数千条健康检查响应，但除了“服务正在运行”之外，这些日志都没有提供有意义的洞察力。

OpenTelemetry Collector 中的 logdedupprocessor 通过在可配置的时间窗口内聚合相同的日志来解决这个问题。它不是转发每一个重复的条目，而是发出一份包含该消息出现次数的单一日志。

## 日志去重的工作原理

核心概念很简单。当日志共享相同的资源属性、范围、正文、属性、严重性和事件名称时，它们被认为是相同的。值得注意的是，时间戳被排除在此身份检查之外，因为它对每个日志条目自然会有所不同。属性的顺序不影响身份。处理器会计算这些字段的哈希值，并在可配置的时间间隔内跟踪其出现次数。

当间隔期满时，处理器会发出一份包含三个额外属性的单一日志条目：`log_count`（重复次数）、`first_observed_timestamp` 和 `last_observed_timestamp`。您无需存储每个相同的条目，即可全面了解频率模式。

这种方法与采样有着重要的区别。采样会永久丢弃数据。去重则保留了重要的信息（发生了什么、多久发生一次、何时发生），同时消除了冗余存储。

## 实用配置

以下是一个去重连接错误但保留审计日志的配置：

```
processors:
  logdedup:
    interval: 1s
    conditions:
      - severity_number >= SEVERITY_NUMBER_ERROR
      - attributes["log.type"] == "connection"
    exclude_fields:
      - attributes.request_id
      - attributes.timestamp

```

`conditions` 字段使用 OpenTelemetry 转换语言 (OTTL) 表达式来筛选哪些日志需要去重。不匹配的日志将保持不变地通过。在此示例中，只有带有 `log.type=connection` 属性的 ERROR 级别日志才会被考虑去重。

`exclude_fields` 选项从比较中移除了高基数字段。像请求 ID 和时间戳这样的字段即使在日志消息在语义上相同的情况下，也会在条目之间有所不同。通过排除它们，仅在这些易变字段上不同的日志将被视为重复。

## 一个完整的管道示例

要使用日志去重处理器，请将其包含在您的 Collector 管道中：

```
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317

processors:
  logdedup:
    interval: 1s
    conditions:
      - severity_number >= SEVERITY_NUMBER_ERROR
      - attributes["log.type"] == "connection"
    exclude_fields:
      - attributes.request_id
      - attributes.timestamp

exporters:
  otlp:
    endpoint: your-backend:4317

service:
  pipelines:
    logs:
      receivers: [otlp]
      processors: [logdedup]
      exporters: [otlp]

```

## 使用 telemetrygen 进行测试

要在本地测试此配置，请使用 telemetrygen 生成连接错误日志：

```
telemetrygen logs \
  --otlp-insecure \
  --logs 100 \
  --rate 10 \
  --severity-text ERROR \
  --severity-number 17 \
  --body "Connection refused: failed to connect to database at 10.0.0.5:5432" \
  --telemetry-attributes 'log.type="connection"' \
  --telemetry-attributes 'service.name="order-service"' \
  --telemetry-attributes 'db.system="postgresql"'

```

这将以每秒 10 条的速度生成 100 条日志，所有日志都具有 ERROR 严重性以及触发去重的 `log.type=connection` 属性。几秒钟后，您应该在后端看到几条带有 `log_count: N` 的日志条目，而不是 100 条单独的条目。

## 权衡与考量

日志去重处理器会引入与您的间隔设置相等的延迟。日志会被保留直到间隔期满才会被转发。对于大多数用例，1秒的延迟是可以接受的，但实时告警系统可能需要进行调整。

对于合规性要求高的日志，即每次出现都必须保留其原始时间戳的日志，请完全跳过去重。审计日志、安全事件和法规记录通常需要完全的准确性。

权衡很简单：以轻微的延迟和丢失单个时间戳为代价，实现存储减少和信号更清晰。对于大批量重复日志，这种权衡通常是值得的。

## 结论

日志去重处理器为现代日志管道中的噪音问题提供了一个实用的解决方案。通过聚合相同的条目并保留频率信息，您可以在不牺牲可观测性的前提下，显著降低存储成本并提高信号清晰度。

结合其他 OpenTelemetry Collector 处理器，例如过滤和采样，日志去重使您能够精细控制您的遥测管道。其结果是一个日志系统，能够捕获重要信息，同时丢弃噪音。