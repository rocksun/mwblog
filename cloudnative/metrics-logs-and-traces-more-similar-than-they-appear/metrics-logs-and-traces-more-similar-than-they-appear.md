# Metrics, Logs 和 Traces：比它们看起来更相似？

翻译自 [Metrics, Logs and Traces: More Similar Than They Appear?](https://thenewstack.io/metrics-logs-and-traces-more-similar-than-they-appear/) 。笔者团队也正在试图用统一框架处理 Metrics, Logs 和 Traces ，我们发现确实很有价值 。

它们需要不同的存储和查询方法，这使得使用单一解决方案成为一项挑战。但 InfluxDB 正在努力将它们整合为一个。

![](https://cdn.thenewstack.io/media/2023/04/0817260c-circuit-board-2-1024x512.jpg)

[时间序列数据](https://www.influxdata.com/what-is-time-series-data/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-04_spnsr-ctn_monitoring-logs_tns)具有独特的特征，使其与其他类型的数据区分开来。但即使在时间序列数据范围内，也有不同类型的数据需要不同的工作负载。Metrics, Traces 和 Logs 都是不同的，这使得设计一个可以处理所有三种数据类型的单一解决方案成为一项挑战。

虽然所有三种类型的数据结构通常相同，但每个工作负载的查询模式却不同。专门设计用于存储时间序列数据系统并不能完全处理这些不同的查询模式。我们可以在时间序列市场中看到这个挑战，在那里有针对 Metrics, Traces 和 Logs 的三类软件。

InfluxDB、Grafana、Prometheus 等解决方案可以收集、存储、分析和可视化度量衡数据。Jaeger 可用于端到端分布式跟踪，并且最近更新后 InfluxDB 也成为了一个可行选项。对于日志，常见解决方案是所谓 ELK 堆栈（ Elasticsearch ,  Logstash 和 Kibana ），但 Loki 等解决方案也能够处理日志。

日志是最具挑战性的时间序列数据类型，因此让我们深入探讨其中原因。

像 Loki 这样的解决方案也可以处理日志。

## 数据模型

如上所述，所有时间序列数据都可以使用相同的数据模型。InfluxDB 的行协议提供了一个有用的示例。

```
measurement,tag1=value,tag2=value field1=value,field2=value timestamp
```

在这里，measurement 就像表名一样，时间戳也是如此。标签和字段是键值对，其中标签作为元数据，而字段表示您想要收集、存储、分析和/或可视化的数据。

series 是 measurement 和标签值的唯一组合，因此您拥有的标签越多，则拥有的唯一系列就越多。我们称之为基数，在基数过高时会影响性能。这个问题对于所有基于日志结构合并树（LSM）的方法来说都很典型，而 LSM 是 measurement 系统常见解决方案。

## 解析日志数据

假设我们正在使用日志数据来调试应用程序。日志的原始输出可能如下所示：

```
"level=debug msg=\"Not resuming any session\" log.target=rustls::client::hs log.module_path=rustls::client::hs log.file=/usr/local/cargo/registry/src/github.com-1ecc6299db9ec823/rustls-0.20.8/src/client/hs.rs log.line=127 target=\"log\" time=1675710426464848718\n"
```

如果我们仔细观察，我们可以开始将这些数据解析为键值对，然后我们可以在我们的数据模型中使用这些键值对。

```
level=debug
log.target=rustls::client::hs
log.module_path=rustls::client::hs log.file=/usr/local/cargo/registry/src/github.com-1ecc6299db9ec823/rustls-0.20.8/src/client/hs.rs
log.line=127
target=\”log\”
msg=”Not resuming any session”
time=1675710426464848718
```

此时，我们可以开始决定哪些键应该是标签（元数据），哪些是字段。针对标签的查询使开发人员能够沿几乎任何维度对数据进行切片和切块。但是存在的标签越多，运行每个查询所需的资源就越多，最终会影响性能。

如果我们查看另一个日志文件，问题就会变得更加清晰。在这里，我们已经将日志文件解析为键值对。

```
level=debug
msg=\”Processing request\”
request=\”Request { method: GET, uri: http://10.144.148.50:8080/metrics, version: HTTP/2.0, headers: {\\\”user-agent\\\”: \\\”Prometheus/2.38.0\\\”, \\\”accept\\\”: \\\”application/openmetrics-text;version=1.0.0,application/openmetrics-text;version=0.0.1;q=0.75,text/plain;version=0.0.4;q=0.5,*/*;q=0.1\\\”, \\\”accept-encoding\\\”: \\\”gzip\\\”, \\\”x-prometheus-scrape-timeout-seconds\\\”: \\\”10\\\”, \\\”x-forwarded-proto\\\”: \\\”http\\\”, \\\”x-request-id\\\”: \\\”001052e8-d898-4b4b-9e21-0b0a4918970a\\\”}, body: Body(Streaming) }\”
target=\”ioxd_common::http\”
location=\”ioxd_common/src/http/mod.rs:121\”
time=1675710425927921595
```

如果我们比较这两个日志文件，我们会看到四个常见标记： `level` 、 `msg` 、 `target` 和 `time` 。还有几个独特的标签： `log.target` 、 `log.module_path` 、 `log.file` 、 `log.line `、 `request` 和 `location` 。因此，每个日志都是一个 series ，因为它包含唯一的标签组合。当我们考虑在调试应用程序时存在多少单独的日志时，很容易看出查询该数据变得多么复杂。

造成这种情况的一个因素是应用程序中属性的命名缺乏一致性。例如，如果您正在调试应用程序，每个进程可能需要不同的信息，因此开发人员自然会为该特定进程创建属性，每个属性都成为关键字值。将这种做法扩展到整个应用程序会产生数千个不同的关键字，因为每个进程都在做不同的事情。

更复杂的是，像“error”这样的属性可能具有 `e` 、 `error` 、 `err` 、 `err_code` 或开发人员可以想出的任何其他描述性排列的标记键。当然，理论上可以清理和标准化像错误这样的属性，但这也会产生大量工作，并且需要您了解每个排列以确保没有任何漏洞。

总之，日志不仅会产生大量的数据，还会产生大量独特的数据。这意味着数据库可能需要以不同于其他类型的时间序列数据的方式存储数据，并且查询模式必须考虑日志数据的形状。

## 比较 logs 和 traces

Traces 也会产生基数问题。但是，当我们考虑跟踪时，存在一些关键差异。

Trace 中的键总数往往更加一致。这是因为应用程序中的点数有限，并且这些过程的输出包含较少的程序员定义的元素。结果是更加结构化的输出。换句话说，标签键更有可能相同，例如 spanID ，但它们的值是无限的（例如，trace 和 span ID）。

无限制的标签值也有助于提高基数。然而，traces 和 logs 之间的主要区别在于 traces 更可能有一个无界元素（tag values），而 logs 有两个无界元素（tag keys 和 tag values）。相比之下，Metrics 倾向于同时具有有界标签键和标签值。这些组合中的每一个都需要不同的存储和查询方法，这就是为什么对所有三种数据类型使用单一解决方案如此具有挑战性。

幸运的是，地平线上有希望。 InfluxDB 长期以来一直很好地处理 metrics，但随着其新数据库核心 InfluxDB IOx 的发布，它现在可以在单个解决方案中管理高基数跟踪数据，以及指标和原始事件数据。随着 InfluxDB 背后的团队将目光投向 Logs，将三类时间序列应用程序整合为一类的努力仍在继续。