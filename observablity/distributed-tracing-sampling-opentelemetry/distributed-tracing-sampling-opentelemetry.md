<!--
title: 采样：分布式追踪的“点金石”？解密可观测性深层奥秘
cover: https://cdn.thenewstack.io/media/2026/03/4194d015-graficon-stuff-85emz4ge7iy-unsplash-scaled.jpg
summary: 分布式追踪采样在现代可观测性中至关重要，但实现复杂。文章对比了头部采样与尾部采样，强调其挑战，并指出单独采样无法提供准确指标，需先物化指标。采样是权衡，而非一劳永逸的解决方案。
-->

分布式追踪采样在现代可观测性中至关重要，但实现复杂。文章对比了头部采样与尾部采样，强调其挑战，并指出单独采样无法提供准确指标，需先物化指标。采样是权衡，而非一劳永逸的解决方案。

> 译自：[Sampling: the philosopher's stone of distributed tracing](https://thenewstack.io/distributed-tracing-sampling-opentelemetry/)
> 
> 作者：Michele Mancioppi

在现代可观测性中，分布式追踪通常被认为是最具表现力的信号。它可以捕捉日志提供的大部分信息，同时增加丰富的执行上下文。如果没有 OpenTelemetry，这种转变在实践中是不可行的，OpenTelemetry 可以在各种框架、库和技术中实现 Span 收集。

然而，分布式追踪也可能代价高昂。在一个（有时是多余的）分布式系统时代，即使是中等规模的环境也能产生海量的 Span。虽然存储大量数据的成本普遍降低，但我们大规模查询 Span 的能力并未跟上我们生成它们的能力。

## 采样来救场

如果我们无法有效查询所有收集到的追踪数据，解决问题的一个直观正确方法是缩小数据规模。**采样**，即选择性地保留生成追踪数据的一部分，这种做法与分布式追踪本身一样古老。它在 2010 年的原始 [Dapper](https://static.googleusercontent.com/media/research.google.com/en//archive/papers/dapper-2010-1.pdf) 论文中显著出现，该论文被广泛认为是最终导致 OpenTelemetry 的现代行业标准方法的起源。早期如 [X-Trace](https://www.usenix.org/legacy/events/nsdi07/tech/fonseca.html) 等分布式追踪论文也提到了采样。

分布式追踪的采样方法通常分为两类：

*   **头部采样**，它预先决定是否为给定请求创建 Span，通常在请求到达第一个被追踪组件时决定。
*   **尾部采样**，它记录所有请求的追踪数据，但只选择性地存储一部分。

这两种方法具有截然不同的权衡。

> “采样，即选择性地保留生成追踪数据的一部分，这种做法与分布式追踪本身一样古老。”

顺便说一句：当与[可观测性](https://thenewstack.io/taking-your-observability-strategy-to-the-next-level/)圈子以外的人交谈时，他们往往会惊讶于“sampled”（已采样）这个词代表“我们保留的这个 Span”；相反，人们通常认为 sample 是过滤的同义词，而不是其反义词。我以前也有过同样的困惑，我用从盘子里摘下多汁覆盆子的心像来提醒自己这个意思。

## 头部采样

头部采样在概念上很简单。当一个新的追踪即将开始时，你立即决定是否要收集它。

### 头部采样的理论

头部采样决策可以基于请求属性，但在实践中，它通常是随机的，通过使用确定性规则（例如模运算）从追踪标识符派生而来。

随机采样通常被称为**一致概率采样**或**确定性采样**。它假设，从统计学上讲，所有追踪都同样有价值。或者，至少在足够高的采样率和足够多的追踪样本下，错误和延迟峰值等重要信号仍然会充分可见并具有良好的统计代表性。

在现实中，特别是在个位数的采样率下，这个假设就会失效。一致概率采样倾向于遗漏或低估局部问题，即一小部分请求的行为与其余请求截然不同。

### OpenTelemetry 中头部采样的实践

在 OpenTelemetry 中，头部采样可以通过两种主要方式实现：更灵活的方法通过[追踪上下文](https://www.dash0.com/knowledge/what-is-distributed-tracing)传播采样决策，这与在追踪中“粘合”Span 的机制相同。更简单的方法，仅限于一致概率采样，可以完全在可观测性管道中完成。

#### 通过追踪上下文传播采样决策

在 OpenTelemetry 中，当创建新的根 Span 时会做出采样决策。SDK 会咨询配置好的采样器，最常见的是用于一致概率采样的 [TraceIdRatioBased](https://opentelemetry.io/docs/specs/otel/trace/sdk/#traceidratiobased)。采样器检查追踪 ID，并确定性地决定是否应该采样该追踪。相同的追踪 ID 无论由哪个服务评估，都会始终产生相同的决策。

该决策被编码为单个比特，即采样标志，位于追踪标志中，并作为追踪上下文的一部分向下游传播。具体来说，考虑 [W3C Trace Context](https://www.w3.org/TR/trace-context/) 规范定义的 traceparent 头部，该规范标准化了通过 HTTP 进行追踪传播的方式：

**traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01**

```

             ^  ^                                ^                ^

       version  trace id                         span id          trace flags
```

最后一个字节编码采样决策：01 表示“已采样”，00 表示“未采样”。

当下游服务收到带有**已采样**标志的 traceparent 头部时，其 SDK 会遵循该决策并为该追踪生成 Span。如果未设置该标志，则根本不导出 Span。

另一个广泛使用的格式是 [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-tracingheader)，它遵循类似的模型，将采样决策编码在 X-Amzn-Trace-Id 头部中。

结果是，在追踪头部做出的一个决策会一致地应用于所有服务，而无需任何集中协调。

为了完整性，还有更精细的[方法](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.53.0/oteps/trace/0235-sampling-threshold-in-trace-state.md)，旨在以更复杂的实现为代价，使采样*更可靠地随机*。从技术角度来看，这些方法很有趣，但在实践中我发现它们大多是不必要的。

#### 可观测性管道中的恒定概率采样

随机采样追踪的另一种方法是始终通过 [AlwaysOn](https://opentelemetry.io/docs/specs/otel/trace/sdk/#alwayson) 采样器创建 Span，然后以廉价和分布式的方式丢弃未采样的追踪。

在这种模型中，应用程序中的 SDK 总是生成 Span。应用程序附近的 OpenTelemetry Collectors 会丢弃属于那些追踪标识符不符合某些确定性标准（例如超出配置的哈希范围）的追踪的 Span。OpenTelemetry Collector 的 [probabilisticsampler](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/probabilisticsamplerprocessor) 处理器使这变得容易：

```

processors:
  probabilistic_sampler:
    sampling_percentage: 10

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [probabilistic_sampler]
      exporters: [otlp]
```

每个 Collector 实例独立地对追踪 ID 进行哈希处理，并只保留属于那些落在配置百分比范围内的追踪的 Span。由于决策是基于追踪标识符的确定性，所以集群中的所有 Collector 实例都会就保留哪些追踪达成一致，而无需相互通信。

这种方法因其简单性而引人注目。它确实通过创建可能稍后被丢弃的 Span 浪费了一些资源，但它易于在大型 Collector 集群中一致部署，这些集群通常由平台团队集中管理，并且依赖于 AlwaysOn 是 OpenTelemetry SDK 中默认采样器的事实。

## 尾部采样

尾部采样始于每个可观测性实践者都了解的一个事实：并非所有追踪都具有同等价值。这个想法在理论上很简单。收集一个追踪的所有 Span，然后决定该追踪是否值得保留。如果实施得当，尾部采样可以非常有效。不幸的是，它也很难实施得好。

### 尾部采样标准

我遇到的大多数尾部采样策略都类似于某种变体：“保留所有带有错误的追踪，并保留其余追踪的 X 百分比作为基线。”

基线很重要。你需要一个具有统计意义的正常行为样本，以了解系统在日常条件下的表现。

仅仅关注采样包含错误的追踪过于简单化。尾部采样的更有用心理模型是基于追踪的*有趣程度*。并非所有错误都具有趣味性。想想你的日志和追踪中累积的反复出现、良性或可恢复的错误。

相反，许多有趣的追踪根本不包含错误。具有高业务影响或强用户可见性的操作值得观察，即使它们成功。

最重要的是，也是经常被忽视的一点，*不寻常*的追踪特别有趣。很少执行的代码路径通常值得追踪，产生意外结果的操作也同样如此，例如发现某个 API 可以返回 [HTTP 状态码 418](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/418)。

### OpenTelemetry 中的尾部采样

无论具体标准如何，大规模的尾部采样因以下几个原因而**困难**。

其核心是，尾部采样需要一个**时间延迟的集中决策**。属于一个追踪的所有 Span 必须一起考虑。这与 OpenTelemetry Collector 的设计优势背道而驰，后者擅长实时、无状态的流式处理。

弥合这一差距需要在可观测性管道中采用更复杂的架构：

![使用两层 OpenTelemetry Collectors 实现尾部采样的常见架构。](https://cdn.thenewstack.io/media/2026/03/796317fc-picture1.png)

*使用两层 OpenTelemetry Collectors 实现尾部采样的常见架构。*

第一层是**代理层**，每个节点一个 Collector 实例（例如，在 Kubernetes 上，作为 DaemonSet 或每个 Pod 作为 sidecar），靠近应用程序。OpenTelemetry SDK 默认使用 **AlwaysOn** 采样器，因此每个 Span 都会被创建并发送到附近的代理。日志和指标直接转发到后端，因为它们被认为不需要尾部采样。（正如你肯定能从字里行间读出的，我对这个问题有强烈的看法，但我将其留待未来的文章讨论，因为这篇文章已经足够庞大了。）追踪的处理方式不同。代理使用 **loadbalancingexporter** 一致地哈希追踪标识符，并将一个追踪的所有 Span 路由到第二层的同一个 Collector。

第二层是**采样层**，一个 Collector 实例池，运行着 **tailsamplingprocessor**。因为 **loadbalancingexporter** 保证一个追踪的所有 Span 都到达同一个实例，所以该 Collector 可以缓冲它们，评估配置的采样策略（错误状态、延迟阈值、速率限制等），然后将追踪转发到后端或丢弃。

这种架构有效，但操作复杂。这两层必须独立扩展和监控。在扩展事件期间，一致性哈希必须保持稳定。使用 DNS 作为第二层中存在哪些 Collector 的记录系统，以及由此产生的最终一致性，都非常难以排查。（因为，你知道，总是 DNS 的问题。）

也存在更深层次的挑战。

从单个 Span 的角度来看，*没有迹象*表明一个追踪已完成。分布式追踪没有可与文件系统中的 EOF 标记相媲美的东西。一旦做出采样决策，就必须记住它，以便对后续到达的 Span 进行一致处理。经常听到这样的说法：“我们的追踪很快，一分钟内就完成了。” 但在这样的系统中，慢速追踪往往*非常有趣*，而且几乎每个环境都包含执行对业务至关重要的工作（例如对账或计费）的[长时间运行的批处理作业](https://thenewstack.io/pgq-queuing-for-long-running-jobs-in-go-written-atop-postgres/)。

采样层本质上是有状态的，在等待足够数据到达以做出决策时会缓冲 Span。理想情况下，尾部采样允许决策*显著延迟*。这样做需要足够持久地存储 Span 以应对这种延迟，同时如果追踪最终被丢弃，仍能高效地删除它们。目前，OpenTelemetry Collector 将待处理的 Span 存储在内存中，这导致了困难的容量规划问题。社区有[提案](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42326)将这种缓冲卸载到磁盘，但我不知道社区是否有生产就绪的解决方案。

如上所示实现的尾部采样，也与弹性分布式系统的设计方式相冲突。服务分布在可用区或区域以避免相关故障。因此，Span 分散在这些区域中。尾部采样要求一个追踪的所有 Span 汇聚到一处，这意味着将数据跨区域路由到特定的 Collector 实例，这破坏了旨在避免中央瓶颈的架构原则。可观测性管道最终会以应用程序架构明确旨在避免的方式集中流量。

最后但同样重要的是：网络成本。将 Span 路由到“正确的 Collector”可能会由于跨可用区网络流量而产生显著的云网络成本。根据我的经验，一旦团队开始研究其可观测性管道的网络成本，结果往往令人咋舌。

## 仅靠采样无法提供可观测性

采样有一个容易被忽视的基本限制：**你无法从采样的追踪中计算出准确的指标。**

RED 指标——请求速率、错误速率和持续时间分布——是可观测性的基础。它们支持仪表盘、SLO 和警报。然而，它们的价值取决于精度，这使得它们与采样之间存在矛盾。

想象一下，使用 10% 的一致概率采样来计算 RED 指标，并将结果乘以 10。请求和错误计数可能偏差高达 90%，并且持续时间直方图很可能被严重低估，因为最慢的请求有相对较高的概率未被记录。

> 采样有一个容易被忽视的基本限制：你无法从采样的追踪中计算出准确的指标。

对于只保留错误、慢速请求和一小部分正常追踪的尾部采样，偏差会向相反方向偏移。错误变得过度代表，并且持续时间直方图严重偏向于“不愉快路径”。（一些可观测性供应商通过在采样过程中在 Span 上注释“多重性”来弥补这一点，这确实可以减少误差范围，但本文重点介绍 OpenTelemetry 中可用的方法。）

在这两种情况下，都无法通过仅查询幸存的 Span 来重建准确的 RED 指标。因此，任何对追踪进行采样的架构都必须在**采样丢弃数据之前物化指标**。

这就是为什么在前面描述的两层架构中，采样层在 **tailsamplingprocessor** 之前运行 **spanmetricsconnector** 或更新的 **signaltometricsconnector** 等连接器。连接器会查看每个 Span 并生成准确的计数和直方图。只有在此之后才会进行采样。

指标生成本身并非易事。OpenTelemetry 指标具有[时间性](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#temporality)的概念。指标可以是**累积的**，表示自进程启动以来的总数，这是我们通常概念化指标的方式；也可以是**增量的**，表示自上次报告间隔以来的变化。两者不可互换，不同的后端有截然相反的偏好。如果指标以错误的时间性发出，则需要 **deltatocumulative** 或 **cumulativetodelta** 等有状态处理器，这会增加内存开销、路由和认知复杂性以及状态性。

此时，自然会问：“如果管道中创建 RED 指标如此困难，为什么不在被追踪的应用程序中生成我们需要的指标呢？”“SDK 不能直接发出准确的 RED 指标吗？”

原则上，它们可以。OpenTelemetry 规范定义了 [HTTP 指标](https://opentelemetry.io/docs/specs/semconv/http/http-metrics/)、[gRPC 指标](https://opentelemetry.io/docs/specs/semconv/rpc/grpc/) 和其他指标的语义约定。这些指标经过精心指定，以避免高基数问题，当指标携带完整 URL、用户标识符或完整查询字符串等属性时会发生这种情况，这些属性可能具有大量不同的值，并导致指标系列组合式爆炸。

我真的很喜欢 OpenTelemetry 语义约定，而关于指标的那些是我最喜欢的之一。但它并非涵盖所有场景的指标列表。例如，我不知道有任何关于“无头”操作的语义约定，比如当你[定期安排一个作业运行](https://thenewstack.io/linux-how-to-use-cron-to-schedule-jobs/)时。

在实践中，SDK 对这些指标的支持不均衡，尤其是在各种自动插桩库中。因此，在许多实际部署中，RED 指标实际上是在可观测性管道中而不是 SDK 中产生的。

即使 SDK 发出指标，问题也并未解决。每个 Collector 可能为每个服务创建指标数据点，你需要对管道中更下游的指标进行聚合以限制指标基数，这有时会导致第三层 OpenTelemetry Collectors、进一步的（尽管与 Span 相比更小）跨可用区网络流量以及更多的复杂性。

## 结论

可观测性并非易事。我们生成海量数据，将这些数据转化为有用且具有成本效益的东西需要精心的工程设计。

在观察大型分布式系统的实践中，采样是不可避免的必要。虽然理念简单，但现实复杂。这种复杂性向外扩散，尤其体现在 RED 指标的生成和保留方式上。

好消息是进展仍在继续。针对 **tailsamplingprocessor** 的基于磁盘缓冲的提案旨在减轻尾部采样的操作痛苦。诸如 **signaltometricsconnector** 之类的新型连接器使得即使在大量采样的管道中也能更实际地生成准确的指标。

唉，没有灵丹妙药。未来的道路是更好的工具、更智能的默认设置以及对采样是一系列权衡而非一次性解决并遗忘的问题的清晰理解的结合。还有一些有趣的想法，例如“[基于存储的样本尾部采样](https://www.youtube.com/watch?v=qq8hTct8zm4)”，虽然名字很长，但基于一个简单的直觉：将所有数据“热存储”一小段时间，然后再进行采样，这可以通过 OpenTelemetry Collectors 相对容易地实现，将传入数据复制到一个短期的、全精度流和一个使用本文中解释的其他技术采样的流中。

点金石依然难以捉摸，但炼金术正在不断改进。