<!--
title: 日志框架评估：10个问题
cover: https://cdn.thenewstack.io/media/2025/08/6002bbaa-framework12.jpg
summary: 本文讨论了选择日志记录框架时应考虑的因素，例如附加器、定制性、易用性、安全性、性能影响等，并提供了一系列问题以帮助评估需求和框架。还提到了Fluentd等工具的集成。
-->

本文讨论了选择日志记录框架时应考虑的因素，例如附加器、定制性、易用性、安全性、性能影响等，并提供了一系列问题以帮助评估需求和框架。还提到了Fluentd等工具的集成。

> 译自：[How to Evaluate Logging Frameworks: 10 Questions](https://thenewstack.io/how-to-evaluate-logging-frameworks-10-questions/)
> 
> 作者：Phil Wilkins

*编者注：本文节选自 Manning 出版的书籍 “[日志记录最佳实践：云原生日志记录实用指南](https://chronosphere.io/resource/logging-best-practices/)”。本书提供了您需要的实用框架，可将日志记录从被动的调试工具转变为主动的竞争优势，您可以下载该书以完整阅读。*

*另请阅读：*

日志记录框架的数量非常多，大多数语言都具有原生能力和开源框架。除了日志记录框架之外，一些库还提供程序化接口以及 API 与几个不同的流行框架之间的映射。

熟悉 Log4J 的人可能听说过 [SL4J](http://www.slf4j.org?utm_source=sponsored-content&utm_id=TNS)，它抽象了 Log4J、Java 原生日志记录框架和另一个名为 Logback 的框架。因此，可以透明地切换日志记录框架。有了这些抽象，就需要一种实例化所需日志记录框架的方法。这可以通过实现[工厂](http://mng.bz/KB00?utm_source=sponsored-content&utm_id=TNS)或[依赖注入](http://mng.bz/DxZw?utm_source=sponsored-content&utm_id=TNS)模式来实现。这种抽象的另一个例子是 [.NET 原生日志记录](http://mng.bz/9KV1?utm_source=sponsored-content&utm_id=TNS)。

## 选择框架

在评估要采用的日志记录框架时，应考虑一些[事项](https://chronosphere.io/learn/controlling-log-volume/?utm_source=sponsored-content&utm_id=TNS)，以帮助选择最合适的框架。我们开发了一系列问题，这些问题将帮助您评估您的需求并选择满足这些需求的框架。审查这些问题将帮助您确定日志记录框架方面的优先级。

一旦对这些问题进行了某种形式的优先级排序，就可以更轻松地根据这些问题评估框架，以了解它们与您的需求的匹配程度。 这些问题如下：

1. 有哪些附加器可用？ 它们是否仅限于一种类型的附加器，例如文件？ 是否有可以与您的日志统一解决方案（例如 Fluentd 或 Logstash）配合使用的开箱即用的附加器？
2. 可以定制或优化附加器的行为吗？ 例如，日志轮换或网络端口和地址是否可配置？
3. 是否可以根据应用程序的不同部分定制日志事件的输出？ 例如，应用程序框架（例如 Spring 或 .NET Core）的日志阈值设置为“`Warning`”和“`Error`”，但您的自定义逻辑可以将阈值设置为“`Info`”。
4. 定制日志记录配置有多容易（不使用代码）？ 您可能希望调整日志记录，并且如果存在操作问题，您最好更新或覆盖默认日志记录配置以选择性地获取更多信息。
5. 框架为您派生多少信息（例如，为跟踪点提供方法和类名）以及正确结构的 时间戳？
6. 您可以定制 [日志输出格式](https://chronosphere.io/learn/what-is-log-file-and-log-data/?utm_source=sponsored-content&utm_id=TNS)（JSON、XML）吗？ 最好的日志具有允许日志事件既可由人读取又可由机器读取的结构。
7. 占用空间有多紧凑？ 对于物联网 (IoT) 和移动解决方案，我们需要有一个紧凑的占用空间来限制资源使用。
8. 您可以使日志输出安全吗 - 使用 TLS、加密文件等？ 安全性对于正在处理的数据是否足够好？
9. 该框架是否会对我的应用程序的吞吐量/性能产生重大影响，尤其是最终的 I/O 阶段？ 日志记录最终会成为线程阻塞机制吗？
10. 日志记录框架的 API 使用起来有多容易？ 如果应用程序代码中的调用难以使用，开发人员可能会避免创建日志事件。 理想情况下，界面将是直观的，但拥有良好的支持文档以供参考可能非常宝贵，特别是对于那些刚开始其开发职业生涯的人。

与其评估每个可能的选项，不如尝试缩小选项范围。

## 将优化应用程序日志记录付诸行动

在您的组织中[采用 Fluentd](https://chronosphere.io/learn/fluent-bit-vs-fluentd/?utm_source=sponsored-content&utm_id=TNS) 进展顺利，并且您已被要求确定当前使用的日志记录框架是否能够胜任未来的工作，或者 Fluentd 的成功是否允许支持更改日志记录框架的情况。 使用所描述的因素，评估您的开发团队当前使用的解决方案。 将其与替代方案进行比较。

## 寻找答案

由于我们显然无法为您提供此练习的特定解决方案，我们希望您发现您已经在使用日志记录框架，并且它非常适合您的需求。 如果您的日志记录框架不是很合适，您可能已经认识到这些问题。 如果您还没有查明当前框架的问题，那么此考虑因素列表应该有助于确定问题。

下载 [电子书](https://chronosphere.io/resource/logging-best-practices/?utm_source=sponsored-content&utm_id=TNS)，了解如果正在使用的日志记录框架不提供特定于 Fluentd 的支持会发生什么，并学习克服此问题的方法。