<!--
title: 关键应用深陷黑盒？5分钟重见光明！
cover: https://opentelemetry.io/img/social/logo-wordmark-001.png
summary: 本文介绍了如何使用 OpenTelemetry 在不修改代码的情况下，对遗留应用程序进行监控。通过配置 Java agent，可以获取 CPU、内存使用情况等基础指标，以及交易延迟、吞吐量、错误率等业务 KPI，从而实现对黑盒系统的可观测性，为决策提供数据支持。
-->

本文介绍了如何使用 OpenTelemetry 在不修改代码的情况下，对遗留应用程序进行监控。通过配置 Java agent，可以获取 CPU、内存使用情况等基础指标，以及交易延迟、吞吐量、错误率等业务 KPI，从而实现对黑盒系统的可观测性，为决策提供数据支持。

> 译自：[Your Critical Legacy App is a Black Box? Let's Change That in 5 Minutes!](https://opentelemetry.io/blog/2025/opentelemetry-for-legacy-app/)
> 
> 作者：Lukasz Ciukaj

几乎在每个老牌企业中，都存在着“那一个”系统。它运行在角落里，多年来执行着关键功能。它很可靠，但也是一个完全的黑盒。没有人想碰它，唯恐弄坏它，而且最初的开发人员早已离开。它可能是一个 90 年代的核心银行账本、仓库中的物流路由引擎，或者是工厂车间的数据聚合器。你知道它在工作，因为，嗯，它还没有出故障……至少现在还没有。

最终目标是明确的：我们需要重写或迁移此应用程序到一个现代、可扩展且可支持的平台。但是这样的项目需要数月甚至数年的时间。在此期间我们该怎么办？我们不能在黑暗中操作。

虽然 OpenTelemetry 经常因其在现代云原生架构中的作用而受到赞扬，但它的价值并不止于此。事实上，它为那些非云原生的系统提供了一个强大且经常被忽视的解决方案。它充当了现代化的桥梁。通过让我们今天对遗留应用程序有一些可观测性，我们可以降低其运营风险，规划其替代方案，并为它的未来构建数据驱动的商业案例。让我们通过一个模拟的遗留应用程序来演练如何做到这一点，所有这些都不需要更改其任何一行代码。

## OpenTelemetry：用于遗留代码的现代可观测性

为了模拟一个常见的遗留模式，我们构建了一个简单的应用程序。一个用 C 编写的核心可执行文件（模拟系统级进程）启动一个 Java 虚拟机 (JVM) 来处理特定的任务，例如处理事务或记录。

流程是：

```
C 应用程序 (legacy_app) -> 启动 JVM -> 调用 Java 方法来处理任务

```

当我们运行 ./legacy\_app 时，它可以工作。但我们无法回答关键问题：它是否能满足业务需求？它是否即将耗尽内存并在一天结束处理期间崩溃？此应用程序中的速度减慢是否是上周客户投诉的根本原因？

让我们来看看。

### 阶段 1：基本健康监控（系统是否稳定？）

我们的首要目标是监控我们应用程序的重要指标。我们需要查看它的 CPU 和内存使用情况，以确保它不会发生故障。我们可以通过使用 OpenTelemetry Java agent，简单地使用 JVM 启动参数中的 `-javaagent` 标志将其附加到应用程序来实现这一点。在我们的示例中，我们可以使用 `_JAVA_OPTIONS` 环境变量来做到这一点。

#### 步骤 1：设置环境

在我们的终端中，我们将配置 agent，而无需接触应用程序本身。

```
# --- 第 1 部分：基本系统健康状况配置 ---

# 1. 给我们的服务起一个描述性的名称
export OTEL_SERVICE_NAME=legacy-part-processor

# 2. 仅启用指标导出器
export OTEL_METRICS_EXPORTER=otlp

# 3. 将 agent 指向收集器的 gRPC 端点
export OTEL_EXPORTER_OTLP_ENDPOINT=http://127.0.0.1:4317

# 4. 指定 OTLP 协议
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc

# 5. 为 Java 8 启用运行时指标
export OTEL_INSTRUMENTATION_RUNTIME_TELEMETRY_JAVA8_ENABLED=true

# 6. 附加 OpenTelemetry Java agent
export _JAVA_OPTIONS="-javaagent:./opentelemetry-javaagent.jar"

```

#### 步骤 2：运行未修改的应用程序并确认它正在工作

首先，让我们验证我们的遗留应用程序是否正在运行。快速查看终端日志显示稳定的消息流，确认我们的进程运行良好：

```
[C Wrapper] Reading new Part ID from assembly line: 3035
[Java Processor] Received Part ID 3035. Fetching processing parameters...
[Java Processor] Part ID 3035 processed successfully.
[C Wrapper] Processing request for Part ID 3035 completed successfully.

[C Wrapper] Reading new Part ID from assembly line: 3036
[Java Processor] Received Part ID 3036. Fetching processing parameters...
[Java Processor] Part ID 3036 processed successfully.
[C Wrapper] Processing request for Part ID 3036 completed successfully.

[C Wrapper] Reading new Part ID from assembly line: 3037
[Java Processor] Received Part ID 3037. Fetching processing parameters...
[Java Processor] Part ID 3037 processed successfully.
[C Wrapper] Processing request for Part ID 3037 completed successfully.

```

我们应用程序中的数据遵循标准路径：OTel agent 将指标发送到 OpenTelemetry Collector，然后 Prometheus 会抓取这些指标以进行存储。然后我们使用 Grafana 连接到 Prometheus 并可视化数据。由于这是一个常见且有据可查的设置，我们将跳过具体的配置文件，直接进入这种可见性允许我们看到的内容。

#### 步骤 3：构建基本监控仪表板

这是所有工作汇集在一起的时刻。我们现在可以前往 Grafana，只需三个简单的查询，即可立即构建我们的第一个仪表板。就这样，我们对应用程序进行了基本监控，涵盖了平均 CPU 利用率、平均内存消耗以及垃圾回收所花费的时间。

![基本监控仪表板](/blog/2025/opentelemetry-for-legacy-app/basic-monitoring.png)

结果：我们遗留应用程序的基础健康指标！

通过这一个简单的更改，我们建立了一个可观测性的基础层。关键的 JVM 指标立即开始流向我们的后端，提供回答关键运营问题所需的数据：

* 内存使用情况：我们的应用程序是否正在泄漏内存？它是否会在业务高峰时段崩溃？
* CPU 负载：该进程是否在高流量期间滞后？
* 垃圾回收：应用程序中频繁的“暂停”是否导致其他服务中的级联超时？

我们已经从一个完全的黑盒转变为拥有一个实时的健康仪表板。

### 阶段 2：性能指标（系统是否高效？）

健康是一回事，但性能是另一回事。在查看代码后，我们可以看到我们应用程序的核心逻辑位于 processTransaction() 方法中。但静态代码无法回答动态问题。在实际负载下，执行此操作需要多长时间？它是否是一个瓶颈？

#### 步骤 1：更新环境

我们添加了一些环境变量来告诉 agent 专门测量此方法。对于无法修改应用程序源代码的情况，OpenTelemetry 的 Java agent 提供了一个强大的解决方案：[otel.instrumentation.methods.include](/docs/zero-code/java/agent/annotations/#creating-spans-around-methods-with-otelinstrumentationmethodsinclude)。此设置允许您指示 agent 自动围绕特定方法创建 span。

```
# --- 第 2 部分：应用程序性能配置 ---

# 1. 启用追踪导出器
export OTEL_TRACES_EXPORTER=otlp

# 2. 告诉 agent 要检测哪个方法
export OTEL_INSTRUMENTATION_METHODS_INCLUDE="LegacyJavaProcessor[processData]"

```

#### 步骤 2：运行应用程序并修改现有仪表板

我们现在收集的追踪 span 是构建更丰富的仪表板的原始材料。我们的 OTel Collector 配置为分析这些 span 并生成应用程序监控的“黄金信号”。让我们回到 Grafana 并为我们的三个核心指标添加图表：每分钟调用次数、平均响应时间和每分钟错误次数。

![扩展监控仪表板](/blog/2025/opentelemetry-for-legacy-app/extended-monitoring.png)

结果：我们遗留应用程序的核心业务 KPI！

OpenTelemetry agent 现在测量每一笔交易。使用带有 spanmetrics 连接器的 OTel Collector，我们可以获得关键的性能指标：

* 延迟（处理时间）：我们终于知道处理一笔交易需要多长时间。它是否足够快？我们是否达到了我们的 SLO？
* 吞吐量（每分钟调用次数）：我们可以看到我们每分钟处理的交易数量。我们的系统是否能满足需求？它可以处理峰值负载吗？
* 错误率（工作质量）：我们现在可以跟踪我们业务逻辑本身的健康状况。我们的失败率是多少？我们能否在问题升级之前发现它们？

### 总结和行动号召

有时，即使有限的可见性也远胜于完全盲目地飞行。通过仅使用几个环境变量和 OpenTelemetry agent 来检测您的遗留黑盒，您无需进行有风险的代码更改或昂贵的全面检查即可获得可操作的见解。这不仅仅是一次技术上的胜利，更是一个具有战略意义的进步。有了真实的数据，您就可以做出更明智的决策，主动解决潜在问题，并在规划未来时建立信心。

即使您的最初直觉是您的应用程序过于老旧而无法从 OpenTelemetry 中受益，也始终值得验证您的技术栈。通常，有一种方法可以对其进行检测，即使无需修改任何代码。生态系统在不断发展，许多框架和平台现在都支持基于 agent 或 sidecar 的检测，使得从最旧的系统中提取有价值的遥测数据比以往任何时候都更容易。

请记住：今天获得的每一丝可见性都为您争取了时间、弹性和安心，直到您的现代化之旅完成。