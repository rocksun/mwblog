
<!--
title: OpenTelemetry：Go可观测性指南
cover: https://www.lucavall.in/images/blog/opentelemetry-a-guide-to-observability-with-go/cover.webp
-->

现代应用程序通常是复杂的分布式系统。调试它们可不是一件有趣的事情：你必须跟踪跨服务的请求，日志会丢失，而且指标通常难以关联。这就像大海捞针——只不过这个草堆正在燃烧，而且针还在移动。这就是 OpenTelemetry (OTel) 可以提供帮助的地方。

> 译自 [OpenTelemetry: A Guide to Observability with Go | Blog](https://www.lucavall.in/blog/opentelemetry-a-guide-to-observability-with-go)，作者 Luca Cavallin。

现代应用程序通常是复杂的分布式系统。调试它们并不有趣：您必须跨服务跟踪请求，日志会丢失，并且指标通常难以关联。这就像大海捞针 - 除非干草堆着火了，而且针还在移动。这就是 [OpenTelemetry](https://opentelemetry.io) (OTel) 可以提供帮助的地方。

OpenTelemetry 是一个开源的可观测性框架，可帮助从应用程序收集和导出**追踪 (traces)**、**指标 (metrics)** 和**日志 (logs)**。它标准化了遥测数据的收集方式，并使其易于与 **Grafana** 等工具集成。借助 OpenTelemetry，我们终于可以清楚地了解应用程序的性能，从而可以回答诸如“为什么此请求很慢？”、“现在有多少个请求处于活动状态？”以及“发生了什么错误，以及在哪里？”之类的问题。

在这篇文章中，我将引导您了解如何在 Go 应用程序中集成 OpenTelemetry。到最后，您将拥有一个可重用的遥测包，该包可以设置日志记录、指标和追踪 - 所有这些都不会使您的应用程序代码混乱！我已在 GitHub 上发布了该软件包，其中包含完整的测试和示例：[gotel](https://github.com/lucavallin/gotel)。您可以随意将其用作您自己项目的起点。

## 首先要了解的几个重要概念

在深入研究代码之前，让我们分解 OpenTelemetry 的主要组成部分：日志、指标和追踪。这些是可观测性的构建块，它们可以帮助我们了解应用程序中发生的事情。

**提供者 (Providers)**、**资源 (resources)**、**导出器 (exporters)** 和 **收集器 (collectors)** 是协同工作以收集、处理遥测数据并将其发送到外部系统的组件。

### 日志、指标和追踪

日志、指标和追踪都是遥测数据类型，但它们用途不同。以下是每种类型的快速概述：

- **日志 (Logs)** 是离散事件的记录。将它们视为应用程序的日记条目。当出现问题时，日志是您首先要查看的地方。
- **指标 (Metrics)** 随时间跟踪数值数据，例如请求持续时间、CPU 使用率或活动连接数。它们有助于监控趋势并发现性能问题。
- **追踪 (Traces)** 跟踪请求在多个服务中的流动。一个追踪由多个 span 组成，每个 span 代表一个单独的操作。

基本上：日志告诉我们发生了什么，指标显示了它发生的频率，而追踪揭示了系统的不同部分是如何交互的。

### 提供者、资源、导出器和收集器

在 OpenTelemetry 中，提供者、资源、导出器和收集器协同工作以收集、处理遥测数据并将其发送到外部系统。提供者负责生成遥测数据，它们依赖于资源，资源**定义有关应用程序的元数据**，例如服务名称、版本和主机。收集遥测数据后，需要将其发送到某个地方，这就是导出器所做的事情。导出器**将数据转发**到像 Grafana 这样的可观测性后端。为了更有效地管理此过程，OpenTelemetry 使用收集器，收集器**充当中间人，在将遥测数据发送到一个或多个后端之前，对其进行聚合、处理和路由**。收集器有助于减少应用程序开销，并提供遥测存储和分析的灵活性。

## 在 Go 中设置遥测

现在，让我们构建一个 Go 包，该包使用 OpenTelemetry 处理日志、指标和追踪。该软件包名为 `gotel`，可在 GitHub 上找到：[gotel](https://github.com/lucavallin/gotel)。此软件包将 OpenTelemetry 的 SDK 包装到一个简单的接口中，使其更易于使用。

### 配置

首先，我们需要一种配置遥测系统的方法。`config.go` 文件通过从环境变量加载设置来处理此问题。这使得在不修改代码的情况下调整配置变得容易。

```go
package gotel

import (
	"fmt"

	"github.com/caarlos0/env"
)

// Config holds the configuration for the telemetry.
type Config struct {
	ServiceName    string `env:"SERVICE_NAME" envDefault:"gotel"`
	ServiceVersion string `env:"SERVICE_VERSION" envDefault:"0.0.1"`
	Enabled        bool   `env:"TELEMETRY_ENABLED" envDefault:"true"`
}

// NewConfigFromEnv creates a new telemetry config from the environment.
func NewConfigFromEnv() (Config, error) {
	telem := Config{}
	if err := env.Parse(&telem); err != nil {
		return Config{}, fmt.Errorf("failed to parse telemetry config: %w", err)
	}
	return telem, nil
}
```

此文件定义了一个 `Config` 结构，用于存储**服务名称 (service name)**、**版本 (version)** 以及用于启用或禁用遥测的标志。`NewConfigFromEnv` 函数从环境变量加载这些值，允许我们在不修改代码的情况下调整设置。如果未设置环境变量，则使用默认值。

### 提供者和导出器

现在我们已经配置好了配置，我们需要设置 **providers** - 负责处理日志、指标和追踪的组件。

`providers.go` 文件包含创建 logger、meter 和 tracer provider 的函数。这些函数用于在 `NewTelemetry` 中初始化遥测系统。`newResource` 函数也在这个文件中定义，用于将元数据附加到所有遥测数据，从而更容易追踪数据的来源。

```go
package gotel

import (
	"context"
	"fmt"
	"os"

	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploggrpc"
	"go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc"
	"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
	"go.opentelemetry.io/otel/sdk/log"
	"go.opentelemetry.io/otel/sdk/metric"
	"go.opentelemetry.io/otel/sdk/resource"
	"go.opentelemetry.io/otel/sdk/trace"
	semconv "go.opentelemetry.io/otel/semconv/v1.17.0"
)

// newLoggerProvider creates a new logger provider with the OTLP gRPC exporter.
func newLoggerProvider(ctx context.Context, res *resource.Resource) (*log.LoggerProvider, error) {
	exporter, err := otlploggrpc.New(ctx)
	if err != nil {
		return nil, fmt.Errorf("failed to create OTLP log exporter: %w", err)
	}
	processor := log.NewBatchProcessor(exporter)
	lp := log.NewLoggerProvider(
		log.WithProcessor(processor),
		log.WithResource(res),
	)
	return lp, nil
}

// newMeterProvider creates a new meter provider with the OTLP gRPC exporter.
func newMeterProvider(ctx context.Context, res *resource.Resource) (*metric.MeterProvider, error) {
	exporter, err := otlpmetricgrpc.New(ctx)
	if err != nil {
		return nil, fmt.Errorf("failed to create OTLP metric exporter: %w", err)
	}
	mp := metric.NewMeterProvider(
		metric.WithReader(metric.NewPeriodicReader(exporter)),
		metric.WithResource(res),
	)
	otel.SetMeterProvider(mp)
	return mp, nil
}

// newTracerProvider creates a new tracer provider with the OTLP gRPC exporter.
func newTracerProvider(ctx context.Context, res *resource.Resource) (*trace.TracerProvider, error) {
	exporter, err := otlptracegrpc.New(ctx)
	if err != nil {
		return nil, fmt.Errorf("failed to create OTLP trace exporter: %w", err)
	}
	// Create Resource
	tp := trace.NewTracerProvider(
		trace.WithBatcher(exporter),
		trace.WithResource(res),
	)
	otel.SetTracerProvider(tp)
	return tp, nil
}

// newResource creates a new OTEL resource with the service name and version.
func newResource(serviceName string, serviceVersion string) *resource.Resource {
	hostName, _ := os.Hostname()
	return resource.NewWithAttributes(
		semconv.SchemaURL,
		semconv.ServiceName(serviceName),
		semconv.ServiceVersion(serviceVersion),
		semconv.HostName(hostName),
	)
}
```

我们首先导入 OpenTelemetry 的 SDK 以及用于日志、指标和追踪的 exporter。这些 exporter **将数据发送到外部系统**，例如 Grafana 或其他兼容 OTLP 的后端。

`providers.go` 文件包含以下函数：

*   `newLoggerProvider`：创建一个 **logger provider**，它收集并导出日志。OTLP gRPC exporter 通过 gRPC 在网络上发送日志，而 `BatchProcessor` 在导出之前有效地批量处理日志条目。
*   `newMeterProvider`：创建一个 **metrics provider**，它负责收集 **metrics**。它定期将 metrics 导出到后端。
*   `newTracerProvider`：创建一个 **tracing provider** 来跟踪请求流并将它们导出到外部后端。
*   `newResource`：创建一个 **resource**，其中包含有关应用程序的元数据，例如服务名称、版本和主机名。此信息附加到所有遥测数据。

对于所有遥测数据，我使用 **OTLP gRPC exporter**，它是 OpenTelemetry 中默认且最常用的 exporter。OTLP（OpenTelemetry 协议）是一种标准化格式，用于在应用程序和可观测性后端之间传输日志、指标和追踪。它支持 gRPC 和 HTTP 传输，允许在高吞吐量环境中高效地发送数据。我选择 OTLP gRPC 是因为它提供低延迟、高性能的通信以及强大的流式传输支持，使其成为生产工作负载的理想选择。但是，OpenTelemetry 支持许多其他 exporter，具体取决于您的用例。

### 整合在一起

`Telemetry` 结构体将所有组件包装在一起。当我们想将遥测系统传递到应用程序的其他部分时，这很方便。例如，我们可以在中间件中使用 `Telemetry` 结构体来记录请求和测量请求持续时间。`telemetry.go` 文件包含 `Telemetry` 结构体和 `TelemetryProvider` 接口，该接口定义了 `Telemetry` 结构体实现的方法。`Telemetry` 结构体是 OpenTelemetry logger、meter 和 tracer 的包装器。

```go
package gotel

import (
	"context"
	"fmt"
	"os"

	"github.com/gin-gonic/gin"
	"go.opentelemetry.io/contrib/bridges/otelzap"
	otelmetric "go.opentelemetry.io/otel/metric"
	"go.opentelemetry.io/otel/sdk/log"
	"go.opentelemetry.io/otel/sdk/metric"
	"go.opentelemetry.io/otel/sdk/trace"
	oteltrace "go.opentelemetry.io/otel/trace"
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
)

// TelemetryProvider is an interface for the telemetry provider.
type TelemetryProvider interface {
	GetServiceName() string
	LogInfo(args ...interface{})
	LogErrorln(args ...interface{})
	LogFatalln(args ...interface{})
	MeterInt64Histogram(metric Metric) (otelmetric.Int64Histogram, error)
	MeterInt64UpDownCounter(metric Metric) (otelmetric.Int64UpDownCounter, error)
	TraceStart(ctx context.Context, name string) (context.Context, oteltrace.Span)
	LogRequest() gin.HandlerFunc
	MeterRequestDuration() gin.HandlerFunc
	MeterRequestsInFlight() gin.HandlerFunc
	Shutdown(ctx context.Context)
}

// Telemetry is a wrapper around the OpenTelemetry logger, meter, and tracer.
type Telemetry struct {
	lp     *log.LoggerProvider
	mp     *metric.MeterProvider
	tp     *trace.TracerProvider
	log    *zap.SugaredLogger
	meter  otelmetric.Meter
	tracer oteltrace.Tracer
	cfg    Config
}

// NewTelemetry creates a new telemetry instance.
func NewTelemetry(ctx context.Context, cfg Config) (*Telemetry, error) {
	rp := newResource(cfg.ServiceName, cfg.ServiceVersion)

	lp, err := newLoggerProvider(ctx, rp)
	if err != nil {
		return nil, fmt.Errorf("failed to create logger: %w", err)
	}

	logger := zap.New(
		zapcore.NewTee(
			zapcore.NewCore(zapcore.NewJSONEncoder(zap.NewProductionEncoderConfig()), zapcore.AddSync(os.Stdout), zapcore.InfoLevel),
			otelzap.NewCore(cfg.ServiceName, otelzap.WithLoggerProvider(lp)),
		),
	)

	mp, err := newMeterProvider(ctx, rp)
	if err != nil {
		return nil, fmt.Errorf("failed to create meter: %w", err)
	}
	meter := mp.Meter(cfg.ServiceName)

	tp, err := newTracerProvider(ctx, rp)
	if err != nil {
		return nil, fmt.Errorf("failed to create tracer: %w", err)
	}
	tracer := tp.Tracer(cfg.ServiceName)

	return &Telemetry{
		lp:     lp,
		mp:     mp,
		tp:     tp,
		log:    logger.Sugar(),
		meter:  meter,
		tracer: tracer,
		cfg:    cfg,
	}, nil
}

// GetServiceName returns the name of the service.
func (t *Telemetry) GetServiceName() string {
	return t.cfg.ServiceName
}

// LogInfo logs a message at the info level.
func (t *Telemetry) LogInfo(args ...interface{}) {
	t.log.Info(args...)
}

// LogErrorln logs a message and then calls os.Exit(1).
func (t *Telemetry) LogErrorln(args ...interface{}) {
	t.log.Errorln(args...)
}

// LogFatalln logs a message and then calls os.Exit(1).
func (t *Telemetry) LogFatalln(args ...interface{}) {
	t.log.Fatalln(args...)
}

// MeterInt64Histogram creates a new int64 histogram metric.
func (t *Telemetry) MeterInt64Histogram(metric Metric) (otelmetric.Int64Histogram, error) { //nolint:ireturn
	histogram, err := t.meter.Int64Histogram(
		metric.Name,
		otelmetric.WithDescription(metric.Description),
		otelmetric.WithUnit(metric.Unit),
	)

	if err != nil {
		return nil, fmt.Errorf("failed to create histogram: %w", err)
	}

	return histogram, nil
}

// MeterInt64UpDownCounter creates a new int64 up down counter metric.
func (t *Telemetry) MeterInt64UpDownCounter(metric Metric) (otelmetric.Int64UpDownCounter, error) { //nolint:ireturn
	counter, err := t.meter.Int64UpDownCounter(
		metric.Name,
		otelmetric.WithDescription(metric.Description),
		otelmetric.WithUnit(metric.Unit),
	)

	if err != nil {
		return nil, fmt.Errorf("failed to create counter: %w", err)
	}

	return counter, nil
}

// TraceStart starts a new span with the given name. The span must be ended by calling End.
func (t *Telemetry) TraceStart(ctx context.Context, name string) (context.Context, oteltrace.Span) { //nolint:ireturn
	//nolint: spancheck
	return t.tracer.Start(ctx, name)
}

// Shutdown shuts down the logger, meter, and tracer.
func (t *Telemetry) Shutdown(ctx context.Context) {
	t.lp.Shutdown(ctx)
	t.mp.Shutdown(ctx)
	t.tp.Shutdown(ctx)
}
```

在此文件中，定义了一个 `TelemetryProvider` 接口，以便更容易地在测试中模拟遥测包，而且更容易在将来更换底层遥测系统。

`NewTelemetry` 函数初始化日志记录、指标和跟踪，并返回 `Telemetry` 结构的一个实例。为了简单起见，我使用了 [zap](https://github.com/uber-go/zap) logger，但你可以使用任何其他与 OpenTelemetry 集成的 logger。请记住，`zap` logger 需要一个所谓的 **"bridge"** (`otelzap`) 才能与 OpenTelemetry 一起工作。

定义 `TelemetryProvider` 接口的一个优点是，我们可以轻松地更换底层遥测系统，例如在测试中。下面是一个 no-op 遥测提供程序的示例，该提供程序可以在测试中使用：

```go
package gotel

import (
	"context"
	"os"

	"github.com/gin-gonic/gin"
	"go.opentelemetry.io/otel/metric"
	"go.opentelemetry.io/otel/trace"
)

// NoopTelemetry is a no-op implementation of the TelemetryProvider interface.
type NoopTelemetry struct {
	serviceName string
}

// NewNoopTelemetry creates a new NoopTelemetry instance.
func NewNoopTelemetry(cfg Config) (*NoopTelemetry, error) {
	return &NoopTelemetry{serviceName: cfg.ServiceName}, nil
}

// GetServiceName returns the service name.
func (t *NoopTelemetry) GetServiceName() string { return t.serviceName }

// LogInfo logs nothing.
func (t *NoopTelemetry) LogInfo(args ...interface{}) {}

// LogErrorln logs nothing.
func (t *NoopTelemetry) LogErrorln(args ...interface{}) {}

// LogFatalln logs nothing, then exits.
func (t *NoopTelemetry) LogFatalln(args ...interface{}) {
	os.Exit(1)
}

// LogRequest is a no-op middleware.
func (t *NoopTelemetry) LogRequest() gin.HandlerFunc {
	return func(c *gin.Context) { c.Next() }
}

// MeterRequestDuration is a no-op middleware.
func (t *NoopTelemetry) MeterRequestDuration() gin.HandlerFunc {
	return func(c *gin.Context) { c.Next() }
}

// MeterRequestsInFlight is a no-op middleware.
func (t *NoopTelemetry) MeterRequestsInFlight() gin.HandlerFunc {
	return func(c *gin.Context) { c.Next() }
}

// TraceStart returns the context and span unchanged.
func (t *NoopTelemetry) TraceStart(ctx context.Context, name string) (context.Context, trace.Span) {
	return ctx, trace.SpanFromContext(ctx)
}

// MeterInt64Histogram returns nil.
func (t *NoopTelemetry) MeterInt64Histogram(metric Metric) (metric.Int64Histogram, error) {
	return nil, nil
}

// MeterInt64UpDownCounter returns nil.
func (t *NoopTelemetry) MeterInt64UpDownCounter(metric Metric) (metric.Int64UpDownCounter, error) {
	return nil, nil
}

// Shutdown does nothing.
func (t *NoopTelemetry) Shutdown(ctx context.Context) {}

```

`NoopTelemetry` 结构体实现了 `TelemetryProvider` 接口，但不执行任何操作。这对于测试非常有用，因为我们不希望将遥测数据发送到外部系统。

## 使用 Telemetry 包

在 `main.go` 中，我们现在可以初始化并使用我们的遥测系统。以下是如何使用 `gotel` 包创建新的遥测系统的示例。在此示例中，如果初始化失败，则 `NewTelemetry` 函数会回退到空操作遥测系统。这对于平稳降级非常有用，即使遥测系统出现故障，我们也希望继续运行应用程序。

```go
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/lucavallin/gotel"
)

func main() {
	ctx := context.Background()
	telemConfig, err := gotel.NewConfigFromEnv()
	if err != nil {
		fmt.Println("failed to load telemetry config")
		os.Exit(1)
	}
	// Initialize telemetry. If the exporter fails, fallback to nop.
	var telem gotel.TelemetryProvider
	telem, err = gotel.NewTelemetry(ctx, telemConfig)
	if err != nil {
		fmt.Println("failed to create telemetry, falling back to no-op telemetry")
		telem, _ = gotel.NewNoopTelemetry(telemConfig)
	}
	defer telem.Shutdown(ctx)
	telem.LogInfo("telemetry initialized")
}

```

`telem` 变量是 `Telemetry` 结构体的一个实例，它实现了 `TelemetryProvider` 接口。它可用于写入信息级别的日志，例如使用 `telem.LogInfo()`。`telem` 变量也可以传递到应用程序的其他部分，如服务、中间件等。

### 关于追踪？

追踪会跟踪请求在多个服务中的流动。一个追踪由 **spans** 组成，每个 span 代表一个单独的操作。`gotel` 包提供的 `TraceStart` 函数是一种启动新 span 并将其附加到当前上下文的便捷方法。这对于检测 HTTP 请求非常有用。

让我们来看一个虚构的 API 示例：

```go
type API struct {
	telem   gotel.TelemetryProvider
	httpSrv *http.Server
}
```

此 API 具有一个 `telem` 字段，用于保存对遥测系统的引用。我喜欢以这种方式构建我的 API，因为它使在 HTTP 处理程序中使用依赖项变得容易。

```go
func (a *API) GetSomething(c *gin.Context) {
	_, span := a.telem.TraceStart(c.Request.Context(), "get_something")
	defer span.End()
	something := []string{"foo", "bar", "baz"}
	c.JSON(http.StatusOK, something)
}
```

在此示例中，`GetSomething` 处理程序启动一个名为 `get_something` 的新 span，并将其附加到当前上下文中。`defer span.End()` 语句在函数返回时结束 span。

### 中间件 & 指标

一种常见的模式是使用 **middlewares** 来检测 HTTP 请求。以下是一个 `telemetry` 中间件的示例，该中间件记录请求持续时间并计算正在处理的请求数。这对于监视应用程序的运行状况非常有用。

在 `metrics.go` 文件中，我们定义了一个 `Metrics` 结构体，用于保存对我们要收集的指标的引用。这使得将指标传递给中间件和应用程序的其他部分变得容易。`Metric` 结构体定义了指标的名称、单位和描述。这对于以可重用的方式定义指标非常有用。

```go
package gotel

// Metric represents a metric that can be collected by the server.
type Metric struct {
	Name        string
	Unit        string
	Description string
}

// MetricRequestDurationMillis is a metric that measures the latency of HTTP requests processed by the server, in milliseconds.
var MetricRequestDurationMillis = Metric{
	Name:        "request_duration_millis",
	Unit:        "ms",
	Description: "Measures the latency of HTTP requests processed by the server, in milliseconds.",
}

// MetricRequestsInFlight is a metric that measures the number of requests currently being processed by the server.
var MetricRequestsInFlight = Metric{
	Name:        "requests_inflight",
	Unit:        "{count}",
	Description: "Measures the number of requests currently being processed by the server.",
}
```

`middleware.go`文件包含用于`gin`网络框架的遥测中间件。定义的中间件函数可用于记录请求、测量请求持续时间以及统计正在进行的请求数量。

现在，让我们创建一个 `telemetry` 中间件，它将记录请求持续时间并计算正在处理的请求数。

```go
package gotel

import (
	"strconv"
	"time"

	"github.com/gin-gonic/gin"
	"go.opentelemetry.io/otel/metric"
)

// TelemetryMiddlewareConfig is the configuration for the telemetry middleware.
type TelemetryMiddlewareConfig struct {
	RequestDuration metric.Int64Histogram
	RequestsInFlight metric.Int64UpDownCounter
}

// TelemetryMiddleware is a middleware that logs request duration and counts requests in flight.
func TelemetryMiddleware(config TelemetryMiddlewareConfig) gin.HandlerFunc {
	return func(c *gin.Context) {
		start := time.Now()
		config.RequestsInFlight.Add(c.Request.Context(), 1)
		defer config.RequestsInFlight.Add(c.Request.Context(), -1)

		c.Next()

		duration := time.Since(start)
		config.RequestDuration.Record(c.Request.Context(), duration.Milliseconds(), metric.WithAttributes())

		// Log additional info
		statusCode := c.Writer.Status()
		method := c.Request.Method
		path := c.Request.URL.Path

		// You can use your logger of choice here
		// slog.Info("request completed", "status_code", statusCode, "method", method, "path", path, "duration", duration.Milliseconds())
		_ = statusCode
		_ = method
		_ = path
	}
}
```

在此示例中，`TelemetryMiddleware` 接收一个 `TelemetryMiddlewareConfig`，其中包含对 `RequestDuration` 和 `RequestsInFlight` 指标的引用。该中间件记录请求的持续时间，并使用 `defer` 语句在请求完成时递减 `RequestsInFlight` 指标。

在 `main.go` 中，我们现在可以初始化我们的指标并使用 `TelemetryMiddleware`。





```go
package gotel

// Metric represents a metric that can be collected by the server.
type Metric struct {
	Name        string
	Unit        string
	Description string
}

// MetricRequestDurationMillis is a metric that measures the latency of HTTP requests processed by the server, in milliseconds.
var MetricRequestDurationMillis = Metric{
	Name:        "request_duration_millis",
	Unit:        "ms",
	Description: "Measures the latency of HTTP requests processed by the server, in milliseconds.",
}

// MetricRequestsInFlight is a metric that measures the number of requests currently being processed by the server.
var MetricRequestsInFlight = Metric{
	Name:        "requests_inflight",
	Unit:        "{count}",
	Description: "Measures the number of requests currently being processed by the server.",
}

```

一个 `middleware.go` 文件包含 `telemetry` 中间件，用于 [gin](https://gin-gonic.com) web 框架。定义的中间件函数可用于记录请求、测量请求持续时间以及计算正在处理的请求。

```go
package gotel

import (
	"fmt"
	"time"

	"github.com/gin-gonic/gin"
	"go.opentelemetry.io/otel/metric"
	"go.opentelemetry.io/otel/semconv/v1.20.0/httpconv"
)

// LogRequest 是一个 gin 中间件，用于记录请求路径。
func (t *Telemetry) LogRequest() gin.HandlerFunc {
	return func(c *gin.Context) {
		t.LogInfo("request to ", c.Request.URL.Path)
		c.Next()
		t.LogInfo("end of request to ", c.Request.URL.Path)
	}
}

// MeterRequestDuration 是一个 gin 中间件，用于捕获请求的持续时间。
func (t *Telemetry) MeterRequestDuration() gin.HandlerFunc {
	// init metric, here we are using histogram for capturing request duration
	histogram, err := t.MeterInt64Histogram(MetricRequestDurationMillis)
	if err != nil {
		t.LogFatalln(fmt.Errorf("failed to create histogram: %w", err))
	}
	return func(c *gin.Context) {
		// capture the start time of the request
		startTime := time.Now()
		// execute next http handler
		c.Next()
		// record the request duration
		duration := time.Since(startTime)
		histogram.Record(
			c.Request.Context(),
			duration.Milliseconds(),
			metric.WithAttributes(
				httpconv.ServerRequest(t.GetServiceName(), c.Request)...,
			),
		)
	}
}

// MeterRequestsInFlight 是一个 gin 中间件，用于捕获正在处理的请求数量。
func (t *Telemetry) MeterRequestsInFlight() gin.HandlerFunc {
	// init metric, here we are using counter for capturing request in flight
	counter, err := t.MeterInt64UpDownCounter(MetricRequestsInFlight)
	if err != nil {
		t.LogFatalln(fmt.Errorf("failed to create counter: %w", err))
	}
	return func(c *gin.Context) {
		// define metric attributes
		attrs := metric.WithAttributes(httpconv.ServerRequest(t.GetServiceName(), c.Request)...)
		// increase the number of requests in flight
		counter.Add(c.Request.Context(), 1, attrs)
		// execute next http handler
		c.Next()
		// decrease the number of requests in flight
		counter.Add(c.Request.Context(), -1, attrs)
	}
}

```

然后，您可以在应用程序中使用中间件来透明地获取可观测性数据。例如，使用 [gin-gonic/gin](https://github.com/gin-gonic/gin)：

```go
r := gin.New()
r.Use(telem.LogRequest())
r.Use(telem.MeterRequestDuration())
r.Use(telem.MeterRequestsInFlight())
```

有关更多信息，请参阅 gin 的 [Custom Middleware](https://gin-gonic.com/docs/examples/custom-middleware/) 文档。

## 那么遥测数据会去哪里呢？

遥测数据被发送到可观测性后端，Grafana 的 `grafana/docker-otel-lgtm` 是一个一体化的 OpenTelemetry 后端，可以轻松上手。

![Grafana's docker-otel-lgtm](https://www.lucavall.in/_next/image?url=%2Fimages%2Fblog%2Fopentelemetry-a-guide-to-observability-with-go%2Fgrafana-docker-otel-lgtm.webp&w=3840&q=75)

Grafana 的 `grafana/docker-otel-lgtm` 是一个 Docker 镜像，提供了一个即用型的 OpenTelemetry 后端。它将 OpenTelemetry Collector 与 Grafana 的 LGTM 堆栈（Loki 用于日志，Grafana 用于可视化，Tempo 用于跟踪，Mimir 用于指标）集成在一起。

通过运行此容器，您可以在默认端口（gRPC 为 4317，HTTP 为 4318）上接收 OpenTelemetry 信号。然后，这些信号会自动转发：日志转到 **Loki**，跟踪转到 **Tempo**，指标转到 **Mimir**。

Grafana 经过预配置，可以可视化所有这些数据源，并且可以通过端口 3000 访问。这使其成为开发、演示和测试环境的绝佳解决方案，提供了一种快速分析遥测数据的方法，而无需进行大量配置。

## 总结

可观测性不仅仅是锦上添花，它还可以防止您在应用程序出现问题时盲目飞行。OpenTelemetry 可以轻松地以标准化和供应商中立的方式**收集、处理和导出日志、指标和跟踪**。在这篇文章中，我们分解了可观测性的关键概念，探讨了 OpenTelemetry 的工作原理，并在 Go 中构建了一个可重用的遥测包，以保持整个应用程序中日志记录、指标和跟踪的清晰和一致。

通过将所有内容构建到一个易于使用的软件包中，我们简化了检测代码的过程，而不会使其混乱。无论您是需要调试慢速请求、跟踪系统性能，还是弄清楚为什么您的服务在凌晨 2 点着火，OpenTelemetry 都能满足您的需求。借助 Grafana 的 `docker-otel-lgtm`，您可以在几秒钟内启动一个功能齐全的 OpenTelemetry 后端，以可视化所有遥测数据。
如果你想尝试一下，可以看看 GitHub 上的 [gotel](https://github.com/lucavallin/gotel)。它被设计成即插即用，所以你可以立即开始收集日志、指标和追踪。祝你编码愉快，愿你的追踪总是能连接，你的指标有意义，你的日志能告诉你实际发生了什么！🚀