
<!--
title: 可观测性设计：OpenTelemetry Weaver赋能一致性
cover: https://opentelemetry.io/img/social/logo-wordmark-001.png
summary: OpenTelemetry Weaver 帮助团队通过设计构建可观测性，通过语义约定实现一致的、类型安全的和自动化的遥测。通过 Weaver，您可以定义、验证和演进您的遥测模式，确保系统的可靠性和清晰度。
-->

OpenTelemetry Weaver 帮助团队通过设计构建可观测性，通过语义约定实现一致的、类型安全的和自动化的遥测。通过 Weaver，您可以定义、验证和演进您的遥测模式，确保系统的可靠性和清晰度。

> 译自：[Observability by Design: Unlocking Consistency with OpenTelemetry Weaver](https://opentelemetry.io/blog/2025/otel-weaver/)
> 
> 作者：[Laurent Quérel (F5), Jeremy Blythe (Evertz), Josh Suereth (Google), Liudmila Molkova (Microsoft)]

## 为什么一致性很重要：进入语义约定

您是否经历过……

* 由于指标名称更改而破坏现有警报或仪表板的部署？
* 因为团队对同一事物使用不同的指标名称而编写过于复杂的查询？
* 由于缺少或不清楚的检测而导致花费数小时调试生产问题？
* 团队难以解释未记录或不一致的指标？

如果以上任何一点听起来很熟悉，那么您并不孤单。这些是将遥测视为事后才考虑的事情，而不是作为软件设计的有意组成部分的症状。这就是语义约定发挥作用的地方。

**语义约定**是一组遥测数据的规则和标准名称。可以将它们视为指标、追踪和日志的“语法”，以便每个人和所有事物（包括您的工具）都知道您所说的 `http.request.method`、`db.system.name` 或 `http.client.request.duration` 是什么意思。

[OpenTelemetry 语义约定](/docs/specs/semconv/)是一个巨大的开放目录，包含 900 多个属性和信号，分布在 70 多个领域，由 9 个特别兴趣小组维护。这个开放目录确保：

* **一致性**：一个名称，一个含义，无处不在。
* **互操作性**：工具、团队和供应商可以相互理解。
* **自动化**：机器可读的标准支持代码和文档生成、静态和动态合规性检查等等。

但是，跨团队和工具维护和发展这样的注册表并非易事。这就是 [OTel Weaver](https://github.com/open-telemetry/weaver) 的用武之地。

## 通过设计实现可观测性：一种现代工程方法

通过设计实现可观测性意味着从一开始就将可观测性集成到您的软件开发生命周期 (SDLC) 中。这通常被称为“可观测性左移”，因为它将可观测性问题提前（向“左”）移动到开发时间线中——从部署后监控返回到设计和开发阶段：

1. **设定明确的目标**：预先定义可观测性目标。您需要什么信号？
2. **自动化**：使用工具从约定生成代码、文档、测试和模式。
3. **验证**：尽早发现可观测性问题，在 CI/CD 中，而不是在生产中。
4. **迭代**：根据实际反馈和不断变化的需求改进您的遥测。

换句话说，**将遥测视为公共 API**。如果您不会在发布之间破坏应用程序的 API，也不要破坏您的遥测。

## OTel Weaver：增强语义约定和通过设计实现可观测性

**OTel Weaver** 是开源 CLI 和自动化平台，可帮助您管理、验证和发展语义约定和可观测性工作流程。

Weaver 可以为您做什么？

* **定义和版本化您的语义约定**：创建您自己的约定或在 OTel 的基础上构建。与您的团队或社区共享您的模式。
* **基于策略的验证**：强制执行最佳实践——命名、稳定性、不变性等等。检测重大更改并保持质量。您甚至可以定义自己的策略！
* **实时检测检查**：检查您的应用程序的遥测是否与您定义的模式和最佳实践相匹配。测量检测覆盖率，类似于代码覆盖率，以确保您的单元测试和集成测试实际上正在执行所有检测的代码。再也不会错过生产中的关键信号。
* **代码和文档生成**：开箱即用地生成 Markdown 文档和多种编程语言的常量。我们还在研究更高级的解决方案，以自动生成类型安全的检测帮助程序（Go、Rust、…），以便更轻松、更安全地集成。
* **差异和演进**：通过自动差异和升级/降级支持，安全地演进您的遥测模式。

> 定义：注册表是语义约定的集合，这些约定是标准化定义，描述了如何命名和构建指标、日志和追踪等遥测数据。OpenTelemetry 维护官方语义约定注册表，但团队、项目或供应商可以定义和发布自己的自定义注册表以满足特定需求。

Weaver 目前支持多注册表的基本形式，允许自定义注册表导入和覆盖另一个注册表（例如，扩展官方 OTel 语义约定）。目前，仅支持两个级别：您的自定义注册表和单个依赖项。这涵盖了许多常见情况，但我们知道灵活性和协作还有更大的潜力。

## Weaver 的实际应用：关键命令

开始使用 Weaver 非常简单：它可以作为预构建的二进制 CLI（参见[发布](https://github.com/open-telemetry/weaver/releases)页面）和 Docker [镜像](https://hub.docker.com/r/otel/weaver)提供，随时可以放入任何 CI/CD 管道或本地工作流程中。

OTel 语义约定社区依赖 Weaver 作为其构建、验证和发展官方注册表的主要工具。以下是社区使用的一些命令。

**检查官方 OTel 注册表：**

Weaver 确保对注册表的每次更改都是一致的、经过验证的，并且遵循核心策略。

```
weaver registry check -r registry-path

```

以下列表简要概述了为 OTel 注册表实施的策略。

| **属性规则** | **命名和结构** | **稳定性和演进** |
| --- | --- | --- |
| 注册表之外没有属性 | 名称必须遵循格式规则 | 不删除元素 |
| 属性上没有需求级别 | ID 必须与命名模式匹配 | 不降级稳定性 |
| 组中没有重复属性 | 属性必须完全限定 | 不更改类型或单位 |
| 属性集必须是不可变的 | 没有命名空间冲突 | 定义需要稳定性 |
| 稳定组中的实验性属性必须是可选的 | 没有常量名称冲突 | 一旦定义，枚举值不得更改 |

**生成 Markdown 文档：**

Weaver 自动生成您在 opentelemetry.io 上看到的人类可读文档。

```
weaver registry update-markdown -r registry-path --target=markdown

```

**为检测帮助程序生成代码：**

每个受支持的 OpenTelemetry SDK 都受益于其本机语言的自动生成的常量和代码，确保没有拼写错误或不一致之处。

例如，可以在此 [存储库](https://github.com/open-telemetry/opentelemetry-go/tree/main/semconv) 中找到从 Weaver 为 Go 客户端 SDK 生成的代码。使用的 Weaver 命令如下所示：

```
weaver registry generate -r registry-path -t templates-root-dir go

```

类似地，可以在此 [项目](https://github.com/open-telemetry/semantic-conventions-java) 中看到为 Java 库的 OpenTelemetry 语义约定生成的代码。Weaver 提供了一个与 Jinja2 兼容的嵌入式模板系统，具有大量自定义函数，以方便使用不同语言生成代码。

**跟踪更改和模式演进：**

Weaver 跟踪注册表版本之间的差异，以突出显示重大更改或改进。

```
weaver registry diff -r current-version-registry-path --baseline-registry previous-version-registry-path

```

**实时检测检查和覆盖率：**

用户和维护人员可以利用 Weaver [实时检查](https://github.com/open-telemetry/weaver/tree/main/crates/weaver_live_check#readme)他们的应用程序是否正确发出符合官方语义约定或自定义注册表的遥测（见下文）。

```
weaver registry live-check --registry registry-path

```

此命令生成应用程序针对注册表发出的信号的合规性报告。

![实时检查报告](https://opentelemetry.io/blog/2025/otel-weaver/live-check.png)

Weaver `live-check` 不仅可用于验证您的应用程序是否符合语义约定，还可以应用于您链接到的所有库，直接在您的 CI/CD 工作流程中！除了基本模型合规性之外，自定义 Rego 策略还支持组织特定的不变性和最佳实践检查。每个属性和信号在接收时都会通过策略引擎传递。例如，您可以定义一个指标值的范围策略，或者某个特定属性的字符串值与某个正则表达式匹配。这些策略独立于语义约定注册表，因此您可以根据需要定义应用程序或库特定的检查。

**使用 `weaver emit` 模拟遥测**

检测您的代码和构建仪表板通常发生在不同的时间，有时由不同的人员完成。这会减慢您的可观测性工作：在应用程序在暂存或生产环境中发出真实数据之前，前端和 SRE 团队无法构建有用的仪表板或警报。Weaver 使用 `emit` 命令解决了这个先有鸡还是先有蛋的问题。

```
weaver registry emit --registry registry-path --endpoint http://localhost:4317

```

此命令生成 OTLP 格式的示例遥测，您可以将其直接发送到您的收集器、后端或可视化工具。

### 自定义注册表：定义和检查您自己的遥测模式

虽然 Weaver 为核心 OTel 注册表提供支持，但您也可以使用它来定义和管理您自己的应用程序的遥测模式。这意味着您可以重用和扩展官方约定，同时添加针对您的领域定制的自定义信号、属性和事件，并且您可以静态和实时检查您的应用程序的遥测是否是最新的和完整的。

> 注意：我们正在积极努力使自定义注册表更容易使用，具有更好的入门体验、更简单的配置以及更集成的代码生成和文档支持。我们正在寻找这方面的反馈和帮助。

为了帮助您入门，这里有一个使用“ToDo”应用程序的自定义注册表的快速示例。首先，创建一个 `registry_manifest.yaml` 文件来指定您的注册表：

```yaml
name: todo_app
description: OTel signals for my native ToDo app
semconv_version: 0.1.0
dependencies:
  - name: otel
    registry_path: https://github.com/open-telemetry/semantic-conventions/archive/refs/tags/v1.34.0.zip[model]
```

导入和扩展现有约定，并定义您自己的信号和属性：

```yaml
imports: # import signals from the dependency registry, i.e. OTel semantic conventions
  metrics:
    - db.client.* # import all metrics with names starting with `db.client.`
  events:
    - app.*
    - exception # import the event named `exception`
  entities:
    - host
    - host.cpu

groups:
  - id: metric.todo.completion_time
    type: metric
    brief: Measures the time between the creation and completion of a ToDo item.
    metric_name: todo.completion_time
    instrument: histogram
    unit: s
    attributes:
      - id: todo.priority # define your own attribute
        type: string
        brief: The priority of the ToDo item.
      - id: todo.category
        type: string
        brief: The category of the ToDo item.
      - ref: user.id # reference an existing attribute from the imported registry
        requirement_level: required # refine the requirement level
    entity_associations:
      - os.name
      - os.version
  - id: event.todo.deleted
    type: event
    brief: Emitted whenever a ToDo item is deleted by the user.
    attributes:
      - id: delete.reason
        type: string
        brief: The reason for deletion.
      - id: todo.priority
        type: string
        brief: The priority of the deleted ToDo item.
      - ref: user.id
        requirement_level: required
    entity_associations:
      - os.name
      - os.version
```

## Weaver 的下一步是什么？

我们正在努力使 Weaver 更加强大、灵活和易于采用：

* **更好的文档和更简单的入门体验**：期待更多动手示例、分步指南，并更加注重易用性。我们还在创建为自定义注册表量身定制的模板和策略。
* **多注册表支持**：增强对组合、分层和管理多个语义约定注册表的支持，包括冲突解决。这也将使库作者能够轻松发布和共享他们自己的注册表。
* **模式 v2**：一组新命令，用于打包和发布应用程序和库的已解析的、独立的遥测模式。这种标准化工作（遥测模式 v2）将使整个可观测性生态系统更容易在语义约定和 Weaver 的基础上构建。
* **类型安全的语义约定 API 生成**：自动生成强类型检测库，以减少错误并加速开发。用于 Prometheus 的 Go 类型安全客户端 API 示例已在 [promconv](https://github.com/sh0rez/promconv/tree/main) 中进行。还在 [MrAlias/semconv-go](https://github.com/MrAlias/semconv-go) 中开发使用 Weaver 的更通用的 Go 类型安全客户端 API。

请继续关注，下一代语义约定管理即将到来，Weaver 将使整个社区无缝衔接。

## 参与进来！

Weaver 被设计为高度可扩展和可配置。您可以使用 Weaver 的内置引擎创建自定义注册表、使用 Rego 编写策略以及使用 Jinja2 设计模板。如果您想开始使用或有疑问，请加入 Slack 上的 [#otel-weaver](https://cloud-native.slack.com/archives/C0697EXNTL3)。我们很乐意提供帮助，并且始终对您的想法感兴趣！

> 可观测性不仅仅是一个工具，而是一种实践。通过设计构建它，通过 OpenTelemetry Weaver 提供支持的清晰、一致和自动化的工作流程。