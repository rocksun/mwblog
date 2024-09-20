
<!--
title: 使用 OpenTelemetry 对 React 应用程序进行仪器化
cover: https://cdn.thenewstack.io/media/2024/09/186602e7-embrace-react-opentelemetry-featured-image.jpg
-->

了解如何在 React 应用程序中使用 OpenTelemetry，包括基本和自动仪器，以及添加自定义跨度和指标。

> 译自 [Instrumenting a React App Using OpenTelemetry](https://thenewstack.io/instrumenting-a-react-app-using-opentelemetry/)，作者 Joaquín Díaz。

[OpenTelemetry](https://opentelemetry.io/) (OTel) 是一款开源可观测性框架，旨在捕获和导出应用程序的遥测数据，以了解其内部状态。它生成可在各种与 [OTel](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide) 兼容的可观测性系统中分析的信号。收集的三种基本数据类型是跟踪、指标和日志。

- [**跟踪**](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app/)描述操作如何在您的分布式服务中端到端地进行。它们由[跨度](https://thenewstack.io/spans-what-are-they-and-why-should-mobile-engineers-care)组成，每个跨度记录每个进程所花费的时间。跨度可以具有属性和事件。
- **指标**衡量您的系统在一段时间内的可用性和性能。
- **日志**是带时间戳的文本记录，可以是结构化的或非结构化的，并包含元数据。

## 为什么您应该关心？

构建 Web 应用程序令人兴奋，但如果用户没有与您的新功能互动，或者应用程序的构建方式使得他们无法与您的功能互动，那么这一切都是徒劳的。无论您是旨在提供最佳用户体验还是评估新更改的影响，您通常都需要回答以下常见问题：

- 此页面加载需要多长时间？
- 有多少用户成功点击了此按钮？
- 用户在哪里流失？

跟踪和衡量此信息对于了解您的产品为何有效或无效至关重要。

从小型初创公司到大型企业，许多公司都提供针对此问题的生产就绪解决方案，为开发人员提供工具来监控他们的应用程序并通过仪表板和图表轻松分析收集的数据。

## 那么，为什么您应该关心 OpenTelemetry？

### 全栈可观测性

即使您的用户只与您的客户端应用程序交互，他们的体验不仅取决于您的网站是否正常运行，还取决于支持每个操作的底层服务。页面加载缓慢可能有多种原因，例如大型 [JavaScript](https://thenewstack.io/javascript/) 包、繁忙的服务器或编写不当的查询。

大多数工具允许通过 API 或直接导出用户数据到数据库或数据湖。但是，这意味着您或您的后端团队需要将该数据（以其特定格式）集成到您的管道中，然后才能将其与堆栈的其余部分相关联。通过使用 OpenTelemetry 标准，您可以让公司中的每个人都与您的客户端指标集成，利用 Tempo、Loki 和 Prometheus 等现有工具，并端到端地分析用户数据。

### 避免供应商锁定

OpenTelemetry 与供应商和工具无关，并为系统提供了一种相互通信的通用语言。有多种免费和商业解决方案可用于收集和查看您的数据，因此您可以选择最适合您业务需求的解决方案。如果某个工具无法正常工作，您可以切换到另一个工具，而无需更改应用程序的监控方式。

您可以自己运行所有内容，标准和协议由社区驱动。

### 自动监控

随着 OpenTelemetry 成为社区标准，越来越多的工具和框架正在被监控，以便在进行最少的代码更改的情况下开箱即用。

## 监控 React 应用程序

我已经监控了一个与 [Go](https://thenewstack.io/go/) API 和 [PostgreSQL](https://roadmap.sh/postgresql-dba) 数据库通信的小型应用程序。堆栈的每个部分都会发出遥测数据——其中大部分是自动监控的；我将在后面介绍 Web 自动监控。

让我们开始吧。如果您想直接深入代码，请随时查看 [GitHub 存储库](https://github.com/embrace-io/react-otel-sample)。

首先，您需要一个地方来发送和查看您的数据。这通常从 [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) 开始，它接收数据并将其转发到各种后端，例如 Prometheus 或 Tempo。幸运的是，[Grafana](https://thenewstack.io/can-grafana-adaptive-metrics-help-slash-observability-costs) 在一个名为 [grafana/otel-lgtm](https://grafana.com/blog/2024/03/13/an-opentelemetry-backend-in-a-docker-image-introducing-grafana/otel-lgtm/) 的 [Docker](https://www.docker.com/?utm_content=inline+mention) 镜像中提供了一个 OTel 就绪的后端，该镜像运行收集器以及 Loki、Grafana、Tempo 和 Mimir 来收集和查看所有数据。

### 设置基本监控

要开始与收集器通信，请先安装必要的库。要向您的应用程序添加跟踪和指标，请包含 [@opentelemetry/api](https://www.npmjs.com/package/@opentelemetry/api)、[@opentelemetry/sdk-metrics](https://www.npmjs.com/package/@opentelemetry/sdk-metrics) 和 [@opentelemetry/sdk-trace-web](https://www.npmjs.com/package/@opentelemetry/sdk-trace-web)。此外，[@opentelemetry/exporter-metrics-otlp-http](https://www.npmjs.com/package/@opentelemetry/exporter-metrics-otlp-http) 和 [@opentelemetry/exporter-metrics-otlp-http](https://www.npmjs.com/package/@opentelemetry/exporter-metrics-otlp-http) 是通过 HTTP 将数据发送到导出器所需的。

```
npm install --save @opentelemetry/api @opentelemetry/sdk-metrics @opentelemetry/sdk-trace-web @opentelemetry/exporter-metrics-otlp-http @opentelemetry/exporter-trace-otlp-http
```

或

```
yarn add --save @opentelemetry/api @opentelemetry/sdk-metrics @opentelemetry/sdk-trace-web @opentelemetry/exporter-metrics-otlp-http @opentelemetry/exporter-trace-otlp-http
```

添加库后，您可以引入允许您对应用程序进行检测的组件。首先创建一个 [资源](https://opentelemetry.io/docs/languages/js/resources/)。资源表示生成遥测数据的实体 - 在这种情况下，是 React 应用程序。

```javascript
const resource = Resource.default().merge(
  new Resource({
    [SEMRESATTRS_SERVICE_NAME]: "react-client",
  }),
);
```

接下来，创建一个 [跟踪器提供程序](https://opentelemetry.io/docs/concepts/signals/traces/#tracer-provider)，这是创建跟踪器所必需的：

```javascript
const tracerProvider = new WebTracerProvider({
  resource: resource,
});
```

然后创建一个跨度导出器。在这里，我将使用 `OTLPTraceExporter`
，因为我通过 HTTP 发送跨度。确保您使用 OTel 收集器的正确 URL：

```javascript
const traceExporter = new OTLPTraceExporter({
  url: "<http://localhost:7070/v1/traces>",
  headers: {},
});
```

接下来，创建一个跨度处理器。使用 `SimpleSpanProcessor`
，跨度在结束后的立即发送：

```javascript
const spanProcessor = new SimpleSpanProcessor(traceExporter);
```

最后，通过将跨度处理器添加到跟踪器提供程序、注册它并将其设置为全局跟踪器提供程序，将所有内容绑定在一起。此设置允许您使用 OTel API 在应用程序中的任何位置获取跟踪器：

```javascript
tracerProvider.addSpanProcessor(spanProcessor);
tracerProvider.register();
trace.setGlobalTracerProvider(tracerProvider);
```

配置指标是一个类似的过程，因为导出任何 OTel 信号至少需要信号提供程序和信号导出器：

```javascript
const metricExporter = new OTLPMetricExporter({
  url: "<http://localhost:7070/v1/metrics>",
  headers: {},
});
 
// Like the SpanProcessor, the metric reader sends metrics to the exporter
const metricReader = new PeriodicExportingMetricReader({
  exporter: metricExporter,
  // Default is 60000ms (60 seconds). Set to 10 seconds for demonstration purposes.
  exportIntervalMillis: 10000,
});
 
const meterProvider = new MeterProvider({
  resource: resource,
  readers: [metricReader],
});
  
metrics.setGlobalMeterProvider(meterProvider);
```

您可以在 [GitHub 存储库](https://github.com/embrace-io/react-otel-sample/blob/main/frontend/src/otel.ts) 中找到完整的文件。
在应用程序启动时运行所有这些代码，您就可以开始对网站进行检测了。

### 配置自动检测

一些软件包开箱即用地提供有用的信息的自动检测。值得注意的是，如果您使用其中一个软件包，但您的应用程序没有集成以发送任何遥测数据，则操作将保持 NoOp - 也就是说，如果您不使用 OTel，它们不会增加任何开销。

对于此演示应用程序，添加 [@opentelemetry/instrumentation-fetch](https://www.npmjs.com/package/@opentelemetry/instrumentation-fetch) 和 [@opentelemetry/instrumentation-document-load](https://www.npmjs.com/package/@opentelemetry/instrumentation-document-load)：

```
npm install --save @opentelemetry/instrumentation-fetch @opentelemetry/instrumentation-document-load
```

或

```
yarn add --save @opentelemetry/instrumentation-fetch @opentelemetry/instrumentation-document-load
```

然后，尽早将此配置添加到应用程序生命周期中 - 理想情况下，甚至在 React 启动之前：

```javascript
registerInstrumentations({
  instrumentations: [
    new FetchInstrumentation({
      propagateTraceHeaderCorsUrls: [
        new RegExp(/http:\\/\\/localhost:8080\\/.*/),
      ],
    }),
    new DocumentLoadInstrumentation(),
  ],
});
```

`FetchInstrumentation` 和 `DocumentLoadInstrumentation`
都提供不同的配置。设置 `propagateTraceHeaderCorsUrls` 至关重要，它将 `Traceparent` 标头添加到使用 Fetch 进行的每个请求中。该标头允许请求将父跨度的上下文传播到其他服务，您可以在 [OpenTelemetry 文档](https://opentelemetry.io/docs/languages/js/propagation/) 中了解更多信息。您还可以在下一节中看到它的实际应用。

### 添加跨度和指标

现在让我们看看所有内容是如何整合在一起的。每个使用 Fetch 方法发出的请求都会创建一个跟踪。通过在标头中传播上下文，这些跟踪将包含 API 创建的跨度作为子跨度。请注意以下内容，说明了如何将来自不同服务的跟踪联系在一起：

![](https://cdn.thenewstack.io/media/2024/09/36825a13-embrace-add-spans-and-metrics.png)

这种透明度是跨堆栈使用 OpenTelemetry 的主要优势。它可以改善跨服务的沟通和对问题的理解。虽然此示例很简单，但实际的 API 调用将涉及许多系统，并且还可能涉及多个子调用或查询。与您的后端团队开始对话时，说“您能查看一下导致此 API 调用变慢的查询吗？”比仅仅说“嘿，这个 API 调用很慢”更有效。

#### 添加自定义跟踪

要使用跟踪器创建跨度，请执行以下操作：

```typescript
const tracer = trace.getTracer("react-client");
const span = tracer.startSpan("Span Name");
```

您可以向此跨度添加属性、事件甚至子跨度，并将其传播到整个应用程序。
一种管理跨度的方法是使用 React 上下文来存储和传播跨度，使其贯穿组件树：

```typescript
const SpansProvider: FC<PropsWithChildren> = ({ children }) => {
  const spansRef = useRef<Map<SpanName, Span>>(new Map());
  const getOrCreateSpan = useCallback(
    (name: SpanName, options?: SpanOptions): [Span, boolean] => {
      if (spansRef.current.has(name)) {
        return [spansRef.current.get(name)!, false];
      }
      const tracer = trace.getTracer("react-client");
      const span = tracer.startSpan(name, options);
      spansRef.current.set(name, span);
      return [span, true];
    },
    [],
  );
  const endSpan = useCallback((name: SpanName) => {
    const span = spansRef.current.get(name);
    if (span) {
      span.end();
      spansRef.current.delete(name);
    }
  }, []);
  return (
    <SpansContext.Provider value={{ getOrCreateSpan, endSpan }}>
      {children}
    </SpansContext.Provider>
  );
};
export default SpansProvider;
```

稍后，您可以对用户流程进行检测：

```typescript
// Home.tsx...
const { getOrCreateSpan, endSpan } = useSpansContext();
const [purchaseFlowSpan, purchaseFlowSpanCreated] = getOrCreateSpan(
  "Purchase Flow",
);
useEffect(() => {
  if (purchaseFlowSpanCreated) {
    purchaseFlowSpan.addEvent("Home Page Visited");
    purchaseFlowSpan.setAttribute("user_id", 123);
  }
}, [purchaseFlowSpan, purchaseFlowSpanCreated]);
...
// ProductDetails.tsx...
const { getOrCreateSpan, endSpan } = useSpansContext();
const handleBuyClicked = useCallback(() => {
  const [activeSpan] = getOrCreateSpan("Purchase Flow");
  activeSpan.addEvent("Buy Button Clicked", { product_id: productId });
  activeSpan.setStatus({ code: SpanStatusCode.OK });
  endSpan("Purchase Flow");
}, [productId, getOrCreateSpan]);
```

此设置可以在 Tempo 中可视化：

![](https://cdn.thenewstack.io/media/2024/09/71a99e01-embrace-custom-trace.png)

您可以从这些跨度生成指标，以衡量页面完全加载（包括网络请求）所需的时间：

![](https://cdn.thenewstack.io/media/2024/09/eb5b6599-embrace-home-page-load-time-graph.png)

#### 添加自定义指标

要添加自定义指标，请获取一个仪表，然后从各种指标类型中进行选择，例如：

- **Counters**: 只能增加或重置值的指标。
- **Gauges**: 可以增加或减少值的指标。
- **Histograms**: 从桶值计算的复杂指标。

例如，要统计访问特定页面的用户数量，您可以创建一个新的钩子：

```typescript
const useTrackPageView = (
  pageName: string,
  extraAttributes: Attributes = {},
) => {
  useEffect(() => {
    const meter = metrics.getMeter("react-client");
    const counter = meter.createCounter("react_client_page_view", {
      description: "Number of views for a page",
      unit: "unit",
    });
    counter.add(1, {
      'react_client.page_name': pageName,
      ...extraAttributes,
    });
    // Ensure this runs only once
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
};
```

这可以在 Grafana 中的图表中可视化：

![](https://cdn.thenewstack.io/media/2024/09/7e70278f-embrace-page-views-graph.png)

## 使用 OpenTelemetry 与 React 的挑战

虽然 OpenTelemetry 最初是为后端应用程序设计的，但它可以适应前端使用。遥测标准化、语义约定和社区生态系统等核心概念对于前端可观察性非常有用，前端可观察性往往跨越许多系统。

挑战在于将这些概念适应前端可观察性，特别是对于 React，React 中的组件由于各种原因经常被挂载、卸载和重新渲染。跟踪用户交互（可以以多种不同的方式和顺序发生）比跟踪具有明确起点和终点的请求或计划作业更复杂。

目前，[Embrace](https://embrace.io/) 软件开发工具包 (SDK) 团队正在开发新的约定和标准，以更好地支持移动应用程序。大多数新增功能也适用于 Web 应用程序，因为它们旨在跟踪和衡量用户体验。更广泛的采用将推动社区贡献，帮助新开发人员开始对其代码进行检测。您会成为早期采用者并帮助 OpenTelemetry 成为前端世界的标准吗？

如果您想了解更多关于基于 OpenTelemetry 的移动可观察性，请查看 [我们的开源仓库](https://github.com/embrace-io?q=&type=public) 或 [加入我们的 Slack 社区](https://embraceio-community.slack.com/)。
