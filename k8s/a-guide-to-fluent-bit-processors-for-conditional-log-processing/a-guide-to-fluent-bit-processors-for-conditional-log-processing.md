<!--
title: Fluent Bit 处理器：条件日志处理权威指南
cover: https://cdn.thenewstack.io/media/2025/09/e10c186a-processors.png
summary: Fluent Bit 4.0 引入了处理器条件日志处理功能。处理器与输入紧密耦合，能依据日志内容选择性地修改数据。这使得根据特定条件，如错误级别，自动添加标签等操作成为可能，提升日志处理的灵活性和效率。
-->

Fluent Bit 4.0 引入了处理器条件日志处理功能。处理器与输入紧密耦合，能依据日志内容选择性地修改数据。这使得根据特定条件，如错误级别，自动添加标签等操作成为可能，提升日志处理的灵活性和效率。

> 译自：[A Guide To Fluent Bit Processors for Conditional Log Processing](https://thenewstack.io/a-guide-to-fluent-bit-processors-for-conditional-log-processing/)
> 
> 作者：Sharad Regoti

[Fluent Bit](https://docs.fluentbit.io/manual) 是一个广泛使用的开源数据收集代理、处理器和转发器，它可以让您从各种来源收集日志、指标和追踪，对其进行过滤和转换，然后转发到多个目的地。

Fluent Bit 2 版本引入了[处理器](https://docs.fluentbit.io/manual/data-pipeline/processors)的概念，它们与过滤器类似，用于丰富或转换遥测数据。

随着 [Fluent Bit 4 版本](https://fluentbit.io/announcements/v4.0.0/)的发布，一项新功能被引入：使用处理器进行条件日志处理。在这篇文章中，我们将探讨如何使用 Fluent Bit 处理器根据日志内容有条件地修改日志。

[![](https://cdn.thenewstack.io/media/2025/09/04a39236-image2-1024x187.png)](https://cdn.thenewstack.io/media/2025/09/04a39236-image2-1024x187.png)

## 先决条件

*   **Docker：** 已安装在您的系统上。
*   **熟悉 Fluent Bit 概念：** 例如输入（inputs）、输出（outputs）、解析器（parsers）和过滤器（filters）。如果您不熟悉这些概念，请参考[官方文档](https://docs.fluentbit.io/manual/concepts/data-pipeline)。

## 什么是处理器？

处理器是当数据流经 Fluent Bit 时，用于修改、转换或增强数据的组件。与[过滤器](https://docs.fluentbit.io/manual/data-pipeline/filters)不同，处理器与输入紧密耦合，这意味着它们会立即执行，避免造成性能瓶颈。

### 处理器与过滤器有何不同？

虽然处理器和过滤器都可以操作数据，但它们之间存在关键差异：

1.  **执行点：** 处理器与输入紧密耦合并立即执行，而过滤器则在[独立的管道阶段](https://thenewstack.io/the-case-for-telemetry-pipelines/)运行。
2.  **性能影响：** 处理器避免创建瓶颈，因为它们不需要在阶段之间进行缓冲。
3.  **配置：** 处理器仅支持 YAML 配置格式。
4.  **范围：** 过滤器可以模仿处理器实现，反之则不行。

### 使用处理器进行条件日志处理

条件处理使您能够根据日志中字段的值选择性地将处理器应用于日志。这使您能够创建仅处理符合特定条件的记录的管道，而忽略其余记录。

您可以通过在处理器的 YAML 配置设置中添加 `condition` 块，将标准处理器转换为条件处理器。这些 `condition` 块使用以下语法：

```
pipeline:
  inputs:
    <...>
  processors:
    logs:
      - name: processor_name
        <...>
        condition:
          op: {and|or}
          rules:
          - field: {field_name1}
            op: {comparison_operator}
            value: {comparison_value1}
          - field: {field_name2}
            op: {comparison_operator}
            value: {comparison_value2}
        <...>
```

### 条件评估

`condition.op` 参数指定条件的评估逻辑。它可以具有以下值之一：

*   **and：** 当 `condition.rules` 数组中的所有规则都为[真值](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)时，日志条目符合此条件。
*   **or：** 当 `condition.rules` 数组中有一个或多个规则为[真值](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)时，日志条目符合此条件。

### 规则

`condition.rules` 数组中的每个项都必须包含以下参数的值：

| **参数** | **描述** |
| --- | --- |
| field | 要评估的[日志字段](https://thenewstack.io/how-to-evaluate-logging-frameworks-10-questions/)。此参数的值必须使用[正确的语法](https://docs.google.com/document/d/1z-QFhd0u4kkAReNDHnUH1iTXaCOFUMJcTbFHXlHhV9w/edit#field-access)来访问日志中的字段。 |
| op | [比较运算符](https://docs.google.com/document/d/1z-QFhd0u4kkAReNDHnUH1iTXaCOFUMJcTbFHXlHhV9w/edit#comparison-operators)，用于评估规则是否为真。此参数 (`condition.rules.op`) 与 `condition.op` 参数不同，并且具有不同的可能值。 |
| value | 指定日志字段的值，用于比较。您可以选择提供一个[包含多个值的数组](https://docs.google.com/document/d/1z-QFhd0u4kkAReNDHnUH1iTXaCOFUMJcTbFHXlHhV9w/edit#array-of-values)。 |

规则将针对流经数据管道的每条日志进行评估。

## 我们的用例

为了演示，我们将实现一个常见场景：

目标：自动为错误级别日志添加 `priority=high` 标签，以便下游进行特殊处理。

这对于以下方面很有价值：

*   为关键错误触发即时警报。
*   将高优先级日志路由到专用分析系统。
*   确保错误日志的保留时间长于常规日志。

## 

## 操作指南

### **1. 创建 Fluent Bit 目录**

```
mkdir fluent-bit-conditional-demo

cd fluent-bit-conditional-demo
```

### **2. 创建输入日志文件**

创建 `input.log` 文件，内容如下：

```
{"timestamp": "2023-10-15T10:30:00", "level": "info", "message": "User login successful", "user_id": 1001}

{"timestamp": "2023-10-15T10:31:00", "level": "warn", "message": "High CPU usage detected", "cpu": 85}

{"timestamp": "2023-10-15T10:32:00", "level": "error", "message": "Database connection failed", "service": "payment"}

{"timestamp": "2023-10-15T10:33:00", "level": "info", "message": "API request completed", "endpoint": "/api/v1/users"}

{"timestamp": "2023-10-15T10:34:00", "level": "error", "message": "Authentication failed", "user_ip": "192.168.1.105"}

{"timestamp": "2023-10-15T10:30:00", "level": "info", "message": "User login successful", "user_id": 2001}
```

### **3. 创建配置**

创建 `fluent-bit.yaml` 文件，内容如下：

```
service:
  flush: 1
  log_level: info
  parsers_file: parsers.yaml

parsers:
  - name: my_json_parser
    format: json
    time_key: time
    time_format: '%Y-%m-%dT%H:%M:%S.%L%z'
    time_keep: true

pipeline:
  inputs:
    - name: tail
      tag: log.test
      path: /test/input.log
      read_from_head: true
      parser: my_json_parser

      # Apply processor to the input
      processors:
        logs:
          - name: content_modifier
            condition:
              op: and
              rules:
                - field: "$level"
                  op: eq
                  value: "error"
            action: insert
            key: priority
            value: high

  outputs:
    - name: stdout
      match: '*'
```

在上述配置中，我们设置了一个管道，它从文件中读取日志条目，将其解析为 JSON，并将其打印到标准输出 (STDOUT)。

在输入部分，`tail` 插件从 `/test/input.log` 文件读取日志，并为每条记录添加 `log.test` 标签。然后，`content_modifier` 处理器检查每个已解析的记录，如果日志级别匹配 `error`，则添加一个新的 priority 字段。最后，所有处理过的日志都路由到标准输出。

### **4. 运行容器**

```
docker run \
  -v $(pwd)/input.log:/test/input.log \
  -v $(pwd)/fluent-bit.yaml:/fluent-bit/etc/fluent-bit.yaml \
  -ti cr.fluentbit.io/fluent/fluent-bit:4.0.8 \
  /fluent-bit/bin/fluent-bit \
  -c /fluent-bit/etc/fluent-bit.yaml
```

### **5. 验证输出**

您应该看到类似于以下内容的输出：

```
[0] log.test: [[1756973650.919511219, {}], {"timestamp"=>"2023-10-15T10:30:00", "level"=>"info", "message"=>"User login successful", "user_id"=>1001}]

[1] log.test: [[1756973650.919514469, {}], {"timestamp"=>"2023-10-15T10:31:00", "level"=>"warn", "message"=>"High CPU usage detected", "cpu"=>85}]

[2] log.test: [[1756973650.919515761, {}], {"timestamp"=>"2023-10-15T10:32:00", "level"=>"error", "message"=>"Database connection failed", "service"=>"payment", "priority"=>"high"}]

[3] log.test: [[1756973650.919516677, {}], {"timestamp"=>"2023-10-15T10:33:00", "level"=>"info", "message"=>"API request completed", "endpoint"=>"/api/v1/users"}]

[4] log.test: [[1756973650.919517636, {}], {"timestamp"=>"2023-10-15T10:34:00", "level"=>"error", "message"=>"Authentication failed", "user_ip"=>"192.168.1.105", "priority"=>"high"}]

[5] log.test: [[1756973650.919518552, {}], {"timestamp"=>"2023-10-15T10:30:00", "level"=>"info", "message"=>"User login successful", "user_id"=>2001}]
```

请注意，只有错误日志（条目 2 和 4）添加了 `priority: high` 字段。

## 结论

[Fluent Bit 的条件处理功能提供了一种强大的方式](https://thenewstack.io/how-to-deploy-fluent-bit-in-a-kubernetes-native-way/)，可以根据日志内容选择性地修改日志。这使得更复杂的日志处理管道成为可能，您可以：

1.  对不同类型的日志应用不同的处理规则。
2.  为特定日志类别添加上下文信息。
3.  根据日志内容创建更智能的路由决策。

通过应用本指南中演示的技术，[您可以构建更复杂的日志处理管道](https://thenewstack.io/using-logging-frameworks-for-application-development/)，以满足您的应用程序和基础设施的独特需求。