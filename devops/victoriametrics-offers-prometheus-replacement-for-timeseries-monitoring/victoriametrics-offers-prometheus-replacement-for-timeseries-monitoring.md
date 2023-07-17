# VictoriaMetrics 提供了用于时间序列监控的 Prometheus 替代方案

MetricsQL 提供了丰富的功能列表，用于各种聚合、转换、汇总和其他针对时间序列的特定功能。

翻译自 [VictoriaMetrics Offers Prometheus Replacement for Time Series Monitoring](https://thenewstack.io/victoriametrics-offers-prometheus-replacement-for-timeseries-monitoring/) 。

![](https://cdn.thenewstack.io/media/2023/07/5e011b44-victoria_metrics-1024x683.png)

Prometheus 作为云原生基础设施监控的[领先开源工具崭露头角](https://thenewstack.io/prometheus-at-10-whats-been-its-impact-on-observability/)。然而，在过去的几年里，一些人认为 [Prometheus 的发展](https://thenewstack.io/grafanacon-2023-fewer-pain-points-promised-for-the-observability-tool/)与其用户群之间存在需求差异。

[VictoriaMetrics](https://victoriametrics.com/) 的联合创始人之一、用户和维护者 [Roman Khavronenko](https://www.linkedin.com/in/roman-khavronenko-47b51a63/) 一直致力于扩展旗舰开源产品 [MetricsQL](https://victoriametrics.com/products/metricsql/) ，用于时间序列数据监控解决方案。

Khavronenko 表示：“我们的查询语言旨在解决我们在使用 Prometheus 时遇到的问题。当我们最初尝试 Prometheus 时，对其功能感到满意，但随着我们的深入研究，我们发现了一些架构层面的问题。例如，Prometheus 社区成员指出了语言问题，但被维护者拒绝了。”他说：“ VictoriaMetrics 倾听了社区的声音，并且不再依赖 Prometheus 的库，我们能够塑造我们的查询引擎以满足新的需求。”

与此相反， Khavronenko 指出，Thanos、Cortex 和 [Mimir](https://grafana.com/oss/mimir/) 等项目重新使用了由 Prometheus 维护者开发的库。他说，这样做有助于保持“最高级别的兼容性，因为所有列出的解决方案基本上都使用相同的代码。”他说：“但一旦其中任何一个想要进行更改，就需要花费很长时间来说服其他相关方需要进行更改，并满足他们的所有要求。” Khavronenko 说：“ VictoriaMetrics 不使用任何 Prometheus 库。虽然这降低了兼容性水平，但使我们能够随时添加所需的功能，具有很大的灵活性。”

![](https://cdn.thenewstack.io/media/2023/06/a165063e-vmalert.png)
*VictoriaMetrics 的警报系统与 Prometheus 类似，只是作为一个独立的服务存在。图片：VictoriaMetrics。*

Khavronenko 表示，对于应用程序开发者来说，保持快速的开发节奏并对开发过程有控制是至关重要的。依赖外部库可能会导致漏洞和其他问题。“我们开发自己的查询引擎的主要原因是使其更高效和灵活。例如，MetricsQL 从一开始就支持多线程，而 PromQL 仍然是单线程的。” Khavronenko 说：“这种语言保留了 Prometheus 查询语言的功能，同时解决了我们遇到的问题。”

确实，有机会开发能够更好满足 Prometheus 用户不同需求的应用程序。“在 Prometheus 的部署和配置过程中，目前存在太多机会造成重大错误。随着企业中 Kubernetes 集群数量的增加，要始终确保可靠准确地监控所有集群，存在太多潜在的故障点。”[企业管理协会（EMA）](https://www.enterprisemanagement.com/)的分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk) 表示。“理想情况下，每个新的 Kubernetes 集群应自动包括对其所有相关指标的监控和警报。这些指标和警报可能因特定集群上运行的应用程序而异，这使得情况变得更加具有挑战性。”

Khavronenko表示，MetricsQL 的设计目标是：

* 帮助用户解决最常见的指标查询问题。
* 与行业标准的 Prometheus PromQL 兼容。
* 提供类似 HDR 的直方图，以准确分析极端数据范围。

MetricsQL 专为查询时间序列数据而设计。它提供了丰富的功能列表，用于各种聚合、转换、汇总和其他时间序列特定功能，并且“在任何规模上使用仍然简单高效”，Khavronenko 说。

应用包括视频游戏流媒体服务、在线音乐服务、科学研究和涉及流媒体数据分发的其他类似应用。Khavronenko 指出，这些应用通常需要监控数十亿个指标，这些指标可能分布在多个云部署中，物理位置可以在世界的任何地方。而这正是 Prometheus 通常做得不好的地方。

Khavronenko 指出，Prometheus 无法很好地处理每秒应用程序处理请求数的功能，而 MetricsQL 正是为此而设计的。“Prometheus 通常提供推算的结果而非精确结果，导致误导性信息和潜在问题。”Khavronenko 说。“这个问题在 2019 年在 Prometheus 的 GitHub 存储库中广泛讨论过。”

Volk 也表示同意：“确保可靠监控 Kubernetes 集群需要太多知识。” Volk 说。“如果 DevOps 团队必须担心如何优化配置他们的查询，以便实际测量正确的数据而不会引起集群的资源问题，对于像 Kubernetes 这样的主流技术来说，有效的监控太困难了。”

VictoriaMetrics 的收入主要来自企业版本和为大型公司提供的服务。“我们提供架构支持和针对大型组织需求的附加功能。” Khavronenko 说。“由于我们没有寻求外部投资，并且在发布后的六个月内开始盈利，所以我们从一开始就是盈利的。”

VictoriaMetrics 最近还推出了 VictoriaLogs ，用于监控应用程序，公司称其为“更具战略意义的全企业范围可观测性的状态”。 VictoriaLogs 适用于结构化和非结构化日志，以最大程度地与用户所需的大规模基础设施向后兼容，无论他们是在学术界还是商业界工作，是在电子商务还是视频游戏团队工作。

尽管日志、指标和追踪组成了可观测性的三个支柱，“许多公司根本不依赖追踪，而我见过使用指标较少的组织。” Khavronenko 说。“但我还没有见过一家 IT 公司不使用日志。” Khavronenko 说。“因此，尽管 VictoriaMetrics 为指标提供可扩展的性能解决方案，但 VictoriaLogs 现在为日志提供相同的解决方案。”