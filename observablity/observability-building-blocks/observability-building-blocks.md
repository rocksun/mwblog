<!--
title: 可观测性的新构件
cover: https://observability-360.com/images/news/obs-building-blocks-3.png
-->

> 译自 [The New Building Blocks of Observability](https://observability-360.com/article/ViewArticle?id=observability-building-blocks)，作者 observability-360。

可观测性领域是一个动态且异质的领域。在这个生态系统中，商业巨头如Datadog、New Relic和Splunk与大型OS/免费堆栈（如ELK、Prometheus/Loki/Grafana和TIG（Telegraf/InfluxDB/Grafana））共存。然而，在近年来，三种技术趋势汇聚在一起，重塑了这一格局，为基于新一代强大开源技术和标准构建的新堆栈铺平了道路。可观测性周期表中的三个新元素是：

- [OpenTelemetry](https://opentelemetry.io/)
- [eBPF](https://ebpf.io/)
- [ClickHouse](https://clickhouse.com/)

这些元素各自独立，具有完全不同的特征和功能，但一种新型的可观测性竞争者正在将它们组装成强大的框架。

## OpenTelemetry

OpenTelemetry是CNCF中第二活跃的项目（仅次于Kubernetes），也是当今最重要的可观测性项目。它的主要好处是为竞争协议和语义的现有巴别塔带来一种通用语言。然而，它也释放了两个额外的副作用。首先，它通过解除供应商锁定，赋予了客户更大的权力。其次，它是市场新进入者的强大推动因素。OpenTelemetry的合规性对消费者具有吸引力，而新进入者可以享受采用其原生方式的优势，而现有企业则必须对现有代码库进行改装或重新设计。目前，OpenTelemetry还提供12种语言的SDK，从而大大减少了编写自己的代理的痛苦和工作量。除此之外，通过几个Helm命令，您可以部署OpenTelemetry Collector，为您提供一个强大且极具威力的遥测收集网关。

## eBPF

第二个元素是eBPF。打开Linux内核可能看起来像是一项难以理解的技术努力。然而，它的影响是巨大的。如果应用程序可以安全地访问内核，那么它们就可以完全了解进程。从这种可见性流中产生原始材料，可以直接构建跟踪和计算指标。公平地说，将这些原材料转化为遥测（并且在没有过多占用空间的情况下这样做）绝非易事。同时，进行该转换的构建块也可以在许多开源存储库中找到。能够利用这些存储库并构建零仪器产品赋予了可观测性供应商改变游戏规则的能力。

## ClickHouse

第三个元素是ClickHouse，是我们勇敢的新可观测性架构中的外星技术。它着陆得像是从洛克希德斯坦克工厂（Lockheed Skunkworks）逃脱的飞船，可以实现超光速飞行。同时，它的压缩算法扭曲了磁盘空间的结构，使其内部比外部更大。好吧，也许这有点夸张了。然而，ClickHouse已成为许多颠覆者和初创公司的后端数据库 - 例如Groundcover、SigNoz和DeepFlow等。每次的逻辑都是相同的。ClickHouse引擎是开源的，可以大规模接收数据并以高速查询。其超高效的压缩也意味着成本节约，可以传递给客户。由于它是开源的，也没有数据库许可费用。

一些精明而灵活的初创公司，如OneUptime、KloudMate和Groundcover，已意识到这三个组件为他们提供了无成本的构建模块，用于组装极其强大、稳健且具有成本效益的系统 - 我们可以称之为OeC堆栈。所有存储、采集和结构化遥测的繁重工作已经预先完成。在开源酒店中，确实有免费的午餐。事实上，通过OpenTelemetry、eBPF和ClickHouse，您可以享受免费的早餐、午餐和晚餐。显然，您不能在没有复杂工程和领域知识的情况下使这些组件一起工作 - 然而，市场的壁垒已大大降低。

## OeC还是只有eC？

随着“云原生”计算的出现，甚至可以排除OpenTelemetry，只运行精简的eBPF/ClickHouse堆栈。显然，“云原生”这个术语有点模糊，并且被广泛地用作营销术语。实际上，它倾向于在云托管的K8S集群中运行微服务。如果您的应用程序遵循这种模式，那么理论上，一个基于eBPF的引擎可以生成所有跟踪和指标，而无需任何仪器。这是Groundcover、DeepFlow和Coroot等云原生解决方案的前提（尽管Coroot也支持用于日志和跟踪的OpenTelemetry）。目前还有其他产品处于隐秘模式，正在采用这种架构。

在现实世界中，许多系统不太可能拥有如此干净和简单的拓扑结构。大多数分布式系统还将调用无服务器应用程序的第三方API和消息传递系统。然而，请求发起点位于K8S边界之外并不一定是一个破坏性因素。例如，Grafana Beyla等产品能够将跨度追加到传入跟踪中，以确保遥测链不中断。

## Post-Instrumentation时代？

越来越多的供应商开始质疑LMT（日志、指标、跟踪）范式，并转向Post-Instrumentation时代。尽管像Honeycomb这样的可观测性领域的领导者们原生支持OpenTelemetry，但他们对当前范式的碎片化本质进行了[公开批评](https://www.honeycomb.io/blog/cost-crisis-observability-tooling)，并主张采用“任意宽的结构化日志事件”为基础的模式。在概念上类似的是Observe和Dynatrace等供应商采取的方法，他们将多种遥测类型汇聚到巨大的数据湖中进行综合分析。

这些趋势引出了整个OpenTelemetry项目的一个令人不安的存在问题。正如我们之前所说，这是一座宏伟的建筑。但是如果它的三个主要支柱中的两个变得多余了怎么办？它是否会像其他精心构建的努力一样，突然被进化飞跃所淘汰？答案可能是否定的。日志仍然是可观测性的一个重要支柱，供应商仍然需要以某种方式摄取它们。然而，即使在这里，Groundcover的解决方案也不需要任何日志配置。它的eBPF驱动的Alligator代理将自动摄取日志并将其转发到内部oTel Collector。同样，APM并不是指标收集的唯一目的 - 收集基础设施、物联网等的设备指标的用例不会消失。

## 采用堆栈的供应商

在这个清单中，我们将看一下采用了三元素中至少两个堆栈的供应商。显然，许多公司支持oTel，但这里列出的公司依赖它作为其主要摄入机制。

|          | oTel | eBPF | ClickHouse |
|----------|------|------|------------|
| SigNoz   |  ✓   |      |     ✓      |
| OneUptime|  ✓   |  ✓   |     ✓      |
| Groundcover | ✓ |  ✓   |     ✓      |
| KloudMate |  ✓   |  ✓   |     ✓      |
| Coroot   |  ✓   |  ✓   |     ✓      |
| DeepFlow |  ✓   |  ✓   |     ✓      |
| [HyperDX](https://www.hyperdx.io/)  |  ✓   |      |     ✓      |

在不久的将来，看到这个名单添上几个名字是意料之中的。

## 展望未来

实际上，OeC/eC很可能不会很快取代LMT范式或使oTel过时。这更可能表明，可观测性是一个快速发展的领域和一个不断增长的市场。可观测性处于不断变化的状态 - 面临着越来越大的需求 - 它正在应用于更多的技术、架构和领域。它还被要求提供更丰富的见解和更低的成本。随着市场的扩大，越来越多的小众玩家有机会采用更新的技术和架构，以解决更具体的问题。这是因为可观测性不是一个零和游戏 - 它是一个不断增长的生态系统，许多范式和技术可以共存、整合和相互补充。