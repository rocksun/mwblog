# Kloudfuse 3.0：一体化可观测性平台诞生

![Featued image for: Kloudfuse 3.0: an All-in-One Observability Platform Emerges](https://cdn.thenewstack.io/media/2024/11/ed331c01-kloudfuse-logo-1024x576.png)

盐湖城——可观测性厂商相对较少的原因是进入门槛非常高。

与针对[Kubernetes](https://roadmap.sh/kubernetes)、安全和测试的众多单一视图平台不同，[可观测性](https://thenewstack.io/observability/)需要在多个方面进行更大量的开发和投资。可观测性平台必须扩展到网络的所有方面，并全面涵盖所有堆栈层中的各种环境。它们必须满足组织的特定需求，尤其是在维护运营安全和确保强大的软件交付方面。

这种全面的需求是像[Kloudfuse](http://www.kloudfuse.com)这样的初创公司值得关注的一个原因，因为它将其平台定位为与[Datadog](https://www.datadoghq.com/?utm_content=inline+mention)、Grafana、[Honeycomb.io](https://www.honeycomb.io/?utm_content=inline+mention)、[New Relic](http://newrelic.com/?utm_content=inline+mention)等老牌公司竞争。

该公司拥有通用电气医疗、印度在线药店塔塔1MG和Workday等客户，凭借本周在[KubeCon+CloudNativeCon 北美大会](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)上发布的版本，该公司已经取得了良好的开端。

## Kloudfuse 提供的功能

更成熟的可观测性平台具有一定的优势。Grafana 拥有那些漂亮的面板，并且与开源监控工具[Prometheus](https://thenewstack.io/prometheus-at-10-whats-been-its-impact-on-observability/)配合得非常好。Datadog 试图涵盖所有方面，提供组织可能大规模寻求的任何可观测性功能。如今的可观测性平台必须展示与[OpenTelemetry](https://thenewstack.io/why-the-latest-advances-in-opentelemetry-are-significant/)、[生成式 AI](https://thenewstack.io/ai-powered-observability-picking-up-where-aiops-failed/)以及越来越多地与[用于可观测性的 eBPF](https://thenewstack.io/ebpf-meaner-hooks-more-webassembly-and-observability-due/)集成，这些集成跨越从[Linux 内核](https://thenewstack.io/linux-kernel-6-12-prepped-for-superior-scheduling-real-time-ops/)扩展的任何堆栈层。

Kloudfuse 试图在其平台中涵盖这些方面并提供更多功能。

Kloudfuse 提供的突出功能包括旨在改进“可观测性的三个支柱”——[指标、日志和追踪](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/)——的新数据流，用于它们不足的情况。通过 Kloudfuse 的指标、事件、日志和追踪 (MELT) 框架，[Kloudfuse 3.0](https://www.kloudfuse.com/product-launch/kloudfuse3.0) 还提供前端可观测性功能，包括实时用户监控和会话回放。

自本世纪初发布 Kloudfuse 1.0 以来，Kloudfuse 一直致力于以[可观测性数据湖](https://thenewstack.io/key-trends-shaping-the-observability-market/)为其平台提供支持，认识到需要将所有可观测性遥测数据整合到一个位置。

![Architecture of the Kloudfuse observability platform.](https://cdn.thenewstack.io/media/2024/11/73e694f1-kloudfuse-architecture-1024x474.png)
Kloudfuse 可观测性平台的架构。(来源：Kloudfuse)

“认识到市场中的碎片化以及开发人员在手动解决问题方面面临的挑战，我们启动了初始版本以在一个平台中捕获指标和日志。我们的愿景是随着我们不断扩展，集成额外的可观测性流，”Kloudfuse 的联合创始人兼首席执行官[Krishna Yadappanavar]、联合创始人兼首席技术官[Pankaj Thakkar]和联合创始人兼首席架构师[Ashish Hanwadikar]在[公司博客上的文章](https://www.kloudfuse.com/blog/unveiling-kloudfuse-3-0)中写道。

“早期的客户反馈证实，这种方法通过将指标与底层日志相关联，从而显著减少了检测问题的平均时间，简化了工程和 DevOps 团队的工作流程。”

随着 Kloudfuse 3.0 的发布，该公司推出了一些新功能。据该公司称，关键功能包括：
**数字体验监控 (DEM)。**新的真实用户监控 (RUM) 功能（前面提到过）提供了对所有堆栈中用户体验的洞察，涵盖前端到后端的跟踪、日志和指标。**持续分析。**此分析功能使开发人员能够识别隐藏的性能瓶颈并实时提高代码质量。通过自动评估 CPU 利用率、内存分配和磁盘 I/O，它有助于确保每行代码的最佳性能，同时最大限度地减少资源使用和成本。**提供数据湖。**自 Kloudfuse 1.0 发布以来，Kloudfuse 一直致力于以可观察性数据湖为平台核心，认识到需要将所有可观察性遥测数据整合到单个平台中，并捕获指标和日志。**高级 AI 分析功能。**Kloudfuse 3.0 新增了 [Prophet](https://github.com/facebook/prophet) 用于异常检测和预测，以提供更准确的结果，有效管理包含缺失值（例如中断或活动较低的间隙）的不规则时间序列。即使训练数据有限，这也减少了调整工作并改进了预测。**K-Lens。**Kloudfuse 的 K-Lens 使用异常值检测分析数千个属性，识别导致特定问题的属性。它通过可操作的见解和清晰的可视化（例如热图和多属性图表序列）来加速调试和事件解决。**FuseQL 语言。**引入功能强大的日志查询语言，具有高级功能、多维聚合和过滤器，解决了 LogQL 等日志查询语言的局限性。**Facet 分析。**利用 Kloudfuse 的专利申请中的 LogFingerprinting 技术，该技术自动从日志中提取关键属性以进行更快的分析和故障排除，此功能提供了高级搜索、过滤、书签和分组选项，从而大大提高了日志分析效率。

为了满足扩展需求，Kloudfuse 3.0 包括：

**日志存档和水化。**此功能可立即访问历史日志，以满足合规性和法规要求，同时降低长期存储成本。日志以经济高效的压缩格式存储在客户自己的存储中。**基数分析和指标汇总。**基数分析提供对传入指标、日志和跟踪的实时洞察，使组织能够主动发现和减少高基数数据，从而降低存储和处理成本。指标汇总聚合数据，从而提高查询性能并降低平均故障恢复时间。

虽然没有像其他功能那样多地讨论，但 Kloudfuse 客户保留了数据存储和实时监控的数据主权，而并非所有竞争对手都提供此功能。它不收取存储费用，因为客户提供自己的存储。

Kloudfuse 包括数据整形和转换功能，以及客户管理的长期存储；该平台用于分析数据，而无需客户放弃数据主权。单个数据湖可以无限扩展，同时持续训练大型语言模型以改进 AI 辅助数据分析。

## 可观察性：激烈的竞争
虽然 Kloudfuse 提供了广泛的功能和一些独特的功能，但它也必须应对激烈的竞争，因为可观察性工具并非商品，必须明确区分自身。已建立的参与者试图在其平台中提供可观察性工具以降低成本，这主要通过优化资源来实现。

Kloudfuse 也是如此。它允许客户在数据到达可观察性分析（在故障排除期间可能变得非常昂贵）之前控制数据，以及虚拟私有云 (VPC) 部署模型（Grafana 也提供），以进一步控制成本。VPC 部署还可以帮助避免公司通常需要支付才能与软件即服务可观察性供应商合作的数据传输/出口文件。

Kloudfuse 将不得不持续提供新的可观察性功能，涵盖所有已建立参与者提供的功能——以及更多功能。易用性和集成必须比竞争对手提供的功能更好。

由于遥测数据的统一，使用 Kloudfuse 的开发人员无需手动将日志查询结果与跟踪、指标等关联。

Kloudfuse 能够处理无限扩展和大量数据，因此客户例如在故障排除时无需支付额外的数据费用。客户可以自由运行许多查询，否则如果他们没有在其自己的 VPC 中直接控制下部署可观察性平台，他们就必须为此付费。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)