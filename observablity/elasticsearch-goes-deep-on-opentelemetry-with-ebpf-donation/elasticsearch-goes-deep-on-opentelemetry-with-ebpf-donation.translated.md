# ElasticSearch 深入 OpenTelemetry，捐赠 eBPF

![ElasticSearch 深入 OpenTelemetry，捐赠 eBPF 的特色图片](https://cdn.thenewstack.io/media/2024/03/e4d9fee6-cristian-palmer-xexawgzyobc-unsplash-1-1024x768.jpg)

监控和 [可观测性](https://thenewstack.io/observability/) 提供商 [Elastic](https://www.elastic.co/) 致力于进一步整合 [Elasticsearch 项目](https://thenewstack.io/this-week-in-programming-the-elasticsearch-saga-continues/) 与 [OpenTelemetry](https://thenewstack.io/observability-in-2024-more-opentelemetry-less-confusion/)，将其视为增强用户搜索体验的重要基石。

通过利用 Elasticsearch 对不同数据库和数据类型进行数据搜索和可观测性，用户可以受益于其多功能性和鲁棒性。OpenTelemetry 在此集成中发挥着关键作用，作为跨各种环境实现无缝数据监控和分析的中心组件。

借助 OpenTelemetry (OTel)，此集成的最新演变突出了其重要性：这体现在增强的分析功能中，使用户能够更深入地了解系统性能和资源利用率。随着 Elasticsearch 与 OpenTelemetry 持续发展，用户可以期待更强大、更全面的工具来有效管理和分析他们的数据。

## 捐赠

根据 [提案文档](https://github.com/open-telemetry/community/issues/1918)，Elastic 分析代理的捐赠将：

“通过成熟、功能丰富且高效的分析解决方案填补 OpenTelemetry 组件格局/架构中的空白。借助 [eBPF](https://thenewstack.io/what-is-ebpf/) 和分析中的尖端技术，将通过 OpenTelemetry 成为收集生产分析数据的标准。通过 OpenTelemetry 在广泛的语言/技术中收集分析数据将带来无摩擦的部署体验。”

此次捐赠遵循可观测性工具 [Elastic Common Schema (ECS)](https://www.elastic.co/guide/en/ecs/current/index.html) 和 [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/) [.](https://opentelemetry.io/) 之间的“结合”。具体来说，开源 Elastic 的创建者正在向 OpenTelemetry 贡献 ECS，并致力于 [这两个项目的联合开发。](https://www.elastic.co/guide/en/ecs/current/ecs-using-ecs.html)

## 集成

Elastic 分析代理以及 ECS 与 OTel 的集成突出了 Elastic 和 OTel 的影响力及其创建者的目标，即允许用户将遥测数据合并到一个面板中，以进行更全面的可观测性分析。事实上，ECS 与 OTel 的集成帮助 OTel 项目朝着与任何可观测性工具或流程完全兼容和标准化的最终目标迈进。

换句话说，Elasticsearch 和 OpenTelemetry（尤其是在它们在 2024 年之前几周发布了 GA 版本之后）都是非常流行的平台，可用于集成和处理来自不同来源的数据日志、指标和跟踪，并且它们的进一步集成应该受到许多人的赞赏。

“一旦分析代理被接受，你将获得的好处是，用户将在 OpenTelemetry 框架内获得持续分析，” Elastic 的总经理 [Abhishek Singh](https://www.linkedin.com/in/abhiksingh/) 告诉 The New Stack。“这是因为我们捐赠的代理使用 eBPF，与基于语言的代理相比，在实现时侵入性更小。”

Elastic 正在与 OpenTelemetry 在各个领域展开合作，不仅在分析方面，还在通用架构和语义约定方面。Singh 说，目标是将 OpenTelemetry 从具有分散功能的碎片化格局转变为客户默认依赖的综合可观测性框架。

其贡献涵盖了持续分析器的完整实现。这包括负责运行系统和执行分析任务的代理。Singh 指出，Elastic 本质上提供了与应用程序软件一起运行的检测组件，收集信息以分析软件，并提供有关应用程序中时间分配位置的足够数据。

实际应用包括成本降低和优化工作。Singh 说，例如，通过利用分析，可以识别和优化应用程序中消耗大量 CPU 的函数，从而减少计算使用并节省成本。
**Elasticsearch 的多功能性**

此外，还提供了对环境影响的见解。辛格表示，可以根据计算使用情况分析碳排放，从而优化某些功能或库，以最大程度地减少环境影响并为客户节省成本。

“从首席技术官的角度来看，在考虑 Elasticsearch 时，我们的目标是在毫秒内提供答案。我们是领先的搜索分析公司，得到超过 50% 的财富 500 强组织的信赖。我们的平台使用户能够使用结构化和非结构化数据实时查找答案，从而使企业能够大规模利用其数据，”辛格说。

“我们的客户受益于一个平台，该平台支持对数据进行搜索和分析，无论其类型如何。将可观察性数据与业务数据集成在一起，可以获得更深入的见解和运营效率。我们的目标是使 OpenTelemetry 成为通用仪表领域，确保仪表方面的进步使整个社区受益，并为客户带来更好的成果。”

Elasticsearch 的主要吸引力在于其多功能性。例如，考虑首席技术官的观点。他们可能希望分析各种方面，例如：

* [Kubernetes](https://thenewstack.io/kubernetes/) 集群中的节点性能
* 欧洲和北美等不同地区的销售数据

在发生灾难或中断的情况下，安全人员依靠 Elasticsearch 通过进行详细搜索来查明根本原因。此外，负责持续监控的运营团队面临着从数据中得出推论和分析数据的艰巨责任，以确保系统稳定性和性能。

## 为什么选择 OpenTelemetry？

作为第二高的 [CNCF “速度项目”](https://www.cncf.io/blog/2023/01/11/a-look-at-the-2022-velocity-of-cncf-linux-foundation-and-top-30-open-source-projects/)，得益于其在 [CNCF](https://cncf.io/?utm_content=inline-mention) 生态系统中的用户群的强劲增长，[OpenTelemetry](https://thenewstack.io/servicenows-lightstep-buy-moves-observability-up-the-stack/) 已成为一种广泛采用的方式，可将仪表添加到应用程序中，以从您最喜欢的可观察性来源收集指标、日志和跟踪。

然后可以将来自不同来源的遥测数据（指标、日志和跟踪）与您最喜欢的面板（例如 [Grafana](https://grafana.com/)）结合起来进行监控。

广受欢迎的 [ECS](https://www.elastic.co/guide/en/ecs/current/index.html) 用于定义在 [Elasticsearch](https://thenewstack.io/properly-monitor-elasticsearch/) 中存储事件数据（例如日志和指标）时要使用的一组通用字段，以及每个字段的特定字段名称和 Elasticsearch 数据类型，并根据其文档提供描述和示例用法。在 OpenTelemetry 保护伞下，ECS 将变得更好。

事实上，机器学习正在与 Elastic 集成，这已经提供了一些非常有趣的结果。[Austin Parker](https://www.linkedin.com/in/austinlparker)，[Honeycomb.io](https://www.honeycomb.io/?utm_content=inline-mention) 的开源总监和 OpenTelemetry 的主要维护人员告诉 The New Stack，弹性分析代理仍在进行中，并指出“在接受之前，必须进行一段时间的尽职调查和技术审查。”

帕克确实注意到，由于该代理是专有的且是封闭源代码的，因此出现了一些“许多不同公司不得不审查的棘手法律问题”，但帕克表示“不希望尽职调查发现任何重大问题或障碍”。

帕克说：“我们很高兴看到 Elastic 继续与开源 [可观察性](https://thenewstack.io/how-we-manage-incident-response-at-honeycomb/) 社区合作，并相信这笔捐赠将有利于 OpenTelemetry 分析信号的进展。”

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)