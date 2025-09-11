
<!--
title: 如何命名你的指标
cover: https://opentelemetry.io/img/social/logo-wordmark-001.png
summary: 本文介绍了如何命名OpenTelemetry指标，强调不要在指标名称中包含服务名称和单位，应将上下文信息放入资源属性中。好的命名能提高查询性能，简化运维，并促进跨服务聚合。
-->

本文介绍了如何命名OpenTelemetry指标，强调不要在指标名称中包含服务名称和单位，应将上下文信息放入资源属性中。好的命名能提高查询性能，简化运维，并促进跨服务聚合。

> 译自：[How to Name Your Metrics](https://opentelemetry.io/blog/2025/how-to-name-your-metrics/)
> 
> 作者：uraci Paixão Kröhling

指标是可观测性的定量支柱——这些数字告诉我们系统的运行状况。这是我们 OpenTelemetry 命名系列的第三篇文章，我们已经在之前探讨了[如何命名 spans](/blog/2025/how-to-name-your-spans/)和[如何使用有意义的属性丰富它们](/blog/2025/how-to-name-your-span-attributes/)。现在，让我们来探讨一下如何命名那些重要的测量值。

与讲述事件经过的 spans 不同，指标告诉我们关于数量的信息：有多少、有多快、有多少。但关键是——良好地命名它们与命名 spans 同样重要，而且我们已经学到的原则也适用于此。 “谁”仍然属于属性，而不是名称。

## 向传统系统学习

在深入研究 OpenTelemetry 的最佳实践之前，让我们先来看看传统的监控系统是如何处理指标命名的。以 Kubernetes 为例，它的指标遵循如下模式：

* `apiserver_request_total`
* `scheduler_schedule_attempts_total`
* `container_cpu_usage_seconds_total`
* `kubelet_volume_stats_used_bytes`

注意到这个模式了吗？**组件名称 + 资源 + 动作 + 单位**。服务或组件名称直接嵌入到指标名称中。这种方法在较简单的数据模型中是有意义的，因为在这些模型中，你存储上下文的选项有限。

但这会产生几个问题：

* **杂乱的可观测性后端**：每个组件都有自己的指标命名空间，使得在数十个或数百个名称相似的指标中找到正确的指标变得更加困难。
* **不灵活的聚合**：难以跨不同组件对指标进行求和。
* **厂商锁定**：指标名称与特定实现绑定。
* **维护开销**：添加新服务需要新的指标名称。

## 核心反模式：指标名称中的服务名称

以下是 OpenTelemetry 指标最重要的原则：**不要在指标名称中包含你的服务名称**。

假设你有一个支付服务。你可能会想创建如下指标：

* `payment.transaction.count`
* `payment.latency.p95`
* `payment.error.rate`

不要这样做。服务名称已经可以通过 `service.name` 资源属性作为上下文提供。 而是使用：

* `transaction.count`，带有 `service.name=payment`
* `http.server.request.duration`，带有 `service.name=payment`
* `error.rate`，带有 `service.name=payment`

为什么这样更好？因为现在你可以轻松地跨所有服务进行聚合：

```
sum(transaction.count)  // 所有服务的所有事务
sum(transaction.count{service.name="payment"})  // 仅支付事务
```

如果每个服务都有自己的指标名称，你需要知道每个服务名称才能构建有意义的仪表板。 使用清晰的名称，一个查询即可满足所有需求。

## OpenTelemetry 的丰富上下文模型

OpenTelemetry 指标受益于我们在 span 属性文章中讨论的[丰富的上下文模型](/docs/specs/otel/common/#attribute)。我们有多个层可以放置上下文，而不是将所有内容都塞进指标名称中：

### 传统方法 (Prometheus 风格):

```
payment_service_transaction_total{method="credit_card",status="success"}
user_service_auth_latency_milliseconds{endpoint="/login",region="us-east"}
inventory_service_db_query_seconds{table="products",operation="select"}
```

### OpenTelemetry 方法:

```
transaction.count
- Resource: service.name=payment, service.version=1.2.3, deployment.environment.name=prod
- Scope: instrumentation.library.name=com.acme.payment, instrumentation.library.version=2.1.0
- Attributes: method=credit_card, status=success

auth.duration
- Resource: service.name=user, service.version=2.0.1, deployment.environment.name=prod
- Scope: instrumentation.library.name=express.middleware
- Attributes: endpoint=/login, region=us-east
- Unit: ms

db.client.operation.duration
- Resource: service.name=inventory, service.version=1.5.2
- Scope: instrumentation.library.name=postgres.client
- Attributes: db.sql.table=products, db.operation=select
- Unit: s
```

这种三层分离遵循 OpenTelemetry 规范的 **Events → Metric Streams → Timeseries** 模型，其中上下文通过多个层次结构级别流动，而不是被塞进名称中。

## 单位：也别放在名称里

正如我们了解到服务名称不应该出现在指标名称中一样，**单位也不应该出现在那里**。

传统系统通常在名称中包含单位，因为它们缺乏正确的单位元数据：

* `response_time_milliseconds`
* `memory_usage_bytes`
* `throughput_requests_per_second`

OpenTelemetry 将单位视为元数据，与名称分开：

* `http.server.request.duration`，单位为 `ms`
* `system.memory.usage`，单位为 `By`
* `http.server.request.rate`，单位为 `{request}/s`

这种方法有几个好处：

1. **清晰的名称**：没有丑陋的后缀来搞乱你的指标名称。
2. **标准化的单位**：遵循[统一测量单位代码 (UCUM)](/docs/specs/semconv/general/metrics/#instrument-units)。
3. **后端灵活性**：系统可以自动处理单位转换。
4. **一致的约定**：与 OpenTelemetry [语义约定](/docs/specs/semconv/general/metrics/)保持一致。

规范建议使用非前缀单位，如 `By` (字节)，而不是 `MiBy` (兆字节)，除非有技术原因需要这样做。

## 实用命名指南

创建指标名称时，应用我们为 spans 学习的相同的 `{动词} {对象}` 原则，如果它有意义的话：

1. **关注操作**：正在测量什么？
2. **不是操作者**：谁在进行测量？
3. **遵循语义约定**：使用[已建立的模式](/docs/specs/semconv/general/metrics/)（如果可用）。
4. **将单位作为元数据保留**：不要在名称后附加单位。

以下是遵循 OpenTelemetry [语义约定](/docs/specs/semconv/general/metrics/)的示例：

* `http.server.request.duration`（不是 `payment_http_requests_ms`）
* `db.client.operation.duration`（不是 `user_service_db_queries_seconds`）
* `messaging.client.sent.messages`（不是 `order_service_messages_sent_total`）
* `transaction.count`（不是 `payment_transaction_total`）

## 真实世界的迁移示例

| 传统（名称中包含上下文 + 单位） | OpenTelemetry（清晰分离） | 为什么更好 |
| --- | --- | --- |
| `payment_transaction_total` | `transaction.count` + `service.name=payment` + 单位 `1` | 可跨服务聚合 |
| `user_service_auth_latency_ms` | `auth.duration` + `service.name=user` + 单位 `ms` | 标准的操作名称，正确的单位元数据 |
| `inventory_db_query_seconds` | `db.client.operation.duration` + `service.name=inventory` + 单位 `s` | 遵循语义约定 |
| `api_gateway_requests_per_second` | `http.server.request.rate` + `service.name=api-gateway` + 单位 `{request}/s` | 清晰的名称，正确的速率单位 |
| `redis_cache_hit_ratio_percent` | `cache.hit_ratio` + `service.name=redis` + 单位 `1` | 比率是无单位的 |

## 清晰命名的好处

将上下文与指标名称分离提供了特定的技术优势，可以提高查询性能和运营工作流程。 第一个好处是跨服务聚合。 像 `sum(transaction.count)` 这样的查询会返回来自所有服务的数据，而不需要你了解或维护服务名称列表。 在一个拥有 50 个微服务的系统中，这意味着一个查询而不是 50 个，并且当你添加第 51 个服务时，该查询不会中断。

这种一致性使仪表板可以在服务之间重复使用。 为监控身份验证服务中的 HTTP 请求而构建的仪表板可以无需修改地用于你的支付服务、库存服务或任何其他提供 HTTP 服务的组件。 你编写一次查询——`http.server.request.duration`，按 `service.name` 过滤——并将其应用到所有地方。 不再需要维护数十个几乎相同的仪表板。 现在，一些可观测性供应商更进一步，基于语义约定指标名称自动生成仪表板——当你的服务发出 `http.server.request.duration` 时，平台会准确地知道哪些可视化和聚合对该指标有意义。

清晰的命名还可以减少指标命名空间的混乱。 考虑一个拥有数十个服务，每个服务都定义了自己的指标的平台。 使用传统的命名，你的指标浏览器会显示数百个特定于服务的变体：`apiserver_request_total`、`payment_service_request_total`、`user_service_request_total`、`inventory_service_request_total` 等等。 找到正确的指标变成了在冗余的变体中滚动和搜索的练习。 使用清晰的命名，你只有一个指标名称（`request.count`），属性捕获上下文。 这使得指标发现变得简单——你找到你需要的测量值，然后按你关心的服务进行过滤。

当单位是元数据而不是名称后缀时，单位处理变得系统化。 可观测性平台可以自动执行单位转换——根据对可视化有意义的内容，在一个图中将相同的持续时间指标显示为毫秒，在另一个图中显示为秒。 该指标仍然是 `request.duration`，单位元数据为 `ms`，而不是两个单独的指标 `request_duration_ms` 和 `request_duration_seconds`。

该方法还确保了手动和自动检测之间的兼容性。 当你遵循语义约定（如 `http.server.request.duration`）时，你的自定义指标与自动检测库生成的指标保持一致。 这创建了一个一致的数据模型，其中查询可以在手动和自动检测的服务之间工作，并且工程师不需要记住哪些指标来自哪个来源。

## 要避免的常见陷阱

工程师经常将特定于部署的信息直接嵌入到指标名称中，从而创建了像 `user_service_v2_latency` 这样的模式。 当版本 3 部署时，这会中断——必须更新引用指标名称的每个仪表板、警报和查询。 具有特定于实例的名称（如 `node_42_memory_usage`）也会出现同样的问题。 在具有动态扩展的集群中，你最终会得到数百个代表相同测量值的不同指标名称，这使得编写简单的聚合查询变得不可能。

特定于环境的前缀会导致类似的维护问题。 使用名为 `prod_payment_errors` 和 `staging_auth_count` 的指标，你无法编写可以在环境之间工作的单个查询。 监控生产环境的仪表板无法在不修改的情况下用于暂存环境。 当你需要比较环境之间的指标（一种常见的调试任务）时，你必须编写显式引用每个环境的指标名称的复杂查询。

指标名称中的技术堆栈详细信息会在未来造成迁移难题。 当你用 Go 重写服务时，名为 `nodejs_payment_memory` 的指标会变得具有误导性。 类似地，如果你迁移到其他东西，则需要重命名 `postgres_user_queries`。 这些特定于技术的名称还阻止你编写可以在使用不同技术堆栈的服务之间工作的查询，即使它们执行相同的业务功能也是如此。

将业务领域与基础设施指标混合会违反系统做什么和如何做之间的分离。 像 `ecommerce_cpu_usage` 这样的指标会将业务目的（电子商务）与技术测量（CPU 使用率）混为一谈。 这使得在不同业务领域之间重用基础设施监控变得更加困难，并使同一基础设施为多个业务功能提供服务的多租户部署变得复杂。

现在 OpenTelemetry 提供了正确的单位元数据，因此在指标名称中包含单位（`latency_ms`、`memory_bytes`、`count_total`）的做法会造成冗余。 它还阻止了自动单位转换。 使用 `request_duration_ms` 和 `request_duration_seconds` 作为单独的指标，你需要针对不同的时间尺度使用不同的查询。 使用包含单位元数据的单个 `request.duration` 指标，可观测性平台会自动处理转换。

模式很清晰：按部署、实例、环境或版本变化的上下文属于属性，而不是指标名称。 指标名称应标识你正在测量的内容。 其他所有内容——谁在测量它，它在哪里运行，它是什么版本——都进入属性层，可以在那里根据需要进行过滤、分组和聚合。

## 培养更好的指标

就像我们在本系列前面介绍的 spans 一样，命名良好的指标是你和你团队的礼物。 它们在事件期间提供清晰度，支持强大的跨服务分析，并使你的可观测性数据真正有用，而不仅仅是大量数据。

关键的见解与我们从 spans 中学到的相同：**关注点分离**。 指标名称描述你正在测量的内容。 上下文——谁在测量它，在哪里，何时以及如何——存在于 OpenTelemetry 提供的丰富的属性层次结构中。

在我们的下一篇文章中，我们将深入探讨**指标属性**——使指标真正强大的上下文层。 我们将探讨如何构建不属于名称的丰富的上下文信息，以及如何平衡信息量与基数问题。

在那之前，请记住：清晰的指标名称就像一条维护良好的花园小路——它会引导你准确地到达你需要去的地方。
