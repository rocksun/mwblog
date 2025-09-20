***编者注：** 本文摘自 Manning 出版的书籍《[Kubernetes 平台的 Fluent Bit](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS)》的第二章。本书教授如何为 Kubernetes 建立和优化可观测性系统等等。从基础配置到高级集成，本书详细介绍了 Fluent Bit 在日志、指标和追踪路由和处理方面的全部功能。[在此处](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS)下载整本书籍。*

当团队开始更广泛地投资于[可观测性和监控](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "可观测性和监控")时，他们会努力检查其应用程序是否平稳运行。通常，没有警报被解释为一切正常的迹象。但是如果监视器停止了呢？在这种情况下，没有事件就是一个问题。因此，Kubernetes 环境中的微服务应实现一个健康检查端点，传统上设置为 `/health`。这就引出了一个问题：[Fluent Bit](https://chronosphere.io/learn/deploy-fluent-bit-on-kubernetes/?utm_source=sponsored-content&utm_id=TNS) 是否有任何可以连接容器健康检查的东西？

## 了解容器和 Pod 健康探针

为了能够有效地管理容器或 Kubernetes pod，我们必须能够查询它们的状态。为此，[Dockerfiles](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/ "Dockerfiles") 包括定义健康检查操作的能力。（有关在 Dockerfiles 中定义健康检查的更多信息，请参见 <https://mng.bz/RN4a>。）对于 pod，我们可以描述几种不同的检查（也称为探针），包括活性。 （有关更多信息，请参见 <https://mng.bz/2gnw>。）如果 pod 没有足够快地响应来自 Kubernetes 的健康检查，我们可以假设 pod 不健康，需要用新实例替换。

Kubernetes 的健康响应通常是包含 HTTP 响应代码 `200` 的响应，该响应代码可能附带包含 `ok` 的主体。`200-299` 范围之外的任何 HTTP 响应代码都被认为是不健康的。容器化应用程序的常见做法是包含某种端点实现，该实现可以响应 `localhost:8080/v1/health` 上的调用，该调用提供有关应用程序运行状况的详细信息。

## 启用 Fluent Bit Web 服务器

为了使 Fluent Bit 能够通信并侦听 Web 传递的事件，我们需要包含一个 Web 服务器，这为我们提供了与 Fluent Bit 通信和查询的手段。第一步是配置 Fluent Bit 以启动 Web 服务器，我们通过 `[SERVICE]` 块中名为 `http_server` 的属性来完成此操作。我们还可以配置服务器应使用的 IP 和端口（分别为 `http_listen` 和 `http_port`）。

## 在 Fluent Bit 中配置健康检查

在服务器处于活动状态的情况下，我们还可以配置 Fluent Bit 如何响应健康检查。我们需要使用值为 `on` 的 `health_check` 属性来启用该功能；否则，将提供默认的 Web 服务器响应。启用运行状况响应后，我们可以控制 Fluent Bit 认为什么是健康的。

### Fluent Bit 认为的“健康”

健康的特征在于来自所有输出插件的错误计数，该计数是根据 `hc_error_count` 定义的阈值以及输出插件的失败重试次数 (`hc_retry_failure_count`) 来衡量的。我们不希望错误计数和重试错误计数是自 Fluent Bit 启动以来的累积分数，因此我们需要定义一个以秒表示的周期 (`hc_period`)，在该周期内应用该计数。

如果我们有一个输出试图写入一个由于文件系统已满而不断失败的文件，我们应该期望错误计数或重试失败计数很快超过阈值。因此，对健康检查 URL 的响应将是不好的。

当我们使用健康检查功能时，我们应该考虑到 Fluent Bit [认为什么是错误](https://chronosphere.io/learn/slos-open-source-microservices/?utm_source=sponsored-content&utm_id=TNS)及其影响。任何失败的输出都将导致不健康的响应，即使我们可以容忍这些输出的丢失。换句话说，无法定义对临时丢失某些输出的容忍度；这是一种全有或全无的方法。

### 输入和部分失败带来的挑战

另一个挑战是健康检查不会测试输入以查看它们是否正在成功工作。如果 tail（文件跟踪）输入无法读取输入文件，则不会成功产生不健康状态，因为该插件被认为是正常的，因为该插件存在并且参数值至少已定义。

## 使用 curl 和 Postman 查询 Fluent Bit 健康状况

以下清单显示了健康检查功能的配置；请参阅 chapter2\fluentbit\hello-world-server.conf。

### 使用 jq 使输出更具可读性

将其包含在我们的 hello-world 配置中后，我们可以运行 Fluent Bit (`fluentbit -c hello-world-server.conf`)，然后使用 curl 或 Postman（甚至浏览器）等工具来访问有关 Fluent Bit 的信息。要使用的 URL 是 `0.0.0.0:2020`，它为我们提供了 JSON 有效负载和有关 Fluent Bit 实例的详细信息。如果我们使用这种方法，我们可以使用 jq 使事情更具可读性：

`curl 0.0.0.0:2020 | jq`

除了 curl 命令之外，我们还创建了 Postman 配置，这些配置可用于执行不同的 API 端点，包括热重载。有关设置 Postman 的详细信息，请参见附录 A。

**注意：** 因为 [Fluent Bit 将其所有数据视为 JSON](https://chronosphere.io/learn/parsing-fluent-bit/?utm_source=sponsored-content&utm_id=TNS)，因此拥有一个可以格式化输出以使其更具可读性的工具（有时称为“漂亮打印”）很有用。要获取 jq 或了解其工作原理，请访问 https:// jqlang.github.io/jq。附录 B 中包含更多信息。

## 比较 API 版本：/api/v1/ 与 /api/v2/

Fluent Bit 提供的 API 不仅仅是检索摘要视图。某些 API 有两个可用版本：v1 通过 URL 路径 `/api/v1/` 访问，v2 通过路径 `/api/v2/` 访问。版本更改代表功能改进；较旧的 URL 版本被保留以实现向后兼容。一个例子是摘要 45 /metrics 端点；v1 提供 JSON 有效负载，v2 响应 Prometheus 格式的数据，并且数据比 `/v1/metrics` 更多。

## 在 Kubernetes 探针中使用 Fluent Bit 健康检查

对于 [Kubernetes 健康](https://chronosphere.io/learn/kubernetes-log-management/?utm_source=sponsored-content&utm_id=TNS) 检查，返回 `ok` 的简单响应表明容器实例运行平稳。要获得此响应，我们需要访问路径 `/api/v1/` 中更有意义的操作端点之一，例如 `/api/v1/ health`。如果我们使用 curl 命令调用健康检查 URL，我们可以期望得到 `ok` 的响应：

curl 0.0.0.0:2020/api/v1/health

## 常见问题解答

### 1. 如何在 Fluent Bit 中启用健康检查？

您需要在 `[SERVICE]` 块中配置三个关键设置：

* 将 `http_server on` 设置为启用 Web 服务器。
* 添加 `health_check on` 以激活健康检查响应。
* 配置 `http_listen` 和 `http_port` 以指定服务器的 IP 和端口（默认值：0.0.0.0:2020）。

### 2. 我应该使用哪个端点来检查 Fluent Bit 是否健康？

使用 `/api/v1/health` 端点获取简单的 `ok` 响应，表明健康状态。完整的 URL 格式为 `http://[host]:[port]/api/v1/health`（例如，`curl 0.0.0.0:2020/api/v1/health`）。此端点专为 Kubernetes 活性探针而设计，并为健康实例返回 HTTP 200 状态代码。

### 3. Fluent Bit 如何确定它是否健康？

Fluent Bit 的健康状态基于定义的时窗内输出插件的性能：

* **错误阈值：** 通过 `hc_error_count` 设置（允许的错误数）。
* **重试失败阈值：** 使用 `hc_retry_failure_count` 配置（失败的重试尝试）。
* **时间段：** 由 `hc_period` 定义（秒），以防止从启动开始的累积分数。
* **全有或全无的方法：** 任何失败的输出插件都会触发不健康的响应，而不能容忍部分失败

***注意：** 健康检查仅监视输出插件；输入插件故障（如无法读取的文件）不会触发不健康状态。*

在 Manning 出版的书籍《[Kubernetes 平台的 Fluent Bit](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS)》的后续章节中（尤其是第 3 章和第 5 章），我们将重新审视可用的 API。下载整本书籍以阅读 Fluent Bit 技术中十年来的创新和发展，包括解决现代可观测性挑战的指南，尤其是在 Kubernetes 等分布式系统中。