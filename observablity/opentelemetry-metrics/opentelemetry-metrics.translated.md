## 目录

[什么是 OpenTelemetry 指标？](#什么是-opentelemetry-指标-)
[为什么 OpenTelemetry 指标有用？](#为什么-opentelemetry-指标-有用-)
[OpenTelemetry 指标主要概念](#opentelemetry-指标-主要概念)
[OpenTelemetry 中的指标类型 + 示例](#opentelemetry-中-的-指标类型-+-示例-)
[OpenTelemetry 指标仪器](#opentelemetry-指标-仪器)
[使用哪种仪器类型？](#使用哪种仪器类型-)
[要跟踪的不同 OpenTelemetry 指标](#要跟踪-的-不同-opentelemetry-指标)
[OpenTelemetry 指标示例](#opentelemetry-指标-示例)
[使用 OpenTelemetry 指标的最佳实践](#使用-opentelemetry-指标-的-最佳实践)
[如何开始使用 OpenTelemetry 指标和 Checkly](#如何开始使用-opentelemetry-指标-和-checkly)
[结论](#结论)

[什么是 OpenTelemetry 指标？](#什么是-opentelemetry-指标-)
OpenTelemetry (OTel) 指标是 OpenTelemetry 项目的一部分，该项目提供用于遥测数据收集的工具、API 和 SDK。这些指标捕获系统性能数据，例如请求延迟、错误率、资源使用情况和吞吐量。[OTel 旨在跨语言和平台标准化可观察性](https://www.checklyhq.com/blog/opentelemetry-observability/)，使遥测数据的使用和集成变得更加容易。

指标是 OpenTelemetry 的三个核心信号之一，另外两个是日志和跟踪。

要开始使用 OTel 指标，请熟悉您首选语言的 OpenTelemetry API 和 SDK。使用 API 对您的代码进行检测，以使用计数器、仪表和直方图创建和记录指标。设置 OpenTelemetry 收集器以收集和处理这些指标，然后将数据导出到 Prometheus 或 Grafana 等监控系统。使用社区提供的库并遵循 OTel 约定将确保您的指标一致且有用。

[为什么 OpenTelemetry 指标有用？](#为什么-opentelemetry-指标-有用-)
OpenTelemetry 指标在各种情况下都很有用。以下是一些了解其用处的关键点：

**性能监控**
跟踪系统性能指标，例如延迟和吞吐量。例如，监控 API 请求时间以识别缓慢的端点。使用 OTel 指标，您可以深入了解系统不同部分的性能，帮助您查明瓶颈。这允许您更有效地调整和优化您的基础设施和代码。

**错误检测**
识别和量化错误和故障。例如，测量错误率以快速发现和解决应用程序中的问题。使用 OTel，您可以根据这些指标设置警报，以便实时收到问题通知。这种主动方法可以显着减少停机时间并提高服务的可靠性。

**资源利用率**
监控资源使用情况，例如 CPU 和内存。示例：通过跟踪 CPU 使用率峰值来优化服务器性能。通过使用 OTel 指标，您可以将资源使用情况与应用程序性能和用户负载相关联。这有助于您做出有关扩展和资源分配的明智决策，确保基础设施的有效利用。

**与合成监控一致的可观察性**
如果您已经在使用[合成监控](https://www.checklyhq.com/blog/what-is-synthetic-monitoring/)，那么跨服务和平台标准化指标收集可能特别有用。例如，使用 OTel 从用不同语言编写的微服务收集一致的指标。这种一致性，通过合成监控增强，简化了来自不同系统的指标的集成，为您的整个架构提供了连贯的视图。

[OpenTelemetry 指标主要概念](#opentelemetry-指标-主要概念)
了解 OpenTelemetry 指标概念的基础知识有助于工程师收集和分析有关其应用程序性能的数据。这些知识使他们能够做出更明智的决策并改进其系统的运行方式。

[API](#api)
OpenTelemetry 指标的[API（应用程序编程接口）](https://www.ibm.com/topics/api) 为开发人员提供了一种方法来检测他们的代码并捕获各种指标。它提供了一组函数和方法，开发人员可以使用这些函数和方法在他们的应用程序中定义和记录指标。

[SDK](#sdk)
SDK（软件开发工具包）是实现 OpenTelemetry API 的工具和库的集合。它提供了将遥测检测集成到用不同编程语言（如 Java、Python、Go 等）编写的应用程序中所需的组件。

[格式](#格式)
OpenTelemetry defines a standard format for representing metric data. This format ensures consistency and interoperability between different telemetry systems and components. By adhering to this format, developers can easily exchange metric data across different parts of the application stack.

[Exporters](#exporters)
Exporters are responsible for sending the metric data collected by OpenTelemetry to external monitoring systems or storage backends. OpenTelemetry supports a variety of exporters, including exporters for popular monitoring platforms like Prometheus, Jaeger, and Grafana.

[Metric Types in OpenTelemetry + Examples](#metric-types-in-opentelemetry-+-examples)
OpenTelemetry provides various types of metrics to effectively monitor applications, providing insights into performance and behavior. Understanding these metrics is crucial for optimizing your monitoring strategy:

**Counters**
**Counters**
[Counters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html) are a simple metric that tracks the number of times something has happened. For example, you can use a counter to count the number of requests received by your application or the number of errors encountered. Due to its intention as a steadily growing number, counters only accept positive numbers.

```
const { MeterProvider, ConsoleMetricExporter, PeriodicExportingMetricReader } = require('@opentelemetry/sdk-metrics-base');
const { ConsoleLogger, LogLevel } = require('@opentelemetry/core');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');
// Set up MeterProvider and ConsoleMetricExporter
const meterProvider = new MeterProvider({
resource: new Resource({
[SemanticResourceAttributes.SERVICE_NAME]: 'my-service',
}),
});
const exporter = new ConsoleMetricExporter();
const reader = new PeriodicExportingMetricReader({
exporter,
exportIntervalMillis: 60000, // Export metrics every 60 seconds
});
meterProvider.addMetricReader(reader);
const meter = meterProvider.getMeter('my-meter');
// Create counters
const requestCounter = meter.createCounter('app_requests_total', {
description: 'Total number of requests received',
unit: '1',
});
const errorCounter = meter.createCounter('app_errors_total', {
description: 'Total number of errors encountered',
unit: '1',
});
// Simulate incrementing counters
function handleRequest(success) {
requestCounter.add(1);
if (!success) {
errorCounter.add(1);
}
}
// Simulate some requests
handleRequest(true);
handleRequest(false);
handleRequest(true);
// Metric export is handled automatically by the reader every 60 seconds
```
This code sets up OpenTelemetry to export metrics to the console every 60 seconds using the `PeriodicExportingMetricReader`. The `ConsoleMetricExporter` is used to print the metrics to the console. The counters `app_requests_total` and `app_errors_total` are used to track the number of requests and errors respectively. The `handleRequest` function simulates requests and increments the counters accordingly.

**Gauges**
**Gauges**
Gauges are a metric that represents a single numerical value that can go up or down. For example, you can use a gauge to track the current temperature or the current number of users logged into your application.

```
const { MeterProvider, ConsoleMetricExporter, PeriodicExportingMetricReader } = require('@opentelemetry/sdk-metrics-base');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');
// Set up MeterProvider and ConsoleMetricExporter
const meterProvider = new MeterProvider({
resource: new Resource({
[SemanticResourceAttributes.SERVICE_NAME]: 'my-service',
}),
});
const exporter = new ConsoleMetricExporter();
const reader = new PeriodicExportingMetricReader({
exporter,
exportIntervalMillis: 60000, // Export metrics every 60 seconds
});
meterProvider.addMetricReader(reader);
const meter = meterProvider.getMeter('my-meter');
// Variable to store the current number of users
let currentUsers = 0;
// Callback function to update the gauge
function getCurrentUsers() {
return currentUsers;
}
// Create gauge
const userGauge = meter.createObservableGauge('app_users_current', {
description: 'Current number of logged-in users',
unit: '1',
});
// Register the callback function with the gauge
userGauge.addCallback((observableResult) => {
observableResult.observe(getCurrentUsers());
});
// Simulate changes in the number of logged-in users
function userLogin() {
currentUsers += 1;
}
function userLogout() {
currentUsers -= 1;
}
// Simulate some user logins and logouts
userLogin();
userLogin();
userLogout();
// Metric export is handled automatically by the reader every 60 seconds
```
Here we set up an OpenTelemetry `MeterProvider` and use the `ConsoleMetricsExporter` to export metrics to the console. The `PeriodicExportingMetricReader` is used to export metrics every 60 seconds. The `userGauge` is used to track the current number of logged-in users. The `getCurrentUsers` function is used to retrieve the current number of users and the `userGauge.addCallback` function is used to register the `getCurrentUsers` function as a callback for the gauge. The `userLogin` and `userLogout` functions simulate user logins and logouts, respectively.
将指标输出到控制台。我们创建一个 Gauge 来跟踪当前登录应用程序的用户数量。`getCurrentUsers` 函数充当回调函数，用于提供当前登录用户的数量，并将其注册到 Gauge 中。

`userLogin` 和 `userLogout` 函数通过增加和减少 `currentUsers` 变量来模拟用户登录和注销。最后，指标被导出到控制台。在实际应用程序中，您需要配置一个合适的后端导出器并设置定期导出。

**直方图**
直方图是一种指标，它将一个值的范围划分为多个桶，并统计每个值落在每个桶中的次数。这对于理解值的分布很有用，例如响应时间或请求大小。

```
const { MeterProvider, ConsoleMetricExporter, PeriodicExportingMetricReader } = require('@opentelemetry/sdk-metrics-base');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');
// 设置 MeterProvider 和 ConsoleMetricExporter
const meterProvider = new MeterProvider({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'my-service',
  }),
});
const exporter = new ConsoleMetricExporter();
const reader = new PeriodicExportingMetricReader({
  exporter,
  exportIntervalMillis: 60000, // 每 60 秒导出一次指标
});
meterProvider.addMetricReader(reader);
const meter = meterProvider.getMeter('my-meter');
// 创建一个直方图
const responseTimeHistogram = meter.createHistogram('app_response_time', {
  description: '请求的响应时间',
  unit: 'ms',
});
// 模拟记录响应时间
function recordResponseTime(responseTime) {
  responseTimeHistogram.record(responseTime);
}
// 模拟一些响应时间
recordResponseTime(120.5);
recordResponseTime(85.3);
recordResponseTime(200.1);
recordResponseTime(95.0);
```
在此代码段中，我们创建一个直方图来跟踪以毫秒为单位的请求响应时间。

`recordResponseTime` 函数通过向直方图添加值来模拟记录响应时间。然后，我们通过使用各种值调用此函数来模拟一些响应时间。最后，指标被导出到控制台。在实际应用程序中，您需要配置一个合适的后端导出器并设置定期导出。

**摘要**
摘要类似于直方图，但它不是将值统计到桶中，而是计算观察到的值的总和、计数和分位数等信息。这对于理解值的分布和识别异常值很有用。from opentelemetry import metrics.

```
const { MeterProvider, ConsoleMetricExporter, PeriodicExportingMetricReader } = require('@opentelemetry/sdk-metrics-base');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');
const { ExplicitBucketHistogramAggregation } = require('@opentelemetry/sdk-metrics-base');
// 设置 MeterProvider 和 ConsoleMetricExporter
const meterProvider = new MeterProvider({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'my-service',
  }),
});
const exporter = new ConsoleMetricExporter();
const reader = new PeriodicExportingMetricReader({
  exporter,
  exportIntervalMillis: 60000, // 每 60 秒导出一次指标
});
meterProvider.addMetricReader(reader);
const meter = meterProvider.getMeter('my-meter');
// 创建一个摘要（在本例中为具有显式桶的直方图）
const responseTimeSummary = meter.createHistogram('app_response_time_summary', {
  description: '请求响应时间的摘要',
  unit: 'ms',
  aggregation: new ExplicitBucketHistogramAggregation([0, 50, 100, 200, 500]),
});
// 模拟记录响应时间
function recordResponseTime(responseTime) {
  responseTimeSummary.record(responseTime);
}
// 模拟一些响应时间
recordResponseTime(120.5);
recordResponseTime(85.3);
recordResponseTime(200.1);
recordResponseTime(95.0);
recordResponseTime(150.0);
recordResponseTime(180.0);
```
在此代码段中，我们创建一个直方图来跟踪和汇总以毫秒为单位的请求响应时间。

`recordResponseTime` 函数通过向直方图添加值来模拟记录响应时间。然后，我们通过使用各种值调用此函数来模拟一些响应时间。

*注意*: OpenTelemetry API 没有像 Prometheus 那样直接提供“摘要”指标类型。但是，具有显式桶配置的直方图可以实现类似的汇总效果，包括计算总和、计数，并提供对分布的洞察。
除了这些之外，这里还有一些其他的 OTel 指标：
**CounterObserver:** 与 Counter 类似，CounterObserver 也会统计事件发生的次数，但它允许您为每个事件附加额外的信息。这对于跟踪诸如请求大小或错误严重程度等内容非常有用。**UpDownCounter:** UpDownCounter 类似于 Counter，但它可以增加或减少其值。这对于跟踪诸如服务器的活动连接数或应用程序使用的内存量等内容非常有用。**UpDownCounterObserver:** 与 UpDownCounter 类似，UpDownCounterObserver 可以增加或减少其值，并允许您为每个事件附加额外的信息。这对于跟踪资源使用情况随时间的变化非常有用。**GaugeObserver:** 与 Gauge 类似，GaugeObserver 表示单个数值，但它允许您为每个值附加额外的信息。这对于跟踪诸如数据库大小或网络请求延迟等内容非常有用。

[OpenTelemetry 指标仪器](#opentelemetry-指标仪器)
OpenTelemetry 提供了几种类型的仪器，用于在应用程序中捕获和记录指标数据。这些仪器具有不同的用途，适合各种用例：

**时间序列:** 时间序列仪器跟踪指标值随时间的演变。它们对于监控应用程序行为的趋势和模式非常有用。时间序列指标的示例包括[CPU 使用率](https://www.lifewire.com/what-is-cpu-usage-5218575)、内存消耗和请求延迟。**累加:** 累加仪器通过将新的数据点添加到现有总数来累积指标值。它们非常适合测量累积量，例如处理的请求总数或传输的数据总量。**同步:** 同步仪器在应用程序代码中被调用时立即记录指标数据。它们提供对应用程序性能的实时可见性，但由于数据收集的同步性质，可能会引入开销。**异步:** 异步仪器将指标数据的记录推迟到单独的线程或进程，允许主应用程序逻辑在不等待指标收集完成的情况下继续执行。这种方法最大程度地减少了性能影响，但可能会导致指标报告略有延迟。

[使用哪种仪器类型？](#使用哪种仪器类型-)
选择正确的仪器类型取决于应用程序的具体要求和特性。下表概述了一些考虑因素，以帮助您做出决定：

仪器类型 | 用例 | 优点 | 缺点 |
---|---|---|---|
时间序列 | 监控随时间的趋势和模式 | 实时可见性，适合持续监控 | 可能会需要大量的存储空间来保留长期数据 |
累加 | 跟踪累积量 | 值的简单累加，易于解释 | 可能无法提供对短期波动的详细见解 |
同步 | 实时指标收集 | 对应用程序性能的即时反馈 | 由于同步数据收集，可能会产生性能开销 |
异步 | 非阻塞指标记录 | 对应用程序性能的影响最小，可以处理数据突发 | 可能会导致指标报告略有延迟 |

通过考虑诸如指标更新频率、实时可见性的重要性以及性能和准确性之间的权衡等因素，您可以确定最适合您的监控需求的仪器类型。

[不同的 OpenTelemetry 指标跟踪](#不同的 OpenTelemetry 指标跟踪)
现在，让我们探索您可以使用 OpenTelemetry 跟踪的不同类型的指标。

[HTTP 响应时间](#http-响应时间)
[HTTP 响应时间](https://www.ibm.com/docs/en/itcam-transactions/7.4.0?topic=time-about-web-response) 测量从向服务器发送请求到收到响应之间的时间。它对于评估 Web 应用程序的性能以及检测可能影响用户体验的任何异常至关重要。

[错误率](#错误率)
错误率表示应用程序中发生的错误频率。监控错误率有助于识别错误、错误配置或可能影响可靠性和用户满意度的其他问题。

[吞吐量](#吞吐量)
吞吐量衡量应用程序在给定时间范围内处理请求或事务的速率。它对于确保系统能够有效地处理预期工作负载至关重要。

[网络延迟](#网络延迟)
网络延迟是指数据在网络上从一个点到另一个点传输所需的时间。高网络延迟会导致组件之间通信延迟，影响整体系统性能。

[数据库查询](#数据库查询)
## 数据库查询指标跟踪数据库操作的性能，包括执行时间、吞吐量和错误率。监控这些指标有助于优化数据库性能并识别潜在的瓶颈。

### 内存利用率

内存利用率指标提供了有关应用程序如何有效地使用可用内存资源的见解。监控内存使用情况有助于防止内存泄漏并优化资源分配。

### CPU 使用率

CPU 使用率指标指示应用程序消耗的 CPU 容量百分比。监控 CPU 使用率有助于识别性能瓶颈并优化资源分配以提高效率。

### OpenTelemetry 指标示例

现在，让我们深入了解一些 OpenTelemetry 指标的实际示例，以演示它们的实现。

### 电子邮件数量

```
const { MeterProvider } = require('@opentelemetry/sdk-metrics-base');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');
// 设置 MeterProvider
const meterProvider = new MeterProvider({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'my-service',
  }),
});
const meter = meterProvider.getMeter('my-meter');
// 创建一个计数器指标来跟踪发送的电子邮件数量
const emailsSentMetric = meter.createCounter('emails_sent', {
  description: '发送的电子邮件数量',
});
// 发送电子邮件并增加计数器的函数
function sendEmail() {
  // 发送电子邮件的代码...
  emailsSentMetric.add(1);
}
// 模拟发送一些电子邮件
sendEmail();
sendEmail();
sendEmail();
```

在这个例子中，我们使用一个计数器指标来跟踪我们的应用程序发送的电子邮件数量。我们将 `emailsSentMetric` 初始化为一个计数器指标，每次调用 `sendEmail()` 函数时，我们使用 `.add()` 方法将计数器增加 1。这使我们能够监控一段时间内发送的电子邮件数量。

### 操作延迟

```
const { MeterProvider } = require('@opentelemetry/sdk-metrics-base');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');
// 设置 MeterProvider
const meterProvider = new MeterProvider({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'my-service',
  }),
});
const meter = meterProvider.getMeter('my-meter');
// 创建一个直方图指标来衡量操作延迟
const operationLatencyMetric = meter.createHistogram('operation_latency_seconds', {
  description: '操作的延迟（以秒为单位）',
});
// 测量操作的延迟
function performOperation() {
  const startTime = Date.now();
  // 操作代码...
  const endTime = Date.now();
  const latency = (endTime - startTime) / 1000; // 转换为秒
  operationLatencyMetric.record(latency);
}
// 模拟执行操作
performOperation();
```

在这里，我们创建一个 [直方图指标](https://medium.com/mercari-engineering/have-you-been-using-histogram-metrics-correctly-730c9547a7a9) 来衡量我们应用程序中操作的延迟。`performOperation()` 函数通过测量执行操作之前和之后的时间来计算操作的持续时间。然后，使用 `record()` 方法将生成的延迟记录在 `operationLatencyMetric` 直方图中。这使我们能够分析一段时间内操作延迟的分布。

### 缓存命中率

```
const { MeterProvider } = require('@opentelemetry/sdk-metrics-base');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');
// 设置 MeterProvider
const meterProvider = new MeterProvider({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'my-service',
  }),
});
const meter = meterProvider.getMeter('my-meter');
// 创建一个仪表指标来跟踪缓存命中率
let cacheHitRateMetric = 0;
const cacheHitRateGauge = meter.createObservableGauge('cache_hit_rate', {
  description: '缓存命中率',
});
// 向仪表注册回调
cacheHitRateGauge.addCallback((observableResult) => {
  observableResult.observe(cacheHitRateMetric);
});
// 计算缓存命中率的函数
function calculateCacheHitRate(cacheHits, cacheMisses) {
  const totalRequests = cacheHits + cacheMisses;
  if (totalRequests > 0) {
    const hitRate = cacheHits / totalRequests;
    cacheHitRateMetric = hitRate;
  }
}
// 示例用法
calculateCacheHitRate(80, 20);
```

此示例演示了如何使用仪表指标来跟踪应用程序缓存系统的缓存命中率。`calculateCacheHitRate()` 函数根据缓存命中和未命中次数计算命中率，然后使用 `observe()` 方法相应地设置 `cacheHitRateMetric` 仪表的值。
方法。这使我们能够随着时间的推移监控缓存策略的有效性。

[错误率](#error-rate)
```
const { MeterProvider } = require('@opentelemetry/sdk-metrics-base');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');
// Set up the MeterProvider
const meterProvider = new MeterProvider({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'my-service',
  }),
});
const meter = meterProvider.getMeter('my-meter');
// Create a counter metric to track the number of errors
const errorRateMetric = meter.createCounter('error_rate', {
  description: 'The rate of errors',
});
// Function to handle an error and increment the counter
function handleError() {
  // Code to handle error...
  errorRateMetric.add(1);
}
// Simulate handling some errors
handleError();
handleError();
handleError();
```
在这个例子中，我们使用一个计数器指标来跟踪应用程序的错误率。`handleError()`
函数在发生错误时被调用，它使用 `add()` 方法将 `errorRateMetric`
计数器增加 1。这使我们能够监控错误的频率并识别任何模式或趋势。

[使用 OpenTelemetry 指标的最佳实践](#best-practices-for-using-opentelemetry-metrics)
了解和实施使用 OpenTelemetry 指标的最佳实践对于有效监控应用程序的性能至关重要。通过遵循这些指南，您可以确保您的指标准确反映系统行为，并提供有关优化和改进领域的宝贵见解。

**1. 一致的命名约定**
为您的指标使用清晰一致的命名约定。名称应具有描述性并遵循标准格式，例如 component_metric_type（例如，http_server_requests_total）。

一致的命名有助于轻松识别和理解不同服务和组件中的指标。

**2. 优化标签和属性**
标签和属性为指标提供了重要的上下文，使它们更具信息量。但是，过多的标签会使分析复杂化并增加存储需求。选择能够添加有意义的差异化而不会压倒数据集的标签。

明智地使用属性可以提高指标的实用性。例如，在登录尝试计数器中添加用户角色标签，可以详细分析登录模式，帮助进行安全监控和用户行为洞察。

**3. 使用聚合和摘要**
利用直方图、摘要和其他聚合技术来捕获和分析指标的分布。这种方法通过显示不仅是平均值，而是值的整个范围和频率，提供了对应用程序性能的更全面视图。

聚合有助于识别可能在简单平均值中被忽略的异常值和趋势。例如，直方图可以揭示某些事务中的延迟峰值，帮助您查明特定问题并相应地优化性能。

**4. 定期审查和更新指标**
持续审查和更新您的指标，以确保它们保持相关性和有用性。随着应用程序的发展，某些指标可能会变得过时，而新的指标可能需要监控新功能或组件。

定期审核您的指标将帮助您淘汰过时的指标并引入与当前业务目标和技术要求一致的新指标。这种做法确保您的监控策略适应变化，并在性能跟踪和故障排除中提供持续价值。

[如何开始使用 OpenTelemetry 指标和 Checkly](#how-to-get-started-with-opentelemetry-metrics-and-checkly)
凭借我们合成监控产品核心中的“监控即代码”，我们使客户能够通过设置监控检查来模拟用户行为。现在，我们正在与 OpenTelemetry 集成，以将合成检查与后端跟踪相关联，并查明检查失败的原因。

**增加信号与噪声比**
通过将合成检查与跟踪数据相关联，您可以过滤掉不必要的信息，并专注于最关键的数据点。这确保了开发和运营团队都可以专注于直接影响关键业务流程的遥测数据，从而减少噪声并提高整体效率。
我们正在开始与 **跟踪** 的 OTel 集成，目前处于测试阶段。此更新提供了两个主要优势：更轻松的跟踪错误关联 **和** 更简单的跟踪设置。配置完成后，每次检查运行都会立即提供端到端跟踪的视图，从前端或 API 端点到后端。这种端到端可见性有助于您快速查明检查运行失败的根本原因。

**它是如何工作的？**
- 通过一键操作，在所有 HTTP 请求上启用跟踪检测。
- 使用相关的 OpenTelemetry (OTel) SDK 检测您的代码。
- 仅将由 Checkly 检查“触发”的跟踪发送到我们的后端，并在您的检查结果中获取结果，甚至在编辑器中实时获取结果。这也适用于由我们的 CLI 触发的测试会话。
以下是一个快速演示，以便您更好地了解集成：

在我们的文档中查找更多信息：

[使用 OpenTelemetry SDK 检测您的代码](https://www.checklyhq.com/docs/open-telemetry/instrumenting-code/)[使用 OpenTelemetry 收集器将跟踪导入 Checkly](https://www.checklyhq.com/docs/open-telemetry/ingesting-traces-otel-collector/)[将跟踪发送到第三方服务](https://www.checklyhq.com/docs/open-telemetry/exporting-traces/)- 如果您是 Coralogix 用户，请查看我们的
[Coralogix 集成](https://www.checklyhq.com/docs/integrations/coralogix/)
通过开始使用我们的 OTel 集成，您可以利用 OpenTelemetry 指标与 Checkly 的强大功能，更深入地了解应用程序的性能和行为。

[结论](#conclusion)
OpenTelemetry 指标提供了一种标准化且灵活的方式来收集、聚合和导出来自您的应用程序和服务的指标数据。通过使用 OpenTelemetry 指标检测您的代码，您可以深入了解系统的性能和行为，从而能够识别问题、优化性能并提供更好的用户体验。借助 Checkly 的 OpenTelemetry 集成，开始使用指标监控比以往更容易，让您能够专注于构建和交付出色的软件。

[免费试用 Checkly](https://auth.checklyhq.com/login?state=hKFo2SBYcFUwdWlRRjB6V3FuYnA0ZmFXX1RxR0ltTVp6LWZuX6FupWxvZ2luo3RpZNkgM2xSODdOcngteWN5QTd0aGE3RDgxNWNhaElRV3RlajWjY2lk2SB4ZzZJTWFKWGY2UDNJWVBvT1pHOEd0cDZNWXZhSlBlVQ&client=xg6IMaJXf6P3IYPoOZG8Gtp6MYvaJPeU&protocol=oauth2&prompt=select_account&audience=https%3A%2F%2Fapi.checklyhq.com&redirect_uri=https%3A%2F%2Fapp.checklyhq.com&scope=openid%20profile%20email&response_type=code&response_mode=query&nonce=X2E1bHNmSEFVQ21ia1NYLmNqZHVEZHdvMURIMX5QQV9NeWZHV1ExcXllQg%3D%3D&code_challenge=qveQZXM7yuPc33CGiwNdykzFwzVYQ2l92JCKbVKxMEQ&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtc3BhLWpzIiwidmVyc2lvbiI6IjEuMjIuMyJ9) 或 [安排定制演示](https://calendly.com/d/5gk-49g-f76/checkly-demo?month=2024-05)。