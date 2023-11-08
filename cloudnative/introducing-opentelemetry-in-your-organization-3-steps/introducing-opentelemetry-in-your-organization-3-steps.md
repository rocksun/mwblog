<!-- 
# 在组织内推广OpenTelemetry？
https://cdn.thenewstack.io/media/2023/11/a444dc72-telescope-observability-opentelemetry-1024x666.jpg
-->

使用 OpenTelemetry 实现可观测性不仅仅是技术问题。了解成功推广的最佳实践非常重要。

译自 [Introducing OpenTelemetry in Your Organization: 3 Steps](https://thenewstack.io/introducing-opentelemetry-in-your-organization-3-steps/) 。

为了在组织内引入基于 OpenTelemetry 的可观测性，需要制定推广策略，确保各团队遵循统一方案，避免实施分散。推广 OpenTelemetry 可分三步走:

* 沟通
* 做足前期准备
* 逐步检测接入

## 1. 沟通

如果不积极告知组织内各部门，他们就不会知道要使用 OpenTelemetry。因此，传播宣传尤为重要。

### 阐明 OpenTelemetry 的优势

首先要向组织内员工宣传 OpenTelemetry 的诸多好处，让他们明确采用的动机。主要优点包括:

1.  **无供应商锁定:** 如果对当前的可观测性供应商感到不满，可以轻松切换到其他供应商，无需重新检测代码。    
2.  **供应商中立:** 由于 OpenTelemetry 具有供应商中立性，可以同时轻松地向多个后端发送遥测数据。这让我们可以同时试用不同可观测性供应商，比较选择最合适的。
3.  **社区活跃:** OpenTelemetry 是 [CNCF](https://cncf.io/?utm_content=inline-mention) 项目中仅次于 Kubernetes 的[第二大活跃项目](https://www.cncf.io/blog/2023/01/11/a-look-at-the-2022-velocity-of-cncf-linux-foundation-and-top-30-open-source-projects/)。
4.  **标准化:** OpenTelemetry 是一个业内主要供应商都支持的标准化框架，已成为事实标准，必将长期存在!它也使我们可以关联所有的三种关键遥测信号:traces、metrics 和 logs，这是之前做不到的。

### 宣布意图

在全组织推广 OpenTelemetry 是一项重大举措。公开宣布将采用 OpenTelemetry，尤其是此类决策来自高层，可以让组织成员知道这绝非空话。可以通过 Slack、Teams 或组织内其他协作工具，以及组织层面的大会进行宣布。

但人们不希望仅被告知要做什么。转型疲劳是真实存在的，因此还必须......

### 详细解释 OpenTelemetry 的相关知识

如果要让人们支持这一举措，他们需要知道具体会涉及到什么。可以由组织内对可观测性比较了解的工程师来解释 OpenTelemetry 的知识点和好处。

召集对 OpenTelemetry 感兴趣的员工，让他们成为推广的领军人物，可以考虑组建可观测性实践小组。该小组可以负责宣传、制定 OpenTelemetry 推广和实现细节，成为 OpenTelemetry 主题专家。小组需要包含可以深入研究 OpenTelemetry、制定内部最佳实践、并成为 OpenTelemetry 相关问题答疑的工程师，同时也邀请个人贡献者和管理者加入。不一定需要现成的 OpenTelemetry 专家；他们可以在推广中成长。最重要的是他们对 OpenTelemetry 有兴趣并愿意推广。

此外，还应与组织外的人交流，学习[其他组织的 OpenTelemetry 推广经验](https://www.youtube.com/playlist?list=PLVYDBkQ1TdyxeQveOb8HdCrTg1JmRPDaH)。可以加入 [CNCF Slack 上的 OpenTelemetry 最终用户工作组(EUWG)](https://opentelemetry.io/community/end-user/slack-channel/)，与 OpenTelemetry 从业者交流经验。他们中的一些人可能愿意与内部工程师进行交流，解答问题。另外，我是该工作组的联合主席之一，可以帮助建立联系！

### 制定计划

要展示对 OpenTelemetry 项目的承诺，需要制定明确的推广计划，并设定不同阶段的时间表和里程碑。在制定时间表时，一定要征求工程师和管理者的意见，确保时间表合理可行。让他们与可观测性实践小组合作，制定好计划后进行沟通宣导。

在计划过程中，可询问工程师以下问题:

1. 系统中最关键的业务路径是哪些？
2. 排查问题时，哪些信息对你最重要？
3. 我们如何帮助你采用 OpenTelemetry？

## 2. 做好功课

要准确制定计划，就需要先了解系统的情况。

### 代码清单

应用程序代码可能包含多个服务，需要逐个清点每个服务使用的语言，以便确定开发团队需要使用的 OpenTelemetry instrumentation 库。

同时还要清点正在使用的所有第三方框架和库(如 Python Django、Java Hibernate)，因为很多流行库和框架都已支持 OpenTelemetry 的自动 instrumentation 。

最后，要确定自研的框架和库，这方面后文会详述。

### 找出最关键的高价值交易

接下来需要更深入地分析，找到最关键的业务交易。应该先对它们进行 instrument ，[因为 OpenTelemetry 联合创始人兼 Lightstep 开发者教育总监 Ted Young 说过](https://gist.github.com/AnaMMedina21/a68903bf06a09bc9795c694c3dcc4ce2): “这可以确保生成完整的链路追踪，可以尽早开始调查重要问题，无需等待整个组织完成迁移。”

### 查明已 Instrumented 的应用代码

如果任何代码已经接入了 Instrumented ，要了解它是否使用的是 [OpenCensus](https://opencensus.io/)、[OpenTracing](https://opentracing.io/) 还是其他。OpenTelemetry [向后兼容](https://opentelemetry.io/docs/specs/otel/compatibility/opencensus/) OpenTracing 和 OpenCensus，所以最初不需要做重大代码修改。但是后续还是要逐步迁移到 OpenTelemetry，以获得全部功能。例如，OpenCensus 和 OpenTracing 不支持日志和指标，也不支持追踪、指标、日志之间的集成。如果使用了自研库或框架，要准备用 OpenTelemetry 重新检测应用程序。

### 确定指标来源

除了应用程序的追踪数据，还需要向后端发送指标数据，以获得整个系统的全景视图。这意味着需要确定指标的来源，是 Kubernetes、Kafka、Docker、Nomad、虚拟机还是其他？同时要考虑需要捕获哪些应用程序指标。

## 3. Instrument

做好以上准备后，就可以开始使用 OpenTelemetry 进行 Instrument 了。这里介绍一些推荐的 Instrument 实践，帮助各团队入门:

### 可能需要暂缓开发某些应用功能

如果系统经常出现可靠性问题，通常意味着需要提升可观测性。因此，可能需要推迟某些计划中的功能，先 Instrument 代码或重新评估已有 Instrument。

### 如果可能，从自动 Instrumentation 开始

如果使用的语言[支持自动 Instrumentation](https://opentelemetry.io/docs/concepts/instrumentation/automatic/)，应积极采用，这是使用 OpenTelemetry 的低门槛方式，投入少但收益大。Java、.NET、Python、JavaScript 和 PHP 目前都已支持自动 Instrumentation，Go 也提供了[自动 Instrumentation](https://opentelemetry.io/docs/instrumentation/go/libraries/) ，但方式稍有不同。

### 考虑自研库和框架

最终还需通过手动 instrumentation 来补充自动 instrumentation。所以要关注自研库和框架的 instrumentation，因为代码中的很大一部分会接触到这些库和框架，这可以覆盖所需的大部分链路追踪。

### 不要检测一切

[过度 instrumentation](https://youtu.be/wMJEgrUnX7M?si=WZlHDuKhRG2eCG3Q) 会产生大量无关数据，导致难以调试。这通常来自自动 instrumentation。所以自动 instrumentation 后，要审视一下哪些被自动 instrumentation 的库确实需要收集 instrumentation 数据。幸运的是，Java 和 Python 等语言提供了限制自动 instrumentation 范围的方式。

### 编码时 Instrument

测试驱动开发(TDD)是在编写应用代码时同步编写测试，可观测驱动开发(ODD)就是在编写应用代码过程中同步添加 Instrument 代码。编码时 Instrument，可以清楚知道需要 Instrument 什么，因为代码还记忆犹新，也可以避免可观测性导致的技术债务。

### Instrument 自己的代码

应用团队应该 Instrument 自己的代码，不该依赖外部团队 Instrument，因为他们最了解自己的代码，每天工作在其上，知道调试时应关注什么。即使时间紧迫，也不应让第三方 Instrument 应用代码，结果不会好。

### 部署至少一个收集器实例

虽然可以直接从 Instrument 代码向后端发送遥测数据，但应该使用至少一个 OpenTelemetry 收集器。它可以从多个数据源收集和处理数据，再导出到首选的后端分析。如果要切换后端，通过简单更新收集器的 YAML 配置，可以同时发送数据到多个后端进行比较选取。选择后端之后，只需在收集器中更改 YAML。

## 最后的思考

在组织内推广 OpenTelemetry 非易事，但有明确的入门指导会大有裨益。请记住进行沟通宣导、做好前期准备并遵循 Instrument 实践。如果遇到困难，我们随时准备提供帮助！