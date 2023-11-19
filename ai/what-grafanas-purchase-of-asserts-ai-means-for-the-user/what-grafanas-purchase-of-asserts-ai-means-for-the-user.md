<!--
title:  Grafana收购Asserts.ai给用户带来的影响
cover: https://cdn.thenewstack.io/media/2023/11/2eafb5be-nathalie-spehner-pxo29ylofg8-unsplash-e1700153336273-1024x683.jpg
-->

Grafana Labs收购Asserts.ai，以便通过更简单、更自动化的方式帮助用户分析指标数据。

> 译自 [What Grafana’s Purchase of Asserts.ai Means for the User](https://thenewstack.io/what-grafanas-purchase-of-asserts-ai-means-for-the-user/)，作者 B. Cameron Gain 是 ReveCom Media 的创始人兼首席分析师。 20 世纪 80 年代初，他黑掉了太空侵略者控制台，整天只花 25 美分在当地电子游戏厅玩游戏，从此开始了他对计算机的痴迷。然后......

[Grafana Labs](https://grafana.com/) 收购 [Asserts.ai](https://www.asserts.ai/) 显示了它对 Grafana，尤其是 [Grafana Cloud](https://thenewstack.io/grafana-extends-free-access-for-cloud-managed-observability/) 的功能进行大规模扩展的积极态度。Asserts 的目标与这种扩展一致，它提供了更简单、更自动化的指标数据分析。Asserts 简化了这一复杂的背景分析任务，这对人类来说是非常困难的。此举表明 Grafana 致力于为其支付用户提供更多价值，尤其是随着 Grafana 支付用户群体的增长。Grafana 与 Datadog、Splunk 和其他可观测性平台等对手竞争。

一个与众不同的因素是，当 Grafana 用于非商业用途时，它不会保留用户数据。至关重要的是，Grafana 的扩展不会损害性能。它保持着历史贡献，并确保与各种开源可观测性工具兼容，尤其是 Grafana 与 OpenTelemetry 的积极集成反映了这一点。此外，Grafana 仍然支持开源项目，特别值得注意的是 Prometheus，并继续推出新的项目，比如最近推出的 Grafana Beyla，这是一个 eBPF 自动 instrumentation 工具。

在不久的将来，Grafana Cloud 用户将能够从 Asserts 的使用中受益，Asserts 的目的是通过使用 AI 来帮助用户发现指标数据(或者如 Grafana 所描述的“上下文化指标数据”)。它专门扫描 Prometheus 指标中的标签，并自动发现应用程序及其基础设施组件以及它们之间的联系。

在本周在伦敦举行的 Grafana 每年一次的用户大会 [ObservabilityCon 2023](https://grafana.com/about/events/observabilitycon/2023/) 上，Asserts.ai 的创始人兼 CEO [Manoj Acharya](https://www.linkedin.com/in/manojacharya)(他是 AppDynamics 聘用的第五名工程师)展示了 Asserts 提供的功能。他展示了如何使用该工具扫描他运行的演示集群中的所有 Prometheus 指标，以构建服务图。“随着它了解新的服务、部件和节点，想象你正在运行一个 Kafka 集群；它也会获取有关新主题的信息，”Acharya 说。 此外，Asserts 正在设计与亚马逊集成，使其能够读取 CloudWatch 指标并访问动态表格、SQS 队列，从而形成一个图形，即数据的实体系统，他说。 “当考虑理解你的数据时，考虑一个 schema - 现在在属性图中构建的实体系统。这是幕后运行的东西，”Acharya 说。 “它目前已经发现了这个特定集群中的所有部分、节点和服务。”

## 可观测性和警报

考虑到仅有大约 20 个不同的指标用于测量各种内存消耗方面的指标时，这些功能的重要性就凸显出来了，[EMA](https://www.enterprisemanagement.com/) 分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk/) 说。 Asserts.ai 可以使用其依赖关系图自动评估哪些指标可能会影响特定应用程序以及它们需要多频繁的收集才能最佳地为机器学习模型提供数据。这会导致更快、更准确的预测，可能节省大量存储空间。 “总体而言，Asserts.ai 将 Grafana 从一个数据可视化平台提升到一个应用程序可观测性和警报系统，这对其现有和未来客户来说都是激动人心的消息，” Volk 说。

事实上，Asserts.ai 为 Grafana 提供了提供“智能”仪表板的能力，这些仪表板可以自动确定哪些指标对预测、优化和故障排除 Kubernetes 集群的性能和运行状况实际相关。 “这不是一项简单的任务，因为 Prometheus 提供了大量的指标，而不区分它们是否以及如何与特定应用程序相关。摄取、存储和分析所有这些指标可能会让平台团队被需要摄取、分析和存储的数据雪崩埋葬，”Volk 说。 “Asserts AI 使用应用程序和基础设施依赖关系的自动跟踪以及机器学习来找到影响应用程序运行状况和性能的指标，并在 Grafana 仪表板上绘制它们。由于 Asserts.ai 知道 Kubernetes 集群内的相互依赖关系，它可以自动检测即将发生的问题并发出显示整个问题链的警报，所有这些都指向根本原因。”

在 ObservabilityCon 上，Grafana 的高级软件工程师 [Yasir Ekinci](https://www.linkedin.com/in/yasirekinci/) 在问答环节中描述了 Asserts 如何融入 Grafana 面板体验。他与 Grafana 高级软件工程师 [Ben Sully](https://www.linkedin.com/in/ben-sully-51bb1591/?originalSubdomain=uk) 的演讲是关于 AI 和 ML 的作用以及 Grafana 如何利用生成式 AI。一个示例是这样的：“我的服务出了什么问题？” 不仅要识别你的服务；你还需要了解它们的组件和依赖关系。这对生成式 AI 来说可能不是特别相关，但对于 [Grafana Sift](https://grafana.com/blog/2023/09/14/announcing-sift-automated-system-checks-for-faster-incident-response-times-in-grafana-cloud/) 来说应该会“更有意思”。 这是因为“一旦你理解了服务，特别是它的入站和出站方向，你可以更快地找到根本原因。”

UberEats 竞争对手及 Grafana 客户 [Just Eat Takeaway](https://www.justeattakeaway.com/) 的高级技术经理 [Alex Murray](https://www.linkedin.com/in/alexmurray30/?originalSubdomain=uk) 表示，Grafana 收购 Asserts 应该有助于更好地解释他的团队经常必须处理的大量指标。该公司在全球运营，挑战在于以“有意义的方式”管理和监控大规模的可观测性数据，他说。 “我将遥测数据看作数据湖中的一种伪身份（pseudo-identity）。所以，你有一个遥测数据的数据湖，所以你可以切割和拼接那些数据，”Murray 在会议幕间表示。 “然而，你想要给你的业务上下文，并能够获得可视化并了解你最初没有计划的有关平台的信息。”

通过 Asserts，Just Eat 的运营团队将能够利用另一层可观测性来集成 Grafana 面板提供的各种选择，Murray 说。 “Asserts 和 Grafana 真正重要的地方在于将你的数据转化为机会，”他说。

此外，Grafana 不需要该组织将数据转移到 Grafana 的服务器也是一个很大的优势，Murray 说。

“你的数据在哪里并不重要。与其他可观测性供应商不同，你不必把所有数据都发送给 Grafana。对于 Grafana 来说，你的数据在哪里并不重要，”Murray 说。 他还补充说，他也很欣赏 Grafana 如何与其他数据源提供充分的兼容性。 “还有一些像 [Correlations](https://grafana.com/docs/grafana/latest/administration/correlations/) 这样更精细的功能，允许你从不同的可观测性平台链接指标。”
