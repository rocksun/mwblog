我的 [演示](https://github.com/nfrankel/opentelemetry-tracing) OpenTelemetry 追踪功能包含两个 Spring Boot 组件。
其中一个使用 Java 代理，我最近将它从 v1.x 升级到 v2.x 时，发现了一些不同的行为。
在另一个组件中，我使用 Micrometer Tracing，因为我编译到 GraalVM 原生，它无法处理 Java 代理。

我想在这篇文章中比较这三种不同的方法：Java 代理 v1、Java 代理 v2 和 Micrometer Tracing。

## 基础应用程序及其基础设施
我将使用相同的基准应用程序：一个用 Kotlin 编写的简单 Spring Boot 应用程序。它提供一个端点。

- 端点背后的函数名为
`entry()`
- 它调用另一个名为
`intermediate()`
的函数
- 后者使用
`WebClient`
实例，替换`RestTemplate`
，来调用上面的端点 - 为了避免无限循环，我传递了一个自定义请求头：
如果
`entry()`
函数找到它，它将不再继续执行
它转换为以下代码：

```kotlin
@SpringBootApplication
class Agent1xApplication

@RestController
class MicrometerController {
    private val logger = LoggerFactory.getLogger(MicrometerController::class.java)

    @GetMapping("/{message}")
    fun entry(@PathVariable message: String, @RequestHeader("X-done") done: String?) {
        logger.info("entry: $message")
        if (done == null) intermediate()
    }

    fun intermediate() {
        logger.info("intermediate")
        RestClient.builder()
            .baseUrl("http://localhost:8080/done")
            .build()
            .get()
            .header("X-done", "true")
            .retrieve()
            .toBodilessEntity()
    }
}
```
对于每种设置，我将检查两个阶段：启用 OpenTelemetry 的主要阶段，以及创建额外内部跨度的自定义阶段。

## Micrometer Tracing
Micrometer Tracing 源于 [Micrometer](https://micrometer.io/)，一个“供应商中立的应用程序可观察性门面”。

Micrometer Tracing 为最流行的跟踪库提供了一个简单的门面，让您可以在没有供应商锁定的情况下对基于 JVM 的应用程序代码进行检测。它旨在为您的跟踪收集活动增加很少或没有开销，同时最大限度地提高跟踪工作的可移植性。

要开始使用 Micrometer Tracing，需要添加一些依赖项：

- Spring Boot Actuator，
`org.springframework.boot:spring-boot-starter-actuator`
- Micrometer Tracing 本身，
`io.micrometer:micrometer-tracing`
- 到目标跟踪后端 API 的“桥梁”。
在我的例子中，它是 OpenTelemetry，因此
`io.micrometer:micrometer-tracing-bridge-otel`
- 到后端的具体导出器，
`io.opentelemetry:opentelemetry-exporter-otlp`
我们不需要 BOM，因为版本已经在 Spring Boot 父级中定义。

但是，我们需要两个运行时配置参数：
跟踪应该发送到哪里，以及组件的名称是什么。
它们由 `MANAGEMENT_OTLP_TRACING_ENDPOINT`
和 `SPRING_APPLICATION_NAME`
变量控制。

```yaml
services:
  jaeger:
    image: jaegertracing/all-in-one:1.55
    environment:
      - COLLECTOR_OTLP_ENABLED=true
    ports:
      - "16686:16686"
micrometer-tracing:
  build:
    dockerfile: Dockerfile-micrometer
  environment:
    MANAGEMENT_OTLP_TRACING_ENDPOINT: http://jaeger:4318/v1/traces
    SPRING_APPLICATION_NAME: micrometer-tracing
```
1. 启用 Jaeger 的 OpenTelemetry 收集器
2. Jaeger OpenTelemetry gRPC 端点的完整 URL
3. 设置 OpenTelemetry 的服务名称

以下是结果：

在没有任何自定义的情况下，Micrometer 在接收和发送 HTTP 请求时会创建跨度。

框架需要将魔法注入到 `RestClient`
中以进行发送。
我们必须让前者实例化后者才能做到这一点：

```kotlin
@SpringBootApplication
class MicrometerTracingApplication {
    @Bean
    fun restClient(builder: RestClient.Builder) =
        builder.baseUrl("http://localhost:8080/done").build()
}
```
我们可以通过多种方式创建手动跨度，其中一种是通过 OpenTelemetry API 本身。
但是，设置需要大量的样板代码。
最直接的方法是 Micrometer 的 [Observation API](https://docs.micrometer.io/micrometer/reference/observation.html)。
它的主要好处是使用单个 API 来管理 *指标* 和 *跟踪*。

以下是更新后的代码：

```kotlin
class MicrometerController(
    private val restClient: RestClient,
    private val registry: ObservationRegistry
) {
    @GetMapping("/{message}")
    fun entry(@PathVariable message: String, @RequestHeader("X-done") done: String?) {
        logger.info("entry: $message")
        val observation = Observation.start("entry", registry)
        if (done == null) intermediate(observation)
        observation.stop()
    }

    fun intermediate(parent: Observation) {
        logger.info("intermediate")
        val observation = Observation.createNotStarted("intermediate", registry)
            .parentObservation(parent)
            .start()
        restClient.get()
            .header("X-done", "true")
            .retrieve()
            .toBodilessEntity()
        observation.stop()
    }
}
```
添加的观察调用反映在生成的跟踪中：

## OpenTelemetry 代理 v1

Micrometer Tracing 的替代方案是通用的 [OpenTelemetry Java Agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation)。
其主要优势在于它既不影响代码也不影响开发人员；
该代理纯粹是运行时范围内的关注点。

`java -javaagent:opentelemetry-javaagent.jar agent-one-1.0-SNAPSHOT.jar`
该代理遵守 OpenTelemetry 的环境变量配置：

```
services:
agent-1x:
build:
dockerfile: Dockerfile-agent1
environment:
OTEL_EXPORTER_OTLP_ENDPOINT: http://jaeger:4317
OTEL_RESOURCE_ATTRIBUTES: service.name=agent-1x
OTEL_METRICS_EXPORTER: none
OTEL_LOGS_EXPORTER: none
ports:
- "8081:8080"
```

1. 设置协议、域名和端口。
库附加 `/v1/traces`
2. 设置 OpenTelemetry 的服务名称
3. 不导出指标或日志

无需更多配置，我们就可以获得以下跟踪：

该代理会自动跟踪接收和发送的请求，**以及使用 Spring 相关注释标记的函数**。
跟踪根据调用堆栈正确地嵌套在彼此内部。
要跟踪其他函数，我们需要在代码库中添加一个依赖项，`io.opentelemetry.instrumentation:opentelemetry-instrumentation-annotations`
。
我们现在可以使用 `@WithSpan`
注释来注释以前未跟踪的函数。

`value()`
部分控制跟踪的标签，而 `kind`
则转换为 `span.kind`
属性。
如果将值设置为空字符串（默认值），则它会输出函数的名称。
就我而言，默认值就足够了。

```
@WithSpan
fun intermediate() {
logger.info("intermediate")
RestClient.builder()
.baseUrl("http://localhost:8080/done")
.build()
.get()
.header("X-done", "true")
.retrieve()
.toBodilessEntity()
}
```
它会生成预期的新的 `intermediate()`
跟踪：

## OpenTelemetry Agent v2
OpenTelemetry 在今年 1 月发布了代理的新主要版本。我用它更新了我的演示；现在只有在应用程序接收和发送请求时才会创建跟踪。

与之前的版本一样，我们可以使用 `@WithSpan`
注释添加跟踪。
唯一的区别是，我们还必须注释 `entry()`
函数。
它默认情况下不会被跟踪。

## 讨论
Spring 成功的两个原因是：
它简化了复杂的解决方案，*例如*，EJBs 2，并为竞争库提供了一个抽象层。
Micrometer Tracing 最初是作为 Zipkin 和 Jaeger 之上的抽象层，这很有道理。
随着 OpenTelemetry 被大多数跨编程语言和跟踪收集器的库支持，这个论点变得毫无意义。
观察 API 仍然是 Micrometer Tracing 的一个重要优势，因为它使用单个 API 来处理指标和跟踪。

在 Java Agent 方面，OpenTelemetry 配置在所有技术栈和库中都类似 - 环境变量。当我从 v1 升级到 v2 时，我有点失望，因为新代理不了解 Spring：默认情况下不会跟踪 Spring 注释的函数。最终，这是一个明智的决定。明确你想要哪些跨度比删除你不想要看到的跨度要好得多。

*感谢 Jonatan Ivanov 的帮助和审查*。
[Github](https://github.com/ajavageek/boot-tracing)。