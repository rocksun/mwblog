# 开始使用 otelsql，Go SQL 的 OpenTelemetry 工具

[otelsql](https://github.com/XSAM/otelsql) 是一个针对 [Go 编程语言的库](https://pkg.go.dev/database/sql) 的工具库。它在与数据库交互时生成应用程序的跟踪和指标。通过这样做，该库允许您识别可能影响应用程序性能的 SQL 查询中的错误或速度下降。

让我们深入了解如何使用此库！

## 开始使用

otelsql 是 `database/sql` 中接口的包装层。当用户使用包装的数据库接口时，otelsql 会生成遥测数据并将操作传递给底层数据库。

在以下示例中，您将使用 [Docker Compose](https://docs.docker.com/compose/) 从 otelsql 存储库运行 `otel-collector` 示例。此示例使用带有 otelsql 工具的 MySQL 客户端。它生成的遥测数据将被推送到 OpenTelemetry Collector。然后，它在 Jaeger 上显示跟踪数据，在 Prometheus 服务器上显示指标数据。

以下是数据流：

流程图 LR；
A[MySQL 客户端]-->B[OpenTelemetry Collector]；
B-->C["Jaeger（跟踪）"]；
B-->D["Prometheus（指标）"]；

让我们在此处克隆 otelsql 存储库并运行示例，并查看最重要的代码行。

```
git clone https://github.com/XSAM/otelsql.git
```

在 `otelsql` 文件夹中，您还可以签出 git 标记 `v0.29.0`（撰写此帖子时的最新标记），以确保示例可运行，因为运行示例的步骤将来可能会更改。

```
git checkout tags/v0.29.0
```

让我们转到 `otel-collector` 示例的文件夹并启动所有服务。

```
cd example/otel-collector
docker compose up -d
```

在构建映像并运行服务后，让我们检查服务日志以确保 SQL 客户端已完成。

```
docker compose logs client
```

然后，我们可以访问 [localhost:16686](http://localhost:16686) 上的 Jaeger UI 和 [localhost:9090](http://localhost:9090) 上的 Prometheus UI 来查看结果。

我们在这里查看 Jaeger 上的跟踪图。我们可以看到与数据库的每次操作的持续时间和参数。

![Jaeger UI 示例](jaeger-example.png)

我们在这里查看 Prometheus 上的指标 `db_sql_latency_milliseconds_sum`。

![Prometheus UI 示例](prometheus-example.png)

可以在 [otelsql 文档](https://github.com/XSAM/otelsql/blob/main/README.md#metric-instruments) 中找到更多 otelsql 生成的指标选项。

## 了解示例

让我们首先查看 `docker-compose.yaml` 文件。

```yaml
version: '3.9'
services:
  mysql:
    image: mysql:8.3
    environment:
      - MYSQL_ROOT_PASSWORD=otel_password
      - MYSQL_DATABASE=db
    healthcheck:
      test:
        mysqladmin ping -h 127.0.0.1 -u root --password=$$MYSQL_ROOT_PASSWORD
      start_period: 5s
      interval: 5s
      timeout: 5s
      retries: 10
  otel-collector:
    image: otel/opentelemetry-collector-contrib:0.91.0
    command: ['--config=/etc/otel-collector.yaml']
    volumes:
      - ./otel-collector.yaml:/etc/otel-collector.yaml
    depends_on:
      - jaeger
  prometheus:
    image: prom/prometheus:v2.45.2
    volumes:
      - ./prometheus.yaml:/etc/prometheus/prometheus.yml
    ports:
      - 9090:9090
    depends_on:
      - otel-collector
  jaeger:
    image: jaegertracing/all-in-one:1.52
    ports:
      - 16686:16686
  client:
    build:
      dockerfile: $PWD/Dockerfile
      context: ../..
    depends_on:
      mysql:
        condition: service_healthy
```

此 Docker compose 文件包含五项服务。

客户端服务是使用 Dockerfile 构建的 MySQL 客户端，示例文件夹中的源代码是 `main.go`。

客户端服务在 `mysql` 服务启动后运行。然后，它初始化 OpenTelemetry 客户端和 otelsql 工具，向 `mysql` 服务发出 SQL 查询，并通过 [OpenTelemetry 协议 (OTLP)](/docs/specs/otel/protocol/) 将指标和跟踪数据发送到 `otel-collector` 服务。

收到数据后，`otel-collector` 服务传输数据格式，并将指标数据发送到 `prometheus` 服务，并将跟踪数据发送到 `jaeger` 服务。

让我们检查 `main.go` 以查看客户端服务中发生了什么。以下是 `main` 函数。

```go
func main() {
  ctx, cancel := signal.NotifyContext(context.Background(), os.Interrupt)
  defer cancel()
  conn, err := initConn(ctx)
  if err != nil {
    log.Fatal(err)
  }
  shutdownTracerProvider, err := initTracerProvider(ctx, conn)
  if err != nil {
    log.Fatal(err)
  }
  defer func() {
    if err := shutdownTracerProvider(ctx); err != nil {
      log.Fatalf("failed to shutdown TracerProvider: %s", err)
    }
  }()
  shutdownMeterProvider, err := initMeterProvider(ctx, conn)
  if err != nil {
    log.Fatal(err)
  }
  defer func() {
    if err := shutdownMeterProvider(ctx); err != nil {
      log.Fatalf("failed to shutdown MeterProvider: %s", err)
    }
  }()
  db := connectDB()
  defer db.Close()
  err = runSQLQuery(ctx, db)
  if err != nil {
    log.Fatal(err)
  }
  fmt.Println("示例已完成")
}
```

此 `main` 函数非常简单。它使用：
**otel-collector 服务**

otel-collector 服务由跟踪提供程序和度量提供程序使用。然后，它使用 `connect` 和 `close` 方法配置跟踪提供程序和度量提供程序，这可确保在退出应用程序之前将遥测数据正确推送到 otel-collector 服务。

完成 OpenTelemetry 客户端设置后，它调用 `connectDB` 方法以使用 otelsql 库与 MySQL 数据库进行交互。我们在此处查看详细信息。

```go
func connectDB() *sql.DB {
    // 连接到数据库
    db, err := otelsql.Open("mysql", mysqlDSN, otelsql.WithAttributes(
        semconv.DBSystemMySQL,
    ))
    if err != nil {
        log.Fatal(err)
    }
    // 将数据库统计信息注册到度量
    err = otelsql.RegisterDBStatsMetrics(db, otelsql.WithAttributes(
        semconv.DBSystemMySQL,
    ))
    if err != nil {
        log.Fatal(err)
    }
    return db
}
```

我们不使用 Go 提供的 [`sql.Open`](https://pkg.go.dev/database/sql#Open) 方法，而是使用 [`otelsql.Open`](https://pkg.go.dev/github.com/XSAM/otelsql#Open) 来创建 [`sql.DB`](https://pkg.go.dev/database/sql#DB) 实例。

`otelsql.Open` 返回的实例是一个包装器，它将所有数据库操作传输并记录到底层 `sql.DB` 实例（由 `sql.Open` 创建）。当用户使用此包装器发送 SQL 查询时，`otelsql` 可以看到查询并使用 OpenTelemetry 客户端生成遥测数据。

除了使用 `otelsql.Open`，`otelsql` 还提供了三种其他方式来初始化记录：`otelsql.OpenDB`、`otelsql.Register` 和 `otelsql.WrapDriver`。这些其他方法涵盖了不同的用例，因为某些数据库驱动程序或框架不提供创建 `sql.DB` 的直接方式。有时，您可能需要这些其他方法来手动创建 `sql.DB` 并将其推送到这些数据库驱动程序。您可以查看 [otelsql 文档中的示例](https://pkg.go.dev/github.com/XSAM/otelsql#pkg-examples) 以了解如何使用这些方法。

继续，我们使用 `otelsql.RegisterDBStatsMetrics` 从 `sql.DBStats` 注册度量数据。度量记录进程在后台运行，并在注册后根据需要更新度量的值，因此我们不必担心为此创建单独的线程。

在 `sql.DB` 被 `otelsql` 包装后，我们可以使用它进行查询。

```go
func runSQLQuery(ctx context.Context, db *sql.DB) error {
    // 创建父级跨度（可选）
    tracer := otel.GetTracerProvider()
    ctx, span := tracer.Tracer(instrumentationName).Start(ctx, "example")
    defer span.End()
    err := query(ctx, db)
    if err != nil {
        span.RecordError(err)
        return err
    }
    return nil
}

func query(ctx context.Context, db *sql.DB) error {
    // 进行查询
    rows, err := db.QueryContext(ctx, `SELECT CURRENT_TIMESTAMP`)
    if err != nil {
        return err
    }
    defer rows.Close()
    var currentTime time.Time
    for rows.Next() {
        err = rows.Scan(&currentTime)
        if err != nil {
            return err
        }
    }
    fmt.Println(currentTime)
    return nil
}
```

此 `runSQLQuery` 方法首先创建一个父级跨度（这是一个可选步骤，它使查询跨度具有父级，并且在跟踪图中看起来不错），然后从 MySQL 数据库查询当前时间戳。

此方法之后，客户端应用程序完成并退出。它们是理解示例最重要的代码行。

## 将示例用作游乐场

在理解示例后，我们可以将其用作游乐场，使其有点复杂，以了解如何在实际场景中使用它。

使用以下代码替换示例中的 `runSQLQuery` 方法。

```go
func runSQLQuery(ctx context.Context, db *sql.DB) error {
    // 创建父级跨度（可选）
    tracer := otel.GetTracerProvider()
    ctx, span := tracer.Tracer(instrumentationName).Start(ctx, "example")
    defer span.End()
    runSlowSQLQuery(ctx, db)
    err := query(ctx, db)
    if err != nil {
        span.RecordError(err)
        return err
    }
    return nil
}

func runSlowSQLQuery(ctx context.Context, db *sql.DB) {
    db.QueryContext(ctx, `SELECT SLEEP(1)`)
}
```

这次，我们向示例中添加了一个新查询，这是一个慢查询，需要 1 秒才能返回。让我们看看可能发生的情况以及如何识别此慢查询。

为了使此更改生效，我们需要重新构建客户端服务。

```
docker compose build client
docker compose up client
```

客户端完成后，我们可以检查 Jaeger 上我们刚刚生成的跟踪的跟踪图。

![真实世界类似 Jaeger UI 的示例](real-world-like-jaeger-example.png)

从这个图中，我们知道整个示例需要 1 秒才能完成。此缓慢的根本原因与数据库和时间戳查询的网络延迟无关。导致缓慢的是 `SELECT SLEEP(1)` 查询。

您还可以通过度量了解数据库的聚合统计信息来了解缓慢。这就是 otelsql 可以提供的可观察性，以便您可以了解您的应用程序正在使用数据库做什么。

## 兼容性
您可能会担心与其他数据库和其他第三方数据库框架（如 ORM）的兼容性问题，并想知道此检测工具的适用范围有多广。

从实现角度来看，只要数据库驱动程序或数据库框架通过 `database/sql` 与上下文一起与数据库（任何数据库，不仅仅是 SQL 数据库）进行交互，`otelsql` 就应该可以正常工作。

这是一个 [示例](https://github.com/ent/ent/issues/1232#issuecomment-1200405070)，展示了 `otelsql` 如何与 Facebook 的 Go 实体框架配合使用。

## 其他酷炫功能

既然您已经体验了主要功能，让我们花点时间来探索 `otelsql` 提供的其他酷炫功能。

### Sqlcommenter 支持

`otelsql` 集成了 [Sqlcommenter](https://google.github.io/sqlcommenter)，这是一个开源 ORM 自动检测库，通过在 SQL 语句中注入注释来与 OpenTelemetry 合并，从而为数据库启用上下文传播。

使用选项 `WithSQLCommenter`，`otelsql` 会为其检测的每个 SQL 语句注入一条注释。

例如，发送到数据库的 SQL 查询

```
SELECT * from FOO
```

将变为

```
SELECT * from FOO /*traceparent='00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01',tracestate='congo%3Dt61rcWkgMzE%2Crojo%3D00f067aa0ba902b7'*/
```

然后，支持 `Sqlcommenter` 的数据库可以为该查询记录其操作，并将其跟踪范围发布到跟踪存储中，这样您就可以在一个地方看到您的应用程序跟踪范围与来自数据库的查询跟踪范围相关联。

![来自 Google Cloud 文档的 Sqlcommenter 示例](sqlcommenter-example.png)

图片来自 [Google Cloud 文档]。

### 自定义范围名称

如果您不喜欢默认范围名称，可以使用 `otelsql.WithSpanNameFormatter` 自定义范围名称。

以下是示例用法：

```go
otelsql.WithSpanNameFormatter(func(ctx context.Context, method otelsql.Method, query string) string {
    return string(method) + ": " + query
})
```

然后，范围名称可以变为 `{method}: {query}`。以下是范围名称的示例：

```
sql.conn.query: select current_timestamp
```

### 筛选范围

您可以使用 `otelsql.SpanOptions` 中的 `otelsql.SpanFilter` 筛选掉您不想生成的范围。当您想要丢弃某些范围时，这很有用。

## 接下来的步骤是什么？

现在，您应该能够将从这篇博文中了解到的内容应用到您自己的 `otelsql` 安装中。

我很想听听您的体验！如果您觉得 `otelsql` 有用，请为其点亮星标！如果您遇到任何问题，请随时 [联系我们](https://github.com/XSAM/otelsql?tab=readme-ov-file#communication) 或 [创建问题](https://github.com/XSAM/otelsql/issues)。