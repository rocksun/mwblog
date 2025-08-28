
<!--
title: Span属性命名指南
cover: https://opentelemetry.io/img/social/logo-wordmark-001.png
summary: 本文介绍了 OpenTelemetry 中 span 属性命名的最佳实践，强调了使用语义约定、领域优先而非公司优先，以及遵循命名结构的重要性。避免使用保留的命名空间，并为可重用性构建属性。
-->

本文介绍了 OpenTelemetry 中 span 属性命名的最佳实践，强调了使用语义约定、领域优先而非公司优先，以及遵循命名结构的重要性。避免使用保留的命名空间，并为可重用性构建属性。

> 译自：[How to Name Your Span Attributes](https://opentelemetry.io/blog/2025/how-to-name-your-span-attributes/)
> 
> 作者：Juraci Paixão Kröhling

欢迎来到我们 OpenTelemetry 命名最佳实践系列的第二篇。在[之前的文章](/blog/2025/how-to-name-your-spans/)中，我们探讨了如何使用 `{动词} {名词}` 模式来命名 span。今天，我们将深入研究 span 属性——这些丰富的上下文数据可以将你的追踪从简单的操作日志转换为强大的调试和分析工具。

本指南面向以下开发者：

* **使用自定义 span 和属性来检测自己的应用程序**
* **增强可观测性**，超越自动检测提供的范围
* **创建库**，供他人检测

你所做的属性命名决策直接影响你的可观测性数据的可用性和可维护性。让我们把它们做好。

## 从语义约定开始

这是最重要的一条规则，可以节省你的时间并提高互操作性：**如果存在 OpenTelemetry
[语义约定](/docs/specs/semconv/registry/attributes/)，并且语义与你的用例相符，请使用它**。

这不仅仅是为了方便——而是为了构建与更广泛的 OpenTelemetry 生态系统无缝集成的遥测数据。当你使用标准化的属性名称时，你的数据会自动与现有的仪表板、警报规则和分析工具配合使用。

### 当语义匹配时，使用约定

| 你的需求 | 使用这个语义约定 | 为什么 |
| --- | --- | --- |
| HTTP 请求方法 | `http.request.method` | 在所有 HTTP 检测中标准化 |
| 数据库集合名称 | `db.collection.name` | 与数据库监控工具配合使用 |
| 服务标识 | `service.name` | 用于服务关联的核心资源属性 |
| 网络对等地址 | `network.peer.address` | 网络级别调试的标准 |
| 错误分类 | `error.type` | 实现一致的错误分析 |

关键原则是**语义匹配优先于命名偏好**。即使你更喜欢 `database_table` 而不是 `db.collection.name`，当语义约定准确地描述你的数据时，也要使用它。

### 当语义不匹配时，不要强行使用

抵制滥用语义约定的诱惑：

| 不要这样做 | 为什么是错的 |
| --- | --- |
| 将 `db.collection.name` 用于文件名 | 文件和数据库集合是不同的概念 |
| 将 `http.request.method` 用于业务操作 | “approve\_payment” 不是 HTTP 方法 |
| 将 `user.id` 用于交易 ID | 用户和交易是不同的实体 |

滥用语义约定比创建自定义属性更糟糕——它会造成混淆，并破坏期望标准语义的工具。

## 黄金法则：领域优先，永远不是公司优先

当你需要超出语义约定的自定义属性时，最关键的原则是：**从领域或技术开始，永远不要从你的公司或应用程序名称开始**。

这个原则看起来很明显，但在整个行业中却经常被违反。以下是它重要的原因以及如何正确地做到这一点。

### 为什么公司优先的命名会失败

| 糟糕的属性名称 | 问题 |
| --- | --- |
| `og.user.id` | 公司前缀污染全局命名空间 |
| `myapp.request.size` | 应用程序特定，不可重用 |
| `acme.inventory.count` | 难以与标准属性关联 |
| `shopify_store.product.sku` | 不必要地将概念与一个供应商联系起来 |

这些方法创建的属性具有以下特点：

* 难以跨团队和组织关联
* 无法在不同的上下文中重用
* 被供应商锁定且不灵活
* 与 OpenTelemetry 的互操作性目标不一致

### 领域优先的成功案例

| 好的属性名称 | 为什么有效 |
| --- | --- |
| `user.id` | 通用概念，与供应商无关 |
| `request.size` | 可在应用程序中重用 |
| `inventory.count` | 清晰、特定于领域的概念 |
| `product.sku` | 标准电子商务术语 |
| `workflow.step.name` | 通用流程管理概念 |

这种方法创建的属性是普遍可理解的，可以被面临类似问题的其他人重用，并且具有面向未来的特性。

## 理解结构：点和下划线

OpenTelemetry 属性名称遵循特定的结构模式，该模式在可读性和一致性之间取得平衡。理解这种模式有助于你创建与标准语义约定自然匹配的属性。

### 使用点进行分层分隔

点 (`.`) 分隔分层组件，遵循以下模式：
`{domain}.{component}.{property}`

来自语义约定的示例：

* `http.request.method` - HTTP 域，请求组件，方法属性
* `db.collection.name` - 数据库域，集合组件，名称属性
* `service.instance.id` - 服务域，实例组件，ID 属性

### 使用下划线表示多词组件

当单个组件包含多个单词时，使用下划线 (`_`)：

* `http.response.status_code` - “status\_code” 是一个逻辑组件
* `system.memory.usage_percent` - “usage\_percent” 是一种测量概念

### 在需要时创建更深层次的层次结构

当增加清晰度时，你可以进一步嵌套：

* `http.request.body.size`
* `k8s.pod.label.{key}`
* `messaging.kafka.message.key`

每个级别应代表一个有意义的概念边界。

## 保留的命名空间：你绝对不能使用的

某些命名空间受到严格保留，违反这些规则可能会破坏你的遥测数据。

### `otel.*` 命名空间是禁区

`otel.*` 前缀专门为 OpenTelemetry 规范本身保留。它用于在本身不支持 OpenTelemetry 概念的遥测格式中表达这些概念。

保留的 `otel.*` 属性包括：

* `otel.scope.name` - 检测范围名称
* `otel.status_code` - Span 状态码
* `otel.span.sampling_result` - 抽样决策

**永远不要创建以 `otel.` 开头的属性**。对此命名空间的任何添加都必须作为 OpenTelemetry 规范的一部分获得批准。

### 其他保留属性

该规范还保留了以下特定属性名称：

* `error.type`
* `exception.message`, `exception.stacktrace`, `exception.type`
* `server.address`, `server.port`
* `service.name`
* `telemetry.sdk.language`, `telemetry.sdk.name`, `telemetry.sdk.version`
* `url.scheme`

## 语义约定模式

培养良好属性命名直觉的最佳方法是研究 OpenTelemetry 的语义约定。这些代表了可观测性专家数千小时的设计工作。

### 域组织模式

请注意语义约定如何围绕清晰的域进行组织：

#### 基础设施域

* `service.*` - 服务标识和元数据
* `host.*` - 主机/机器信息
* `container.*` - 容器运行时信息
* `process.*` - 操作系统进程

#### 通信域

* `http.*` - HTTP 协议规范
* `network.*` - 网络层信息
* `rpc.*` - 远程过程调用属性
* `messaging.*` - 消息队列系统

#### 数据域

* `db.*` - 数据库操作
* `url.*` - URL 组件

### 通用属性模式

在所有域中，都出现了常见属性的一致模式：

#### 标识属性

* `.name` - 人类可读的标识符 (`service.name`, `container.name`)
* `.id` - 系统标识符 (`container.id`, `process.pid`)
* `.version` - 版本信息 (`service.version`)
* `.type` - 分类 (`messaging.operation.type`, `error.type`)

#### 网络属性

* `.address` - 网络地址 (`server.address`, `client.address`)
* `.port` - 端口号 (`server.port`, `client.port`)

#### 测量属性

* `.size` - 字节测量 (`http.request.body.size`)
* `.count` - 数量 (`messaging.batch.message_count`)
* `.duration` - 时间测量 (`http.server.request.duration`)

创建自定义域时，请遵循相同的模式。对于库存管理，请考虑：

* `inventory.item.name`
* `inventory.item.id`
* `inventory.location.address`
* `inventory.batch.count`

## 安全地创建自定义域

有时，你的业务逻辑需要超出现有语义约定的属性。这是正常的——OpenTelemetry 无法涵盖所有可能的业务域。

### 安全自定义域的指南

1. **选择描述性、通用的名称**，其他人可以重用。
2. **避免在域名中使用公司特定的术语**。
3. **遵循语义约定建立的分层模式**。
4. **考虑你的域是否可以成为未来的语义约定**。

### 设计良好的自定义属性示例

| 域 | 好的属性 | 为什么有效 |
| --- | --- | --- |
| 业务 | `payment.method`, `order.status` | 清晰、可重用的业务概念 |
| 物流 | `inventory.location`, `shipment.carrier` | 特定于领域但可转移 |
| 流程 | `workflow.step.name`, `approval.status` | 通用流程管理 |
| 内容 | `document.format`, `media.codec` | 通用内容概念 |

## 罕见的例外：何时前缀有意义

在极少数情况下，你可能需要公司或应用程序前缀。这种情况通常发生在你自定义的属性可能与分布式系统中来自其他来源的属性冲突时。

**在以下情况下考虑前缀：**

* 你的属性可能与分布式系统中的供应商属性冲突。
* 你正在检测真正特定于公司的专有技术。
* 你正在捕获不应概括的内部实现细节。

对于大多数业务逻辑属性，请坚持使用领域优先的命名。

## 你的行动计划

良好地命名 span 属性可以创建可维护、可互操作且在你的组织内有价值的遥测数据。以下是你的路线图：

1. **始终首先检查语义约定** - 当语义匹配时使用它们。
2. **以领域为先，永远不要以公司为先** - 创建与供应商无关的属性。
3. **尊重保留的命名空间** - 尤其要避免 `otel.*`。
4. **遵循分层模式** - 一致地使用点和下划线。
5. **为可重用性而构建** - 考虑超出你当前的需求。

通过遵循这些原则，你不仅解决了今天的检测挑战，而且为更连贯、可互操作的可观测性生态系统做出了贡献，使每个人都受益。

在本系列的下一篇文章中，我们将把重点从 span 转移到指标——探索如何命名定量测量，这些测量告诉我们系统的性能如何，以及为什么分离和领域优先思维的相同原则适用于最重要的数字。
